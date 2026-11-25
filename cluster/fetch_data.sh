#!/bin/bash
# Download + extract Replica (Semantic-NeRF release) and SplatLoc's generated files (~11 GB download,
# ~20 GB extracted). Run on the LOGIN node inside tmux/screen, it takes a while:
#   bash cluster/fetch_data.sh 2>&1 | tee fetch_data.log
# If a download fails, copy the zips from the laptop instead and rerun this script:
#   rsync -avP ~/Documents/VGAR/data/downloads/ <cluster>:$VGAR_WORK/downloads/
set -euo pipefail
source cluster/config.sh
D=$VGAR_WORK/downloads; mkdir -p "$D"
REPLICA_URL='https://www.dropbox.com/scl/fo/puh6djua6ewgs0afsswmz/AGudMbll0n0v_iADmqrrRds?rlkey=ep5495umv628y2sk8hvnh8msc&dl=1'
GEN_ID=1MkZvLV6DakUHEE0RHplJqxa-iuUWn59z
activate dav2

if [ ! -s "$D/replica_semantic_nerf.zip" ]; then
  echo "== downloading Replica (6.3 GB)"
  curl -L --fail --retry 5 -C - -o "$D/replica_semantic_nerf.zip.part" "$REPLICA_URL"
  mv "$D/replica_semantic_nerf.zip.part" "$D/replica_semantic_nerf.zip"
fi
if [ ! -s "$D/splatloc-generated-files.zip" ]; then
  echo "== downloading SplatLoc generated files (4.6 GB)"
  gdown --continue "$GEN_ID" -O "$D/splatloc-generated-files.zip"
fi
ls -la "$D"
python vgar/extract_data.py "$D" "$VGAR_WORK/data"
# On home (100 GB quota) the zips are not worth keeping; they can be downloaded again.
case "$VGAR_WORK" in "$HOME"*) [ "${KEEP_ZIPS:-0}" = 1 ] || { rm -f "$D"/*.zip; echo "== removed zips to save ~11 GB"; } ;; esac
du -sh "$VGAR_WORK" "$MAMBA_ROOT_PREFIX" 2>/dev/null
echo "== data ready. Next: bash cluster/submit_maps.sh"
