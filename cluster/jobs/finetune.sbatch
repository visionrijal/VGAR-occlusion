#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=01:00:00
# Fine-tune one map (vgar/occ_finetune.py), then compute its features and object features.
# Needs SCENE, COND (rgbd|mono), LAM (0 = control), TAG (ctl|occ).
set -euo pipefail
cd "$SLURM_SUBMIT_DIR"; source cluster/config.sh
: "${SCENE:?}" "${COND:?}" "${LAM:?}" "${TAG:?}"
activate splatloc
python vgar/occ_finetune.py "$SCENE" "$COND" --lam "$LAM" --tag "$TAG"
python vgar/features.py "$SCENE" "${COND}_${TAG}"
python vgar/obj_features.py "$SCENE" "${COND}_${TAG}"
