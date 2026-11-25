#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=00:45:00
# Per-object depth slices (16, plus 4/8 subsets) for every placed object in one map. Needs SCENE, COND.
set -euo pipefail
cd "$SLURM_SUBMIT_DIR"; source cluster/config.sh
: "${SCENE:?}" "${COND:?}"
activate splatloc
python vgar/obj_features.py "$SCENE" "$COND"
