"""Per-view ray features from one frozen 3DGS map, for every Sequence_2 test view (every 10th frame).

For each view we store everything any occlusion method needs, so that planes, objects and every
learned model read the same numbers:
  slices  [V,K,H,W] f16  A(p, z_k): opacity of Gaussians with centre depth < z_k, for a fixed grid z_k
  atot    [V,H,W]   f16  total accumulated opacity A_tot
  D       [V,H,W]   f16  expected depth sum(w z) / A_tot   (B0 uses z_v - D)
  sigma   [V,H,W]   f16  depth spread along the ray
  rgb     [V,3,H,W] u8   ordinary colour render of the map
  gt_mm   [V,H,W]   u16  ground-truth depth in mm (labels only)
The grid has 32 depths: 28 log-spaced in [0.3, 8] m plus the plane depths 1, 1.5, 2, 3 m, so plane
masks get A exactly; object masks interpolate between neighbouring slices (vgar/data.py).

Usage (splatloc env): python vgar/features.py <scene> <rgbd|mono|rgbonly>
Output: $VGAR_WORK/features/<cond>/<scene>/*.npy + meta.json
"""
import json
import os
import sys
import time

import numpy as np
import torch

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # before common.py changes the working dir
from common import ROOT, clipped_opacity, load_model, make_camera, ray_stats, render_rgb, test_dataset

PLANES = [1.0, 1.5, 2.0, 3.0]
Z_GRID = sorted(set(np.round(np.geomspace(0.3, 8.0, 28), 4).tolist()) | set(PLANES))


def main(scene, cond):
    out = os.path.join(ROOT, "features", cond, scene)
    if os.path.exists(os.path.join(out, "meta.json")) and os.environ.get("FORCE", "0") != "1":
        print(f"{scene}/{cond}: features exist, skipping")
        return
    os.makedirs(out, exist_ok=True)
    cfg, pc = load_model(f"configs/vgar/{scene}_{cond.split('_')[0]}.yaml", cond)  # rgbd_occ etc. reuse the base config
    ds = test_dataset(cfg)
    views = list(range(0, ds.num_imgs, 10))
    V, K, H, W = len(views), len(Z_GRID), ds.height, ds.width
    arr = {
        "slices": np.lib.format.open_memmap(os.path.join(out, "slices.npy"), "w+", np.float16, (V, K, H, W)),
        "atot": np.zeros((V, H, W), np.float16), "D": np.zeros((V, H, W), np.float16),
        "sigma": np.zeros((V, H, W), np.float16), "rgb": np.zeros((V, 3, H, W), np.uint8),
        "gt_mm": np.zeros((V, H, W), np.uint16),
    }
    t_stats, t_slices, quality = [], [], []
    for i, idx in enumerate(views):
        cam, gt_rgb, gt_d = make_camera(ds, idx)
        torch.cuda.synchronize(); t0 = time.perf_counter()
        st = ray_stats(cam, pc)
        torch.cuda.synchronize(); t1 = time.perf_counter()
        sl = torch.stack([clipped_opacity(cam, pc, z, st["z"]) for z in Z_GRID])
        torch.cuda.synchronize(); t2 = time.perf_counter()
        t_stats.append(t1 - t0); t_slices.append((t2 - t1) / K)
        arr["slices"][i] = sl.half().cpu().numpy()
        arr["atot"][i] = st["A"].half().cpu().numpy()
        arr["D"][i] = st["D"].clamp(max=60000).half().cpu().numpy()
        arr["sigma"][i] = st["sigma"].clamp(max=60000).half().cpu().numpy()
        rgb = render_rgb(cam, pc)[0].clamp(0, 1)
        arr["rgb"][i] = (rgb * 255).round().byte().cpu().numpy()
        # map quality at this novel-trajectory view (same definitions as the pilot's check_geometry.py)
        valid = gt_d > 0.01
        err = (st["D"] - gt_d).abs()[valid & (st["A"] > 0.5)]
        quality.append(dict(psnr=-10 * np.log10(((rgb - gt_rgb) ** 2).mean().item()),
                            depth_med_cm=100 * err.median().item(), within_5cm=(err < 0.05).float().mean().item(),
                            low_coverage=(st["A"] < 0.5)[valid].float().mean().item()))
        arr["gt_mm"][i] = (gt_d * 1000).round().clamp(0, 65535).cpu().numpy().astype(np.uint16)
    arr["slices"].flush()
    for k, a in arr.items():
        if k != "slices":
            np.save(os.path.join(out, f"{k}.npy"), a)
    meta = dict(scene=scene, cond=cond, views=views, z_grid=Z_GRID, planes=PLANES, H=H, W=W,
                n_gaussians=int(pc.get_xyz.shape[0]),
                ms_stats_pass=round(1000 * float(np.median(t_stats)), 3),
                ms_per_slice=round(1000 * float(np.median(t_slices)), 3),
                gpu=torch.cuda.get_device_name(),
                quality={k: round(float(np.mean([q[k] for q in quality])), 4) for k in quality[0]})
    json.dump(meta, open(os.path.join(out, "meta.json"), "w"), indent=1)
    qdir = os.path.join(REPO, "results", "maps", cond)
    os.makedirs(qdir, exist_ok=True)
    json.dump({k: meta[k] for k in ("scene", "cond", "n_gaussians", "ms_stats_pass", "ms_per_slice", "gpu", "quality")},
              open(os.path.join(qdir, f"{scene}.json"), "w"), indent=1)
    print(f"{scene}/{cond}: {V} views x {K} slices, {meta['n_gaussians']:,} Gaussians, "
          f"{meta['ms_stats_pass']} ms stats pass, {meta['ms_per_slice']} ms/slice on {meta['gpu']} | "
          f"PSNR {meta['quality']['psnr']:.2f} dB, depth error {meta['quality']['depth_med_cm']:.2f} cm -> {out}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
