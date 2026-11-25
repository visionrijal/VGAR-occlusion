"""G2: reconstruction sanity at Sequence_2 (novel-trajectory) poses: PSNR vs GT RGB,
rendered expected depth vs GT depth (catches pose/convention bugs), coverage."""
import json
import os
import sys

import numpy as np
import torch

from common import ROOT, load_model, make_camera, ray_stats, render_rgb, test_dataset

cfg_path = sys.argv[1] if len(sys.argv) > 1 else "configs/vgar/room_0_rgbd.yaml"
condition = sys.argv[2] if len(sys.argv) > 2 else "rgbd"
cfg, pc = load_model(cfg_path, condition)
ds = test_dataset(cfg)
scene = os.path.basename(cfg["Dataset"]["dataset_path"])

rows = []
for idx in range(0, ds.num_imgs, 10):
    cam, gt_rgb, gt_d = make_camera(ds, idx)
    rgb, _, _ = render_rgb(cam, pc)
    st = ray_stats(cam, pc)
    valid = gt_d > 0.01
    mse = ((rgb.clamp(0, 1) - gt_rgb) ** 2).mean().item()
    err = (st["D"] - gt_d).abs()[valid & (st["A"] > 0.5)]
    rows.append(dict(
        idx=idx, psnr=-10 * np.log10(mse),
        depth_med_cm=100 * err.median().item(),
        depth_mean_cm=100 * err.mean().item(),
        within_2cm=(err < 0.02).float().mean().item(),
        within_5cm=(err < 0.05).float().mean().item(),
        low_coverage=(st["A"] < 0.5)[valid].float().mean().item(),
    ))
    if idx == 0:  # save a visual check
        import cv2
        out = os.path.join(ROOT, "outputs", "checks"); os.makedirs(out, exist_ok=True)
        vis = lambda d: cv2.applyColorMap((np.clip(d / 6.0, 0, 1) * 255).astype(np.uint8), cv2.COLORMAP_JET)
        top = np.concatenate([(gt_rgb.permute(1, 2, 0).cpu().numpy()[..., ::-1] * 255),
                              (rgb.clamp(0, 1).permute(1, 2, 0).cpu().numpy()[..., ::-1] * 255)], 1)
        bot = np.concatenate([vis(gt_d.cpu().numpy()), vis(st["D"].cpu().numpy())], 1)
        cv2.imwrite(os.path.join(out, f"{scene}_{condition}_view0.png"), np.concatenate([top, bot], 0).astype(np.uint8))

agg = {k: float(np.mean([r[k] for r in rows])) for k in rows[0] if k != "idx"}
print(json.dumps({"scene": scene, "condition": condition, "n_views": len(rows), **{k: round(v, 4) for k, v in agg.items()}}, indent=1))
worst = sorted(rows, key=lambda r: -r["depth_med_cm"])[:3]
print("worst views:", [(r["idx"], round(r["depth_med_cm"], 2)) for r in worst])
json.dump(dict(agg=agg, rows=rows), open(os.path.join(ROOT, "outputs", "checks", f"{scene}_{condition}_geometry.json"), "w"), indent=1)
