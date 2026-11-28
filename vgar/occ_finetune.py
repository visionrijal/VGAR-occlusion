"""Occlusion-aware fine-tuning of a trained 3DGS map (step 1 of the extension).

Goal: make the map's own depth-clipped opacity A(p, z) a sharp step at the true surface, so that the
training-free soft composite (B2) improves without any post-hoc network. Labels come only from the
TRAINING views (Sequence_1, every 5th frame): sensor depth for 'rgbd' maps, Depth Anything depth for
'mono' maps. Test views (Sequence_2) are never touched. RGB-only maps have no depth labels.

Per iteration, on one random training view:
  L = L1(rgb) + L1(depth)                                  (SplatLoc's mapping loss, keeps appearance)
    + lambda_occ * BCE(A_soft(p, z_k), [D_label(p) < z_k])  for 2 depths z_k drawn near the surface
A_soft uses a differentiable gate on each Gaussian's opacity, alpha_i * sigmoid((z_k - z_i) / tau_g),
rendered with the stock rasterizer, so gradients reach opacity, position, scale and rotation.
Pixels with |D_label - z_k| < 2 cm are ignored; pixels near the label's occlusion edge get weight 5.
lambda_occ = 0 is the control: the same extra training without the occlusion term.

Usage (splatloc env): python vgar/occ_finetune.py <scene> <rgbd|mono> [--lam 1.0] [--iters 3000] [--tag occ]
Output: $VGAR_WORK/outputs/<cond>_<tag>/replica/<scene>/point_cloud/final/point_cloud.ply (+ log json)
"""
import argparse
import json
import math
import os
import time

import cv2
import numpy as np
import torch
import torch.nn.functional as F

from common import ROOT, load_model, make_camera, view_depth

p = argparse.ArgumentParser()
p.add_argument("scene")
p.add_argument("cond", choices=["rgbd", "mono"])
p.add_argument("--lam", type=float, default=1.0)
p.add_argument("--iters", type=int, default=3000)
p.add_argument("--tau_g", type=float, default=0.01, help="gate width (m)")
p.add_argument("--tag", default=None)
p.add_argument("--seed", type=int, default=0)
args = p.parse_args()
tag = args.tag or ("occ" if args.lam > 0 else "ctl")
torch.manual_seed(args.seed)
rng = np.random.default_rng(args.seed)

from diff_gauss import GaussianRasterizationSettings, GaussianRasterizer  # noqa: E402
from gaussian_splatting.utils.sh_utils import eval_sh  # noqa: E402
from utils.dataset import load_dataset  # noqa: E402

cfg, pc = load_model(f"configs/vgar/{args.scene}_{args.cond}.yaml", args.cond)
train_ds = load_dataset(cfg, train=True)
n_train = len(train_ds.color_paths)
mono_dir = cfg["Dataset"].get("mono_depth_folder")


def label_depth(i, sensor):
    if args.cond == "mono":
        name = os.path.basename(train_ds.color_paths[i])[:-4]
        return torch.from_numpy(np.load(os.path.join(mono_dir, name + ".npy")).astype(np.float32)).cuda()
    return sensor


def render(cam, colors4, opac):
    s = GaussianRasterizationSettings(
        image_height=int(cam.image_height), image_width=int(cam.image_width),
        tanfovx=math.tan(cam.FoVx * 0.5), tanfovy=math.tan(cam.FoVy * 0.5),
        bg=torch.zeros(4, device="cuda"), scale_modifier=1.0,
        viewmatrix=cam.world_view_transform, projmatrix=cam.full_proj_transform,
        sh_degree=pc.active_sh_degree, campos=cam.camera_center, prefiltered=False, debug=False)
    z = view_depth(cam, pc.get_xyz)
    m = (z > 0.2).detach()  # near-plane cull, as in common.render_aux
    sc = pc.get_scaling
    if sc.shape[-1] == 1:
        sc = sc.repeat(1, 3)
    xyz = pc.get_xyz[m]
    img, depth, alpha, _ = GaussianRasterizer(raster_settings=s)(
        means3D=xyz, means2D=torch.zeros_like(xyz, requires_grad=True), opacities=opac[m],
        colors_precomp=colors4[m].contiguous(), scales=sc[m], rotations=pc.get_rotation[m])
    return img, depth[0], alpha[0], z


params = [
    {"params": [pc._xyz], "lr": 1.6e-5, "name": "xyz"},
    {"params": [pc._features_dc], "lr": 2.5e-3, "name": "f_dc"},
    {"params": [pc._features_rest], "lr": 1.25e-4, "name": "f_rest"},
    {"params": [pc._opacity], "lr": 0.01, "name": "opacity"},
    {"params": [pc._scaling], "lr": 1e-3, "name": "scaling"},
    {"params": [pc._rotation], "lr": 1e-3, "name": "rotation"},
]
opt = torch.optim.Adam(params, lr=0.0, eps=1e-15)
use_depth_loss = cfg["Training"].get("depth_loss", True)
log, t0 = [], time.time()
for it in range(args.iters):
    i = int(rng.integers(n_train))
    cam, gt_rgb, sensor = make_camera(train_ds, i)
    target = label_depth(i, sensor)
    valid = target > 0.01
    # appearance + depth (SplatLoc's mapping loss)
    shs = pc.get_features.transpose(1, 2).view(-1, 3, (pc.max_sh_degree + 1) ** 2)
    d = pc.get_xyz - cam.camera_center
    rgb = torch.clamp_min(eval_sh(pc.active_sh_degree, shs, d / d.norm(dim=1, keepdim=True)) + 0.5, 0.0)
    img, depth, _, z = render(cam, torch.cat([rgb, torch.zeros_like(rgb[:, :1])], 1), pc.get_opacity)
    l_rgb = (img[:3] - gt_rgb).abs().mean()
    l_depth = ((depth - target).abs() * valid).mean() if use_depth_loss else torch.zeros((), device="cuda")
    loss = l_rgb + l_depth
    l_occ = torch.zeros((), device="cuda")
    if args.lam > 0:
        tv = target[valid]
        for _ in range(2):
            zk = float(tv[int(rng.integers(tv.numel()))]) + float(rng.uniform(-0.3, 0.3))
            zk = max(zk, 0.3)
            gate = torch.sigmoid((zk - z) / args.tau_g)[:, None]
            _, _, A, _ = render(cam, torch.zeros(z.shape[0], 4, device="cuda"), pc.get_opacity * gate)
            y = (target < zk).float()
            m = valid & ((target - zk).abs() >= 0.02)
            yy = y.cpu().numpy().astype(np.uint8)
            edge = cv2.morphologyEx(yy, cv2.MORPH_GRADIENT, np.ones((3, 3), np.uint8))
            band = torch.from_numpy(cv2.dilate(edge, np.ones((7, 7), np.uint8)).astype(np.float32)).cuda()
            w = m.float() * (1 + 4 * band)
            bce = F.binary_cross_entropy(A.clamp(1e-4, 1 - 1e-4), y, reduction="none")
            l_occ = l_occ + (bce * w).sum() / w.sum().clamp_min(1) / 2
        loss = loss + args.lam * l_occ
    opt.zero_grad(set_to_none=True)
    loss.backward()
    opt.step()
    if it % 250 == 0 or it == args.iters - 1:
        log.append(dict(it=it, rgb=round(l_rgb.item(), 5), depth=round(l_depth.item(), 5), occ=round(l_occ.item(), 5)))
        print(f"  it {it:5d}  rgb {l_rgb.item():.4f}  depth {l_depth.item():.4f}  occ {l_occ.item():.4f}  {time.time() - t0:.0f}s", flush=True)

out = os.path.join(ROOT, "outputs", f"{args.cond}_{tag}", "replica", args.scene, "point_cloud", "final")
os.makedirs(out, exist_ok=True)
pc.save_ply(os.path.join(out, "point_cloud.ply"))
json.dump(dict(vars(args), tag=tag, minutes=round((time.time() - t0) / 60, 2), log=log),
          open(os.path.join(out, "finetune.json"), "w"), indent=1)
print(f"saved {out}/point_cloud.ply ({(time.time() - t0) / 60:.1f} min)")
