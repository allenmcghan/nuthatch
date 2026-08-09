# Borrowed Optimizations: What the Ultralight World Does That This Design Hasn't

**The question:** looking at other ultralights, what else is worth stealing?
Script: `analysis/borrowed-optimizations.py`.

This project is already a borrowing machine — Sky Pup wing, Airbike steel,
Kolb boom, bicycle wheels and brakes, MTB coil-overs, glider Johnson bar,
sling seat from Quicksilver/Kolb practice. So the useful question is not
"what could we copy" but **what is left that this design would regret not
knowing**. Six items, ordered by value. Nothing here is adopted — these are
proposals for the owner, except §3, which is a hole rather than an upgrade.

---

## 1. Vortex generators — and they may be the flaps decision's real safety net

**The finding that matters most.** Design-log §10 justified slats with a
specific argument that had nothing to do with stall speed:

> *"Slats specifically, rather than flaps, because there are no ailerons.
> Spoilerons need attached flow over the outer panel."*

Yesterday's flaps-for-slats decision deleted the device that was doing that
job. The mitigation on record is **passive** — 2.5° washout, inboard-only
flaps, and a quarter-scale model test — with a heavy escape clause (a wing
drop reverts the whole decision back to slats).

**Vortex generators are the STOL world's standard active answer to exactly
this problem**: a spanwise row of small vanes near the leading edge that
re-energize the boundary layer and keep the outer panel attached several
degrees past where a clean wing breaks. They are used across the
backcountry/STOL kit fleet (Kitfox, Just Highlander, Rans, Zenith, Cub
retrofit kits), which is the same flight regime this aircraft lives in.

Why they suit this aircraft unusually well:

- **They target the exact failure mode the design fears** — not stall speed,
  but *roll control at high alpha*. The spoilerons need attached flow; VGs
  are the cheapest way to guarantee it.
- **They are a Phase I development part, not a design commitment.** Ounces
  of vanes bonded to fabric, tunable in position and count on the flight
  line, removable without trace. Nothing about them has to be decided now —
  they only have to be *not designed out*.
- **They change the escape clause economics.** Today a wing drop on the
  model reverts the airframe to slats — a 6 lb, 103-margin-eating reversal.
  With VGs in the toolkit, the first response to a wing drop is a $100 strip
  of vanes, and slats become the fallback behind that.

**Cost of holding the option open: zero.** The only requirement is that the
outer-panel leading edge stay accessible and bondable — which Oratex is, and
a moulded carbon tip cap must not interfere with.

**Recommendation: adopt as a Phase I development item, not a design change.**
Record the intent so the wing drawings do not accidentally preclude it, and
carry VGs as the first-line remedy in the flaps escape clause.

## 2. Drag cleanup: the 80% the audit found and nobody has attacked

The audit's own words: *"the smooth airframe is only f = 0.084 m² against the
0.45 carried — ~80% of the drag budget is cockpit, pilot, gear, rigging, and
cooling."* It then filed the finding under "housekeeping" and moved on. **No
trade has ever attacked it**, while the project has spent real effort on
wingtip shape worth +2.9%.

Housekeeping is **3.94 of the 4.84 ft²** of equivalent flat plate. Estimated
breakdown (engineering estimate, not measured — the back-solve is calibrated
to the total, so treat the split as indicative):

| Item | est. f, ft² |
|---|---|
| Three bare spoked bicycle wheels | 0.94 |
| Gear legs, cabane, exposed tubes | 0.30 |
| Pilot head/shoulders + cockpit opening | 2.10 |
| Cooling, rigging, leaks | 0.60 |

Ultralight practice fixes all of these cheaply. Scenarios at 456 lb, 50 mph,
e = 0.75:

| Case | f ft² | L/D max | L/D cruise | hp @ 50 | glide, mi/1,000 ft |
|---|---|---|---|---|---|
| Today | 4.84 | 10.81 | 10.06 | 6.04 | 2.05 |
| Wheel covers, mains only | 4.54 | 11.16 | 10.50 | 5.79 | 2.11 |
| + nose wheel + leg fairings | 4.29 | 11.48 | 10.91 | 5.58 | 2.17 |
| **+ footwell closeout, windscreen** | **3.89** | **12.06** | **11.62** | **5.23** | **2.28** |
| Aggressive, tuned | 3.49 | 12.73 | 12.43 | 4.89 | 2.41 |

**The realistic target is −0.95 ft² (−20% of f): cruise L/D +15%, cruise
power −13%.** On the 103 aircraft that 13% comes back as climb margin on an
engine the audit already called marginal, or as endurance on 5 gallons. It
is the largest single performance number left in the design, and it dwarfs
every aerodynamic refinement the project has argued about.

Three specifics, each borrowed and each with a caveat this aircraft must
respect:

- **Wheel covers on the mains.** Spoked wheels are aerodynamically awful and
  the bicycle world sells snap-on disc covers for pennies and ounces — the
  parts-bin theme continues. **Mains only.** Do *not* cover the nose wheel:
  it castors, and adding side area to a castoring wheel in a crosswind makes
  a weathervane out of the one component already carrying a shimmy-damper
  requirement. Watch mud shedding on grass and brake cooling.
- **Faired legs and cabane.** Round tube runs Cd ≈ 1.2; a cheap fabric or
  formed fairing gets to ≈ 0.15. Pure profit if the fairing does not trap
  water against steel.
- **Footwell closeout and windscreen shape.** This is *newly free*: deleting
  the rudder pedals emptied the footwell, and the rev E pod is
  non-structural, so the shape can be chosen for pressure recovery instead
  of clearance. The two decisions made yesterday opened this door.

**Weight cost ≈ 1.6 lb, and the money is already in the bank:** yesterday's
decisions freed roughly 4.8 lb unbanked (flaps −1, twist grip −2, sling seat
−1.8). **The highest-value use of that margin is buying it back as drag
cleanup**, not letting it evaporate into detail growth.

## 3. There is no pitch trim system. Anywhere.

Not an optimization — **a hole**. `trim-tail.md` is about *aerodynamic* trim
(elevator angle to balance at a given CG), and it fixes tail incidence at
−1.1°. The controls weight ledger is stick 7 lb, pedals 5 (now deleted),
spoileron rig 4. **Nothing lets the pilot relieve stick force in flight.**

Elevator hinge moments at the gate-3 gearing (4.5°/in):

| Condition | Deflection | HM, in-lb | Stick force |
|---|---|---|---|
| Cruise 50 mph, 1 g | 3.0° | 34 | 2.6 lb |
| Slow 35 mph, 1 g | 6.0° | 33 | 2.6 lb |
| Climb 40 mph, full power | 4.5° | 32 | 2.5 lb |
| Vne 62 descent | 2.0° | 34 | 2.7 lb |

**2–3 lb held continuously is squarely in the band that needs trim** on a
2–3 hour endurance aircraft. And it matters *more* here than on a
conventional aircraft, because of a decision made yesterday: the twist grip
put pitch and rudder on **the same hand**. An out-of-trim force is therefore
held by the wrist that must simultaneously make precise small yaw inputs —
the two tasks fight each other in a way pedals never would.

**Recommendation: bungee/spring trim**, the standard ultralight answer — a
spring to the stick base with a small ratchet or friction lever, ≈ 0.4 lb.
No tab, no elevator change, no extra hinge, no flutter surface added to an
aircraft whose flutter analysis does not exist. It uses 8% of the margin
freed yesterday and it should be treated as required equipment, not a
refinement.

## 4. Gap seals — and this aircraft must split the decision

Sealing a control-surface gap is standard cheap practice: roughly ~10% more
control effectiveness plus a small drag credit, for tape or mylar. But it
raises hinge moment by a similar order, and **this aircraft's two surfaces
now have opposite margins**:

- **Elevator: seal it.** More authority per degree is exactly what the
  pending gate-3 flap-flare rerun may need (full flap at forward CG was
  already projected to be tight), and the added stick force is precisely
  what §3's trim system exists to remove.
- **Rudder: do not seal it.** The twist grip closes on a wrist-torque budget
  — ~9 in-lb sustained, ~19 peak, and only *after* a 45% horn balance. A
  ~10% seal penalty pushes the peak to ~21 in-lb, spending hard-won margin
  to buy authority the rudder does not need.

A nice illustration of the project's own rule: a "free" improvement is only
free until you check it against the invariant it touches.

## 5. Ground-adjustable propeller — EAB only

The fleet plan currently buys **two different fixed-pitch wood props** (53 in
compliance pitch for the 103 kit, 60 in cruise pitch for the EAB). The
ultralight world overwhelmingly uses ground-adjustable composite props
(Warp Drive, Powerfin, GSC class) precisely because pitch is the one thing
you cannot predict before flying — and this project has *two* engines, an
unverified static-thrust claim, and a Phase I measurement program.

The catch is weight: composite ground-adjustable hubs run heavier than a
wood prop of the same diameter, and **the 103 kit has ~1 lb of margin — it
cannot pay.** So the honest split:

- **103 kit: wood, fixed pitch.** Unchanged.
- **EAB kit: ground-adjustable is worth serious consideration**, because
  the EAB is the development aircraft, carries the weight easily, and is
  where re-pitching against measured climb and cruise actually pays.

Confirm real hub weights on a scale before committing; the prop trade's
blade-count conclusion (two blades to ~1,750 rpm) is unaffected either way.

## 6. Adjustable horizontal stabilizer incidence — cheap insurance

Kit practice commonly builds shim or jackscrew adjustment into the stab
front attach, because first-flight trim never lands exactly where the
analysis said. **This design has a specific, already-identified reason to
want it:** the pending gate-3 rerun with flap moments expects to need
"a 25° landing notch **or ~1° of tail incidence**." Today that 1° would be a
rebuild; with three shim positions at ±0.5° it is a wrench and an afternoon.

Cost is grams and two extra holes, and it must be decided **before the tail
is welded**, which makes it a now-item rather than a later-item.

## 7. Field rigging deserves to be a requirement, not an outcome

The wing is three-piece removable for a 22 ft garage and 16 ft trailer, but
**no rigging-time requirement exists anywhere**, and Kolb/Quicksilver
practice is emphatic that assembly time is what decides whether a trailered
aircraft actually gets flown. Features that buy it: single-pin or
captive-pin attach, self-aligning bushings, control connections that cannot
be assembled wrong, and a rigging dolly or wing stand so one person can do
it alone.

**Recommendation: adopt a numeric requirement now** — *one person, no
helper, 15 minutes, no tools beyond a single pin puller* — and let it
constrain the joint design, rather than discovering the answer after the
joints are drawn. This is free if decided early and expensive later, which
is the same argument the digital-fabrication trade already won.

---

## Bookkeeping catch: the headline L/D is right for the wrong reasons

While pulling drag numbers, two corrections turned out to have quietly
cancelled:

| Effect | L/D change |
|---|---|
| Slats deleted by the flaps decision (CD0 0.0430 → 0.0373) | **+7.4%** |
| Audit's Oswald correction (e 0.85 → 0.75) | **−6.1%** |
| **Net** | **10.80 vs the 10.7 quoted** |

The README's 10.7 survives — but only because the flaps decision handed back
almost exactly what the Oswald correction took away. **Anyone who fixes one
of these without the other will introduce a real error.** Recorded here so
the coincidence is documented rather than rediscovered.

## What this does not settle

- Every drag number above is an **estimate against a back-solved model**.
  The split between pilot, gear, and cooling is indicative; Phase I glide
  measurement is what makes any of it real.
- VG placement, count, and actual benefit — a flight-line tuning exercise,
  and manufacturer stall-reduction claims in this space are marketing until
  measured.
- Gap-seal material and the real hinge-moment penalty (measure on the built
  surfaces with a spring scale, the same way the spoileron close direction
  is already scheduled to be checked).
- Ground-adjustable hub weights on a scale.
- Whether wheel covers survive a wet grass field without packing mud — try
  before trusting.
