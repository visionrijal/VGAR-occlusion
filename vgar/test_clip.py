"""Check the one-pass clip rasterizer against depth-slice rendering, which it must reproduce exactly.
1. constant clip depth z  ==  slice at z                         (planes)
2. clip map with 6 depth levels in blocks  ==  slices composed per block   (arbitrary per-pixel depth)
3. timing: one clip pass vs one slice
Usage (splatloc env): python vgar/test_clip.py [scene] [cond]"""
import sys
import time

import numpy as np
import torch

from common import clip_opacity, clipped_opacity, load_model, make_camera, test_dataset, view_depth

scene = sys.argv[1] if len(sys.argv) > 1 else "room_0"
cond = sys.argv[2] if len(sys.argv) > 2 else "rgbd"
cfg, pc = load_model(f"configs/vgar/{scene}_{cond}.yaml", cond)
ds = test_dataset(cfg)
worst1, worst2, t_clip, t_slice = 0.0, 0.0, [], []
rng = np.random.default_rng(0)
for idx in range(0, ds.num_imgs, 100):
    cam, _, _ = make_camera(ds, idx)
    z = view_depth(cam, pc.get_xyz)
    H, W = int(cam.image_height), int(cam.image_width)
    for zc in [0.7, 1.0, 1.5, 2.0, 3.0, 5.0]:
        a = clip_opacity(cam, pc, torch.full((H, W), zc), z)
        b = clipped_opacity(cam, pc, zc, z)
        worst1 = max(worst1, (a - b).abs().max().item())
    levels = rng.uniform(0.5, 4.0, 6)
    lab = rng.integers(0, 6, (H // 40 + 1, W // 40 + 1)).repeat(40, 0).repeat(40, 1)[:H, :W]
    clip = torch.as_tensor(levels[lab], dtype=torch.float32, device="cuda")
    a = clip_opacity(cam, pc, clip, z)
    ref = torch.zeros(H, W, device="cuda")
    for k, zc in enumerate(levels):
        m = torch.as_tensor(lab == k, device="cuda")
        ref[m] = clipped_opacity(cam, pc, float(zc), z)[m]
    worst2 = max(worst2, (a - ref).abs().max().item())
    for _ in range(5):
        torch.cuda.synchronize(); t0 = time.perf_counter(); clip_opacity(cam, pc, clip, z); torch.cuda.synchronize()
        t_clip.append(time.perf_counter() - t0)
        torch.cuda.synchronize(); t0 = time.perf_counter(); clipped_opacity(cam, pc, 2.0, z); torch.cuda.synchronize()
        t_slice.append(time.perf_counter() - t0)
print(f"{scene}/{cond}: max |clip - slice| constant depth {worst1:.2e}, per-pixel blocks {worst2:.2e} "
      f"| clip pass {1000 * np.median(t_clip):.2f} ms, one slice {1000 * np.median(t_slice):.2f} ms on {torch.cuda.get_device_name()}")
print("PASS" if max(worst1, worst2) < 1e-5 else "FAIL")
