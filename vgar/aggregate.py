"""Summarize LOSO results: mean ± std over test scenes, plus a paired Wilcoxon test of the U-Net against
the best baseline over (scene, view) units. Usage: python vgar/aggregate.py <tag>   (e.g. main)
Writes results/<tag>/summary.md and results/<tag>/summary.csv."""
import csv
import glob
import json
import os
import sys

import numpy as np
from scipy.stats import wilcoxon

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tag = sys.argv[1] if len(sys.argv) > 1 else "main"
base = os.path.join(REPO, "results", tag)
CONDS = ["rgbd", "mono", "rgbonly"]
COND_NAME = {"rgbd": "RGB-D", "mono": "RGB + Depth Anything V2", "rgbonly": "RGB-only"}
ORDER = ["B0", "B1", "B2", "LR", "MLP", "UNet"]

runs = {c: [json.load(open(f)) for f in sorted(glob.glob(os.path.join(base, c, "*.json")))] for c in CONDS}
lines, rows = [f"# Results: {tag}", ""], []
for c in CONDS:
    R = runs[c]
    if not R:
        continue
    lines += [f"## {COND_NAME[c]} ({len(R)} test scenes: {', '.join(r['test'] for r in R)})", ""]
    for subset in ["all", "planes", "objects"]:
        lines += [f"**{subset}** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)", "",
                  "| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |",
                  "|---|---|---|---|---|---|---|---|---|"]
        for m in ORDER:
            def stat(region, key):
                v = [r["results"].get(subset, {}).get(region, {}).get(m, {}).get(key) for r in R]
                v = [x for x in v if x is not None]
                return (np.mean(v), np.std(v), len(v)) if v else None
            cells = []
            for region, key in [("all", "AP"), ("band3", "AP"), ("band5", "AP"), ("band3", "F1"),
                                ("band3", "missed_occ"), ("band3", "false_occ"), ("all", "brier"), ("all", "ece")]:
                s = stat(region, key)
                cells.append("-" if s is None else f"{s[0]:.3f} ± {s[1]:.3f}")
                if s is not None:
                    rows.append(dict(cond=c, subset=subset, method=m, region=region, metric=key,
                                     mean=round(s[0], 4), std=round(s[1], 4), n_scenes=s[2]))
            if any(x != "-" for x in cells):
                lines.append(f"| {m} | " + " | ".join(cells) + " |")
        lines.append("")
    # paired test: U-Net vs the better baseline, per (scene, view) band-3 AP
    pv = [(r["test"], v, d) for r in R for v, d in r["per_view_band3_AP"].items()]
    if pv and all("UNet" in d for _, _, d in pv):
        means = {m: np.mean([d[m] for _, _, d in pv]) for m in ("B0", "B2")}
        best = max(means, key=means.get)
        a, b = np.array([d["UNet"] for _, _, d in pv]), np.array([d[best] for _, _, d in pv])
        stat, pval = wilcoxon(a, b)
        lines += [f"Wilcoxon signed-rank, U-Net vs {best} (per-view band-3 AP, n = {len(a)} views): "
                  f"median difference {np.median(a - b):+.4f}, U-Net better in {(a > b).mean():.0%} of views, p = {pval:.2e}", ""]
    rt = [r for r in R if "unet_ms_per_frame" in r["info"]]
    if rt:
        r0 = rt[0]
        lines += [f"Runtime on {r0['feature_ms']['gpu']}: stats pass {r0['feature_ms']['stats_pass']} ms, "
                  f"{r0['feature_ms']['per_slice']} ms per depth slice, U-Net {np.mean([r['info']['unet_ms_per_frame'] for r in rt]):.2f} ms "
                  f"per 640x480 frame ({r0['info']['unet_params']:,} parameters).", ""]

os.makedirs(base, exist_ok=True)
open(os.path.join(base, "summary.md"), "w").write("\n".join(lines))
with open(os.path.join(base, "summary.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["cond"])
    w.writeheader(); w.writerows(rows)
print("\n".join(lines))
