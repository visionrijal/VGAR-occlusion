"""Extract the 8 Replica scenes and SplatLoc's Replica generated files, then check frame counts.
Uses Python zipfile because `unzip` misreports these zip64 archives as zip bombs.
Usage: python vgar/extract_data.py <downloads_dir> <data_dir>"""
import os
import sys
import zipfile

SCENES = ["room_0", "room_1", "room_2", "office_0", "office_1", "office_2", "office_3", "office_4"]
dl, data = sys.argv[1], sys.argv[2]
rep = os.path.join(data, "replica")
os.makedirs(rep, exist_ok=True)

outer = zipfile.ZipFile(os.path.join(dl, "replica_semantic_nerf.zip"))
for s in SCENES:
    if os.path.isdir(os.path.join(rep, s, "Sequence_2", "rgb")):
        print(f"replica/{s}: already extracted")
        continue
    print(f"replica/{s}: extracting")
    with outer.open(f"Replica_Dataset/{s}.zip") as f:
        zipfile.ZipFile(f).extractall(rep)

gen = zipfile.ZipFile(os.path.join(dl, "splatloc-generated-files.zip"))
gdir = os.path.join(data, "generated")
names = [n for n in gen.namelist() if n.startswith("splatloc-generated-files/replica/")]
if os.path.isdir(os.path.join(gdir, "splatloc-generated-files", "replica", SCENES[-1])):
    print("generated/replica: already extracted")
else:
    print(f"generated/replica: extracting {len(names)} files")
    gen.extractall(gdir, members=names)

bad = 0
for s in SCENES:
    for seq in ["Sequence_1", "Sequence_2"]:
        for sub in ["rgb", "depth"]:
            n = len(os.listdir(os.path.join(rep, s, seq, sub)))
            if n != 900:
                print(f"!! {s}/{seq}/{sub}: {n} files (expected 900)"); bad += 1
    if not os.path.isdir(os.path.join(gdir, "splatloc-generated-files", "replica", s)):
        print(f"!! generated files missing for {s}"); bad += 1
print("CHECK FAILED" if bad else "CHECK OK: 8 scenes x 2 sequences x 900 RGB-D frames + generated files")
sys.exit(1 if bad else 0)
