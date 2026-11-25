"""Shared helpers: load a trained SplatLoc model, build Sequence_2 test cameras,
and render auxiliary per-pixel quantities with the stock 4-channel rasterizer."""
import math
import os
import sys

import numpy as np
import torch

# Paths come from the environment (cluster/config.sh or local env.sh); defaults match the laptop layout.
ROOT = os.environ.get("VGAR_WORK", "/home/regex/Documents/VGAR")
SPLATLOC = os.environ.get("SPLATLOC_DIR", os.path.join(ROOT, "code", "SplatLoc"))
sys.path.insert(0, SPLATLOC)
os.chdir(SPLATLOC)  # SplatLoc configs use paths relative to the repo root

from diff_gauss import GaussianRasterizationSettings, GaussianRasterizer  # noqa: E402
from gaussian_splatting.scene.gaussian_model import GaussianModel  # noqa: E402
from gaussian_splatting.utils.graphics_utils import getProjectionMatrix2  # noqa: E402
from utils.camera_utils import Camera  # noqa: E402
from utils.config_utils import load_config  # noqa: E402
from utils.dataset import load_dataset  # noqa: E402


def load_model(config_path, condition="rgbd"):
    cfg = load_config(config_path)
    scene = os.path.basename(cfg["Dataset"]["dataset_path"].rstrip("/"))
    ply = os.path.join(ROOT, "outputs", condition, "replica", scene, "point_cloud/final/point_cloud.ply")
    pc = GaussianModel(cfg["model_params"]["sh_degree"], config=cfg)
    pc.load_ply(ply)
    return cfg, pc


def test_dataset(cfg):
    return load_dataset(cfg, train=False)


def make_camera(ds, idx):
    proj = getProjectionMatrix2(znear=0.01, zfar=100.0, fx=ds.fx, fy=ds.fy, cx=ds.cx, cy=ds.cy,
                                W=ds.width, H=ds.height).transpose(0, 1)
    ret = ds[idx]
    cam = Camera.init_from_pose(idx, ds, ret["w2c"].to(ds.device), proj)
    gt_rgb = ret["rgb"].permute(2, 0, 1).float().cuda()
    gt_depth = torch.as_tensor(np.asarray(ret["depth"]), dtype=torch.float32, device="cuda")
    return cam, gt_rgb, gt_depth


def view_depth(cam, xyz):
    """Camera-space z of each Gaussian centre (same quantity the rasterizer sorts by)."""
    ones = torch.ones_like(xyz[:, :1])
    p = torch.cat([xyz, ones], 1) @ cam.world_view_transform  # row-vector convention
    return p[:, 2]


@torch.no_grad()
def render_aux(cam, pc, colors4, mask=None):
    """Rasterize with precomputed 4-channel colours, optionally on a subset of Gaussians.
    Returns (image[4,H,W], depth[1,H,W] = sum w z (unnormalized), alpha[1,H,W] = 1 - T)."""
    settings = GaussianRasterizationSettings(
        image_height=int(cam.image_height), image_width=int(cam.image_width),
        tanfovx=math.tan(cam.FoVx * 0.5), tanfovy=math.tan(cam.FoVy * 0.5),
        bg=torch.zeros(4, device="cuda"), scale_modifier=1.0,
        viewmatrix=cam.world_view_transform, projmatrix=cam.full_proj_transform,
        sh_degree=pc.active_sh_degree, campos=cam.camera_center, prefiltered=False, debug=False)
    r = GaussianRasterizer(raster_settings=settings)
    xyz, op, sc, rot = pc.get_xyz, pc.get_opacity, pc.get_scaling, pc.get_rotation
    if sc.shape[-1] == 1:
        sc = sc.repeat(1, 3)
    # The SplatLoc/MonoGS fork culls in NDC only, so Gaussians *behind* the camera (|z| > ~2 m)
    # pass culling and, because depth is sorted as raw float bits, are composited last.
    # Apply the standard 3DGS near-plane cull (view z > 0.2) to every render we make.
    near_ok = view_depth(cam, xyz) > 0.2
    mask = near_ok if mask is None else (mask & near_ok)
    xyz, op, sc, rot, colors4 = xyz[mask], op[mask], sc[mask], rot[mask], colors4[mask]
    means2D = torch.zeros_like(xyz)
    img, depth, alpha, _ = r(means3D=xyz, means2D=means2D, opacities=op, colors_precomp=colors4.contiguous(),
                             scales=sc, rotations=rot)
    return img, depth, alpha


@torch.no_grad()
def render_rgb(cam, pc):
    """Ordinary colour render (SH degree 0 in SplatLoc configs -> RGB = SH0*C0 + 0.5)."""
    from gaussian_splatting.utils.sh_utils import eval_sh
    shs = pc.get_features.transpose(1, 2).view(-1, 3, (pc.max_sh_degree + 1) ** 2)
    d = pc.get_xyz - cam.camera_center
    rgb = torch.clamp_min(eval_sh(pc.active_sh_degree, shs, d / d.norm(dim=1, keepdim=True)) + 0.5, 0.0)
    c4 = torch.cat([rgb, torch.zeros_like(rgb[:, :1])], 1)
    img, depth, alpha = render_aux(cam, pc, c4)
    return img[:3], depth, alpha


@torch.no_grad()
def ray_stats(cam, pc):
    """One pass: A_tot, expected depth D = sum(wz)/A, depth std sigma_D."""
    z = view_depth(cam, pc.get_xyz)
    c4 = torch.stack([torch.ones_like(z), z, z * z, torch.zeros_like(z)], 1)
    img, depth_native, alpha_native = render_aux(cam, pc, c4)
    A = img[0]
    eps = 1e-6
    D = img[1] / A.clamp_min(eps)
    var = (img[2] / A.clamp_min(eps) - D * D).clamp_min(0)
    return dict(A=A, D=D, sigma=var.sqrt(), z=z, img=img, depth_native=depth_native[0], alpha_native=alpha_native[0])


@torch.no_grad()
def clipped_opacity(cam, pc, z_thresh, z=None):
    """A(p, z_thresh): accumulated opacity of Gaussians whose centre depth < z_thresh."""
    if z is None:
        z = view_depth(cam, pc.get_xyz)
    m = z < z_thresh
    if m.sum() == 0:
        return torch.zeros(int(cam.image_height), int(cam.image_width), device="cuda")
    c4 = torch.zeros(z.shape[0], 4, device="cuda")
    _, _, alpha = render_aux(cam, pc, c4, mask=m)
    return alpha[0]
