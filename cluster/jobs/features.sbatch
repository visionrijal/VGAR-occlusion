#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=00:45:00
# Ray features (stats pass + 32 depth slices + RGB) for the 90 test views of one map. Needs SCENE, COND.
set -euo pipefail
cd "$SLURM_SUBMIT_DIR"; source cluster/config.sh
: "${SCENE:?}" "${COND:?}"
activate splatloc
python vgar/features.py "$SCENE" "$COND"
