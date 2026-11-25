"""Leave-one-scene-out training + evaluation of every occlusion method for one condition and test scene.

Methods (proposal §6):
  B0  expected-depth test, score z_v - D               B1  median-depth test, A(p,z_v) >= 0.5
  B2  depth-clipped opacity A(p,z_v), no training      LR  logistic regression on per-pixel features
  MLP per-pixel MLP on the same features               UNet tiny U-Net on feature maps (+ RGB)
Learned models train on the other 7 scenes; every threshold is chosen on held-out training views
(10% of training samples), never on the test scene.

Usage (splatloc env):
  python vgar/loso.py --cond rgbd --test room_0                       # main LOSO fold
  python vgar/loso.py --cond rgbd --test room_0 --feats depth_only --models unet --tag abl_depth_only
  python vgar/loso.py --cond rgbd --test room_0 --smoke               # one scene, first/second half of views
Output: <repo>/results/<tag>/<cond>/<test>.json
"""
import argparse
import json
import os
import time

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from data import FEATURE_SETS, PIXEL_FEATURES, SCENES, SceneData

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = argparse.ArgumentParser()
p.add_argument("--cond", required=True)
p.add_argument("--test", required=True)
p.add_argument("--models", default="lr,mlp,unet")
p.add_argument("--feats", default="all")
p.add_argument("--K", type=int, default=32)
p.add_argument("--iters", type=int, default=6000)
p.add_argument("--batch", type=int, default=16)
p.add_argument("--crop", type=int, default=256)
p.add_argument("--tag", default="main")
p.add_argument("--seed", type=int, default=0)
p.add_argument("--smoke", action="store_true")
p.add_argument("--preload", action="store_true")
args = p.parse_args()
models = [m for m in args.models.split(",") if m]
FEATS = FEATURE_SETS[args.feats]
rng = np.random.default_rng(args.seed)
torch.manual_seed(args.seed)
dev = "cuda"
t_start = time.time()

# ---------------------------------------------------------------- data
if args.smoke:
    sd = SceneData(args.cond, args.test, args.K, args.preload)
    half = len(sd.views) // 2
    train = [(sd, s) for s in sd.samples if s[1] < half]
    test_sd, test_samples = sd, [s for s in sd.samples if s[1] >= half]
    train_scenes = [args.test + "(first half)"]
else:
    train_scenes = [s for s in SCENES if s != args.test]
    sds = [SceneData(args.cond, s, args.K, args.preload) for s in train_scenes]
    train = [(sd, s) for sd in sds for s in sd.samples]
    test_sd = SceneData(args.cond, args.test, args.K, args.preload)
    test_samples = test_sd.samples
# hold out 10% of training *views* (per scene) for threshold selection
val_keys = {(sd.scene, vi) for sd in {id(x[0]): x[0] for x in train}.values()
            for vi in rng.choice(len(sd.views), max(1, len(sd.views) // 10), replace=False)}
val = [(sd, s) for sd, s in train if (sd.scene, s[1]) in val_keys]
fit = [(sd, s) for sd, s in train if (sd.scene, s[1]) not in val_keys]
print(f"{args.cond} test={args.test} train={train_scenes} | fit {len(fit)} val {len(val)} test {len(test_samples)} samples")


def stack(b, names):
    return np.stack([b["feats"][n] for n in names], 0)


def pixel_set(pairs, n_samples, per_sample, band_frac=0.5):
    """Per-pixel training/validation set: random valid pixels, half drawn from the boundary band."""
    X, Y = [], []
    for k in rng.choice(len(pairs), min(n_samples, len(pairs)), replace=False):
        sd, s = pairs[k]
        b = sd.build(s, band_px=(3,))
        for msk, n in [(b["band3"], int(per_sample * band_frac)), (b["valid"] & ~b["band3"], per_sample - int(per_sample * band_frac))]:
            idx = np.flatnonzero(msk)
            if len(idx):
                idx = rng.choice(idx, min(n, len(idx)), replace=False)
                X.append(stack(b, PIXEL_FEATURES).reshape(len(PIXEL_FEATURES), -1)[:, idx].T)
                Y.append(b["y"].ravel()[idx])
    return np.concatenate(X).astype(np.float32), np.concatenate(Y)


# ---------------------------------------------------------------- models
class TinyUNet(nn.Module):
    def __init__(self, cin, c=32):
        super().__init__()
        blk = lambda i, o: nn.Sequential(nn.Conv2d(i, o, 3, padding=1), nn.ReLU(), nn.Conv2d(o, o, 3, padding=1), nn.ReLU())
        self.e1, self.e2, self.e3 = blk(cin, c), blk(c, 2 * c), blk(2 * c, 4 * c)
        self.d2, self.d1 = blk(6 * c, 2 * c), blk(3 * c, c)
        self.out = nn.Conv2d(c, 1, 1)

    def forward(self, x):
        e1 = self.e1(x); e2 = self.e2(F.max_pool2d(e1, 2)); e3 = self.e3(F.max_pool2d(e2, 2))
        d2 = self.d2(torch.cat([F.interpolate(e3, scale_factor=2), e2], 1))
        d1 = self.d1(torch.cat([F.interpolate(d2, scale_factor=2), e1], 1))
        return self.out(d1)[:, 0]


class CropStream(torch.utils.data.IterableDataset):
    def __init__(self, pairs, seed):
        self.pairs, self.seed = pairs, seed

    def __iter__(self):
        wi = torch.utils.data.get_worker_info()
        r = np.random.default_rng(self.seed + (wi.id if wi else 0))
        c = args.crop
        while True:
            sd, s = self.pairs[r.integers(len(self.pairs))]
            if s[0] == "object":
                ys, xs = sd.object_crop(s[2], c, r)
            else:
                y0, x0 = r.integers(0, sd.H - c + 1), r.integers(0, sd.W - c + 1)
                ys, xs = slice(y0, y0 + c), slice(x0, x0 + c)
            b = sd.build(s, ys, xs, band_px=(3,))
            x = stack(b, FEATS)
            y, m, bd = b["y"], b["valid"], b["band3"]
            if r.random() < 0.5:
                x, y, m, bd = x[..., ::-1], y[:, ::-1], m[:, ::-1], bd[:, ::-1]
            yield (torch.from_numpy(np.ascontiguousarray(x)), torch.from_numpy(np.ascontiguousarray(y)).float(),
                   torch.from_numpy(np.ascontiguousarray(m)).float(), torch.from_numpy(np.ascontiguousarray(bd)).float())


trained, info = {}, {}
if "lr" in models or "mlp" in models:
    Xf, Yf = pixel_set(fit, 3000, 200)
    print(f"per-pixel training set: {len(Yf):,} pixels, occluded rate {Yf.mean():.3f}")
    if "lr" in models:
        trained["LR"] = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000)).fit(Xf, Yf)
        info["LR_coef"] = dict(zip(PIXEL_FEATURES, np.round(trained["LR"][-1].coef_[0], 3).tolist()))
    if "mlp" in models:
        trained["MLP"] = make_pipeline(StandardScaler(), MLPClassifier((64, 64), max_iter=100, early_stopping=True,
                                                                     random_state=args.seed)).fit(Xf, Yf)
if "unet" in models:
    net = TinyUNet(len(FEATS)).to(dev)
    info["unet_params"] = sum(p.numel() for p in net.parameters())
    opt = torch.optim.Adam(net.parameters(), 1e-3)
    sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, args.iters)
    loader = torch.utils.data.DataLoader(CropStream(fit, args.seed), batch_size=args.batch,
                                         num_workers=int(os.environ.get("SLURM_CPUS_PER_TASK", 4)) - 1)
    t0 = time.time()
    for it, (x, y, m, bd) in enumerate(loader):
        if it == args.iters:
            break
        x, y, m, bd = x.to(dev), y.to(dev), m.to(dev), bd.to(dev)
        w = m * (1 + 4 * bd)  # emphasise the boundary band (proposal §4)
        loss = (F.binary_cross_entropy_with_logits(net(x), y, reduction="none") * w).sum() / w.sum().clamp_min(1)
        opt.zero_grad(); loss.backward(); opt.step(); sched.step()
        if it % 500 == 0:
            print(f"  unet it {it:5d}  loss {loss.item():.4f}  {time.time() - t0:.0f}s", flush=True)
    info["unet_train_min"] = round((time.time() - t0) / 60, 2)
    net.eval()
    trained["UNet"] = net


# ---------------------------------------------------------------- scoring
@torch.no_grad()
def scores_for(sd, s):
    b = sd.build(s)
    out = {"B0": b["score_b0"], "B2": b["feats"]["A_zv"]}
    if "LR" in trained or "MLP" in trained:
        Xp = stack(b, PIXEL_FEATURES).reshape(len(PIXEL_FEATURES), -1).T
        for k in ("LR", "MLP"):
            if k in trained:
                out[k] = trained[k].predict_proba(Xp)[:, 1].reshape(sd.H, sd.W).astype(np.float32)
    if "UNet" in trained:
        x = torch.from_numpy(stack(b, FEATS)[None]).to(dev)
        out["UNet"] = torch.sigmoid(trained["UNet"](x))[0].cpu().numpy()
    return b, out


def best_threshold(sc, y):
    """Threshold maximizing F1 over the score's own quantiles."""
    qs = np.unique(np.quantile(sc, np.linspace(0.01, 0.99, 197)))
    best, bt = -1, qs[0]
    P = y.sum()
    for t in qs:
        h = sc > t
        tp = (h & y).sum()
        f1 = 2 * tp / max(h.sum() + P, 1)
        if f1 > best:
            best, bt = f1, t
    return float(bt)


METHODS = ["B0", "B2"] + [m for m in ("LR", "MLP", "UNet") if m in trained]
# thresholds on held-out training views
vs = {m: [] for m in METHODS}; vy = []
for k in rng.choice(len(val), min(400, len(val)), replace=False):
    b, sc = scores_for(*val[k])
    v = b["valid"] & (b["band3"] | (rng.random(b["valid"].shape) < 0.05))  # band pixels + 5% of the rest
    vy.append(b["y"][v])
    for m in METHODS:
        vs[m].append(sc[m][v])
vy = np.concatenate(vy)
thr = {m: best_threshold(np.concatenate(vs[m]), vy) for m in METHODS}
thr["B1"] = 0.5
print("thresholds (chosen on held-out training views):", {k: round(v, 4) for k, v in thr.items()})

# test scene: keep every band-5 pixel and 2% of the rest (weight 50) to bound memory
KEEP_REST = 0.02
cols = {m: [] for m in METHODS}
meta_cols = {k: [] for k in ["y", "w", "band3", "band5", "is_obj", "view"]}
t_unet = []
for s in test_samples:
    b, sc = scores_for(test_sd, s)
    v = b["valid"]
    keep = v & (b["band5"] | (rng.random(v.shape) < KEEP_REST))
    meta_cols["y"].append(b["y"][keep]); meta_cols["w"].append(np.where(b["band5"][keep], 1.0, 1 / KEEP_REST))
    meta_cols["band3"].append(b["band3"][keep]); meta_cols["band5"].append(b["band5"][keep])
    meta_cols["is_obj"].append(np.full(keep.sum(), s[0] == "object")); meta_cols["view"].append(np.full(keep.sum(), s[1]))
    for m in METHODS:
        cols[m].append(sc[m][keep].astype(np.float32))
cat = {k: np.concatenate(v) for k, v in {**cols, **meta_cols}.items()}
if "UNet" in trained:  # runtime of one full-frame forward pass
    x = torch.zeros(1, len(FEATS), test_sd.H, test_sd.W, device=dev)
    for i in range(30):
        torch.cuda.synchronize(); t0 = time.perf_counter(); trained["UNet"](x); torch.cuda.synchronize()
        if i >= 10:
            t_unet.append(time.perf_counter() - t0)
    info["unet_ms_per_frame"] = round(1000 * float(np.median(t_unet)), 3)


def metrics(sc, y, w, t, prob):
    h = sc >= t if t == 0.5 and prob == "B1" else sc > t
    tp, fp, fn = (w * (h & y)).sum(), (w * (h & ~y)).sum(), (w * (~h & y)).sum()
    r = dict(F1=2 * tp / max(2 * tp + fp + fn, 1e-9), IoU=tp / max(tp + fp + fn, 1e-9),
             missed_occ=fn / max((w * y).sum(), 1e-9),          # virtual drawn over a real occluder
             false_occ=fp / max((w * ~y).sum(), 1e-9))          # virtual hidden although visible
    return {k: round(float(v), 4) for k, v in r.items()}


def calib(pr, y, w, bins=15):
    pr = np.clip(pr, 0, 1)
    brier = float(np.average((pr - y) ** 2, weights=w))
    e, idx = 0.0, np.minimum((pr * bins).astype(int), bins - 1)
    for k in range(bins):
        m = idx == k
        if m.any():
            e += w[m].sum() * abs(np.average(y[m], weights=w[m]) - np.average(pr[m], weights=w[m]))
    return dict(brier=round(brier, 4), ece=round(float(e / w.sum()), 4))


res = dict(cond=args.cond, test=args.test, train=train_scenes, tag=args.tag, feats=args.feats, K=args.K,
           models=models, thresholds={k: round(v, 5) for k, v in thr.items()}, info=info,
           n_test_samples=len(test_samples), n_planes=sum(s[0] == "plane" for s in test_samples),
           n_objects=sum(s[0] == "object" for s in test_samples),
           feature_ms=dict(stats_pass=test_sd.meta["ms_stats_pass"], per_slice=test_sd.meta["ms_per_slice"],
                           gpu=test_sd.meta["gpu"]), results={}, per_view_band3_AP={})
y, w = cat["y"].astype(bool), cat["w"]
for subset, sm in [("all", np.ones_like(y)), ("planes", ~cat["is_obj"]), ("objects", cat["is_obj"])]:
    for region, rm in [("all", np.ones_like(y)), ("band3", cat["band3"]), ("band5", cat["band5"])]:
        msk = sm & rm
        if msk.sum() == 0 or y[msk].all() or (~y[msk]).all():
            continue
        for m in METHODS + ["B1"]:
            sc = cat["B2"] if m == "B1" else cat[m]
            r = {} if m == "B1" else {"AP": round(float(average_precision_score(y[msk], sc[msk], sample_weight=w[msk])), 4)}
            r.update(metrics(sc[msk], y[msk], w[msk], thr[m], m))
            if m in ("B2", "LR", "MLP", "UNet") and region == "all":
                r.update(calib(sc[msk], y[msk].astype(np.float32), w[msk]))
            res["results"].setdefault(subset, {}).setdefault(region, {})[m] = r
# per-view band AP (unit for the paired Wilcoxon test across scenes)
for vi in np.unique(cat["view"]):
    msk = (cat["view"] == vi) & cat["band3"]
    if msk.sum() < 50 or y[msk].all() or (~y[msk]).all():
        continue
    res["per_view_band3_AP"][int(vi)] = {m: round(float(average_precision_score(y[msk], cat[m][msk], sample_weight=w[msk])), 4)
                                         for m in METHODS}
res["minutes"] = round((time.time() - t_start) / 60, 2)

out = os.path.join(REPO, "results", args.tag + ("_smoke" if args.smoke else ""), args.cond, f"{args.test}.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump(res, open(out, "w"), indent=1)
for subset in res["results"]:
    line = " | ".join(f"{m} {res['results'][subset]['band3'][m].get('AP', '-')}" for m in METHODS)
    print(f"[{subset:7s}] band3 AP: {line}")
print(f"saved {out} ({res['minutes']} min)")
