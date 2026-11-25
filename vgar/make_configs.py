"""Write SplatLoc configs for this machine: configs/templates/*.yaml with @WORK@ -> $VGAR_WORK,
into $SPLATLOC_DIR/configs/vgar/ (SplatLoc resolves inherit_from relative to its repo root)."""
import glob
import os

repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
work, splatloc = os.environ["VGAR_WORK"], os.environ["SPLATLOC_DIR"]
out = os.path.join(splatloc, "configs", "vgar")
os.makedirs(out, exist_ok=True)
files = sorted(glob.glob(os.path.join(repo, "configs", "templates", "*.yaml")))
for f in files:
    with open(f) as src, open(os.path.join(out, os.path.basename(f)), "w") as dst:
        dst.write(src.read().replace("@WORK@", work))
print(f"wrote {len(files)} configs to {out} (VGAR_WORK={work})")
