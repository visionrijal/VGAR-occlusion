"""Pilot for the learned component with spatial context: a tiny U-Net over per-pixel ray-feature
maps + rendered RGB, plane protocol, first-half/second-half split of Sequence_2 (pilot only).
Baselines are recomputed on exactly the same pixels for an apples-to-apples comparison."""
import json
import os
import sys

import cv2
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import average_precision_score

from common import ROOT, clipped_opacity, load_model, make_camera, ray_stats, render_rgb, test_dataset

cfg_path, condition = sys.argv[1], sys.argv[2]
PLANES, TAU, BAND = [1.0, 1.5, 2.0, 3.0], 0.01, 3
torch.manual_seed(0); np.random.seed(0)
cfg, pc = load_model(cfg_path, condition)
ds = test_dataset(cfg)
scene = os.path.basename(cfg["Dataset"]["dataset_path"])
views = list(range(0, ds.num_imgs, 10)); half = len(views) // 2

Xs, Ys, Ms, Bs, split = [], [], [], [], []
for vi, idx in enumerate(views):
    cam, _, gt_d = make_camera(ds, idx)
    st = ray_stats(cam, pc)
    rgb = render_rgb(cam, pc)[0].clamp(0, 1)
    D = torch.where(st["A"] > 1e-3, st["D"], torch.full_like(st["D"], 10.0)).clamp(max=10)
    gtd = gt_d.cpu().numpy()
    for zv in PLANES:
        A = clipped_opacity(cam, pc, zv, st["z"])
        margin = (zv - D).clamp(-2, 2)
        f = torch.stack([A, st["A"], margin, (margin / (st["sigma"] + 1e-3)).clamp(-20, 20) / 10,
                         st["sigma"].clamp(max=2), torch.full_like(A, zv / 3)], 0)
        Xs.append(torch.cat([f, rgb], 0).half().cpu())
        occ = gtd < zv - TAU
        valid = (gtd > 0.01) & (np.abs(gtd - zv) >= TAU)
        edge = cv2.morphologyEx(occ.astype(np.uint8), cv2.MORPH_GRADIENT, np.ones((3, 3), np.uint8))
        band = cv2.dilate(edge, np.ones((2 * BAND + 1,) * 2, np.uint8)).astype(bool)
        Ys.append(torch.from_numpy(occ)); Ms.append(torch.from_numpy(valid)); Bs.append(torch.from_numpy(band))
        split.append(vi < half)
X, Y, M, Bd = torch.stack(Xs), torch.stack(Ys).float(), torch.stack(Ms), torch.stack(Bs)
tr = torch.tensor(split); te = ~tr


class TinyUNet(nn.Module):
    def __init__(self, cin=9, c=32):
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


net = TinyUNet().cuda()
opt = torch.optim.Adam(net.parameters(), 1e-3)
Xtr, Ytr, Mtr, Btr = X[tr], Y[tr], M[tr], Bd[tr]
n = Xtr.shape[0]
for it in range(1500):
    i = torch.randint(0, n, (8,))
    y0, x0 = np.random.randint(0, 480 - 256), np.random.randint(0, 640 - 256)
    sl = (slice(None), slice(y0, y0 + 256), slice(x0, x0 + 256))
    x = Xtr[i][(slice(None),) + sl].float().cuda()
    y, m, b = Ytr[i][sl].cuda(), Mtr[i][sl].cuda().float(), Btr[i][sl].cuda().float()
    if np.random.rand() < 0.5:
        x, y, m, b = x.flip(-1), y.flip(-1), m.flip(-1), b.flip(-1)
    w = m * (1 + 4 * b)  # emphasise the boundary band
    loss = (F.binary_cross_entropy_with_logits(net(x), y, reduction="none") * w).sum() / w.sum()
    opt.zero_grad(); loss.backward(); opt.step()
net.eval()
nparams = sum(p.numel() for p in net.parameters())

with torch.no_grad():
    P = torch.cat([torch.sigmoid(net(X[te][k:k + 4].float().cuda())).cpu() for k in range(0, int(te.sum()), 4)])
Xte, Yte, Mte, Bte = X[te].float(), Y[te].bool(), M[te], Bd[te]
scores = {"B0 expected-depth": Xte[:, 2], "B2 soft opacity": Xte[:, 0], "CNN (ray feats + RGB)": P}
res = {}
for name, s in scores.items():
    r = {}
    for region, msk in [("all", Mte), ("band", Mte & Bte)]:
        r[region] = round(average_precision_score(Yte[msk].numpy(), s[msk].numpy()), 4)
    res[name] = r
    print(f"{scene}/{condition} {name:24s} AP all {r['all']}  band {r['band']}")
print(f"U-Net params: {nparams:,}")
json.dump(res, open(os.path.join(ROOT, "outputs", "checks", f"{scene}_{condition}_cnn_pilot.json"), "w"), indent=1)
