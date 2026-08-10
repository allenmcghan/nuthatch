# analysis

The models. Every number quoted anywhere in this repo comes from one of these,
and every drawing, render and CAD file regenerates from them.

Most take an optional scratch-directory argument (where the intermediate mesh
JSON is written); with no argument they use the current directory.

## The source of truth

| | |
|---|---|
| **`frame.py`** | **the steel frame as a node table, a member table and a stock table.** Not a drawing — a design. Run it directly for the tube schedule, the joint angles and the connectivity check. Everything structural reads it |
| `geometry-mesh.py` | builds the whole aircraft: wing, tail, pod, glazing, cowl, boom, gear, plus the frame from `frame.py`. Writes `model/nuthatch.stl`, the mesh JSON and the general-arrangement sheet |

## Analysis

| | |
|---|---|
| `aero-model.py` | AeroSandbox + NeuralFoil: CLmax, Oswald efficiency, dihedral derivatives |
| `visibility.py` | ray-cast from the pilot's eye — what the pilot can see, and what blocks it |
| `trim-tail.py` | tail sizing, trim, stick force, flare authority, rudder-roll rate |
| `weight-scrub.py` | line-by-line weight scrub against the Part 103 cap |
| `common-airframe.py` | the two-configuration fleet: balance, Vne, ballast |
| `gear-design.py` | stance, stroke, drop loads, nose-over protection |
| `flaps.py` | flap increment, VFE, stall margin |
| `cage-design.py` | all-steel boom trade, wing attach loads, cage station convergence |
| `enclosed-cockpit.py` | recline, CG, wing height, drag, the rev G ledger |
| `glazing-ventilation.py` | glazing weight (measured off the mesh), tautness, ram-air flow, wind chill, egress, the enclosure ledger |
| `twist-grip-rudder.py` | wrist torque, horn balance, gearing |
| `sling-seat.py` | sling tension, crush pad, proof load |
| `borrowed-optimizations.py` | VGs, gap seals, drag cleanup, ground-adjustable prop |
| `fly-by-wire.py` | servo weights, hardover authority, the case against |
| `fuselage-boom.py` | **superseded in part** — boom sizing method stands, its aluminium answer does not |

## Output

| | |
|---|---|
| `cad-export.py` | writes `cad/` — DXF, AutoCAD script, tube schedule. `--from-dxf FILE` reads an edited DXF back |
| `cad-sheets.py` | the dimensioned drawing sheets, GA-001 / LG-001 / CP-001 / ST-001 |
| `render-hero.py` | shaded renderings, including the pilot's-eye view |
| `render-kxnx.py` | the takeoff renderings |

## Regeneration order

`frame.py` → `geometry-mesh.py` → everything else. If you change the frame or
the pod, run it in that order; the mesh JSON is what the CAD sheets, the
renderers and the visibility analysis all read.

```
python3 analysis/frame.py
python3 analysis/geometry-mesh.py
python3 analysis/cad-export.py
python3 analysis/cad-sheets.py
python3 analysis/visibility.py
python3 analysis/render-hero.py
```
