# CAD

The steel frame, exported for a CAD package. **Everything in this folder is
generated** — `analysis/frame.py` is the source of truth, and
`analysis/cad-export.py` writes these files from it.

Units are **inches**. Datum is the aircraft datum used everywhere else in the
repo: **X aft from the propeller plane** (so X is the station number), **Y
right**, **Z up**, **ground at z = 0** with the gear at static. Set your CAD
units to inches and it lands in the right place with no scaling.

| File | What it is |
|---|---|
| `nuthatch-frame-3d.dxf` | 3D wireframe, every tube centreline, on layers by structure group, with node markers, node labels and datum/station reference lines. **This is the one to open and start moving.** |
| `nuthatch-views-2d.dxf` | Side / top / front orthographic projections on one flat sheet, with a station grid and waterlines. For drafting, not for editing. |
| `nuthatch-frame.scr` | An AutoCAD script that draws the same wireframe with `LINE` commands. For when a DXF import argues with you. |
| `tube-schedule.csv` | Cut list: every member, stock, centreline length, weight, and the tightest joint angle at each end. |
| `nodes.csv` | Every node, mirrored, with the members that land on it. |

`model/nuthatch.stl` alongside is the full aircraft as a mesh — good for
visualising and for checking clearances, useless for editing.

## Two things these files are not

**They are not a fabrication drawing.** No member has been sized against a
load case. `docs/open-questions.md` carries *"cage member sizing + a rollover
load basis"* as unresolved and no rollover standard has been chosen. The tube
sizes here carry the right geometry and a plausible weight and nothing more.
**Do not cut steel from them.**

**Lengths are centreline to centreline.** Deduct for the fishmouth at each
end. The `min_joint_angle` columns are there because that is what sets the
notch — anything much under 20° is a bad joint however well you cope it.

## The frame is currently in six disconnected pieces

Run `python3 analysis/frame.py`. Drawn as overlapping cylinders the cage looks
solid; drawn as a graph it is not. Only the 14-node cage box is welded
together. The rear frame, the tail boom and all three gear legs are islands,
and several nodes sit two to three inches away from the member they are
supposed to land on — close enough to read as a joint on a drawing, not close
enough to be one in steel.

That is not a bug in the exporter. It is the actual state of the design, and
it is the first thing worth fixing. See `docs/open-questions.md`.

## Which CAD

**If you want to move geometry and get a cut list back: Onshape, free plan.**
Parametric, runs in a browser, and its **Frames** tool does exactly this job —
sweep tube profiles down a wireframe and it generates a cut list with miter
angles. The free tier requires documents to be public, which for a CERN-OHL-S
project is where the CAD should be anyway. Import `nuthatch-frame-3d.dxf` as a
sketch/curve set, then apply frame profiles to it.

**If you want it offline and open source: FreeCAD.** Matches the licence
posture of the repo. Weaker weldment story than Onshape but it will do it.

**AutoCAD works for what you asked for.** The 3D DXF is native LINE geometry
on sensible layers; move endpoints, add members, delete members. What AutoCAD
will not give you is a cut list or a weight — which is what the round trip
below is for.

**If you have access to SolidWorks, its Weldments module is still the best
tool for this specific job** — structural members along a 3D sketch, automatic
cut list with lengths and end angles. It is the only one of these that was
designed for tube frames from the start.

## Round trip

Edit the wireframe in CAD, save as DXF, then:

```
python3 analysis/cad-export.py --from-dxf path/to/edited.dxf
```

It parses the `LINE` entities, matches each endpoint to the nearest known
node, and reports what moved, what is new and what vanished — then prints a
node table in `frame.py` format to paste back in.

It reads **positions only.** Added members, deleted members and changed tube
sizes have to go into `_M` by hand: a DXF line has no way to tell you which
stock it is meant to be.

Once `frame.py` is updated, re-run and everything downstream follows:

```
python3 analysis/frame.py                    # weight, joints, connectivity
python3 analysis/cad-export.py               # these files
python3 analysis/geometry-mesh.py            # STL + mesh + general arrangement
python3 analysis/cad-sheets.py               # drawing sheets
python3 analysis/visibility.py               # what the pilot can see
python3 analysis/render-hero.py              # renders
```

Keep `frame.py` as the source of truth. If the CAD becomes the master, the
weights, the drawings and the visibility numbers quietly stop matching the
aeroplane.
