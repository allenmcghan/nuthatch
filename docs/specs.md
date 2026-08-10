# Specification

**Rev H, entering final design.** One page, current numbers, with the source of
each. Where the repo carries two numbers for the same thing, both are here and
so is the reason.

Nothing has been built or flown. Every performance figure is a prediction and
every weight is an estimate.

---

## Geometry

Datum: **X aft from the propeller plane** (so X is the station number, inches),
**Y right**, **Z up**, **ground at z = 0** with the gear at static. Every
drawing, script and CAD file in the repo uses it.

| | | Source |
|---|---|---|
| Span | 31 ft | |
| Wing area | 130 ft² | |
| Chord | 50 in, constant | |
| Aspect ratio | 7.39 | |
| Section | NACA 4412 | [design-audit](trades/design-audit.md) addendum |
| Dihedral | 5° per side | `aero-model.py` |
| Washout | 2.5° | |
| Wing LE | sta 48; chord line z 58, underside z 55 | design-log §25 |
| Wing | 3-piece removable, two bolts per cap per joint | |
| Cage | sta 30 – 96, welded 4130 | [cockpit-cage](trades/cockpit-cage.md) |
| Main hoop | **sta 61.5** — front spar + rollover + CG on one frame | design-log §24 |
| Rear frame | sta 80.5 — rear spar, seat back, harness anchor | |
| Tail boom | sta 96 – 184, **3.50 × .049 4130, constant section** | design-log §24 |
| Tail | 30 ft² horizontal + 15 ft² vertical, elevator 45% chord ±25° | [trim-tail](trades/trim-tail.md) |
| Thrustline | z 40 | [landing-gear](trades/landing-gear.md) |
| Propeller | 60 in disc, two blades, wood | [propeller-blade-count](trades/propeller-blade-count.md) |
| Mains | sta 70.5, track 56 in | |
| Belly | 16 in AGL, seat 20 in | |

Full node and member table: [`analysis/frame.py`](../analysis/frame.py).
CAD exports: [`cad/`](../cad/).

## Limits

| | | Source |
|---|---|---|
| **Vne** | **62 mph, fleet-wide** | [common-airframe](trades/common-airframe.md) |
| VFE | 55 mph | [flaps](trades/flaps.md) |
| Gross, EAB | 580 lb | |
| Gross, Part 103 | 450 lb (stall gate caps it at 456) | [weight-scrub-103](trades/weight-scrub-103.md) |
| Structural pilot cap | 200 lb | |
| Ballast placard | 8 lb nose below a 135 lb pilot | |

Vne 62 is not a performance limit — it is the **load basis**. At 62 mph the
wing stalls before it can be overstressed, at every gross, with zero added
weight. Every load case in the repo depends on it.

## Performance, predicted

| | EAB | Part 103 | Source |
|---|---|---|---|
| Stall, flaps 40° | 28.4 mph | 22.9 kt | [flaps](trades/flaps.md) |
| Takeoff roll | ~140 ft | ~160 ft | |
| Climb | ~1,010 fpm | ~500 fpm | |
| **Glide ratio** | **12.4** | 12.4 | design-log §25 |
| Cruise | 55–60 mph | 55 kt limited | |
| Range | ~150 mi | fuel limited (5 gal) | |
| Engine | Hirth F-33, 28 hp | direct-drive ~16 hp, Thor-DS class | [weight-scrub-103](trades/weight-scrub-103.md) |

**On the glide number.** The repo quoted **10.7** for a long time. Rev G lowered
the wing onto the cabin roof and deleted the cabane, which took f from 4.84 to
3.68 ft² and L/D from 10.8 to **12.4**. If the §22 drag cleanup is adopted —
wheel pants on the mains, streamlined tube, footwell closeout — it goes to
**13.6**, but those are *proposed, not adopted*. **12.4 is the number of
record.** None of it is measured.

## Weight — two statements, deliberately not reconciled

| | EAB | Part 103 | Source |
|---|---|---|---|
| Workbook | 296 lb | 250 lb | `weight-cost-hours.xlsx` |
| Build-log CSV, honest | ~308 lb | ~262 lb | `measured-weights.csv` |
| Scrubbed single-build path | — | 253.2 lb → **247.7 lb** after the cabane deletion | design-log §25 |
| Part 103 limit | — | 254 lb | §103.1(e)(1) |

The workbook omits rows the CSV carries. **This is parked by owner decision**,
not resolved: the frame is being redrawn by hand, and reconciling a workbook
against superseded geometry buys nothing until that lands. Quote the source,
not a consensus.

Two things that *are* measured off the current geometry:

- **Steel frame, tube only: 48.4 lb** — 27.5 cage, 13.2 boom, 7.7 gear. No
  gussets, no fittings, no weld metal. [`cad/tube-schedule.csv`](../cad/tube-schedule.csv)
- **Enclosure kit: 14.4 lb gross** — glazing, frames, bead track, cutters,
  ducts, closeout. `analysis/glazing-ventilation.py`

## Configuration

- **Nose-mounted tractor.** Pusher analysed and rejected for the gasoline
  aircraft — [pusher-vs-tractor](trades/pusher-vs-tractor.md)
- **All-steel airframe**: welded 4130 cage + single straight 4130 boom, all-wood
  cantilever wing sitting directly on the cabin roof, no cabane, fabric over
  everything
- **The entire nose is glazed** — cowl joint at sta 22 back to the wing leading
  edge, down to the cage's lower longeron. **0.040 Lexan**; the engine cowl is
  the only opaque panel forward of the pilot. Two doors in 20 mil clear film
- **Ram-air NACA ducts**, closable for winter. Doors both sides are an **EAB kit
  item**; the 103 carries windshield and vents without them
- **Two-axis control**: elevator and rudder, roll via spoilerons and dihedral.
  One stick — pitch fore/aft, spoilerons lateral, **twist-grip rudder** — plus a
  left-hand symmetric spoiler lever. **No rudder pedals**
- **Single-lever plain flaps**, inboard ~60% span, 0/25/40°, one-piece torque
  tube (replaced the fixed slats)
- **Tricycle gear**: castoring raked nose leg with the wheel just aft of the
  prop disc, trailing-arm mains on MTB coil-overs, bicycle hydraulic discs
- **Crash structure**: nose bow ahead of the feet, rollover hoop, 5-point
  harness to the cage, mesh sling seat over a crushable bottom-out pad
- **BRS hard points** designed in
- Douglas fir truss ribs, plywood D-tube leading edge, **Oratex** covering,
  aluminium tube spar caps with a wrapped sheet shear web

## Visibility, measured

Ray-cast from the pilot's eye against the mesh — [`analysis/visibility.py`](../analysis/visibility.py).

| Sector | rev G | **rev H** |
|---|---|---|
| whole sphere | 40.0% | **61.3%** |
| forward hemisphere | 45.3% | 67.9% |
| the approach window | 48.9% | 74.7% |
| ahead and down, ±30° | 4.2% | **41.9%** |

Straight ahead is limited by the **engine**, not the glazing: the cowl crown
sits 1.8 in above the eye, so there is no over-the-nose depression angle at all.
See design-log §26 and the cowl-height item in
[open-questions](open-questions.md).

## Fleet rule

**One airframe, two bolt-on kits**, both balancing on the same wing position.
Aircraft #1 registers EAB by choice; aircraft #2 stays a pure Part 103 for a
105 lb pilot, and is **deferred until #1 proves out**. Glazing is a kit item
either way — the EAB takes the Lexan nose, the 103 takes film in the same frame
and the same bead track, because at rev H the 103 cannot afford the Lexan.

## What this page is not

It is not a build standard. **No structural member has been sized against a
load case**, no rollover load basis has been chosen, and the frame is currently
in six disconnected pieces. See [open-questions.md](open-questions.md) — the
four items at the top of it gate everything here.
