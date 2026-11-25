#!/bin/bash
#SBATCH --job-name=vgar-mono
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=02:00:00
# Depth Anything V2 metric depth for the 180 Sequence_1 training frames of every scene (skips finished scenes).
set -euo pipefail
cd "$SLURM_SUBMIT_DIR"; source cluster/config.sh
nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv
activate dav2
python vgar/mono_depth.py "${SCENES[@]}"
