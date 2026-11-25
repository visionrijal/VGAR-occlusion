#!/bin/bash
# Stage 2: object placements (CPU), features for all 24 maps, then the 24 main LOSO folds
# (3 conditions x 8 test scenes). Each fold waits for that condition's 8 feature jobs.
# Run after `bash cluster/status.sh` shows all 24 maps ok.   Usage: bash cluster/submit_stage2.sh
set -euo pipefail
source cluster/config.sh
missing=0
for s in "${SCENES[@]}"; do for c in "${CONDS[@]}"; do
  [ -f "$VGAR_WORK/outputs/$c/replica/$s/point_cloud/final/point_cloud.ply" ] || { echo "map missing: $s $c"; missing=1; }
done; done
[ $missing = 0 ] || { echo "!! wait until all maps exist (bash cluster/status.sh)"; exit 1; }
L=$VGAR_WORK/logs; mkdir -p "$L"
acct=(--account="$SLURM_ACCOUNT" --parsable)
obj=$(sbatch "${acct[@]}" --partition=compute -o "$L/objects-%j.out" cluster/jobs/objects.sbatch)
echo "objects: job $obj"
for c in "${CONDS[@]}"; do
  feats=()
  for s in "${SCENES[@]}"; do
    feats+=($(sbatch "${acct[@]}" --partition="$SLURM_PARTITION" -J "feat-$s-$c" -o "$L/feat-$s-$c-%j.out" \
              --export=ALL,SCENE=$s,COND=$c cluster/jobs/features.sbatch))
  done
  dep=$(IFS=:; echo "afterok:$obj:${feats[*]}")
  for t in "${SCENES[@]}"; do
    j=$(sbatch "${acct[@]}" --partition="$SLURM_PARTITION" --dependency="$dep" -J "loso-$c-$t" \
        -o "$L/loso-$c-$t-%j.out" --export=ALL,COND=$c,TEST=$t cluster/jobs/loso.sbatch)
    echo "loso $c $t: job $j"
  done
done
echo "When all loso jobs finish: python vgar/aggregate.py main && git add results && git commit -m 'main results' && git push"
