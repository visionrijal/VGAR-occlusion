"""Predict metric depth with Depth Anything V2 (metric indoor / Hypersim, ViT-S) for the
Sequence_1 training frames SplatLoc uses (every 5th), saved as <name>.npy in metres.
Run in the `dav2` env:  python mono_depth.py room_0 [room_1 ...]"""
import glob
import os
import sys

import cv2
import numpy as np
import torch

ROOT = os.environ.get("VGAR_WORK", "/home/regex/Documents/VGAR")
DAV2 = os.path.join(os.environ.get("DAV2_DIR", os.path.join(ROOT, "code", "Depth-Anything-V2")), "metric_depth")
CKPT_DIR = os.environ.get("VGAR_CKPT", os.path.join(ROOT, "code", "checkpoints"))
sys.path.insert(0, DAV2)
from depth_anything_v2.dpt import DepthAnythingV2  # noqa: E402

model = DepthAnythingV2(encoder="vits", features=64, out_channels=[48, 96, 192, 384], max_depth=20)
model.load_state_dict(torch.load(os.path.join(CKPT_DIR, "depth_anything_v2_metric_hypersim_vits.pth"), map_location="cpu"))
model = model.cuda().eval()

for scene in sys.argv[1:]:
    paths = sorted(glob.glob(f"{ROOT}/data/replica/{scene}/Sequence_1/rgb/*.png"),
                   key=lambda x: int(os.path.basename(x)[4:-4]))[::5]
    out = f"{ROOT}/data/mono_depth/{scene}"
    os.makedirs(out, exist_ok=True)
    if len(glob.glob(os.path.join(out, "*.npy"))) == len(paths):
        print(f"{scene}: {len(paths)} depth maps already present, skipping")
        continue
    errs = []
    for p in paths:
        # Metric models assume their training intrinsics (Hypersim: 60 deg HFOV, fx/W = 0.866).
        # Rescale by the known focal ratio to Replica's camera (fx/W = 320/640): no GT involved.
        FOCAL_RATIO = (320.0 / 640.0) / (0.5 / np.tan(np.radians(30.0)))
        d = model.infer_image(cv2.imread(p), 518).astype(np.float32) * FOCAL_RATIO
        name = os.path.basename(p)[:-4]
        np.save(os.path.join(out, name + ".npy"), d)
        gt = cv2.imread(p.replace("/rgb/rgb_", "/depth/depth_"), cv2.IMREAD_UNCHANGED).astype(np.float32) / 1000.0
        v = gt > 0.01
        errs.append((np.median(np.abs(d[v] - gt[v])), np.median(d[v] / gt[v])))
    e = np.array(errs)
    print(f"{scene}: {len(paths)} frames | median |pred-gt| = {100 * e[:, 0].mean():.1f} cm | median scale pred/gt = {e[:, 1].mean():.3f}")
