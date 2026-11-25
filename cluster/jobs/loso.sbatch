#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=04:00:00
# One leave-one-scene-out fold: train on 7 scenes, evaluate every method on TEST. Needs COND, TEST;
# optional EXTRA (more loso.py arguments, e.g. "--feats depth_only --models unet --tag abl_depth_only").
set -euo pipefail
cd "$SLURM_SUBMIT_DIR"; source cluster/config.sh
: "${COND:?}" "${TEST:?}"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
activate splatloc
python vgar/loso.py --cond "$COND" --test "$TEST" --preload ${EXTRA:-}
