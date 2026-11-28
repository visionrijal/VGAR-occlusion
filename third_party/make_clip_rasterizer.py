"""Generate `diff_gauss_clip`: a copy of SplatLoc's rasterizer with one extra, optional forward input,
a per-pixel clip depth. Each pixel composites only the Gaussians whose centre depth is below its own clip
depth, so the returned alpha is exactly A(p, z_v(p)) for an arbitrary virtual depth map in ONE pass
(previously approximated by interpolating K depth slices).

Why stopping early is exact: the rasterizer sorts each tile's Gaussians by view-space centre depth and
composites them front to back, so once one Gaussian reaches the clip depth every later one does too.
Depth-slice rendering (render only Gaussians with z_i < z) uses the same rule, so the two must agree
up to float rounding (tested in vgar/test_clip.py).

Only the forward pass is changed; the backward pass ignores the clip, so use it under torch.no_grad().
The original `diff_gauss` used by SplatLoc training is untouched.

Usage: python third_party/make_clip_rasterizer.py <src: SplatLoc/submodules/diff-gaussian-rasterization> <dst>
       pip install --no-build-isolation <dst>
"""
import os
import shutil
import sys

src, dst = sys.argv[1], sys.argv[2]
if os.path.exists(dst):
    shutil.rmtree(dst)
shutil.copytree(src, dst, ignore=shutil.ignore_patterns("build", "*.egg-info", "__pycache__", ".git"))
os.rename(os.path.join(dst, "diff_gauss"), os.path.join(dst, "diff_gauss_clip"))


def edit(rel, old, new, count=1):
    p = os.path.join(dst, rel)
    s = open(p).read()
    n = s.count(old)
    assert n == count, f"{rel}: expected {count} match(es), found {n}:\n{old}"
    open(p, "w").write(s.replace(old, new))


# --- build: new package name so it can sit next to diff_gauss
edit("setup.py", 'name="diff_gauss"', 'name="diff_gauss_clip"')
edit("setup.py", "packages=['diff_gauss']", "packages=['diff_gauss_clip']")
edit("setup.py", 'name="diff_gauss._C"', 'name="diff_gauss_clip._C"')

# --- kernel: read the pixel's clip depth, stop at the first Gaussian at or beyond it
edit("cuda_rasterizer/forward.cu",
     "\tfloat* __restrict__ out_color,\n\tfloat* __restrict__ out_depth)\n{",
     "\tfloat* __restrict__ out_color,\n\tfloat* __restrict__ out_depth,\n\tconst float* __restrict__ clip_depth)\n{")
edit("cuda_rasterizer/forward.cu",
     "\tbool done = !inside;\n",
     "\tbool done = !inside;\n\t// VGAR: per-pixel clip depth (+inf when no clip buffer is given)\n"
     "\tconst float clip = (clip_depth != nullptr && inside) ? clip_depth[pix_id] : INFINITY;\n")
edit("cuda_rasterizer/forward.cu",
     "\t\t\t// Keep track of current position in range\n\t\t\tcontributor++;\n",
     "\t\t\t// VGAR: Gaussians arrive sorted by centre depth; the first one at/after the clip ends this pixel\n"
     "\t\t\tif (depths[collected_id[j]] >= clip)\n\t\t\t{\n\t\t\t\tdone = true;\n\t\t\t\tcontinue;\n\t\t\t}\n\n"
     "\t\t\t// Keep track of current position in range\n\t\t\tcontributor++;\n")
edit("cuda_rasterizer/forward.cu",
     "\tfloat* out_color,\n\tfloat* out_depth)\n{\n\trenderCUDA<NUM_CHANNELS> << <grid, block >> > (",
     "\tfloat* out_color,\n\tfloat* out_depth,\n\tconst float* clip_depth)\n{\n\trenderCUDA<NUM_CHANNELS> << <grid, block >> > (")
edit("cuda_rasterizer/forward.cu",
     "\t\tout_color,\n\t\tout_depth);\n}",
     "\t\tout_color,\n\t\tout_depth,\n\t\tclip_depth);\n}")
edit("cuda_rasterizer/forward.h",
     "\t\tfloat* out_color,\n\t\tfloat* out_depth);\n\n\tvoid fusedPreprocess4D(",
     "\t\tfloat* out_color,\n\t\tfloat* out_depth,\n\t\tconst float* clip_depth);\n\n\tvoid fusedPreprocess4D(")

# --- Rasterizer::forward: thread the pointer through (defaults to no clip)
edit("cuda_rasterizer/rasterizer.h",
     "\t\t\tint* radii = nullptr,\n\t\t\tbool debug = false);",
     "\t\t\tint* radii = nullptr,\n\t\t\tbool debug = false,\n\t\t\tconst float* clip_depth = nullptr);")
edit("cuda_rasterizer/rasterizer_impl.cu",
     "\tint* radii,\n\tbool debug)\n{\n\tconst float focal_y",
     "\tint* radii,\n\tbool debug,\n\tconst float* clip_depth)\n{\n\tconst float focal_y")
edit("cuda_rasterizer/rasterizer_impl.cu",
     "\t\tout_color,\n\t\tout_depth), debug)",
     "\t\tout_color,\n\t\tout_depth,\n\t\tclip_depth), debug)")

# --- torch entry point: optional clip tensor (empty = no clip)
edit("rasterize_points.h",
     "\tconst bool prefiltered,\n\tconst bool debug);\n\n\nstd::tuple",
     "\tconst bool prefiltered,\n\tconst bool debug,\n\tconst torch::Tensor& clip_depth);\n\n\nstd::tuple")
edit("rasterize_points.cu",
     "\tconst bool prefiltered,\n\tconst bool debug)\n{\n  if (means3D.ndimension() != 2",
     "\tconst bool prefiltered,\n\tconst bool debug,\n\tconst torch::Tensor& clip_depth)\n{\n  if (means3D.ndimension() != 2")
edit("rasterize_points.cu",
     "\t\tradii.contiguous().data_ptr<int>(),\n\t\tdebug);\n  }\n  return std::make_tuple(rendered, out_color",
     "\t\tradii.contiguous().data_ptr<int>(),\n\t\tdebug,\n"
     "\t\tclip_depth.numel() == H * W ? clip_depth.contiguous().data_ptr<float>() : nullptr);\n"
     "  }\n  return std::make_tuple(rendered, out_color")

# --- Python wrapper: GaussianRasterizer(...)(..., clip_depth=<H x W float tensor>)
pkg = "diff_gauss_clip/__init__.py"
edit(pkg, "    tile_mask,\n    raster_settings,\n):\n    return _RasterizeGaussians.apply(",
     "    tile_mask,\n    raster_settings,\n    clip_depth=None,\n):\n    return _RasterizeGaussians.apply(")
edit(pkg, "        tile_mask,\n        raster_settings,\n    )\n\n\nclass _RasterizeGaussians",
     "        tile_mask,\n        raster_settings,\n        clip_depth,\n    )\n\n\nclass _RasterizeGaussians")
edit(pkg, "        tile_mask,\n        raster_settings,\n    ):\n\n        # Restructure arguments the way that the C++ lib expects them",
     "        tile_mask,\n        raster_settings,\n        clip_depth=None,\n    ):\n\n        # Restructure arguments the way that the C++ lib expects them")
edit(pkg, "            raster_settings.prefiltered,\n            raster_settings.debug\n        )\n\n        # Invoke C++/CUDA rasterizer",
     "            raster_settings.prefiltered,\n            raster_settings.debug,\n"
     "            clip_depth.float().contiguous() if clip_depth is not None else torch.empty(0, device=means3D.device),\n"
     "        )\n\n        # Invoke C++/CUDA rasterizer")
edit(pkg, "    def backward(ctx, grad_out_color, grad_out_depth, grad_out_alpha, _):",
     "    def backward(ctx, grad_out_color, grad_out_depth, grad_out_alpha, _):\n"
     "        # VGAR: the clip only exists in the forward pass; gradients would ignore it\n")
p = os.path.join(dst, pkg)
s = open(p).read()
# backward returns one gradient per forward input: add None for clip_depth
import re
m = re.search(r"\n        grads = \((.*?)\n        \)\n", s, re.S)
assert m, "could not find the grads tuple in backward()"
s = s[:m.end() - len("\n        )\n")] + "\n            None,  # clip_depth\n        )\n" + s[m.end():]
open(p, "w").write(s)
edit(pkg, "    def forward(self, means3D, means2D, opacities, shs=None, colors_precomp=None, scales=None, rotations=None, cov3D_precomp=None, tile_mask=None):",
     "    def forward(self, means3D, means2D, opacities, shs=None, colors_precomp=None, scales=None, rotations=None, cov3D_precomp=None, tile_mask=None, clip_depth=None):")
edit(pkg, "            tile_mask,\n            raster_settings,\n        )\n\n\ndef mark_visible(",
     "            tile_mask,\n            raster_settings,\n            clip_depth,\n        )\n\n\ndef mark_visible(")
print(f"wrote {dst}")
