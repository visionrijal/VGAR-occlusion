#!/bin/bash
# One-time setup on the LOGIN node (needs internet, no GPU): micromamba, both envs,
# SplatLoc + Depth-Anything-V2 at pinned commits, our SplatLoc patch, CUDA extensions, DAv2 weights.
# Usage (from the repo root):  bash cluster/setup_env.sh 2>&1 | tee setup_env.log
set -euo pipefail
source cluster/config.sh
source third_party/pins.sh
echo "VGAR_WORK=$VGAR_WORK"
mkdir -p "$VGAR_WORK"/{src,checkpoints,logs,downloads,data,outputs}

# 1. micromamba (user space)
if [ ! -x "$MAMBA_EXE" ]; then
  echo "== installing micromamba"
  mkdir -p "$HOME/.local"
  curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xj -C "$HOME/.local" bin/micromamba
fi
"$MAMBA_EXE" --version

# 2. environments
for env in splatloc dav2; do
  if [ -d "$MAMBA_ROOT_PREFIX/envs/$env" ]; then echo "== env $env exists"; else
    echo "== creating env $env (10-20 min)"
    "$MAMBA_EXE" create -y -n "$env" -f "env/$env.yml"
  fi
done
"$MAMBA_EXE" clean -a -y >/dev/null   # drop the package cache (~7 GB) to stay well inside the 100 GB home quota

# 3. sources at pinned commits
if [ ! -d "$SPLATLOC_DIR/.git" ]; then git clone "$SPLATLOC_URL" "$SPLATLOC_DIR"; fi
cd "$SPLATLOC_DIR"
git fetch -q origin && git checkout -q "$SPLATLOC_COMMIT"
git submodule update --init submodules/diff-gaussian-rasterization submodules/simple-knn
if git apply --check "$REPO/third_party/splatloc.patch" 2>/dev/null; then
  git apply "$REPO/third_party/splatloc.patch"; echo "== applied VGAR patch to SplatLoc"
elif git apply --reverse --check "$REPO/third_party/splatloc.patch" 2>/dev/null; then
  echo "== VGAR patch already applied"
else
  echo "!! VGAR patch does not apply cleanly"; exit 1
fi
cd "$REPO"
if [ ! -d "$DAV2_DIR/.git" ]; then git clone "$DAV2_URL" "$DAV2_DIR"; fi
(cd "$DAV2_DIR" && git fetch -q origin && git checkout -q "$DAV2_COMMIT")

# 4. CUDA extensions (compiles on the login node; no GPU needed)
activate splatloc
echo "== building rasterizer + simple-knn for TORCH_CUDA_ARCH_LIST=$TORCH_CUDA_ARCH_LIST (5-15 min)"
pip install --no-build-isolation "$SPLATLOC_DIR/submodules/diff-gaussian-rasterization" "$SPLATLOC_DIR/submodules/simple-knn"

# 5. per-machine SplatLoc configs
python vgar/make_configs.py

# 6. Depth Anything V2 metric (Hypersim, ViT-S) weights
ck="$VGAR_CKPT/depth_anything_v2_metric_hypersim_vits.pth"
[ -s "$ck" ] || curl -L --fail -o "$ck" "$DAV2_CKPT_URL"

# 7. smoke tests (CUDA is not available on the login node; imports only)
python -c "import torch, diff_gauss, simple_knn, open3d; import open3d.visualization.gui; print('splatloc env OK, torch', torch.__version__, 'cuda build', torch.version.cuda)"
activate dav2
python -c "import torch, cv2, gdown; print('dav2 env OK, torch', torch.__version__)"
ls -la "$ck"
echo "== setup done. Next: bash cluster/fetch_data.sh"
