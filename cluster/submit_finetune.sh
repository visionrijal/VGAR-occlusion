#!/bin/bash
# Step 1 of the extension: fine-tune every RGB-D and Depth Anything map with (occ, lambda=1) and without
# (ctl, lambda=0) the occlusion loss, then run the main LOSO folds on each new map version.
# 32 fine-tune jobs (~5 min each incl. features) + 32 folds.   Usage: bash cluster/submit_finetune.sh
set -euo pipefail
source cluster/config.sh
L=$VGAR_WORK/logs; mkdir -p "$L"
acct=(--account="$SLURM_ACCOUNT" --partition="$SLURM_PARTITION" --parsable)
for c in rgbd mono; do
  for spec in "ctl 0" "occ 1"; do
    set -- $spec; tag=$1; lam=$2; ids=()
    for s in "${SCENES[@]}"; do
      ids+=($(sbatch "${acct[@]}" -J "ft-$s-${c}_$tag" -o "$L/ft-$s-${c}_$tag-%j.out" \
              --export=ALL,SCENE=$s,COND=$c,LAM=$lam,TAG=$tag cluster/jobs/finetune.sbatch))
    done
    dep=$(IFS=:; echo "afterok:${ids[*]}")
    for t in "${SCENES[@]}"; do
      sbatch "${acct[@]}" --dependency="$dep" -J "loso-${c}_$tag-$t" -o "$L/loso-${c}_$tag-$t-%j.out" \
        --export=ALL,COND=${c}_$tag,TEST=$t cluster/jobs/loso.sbatch >/dev/null
    done
    echo "${c}_$tag: 8 fine-tune jobs + 8 folds submitted"
  done
done
