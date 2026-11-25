"""Masks, labels and model inputs built from stored features (vgar/features.py) and objects (vgar/objects.py).

A *sample* is one virtual geometry in one test view: a fronto-parallel plane at 1, 1.5, 2 or 3 m
(depth-plane protocol, every pixel) or one placed object (object protocol, its silhouette only).

Labels (proposal §5): occluded(p) = D_gt(p) < z_v(p) - tau; pixels with |D_gt - z_v| < tau or no
GT depth are excluded. The boundary band is every valid pixel within `band` px of a pixel whose
3x3 neighbourhood contains both occluded and visible valid pixels.

A(p,z_v): planes read the global depth grid (exact at the plane depths); objects read per-object
slices over their own depth range (obj_features.py).

Model input (10 channels): A(p,z_v), A_tot, clip(z_v-D), clip((z_v-D)/sigma)/10, clip(sigma), z_v/3,
silhouette M_v, rendered RGB. z_v-dependent channels are zero outside the silhouette.
"""
import json
import os

import cv2
import numpy as np

ROOT = os.environ.get("VGAR_WORK", "/home/regex/Documents/VGAR")
SCENES = ["room_0", "room_1", "room_2", "office_0", "office_1", "office_2", "office_3", "office_4"]
TAU = 0.01
FEATURES = ["A_zv", "A_tot", "margin", "margin_n", "sigma", "z_v", "M_v", "r", "g", "b"]
FEATURE_SETS = {  # ablations: which input channels the learned models see
    "all": FEATURES,
    "depth_only": ["margin", "margin_n", "sigma", "z_v", "M_v"],
    "opacity_only": ["A_zv", "A_tot", "z_v", "M_v"],
    "no_rgb": FEATURES[:7],
}
PIXEL_FEATURES = ["A_zv", "A_tot", "margin", "margin_n", "sigma", "z_v"]  # per-pixel models (no RGB)


def k_subset(z_grid, planes, K):
    """Indices of K slices spread evenly over the 32-depth grid (K=32 keeps all)."""
    n = len(z_grid)
    if K >= n:
        return np.arange(n)
    return np.unique(np.round(np.linspace(0, n - 1, K)).astype(int))


class SceneData:
    def __init__(self, cond, scene, K=32, preload=False, obj_K="16"):
        d = os.path.join(ROOT, "features", cond, scene)
        self.meta = json.load(open(os.path.join(d, "meta.json")))
        self.scene, self.cond = scene, cond
        self.H, self.W = self.meta["H"], self.meta["W"]
        keep = k_subset(self.meta["z_grid"], self.meta["planes"], K)
        self.z_grid = np.asarray(self.meta["z_grid"], np.float32)[keep]
        self.keep = keep
        sl = np.load(os.path.join(d, "slices.npy"), mmap_mode="r")
        self.slices = np.ascontiguousarray(sl[:, keep]) if preload else sl
        self.mmap_keep = None if preload else keep
        self.atot = np.load(os.path.join(d, "atot.npy")).astype(np.float32)
        D = np.load(os.path.join(d, "D.npy")).astype(np.float32)
        self.D = np.where(self.atot > 1e-3, D, 1e3).astype(np.float32)  # no geometry -> nothing in front
        self.sigma = np.load(os.path.join(d, "sigma.npy")).astype(np.float32)
        self.rgb = np.load(os.path.join(d, "rgb.npy"))
        self.gt = np.load(os.path.join(d, "gt_mm.npy")).astype(np.float32) / 1000.0
        self.views = self.meta["views"]
        vidx = {v: i for i, v in enumerate(self.views)}
        ob = np.load(os.path.join(ROOT, "objects", f"{scene}.npz"))
        self.obj_zv = ob["zv_mm"]
        self.obj_view = np.array([vidx[v] for v in ob["view"]])
        self.obj_kind = ob["kind"]
        # objects: A(p,z_v) from slices over each object's own depth range (vgar/obj_features.py);
        # obj_K="grid" falls back to interpolating the global 32-depth grid (ablation)
        self.obj_K = str(obj_K)
        self.A_obj = None if self.obj_K == "grid" else np.load(os.path.join(d, f"A_obj_K{self.obj_K}.npy"),
                                                               mmap_mode=None if preload else "r")
        self.samples = [("plane", vi, z) for vi in range(len(self.views)) for z in self.meta["planes"]]
        self.samples += [("object", int(self.obj_view[j]), j) for j in range(len(self.obj_view))]

    # ---- geometry ---------------------------------------------------------------------------------
    def zv_map(self, s, ys, xs):
        kind, vi, p = s
        if kind == "plane":
            return np.full((ys.stop - ys.start, xs.stop - xs.start), p, np.float32)
        return self.obj_zv[p, ys, xs].astype(np.float32) / 1000.0

    def A_at(self, vi, zv, ys, xs):
        """A(p, z_v(p)) by linear interpolation between the stored depth slices (exact on grid depths)."""
        z = self.z_grid
        K = len(z)
        idx = np.searchsorted(z, zv, side="right")
        i1 = np.clip(idx, 1, K - 1)
        i0 = i1 - 1
        lo, hi = int(i0.min()), int(i1.max())
        if self.mmap_keep is None:
            slab = self.slices[vi, lo:hi + 1, ys, xs].astype(np.float32)
        else:
            slab = self.slices[vi, self.mmap_keep[lo:hi + 1], ys, xs].astype(np.float32)
        a0 = np.take_along_axis(slab, (i0 - lo)[None], 0)[0]
        a1 = np.take_along_axis(slab, (i1 - lo)[None], 0)[0]
        w = np.clip((zv - z[i0]) / (z[i1] - z[i0]), 0, 1)
        A = a0 + w * (a1 - a0)
        A = np.where(zv < z[0], a0 * np.clip((zv - 0.2) / (z[0] - 0.2), 0, 1), A)  # near cull at 0.2 m
        A = np.where(zv >= z[-1], self.atot[vi, ys, xs], A)
        return A.astype(np.float32)

    # ---- one sample -------------------------------------------------------------------------------
    def build(self, s, ys=None, xs=None, band_px=(3, 5)):
        ys = ys or slice(0, self.H)
        xs = xs or slice(0, self.W)
        kind, vi, _ = s
        zv = self.zv_map(s, ys, xs)
        sil = zv > 0
        gt = self.gt[vi, ys, xs]
        occ = (gt < zv - TAU) & sil
        valid = sil & (gt > 0.01) & (np.abs(gt - zv) >= TAU)
        if kind == "object" and self.A_obj is not None:
            A_zv = np.where(sil, self.A_obj[s[2], ys, xs].astype(np.float32), 0)
        else:
            A_zv = np.where(sil, self.A_at(vi, np.where(sil, zv, self.z_grid[0]), ys, xs), 0)
        D, sig, at = self.D[vi, ys, xs], self.sigma[vi, ys, xs], self.atot[vi, ys, xs]
        score_b0 = np.where(sil, zv - D, -1e3)
        Dc = np.minimum(D, 10.0)
        margin = np.clip(zv - Dc, -2, 2)
        feats = {
            "A_zv": A_zv, "A_tot": at,
            "margin": np.where(sil, margin, 0),
            "margin_n": np.where(sil, np.clip(margin / (sig + 1e-3), -20, 20) / 10, 0),
            "sigma": np.clip(sig, 0, 2), "z_v": zv / 3, "M_v": sil.astype(np.float32),
        }
        rgb = self.rgb[vi, :, ys, xs].astype(np.float32) / 255
        feats.update(r=rgb[0], g=rgb[1], b=rgb[2])
        u8 = np.ones((3, 3), np.uint8)
        vis = valid & ~occ
        edge = cv2.dilate((valid & occ).astype(np.uint8), u8).astype(bool) & cv2.dilate(vis.astype(np.uint8), u8).astype(bool)
        bands = {f"band{b}": cv2.dilate(edge.astype(np.uint8), np.ones((2 * b + 1,) * 2, np.uint8)).astype(bool) & valid
                 for b in band_px}
        return dict(feats=feats, y=occ, valid=valid, score_b0=score_b0, **bands)

    def object_crop(self, j, size, rng):
        """A size x size window around a random silhouette pixel of object j (for training crops)."""
        ys, xs = np.nonzero(self.obj_zv[j] > 0)
        k = rng.integers(len(ys))
        cy = int(np.clip(ys[k] + rng.integers(-size // 4, size // 4 + 1), size // 2, self.H - size // 2))
        cx = int(np.clip(xs[k] + rng.integers(-size // 4, size // 4 + 1), size // 2, self.W - size // 2))
        return slice(cy - size // 2, cy + size // 2), slice(cx - size // 2, cx + size // 2)
