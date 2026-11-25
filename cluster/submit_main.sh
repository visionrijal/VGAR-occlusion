#!/bin/bash
# Per-object slices for all 24 maps, then the 24 main LOSO folds (all methods), each condition's folds
# waiting for that condition's 8 object-feature jobs. Needs features + objects from submit_stage2.sh.
# Usage: scancel -u $USER   (if older folds are still queued)   then   bash cluster/submit_main.sh
set -euo pipefail
source cluster/config.sh
L=$VGAR_WORK/logs; mkdir -p "$L"
acct=(--account="$SLURM_ACCOUNT" --partition="$SLURM_PARTITION" --parsable)
for c in "${CONDS[@]}"; do
  ids=()
  for s in "${SCENES[@]}"; do
    ids+=($(sbatch "${acct[@]}" -J "objf-$s-$c" -o "$L/objf-$s-$c-%j.out" --export=ALL,SCENE=$s,COND=$c cluster/jobs/obj_features.sbatch))
  done
  dep=$(IFS=:; echo "afterok:${ids[*]}")
  for t in "${SCENES[@]}"; do
    sbatch "${acct[@]}" --dependency="$dep" -J "loso-$c-$t" -o "$L/loso-$c-$t-%j.out" \
      --export=ALL,COND=$c,TEST=$t cluster/jobs/loso.sbatch >/dev/null
  done
  echo "$c: 8 object-feature jobs + 8 folds submitted"
done
echo "When done: activate splatloc; python vgar/aggregate.py main; git add results; git commit -m 'main results'; git push"
