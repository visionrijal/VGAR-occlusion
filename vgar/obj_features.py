"""A(p, z_v) for every placed object, from depth slices spanning that object's own depth range.

The global 32-depth grid (features.py) is ~12% apart in depth (about 18 cm at 1.5 m). Objects resting
on a surface cross the real surface within centimetres, so interpolating across that gap blurs exactly
the boundary we evaluate (room_0 RGB-D, objects, 3 px band AP: 0.857 with the global grid vs 0.940 with
16 per-object slices; 64 per-object slices give 0.941). Here each object gets 16 slices evenly spaced
over [min z_v - 5 mm, max z_v + 5 mm]; we also store the 4- and 8-slice subsets for the ablation.

Usage (splatloc env): python vgar/obj_features.py <scene> <cond>
Also writes A_obj_exact.npy: the exact value from one pass of the clip rasterizer (common.clip_opacity).
Output: $VGAR_WORK/features/<cond>/<scene>/A_obj_{K4,K8,K16,exact}.npy  [N_obj,H,W] float16 (0 outside silhouette)
"""
import json
import os
import sys
import time

import numpy as np
import torch

from common import ROOT, clip_opacity, clipped_opacity, load_model, make_camera, test_dataset, view_depth

K_DENSE = 16
SUBSETS = {4: [0, 5, 10, 15], 8: [0, 2, 4, 6, 9, 11, 13, 15], 16: list(range(16))}


def interp(sl, grid, zv):
    K = len(grid)
    i1 = np.clip(np.searchsorted(grid, zv, side="right"), 1, K - 1)
    i0 = i1 - 1
    a0 = np.take_along_axis(sl, i0[None], 0)[0]
    a1 = np.take_along_axis(sl, i1[None], 0)[0]
    w = np.clip((zv - grid[i0]) / (grid[i1] - grid[i0]), 0, 1)
    return a0 + w * (a1 - a0)


def main(scene, cond):
    d = os.path.join(ROOT, "features", cond, scene)
    if os.path.exists(os.path.join(d, "A_obj_exact.npy")) and os.environ.get("FORCE", "0") != "1":
        print(f"{scene}/{cond}: object features exist, skipping")
        return
    meta = json.load(open(os.path.join(d, "meta.json")))
    ob = np.load(os.path.join(ROOT, "objects", f"{scene}.npz"))
    zv_all, views = ob["zv_mm"], ob["view"]
    cfg, pc = load_model(f"configs/vgar/{scene}_{cond.split('_')[0]}.yaml", cond)  # rgbd_occ etc. reuse the base config
    ds = test_dataset(cfg)
    N, H, W = zv_all.shape
    out = {k: np.lib.format.open_memmap(os.path.join(d, f"A_obj_K{k}.npy"), "w+", np.float16, (N, H, W)) for k in SUBSETS}
    exact = np.lib.format.open_memmap(os.path.join(d, "A_obj_exact.npy"), "w+", np.float16, (N, H, W))
    t_exact = []
    t0, cur_view, cam, z = time.time(), None, None, None
    for j in range(N):
        if views[j] != cur_view:
            cur_view = int(views[j])
            cam, _, _ = make_camera(ds, cur_view)
            z = view_depth(cam, pc.get_xyz)
        zv = zv_all[j].astype(np.float32) / 1000
        sil = zv > 0
        grid = np.linspace(zv[sil].min() - 0.005, zv[sil].max() + 0.005, K_DENSE)
        sl = torch.stack([clipped_opacity(cam, pc, float(t), z) for t in grid]).cpu().numpy()
        for k, idx in SUBSETS.items():
            out[k][j] = np.where(sil, interp(sl[idx], grid[idx], np.where(sil, zv, grid[0])), 0).astype(np.float16)
        # exact A(p, z_v(p)) in one pass with the clip rasterizer (clip 0 outside the silhouette -> A = 0)
        torch.cuda.synchronize(); t1 = time.perf_counter()
        a = clip_opacity(cam, pc, zv, z)
        torch.cuda.synchronize(); t_exact.append(time.perf_counter() - t1)
        exact[j] = a.half().cpu().numpy()
    for a in list(out.values()) + [exact]:
        a.flush()
    meta["obj_features"] = dict(K_dense=K_DENSE, subsets=list(SUBSETS), n_objects=int(N),
                                ms_exact_pass=round(1000 * float(np.median(t_exact)), 3),
                                seconds=round(time.time() - t0, 1))
    json.dump(meta, open(os.path.join(d, "meta.json"), "w"), indent=1)
    print(f"{scene}/{cond}: {N} objects x {K_DENSE} slices in {time.time() - t0:.0f} s -> {d}/A_obj_K*.npy")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
