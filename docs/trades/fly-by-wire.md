# Fly-By-Wire and Servo-Augmented Controls

**The question:** has anyone built a fly-by-wire ultralight, is it worth
trying here, and would servos *supplementing* the pilot — with manual
reversion by cutting power — make this aircraft safer and handle the control
forces? Script: `analysis/fly-by-wire.py`.

**Short answer: the augmentation instinct is right, the reversion instinct is
right, and this specific airframe is the wrong one for both — for a reason
created two decisions ago.** But one servo *should* exist, it is already in
the plan, and this trade explains why it is the only one.

> **Prior-art section (§1) pending verification.** A sourced research pass is
> running; claims there are from general knowledge and are marked as such
> until confirmed.

## 1. Has anyone done it? Yes — and the examples prove the opposite point

*Pending verification.* Full fly-by-wire ultralights exist and fly under
**Part 103**: the Pivotal (ex-Opener) BlackFly/Helix and the Jetson ONE are
believed to be FBW with **no mechanical linkage at all**.

That sounds like a green light. It is the reverse, because of *why* those
aircraft are fly-by-wire: they are multi-rotor eVTOLs that **cannot be flown
by a human without computers**. There is no mechanical control system to
revert to, because no arrangement of cables could stabilise them. FBW is not
a safety feature they chose; it is the entry fee for their configuration.

Part 103 imposes no equipment requirements, so the legality is not in doubt
— only the engineering is. And the relevant asymmetry is this: **FBW appears
on ultralights exactly where the airframe is uncontrollable without it, and
essentially nowhere else.** No conventional fixed-wing ultralight is known to
use it.

This aircraft is the far end of that spectrum. Its safety case is *passive*
and always has been: Sky Pup lineage stall and spin proofing, a two-axis
layout with no aileron spin mode, dihedral that self-rights, a wing that is
stall-limited so it cannot be aerodynamically overstressed. **Active
protection pays best on aircraft that are passively unsafe.** Adding it here
buys less than it would anywhere else, and it introduces failure modes into
a system that currently has none.

## 2. Weight: the 103 is out, and the EAB fits only the wrong architecture

Aviation-grade autopilot servos run ~2.0–3.0 lb installed:

| Architecture | Servos | Ctrl | Wiring | Battery | **Total** |
|---|---|---|---|---|---|
| Single-string 3-axis | 7.5 | 1.5 | 1.5 | 2.0 | **12.5 lb** |
| Dual-redundant (what a primary control needs) | 15.0 | 3.0 | 3.0 | 4.0 | **25.0 lb** |

| | Margin | Single-string | Redundant |
|---|---|---|---|
| **103 kit** | 0.8 lb empty | over by 11.7 | over by 24.2 |
| **EAB** (200 lb pilot, full fuel) | to 525 gross | 518.2 — **fits, +6.8** | 530.7 — **over, −5.7** |

**The whole problem in one line: the only architecture that fits is the only
architecture you must not use for a primary flight control.** A single-string
servo chain has no backup but the pilot; a redundant one the aircraft cannot
lift. The 103 aircraft is out by more than an order of magnitude and needs no
further discussion.

## 3. Hardover — and the twist grip makes it far worse

A servo commanding full deflection and staying there is the failure that
matters. Can the pilot win?

| Case | Deflection | HM, in-lb | Pilot must apply |
|---|---|---|---|
| Elevator, approach 35 mph | 25° | 137 | 10.8 lb stick |
| Elevator, cruise 50 mph | 25° | 280 | 22.0 lb |
| Elevator, Vne 62 mph | 25° | 430 | 33.8 lb |
| **Rudder, approach 35 mph** | 25° | 47 | **19 in-lb at the wrist** |
| **Rudder, Vne 62 mph** | 25° | 146 | **61 in-lb at the wrist** |

**Elevator is survivable with a standard fix.** 34 lb of stick at Vne is
overpowerable — though not comfortably while the same hand is twisting for
yaw. The conventional answer is a slip clutch limiting servo authority: for
override under 15 lb at Vne, the servo may command at most **~11° of the 25°
throw (44% authority)**. That is ordinary GA autopilot practice.

**The rudder is the problem, and it is self-inflicted.** A pedal-driven
rudder lets the pilot push back with a *leg* — 100+ lb available, with the
whole body braced. The twist grip caps override at a *wrist*: roughly
10–15 in-lb sustained, 50–90 in-lb for a brief maximum. A rudder hardover
demands **19 in-lb held on approach and 61 in-lb at Vne**, at or past
sustainable wrist capability, in the phase of flight with the least altitude
to spare.

The controls-mechanization decision that made the cockpit simple also removed
the strongest muscle group the pilot had for fighting a runaway.

## 4. Manual reversion: the right instinct, killed by back-drive friction

"Cut power to the servos and fly it manually" is the correct architecture —
it is automotive electric power steering, not fly-by-wire, and it is the only
way single-string hardware belongs anywhere near a primary control. It fails
here on a detail this project has already flagged twice.

A slip clutch must sit **above** the largest normal aerodynamic load (or it
slips in normal flight) and **below** pilot override (or the pilot cannot
win). On the twist grip that band is **9 to 19 in-lb at the wrist — a 10 in-lb
window.** Set the clutch mid-band at ~14 in-lb, and with the power off the
pilot back-drives the gearbox through that clutch on *every input*: about
**14 in-lb of dead friction against a 9 in-lb comfortable budget.**

**Manual reversion would be heavier to fly than the unassisted aircraft.**

This is the same property the gap-seal work already turned on — breakout
friction is what kills small precise yaw inputs, which is why a teflon chafe
strip under the seal is mandatory. A geared servo is the largest possible
source of exactly that friction, installed in exactly the wrong circuit.

The escape is a true **electromagnetic de-clutch** that fully disengages on
power loss. It works, it costs weight, and it substitutes one failure for
another: a clutch that fails to release leaves a jammed control, which is
worse than anything it was protecting against.

## 5. The one surface where a servo is already fail-safe

Design-log §9, on the spoilerons:

> *"Single-acting, tension-only, spring return to closed. Airflow and spring
> both push them shut, so a broken or disconnected cable retracts rather than
> floats. On a two-axis aircraft a stuck-open spoiler is the one control
> failure with no good answer, so this is not optional."*

**That physics does not care whether the tension came from a cable or a
servo.** Kill power to a spoileron servo and the surface closes itself. And a
spoileron hardover is the mildest failure available on this airframe: one
wing drops slowly, and the rudder — the actual roll control — overpowers it.

Elevator and rudder have no such property. A hardover there holds the surface
deflected *against* spring and airflow, which is precisely the failure mode
§9 refused to accept on the spoilerons.

**So the spoileron servo provision already in the plan (§21, for the EAB's
Junco wing-leveling) is not a small first step toward fly-by-wire. It is the
one place on this airframe where the existing fail-safe already covers a
servo — and that is exactly why it is the one that should exist.**

## 6. There is no force problem to solve

| Control | Steady force |
|---|---|
| Elevator, cruise trimmed | 2.6 lb |
| Rudder, cruise (twist) | ~9 in-lb |

Neither is a strength problem. Both are *endurance* problems, and the fixes
are already identified: a **0.4 lb spring trim** and a horn-balanced rudder.
Servos would be spending 12.5 lb and a new class of failure to solve what
0.4 lb of spring already solves.

## 7. What to do instead — in descending order of value

1. **Angle-of-attack annunciation, not protection.** The dominant killer in
   this class is loss of control at low speed. An AoA indication (the Junco
   tablet is already in the EAB plan; a probe is ounces) delivers most of the
   safety benefit of stall protection with **no actuator, no authority
   question, and no failure mode** — it informs the pilot instead of fighting
   them. Best safety-per-pound on the entire aircraft.
2. **The spoileron servo already planned** (§5 above) — wing-leveling in
   crosswind, fail-safe by spring return, hardover overpowered by rudder.
3. **Electric pitch trim, if wanted.** A *trim* servo is low-authority by
   construction, and a trim runaway is slow and overpowerable — which is why
   the whole GA world accepts electric trim on aircraft that would never
   accept electric primary control. A legitimate servo application; weigh it
   against the 0.4 lb spring before buying.
4. **Nothing in pitch or yaw.** Not as primary, not as assist.

**The EAB may legitimately experiment**, since it is the fleet's declared
development platform: a single-string system, flown at altitude, with a
prominent disconnect, is a reasonable research exercise. What it can never
become is a primary control the pilot depends on, because the redundancy that
would justify that dependence does not fit in the weight class.

## 8. What this does not settle

- Servo weights and clutch specifications are class estimates; confirm on a
  scale and against real torque data before any of §7 is built.
- The de-clutch option (§4) is dismissed on judgement, not on measurement —
  if a light electromagnetic clutch with genuinely zero residual drag exists,
  the rudder conclusion is worth revisiting.
- AoA probe location and calibration on this wing — and note it interacts
  with the pitot alignment item already open, since both are air-data sensors
  in a flow field nobody has mapped.
- Whether the Junco autopilot's own fail-safe design (EAB work, not this
  airframe's critical path) meets the §9 standard.
