# Landing Gear: Grass, Easy Entry, Strong and Forgiving

**Requirements as stated:** good for grass, low enough that a 6'0" / 170 lb
pilot gets in comfortably, strong and forgiving. Script:
`analysis/gear-design.py`. This resolves the gear-geometry open question and
replaces the placeholder gear in the general-arrangement model (rev B).

**The three requirements pull the same direction — down.** A low stance makes
entry easy, improves the tip-back angle, lowers the rollover risk on rough
ground, and shortens the gear legs (lighter and stiffer). The design is
Airbike-like: low pod, sprung 4130 main legs in a V, castoring sprung
nosewheel.

## 1. Stance — the entry requirement sets it

| | |
|---|---|
| Belly at cockpit | **16 in AGL** |
| Seat pan | **~20 in AGL — kitchen-chair height.** Sit down, don't climb in |
| Step-over sill | ~26 in (a bathtub wall), cabane strut as the grab handle |
| Seated head top, 6'0" pilot | ~56 in → wing underside at 64 in clears by ~8 in |
| Thrustline | 40 in AGL — unchanged from §16 |
| 60 in prop static tip clearance | 10 in; **+2.5 in remaining at full gear stroke + flat tire** (the standard emergency case, still positive) |

## 2. Energy — the "forgiving" requirement, with numbers

Design sink **8 fps at the 525 lb fleet max** (FAR-23-equivalent is ~7; 8 is
the student-proof margin): 522 ft-lb to absorb.

- **Total stroke 6.6 in** at gear reaction factor 3.0: ~2.0 in from the tire at
  8–10 psi + **~4.6 in of vertical travel at the axle** from the sprung leg.
- Loads: 1,575 lb total limit reaction → **788 lb per main leg limit, 1,181 lb
  ultimate**. Size the leg, its fitting, *and the longeron cluster it feeds* —
  the cluster is where gear failures actually start.
- **The tire is the damper.** A tube-spring leg stores and returns energy —
  that return is the bounce. Low-pressure tires are the only real damping in
  this architecture, which is why the pressure (8–10 psi) is a placard, not a
  suggestion.

## 3. Geometry — every check passes

| Parameter | Value | Check |
|---|---|---|
| Mains | sta 70.5, **15% MAC aft of CG** | target band 12–16% ✓ |
| Nose | sta 15 (rev D raked leg, §8) | static nose load **13.5%** (castoring band 8–15%) ✓ |
| Wheelbase | 55.5 in | |
| Track | **56 in** | wide for grass + crosswind |
| Tip-back angle | **15.5°** | ≥15 ✓ — rotation works without fighting the gear |
| Overturn angle | 51° | <60 ✓ (improved from 56° by the longer wheelbase) |
| Tail-strike attitude | **13.4°** | see below |

**Tail strike, stated honestly:** normal touchdown is 8–12°, fine. A full-stall
landing (slats stall near 19°) *will* touch the boom first. The fix is a small
steel **tail skid at the tail post (~0.3 lb)** — now in the model — and a
placard note. This is the standard trike-with-slats compromise; raising the
boom instead would cost tail arm.

## 4. Wheels and tires

- **Mains: 13×5.00-6 on 6 in rims at 8–10 psi.** The bicycle discs (§11) bolt
  to these hubs as before.
- **Nose: 20×2.4 BMX/junior-MTB wheel (rev D, §8)**, castoring ±60° with
  steering stops and a **castor trail + friction damper** — the nose leg meets
  the ruts first, so it gets its own compliance, and a light castoring bike
  wheel *will* shimmy without the damper.
- **EAB kit option: 16×6.5 low-pressure tires on the same rims** (+3–4 lb).
  A kit item like the windshield — never on the 103 aircraft, where the 0.8 lb
  margin cannot afford it. Soft-field technique (aft stick, nosewheel light)
  covers the 103 kit on the home strip.

## 5. Structure — starting point for the gate-4 detail

Per-leg ultimate 1,181 lb on an ~18 in bending arm:

| Leg tube | σ at ultimate | Verdict |
|---|---|---|
| 1.500 × .120 4130 | 128 ksi | needs heat treat |
| **1.625 × .120 4130** | **107 ksi** | **heat-treated to ~150–180 ksi — the pick** |
| 1.750 × .120 4130 | 91 ksi | normalized-marginal; heavier |

Heat-treat after welding, or increase the leg sweep to shorten the arm. The
deflection (spring-rate) check that confirms the 4.6 in of travel comes with
the real leg curve in the gate-4 drawings — a straight tube at this stress
won't give the travel; the legs want a swept/curved form like the Airbike's.

Weight check: legs 8 lb + wheels/tires 7 + brakes 2.5 + nose 9 + mounts 3 =
**29.5 lb — unchanged from the common-airframe invariant.** The tail skid adds
0.3 lb; take it from the AN/hardware line's rounding or accept 253.5 on the
103 kit (still under 254, margin 0.5 lb — one more reason to weigh everything).

## 6. What changed in the model (rev B)

Fuselage lowered to the 16 in belly, wing to 64 in, thrustline to 40 in, mains
moved sta 78 → 70.5 (the CSV's sta-78 placeholder was 30% MAC aft — too far
aft to rotate), track widened to 56 in, nose gear at sta 32 with a smaller
wheel, V-strut main legs, tail skid added. `model/nuthatch.stl` and the GA
drawing regenerated; the interactive artifact republished as rev B.

## 7. Revision: trailing arms with MTB coil-over shocks; tire size split

The "absorb everything with the shocks, run small tires" proposal splits into
two halves with opposite verdicts.

**The shock half is adopted — it is better than what §2 specced.** The sprung
4130 legs are springs: they store landing energy and give it back, and that
return is the bounce. The only damping in the original architecture was the
soft tire. **Trailing-arm mains with mountain-bike downhill coil-over shocks**
add real, *adjustable* rebound damping:

| Lever ratio | Shock stroke (4.6 in at wheel) | Shock force at 788 lb limit |
|---|---|---|
| 1.5:1 | 3.1 in | 1,182 lb |
| 2:1 | 2.3 in | 1,576 lb |

DH coil shocks run 2.5–3.0 in stroke, ~1 lb, $60–150, with swappable springs —
which means **each aircraft in the fleet gets a spring rate matched to its
weight**, and the rebound clickers tune out bounce at the strip. This extends
§11's bicycle-components philosophy from the brakes to the suspension. *Verify
before committing: shock structural rating near 1,600 lb, and clevis the eyes —
DH shocks are not designed for side load.*

**The 8-in tire half is rejected for the mains — diameter is what grass
taxes, and suspension cannot buy it back.** Load capacity is irrelevant (scooter
tires carry more per wheel than this aircraft needs). The problem is geometry:
a wheel crossing a rut or grass clump is *stopped*, not deflected — vertical
suspension fixes sink energy, not rolling obstacles:

| Over a 2 in bump | Drag ÷ wheel load |
|---|---|
| 13×5.00-6 | 1.04 |
| 8×2 scooter | **1.73** |

And rolling friction moves the takeoff roll the wrong way on the one field that
matters: ~96 ft on 13-in wheels in normal grass vs **~210 ft on 8-in** — most
of the short-field margin spent on wheel choice. The honest weight prize
(pneumatic 8×2 pair ≈ −3.5 lb, net ≈ −2.5 lb with the shock hardware, taking
the 103 margin from 0.5 to ~3 lb, plus ~2% less parasite drag) is real, which
is why the decision is a **per-field placard, not a redesign**: the axles take
either wheel. 13-in is the grass default; 8-in pneumatic is legal and lighter
if the strip is kept mowed and the pilot accepts the longer roll. **Solid
scooter tires are forbidden outright** — zero compliance, energy spikes into
the shock, and they shed on grass.

The nosewheel keeps its 4.10-6 regardless: it meets every rut first, and
nose-over is the failure that ends a flying day.

## 7a. Second revision: large-narrow bicycle wheels — adopted as the primary main

The refined proposal — **a large-diameter, narrow, high-performance bicycle
wheel** (20×2.4 BMX/DH class, or 24×2.6) — is the opposite corner of the tire
trade from the 8-in scooter wheel, and the shock adoption changed the physics
in its favour.

**Bump crossing (drag ÷ wheel load over a 2 in clump):** 8-in scooter 1.73,
13×5.00-6 1.04, **20×2.4 bike 0.75**, 24×2.6 0.66. Diameter is what grass
taxes, and the bike wheel has the most of it.

**Why narrow works now:** the 8-in rejection stood on two legs — diameter and
the tire-as-damper. Big-narrow fixes the first, and the adopted MTB coil-overs
took over the damping job entirely. A stiff dual-ply DH casing at 22–28 psi
riding on a damped 4.6 in of trailing-arm travel is a *better* energy chain
than a fat tire on an undamped spring leg.

**Weight is honestly a wash** (7–9 lb/pair vs 6.5–8 for light 13s — weigh
before believing), but the bike wheel buys three real things: the bump
crossing above, **~40% less frontal area in flight**, and — the quiet win —
**the bicycle disc hub is native**, so §11's machined rotor-to-hub adapter is
deleted (−0.5 lb and a machine-shop task gone). Brakes, shocks, and now wheels
all come from the same bicycle-industry parts bin.

**The structural catch, and the gate:** a spoked wheel is superb radially and
weakest laterally, and a crosswind touchdown is a lateral event. Adoption
requirements: 36–48 spokes (13/14 g), modern disc rim, through-axle hub
(12–20 mm), dual-ply DH casing at a 22–28 psi placard, and a **shop-floor
lateral proof test — ~400 lb side load at the rim (0.5 × vertical limit) held
without buckling — before either aircraft flies on them.** Precedent exists:
Legal-Eagle-class and Bloop minimum ultralights have flown spoked bicycle
wheels at these weights for decades.

**Refinement — modern high-performance wheelsets, already owned:** the wheels
in hand are high-end aluminum/carbon MTB wheelsets with sub-2 lb tires, which
puts the pair at the light end of the range (~6–7 lb with sealant) at zero
cost — and a 29er, if that's the size, crosses the 2 in bump at **0.59**,
better still. Updates that follow:

- **Prefer the aluminum rims for the gear.** An aluminum rim fails by denting
  and keeps rolling; carbon fails by cracking, suddenly, and a crack from a
  hard landing is hard to see (tap-test at best). For a *forgiving* gear the
  dent is the right failure mode. Carbon is acceptable with a
  post-hard-landing inspection protocol and a tire insert — the §7 spar
  objection (undetectable void) doesn't carry to a factory-molded QC'd rim,
  but inspectability still favours metal here.
- **Use rear boost hubs (12×148 through-axle) on both sides** — widest flange
  spacing, stiffest laterally, native 6-bolt disc; a single-speed spacer kit
  replaces the cassette. Modern 28–32-spoke boost disc wheels are far stronger
  laterally than the old 36h assumption; the ~400 lb lateral proof test stands
  regardless, and MTB wheels routinely take bigger instantaneous hits under a
  250 lb rider than this aircraft's 788 lb limit case.
- **Tubeless with a tire insert** (CushCore-class): rim-strike protection at
  landing loads *and* a run-flat — which improves the flat-tire prop-clearance
  case the stance analysis already carries.
- Weigh the actual wheels and tires and enter them in the build log — these
  are the first components where "estimate" can become "measurement" today.

**Flotation is the accepted trade:** ~24 psi ground pressure against the fat
tire's ~9. Fine on the firm mowed home strip; the 13×5 (or EAB 16×6.5) remains
the soft/wet-field wheel. Design the trailing-arm axle with **interchangeable
inserts (bike through-axle or 5/8 in aircraft axle)** so the choice stays
per-field, as §7 already established.

## 8. Rev D: raked nose leg — the wheel just behind the propeller

The nose leg tilts forward so the wheel sits **just aft of the prop disc**:
20×2.4 wheel (R = 10 in), axle at **sta 15, z = 10**, tire front face at sta 5
— **3.0 in behind the prop plane** (an axle at sta 10 would put the tire face
*inside* the prop plane; 15 is as far forward as it goes). Every geometry
check improves or stays in band:

| Check | rev C (vertical, sta 32) | rev D (raked, sta 15) |
|---|---|---|
| Nose-over prop-protection angle | 17.9° | **35.5° — roughly doubled** |
| Static nose load | 19.5% (slightly heavy) | **13.5%** (8–15% castoring band ✓) |
| Wheelbase | 38.5 in | 55.5 in |
| Overturn angle | 56° | **51°** |
| Flat-nose-tire prop clearance | ~4.6 in | **~7 in** |
| Braking pitch-over margin | — | atan(48/27) = **60.6°** — huge |

**Prop protection:** with the wheel at sta 15, the aircraft must pitch **35.5°**
nose-down about the nose axle before a 60-in prop tip reaches the ground —
about twice the rev C figure. (A tiny 6-in wheel tucked at sta 10.25 would give
47°, but the bike wheel wins where it matters: crossing ruts, which the nose
meets first. Diameter is what grass taxes — §7a's own rule.)

**Crush structure — the second half of the request.** The leg is a
**triangulated bay**: the main raked member runs (30, 0, 17) → (15, 0, 10) at
~63°, so a rut-strike or nose-first impact loads it near-axially — the genuine
structural advantage of the rake — and a second near-vertical member
(14, 0, 30) → (15.5, 0, 10.5) closes the triangle. That triangle is
**~15 in of progressive crush structure ahead of the rudder pedals**: in a
nose-first accident it collapses and absorbs energy before the cockpit sees
the load, exactly the "extend it forward at an angle" intent.

**Loads and weight:** nose gear limit ≈ static 71 lb + 0.35 g braking transfer
89 lb ≈ **160 lb** — members of ~1.0 × .049 4130 carry that with margin
(gate-4 detail with the fittings). Weight is a wash: the added tube length is
offset by the 20-in bike wheel replacing the 6-in pneumatic assembly —
**weigh it on the bench**. The nosewheel now comes from the same bicycle parts
bin as the mains (rim, tire, sealant, disc hub standards all shared).

**Gate-4 verifications this adds:** castor-swing prop clearance ≥ 2.5 in at
full ±60° steering throw, and the friction-damper detail (shimmy on a light
castoring bike wheel is a real risk, not a formality).

## 9. What this does not settle

- Trailing-arm geometry and pivot bearing detail (gate-4 drawing); shock
  structural rating verification at ~1,600 lb; axle inserts for both wheel
  standards.
- The bike-wheel lateral proof test (~400 lb at the rim) and real pair weights
  on a scale.
- Drop test. AC 103-7-era practice is a static-plus-drop demonstration — plan a
  free drop of the complete gear at 456 lb from h = v²/2g ≈ 12 in onto the
  mains before first flight. Cheap, and it converts N=3 from assumption to
  measurement.
- Nose-leg spring detail and steering-stop angles.
- Grass rolling resistance was carried at µ=0.1 in every takeoff number —
  tall/wet grass is worse; the home strip should be mowed for Phase I.
