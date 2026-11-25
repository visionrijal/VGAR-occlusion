#!/bin/bash
# Submit Depth Anything depth (1 job) and all 24 maps (8 scenes x 3 conditions).
# 'mono' maps wait for the depth job; the rest start at once. Finished maps are skipped.
# Usage (repo root, login node):  bash cluster/submit_maps.sh      FORCE=1 to retrain everything
set -euo pipefail
source cluster/config.sh
L=$VGAR_WORK/logs; mkdir -p "$L"
activate splatloc; python vgar/make_configs.py   # write configs once, before jobs start
common=(--account="$SLURM_ACCOUNT" --partition="$SLURM_PARTITION" --parsable)
mono=$(sbatch "${common[@]}" -o "$L/mono_depth-%j.out" cluster/jobs/mono_depth.sbatch)
echo "mono depth: job $mono"
for s in "${SCENES[@]}"; do for c in "${CONDS[@]}"; do
  dep=(); [ "$c" = mono ] && dep=(--dependency=afterok:$mono)
  j=$(sbatch "${common[@]}" "${dep[@]}" -J "map-$s-$c" -o "$L/map-$s-$c-%j.out" \
      --export=ALL,SCENE=$s,COND=$c,FORCE=${FORCE:-0} cluster/jobs/map.sbatch)
  echo "map $s $c: job $j"
done; done
echo "Watch with: bash cluster/status.sh"
