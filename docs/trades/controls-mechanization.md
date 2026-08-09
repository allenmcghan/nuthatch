# Controls Mechanization: One Stick, Twist-Grip Rudder, No Pedals

**Owner decision 2026-08-09.** The control scheme is:

| Control | Motion | Function |
|---|---|---|
| Stick | fore/aft | elevator |
| Stick | left/right | spoilerons, differential (roll) |
| Stick grip | **twist** | **rudder** |
| Left-hand lever | pull | **both spoilers symmetric** (glidepath), spring-return closed |
| Left hand | throttle; flap Johnson bar (detented 0/25/40°) | |

**Rudder pedals are deleted.** Script: `analysis/twist-grip-rudder.py`.

## 1. Why this mapping is coherent on this aircraft

On a three-axis airplane a twist rudder would be eccentric. On this two-axis
aircraft it is defensible: rudder-then-dihedral *is* the turn, and the
spoilerons are the roll trim — so the two roll-producing controls live on two
independent degrees of freedom of the same wrist, and a coordinated entry is
one blended hand motion. The crosswind decrab — the case that actually needs
rudder *independent* of wing-leveling — gets exactly that: twist decrabs
while lateral tilt holds the upwind wing down, one hand, no foot dance.

Two honest caveats, recorded rather than buried:

- **Convention says otherwise.** Classic two-axis ultralights (Weedhopper
  style) map *lateral stick to the rudder* because it matches every pilot's
  bank instinct. This scheme reserves lateral for spoilerons instead. The
  blended result is similar — tilting and twisting the same direction — but
  it is a nonstandard mapping and produces **negative transfer** both ways
  for any pilot who also flies standard aircraft. That matters for the fleet
  plan's second pilot; the quarter-scale-to-mockup pipeline should confirm
  the mapping feels natural before the linkage is drawn.
- **Precedent is thin for cable-driven twist yaw.** The pedal-less Ercoupe
  proves an airplane doesn't need pedals; modern eVTOL sidesticks (BlackFly
  class) prove twist-yaw ergonomics — but those are fly-by-wire, where twist
  torque is a sensor input. A *cable* twist grip fights the real hinge
  moment, which is why §2 is the gate.

## 2. The physics gate: wrist torque

VT 15 ft² (36 in chord × 60 in); rudder 50% chord → 7.5 ft², mean chord
1.5 ft; hinge coefficient 0.008/deg unbalanced. Wrist gearing 2.4:1 (±60°
grip to ±25° rudder). Numbers from the script:

| Case | HM raw (in-lb) | w/ 45% horn balance | at the wrist |
|---|---|---|---|
| Taxi prop-wash steering, 15 mph full | 16 | 9 | **3.6** |
| Rotation 28 mph, full | 54 | 30 | **12.4** |
| Crosswind decrab 35 mph, 12° | 41 | 22 | **9.3** |
| Crosswind decrab 35 mph, full | 85 | 47 | **19.4** |
| Vne 62, 8° | 85 | 47 | **19.5** |

Published wrist pronation/supination capability: ~10–15 in-lb sustained
comfortable, ~50–90 in-lb brief maximum. **The scheme closes only with both
the aerodynamic balance and the gearing**: unbalanced and ungeared, full
rudder at 35 mph is ~85 in-lb at the wrist — at the edge of maximum effort.
Balanced and geared, the routine sustained case is ~9 in-lb and the worst
transient ~19: acceptable.

**Two requirements therefore attach to the rudder itself:**

1. **Horn balance, ~45% hinge-moment reduction** — a rudder design change,
   sized (or copied from practice) before the tail drawings freeze. Bonus:
   the horn's mass ahead of the hinge line works *toward* the mass balance
   the flutter item will want anyway.
2. **Gearing 2.4:1 with a centering spring/detent** — the throw trade is
   fixed by wrist range, so the balance is not optional headroom, it is the
   mechanism's feasibility.

## 3. What deleting the pedals buys

- **Weight:** pedals + cables out (−4.5 lb ledger line), twist grip + torque
  stub + centering spring + cable run in (~+2.5): **net ~−2 lb, unbanked**
  until weighed. The measured-weights CSV's "Rudder pedals and cables" row
  retires at the workbook reconciliation.
- **The adjustable-pedal requirement dies.** The 105–200 lb pilot range was
  going to need three-position pedals (common-airframe §7); now only the
  seat adjusts. One less mechanism, and the short-pilot fit problem gets
  easier, not harder.
- **The crush bay gets cleaner.** Rev D put ~15 in of progressive crush
  structure ahead of the pilot's feet; with no pedals there is nothing in
  the footwell to trap or spear feet in a collapse — a smooth floor and a
  footrest. A real crash-safety improvement, free.
- **The pod simplifies.** No pedal cutouts or pedal-travel clearance in the
  nose of the fairing — the §5 fuselage trade's "shape is free" gets freer.

## 4. Fail-safe coherence (all recorded as requirements)

- Symmetric lever **spring-returns closed**; a go-around is *release the
  lever, same hand to throttle* — the spoilers stow themselves.
- The symmetric path must never be able to hold **one** side up alone.
- Twist grip carries a **centering spring with a light breakout**, and the
  grip shape must be chosen so a panic grip or a hard flare pull does not
  input twist — verify on the full-size seating mockup (already planned in
  the digital-fab package) by measuring inadvertent twist during simulated
  flare pulls.
- The Junco servo provision (design-log §21) taps the spoileron circuit
  downstream of both the lateral-stick and symmetric-lever inputs; manual
  always overrides.

## 5. Ground operations

Castoring nosewheel steering is rudder prop-wash plus brakes, unchanged.
Taxi rudder torque at the wrist is ~4 in-lb — trivial. **Open detail for the
mockup:** where the brake lever(s) live now (bicycle levers; options: on the
stick, on the symmetric lever like a bike bar, one per side for differential
steering). Decide at the seating mockup with the other grip questions.

## 6. What this does not settle

- Horn balance geometry (size/copy, then NeuralFoil or spring-scale check on
  the built rudder — the 45% is a target, not a measurement).
- Grip hardware: twist range stops, breakout force, friction.
- Brake lever placement (§5).
- Whether the flap Johnson bar and the symmetric spoiler lever can share the
  left console without confusion — mockup question; they must be
  distinguishable by feel (notched bar vs smooth spring lever).
