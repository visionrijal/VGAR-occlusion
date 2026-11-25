# Sourced by every cluster script and job. Run all commands from the repo root.
# Override any of these by exporting them before you run a script.
export REPO=${REPO:-$(pwd)}
_user=${USER%%@*}
# Innovator: home has a 100 GB quota; scratch (/scratch/jacks.local/<user>) exists only if requested,
# has no quota, but will get a data-expiration policy. Use scratch when it exists, else home (~50 GB needed).
if [ -z "${VGAR_WORK:-}" ]; then
  _scr=/scratch/jacks.local/$_user
  if [ -d "$_scr" ] && [ -w "$_scr" ]; then VGAR_WORK=$_scr/vgar; else VGAR_WORK=$HOME/vgar_work; fi
fi
export VGAR_WORK
export SPLATLOC_DIR=$VGAR_WORK/src/SplatLoc
export DAV2_DIR=$VGAR_WORK/src/Depth-Anything-V2
export VGAR_CKPT=$VGAR_WORK/checkpoints
export MAMBA_ROOT_PREFIX=${MAMBA_ROOT_PREFIX:-$HOME/micromamba}
export MAMBA_EXE=$HOME/.local/bin/micromamba
export SLURM_ACCOUNT=${SLURM_ACCOUNT:-337661}
export SLURM_PARTITION=${SLURM_PARTITION:-gpu}
# Innovator GPU nodes: 14 x (2 x A100 80GB) -> compute capability 8.0
export TORCH_CUDA_ARCH_LIST=${TORCH_CUDA_ARCH_LIST:-"8.0"}
export TQDM_MININTERVAL=60   # keep progress bars from flooding Slurm logs
SCENES=(room_0 room_1 room_2 office_0 office_1 office_2 office_3 office_4)
CONDS=(rgbd mono rgbonly)

activate() {   # activate <splatloc|dav2>
  local _u=$-; set +u
  eval "$("$MAMBA_EXE" shell hook -s bash)"
  micromamba activate "$1"
  if [ "$1" = splatloc ]; then
    export CUDA_HOME=$CONDA_PREFIX
    export CC=$CONDA_PREFIX/bin/x86_64-conda-linux-gnu-gcc CXX=$CONDA_PREFIX/bin/x86_64-conda-linux-gnu-g++
    export PATH=$CONDA_PREFIX/bin:$PATH
    export LIBRARY_PATH=$CONDA_PREFIX/lib:$CONDA_PREFIX/lib/stubs:${LIBRARY_PATH:-}
    export CPATH=$CONDA_PREFIX/include:${CPATH:-}
  fi
  [[ $_u == *u* ]] && set -u; return 0
}
