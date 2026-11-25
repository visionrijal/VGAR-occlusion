# VGAR: learned real–virtual occlusion on 3DGS maps (CSC 792)

Code and cluster runbook. Data, maps and weights live outside git in `$VGAR_WORK`:
`/scratch/jacks.local/<user>/vgar` if you have a scratch directory, otherwise `~/vgar_work`
(see `cluster/config.sh`). Everything fits in the 100 GB home quota (~50 GB: envs 16 GB, data 15 GB,
maps <1 GB). Scratch has no quota but will get an expiration policy, so copy results back.

## Run on Innovator (all commands from the repo root, on the login node)

```bash
git clone <repo-url> vgar-occlusion && cd vgar-occlusion
bash cluster/setup_env.sh 2>&1 | tee setup_env.log     # once, ~30 min: envs, SplatLoc @ pinned commit + patch, CUDA build
tmux new -s fetch                                       # the download takes a while
bash cluster/fetch_data.sh 2>&1 | tee fetch_data.log    # once: Replica + SplatLoc generated files, ends with "CHECK OK"
bash cluster/submit_maps.sh                             # 1 depth job + 24 map jobs
bash cluster/status.sh                                  # repeat to watch progress
```

Each step ends with a check line. If one fails, send the log (`setup_env.log`, `fetch_data.log`,
or `$VGAR_WORK/logs/<job>.out`).

After `git pull`, rerun only what the change needs (the commit message will say).

## Copy maps back to the laptop

```bash
rsync -avP --include='*/' --include='point_cloud.ply' --include='config.yml' --exclude='*' \
  <cluster>:<VGAR_WORK>/outputs/ ~/Documents/VGAR/outputs_cluster/
```

## Layout

| Path | Contents |
|---|---|
| `vgar/` | our code: renderer helpers, Depth Anything depth, pilot scripts, data/config utilities |
| `configs/templates/` | SplatLoc configs for 8 scenes × 3 conditions (`@WORK@` is filled in by `make_configs.py`) |
| `third_party/` | pinned upstream commits and our SplatLoc patch (`depth_source`, `depth_loss`, optional tcnn) |
| `env/` | micromamba specs: `splatloc` (Py 3.7, PyTorch 1.12.1, CUDA 11.6), `dav2` (Py 3.11, PyTorch 2.3) |
| `cluster/` | setup, data fetch, Slurm jobs, status |
| `results/` | small CSV/JSON results only |

## Conditions

`rgbd`: SplatLoc as released (sensor depth for init + loss). `mono`: Depth Anything V2 metric depth
replaces sensor depth. `rgbonly`: no depth loss, noisy constant-depth init, no key-primitive regularization.
