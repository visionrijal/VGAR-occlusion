#!/bin/bash
#SBATCH --job-name=vgar-objects
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --time=01:00:00
# Object placements for all 8 scenes (CPU only, ~15 s per scene). Skips scenes already done.
set -euo pipefail
cd "$SLURM_SUBMIT_DIR"; source cluster/config.sh
activate splatloc
python vgar/objects.py "${SCENES[@]}"
