#!/bin/bash
# Build diff_gauss_clip (one-pass exact A(p, z_v(p)); see third_party/make_clip_rasterizer.py) into the
# splatloc env. Login node, ~5 min. Safe to rerun.   Usage: bash cluster/build_clip.sh
set -euo pipefail
source cluster/config.sh
activate splatloc
python third_party/make_clip_rasterizer.py "$SPLATLOC_DIR/submodules/diff-gaussian-rasterization" "$VGAR_WORK/src/diff_gauss_clip"
pip install --no-build-isolation "$VGAR_WORK/src/diff_gauss_clip"
python -c "import diff_gauss_clip, diff_gauss; print('diff_gauss_clip OK')"
