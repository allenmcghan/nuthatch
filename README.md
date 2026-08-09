# Nuthatch — An Open Single-Seat Ultralight

The Part 103 fleet is mostly 1980s designs. They are cheap, they are buildable in
a garage, and they hurt people in a small number of well-understood ways:

- **Ground loops**, because almost all of them are taildraggers
- **Stall-spin departures**
- **Nothing structural ahead of the pilot's legs**
- **Lap belts instead of harnesses**
- **A 7:1 glide**, so an engine failure leaves you very few fields to choose from

Every one of those is fixable for roughly 100 build hours and $1,900. Nuthatch is
what that looks like.

A single-seat wood-and-steel ultralight derived from the TEAM Sky Pup and Ison
Airbike. Plans, drawings, calculations, build log, and measured flight data all
live here. So do the mistakes.

**Named after the only bird that climbs down a tree headfirst.** Small, plain, and
does it backwards from everything else in the class.

**Status:** design phase. Nothing is drawn yet. See
[docs/open-questions.md](docs/open-questions.md) for what is still undefined.

---

## Design targets

| | |
|---|---|
| Cost, materials | under $15,000 |
| Build hours | under 750 |
| Takeoff roll | under 200 ft |
| Fits | a 22 ft garage and a 16 ft flatbed trailer |
| Part 103 | a compliant configuration off the same drawings |

## Current specification

Two configurations, one set of drawings. See [docs/specs.md](docs/specs.md).

| | EAB build | Part 103 build |
|---|---|---|
| Empty weight | 296 lb* | 250 lb* |
| Gross | 580 lb | 450 lb |
| Span / area | 31 ft / 130 ft² | same |
| Stall, flaps 40° | 28.4 mph | 22.9 kt |
| Takeoff roll | 140 ft | ~160 ft |
| Climb | 1,010 fpm | ~500 fpm |
| Glide ratio | 10.7 | 10.7 |
| Cruise | 55–60 mph | 55 kt limited |
| Range | ~150 mi | fuel limited |
| Engine | Hirth F-33, 28 hp | direct-drive, ~16 hp |
| Brakes | yes | yes |

\* The weight workbook omits rows (slats — since retired for flaps — and
cabane) that the build-log CSV carries; honest totals are ~308 / ~262 lb until
reconciled — see
[docs/trades/weight-scrub-103.md](docs/trades/weight-scrub-103.md), which also
works a single-build path to ~253 lb.

**Powerplant roadmap: gasoline first, hybrid second, electric third.** Electric,
when it comes, is an EAB-only path — a Part 103 all-electric build has 8 lb of
battery budget left after the airframe and drive, which is about four minutes.
Part 103 stays gasoline. Worked in
[docs/trades/pusher-vs-tractor.md](docs/trades/pusher-vs-tractor.md).

## Configuration

- Nose-mounted tractor propeller. Pusher was analysed and rejected for the
  gasoline aircraft: efficiency is a wash, and it does not close on balance
- Welded 4130 cockpit cage + single straight 6061 tail boom, all-wood
  cantilever wing, non-structural stringer-and-fabric cockpit fairing
- Constant chord, 3-piece removable wing, two bolts per cap per joint
- Douglas fir truss ribs, plywood D-tube leading edge, Oratex covered
- Aluminum tube spar caps with a wrapped sheet shear web
- Single-lever plain flaps, inboard ~60% span (0/25/40°, one-piece torque
  tube; replaced the fixed slats — [docs/trades/flaps.md](docs/trades/flaps.md))
- Two-axis control: elevator and rudder, roll via spoilerons and dihedral —
  one stick (pitch fore/aft, spoilerons lateral, twist-grip rudder), left-hand
  symmetric spoiler lever for glidepath; no rudder pedals
- Tricycle gear, castoring raked nose leg, trailing-arm mains with MTB
  coil-overs, bicycle hydraulic disc brakes
- Structural nose bow ahead of the pedals, rollover hoop, 5-point harness,
  energy-absorbing seat
- BRS hard points designed in

## What makes it different

**Glide.** 10.7:1 against roughly 7 or 8 for the aluminum-and-Dacron aircraft in
this class. That is a safety number as much as an efficiency one: engine-out you
reach twice the ground area.

**Crash structure.** Steel tube nose bow forward of the pedals and a rollover
hoop behind your head, so there is a survivable volume rather than fabric.

**No ground loop.** Tricycle gear with a steerable nose.

**No aileron spin mode.** Roll comes from spoilerons, which produce proverse yaw
and cannot be cross-controlled into a spin.

**A fail-safe autopilot path.** Spoilerons are single-acting with spring return,
so an autopilot servo has no failure mode that takes roll control away from the
pilot. See [Junco](https://github.com/allenmcghan/junco).

## Repository layout

```
docs/          design log, specs, load cases, open questions
docs/trades/   worked configuration trades, with the numbers
analysis/      spar sizing, performance, V-n diagram
drawings/      wing, fuselage, tail, gear, fittings
model/         quarter-scale RC validation aircraft
build-log/     measured weights against estimates, failures
flight-test/   Phase I plan and logged data
```

## The two files worth reading first

**[docs/design-log.md](docs/design-log.md)** — every decision and the number
behind it, including the configurations that lost and why. Drawings exist for a
dozen aircraft in this class. Reasoning does not.

**[build-log/measured-weights.csv](build-log/measured-weights.csv)** — estimated
against actual weight, part by part, as parts arrive. Every published weight in
this class is a claim. This one will be a measurement.

## Contributing

Corrections to the analysis are the most valuable contribution, especially on
spar sizing, flap geometry, and load cases. Open an issue with your numbers.

## License

Documentation and drawings: CERN-OHL-S v2 (see [LICENSE](LICENSE)).
Firmware and tooling, where present: MIT.

## Disclaimer

**This is an experimental amateur-built aircraft design published as a work in
progress. It has never been built or flown.**

Nothing here has been reviewed, certified, or validated by any authority. The
structural analysis is preliminary and every weight is an estimate until the
build log says otherwise. Slat geometry, spar sizing, and load cases are
explicitly unresolved.

If you build from this, **you are the manufacturer.** You are responsible for
your own structural analysis, your own airworthiness determination, and your own
decision to fly. No warranty of any kind is offered or implied, expressed or
otherwise, including fitness for any purpose.

Aircraft built to Part 103 require no pilot certificate. That does not make them
safe to fly without training. Get instruction.
