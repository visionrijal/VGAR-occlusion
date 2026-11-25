"""Object protocol: place virtual primitives in each Sequence_2 test view and ray-cast their depth.

Placements depend only on ground-truth depth, so they are generated once per scene and shared by all
map conditions. For each test view (every 10th frame, 90 per scene) we try random placements of a
sphere, a box and a thin cylinder (fixed seed per scene/view) and keep up to 5 whose visible-pixel
silhouette is 10-90% occluded by real geometry (at most 2 per shape per view):
  - 'surface': centre on the observed surface point of a random pixel (object partly embedded)
  - 'free':    centre in free space, uniformly between 0.5 m and the observed surface depth
Objects are built in the camera frame (x right, y down, z forward) and ray-cast with Open3D; with ray
directions ((u-cx)/fx, (v-cy)/fy, 1) the hit distance t equals camera-space depth z.

Output: $VGAR_WORK/objects/<scene>.npz with zv_mm [N,H,W] uint16 depth in mm (0 = outside silhouette), view [N],
kind [N] (0 sphere, 1 box, 2 cylinder), mode [N] (0 surface, 1 free), occ_frac [N].
Usage: python vgar/objects.py room_0 [room_1 ...]
"""
import os
import sys
import zlib

import cv2
import numpy as np
import open3d as o3d

ROOT = os.environ.get("VGAR_WORK", "/home/regex/Documents/VGAR")
FX = FY = 320.0
CX, CY, W, H = 319.5, 239.5, 640, 480
TAU = 0.01
VIEWS = list(range(0, 900, 10))
PER_VIEW, TRIES = 5, 80
MIN_PIX = 400

u, v = np.meshgrid(np.arange(W), np.arange(H))
DIRS = np.stack([(u - CX) / FX, (v - CY) / FY, np.ones_like(u, dtype=np.float64)], -1).reshape(-1, 3)
RAYS = o3d.core.Tensor(np.concatenate([np.zeros_like(DIRS), DIRS], 1).astype(np.float32))


def rand_rotation(rng):
    q = rng.normal(size=4)
    q /= np.linalg.norm(q)
    return o3d.geometry.get_rotation_matrix_from_quaternion(q)


def make_mesh(kind, rng):
    if kind == 0:
        m = o3d.geometry.TriangleMesh.create_sphere(radius=rng.uniform(0.05, 0.25), resolution=24)
    elif kind == 1:
        s = rng.uniform(0.1, 0.5, size=3)
        m = o3d.geometry.TriangleMesh.create_box(*s)
        m.translate(-s / 2)
    else:
        m = o3d.geometry.TriangleMesh.create_cylinder(radius=rng.uniform(0.01, 0.03),
                                                      height=rng.uniform(0.3, 0.8), resolution=24)
    if kind != 0:
        m.rotate(rand_rotation(rng), center=(0, 0, 0))
    return m


def cast(mesh):
    scene = o3d.t.geometry.RaycastingScene()
    scene.add_triangles(o3d.t.geometry.TriangleMesh.from_legacy(mesh))
    t = scene.cast_rays(RAYS)["t_hit"].numpy().reshape(H, W)
    return np.where(np.isfinite(t), t, 0.0).astype(np.float32)


def place_view(scene, view, gt):
    rng = np.random.default_rng(zlib.crc32(f"{scene}/{view}".encode()))
    out = []
    for _ in range(TRIES):
        if len(out) == PER_VIEW:
            break
        kind, mode = int(rng.integers(3)), int(rng.integers(2))
        if sum(o[1] == kind for o in out) >= 2:  # at most 2 of each shape per view, keeps shapes balanced
            continue
        pu, pv = int(rng.integers(64, W - 64)), int(rng.integers(48, H - 48))
        d = gt[pv, pu]
        if d < 0.6:
            continue
        z = d if mode == 0 else rng.uniform(0.5, d)
        mesh = make_mesh(kind, rng)
        mesh.translate(z * DIRS[pv * W + pu])
        zv = cast(mesh)
        sil = (zv > 0) & (gt > 0.01) & (np.abs(gt - zv) >= TAU)
        if sil.sum() < MIN_PIX:
            continue
        frac = float((gt[sil] < zv[sil] - TAU).mean())
        if 0.1 <= frac <= 0.9:
            out.append((zv, kind, mode, frac))
    return out


def main(scene):
    path = os.path.join(ROOT, "objects", f"{scene}.npz")
    if os.path.exists(path):
        print(f"{scene}: {path} exists, skipping")
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    zvs, views, kinds, modes, fracs = [], [], [], [], []
    for view in VIEWS:
        gt = cv2.imread(os.path.join(ROOT, "data", "replica", scene, "Sequence_2", "depth", f"depth_{view}.png"),
                        cv2.IMREAD_UNCHANGED).astype(np.float32) / 1000.0
        for zv, kind, mode, frac in place_view(scene, view, gt):
            zvs.append(np.round(zv * 1000).astype(np.uint16)); views.append(view); kinds.append(kind); modes.append(mode); fracs.append(frac)
    np.savez(path, zv_mm=np.stack(zvs), view=np.array(views), kind=np.array(kinds), mode=np.array(modes),
             occ_frac=np.array(fracs, dtype=np.float32))
    k = np.bincount(kinds, minlength=3)
    print(f"{scene}: {len(zvs)} objects in {len(VIEWS)} views (sphere {k[0]}, box {k[1]}, cylinder {k[2]}; "
          f"surface {modes.count(0)}, free {modes.count(1)}; mean occluded {np.mean(fracs):.2f}) -> {path}")


if __name__ == "__main__":
    for s in sys.argv[1:]:
        main(s)
