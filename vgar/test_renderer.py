"""G3: unit tests for depth-clipped opacity on the stock 4-channel rasterizer."""
import sys
import time

import torch

from common import clipped_opacity, make_camera, load_model, ray_stats, render_aux, test_dataset, view_depth

cfg_path = sys.argv[1] if len(sys.argv) > 1 else "configs/vgar/room_0_rgbd.yaml"
cfg, pc = load_model(cfg_path)
ds = test_dataset(cfg)
print(f"Gaussians: {pc.get_xyz.shape[0]:,}")
ok = True

for idx in [0, 300, 600]:
    cam, _, _ = make_camera(ds, idx)
    z = view_depth(cam, pc.get_xyz)
    st = ray_stats(cam, pc)

    # T1: override channel 0 (colour 1) must equal the native alpha output; channel 1 (colour z) the native depth
    t1a = (st["img"][0] - st["alpha_native"]).abs().max().item()
    t1b = (st["img"][1] - st["depth_native"]).abs().max().item()

    # T2: all-true mask must equal the unmasked render
    c4 = torch.zeros(z.shape[0], 4, device="cuda")
    _, _, a_full = render_aux(cam, pc, c4)
    _, _, a_mask = render_aux(cam, pc, c4, mask=torch.ones_like(z, dtype=torch.bool))
    t2 = (a_full - a_mask).abs().max().item()

    # T3: masked render (only z_i < zk) == full render with indicator colour [z_i < zk]
    #     -> holds only if compositing is front-to-back in centre-depth order (the slicing assumption)
    t3 = 0.0
    zs = [1.0, 1.5, 2.0, 3.0]
    prev = None
    mono = True
    for zk in zs:
        a_k = clipped_opacity(cam, pc, zk, z)
        ind = torch.zeros(z.shape[0], 4, device="cuda")
        ind[:, 0] = (z < zk).float()
        img, _, _ = render_aux(cam, pc, ind)
        t3 = max(t3, (a_k - img[0]).abs().max().item())
        # T4: monotone non-decreasing in zk
        if prev is not None and (a_k - prev).min().item() < -1e-5:
            mono = False
        prev = a_k
    print(f"view {idx:3d}: T1 alpha {t1a:.2e} depth {t1b:.2e} | T2 mask {t2:.2e} | T3 slice-vs-indicator {t3:.2e} | T4 monotone {mono}")
    ok &= t1a < 1e-4 and t1b < 1e-3 and t2 < 1e-5 and t3 < 1e-3 and mono

# T5: timing of one slice pass
cam, _, _ = make_camera(ds, 0)
z = view_depth(cam, pc.get_xyz)
torch.cuda.synchronize(); t = time.time()
for _ in range(20):
    clipped_opacity(cam, pc, 2.0, z)
torch.cuda.synchronize()
print(f"T5: one depth-slice pass = {(time.time() - t) / 20 * 1000:.1f} ms at 640x480")
print("G3", "PASS" if ok else "FAIL")
