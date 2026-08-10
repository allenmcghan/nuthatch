# Borrowed Optimizations: What the Ultralight World Does That This Design Hasn't

**The question:** looking at other ultralights, what else is worth stealing?
Script: `analysis/borrowed-optimizations.py`. Sources are marked
**[M]** measured / flight-test · **[B]** builder report, uncontrolled ·
**[V]** vendor marketing — the distinction matters more here than the numbers.

This project is already a borrowing machine — Sky Pup wing, Airbike steel,
Kolb boom, bicycle wheels and brakes, MTB coil-overs, glider Johnson bar,
sling seat. So the useful question is what is *left*. Eight items. Nothing
is adopted except §3, which is a hole rather than an upgrade.

---

## 1. Vortex generators — the flaps decision's real safety net

Design-log §10 justified slats on **roll control**, not stall speed:

> *"Slats specifically, rather than flaps, because there are no ailerons.
> Spoilerons need attached flow over the outer panel."*

§21 deleted the slats. The only mitigation on record is passive — washout,
inboard-only flaps, a model test — behind a 6 lb revert-to-slats escape
clause. VGs are the STOL world's *active* fix for that property.

**The precedent is nearly exact.** The Glasair GlaStar/Sportsman fits
**outboard delta VGs** for this reason and no other: *"when the airflow on
the outboard end of the wing can be made to stay attached, it greatly
improves the roll dampening,"* isolating the outboard section so it behaves
"like a low aspect ratio wing with higher stalling angles of attack" **[B]**.
Wainfan's sizing column states the general case: *"VGs placed upstream of
control surfaces allow increased deflection before flow separation,
improving control effectiveness"* **[M]**. StolSpeed's own placement
schedule tightens spacing to **60 mm for the first 900 mm from each tip**
and 90 mm inboard — tighter *specifically to protect the outer panel*, which
is exactly the spoileron region **[V, with test rationale]**.

**Sizing rules** (Wainfan **[M]**): height ≈ 1.2× local boundary-layer
thickness; BL is 1–2% of distance from the LE, so at 7–10% chord on a 50 in
chord this wing wants **~0.1–0.15 in** — commercial UL vanes are 12 mm
(0.47 in), deliberately oversized to tolerate sloppy placement. Co-rotating:
chord ≈ 4× height, spaced 5–6 heights. Must sit **upstream of the separation
point**. Drag penalty is normally offset downstream *except on laminar
sections* — and 4412 is not laminar, which is favourable here.

**Off the shelf:** StolSpeed **$133.95/80 or $178.85/120**, polycarbonate,
adhesive and templates included, experimental-only. Placement 7% chord
(*"from 8–12% I could detect no difference"*). Micro AeroDynamics is the
STC'd version at $695–1,450 — irrelevant to an experimental/103 aircraft.
**No vendor publishes a kit weight**; a few ounces is the honest estimate,
to be confirmed on a scale.

**The honest negatives, which matter more than the claims:**

- **VGs are not slats.** A CH701 owner who swapped slats for VGs measured
  **400 ft takeoff versus 200 ft with slats** **[B]** — the same nosewheel
  liftoff speed, but double the roll. If this aircraft ever needs the slats'
  *CLmax*, VGs will not supply it.
- **Many Kitfox owners report VGs did nothing at all** on their wing **[B]**.
  Results are wing- and placement-specific.
- The credible drag number is small either way: the FAA STC flight test
  found **1 kt top-speed loss at 12,000 ft full power, none at 75%** **[M]**.
- Stall-reduction claims of 4–9 mph are all **[B]** or **[V]**. Treat as
  unmeasured.
- **No documented case exists of VGs on a two-axis or spoiler-roll aircraft**
  used to preserve outer-panel flow for roll. Instrumenting this would be
  genuinely new data.

**Recommendation: hold the option open as a Phase I development item.** Cost
is zero — the only requirement is that the outer-panel leading edge stay
accessible and bondable, and that the moulded tip cap not preclude vanes.
The payoff is in the *escape clause*: today a wing drop on the model reverts
the airframe to slats; with VGs, the first response is $134 of polycarbonate
and slats become the fallback behind that.

## 2. Drag cleanup: the 80% the audit found and filed away

The audit: *"the smooth airframe is only f = 0.084 m² against the 0.45
carried — ~80% of the drag budget is cockpit, pilot, gear, rigging and
cooling."* It called that housekeeping and moved on, while the project spent
real effort on a tip shape worth 2.9%.

Housekeeping is **3.94 of 4.84 ft²**. Scenarios at 456 lb, 50 mph, e = 0.75:

| Case | f ft² | L/D max | L/D cruise | hp @ 50 | glide, mi/1,000 ft |
|---|---|---|---|---|---|
| Today | 4.84 | 10.81 | 10.06 | 6.04 | 2.05 |
| Wheel covers, mains only | 4.54 | 11.16 | 10.50 | 5.79 | 2.11 |
| + nose wheel + leg fairings | 4.29 | 11.48 | 10.91 | 5.58 | 2.17 |
| **+ footwell closeout, windscreen** | **3.89** | **12.06** | **11.62** | **5.23** | **2.28** |
| Aggressive, tuned | 3.49 | 12.73 | 12.43 | 4.89 | 2.41 |

**Target −0.95 ft²: cruise L/D +15%, cruise power −13%.**

**Frame the payoff as climb, not speed.** Drag *power* goes as V³, so at
50 mph the absolute mph gain is modest — but against 22–31 hp, drag saved is
a large fraction of *excess* power, and excess power is climb. Do not import
RV-world expectations: a fairing worth 0.1 kt at 100 kt is worth 5.5 kt at
250 kt **[M]**, and the +6 to +19 mph figures quoted for wheel pants and leg
fairings are all from 160–200 mph aircraft.

Three specifics, each sourced and each with a caveat:

- **Streamline the exposed tubing — the best-supported item.** KITPLANES
  gives **~1 mph of cruise per 4 ft of round tubing streamlined**, with one
  builder gaining **7 mph from ~28 ft on an experimental ultralight**
  **[B]**. A cylinder runs **Cd ≈ 1.1** at this Reynolds number against
  ~0.05–0.1 faired — a 10–20× reduction, with gear legs called out as the
  worst offenders. Gear legs, cabane, and boom junctions are the targets.
- **Wheel covers on the mains only.** Bicycle disc covers cost ounces. **Not
  the nose** — it castors, and side area on a castoring wheel in a crosswind
  makes a weathervane of the one component already carrying a shimmy-damper
  requirement. Note also that the Alaska STOL community *removes* pants for
  grass and mud; treat covers as removable, not permanent.
- **Footwell closeout and windscreen.** *Newly free*: deleting the rudder
  pedals emptied the footwell and the rev E pod is non-structural, so shape
  can serve pressure recovery instead of clearance.

**What not to copy:** the Quicksilver nose bubble buys **+7 mph for +15 lb**
at $415 **[V]**. On a 254 lb limit that is disqualifying. The 3–5 lb partial
fairing is the version this aircraft can afford.

**Weight ≈ 1.6 lb, already paid for** by the ~4.8 lb §21 freed (flaps −1,
twist grip −2, sling −1.8). Spending it here beats letting it evaporate.

## 3. There is no pitch trim system. Anywhere.

**A hole, not an optimization.** `trim-tail.md` covers *aerodynamic* trim and
fixes tail incidence at −1.1°; the controls ledger is stick 7 lb, pedals 5
(deleted), spoileron rig 4. Nothing relieves stick force in flight.

| Condition | Deflection | HM, in-lb | Stick force |
|---|---|---|---|
| Cruise 50 mph, 1 g | 3.0° | 34 | 2.6 lb |
| Slow 35 mph, 1 g | 6.0° | 33 | 2.6 lb |
| Climb 40 mph full power | 4.5° | 32 | 2.5 lb |
| Vne 62 descent | 2.0° | 34 | 2.7 lb |

2.5–2.7 lb held continuously needs trim on a 2–3 hour aircraft — and more so
here, because §21's twist grip put pitch and rudder on **the same hand**, so
the force is held by the wrist that must also make precise yaw inputs.

A forum objection exists — *"a Part 103 UL has such a narrow operating range
that adjustable trim may be pointless"* **[B]** — and **it does not apply**:
this envelope runs 23 kt stall to 54 kt, and the pilot is 35–45% of gross
across a 105–200 lb range, which moves CG far more than fuel burn does.

**Two options, and the second is more interesting than it first looks:**

1. **Spring/bungee trim at the stick base** — the ultralight standard. The
   AeroConversions system (a trim wheel tensioning **two opposing springs**,
   built for Y-tails that cannot take a tab) is **$95**, roughly
   **2–3 mph of trim speed per turn** on a Sonex **[V]**; weight not
   published. No tab, no hinge, no new flutter surface. Lightest and
   simplest.
2. **Jackscrew-trimmable stabilizer** (Piper J-3 family; a Kitfox option) —
   heavier and more cables, but it **solves three problems with one
   mechanism**: in-flight trim, the ground-adjustable incidence of §6, and —
   critically — it **preserves full elevator travel at every trim setting**,
   which a tab does not. One builder reported his jackscrew installation
   weighed *less* than the fixed one because it replaced the stabilizer
   cross tube **[B]**.

Point 2's third property is not academic here: the flare is this aircraft's
tightest control case (−19.3° of −25° before flaps, and the gate-3 flap
rerun expects it to get tighter). A trim system that eats elevator authority
is spending exactly the wrong currency. **Recommend evaluating the
trimmable stabilizer against spring trim in the gate-3 rerun**, rather than
defaulting to the spring because it is lighter.

## 4. Gap seals — with the real numbers, and the real enemy

My first pass had this backwards. The canonical measurement is **NACA
TN-632**, flight-tested on a Fairchild 22 **[M]**:

- Sealing gained **~20%** effectiveness on 0.18c ailerons, **~33%** on 0.09c
  — *smaller surfaces benefit more*.
- **The design lesson:** sealed 0.09c ailerons matched the effectiveness of
  unsealed 0.18c ailerons **while requiring about one-third the operating
  force.**

So the right question is not "does sealing cost hinge moment" but **"can a
sealed smaller surface do the same job for less force?"** — which is a live
question for a rudder on a wrist-torque budget, not a closed one.

A first-order pass says the answer may be yes, by a lot. Holding yaw
authority constant with ideal thin-airfoil effectiveness and a mid-range
seal factor, the rudder goes from **cf/c 0.50 to ~0.29**, and hinge moment —
seal penalty already included — falls **~57%**:

| | As drawn | Sealed and shrunk |
|---|---|---|
| Rudder chord / VT chord | 0.50 | ~0.29 |
| Effectiveness (τ, × seal) | 0.818 | 0.818 |
| Twist-grip peak, 35 mph full | ~19 in-lb | **~8 in-lb** |

If that survives a real analysis it does more than save effort: it could
**relax the 45% horn balance the twist-grip scheme currently depends on** —
turning a hard requirement into a choice. Treat the number as an estimate
(ideal τ, assumed seal factors) and **do not size on it** — the finding is
that the question must be asked *before the tail is drawn*, when both
variables are still free.

**The real downside is friction, not hinge moment.** Sailplane practice
**[B]** builds a three-layer stack — double-sided tape to the fixed surface,
a pre-curved **mylar** strip bridging the gap, capping tape over its leading
edge — and applies **teflon glass tape to the moving surface as a chafe
strip, specifically to stop a friction-driven rise in control forces.** For a
twist-grip rudder, breakout friction is the one thing that must not creep
in: **the teflon strip is mandatory, not optional.**

Recommendations: **seal the elevator** (authority for the flap flare, and
§3's trim absorbs the force). **On the rudder, treat sealing as coupled to
sizing** — sealed-and-smaller may beat unsealed-and-larger on wrist torque,
per TN-632 — and measure breakout force on the built surface with a spring
scale, alongside the spoileron-close-direction test already scheduled.
Note that **none of this applies to the spoilerons**, which are not hinged
trailing-edge surfaces. Vendor claims of *"roll rate close to 100% higher"*
are **[V]** and unsupported by the NACA data.

## 5. Ground-adjustable propeller — and it need not cost weight

**My EAB-only conclusion was wrong, on one fact:** **GSC Systems makes a
ground-adjustable *wood* propeller** (Tech II/III) — CNC 6061-T6 hub,
laminated maple blades with composite-encapsulated roots, **36–72 in in 2 in
increments** (60 in is stock), and **individually replaceable blades**. That
removes the composite-hub weight penalty that ruled the 103 kit out, and it
directly obsoletes the plan to buy **two different fixed wood props**.

Three supporting findings:

- **Props buy climb, not cruise.** A back-to-back test of nine props
  (EProp, Bolly, Kiev, Warp Drive, Meglin and others) **[M]** found static
  thrust spanning **155–196 kg** and climb **910–1,034 fpm**, while **cruise
  at equal manifold pressure fell within 1–2 kt across all of them** —
  concluding that big cruise claims usually reflect *applying more power*,
  not a better prop. For an aircraft whose binding requirement is a 200 ft
  takeoff roll, this says optimize pitch for the ground roll and ignore
  cruise marketing.
- **Pitch is how you manage a two-stroke's EGT** — *"too much pitch and low
  EGTs, too little and you have high EGTs"* **[B]**. A fixed prop makes that
  a jetting problem instead.
- **Pitch is the cleanest way to set Vh for §103.1(e)(3).** The 103 kit
  already plans a "compliance pitch" prop; ground-adjustable makes the
  compliance setting a wrench rather than a second purchase.

**Blocking fact: GSC publishes no weight or price** (nor does Warp Drive
credibly — ~7–8 lb for a 2-blade is weakly sourced). **Call GSC and Warp
Drive directly; this single number decides the prop question**, because the
103 kit has ~1 lb of margin. If GSC's hub costs more than ~1 lb over a fixed
wood prop, the EAB-only split stands after all.

## 6. Adjustable stabilizer incidence — decide before the tail is welded

Van's RV sets incidence with **shims at the forward spar attach**, and real
post-first-flight corrections are documented: an RV-6A added a second 1/8 in
shim at ~50 hours, moving cruise trim from 3/4 travel to 1/4 and **gaining
2–3 kt**; an RV-9 builder went from 3/16 to 1/4 in shims and **halved** the
cruise trim deflection **[B]**.

An incidence error shows up as permanently deflected trim, which is
permanent trim drag — 2–3 kt out of ~150 on an RV, but a much larger share
of *excess power* on 22–31 hp. The pending gate-3 flap rerun already expects
to want ~1°.

**On a welded cage with a single aluminum boom, retrofitting this means
cutting and re-welding.** It is nearly free at build time and expensive
after. Provide a shim stack or eccentric bushing at the stabilizer front
attach — or adopt §3's jackscrew stabilizer, which delivers this and the
trim system together.

## 7. Field rigging deserves to be a requirement

Sourced one-person times: **Kolb FireFly ~15 min** (wings fold rearward on
universal joints and never detach; struts stay attached at the wing end,
halving the pin count) **[V/B]**; **Aerolite 103** ~20 min off / 30 on
**[V]**; **Sonex** 15 min with two people factory, ~30 min for builders
**[V/B]**.

The features that actually buy speed: **controls stay connected through the
joint** (the slow, error-prone, fatal-if-wrong step), fold rather than
remove, clevis pins with rings instead of bolts, and **wheeled wing dollies
with adjustable stands** so one person never holds a panel.

**The honest caveat for this aircraft:** every fast-rigging example above is
strut-braced. A 31 ft **cantilever** wing has root joints carrying full wing
bending — large pins in double shear plus separate drag/anti-drag fittings —
and panels that are heavy and awkward solo. **Rolling dollies are not a
convenience here, they are the mechanism.**

One dimension check, cheap and worth doing now: the research flagged that a
16 ft trailer will not swallow a 15.5 ft panel. This design is **three**
piece with ~11.5 ft outer panels (§6), so it clears — but confirm the centre
section and dolly footprint against the 16 ft box before the joints are
drawn.

**Recommendation: adopt a numeric requirement** — one person, no helper,
15 minutes, no tools past a pin puller — so it constrains the joint design
rather than being discovered after.

## 8. The Quicksilver precedent — read this one twice

The most directly cautionary evidence found, on an aircraft of nearly
identical size (28 ft span, 156 ft², 250 lb empty, 24 mph stall, 50 mph
cruise). Eipper's MX went two-axis with heavy dihedral; pilots wanted roll
authority; **Eipper added spoilerons, which were "only minimally
effective"**; the next generation got **true ailerons**, which "finally
provided full roll authority" **[B]**.

That is this project's core control decision, tried at this scale, and found
wanting. It belongs in the record.

**The counter-evidence is stronger, and the distinction is the point.**
Kohlman's flight tests of spoiler roll control on three light aircraft (SAE
770441) **[M]** found *"excellent roll characteristics,"* **yaw coupling
with roll input virtually eliminated** (a real prize when the rudder is
already doing double duty), roll rates that **stay high with flaps deployed
at low speed**, and *"very mild nonlinearities"* with **no deadband or lag**
— flatly contradicting the usual folklore.

The critical caveat: Kohlman's aircraft were **designed around spoilers**,
where Quicksilver's were **added to a wing that was not**. This design is in
the first category, which is the reason to expect the good outcome rather
than the bad one — but it converts the quarter-scale model's roll work from
a formality into the item that decides whether the configuration works. The
audit's existing rudder-roll numbers (17–23°/s, ~2 s to 30° bank) are the
prediction; Quicksilver is what failure looks like.

**A gift in the same history:** on the MX, *"the pilot could deploy both
spoilerons at the same time by depressing the rudder pedals. This killed
lift on the wings and allowed the aircraft to get into very short
runways"* **[B]**. The symmetric spoiler mode adopted in §21 is not novel —
it is recovered practice from the closest relative this configuration has.

A structural note worth carrying: spoilers put **almost no torsion into the
wing**, which on a 31 ft cantilever *wood* wing — where torsional stiffness
drives D-tube and spar weight — is a structural argument for the
configuration, not merely an aerodynamic one.

---

## Bookkeeping catch: the headline L/D is right for the wrong reasons

| Effect | L/D change |
|---|---|
| Slats deleted by the flaps decision (CD0 0.0430 → 0.0373) | **+7.4%** |
| Audit's Oswald correction (e 0.85 → 0.75) | **−6.1%** |
| **Net** | **10.80 vs the 10.7 quoted** |

The README's 10.7 survives only because the flaps decision handed back
almost exactly what the Oswald correction took. **Fixing either without the
other introduces a real error.**

## Checked and cleared: the Part 103 stall alarm

The research flagged that 23 kt × √(525/456) = 24.7 kt "busts the Part 103
stall limit." **It does not** — it conflates the two grosses. 456 lb *is*
the Part 103 gross, set by the 24 kt gate; **525 lb is the EAB gross** and
the gear/fitting structural case, and an EAB aircraft is not subject to
§103.1(e)(4) at all. Recorded because the arithmetic looks alarming and will
be re-derived by someone else eventually.

## Two new verification items this survey produced

- **The airspeed indicator will lie during stall testing.** A Belite
  (Part 103) builder found his **ASI failed completely at high alpha because
  the pitot was micro-stalling** on oblique flow — measured 28–32.5 mph
  against 29.1 calculated — fixed by bending the pitot down into the local
  flow **[B]**. This project is chasing a **23 kt stall with ~1 kt of
  regulatory margin**: that number cannot be verified with a misaligned
  pitot. Plan pitot alignment and a calibration method (GPS three-leg or
  trailing cone) *before* first stall testing.
- **BRS installation on a pod-and-boom airframe.** §103.1 excludes the
  chute from the 254 lb empty weight (Kolb cites a 24 lb allowance on a
  254 lb FireFly), but an open cockpit with a single tail boom **has nowhere
  to bury a softpack** — which is why BRS catalogues **VLS (vertical launch,
  top-mounted)** units specifically for the FireFly and FireStar. Ultralight
  systems run **$6,206–7,784**. The rev E architecture should confirm its
  BRS tray suits a VLS or canister unit, not a softpack.

## What this does not settle

- Every drag number is an **estimate against a back-solved model**; the
  split between pilot, gear and cooling is indicative. Phase I glide
  measurement is what makes it real. **No component drag breakdown for
  open-cockpit ultralights exists in accessible literature** — the "pilot is
  the biggest drag item" claim is repeated everywhere and measured nowhere.
- **Three weights nobody publishes**, each blocking a decision: VG kits,
  GSC/Warp Drive hubs, and the AeroConversions trim system. All three want a
  phone call and a scale.
- VG placement and benefit on *this* wing — flight-line tuning, and a real
  chance to generate data that does not currently exist.
- Gap-seal breakout force on the built surfaces, by spring scale.
- Whether wheel covers survive wet grass without packing mud.
