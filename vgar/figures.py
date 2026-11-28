"""Figures for the report and slides, from results/*.json (and local features for the qualitative figure).
Usage (splatloc env): python vgar/figures.py [main|gain|ablation|qual|all]   -> figures/*.pdf + *.png

Colours: validated categorical slots (blue, orange, aqua) in fixed order B0, B2, U-Net; every series
also has its own marker shape and a legend, since orange and aqua are below 3:1 contrast on white."""
import glob
import json
import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(REPO, "results")
OUT = os.path.join(REPO, "figures")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.family": "serif", "font.serif": ["Liberation Serif", "Times New Roman", "DejaVu Serif"],
                     "font.size": 8, "axes.titlesize": 8.5, "axes.labelsize": 8, "legend.fontsize": 7.5,
                     "xtick.labelsize": 7.5, "ytick.labelsize": 7.5, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.linewidth": 0.6, "xtick.major.width": 0.6,
                     "ytick.major.width": 0.6, "lines.linewidth": 1.4})
INK, GRID = "#222222", "#dddddd"
METHOD = {"B0": ("Depth test (B0)", "#257de0", "o"), "B2": ("Soft opacity (B2)", "#f47230", "s"),
          "UNet": ("U-Net", "#00b894", "^")}
CONDS = [("rgbd", "RGB-D"), ("mono", "Depth Anything"), ("rgbonly", "RGB-only")]


def load(tag, cond):
    return {json.load(open(f))["test"]: json.load(open(f)) for f in sorted(glob.glob(os.path.join(RES, tag, cond, "*.json")))}


def quality(cond):
    return {json.load(open(f))["scene"]: json.load(open(f))["quality"]
            for f in glob.glob(os.path.join(RES, "maps", cond, "*.json"))}


def save(fig, name):
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"), dpi=300, bbox_inches="tight")
    plt.close(fig)
    print("wrote", os.path.join(OUT, name + ".pdf"))


def grid(ax, axis="y"):
    ax.grid(axis=axis, color=GRID, lw=0.5)
    ax.set_axisbelow(True)


def fig_main():
    """Band-3 AP per method and map type: per-scene dots (faint) and the mean over 8 scenes (bold)."""
    fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.4), sharey=True)
    for ax, subset in zip(axes, ["planes", "objects"]):
        for ci, (c, cname) in enumerate(CONDS):
            R = load("main", c)
            for mi, m in enumerate(["B0", "B2", "UNet"]):
                name, col, mk = METHOD[m]
                v = np.array([r["results"][subset]["band3"][m]["AP"] for r in R.values()])
                x = ci + (mi - 1) * 0.24
                ax.scatter(np.full(len(v), x) + np.linspace(-0.05, 0.05, len(v)), v, s=9, color=col, alpha=0.35,
                           marker=mk, lw=0, zorder=2)
                ax.plot([x - 0.09, x + 0.09], [v.mean()] * 2, color=col, lw=2.2, solid_capstyle="round", zorder=3)
                ax.scatter([x], [v.mean()], s=26, color=col, marker=mk, edgecolor="white", lw=0.8, zorder=4,
                           label=name if ci == 0 else None)
        ax.set_xticks(range(3)); ax.set_xticklabels([n for _, n in CONDS])
        ax.set_title({"planes": "Depth planes", "objects": "Placed objects"}[subset], color=INK)
        grid(ax)
    axes[0].set_ylabel("AP within 3 px of the occlusion boundary")
    axes[0].legend(loc="lower left", frameon=False, handletextpad=0.3)
    fig.tight_layout()
    save(fig, "fig_main_band_ap")


def fig_gain():
    """Gain of each step against the map's depth error, one point per (scene, map type)."""
    fig, ax = plt.subplots(figsize=(3.6, 2.5))
    shapes = {"rgbd": "o", "mono": "s", "rgbonly": "^"}
    for c, cname in CONDS:
        R, Q = load("main", c), quality(c)
        for key, col, lab in [("soft", "#f47230", "Soft opacity − depth test"), ("unet", "#00b894", "U-Net − soft opacity")]:
            xs, ys = [], []
            for s, r in R.items():
                a = r["results"]["all"]["band3"]
                xs.append(Q[s]["depth_med_cm"])
                ys.append(100 * ((a["B2"]["AP"] - a["B0"]["AP"]) if key == "soft" else (a["UNet"]["AP"] - a["B2"]["AP"])))
            ax.scatter(xs, ys, s=18, color=col, marker=shapes[c], edgecolor="white", lw=0.5,
                       label=f"{lab}" if c == "rgbd" else None, zorder=3)
    ax.axhline(0, color=INK, lw=0.6)
    ax.set_xscale("log"); ax.set_xticks([1, 2, 5, 10, 20, 50]); ax.set_xticklabels(["1", "2", "5", "10", "20", "50"])
    ax.set_xlabel("Map median depth error (cm, log scale)")
    ax.set_ylabel("AP gain, 3 px band (points)")
    grid(ax, "both")
    for t, (c, cname) in zip(["o", "s", "^"], CONDS):
        ax.scatter([], [], marker=t, color="#888888", s=14, label=cname)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, loc="upper left", bbox_to_anchor=(1.02, 1.0), frameon=False, handletextpad=0.3, ncol=1)
    fig.tight_layout()
    save(fig, "fig_gain_vs_depth_error")


def fig_ablation():
    """Left: soft opacity on objects vs how A(p, z_v) is computed. Right: U-Net input ablation."""
    fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.4))
    ax = axes[0]
    variants = [("abl_objK_grid", "global\ngrid"), ("abl_objK_4", "4"), ("abl_objK_8", "8"), ("abl_objK_16", "16"),
                ("main", "exact\n(1 pass)")]
    cmark = {"rgbd": ("#257de0", "o"), "mono": ("#f47230", "s"), "rgbonly": ("#00b894", "^")}
    for c, cname in CONDS:
        ys = []
        for tag, _ in variants:
            R = load(tag, c)
            ys.append(np.mean([r["results"]["objects"]["band3"]["B2"]["AP"] for r in R.values()]) if len(R) == 8 else np.nan)
        col, mk = cmark[c]
        ax.plot(range(len(variants)), ys, color=col, marker=mk, ms=4.5, mec="white", mew=0.6, label=cname)
    ax.set_xticks(range(len(variants))); ax.set_xticklabels([v for _, v in variants])
    ax.set_xlabel("Slices per object used for A(p, z_v)")
    ax.set_ylabel("Soft opacity AP, objects, 3 px band")
    ax.set_title("Exact per-pixel depth matters for objects", color=INK)
    grid(ax)
    ax = axes[1]
    rows = [("main", "all inputs"), ("abl_feats_no_rgb", "no RGB"), ("abl_feats_opacity_only", "opacity only"),
            ("abl_feats_depth_only", "depth stats only")]
    for ci, (c, cname) in enumerate(CONDS):
        col, mk = cmark[c]
        b2 = np.mean([r["results"]["all"]["band3"]["B2"]["AP"] for r in load("main", c).values()])
        for ri, (tag, _) in enumerate(rows):
            R = load(tag, c)
            if len(R) < 8:
                continue
            u = np.mean([r["results"]["all"]["band3"]["UNet"]["AP"] for r in R.values()])
            ax.scatter([100 * (u - b2)], [ri + (ci - 1) * 0.22], color=col, marker=mk, s=24, edgecolor="white", lw=0.6,
                       label=cname if ri == 0 else None, zorder=3)
    ax.axvline(0, color=INK, lw=0.6)
    ax.set_yticks(range(len(rows))); ax.set_yticklabels([n for _, n in rows]); ax.invert_yaxis()
    ax.set_xlabel("U-Net − soft opacity, AP points (3 px band)")
    ax.set_title("U-Net inputs", color=INK)
    grid(ax, "x")
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, loc="upper center", ncol=3, frameon=False, bbox_to_anchor=(0.5, 1.07), handletextpad=0.3)
    fig.tight_layout()
    save(fig, "fig_ablations")


def fig_qual(scene="room_0", cond="rgbd", n_examples=3):
    """Composites for objects with the largest disagreement between B0 and B2 near the boundary."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from data import SceneData
    sd = SceneData(cond, scene)
    cands = []
    for s in sd.samples:
        if s[0] != "object":
            continue
        b = sd.build(s, band_px=(3,))
        v = b["valid"] & b["band3"]
        if v.sum() < 300:
            continue
        hard0 = b["score_b0"] > 0
        err0 = ((hard0 != b["y"]) & v).sum() / v.sum()
        err2 = (((b["feats"]["A_zv"] > 0.5) != b["y"]) & v).sum() / v.sum()
        cands.append((err0 - err2, s))
    cands.sort(key=lambda t: -t[0])
    picks = [s for _, s in cands[:n_examples]]
    fig, axes = plt.subplots(n_examples, 4, figsize=(6.6, 1.32 * n_examples + 0.25))
    obj_col = np.array([0.96, 0.45, 0.19])
    for ri, (row, s) in enumerate(zip(np.atleast_2d(axes), picks)):
        b = sd.build(s)
        rgb = sd.rgb[s[1]].transpose(1, 2, 0).astype(np.float32) / 255
        sil = b["feats"]["M_v"] > 0
        ys, xs = np.nonzero(sil)
        cy, cx = int(ys.mean()), int(xs.mean())
        h = max(60, int(1.3 * max(np.ptp(ys), np.ptp(xs)) / 2))
        y0, y1 = max(0, cy - h), min(sd.H, cy + h); x0, x1 = max(0, cx - h), min(sd.W, cx + h)
        shade = 0.75 + 0.25 * (1 - (b["feats"]["z_v"] * 3 - (b["feats"]["z_v"] * 3)[sil].min()) / max(np.ptp((b["feats"]["z_v"] * 3)[sil]), 1e-3))
        objimg = obj_col[None, None] * np.clip(shade, 0.5, 1)[..., None]
        gt_vis = sil & ~b["y"]
        def comp(vis_w):
            return rgb * (1 - vis_w[..., None]) + objimg * vis_w[..., None]
        panels = [("Ground truth", comp(gt_vis.astype(np.float32)), None),
                  ("Depth test (B0)", comp((sil & (b["score_b0"] <= 0)).astype(np.float32)),
                   sil & ((b["score_b0"] > 0) != b["y"]) & b["valid"]),
                  ("Soft opacity (B2), A ≥ 0.5", comp((sil & (b["feats"]["A_zv"] < 0.5)).astype(np.float32)),
                   sil & ((b["feats"]["A_zv"] >= 0.5) != b["y"]) & b["valid"]),
                  ("Soft opacity, blended", comp(np.where(sil, 1 - b["feats"]["A_zv"], 0).astype(np.float32)), None)]
        for ax, (title, img, err) in zip(row, panels):
            im = img[y0:y1, x0:x1].copy()
            if err is not None:
                e = err[y0:y1, x0:x1]
                im[e] = [0.85, 0.0, 0.85]
            ax.imshow(np.clip(im, 0, 1), interpolation="nearest")
            ax.set_xticks([]); ax.set_yticks([])
            for sp in ax.spines.values():
                sp.set_visible(False)
            if ri == 0:
                ax.set_title(title, color=INK)
    fig.text(0.5, 0.0, "Magenta: pixels whose hidden/visible decision is wrong. "
             f"{scene}, {cond}; objects where the depth test and soft opacity disagree most.",
             ha="center", va="top", fontsize=7, color="#444444")
    fig.tight_layout()
    save(fig, f"fig_qualitative_{scene}_{cond}")


def fig_finetune():
    """Soft opacity and U-Net on the original map vs. depth fine-tune (control) vs. occlusion fine-tune.
    Thin lines: one scene each; thick: mean over 8 scenes. x labels carry the map's mean depth error."""
    fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.5), sharey=True)
    versions = [("", "original"), ("_ctl", "depth\nfine-tune"), ("_occ", "occlusion\nfine-tune")]
    for ax, (base, bname) in zip(axes, [("rgbd", "RGB-D maps"), ("mono", "Depth Anything maps")]):
        labels = []
        for vi, (suf, vname) in enumerate(versions):
            Q = quality(base + suf)
            labels.append(f"{vname}\n{np.mean([q['depth_med_cm'] for q in Q.values()]):.1f} cm")
        for m in ["B2", "UNet"]:
            name, col, mk = METHOD[m]
            per = np.array([[load("main", base + suf)[sc]["results"]["all"]["band3"][m]["AP"] for suf, _ in versions]
                            for sc in sorted(load("main", base))])
            for row in per:
                ax.plot(range(3), row, color=col, lw=0.6, alpha=0.35, zorder=2)
            ax.plot(range(3), per.mean(0), color=col, lw=2.2, marker=mk, ms=5.5, mec="white", mew=0.7, label=name, zorder=3)
        ax.set_xticks(range(3)); ax.set_xticklabels(labels)
        ax.set_xlim(-0.3, 2.3)
        ax.set_title(bname, color=INK)
        grid(ax)
    axes[0].set_ylabel("AP within 3 px of the occlusion boundary")
    axes[0].legend(loc="lower right", frameon=False, handletextpad=0.3)
    fig.tight_layout()
    save(fig, "fig_finetune")


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    for name, f in [("main", fig_main), ("gain", fig_gain), ("ablation", fig_ablation), ("qual", fig_qual),
                    ("finetune", fig_finetune)]:
        if which in (name, "all"):
            f()
