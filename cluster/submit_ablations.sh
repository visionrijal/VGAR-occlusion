#!/bin/bash
# Ablations (U-Net only; baselines are recomputed in every fold), 3 conditions x 8 folds each:
#   input features   depth_only | opacity_only | no_rgb
#   object slices    4 | 8 | 16 per-object slices, or grid (the global 32-depth grid) instead of the exact clip
#   plane slices     global grid with K = 4 | 8 | 16 depths (planes are then interpolated too)
# Run after the main folds have finished.   Usage: bash cluster/submit_ablations.sh [names...]
set -euo pipefail
source cluster/config.sh
L=$VGAR_WORK/logs; mkdir -p "$L"
declare -A ABL=(
  [feats_depth_only]="--feats depth_only" [feats_opacity_only]="--feats opacity_only" [feats_no_rgb]="--feats no_rgb"
  [objK_4]="--objK 4" [objK_8]="--objK 8" [objK_16]="--objK 16" [objK_grid]="--objK grid"
  [K_4]="--K 4" [K_8]="--K 8" [K_16]="--K 16"
)
names=("$@"); [ ${#names[@]} -gt 0 ] || names=("${!ABL[@]}")
n=0
for a in "${names[@]}"; do
  for c in "${CONDS[@]}"; do for t in "${SCENES[@]}"; do
    sbatch --account="$SLURM_ACCOUNT" --partition="$SLURM_PARTITION" --time=01:30:00 -J "abl-$a-$c-$t" \
      -o "$L/abl-$a-$c-$t-%j.out" --export=ALL,COND=$c,TEST=$t,EXTRA="--models unet --tag abl_$a ${ABL[$a]}" \
      cluster/jobs/loso.sbatch >/dev/null; n=$((n+1))
  done; done
done
echo "submitted $n ablation folds: ${names[*]}"
echo "When done: for t in results/abl_*; do python vgar/aggregate.py \$(basename \$t); done; git add results; git commit -m ablations; git push"
