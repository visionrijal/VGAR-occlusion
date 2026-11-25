"""One ablation table from results/main and results/abl_*: 3 px band AP (mean over the 8 LOSO test scenes)
for soft opacity (B2, recomputed in every fold) and the U-Net, per condition and subset, with the number
of scenes where that U-Net beats the main run's B2.  Usage: python vgar/ablations.py -> results/ablations.md"""
import glob
import json
import os

import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(REPO, "results")
CONDS = [("rgbd", "RGB-D"), ("mono", "Depth Anything"), ("rgbonly", "RGB-only")]
ROWS = [
    ("main", "U-Net, all inputs (main)"),
    ("abl_feats_no_rgb", "no RGB input"),
    ("abl_feats_depth_only", "depth statistics only (no opacity)"),
    ("abl_feats_opacity_only", "opacity only (no depth statistics)"),
    ("abl_objK_grid", "objects: global 32-depth grid"),
    ("abl_objK_4", "objects: 4 slices per object"),
    ("abl_objK_8", "objects: 8 slices per object"),
    ("abl_K_4", "planes: 4-depth global grid"),
    ("abl_K_8", "planes: 8-depth global grid"),
    ("abl_K_16", "planes: 16-depth global grid"),
]


def load(tag, cond):
    out = {}
    for f in glob.glob(os.path.join(RES, tag, cond, "*.json")):
        r = json.load(open(f))
        out[r["test"]] = r
    return out


lines = ["# Ablations", "",
         "3 px boundary-band AP, mean over the 8 leave-one-scene-out test scenes. Each cell: soft opacity B2 "
         "(training-free, recomputed with that run's slices) / U-Net, and in brackets the number of scenes where "
         "that U-Net beats the main run's B2. Defaults: all 10 inputs, 32-depth global grid, 16 slices per object.", ""]
for subset in ["planes", "objects"]:
    lines += [f"## {subset}", "", "| Variant | " + " | ".join(n for _, n in CONDS) + " |", "|---|" + "---|" * len(CONDS)]
    for tag, name in ROWS:
        cells = []
        for c, _ in CONDS:
            R, M = load(tag, c), load("main", c)
            if len(R) < 8 or len(M) < 8:
                cells.append(f"{len(R)}/8 folds")
                continue
            ap = lambda r, m: r["results"][subset]["band3"][m]["AP"]
            b2 = np.mean([ap(r, "B2") for r in R.values()])
            u = np.mean([ap(r, "UNet") for r in R.values()])
            wins = sum(ap(R[s], "UNet") > ap(M[s], "B2") for s in R)
            cells.append(f"{b2:.3f} / {u:.3f} [{wins}/8]")
        lines.append(f"| {name} | " + " | ".join(cells) + " |")
    lines.append("")
open(os.path.join(RES, "ablations.md"), "w").write("\n".join(lines))
print("\n".join(lines))
