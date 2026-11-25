"""End-to-end AR compositing check: ray-cast a virtual sphere with Open3D into a Sequence_2 view,
build the GT occlusion label from Replica depth, composite with B0 (depth test) and B2 (soft
opacity, interpolated over K depth slices), and save a figure + per-object error numbers."""
import os
import sys

import cv2
import numpy as np
import open3d as o3d
import torch

from common import ROOT, clipped_opacity, load_model, make_camera, ray_stats, render_rgb, test_dataset

cfg_path = sys.argv[1] if len(sys.argv) > 1 else "configs/vgar/room_0_rgbd.yaml"
condition = sys.argv[2] if len(sys.argv) > 2 else "rgbd"
K_SLICES, TAU, RADIUS = 16, 0.01, 0.15
rng = np.random.default_rng(1)

cfg, pc = load_model(cfg_path, condition)
ds = test_dataset(cfg)
H, W = ds.height, ds.width
Kmat = ds.K.astype(np.float64)


def raycast_sphere(center, w2c):
    mesh = o3d.geometry.TriangleMesh.create_sphere(radius=RADIUS, resolution=40)
    mesh.translate(center); mesh.compute_vertex_normals()
    scene = o3d.t.geometry.RaycastingScene()
    scene.add_triangles(o3d.t.geometry.TriangleMesh.from_legacy(mesh))
    rays = o3d.t.geometry.RaycastingScene.create_rays_pinhole(
        o3d.core.Tensor(Kmat), o3d.core.Tensor(w2c.astype(np.float64)), W, H)
    ans = scene.cast_rays(rays)
    t = ans["t_hit"].numpy(); hit = np.isfinite(t)
    r = rays.numpy()
    X = r[..., :3] + t[..., None] * r[..., 3:]                      # world hit points
    Xc = X @ w2c[:3, :3].T + w2c[:3, 3]                              # camera frame -> z-depth (convention-free)
    zv = np.where(hit, Xc[..., 2], np.inf)
    nrm = ans["primitive_normals"].numpy()
    return zv.astype(np.float32), hit, nrm


found = None
for attempt in range(400):
    idx = int(rng.integers(0, ds.num_imgs))
    cam, gt_rgb, gt_d = make_camera(ds, idx)
    gtd = gt_d.cpu().numpy()
    u, v = int(rng.integers(80, W - 80)), int(rng.integers(80, H - 80))
    if gtd[v, u] < 0.5:
        continue
    w2c = cam.W2C.cpu().numpy(); c2w = np.linalg.inv(w2c)
    # back-project a surface point, then pull the sphere toward the camera so it rests in front of the surface
    p_cam = np.linalg.inv(Kmat) @ np.array([u, v, 1.0]) * gtd[v, u]
    p_cam = p_cam * (1 - (RADIUS * 1.05) / np.linalg.norm(p_cam))
    center = c2w[:3, :3] @ p_cam + c2w[:3, 3]
    # move it laterally by a random offset so nearby geometry can occlude part of it
    center = center + c2w[:3, :3] @ np.array([rng.normal(0, 0.25), rng.normal(0, 0.1), rng.uniform(0.0, 0.8)])
    zv, hit, nrm = raycast_sphere(center, w2c)
    if hit.sum() < 500:
        continue
    occ = (gtd < zv - TAU) & hit & (gtd > 0.01)
    frac = occ[hit].mean()
    if 0.1 <= frac <= 0.9:
        found = (idx, cam, gt_rgb, gtd, zv, hit, nrm, occ, frac)
        break
assert found, "no partially occluded placement found"
idx, cam, gt_rgb, gtd, zv, hit, nrm, occ, frac = found

st = ray_stats(cam, pc)
D = torch.where(st["A"] > 1e-3, st["D"], torch.full_like(st["D"], 1e3)).cpu().numpy()
o_b0 = (D < zv) & hit
# B2: A(p, z_v(p)) by linear interpolation between K depth slices spanning the object's depth range
zmin, zmax = zv[hit].min(), zv[hit].max()
zk = np.linspace(zmin, zmax, K_SLICES)
Ak = np.stack([clipped_opacity(cam, pc, float(z), st["z"]).cpu().numpy() for z in zk])  # [K,H,W]
pos = np.clip((np.where(hit, zv, zmin) - zmin) / max(zmax - zmin, 1e-6) * (K_SLICES - 1), 0, K_SLICES - 1)
lo = np.floor(pos).astype(int); hi = np.minimum(lo + 1, K_SLICES - 1); fr = pos - lo
ii, jj = np.indices(zv.shape)
A_zv = (1 - fr) * Ak[lo, ii, jj] + fr * Ak[hi, ii, jj]
o_b2 = A_zv * hit

real = render_rgb(cam, pc)[0].clamp(0, 1).permute(1, 2, 0).cpu().numpy()
gtimg = gt_rgb.permute(1, 2, 0).cpu().numpy()
shade = np.clip(0.35 + 0.65 * np.abs(nrm @ np.array([0.3, -0.5, -0.8]) / np.linalg.norm([0.3, -0.5, -0.8])), 0, 1)
virt = np.stack([0.9 * shade, 0.2 * shade, 0.2 * shade], -1)


def comp(img, O):  # I = M_v [(1-O) I_v + O I_real] + (1-M_v) I_real
    O = O[..., None]; M = hit[..., None].astype(np.float32)
    return M * ((1 - O) * virt + O * img) + (1 - M) * img


def err_overlay(img, pred):
    e = img.copy(); fo = pred & ~occ & hit; mo = ~pred & occ & hit
    e[fo] = [1, 1, 0]; e[mo] = [0, 1, 1]
    return e


m = hit & (gtd > 0.01) & (np.abs(gtd - zv) >= TAU)
iou = lambda p: (p & occ & m).sum() / max(((p | occ) & m).sum(), 1)
print(f"view {idx}: object px {hit.sum()}, GT occluded fraction {frac:.2f} | IoU(occluded) B0 {iou(o_b0):.3f}  B1(A>=.5) {iou((A_zv >= 0.5) & hit):.3f}"
      f" | errors B0 {((o_b0 != occ) & m).sum()} px, B1 {(((A_zv >= 0.5) & hit) != occ)[m].sum()} px")
row1 = np.concatenate([comp(gtimg, occ.astype(np.float32)), comp(real, o_b0.astype(np.float32)), comp(real, o_b2.astype(np.float32))], 1)
row2 = np.concatenate([np.repeat(occ[..., None], 3, -1).astype(np.float32), err_overlay(real, o_b0), np.repeat(A_zv[..., None] * hit[..., None], 3, -1)], 1)
out = os.path.join(ROOT, "outputs", "checks", f"compose_{os.path.basename(cfg['Dataset']['dataset_path'])}_{condition}.png")
cv2.imwrite(out, (np.concatenate([row1, row2], 0)[..., ::-1] * 255).astype(np.uint8))
print("saved", out, "| top: GT composite, B0 composite, soft-opacity composite | bottom: GT label, B0 errors (yellow=false occl, cyan=missed), A(p,z_v)")
