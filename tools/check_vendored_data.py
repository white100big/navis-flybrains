#!/usr/bin/env python3
"""Check that an *installed* flybrains vendors every file it needs at runtime.

Run this from outside the repo root, otherwise it inspects the source tree
(which always looks complete) rather than the installed package::

    cd /tmp && python3 /path/to/repo/tools/check_vendored_data.py

Versions 0.6.0 to 0.6.2 shipped to PyPI without their elastix parameter files
and/or without any of their landmark CSVs; the publish workflow did not notice
because its import test ran from the repo root and picked up the source tree.
"""

import os
import pathlib
import sys

import flybrains
from flybrains.core import data_filepath
from flybrains.templates import mesh_filepath

data_filepath = pathlib.Path(data_filepath)
mesh_filepath = pathlib.Path(mesh_filepath)

if pathlib.Path(__file__).resolve().parent.parent in pathlib.Path(
    flybrains.__file__
).resolve().parents:
    sys.exit(
        f"Refusing to check the source tree at {flybrains.__file__}. "
        "Run this from a directory outside the repo so that the installed "
        "package is picked up instead."
    )

missing = []

# Every landmark/parameter file referenced from core.py, plus the template
# metadata. Meshes are checked against template_meta.json below.
for rel in [
    "template_meta.json",
    "Aedes_mirror_landmarks_nm.csv",
    "BANC_mirror_landmarks_nm.csv",
    "FAFB14_maleCNS_landmarks.csv",
    "FAFB14_mirror_landmarks.csv",
    "FAFB14_symmetrize_landmarks_nm.csv",
    "FANC_mirror_landmarks.csv",
    "FLYWIRE_maleCNS_landmarks.csv",
    "FLYWIRE_mirror_landmarks.csv",
    "FLYWIRE_symmetrize_landmarks_nm.csv",
    "JRCFIB2018F_mirror_landmarks.csv",
    "JRCFIB2022M_plotting_landmarks.csv",
    "MANC_FANC_landmarks_nm.csv",
    "MANC_mirror_landmarks.csv",
    "maleCNS_BANC_landmarks_nm.csv",
    "maleCNS_mirror_landmarks_nm.csv",
    "lm-em-landmarks_v14.csv",
    "BANC_JRC2018F/BANC_to_template.txt",
    "BANC_JRC2018F/template_to_BANC.txt",
    "BANC_JRC2018F/0_manual_affine.txt",
    "BANC_JRC2018F/1_elastix_affine.txt",
    "BANC_JRC2018F/2_elastix_Bspline_coarse.txt",
    "BANC_JRC2018F/3_elastix_Bspline_fine.txt",
    "BANC_JRCVNC2018F/BANC_to_template.txt",
    "BANC_JRCVNC2018F/template_to_BANC.txt",
    "BANC_JRCVNC2018F/0_manual_affine.txt",
    "BANC_JRCVNC2018F/1_elastix_affine.txt",
    "BANC_JRCVNC2018F/2_elastix_Bspline_coarse.txt",
    "BANC_JRCVNC2018F/3_elastix_Bspline_fine.txt",
    "FANC_JRCVNC2018F/TransformParameters.FixedFANC.txt",
    "FANC_JRCVNC2018F/TransformParameters.FixedTemplate.affine.txt",
    "FANC_JRCVNC2018F/TransformParameters.FixedTemplate.Bspline.txt",
]:
    if not (data_filepath / rel).is_file():
        missing.append(f"flybrains/data/{rel}")

# Meshes: force every template to load its mesh(es) rather than hard-coding a
# list, so that newly added templates are covered automatically.
for name in dir(flybrains):
    tmp = getattr(flybrains, name)
    if not isinstance(tmp, flybrains.templates.FlyTemplateBrain):
        continue
    for prop in ("mesh", "mesh_whole_brain", "mesh_brain", "mesh_vnc"):
        if not isinstance(getattr(type(tmp), prop, None), property):
            continue
        try:
            getattr(tmp, prop)
        except FileNotFoundError as e:
            fp = pathlib.Path(e.filename or "?")
            missing.append(f"flybrains/meshes/{fp.name} (for {name}.{prop})")
        except ValueError:
            # Some templates legitimately ship without a mesh.
            pass

if missing:
    print(f"Checked installation at {os.path.dirname(flybrains.__file__)}")
    print(f"{len(missing)} vendored file(s) MISSING:")
    for m in missing:
        print(f"  {m}")
    sys.exit(1)

print(f"OK: all vendored data files present in {os.path.dirname(flybrains.__file__)}")
