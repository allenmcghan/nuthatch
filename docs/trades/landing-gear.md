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
| Nose | sta 32 | static nose load **19%** (15–20%) ✓ |
| Wheelbase | 38.5 in | |
| Track | **56 in** | wide for grass + crosswind |
| Tip-back angle | **15.5°** | ≥15 ✓ — rotation works without fighting the gear |
| Overturn angle | 56° | <60 ✓ |
| Tail-strike attitude | **13.4°** | see below |

**Tail strike, stated honestly:** normal touchdown is 8–12°, fine. A full-stall
landing (slats stall near 19°) *will* touch the boom first. The fix is a small
steel **tail skid at the tail post (~0.3 lb)** — now in the model — and a
placard note. This is the standard trike-with-slats compromise; raising the
boom instead would cost tail arm.

## 4. Wheels and tires

- **Mains: 13×5.00-6 on 6 in rims at 8–10 psi.** The bicycle discs (§11) bolt
  to these hubs as before.
- **Nose: 4.10/3.50-6**, castoring with steering stops, rubber-disc or bungee
  springing — the nose leg meets the ruts first, so it gets its own compliance.
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

## 7. What this does not settle

- The actual leg curve and spring rate (gate-4 drawing; verify 4.6 in travel).
- Drop test. AC 103-7-era practice is a static-plus-drop demonstration — plan a
  free drop of the complete gear at 456 lb from h = v²/2g ≈ 12 in onto the
  mains before first flight. Cheap, and it converts N=3 from assumption to
  measurement.
- Nose-leg spring detail and steering-stop angles.
- Grass rolling resistance was carried at µ=0.1 in every takeoff number —
  tall/wet grass is worse; the home strip should be mowed for Phase I.
