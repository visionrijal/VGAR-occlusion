#!/bin/bash
# Queue, which maps exist, mono-depth counts, and any errors in the logs.
source cluster/config.sh
squeue -u "$USER" -o "%.10i %.24j %.8T %.10M %R" 2>/dev/null
printf "\n%-10s %-6s %-6s %-8s\n" scene rgbd mono rgbonly
for s in "${SCENES[@]}"; do
  row="$s"; for c in "${CONDS[@]}"; do
    [ -f "$VGAR_WORK/outputs/$c/replica/$s/point_cloud/final/point_cloud.ply" ] && row="$row ok" || row="$row --"
  done
  n=$(ls "$VGAR_WORK/data/mono_depth/$s" 2>/dev/null | wc -l)
  echo "$row" | awk -v n="$n" '{printf "%-10s %-6s %-6s %-8s mono_depth=%s/180\n",$1,$2,$3,$4,n}'
done
echo; grep -l -E "Traceback|Error|error:|CANCELLED|OUT_OF_MEMORY" "$VGAR_WORK"/logs/*.out 2>/dev/null | sed 's/^/log with errors: /' || true
grep -h "^DONE" "$VGAR_WORK"/logs/map-*.out 2>/dev/null | sort | uniq
