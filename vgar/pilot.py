"""G4 (headroom) + G5 (pilot signal) on one scene with the depth-plane protocol.

For each Sequence_2 test view and each fronto-parallel virtual plane at depth z_v:
  GT label    occluded(p) = D_gt(p) < z_v - tau   (pixels with |D_gt - z_v| < tau are ignored)
  B0          expected-depth test:  score = z_v - D(p)          (hard: score > 0)
  B1          median-depth test  == A(p, z_v) >= 0.5
  B2          soft depth-clipped opacity A(p, z_v)
  L-pilot     logistic regression / MLP on per-pixel ray features
Learned models train on the first half of the trajectory and are tested on the second half
(pilot split only; the real protocol is leave-one-scene-out).
"""
import json
import os
import sys

import cv2
import numpy as np
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, f1_score
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from common import ROOT, clipped_opacity, load_model, make_camera, ray_stats, test_dataset

cfg_path = sys.argv[1] if len(sys.argv) > 1 else "configs/vgar/room_0_rgbd.yaml"
condition = sys.argv[2] if len(sys.argv) > 2 else "rgbd"
PLANES = [1.0, 1.5, 2.0, 3.0]
TAU = 0.01
BAND = 3  # px half-width of the boundary band
rng = np.random.default_rng(0)

cfg, pc = load_model(cfg_path, condition)
ds = test_dataset(cfg)
scene = os.path.basename(cfg["Dataset"]["dataset_path"])
views = list(range(0, ds.num_imgs, 10))
half = len(views) // 2

FEATS = ["A_zv", "A_tot", "margin", "margin_over_sigma", "sigma", "z_v", "gradD"]
store = {k: [] for k in ["train", "test"]}

for vi, idx in enumerate(views):
    cam, _, gt_d = make_camera(ds, idx)
    st = ray_stats(cam, pc)
    A_tot, D, sig = st["A"], st["D"], st["sigma"]
    D = torch.where(A_tot > 1e-3, D, torch.full_like(D, 1e3))  # no geometry -> nothing in front
    Dn = D.cpu().numpy()
    gradD = np.hypot(cv2.Sobel(np.minimum(Dn, 10), cv2.CV_32F, 1, 0), cv2.Sobel(np.minimum(Dn, 10), cv2.CV_32F, 0, 1))
    gtd = gt_d.cpu().numpy()
    for zv in PLANES:
        A_zv = clipped_opacity(cam, pc, zv, st["z"]).cpu().numpy()
        occ = gtd < zv - TAU
        valid = (gtd > 0.01) & (np.abs(gtd - zv) >= TAU)
        edge = cv2.morphologyEx(occ.astype(np.uint8), cv2.MORPH_GRADIENT, np.ones((3, 3), np.uint8))
        band = cv2.dilate(edge, np.ones((2 * BAND + 1, 2 * BAND + 1), np.uint8)).astype(bool)
        f = np.stack([A_zv, A_tot.cpu().numpy(), zv - Dn, (zv - Dn) / (sig.cpu().numpy() + 1e-3),
                      sig.cpu().numpy(), np.full_like(Dn, zv), gradD], -1)
        m = valid.ravel()
        rec = dict(X=f.reshape(-1, len(FEATS))[m].astype(np.float32), y=occ.ravel()[m], band=band.ravel()[m])
        # subsample non-band pixels to keep memory sane; keep every band pixel
        keep = rec["band"] | (rng.random(rec["y"].shape[0]) < 0.05)
        sub = {k: v[keep] for k, v in rec.items()}
        sub["w"] = np.where(sub["band"], 1.0, 20.0)  # undo the 5% subsampling of non-band pixels
        store["train" if vi < half else "test"].append(sub)

cat = lambda split, k: np.concatenate([r[k] for r in store[split]])
Xtr, ytr = cat("train", "X"), cat("train", "y")
Xte, yte, bte, wte = cat("test", "X"), cat("test", "y"), cat("test", "band"), cat("test", "w")
Xtr = np.nan_to_num(np.clip(Xtr, -1e3, 1e3)); Xte = np.nan_to_num(np.clip(Xte, -1e3, 1e3))
print(f"{scene}/{condition}: test pixels {len(yte):,} (band {bte.sum():,}), occluded rate {np.average(yte, weights=wte):.3f}")

# training subsample, class-balanced-ish
sel = rng.choice(len(ytr), size=min(300_000, len(ytr)), replace=False)
lr = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000, class_weight="balanced")).fit(Xtr[sel], ytr[sel])
mlp = make_pipeline(StandardScaler(), MLPClassifier((64, 64), max_iter=60, early_stopping=True, random_state=0)).fit(Xtr[sel], ytr[sel])
# thresholds for learned models chosen on the training half (max F1)
def best_thr(p, y):
    ts = np.linspace(0.05, 0.95, 19)
    return ts[int(np.argmax([f1_score(y, p > t) for t in ts]))]
p_lr_tr, p_mlp_tr = lr.predict_proba(Xtr[sel])[:, 1], mlp.predict_proba(Xtr[sel])[:, 1]
t_lr, t_mlp = best_thr(p_lr_tr, ytr[sel]), best_thr(p_mlp_tr, ytr[sel])

methods = {
    "B0 expected-depth": (Xte[:, 2], 0.0),
    "B1 median (A>=0.5)": (Xte[:, 0], 0.5),
    "B2 soft opacity": (Xte[:, 0], 0.5),
    "L logistic": (lr.predict_proba(Xte)[:, 1], t_lr),
    "L MLP": (mlp.predict_proba(Xte)[:, 1], t_mlp),
}
res = {}
for name, (s, t) in methods.items():
    hard = s > t if not name.startswith("B1") else s >= t
    r = {}
    for region, msk in [("all", np.ones_like(bte)), ("band", bte)]:
        y, w, sc, h = yte[msk], wte[msk], s[msk], hard[msk]
        r[region] = dict(
            AP=None if name.startswith("B1") else round(average_precision_score(y, sc, sample_weight=w), 4),
            F1=round(f1_score(y, h, sample_weight=w), 4),
            false_occl=round(float(np.average(h[~y], weights=w[~y])), 4),   # virtual hidden but should be visible
            missed_occl=round(float(np.average(~h[y], weights=w[y])), 4),   # virtual drawn over a real occluder
        )
    res[name] = r
    print(f"{name:20s} | all: AP {r['all']['AP']}  F1 {r['all']['F1']}  FO {r['all']['false_occl']}  MO {r['all']['missed_occl']}"
          f" | band: AP {r['band']['AP']}  F1 {r['band']['F1']}  FO {r['band']['false_occl']}  MO {r['band']['missed_occl']}")
print("LR coefficients (standardized):", dict(zip(FEATS, np.round(lr[-1].coef_[0], 2))))
out = os.path.join(ROOT, "outputs", "checks", f"{scene}_{condition}_pilot.json")
json.dump(res, open(out, "w"), indent=1)
print("saved", out)
