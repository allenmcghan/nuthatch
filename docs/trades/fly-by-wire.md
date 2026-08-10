# Fly-By-Wire and Servo-Augmented Controls

**The question:** has anyone built a fly-by-wire ultralight, is it worth
trying here, and would servos *supplementing* the pilot — with manual
reversion by cutting power — make this aircraft safer and handle the control
forces? Script: `analysis/fly-by-wire.py`. Sources marked **[M]** measured /
documented / regulatory · **[B]** builder report · **[V]** vendor claim.

**Short answer: the augmentation instinct is right, the manual-reversion
instinct is right, and this airframe is the wrong one for both.** One servo
*should* exist, it is already in the plan, and §6 explains why it is the only
one.

## 1. Yes — and every example proves the opposite point

Full-FBW ultralights fly under **Part 103** today **[M]**:

| Aircraft | Empty | Architecture |
|---|---|---|
| Pivotal BlackFly | 313 lb | 8 motors, **triple-redundant FBW**, dual joysticks (either alone suffices) |
| Pivotal Helix | 348 lb | Triple modular redundancy, 4 split elevon pairs, whole-aircraft chute |
| Jetson ONE | ~198 lb | Triple-redundant IMU **and** flight computer; flies with a motor failed |
| LIFT HEXA | ~432 lb | 18 independent motors/props/batteries, 3 redundant flight-control systems |

BlackFly's documentation is explicit: *"no mechanical linkages from pilot to
control surfaces… **The aircraft cannot be flown without flight computers —
there are no mechanical backups.**"* **[M]**

That is the whole finding. **None of these chose FBW.** They are multirotors
and tailsitters that are aerodynamically incapable of flight without
computers; FBW is the entry fee for the configuration, not a safety upgrade.

**And there is no counterexample.** The research found **not one fixed-wing
ultralight, LSA, homebuilt, or certified light aircraft with full fly-by-wire
and no mechanical reversion** **[M]**. The first fixed-wing aircraft to fly
digital FBW without mechanical backup was NASA's **F-8C in 1972** — a
national research programme with a test pilot and an ejection seat.

### The Part 103 weight loophole — and it runs the wrong way here

This is the finding that changes the arithmetic. §103.1(e)(1) caps empty
weight at 254 lb **"excluding floats and safety devices which are intended
for deployment in a potentially catastrophic situation"** **[M]**. BlackFly
is 313 lb and Helix 348 — the ballistic parachute and amphibious flotation
are roughly **90+ lb of legally invisible hardware** that bridges the gap.

**Servos, flight computers, wiring harnesses and their batteries are not
excluded.** The exemption that makes FBW ultralights legal cannot be used to
carry the FBW. (The related "batteries don't count as fuel" theory is also
wrong — FAA Chief Counsel has held batteries count against empty weight, a
point this project already relies on in design-log §3.)

This aircraft is the opposite case in every respect. Its safety is *passive*:
Sky Pup stall and spin proofing, a two-axis layout with no aileron spin mode,
dihedral that self-rights, a wing that is stall-limited so it cannot be
aerodynamically overstressed. **A two-axis dihedral aircraft is already a
stability-augmented aircraft — mechanically, passively, at zero weight, with
zero failure modes and no power required.** It has already solved the problem
FBW is usually deployed to solve.

## 2. Weight, using the lightest hardware that exists

Real servo weights **[M/V]**: **Garmin GSA 28 = 1.4 lb, $975** experimental;
Dynon SV32 = 2.17 lb, $948. The table below uses the GSA 28 — the most
favourable case the idea can be given.

| Architecture | Servos | Ctrl | Wiring | Battery | Total |
|---|---|---|---|---|---|
| Single-string 3-axis | 4.2 | 1.0 | 1.0 | 3.0 | **9.2 lb** |
| Dual-redundant (primary-control minimum) | 8.4 | 2.0 | 2.0 | 5.0 | **17.4 lb** |
| Triple-redundant (what real FBW ULs use) | 12.6 | 3.0 | 3.0 | 7.0 | **25.6 lb** |

| | Single-string | Dual | Triple |
|---|---|---|---|
| **103 kit** (0.8 lb margin) | over by 8.4 | over by 16.6 | over by 24.8 |
| **EAB** (200 lb pilot, full fuel, 525 gross) | 514.9 — fits **+10.1** | 523.1 — fits **+1.9** | 531.3 — **over 6.3** |

*(Correction to this trade's first pass, which used a 2.5 lb servo and
concluded dual-redundant could not fit the EAB. With real hardware it fits,
barely.)*

**The 103 aircraft is out by an order of magnitude and needs no further
discussion.** On the EAB the fit that matters is the wrong one: **the
architecture with room to spare is single-string, which is precisely the
architecture that must not carry a primary control.**

### Electrical power — the gating item nobody plans for

A Dynon SV42 draws **2.03 A moving at full torque** **[M]** — three servos
plus a controller is ~78 W, or ~156 Wh over two hours, about 2.3 lb of cells
before BMS, case, or a second pack. **Many Part 103 engines (Hirth, Polini,
Vittorazi class) have a very small alternator or none**, sometimes only
enough for ignition.

If servos are load-bearing for control, the battery becomes **flight
critical** — engine-out must not mean control-out — so it needs its own pack
sized for full duration, and then a second, because one pack is a single
point of failure for the whole aircraft. **This is why every FBW ultralight
is an electric aircraft**: they already own a large, redundant, monitored
battery system. Verify the chosen engine's actual charging surplus before
anything else.

## 3. Hardover — and the twist grip makes it far worse

| Case | Deflection | HM, in-lb | Pilot must apply |
|---|---|---|---|
| Elevator, approach 35 mph | 25° | 137 | 10.8 lb stick |
| Elevator, cruise 50 mph | 25° | 280 | 22.0 lb |
| Elevator, Vne 62 mph | 25° | 430 | 33.8 lb |
| **Rudder, approach 35 mph** | 25° | 47 | **19 in-lb at the wrist** |
| **Rudder, Vne 62 mph** | 25° | 146 | **61 in-lb at the wrist** |

**Elevator is survivable with standard practice** — a clutch limiting servo
authority to ~11° of the 25° throw (44%) keeps override under 15 lb at Vne.
The industry invariant is simply *the servo may not have more authority than
the pilot*.

**The rudder is the problem, and it is self-inflicted.** A pedal rudder lets
the pilot push back with a *leg* — 100+ lb, whole body braced. The twist grip
caps override at a *wrist*: ~10–15 in-lb sustained, 50–90 brief maximum. A
hardover demands **19 in-lb held on approach and 61 in-lb at Vne**.

Worse, this is uncharted: **no surveyed product is designed to assist or
back-drive a twist grip, and no human-factors data on torsional override
force exists** **[M — explicit data void]**. Every autopilot servo on the
market assumes stick/yoke in pitch and roll, pedals in yaw. The numbers above
are, as far as the research could establish, the only ones anyone has.

### The certification arithmetic says there is no altitude to do this in

Part 23 practice assumes a **3-second pilot recognition delay** for an
autopilot malfunction in cruise, climb or descent, and **1 second on a low
approach** **[M]**. Operating rules (§121.579, §135.93) then require autopilot
use no lower than **twice the AFM altitude loss**.

At 50 mph, three seconds is **220 ft of travel**. Ultralight pattern work
happens at 500–800 ft AGL. A hardover, plus the delay, plus the 2× factor,
plausibly consumes more altitude than this aircraft ever has beneath it.
**By the certification world's own arithmetic, a servo with meaningful
authority has no legal operating altitude band in a Part 103 mission
profile.**

## 4. Manual reversion — corrected: the clutch exists, the ratio still bites

"Cut power and fly it manually" is the right architecture — automotive
electric power steering, not FBW. EPS confirms the principle **[M]**: *"most
electric power steering malfunctions do not disconnect the steering wheel
from the front wheels — the mechanical linkage remains intact."*

**Correction to this trade's first pass.** I dismissed a true de-clutch as
hypothetical. It is a shipping product: the **Garmin GSA 28 uses a solenoid
engagement clutch** that decouples the motor when unpowered, explicitly for
*"virtually no control system friction with the autopilot turned off"*, and
Garmin deleted the shear pin entirely **[V]**. Dynon, Trio and TruTrak
instead use **permanently coupled slip clutches**.

So the friction objection is not fatal — it is an **architecture rule**:

> **An engagement-clutch servo is mandatory here; permanently-coupled
> slip-clutch servos are disqualified.**

But the underlying ratio argument survives and is the real warning. **Servo
gear-train friction is roughly fixed in inch-pounds, while this aircraft's
control forces are unusually small in inch-pounds.** A builder describes
Dynon friction as *"low enough in percentage compared to the control forces"*
on an RV-12 **[B]** — an aircraft with several times this one's stick force.
**The ratio is the worst of any airframe these products were designed for**,
which is why Garmin spent real money engineering the friction out for
customers who needed it far less.

And EPS supplies the caution for the failure case **[M]**: production systems
mask gear friction and rotor inertia with **active software compensation
running on the powered motor**. Cut power and you inherit the raw,
uncompensated friction plus reflected rotor inertia — one-handed, on a stick
that also twists for rudder. *(No published numerical back-drive figures
exist for any production EPS system; this would have to be bench-measured.)*

## 5. The Baron — read this one twice

**Beechcraft E55, Fayetteville NC, 27 June 2019** **[M]**. Uncommanded
nose-down pitch trim. The system had a correctly designed manual override.
The fastener securing the clutch to the pitch trim servo had been
overtightened:

> **Required clutch breakaway force: 13 ± 2 lb. As found: 45 lb.**

NTSB probable cause: *"The pilot's failure to disengage an uncommanded
nose-down pitch input. Contributing… improper maintenance of the pitch trim
servo, which would have precluded a physical override."* The pilot was killed
— **and so was a person on the ground, inside their own home.**

One overtightened fastener turned a survivable nuisance into a double
fatality. **The slip clutch is not a safety feature you install; it is a
safety feature you maintain, forever, correctly, with a calibrated
measurement.**

On a Part 103 aircraft there is **no annual, no A&P, and no mandatory
inspection of that clutch, ever.** The person who has to catch it is the
owner, indefinitely. And §103.9 — *"no person may operate any ultralight
vehicle in a manner that creates a hazard to other persons or property"* — is
exactly the open-ended rule that fact pattern reaches.

## 6. The one surface where a servo is already fail-safe

Design-log §9, on the spoilerons:

> *"Single-acting, tension-only, spring return to closed. Airflow and spring
> both push them shut, so a broken or disconnected cable retracts rather than
> floats. On a two-axis aircraft a stuck-open spoiler is the one control
> failure with no good answer, so this is not optional."*

**That physics does not care whether the tension came from a cable or a
servo.** Kill power to a spoileron servo and the surface closes itself. A
spoileron hardover is also the mildest failure available here: one wing drops
slowly, and the rudder — the actual roll control — overpowers it. Spoilers
also do not suffer aileron reversal near the stall.

Elevator and rudder have no such property. A hardover there holds the surface
deflected *against* spring and airflow — precisely the failure mode §9
refused to accept on the spoilerons.

**So the §21 spoileron servo provision is not a first step toward FBW. It is
the one surface whose existing fail-safe already covers a servo, which is
exactly why it is the one that should exist.**

**New caveat from the research, and it is a real one:** every surveyed
autopilot's gain scheduling assumes roughly linear aileron response.
Spoilerons are **strongly nonlinear with a deadband** — §9 itself specifies
roughly 30% of stick travel as deadband — followed by a steep and possibly
hysteretic response. **Expect PIO or limit-cycle behaviour on the first
tuning attempt**, and budget tuning time accordingly. The good option is
still the good option; it is not the easy option.

## 7. There was never a force problem

| Control | Steady force |
|---|---|
| Elevator, cruise trimmed | 2.6 lb |
| Rudder, cruise (twist) | ~9 in-lb |

Power assist exists to reduce *high* control forces. A 456 lb aircraft at
50 mph does not have high control forces. Neither figure is a strength
problem; both are *endurance* problems, already solved by a spring trim and
the horn-balanced rudder. Servos would spend 9+ lb and a new class of failure
on what ounces of spring already handles.

## 8. What to do instead — in descending order of value

1. **Angle-of-attack annunciation, not protection.** Loss of control in
   flight is **~40% of fatal GA accidents, more than the next six causes
   combined**, and the GA Joint Steering Committee's top recommendation was
   AoA indicators **[M]**. An AoA display adds **no actuator, no authority
   question, and nothing that can fail inside the control circuit** — it
   informs the pilot instead of fighting them.
   **Honest caveat:** the 40% figure describes the *problem*, not AoA
   effectiveness. **No controlled study quantifying accident-rate reduction
   from AoA indicators exists** — the FAA/GAJSC position is a reasoned
   recommendation, not a measured outcome. Discount any percentage quoted.
   **Weight caveat:** a complete Alpha Systems installation is *"not quite
   two pounds"*, $200–$1,995 **[V]** — which the **103 kit cannot afford**.
   On the EAB, where the Junco tablet already provides the display and
   pitot-static plumbing, the marginal cost is close to a probe. **This is an
   EAB item, and the 103 keeps its stall margin the hard way.**
2. **The spoileron servo already planned** (§6), with the tuning caveat.
3. **Electric pitch trim, if wanted — and it is lighter than the spring.**
   Ray Allen T2/T3 actuators weigh **2.5 oz** **[M]**, against the ~0.4 lb
   spring-trim estimate, and the jackscrew **locks in position when power is
   off** rather than flopping. Trim runaway is tolerated where surface
   runaway is not because of four properties that must *all* hold: it moves
   slowly, its authority is a fraction of the surface's, cutting power stops
   it instantly, and the residual force is holdable by muscle. **Property
   four is what failed in the Baron.** Ray Allen claims runaway is impossible
   because there is no electronic path from sensor to motor **[V]**; builders
   report **stuck-switch, chafed-wire and welded-relay runaways anyway
   [B]**, mitigated with a 1 A breaker, a guarded switch, and an aftermarket
   limiting controller. Worth it; not free.
4. **Nothing in pitch or yaw.**

**On open-source autopilots**, since it is the obvious cheap path: the
ArduPilot project's own Developer Code of Conduct states that *"ArduPilot is
NOT certified for use in applications where ArduPilot is effectively in
control of human lives,"* explicitly including manned aircraft, and
developers are directed not to assist such projects **[M]**. Builders asking
for help are told *"you will get no support for such a project."* Nothing
there binds a Part 103 builder legally — but it means **no bug triage, no
peer review, and no help from the only people who understand the code**, at
the moment it would matter most. The research also found **no published
flight-test report and no accident report** for a manned ultralight on
Pixhawk/ArduPilot/PX4 — and since Part 103 vehicles are unregistered and
largely uninvestigated, **that silence is a data void, not a safety record.**

**The EAB may legitimately experiment** — it is the fleet's declared
development platform, and a single-string engagement-clutch system flown at
altitude with a prominent disconnect is a reasonable research exercise. What
it can never become is a control the pilot depends on, because the redundancy
that would justify that dependence does not fit.

## 9. What this does not settle

- Back-drive torque of an engagement-clutch servo **with power off, measured
  on a bench** — the one number that would move the §4 conclusion, and it is
  published nowhere.
- Trio servo weight and current draw (factory contact required); Dynon's
  2.17/3.10/4.02 lb figures want confirmation against Dynon's own datasheet.
- The chosen engine's actual alternator surplus (§2).
- AoA probe location and calibration — **pair it with the open pitot
  alignment item**, since both are air-data sensors in a flow field nobody
  has mapped and the 103's ~1 kt stall margin depends on both.
- Whether the Junco autopilot's own fail-safe design meets the §9 standard —
  EAB work, not this airframe's critical path.
