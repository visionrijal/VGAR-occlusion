#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=01:30:00
# Train one SplatLoc 3DGS map. Needs SCENE and COND (rgbd|mono|rgbonly) via --export.
# Skips if the map exists; set FORCE=1 to retrain.
set -euo pipefail
cd "$SLURM_SUBMIT_DIR"; source cluster/config.sh
: "${SCENE:?}" "${COND:?}"
ply=$VGAR_WORK/outputs/$COND/replica/$SCENE/point_cloud/final/point_cloud.ply
if [ -f "$ply" ] && [ "${FORCE:-0}" != 1 ]; then echo "exists: $ply"; exit 0; fi
nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv
activate splatloc
cd "$SPLATLOC_DIR"
start=$(date +%s)
python train_gaussians.py --config "configs/vgar/${SCENE}_${COND}.yaml"
test -f "$ply" || { echo "!! map not written: $ply"; exit 1; }
echo "DONE $SCENE $COND in $(( ($(date +%s) - start) / 60 )) min"
