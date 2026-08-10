# Design Log

Decisions in the order they were made, with the number that decided each one and
the alternatives that lost. Read this before the drawings.

---

## 0. How the mission got defined

Started as an all-electric autonomous gyroplane with a prerotator for near-vertical
takeoff. Ended as a two-axis wood-and-steel ultralight. Every step of that
narrowing was driven by a number, and the numbers are below.

**Final mission:** single seat, safe, cheap, trailerable, operable from a
300 × 1000 ft backyard with trees at one end, 200 ft takeoff roll or less, 22 ft
garage storage, 16 ft trailer.

---

## 1. Configuration: why not a gyroplane

Gyroplanes cannot use flaps, glide at L/D 4–5, and need a collective-pitch rotor
head to achieve a short takeoff. Energy per hour of flight is roughly twice a
fixed wing's and per mile is nearly three times.

The collective head is also the highest-risk subsystem available: no commercial
source, blade grips carrying ~10,000 lb of centrifugal force in pitch bearings,
and a failure mode that turns the rotor into a rock. **Rejected on efficiency and
on the fact that a fixed-pitch gyro rotor has almost nothing that can fail, and
adding collective throws that away.**

## 2. Configuration: why not a multirotor

Disc loading governs everything. A single-seat multirotor with stacked props runs
about 13 lb/ft²; a 31 ft wing runs 3.8. Induced power goes as the square root of
disc loading, so the multirotor pays roughly three times more per pound just to
stay up, continuously, with no other lift source.

It also has no energy-out mode. Power loss means falling, and the parachute needs
altitude you do not have in the regime the aircraft exists for. **Rejected.**

Reference point: the Jetson ONE uses 13.5 kWh for about 20 minutes.

## 3. Powerplant: why not electric

Battery capital cost is roughly $500/kWh. Gasoline stored in a tank is about
$3/kWh-equivalent. That is a 150x gap in energy storage cost and no parts list
inverts it.

At 2.5 kWh a pure-electric version of this airframe flies 32 minutes for
$17,500. The same airframe on 5 gallons flies 3.6 hours for less.

**Electric was pursued on the hypothesis that it would be cheaper. It is not.**
The airframe retains an electric conversion path, and at 12:1 glide it needs only
about 7 hp to cruise, which makes it a better electric candidate than most. But
not for version one.

Verified along the way: FAA Chief Counsel (2012) holds that batteries count
toward the 254 lb Part 103 empty weight, and that Part 103 imposes no
reciprocating-engine restriction, unlike light-sport. A hybrid Part 103 is legal.
It just is not cheaper.

**Powerplant priority is gasoline first, hybrid second, electric third.** That
ordering is the project's, not a conclusion of this analysis, and the sections
below are written to serve it.

**Electric, if it happens, is EAB only.** Worked in
[trades/pusher-vs-tractor.md §3](trades/pusher-vs-tractor.md): the Part 103
airframe less propulsion is 206 lb, a 15 kW direct-drive electric group adds
about 40 lb, and that is 246 lb before a single cell. Eight pounds of pack
against the 254 lb cap is 0.6 kWh, or **four minutes**. Part 103 electric is not
a weight-optimisation problem, it is arithmetic. **Part 103 stays gasoline.**

That is a limit of the *rule*, not of the airframe. The same analysis found that
on an equal 5 kWh pack Nuthatch would fly roughly **50% longer than the European
electric ULMs it gets compared to** — about 30 minutes against 20 at 50 mph —
because those aircraft fly under a 330 kg gross limit with no empty weight cap at
all, and glide at about 8 where this one glides at 10.7. Every point of L/D is
endurance that does not have to be bought in cells.

**The $500/kWh figure above has not been re-verified** and it is the number the
whole electric argument turns on. Re-check it against current DIY 21700 pack
costs before citing this section again.

## 4. Airframe: why derive from an existing design

A clean-sheet version of this aircraft came out at roughly 2,000 hours and
$21,000, of which about 300 hours was design work and n=1 at first flight.

The Sky Pup is a 1982 design by a trained aeronautical engineer: 31 ft cantilever
wing, 130 ft², 12:1 glide, stall and spin proof, wood and foam and fabric,
450–600 hour build, roughly 350 built and flown with no reported aerodynamic or
structural problems.

**Deriving from it eliminates the design work and replaces n=1 with n=350.** The
delta for the entire safety package is about 100 hours and $1,900.

## 5. Fuselage: welded 4130, not a wood box

Borrowed from the Ison Airbike, which mates a welded steel tube fuselage to an
all-wood wing and has been in production since 1995 at 251 lb empty.

Weight comes out about even with a wood box. Steel wins on the things being
added: nose bow, rollover hoop, harness anchors, gear mounts, engine mount. Those
all want welded joints rather than wood with gussets.

**Addendum (rev E):** the steel argument only ever applied to the
concentrated-load hardware, all of which lives forward of sta 96. The welded
truss now ends there — a **cockpit cage** — and the tail rides a single
straight boom (Kolb architecture, ~80 fishmouth joints and the aft jig
deleted). The cockpit fairing is non-structural: stringers and fabric over
the cage, shaped freely. Worked in
[trades/fuselage-architecture.md](trades/fuselage-architecture.md).

**Addendum 2 (rev F) — the boom goes back to steel.** Rev E chose 6061-T6 on
weight; re-run over the tube sizes actually stocked, the penalty for
**4130 3.50 × .049** is only **+4.4 lb raw and +2.2 lb net** once the welded
boom-root and tail-post clusters replace a machined sleeve joint and its
bolted brackets. The reason the gap is small: a thin-wall boom is
**buckling-limited, not strength-limited**, and steel's 2.9× stiffness very
nearly cancels its 2.89× density — steel never gets to use its 95 ksi. Two
things then decide it: the aluminium-to-steel transition joint disappears
(one material, one process, and the "copy Kolb's fittings" gate retires),
and **4130 has a true endurance limit where 6061-T6 has none** — an aluminium
boom is a fatigue-managed part behind a vibrating two-stroke, a steel one is
not. **Adopted: all-steel cage + boom, fabric over everything.** Worked in
[trades/cockpit-cage.md](trades/cockpit-cage.md).

## 6. Wing: constant chord, cantilever, 130 ft²

**Constant chord** because 31 identical ribs need one template and one jig.
Tapering costs about 40 hours and saves roughly 3% in induced drag.

**Cantilever, not strut-braced.** Struts drop L/D from 12 to about 10, which is a
20% power penalty. Cantilever costs about 9 lb of cap. Cantilever wins by 8x.

**130 ft², not 150.** The larger wing is better for stall speed and takeoff, but
you cannot shrink a wing later and the 20 ft² is the difference between a Part 103
configuration being reachable and not. Cost is 24 ft of takeoff roll.

**No winglets, and shape the tips instead.** Worked in
[trades/winglets.md](trades/winglets.md). A buildable winglet returns +3 to +4.5%
L/D, which is real — but the wing is already three-piece removable, so the garage
and trailer bound the *panel*, not the span. One foot of span beats a 1.0 ft
winglet and adds 4 ft² of wing on the way past. Winglets exist to buy span
efficiency when you cannot buy span, and here you can.

More to the point, **a properly shaped tip is worth +2.9% off the assumed baseline
and +9.5% against a square-cut tip, for zero weight and zero structure.** The
`e = 0.85` every number in this project rests on is a placeholder with a ±0.05
band, which is wider than the winglet's whole benefit. Fitting winglets before the
Phase I glide measurement is tuning below the noise floor of the model.

Tip mass is also the worst mass on this aircraft. A winglet is a mass *and* a
lifting surface at the tip of an 11.5 ft removable panel that carries the
spoilerons, and it feeds torsion into a joint §13 sized for bending. §12's
stall-limited argument is about load factor and says nothing about flutter —
**for which no analysis exists at any configuration.**

One argument does survive: winglets add effective span without adding *area*, so
unlike a span extension they do not move the Part 103 empty weight. If the 103
configuration ever needs span efficiency it cannot pay for in wing area, this is
where to come back.

Carbon, if they are ever built, is fine here — near-zero CTE against fir's 4 is a
far better thermal match than the aluminium-to-birch bond rejected below, and §7's
"undetectable void" objection does not carry to a secondary surface.

**Moulded carbon tip caps instead, and this one is worth building.** Detailed in
[trades/wingtip-caps.md](trades/wingtip-caps.md). Two plies of 3.7 oz cloth
vacuum bagged comes to 0.54 lb per tip against 0.65 lb for a laminated wood bow
with fabric — **weight neutral**, so none of the tip-mass objection above applies.

The reason is not surface finish. **A Hoerner tip's defining feature is a sharp
lower outboard corner, and fabric over a wood bow cannot hold a sharp edge** — it
shrinks into a radius. A moulded part holds it exactly, so the mould enables a
geometry that is otherwise unbuildable on this wing. Symmetry is the second
reason and it is a handling item: two parts off mirrored moulds are identical by
construction, and with §9's roll authority already "adequate rather than crisp,"
a tip mismatch spends spoileron travel holding a wing up.

Two build notes that belong on the drawing rather than in a note. **Print the
mould female and lay up inside it** — wrapping carbon around a printed plug puts
the tool surface on the inside of the part, and the air only touches the outside.
And **isolate the carbon from the aluminium spar caps with a glass ply and
sealant**: carbon is strongly cathodic to aluminium, the caps run to the tip, and
the resulting corrosion happens inside a closed bay where nothing will be seen
until an inspection that may never happen.

Resin fraction is the whole weight budget — bagged runs 55% fibre, wet hand layup
40%. If it is not going to be bagged, use the light cloth anyway. Heavy twill wet
is +1.9 lb over both tips for nothing.

**Printed ASA tips are a Phase I development step, not the final part.** ASA is
2.0 GPa against 45 for a carbon laminate, and since panel stiffness goes as `E·t³`
it takes 1.4 mm of ASA to match a 0.5 mm carbon skin. With internal ribs at
1.2–1.6 mm that lands at **3 to 4 lb across both tips** — 60–75% of the winglet
mass penalty this section just rejected, arriving through the back door on a part
that was supposed to be free. Better than a winglet, because the mass wraps onto
the tip rather than cantilevering outboard and adds no lifting surface, but not
free.

Print them anyway for Phase I: they cost nothing, item 7 of the flight test plan
already measures glide by timed descent, and that measurement is what says whether
the shape earned its keep. If it did, the printed tip becomes the plug for the
female tool and 2 lb comes back off the tips. If glide did not move, the answer
was a plain wood bow all along.

Two print notes. **0.12 mm layers put the ridge height at 0.06 mm, just under the
0.065 mm admissible roughness at 50 mph**, so a fine-layer print needs no filling
at all — coarser layers do. And do not print or paint them black: black ASA in
direct sun reaches 70–80 °C against a Tg near 100 °C.

**Fibre-filled ASA does not change the answer.** CF-ASA raises modulus 2.0 → 5.5
GPa, which on paper allows a 1.01 mm wall instead of 1.41. But chopped fibre needs
a 0.5–0.6 mm nozzle, and two perimeters at 0.6 is 1.2 mm — the thin wall is
unreachable, and at identical geometry the denser filament comes out *heavier*
(3.13 lb against 3.01). The stiffness cashes out in **rib spacing** instead, about
28% wider bays at the same wall. Meanwhile elongation drops from 10–20% to 1–3%,
which is the wrong trade at the one location on the aircraft chosen partly for
impact resistance. Every printed option lands between 2.6 and 3.5 lb; only a
carbon/epoxy laminate reaches weight-neutral.

Use a filled filament if warping across the printed sections is the practical
blocker — that alone justifies it. Prefer **glass** over carbon if so: less
stiffness, but it keeps 3–6% elongation, needs no hardened nozzle, and comes in
light colours, which settles the solar heating note above for free.

## 7. Spar: aluminum caps and a shear web

Bending is carried at maximum distance from the neutral axis. A wrapped tube puts
most of its fiber near the middle, where it weighs full price and does nothing.

At 128,900 in-lb ultimate root moment and 6.3 in of cap separation:

| | Weight |
|---|---|
| Single aluminum tube, 3.5 × 0.156 | 44 lb |
| Aluminum tube caps + foam/sheet web | 22 lb |
| Carbon caps + foam web | 10 lb |

**Aluminum caps chosen.** Carbon is lighter, but the spar is the one part where a
wet-layup void is both unsurvivable and undetectable. Extruded 6061-T6 arrives
with published allowables and stays inspectable. The 12 lb is about 3% of power.

Caps are 1.25 sch 40 6061-T6. Note that hardware-store aluminum pipe is often
6063-T5, which yields around 25 ksi against 40 for 6061-T6. Buy from a metal
supplier.

Architecture is carried over from a Red Bull Flugtag glider the author built and
flew: tube caps top and bottom, foam spacer, aluminum sheet wrapped from one face
down and under and riveted to the top so it forms a double-thickness web. Changes
from that build: one pipe size up, structural epoxy instead of polyurethane glue,
and hemmed web edges instead of tape.

**Strut position matters more than anything else in spar sizing.** Moving the
attach point from 8 ft to 10 ft dropped ultimate bending at the strut station
from 87,400 to 48,700 in-lb, before the design went cantilever.

## 8. Ribs: Douglas fir truss, not foam

Counterintuitive result, at a 50 in chord:

- Foam rib: 0.22 lb of 1 in core + 0.19 lb of cap strips = **0.41 lb**
- Truss rib: 0.09 caps + 0.06 web members + 0.03 gussets = **0.20 lb**

A solid slab of foam outweighs an open truss even at 1.5 lb/ft³. Thirty-one ribs,
so about 6.5 lb saved, and the truss is stronger per pound because diagonals
carry shear where foam just sits there. Costs about 29 hours.

**Douglas fir, lumber yard, select vertical grain.** Roughly $1/board-foot against
$15–25 for aircraft spruce. Fir is 30% denser than spruce so ribs come to 8 lb
rather than 6.2, and $800 stays in your pocket. You are grading the wood yourself:
vertical grain, six or more rings per inch, no knots or runout, reject grain
deviation worse than 1 in 15.

Wood ribs also permit proper rib stitching and remove the solvent constraint that
foam ribs impose on the covering system.

## 9. Roll control: spoilerons, not ailerons

The Sky Pup is two-axis because the design predates the final Part 103 rule and
the industry expected a 220 lb empty weight limit rather than 254. Ailerons were
omitted to hit a number that was never real. It is not a safety decision, but the
result is a spin-proof aircraft, and that is worth keeping.

Spoilerons over ailerons:
- Proverse yaw rather than adverse, because a raised spoiler adds drag on the
  descending wing
- Still effective at high alpha, where an aileron is stalling
- Cannot be cross-controlled into a spin

Cost is asymmetric response and a deadband. Gliders that use them call it adequate
rather than crisp.

**Single-acting, tension-only, spring return to closed.** Airflow and spring both
push them shut, so a broken or disconnected cable retracts rather than floats.
On a two-axis aircraft a stuck-open spoiler is the one control failure with no
good answer, so this is not optional. One cable per side, differential off a stick
bellcrank, roughly 30% of stick travel as deadband.

**Verify the aerodynamic close direction before flight.** Tape a panel on and
measure with a spring scale at 25 and 35 mph. "Usually wants to close" is not a
design basis.

## 10. Slats: mandatory, not optional

At 496 lb on 130 ft²:

| CLmax | Stall | Takeoff | Landing roll |
|---|---|---|---|
| 1.4 clean | 32.7 mph | 180 ft | 108 ft |
| 1.8 slats | 28.8 | 140 | 84 |
| 2.3 slats + slotted flaps | 25.5 | 110 | 65 |

Slats cost CD0 going 0.0373 to 0.0430, so L/D drops 11.5 to 10.7 and glide from
1,000 ft goes 2.18 to 2.03 miles. Seven percent for 40 ft at each end.

**Slats specifically, rather than flaps, because there are no ailerons.**
Spoilerons need attached flow over the outer panel. A slat keeps it flying well
past where a clean wing breaks.

**And slats are what make the Part 103 configuration legal.** At 450 lb loaded,
power-off stall clean is 27.0 kt against the 24 kt limit. With slats, 23.8.
Empty weight was never the only binding criterion.

Slat gap, chord, overlap, and droop should be copied dimension-for-dimension from
a known installation (CH701, Highlander) rather than derived. Millimeters decide
whether a slat works or is pure drag.

**Addendum — superseded (owner decision 2026-08-09): flaps replace the slats.**
This section's "slats, not flaps, because there are no ailerons" argument
assumed flaps would strip the outer panel; the adopted flap is **inboard-only
(~60% span), leaving the spoileron panels on washed-out outer wing** — the tips
keep flying by geometry, verified on the quarter-scale model before the wing
drawings freeze. The swap nets ~−1 lb, moves the 103 stall margin from 0.1 kt
on an unverified slatted CLmax to ~1.2 kt on better-known aerodynamics, and
deletes the slat cruise drag this section priced at 7% of L/D. Worked in
[trades/flaps.md](trades/flaps.md), which carries the escape clause: a wing
drop on the model reverts this decision.

## 11. Brakes: bicycle hydraulic discs

To decelerate 424 lb at 0.4g needs 85 lb of tire friction per wheel, which at a
6.5 in tire radius is 553 in-lb of wheel torque. Through a 203 mm rotor that is
138 lb of pad force. A four-piston downhill caliper makes closer to 800.

**Two pounds against 12–18 for aircraft brakes.** Single-stop heat load is 23 kJ,
which a downhill bike dissipates repeatedly on a long descent.

This is what lets the Part 103 configuration keep brakes instead of deleting them.
Needs a machined rotor-to-hub adapter and a lever lock, since there is no parking
brake.

## 12. Structural design point: 4.7g limit

The most g a wing can generate is (V/Vs)². At Vne 69 and a 32.7 mph stall, that
is 4.65.

**So limit load is set at 4.7g, ultimate at 7.0.** Above that the wing stalls
before it breaks, at any speed in the envelope, with full elevator. The aircraft
cannot be aerodynamically overstressed.

Going from 4.0 to 4.7 limit costs about 4 lb of cap. Going past 7.0 ultimate costs
weight and buys nothing. **Overbuilding past the stall-limited point is not a
safety margin, it is ballast**, and weight is not free: empty 296 to 360 raises
stall speed and therefore impact energy.

Spend margin instead on fittings, bolt bearing, and bonded joints, which is where
manufacturing variability actually lives.

**Correction, from the end-to-end audit
([trades/design-audit.md](trades/design-audit.md)): this section's argument fails
once §10 fixes the slats.** First the arithmetic: (69/32.7)² is 4.45, not 4.65.
Then the substance: with fixed full-span slats, CLmax 1.8 is always available and
the clean 32.7 mph stall never exists in flight. At the slatted stall the g
available at Vne is **5.74 at the design point** (and 6.7 at light weight) — the
wing *can* be aerodynamically overstressed, and pulling to CLmax at Vne needs 23%
more ultimate than is provided. Recommended fix is raising limit load to 5.74 g
(ultimate 8.6) at a cost of roughly 6–10 lb of cap by this section's own pricing,
which honestly restores the stall-protected property for the aircraft as actually
configured. Alternatives — Vne down to ~62 mph, or a tail-authority analysis
showing CLmax is unreachable at speed — are worked in the audit.

Two adjacent gaps from the same audit: **no negative-g case exists** anywhere
(gusts reach −1.9 at Vc, and the §7 spar web wrap is asymmetric top-to-bottom, so
check reversed bending before drawings freeze), and **fixed-mass fittings should
be sized at the light-weight load factor**, since available g rises as weight
falls. Also note full-throttle level flight reaches ~80 mph against a 69 mph Vne —
pick the fixed prop pitch so the engine runs out of rpm near redline.

## 13. Wing joints: bearing, not shear

At an 8 ft center section the joint sits 4 ft out, where moment is about 72,400
in-lb, so 11,490 lb through each cap.

**Bolt bearing in the tube wall governs, not bolt shear.** A 3/8 bolt through both
walls of 1.25 sch 40 gives 0.105 in² of bearing, about 6,300 lb. Less than half
of what is needed.

The internal solid rod plus external sleeve is what fixes it, adding roughly
0.094 in² more bearing. Even then, **two bolts per cap, four per wing**, which
takes margin from 4% to 108%.

The rod's separate job is preventing the tube from ovalizing at the bolt hole,
which is what makes the published bearing allowable actually apply.

Chamfer the rod nose and hold close tolerance only in the last two inches near
each bolt. Loose lead-in, tight where it matters, or a 20 lb panel balanced on
your knee becomes a wrestling match.

## 14. Covering: Stewart waterborne

Over about 430 ft² of total covered area:

| System | Cost | Weight |
|---|---|---|
| Nitrate/butyrate dope | $900 | 37 lb |
| Poly-Fiber (MEK) | $1,150 | 32 lb |
| Stewart waterborne | $1,400 | 24 lb |
| Oratex | $2,800 | 16 lb |

Wood ribs remove the foam-solvent constraint, so dope becomes available. But dope
is the heaviest and slowest option, at ten to twelve coats with sanding between.
With a Part 103 configuration in play, spending 13 lb to save $500 is the wrong
direction.

Oratex buys 75 hours for about $1,400 and is worth considering if hours bind
harder than dollars.

**Addendum (owner decision 2026-08-09): Oratex adopted.** Hours bind harder
than dollars on this build, and Oratex is also the lightest system on the
table — 8 lb under Stewart, on an airframe with a ~1 lb legality margin. The
[second-build](trades/second-build.md) caveat (covering is 27% of aircraft #2
and Oratex pays the premium twice) is acknowledged and accepted: the second
aircraft is deferred until #1 proves out, and covering #1 in Stewart to hedge
a hypothetical #2 would be optimizing the wrong aircraft.

## 15. Engine: Hirth F-33

Designed specifically to fill the niche of the out-of-production Rotax 277, which
is the Sky Pup's own largest specified engine. 28 hp, 35 lb dry including exhaust,
**dual CDI ignition**, free-air cooling via propeller slipstream, 1,000 hour TBO
at 75% power.

Dual ignition is the reason. It removes the most common two-stroke failure, and
the operating site has trees at the end.

Considered and rejected:

- **Half VW**: 85–90 lb for 28–37 hp, and the light version is hand-prop only.
  Four-stroke reliability and direct drive are real advantages, but 45 lb is not.
- **Kawasaki 440**: snowmobile conversion, never condoned by Kawasaki, production
  ended in the early 1980s. Documented CHT hitting 390°F within a minute of
  full-throttle climb against a 395° limit. This aircraft cruises at 55 mph, which
  is the worst cooling environment a free-air two-stroke could ask for.
- **Paramotor engines** (Polini, Vittorazi): light and cheap, but roughly 300 hour
  TBO against 1,000.

## 16. Propeller: 60 in, two blades, wood

60 in rather than 66 because a 66 in disc needs a 45 in thrustline, and a
thrustline that far above the CG gives pitch-down with power, which is a go-around
hazard near the ground. At 40 in the offset is 16 in and the trim change is 30 lb
of tail load rather than 68.

**Two blades, not three or four.** Fewer blades means less total blade wetted area
at a given diameter. Three costs 1–3%, four costs 3–5%. More blades only win when
diameter is constrained.

**Correction: that is true at 1900 rpm and false at 1600.** Worked in
[trades/propeller-blade-count.md](trades/propeller-blade-count.md). Blade count is
not a free-standing choice — it is downstream of diameter and tip speed. Holding
28 hp through a 60 in disc, dropping 1900 → 1600 rpm requires **1.67× the power
coefficient**, and a two-blade prop cannot carry it: blade loading goes from
Cp/σ 0.77 to 1.29, and the chord needed rises from 4.0 to 6.7 in, an aspect ratio
of 4.5. **The two-blade recommendation and the tip-speed recommendation below
cannot both be satisfied.**

Two blades is comfortable to about **1750 rpm** and marginal by 1700, which is
worth **3–4 dB** — roughly half the claimed benefit — with no change to blade
count, hub, or the carved wood plan. That is the recommendation. The full 8 dB
needs three blades, costs about 1.2% cruise efficiency, and quietly deletes the
carved-prop endgame, because three blades means a bolted hub with individually
rooted blades: a part you buy, not a part you carve.

Four and five blades never pay here. At any rpm the engine can turn they are
*under*-loaded — carrying blade area the engine cannot use — at 2–3% in profile
drag, because on a prop this small the narrower blades lose more to Reynolds
number than they regain in tip losses.

Three blades does win on vibration: a two-blade prop produces a 2P pitch and yaw
excitation that three does not, which is a real fatigue input to a belt redrive
and a welded mount.

**And do not shrink the disc to justify more blades.** 48 in buys 6 in of
thrustline and costs 32 ft of takeoff roll — 172 ft against 140 — which spends
most of the margin to the 200 ft target on a trim problem already priced at 30 lb
of tail load. Disc area is the most valuable thing on this aircraft.

**No winglets on the prop.** Tip acceleration is about 3,000g. A tenth-pound
winglet three inches off the blade axis generates 77 ft-lb of bending at the most
heavily loaded point on the blade. Swept or anhedral tips keep the mass in the disc
plane and are worth 3–6% plus a few dB, but they are molded parts, not carved.

**Cut tip speed instead.** Noise goes roughly as the fifth power of tip speed, so
dropping from 1,900 to 1,600 rpm is about 8 dB and costs nothing but a taller
reduction and more pitch. Nothing else on the list comes close.

Two caveats on that, from the blade-count trade. It does **not** cost "nothing but
a taller reduction" — at 1,600 rpm it also costs the two-blade propeller. And the
8 dB assumes sound *pressure* going as tip speed to the fifth; that reproduces as
−7.5 dB, so the number is consistent, but it is very sensitive to the exponent and
a power-based reading gives roughly −3.7 dB instead. Pin it to a measurement
before spending a redrive ratio on it. Check the available belt ratios too — the
F-33 makes power above 6,000 rpm, so 1,600 at the prop is close to 3.9:1, and the
redrive may cap the tip speed reduction before the aerodynamics does.

Advance ratio only ranges 0.39 to 0.48, which is unusually narrow, so fixed pitch
is correct and constant speed is not worth paying for. Buy a cheap ground
adjustable for Phase I, then carve wood once the pitch is known.

## 17. Transport: removable wings, not folding

Folding was designed first, including a hollow fold pin carrying four coaxial
control cable pulleys so that no control ever disconnected. Removable was chosen
instead because a three-piece wing with 20 lb panels is a one-person ten-minute
job, and the fold pin was concentrating too much function in one fitting.

**Cost of that choice: the control disconnects are back**, and they are the
highest-risk item on the aircraft. Mitigated by spoilerons being single-acting
tension-only with spring return, so a disconnected line fails toward closed.

Locking pins are bright red, permanently lanyarded to the underside of the wing,
and pushed up into place, so an unengaged pin hangs visibly below the wing on
walkaround. The lanyard is for seeing, not for retention: use a spring detent or
quarter-turn cam so vibration cannot walk the pin down.

Preflight is a full-deflection check in both directions with eyes on both
spoilerons, not a tug on the stick.

## 18. Tractor, not pusher — and why that answer is different for electric

Full working in [trades/pusher-vs-tractor.md](trades/pusher-vs-tractor.md). The
baseline is unchanged: nose-mounted tractor.

**Efficiency does not decide it.** A tractor gives away 8–11% of cruise power
scrubbing its own slipstream over the fuselage, the open-cockpit pilot, and the
tail — a bigger penalty than the usual 2–5% quoted for light aircraft, because
this airframe is parasite-dominated and the slipstream covers a lot of it. A
pusher recovers that and then spends 4–7% on propeller efficiency lost to
distorted inflow behind the wing and pylon, plus about 4% on pylon parasite drag.
**Net is 0 to +5% for the pusher, inside the error bar on an `f` that was itself
back-solved from a published glide ratio.** Nobody should switch configuration
for a number that small.

**What decides it is the tail.** A tractor's empennage sits in accelerated flow.
On a two-axis aircraft **the rudder is the roll control**, so an unblown tail
loses authority at rotation, in the go-around, and in the low-and-slow regime the
aircraft exists for. That is a handling argument, it never shows up in a drag
calculation, and it is the strongest single reason this design stays a tractor.
Debris off the nosewheel into the disc on a grass strip is the second reason, and
it also conflicts with the carved wood prop of §16.

**Balance is where it gets interesting.** The gas power group — engine, redrive,
mount, 58 lb — has to move aft as a unit, because the engine must be at the
propeller. That shifts empty CG aft 19 in, which forces the wing 12 in aft, which
drives the trailing edge into the volume the disc needs. Move the prop further
back to make room and the CG follows it, the tail arm keeps shrinking, and the
tail has to grow. It diverges. **A gasoline pusher is not a modification of this
fuselage, it is the Quicksilver/Minifox layout with the pilot forward of the
wing** — a new fuselage, cabane, gear, and tail.

**Electric breaks that loop**, and this is the useful finding:

> An electric drivetrain decouples the mass of the powerplant from the location
> of the thrust. Only the motor must be at the propeller. The pack, controller,
> and HV gear go wherever balance wants them.

Of a ~68 lb electric drive group only about 38 lb is forced aft; the pack becomes
a trim tool rather than a trim problem, and it does not move in flight the way
fuel does. With the prop on a pylon about 32 in aft of the wing TE it closes at
the existing seat station, 29–31% MAC across a 130–220 lb pilot range, no ballast.

**So a pusher, if it ever happens, arrives with the electric conversion and not
before.** For the gasoline aircraft the question is closed.

---

## Configurations that lost, with the number

| Considered | Rejected because |
|---|---|
| Canard, Long-EZ style | Cannot use flaps by definition, since the canard must stall first. 14 lb/ft² wing loading, 66 mph stall, 775 ft takeoff. Rutan's own canard sailplane needed mid-span twist to fight canard downwash and still underperformed conventional ships of the same span. |
| Shorter front wing on a tandem | 25% of lift on 53% of the span generates 3.6x the induced drag it would on the main wing. Comes out 14% worse than a plain monoplane. |
| Equal-span tandem wing | Genuinely good: Prandtl's biplane relation gives 22% off induced drag at 15% gap-to-span. But chords fall to 1.4–2.1 ft, Reynolds number drops to 430,000, and you are building 76 ft of wing and folding four panels. Net win about 8%. |
| Pusher propeller, gasoline | Does not close on balance. The 58 lb power group must move aft as a unit, shifting empty CG 19 in aft; rebalancing drives the wing TE into the propeller disc, and chasing it aft shrinks the tail arm and grows the tail. Net cruise efficiency was only 0 to +5% anyway, and the unblown tail costs roll authority on a two-axis aircraft. See [trades/pusher-vs-tractor.md](trades/pusher-vs-tractor.md). |
| Part 103 all-electric | 206 lb of airframe plus a 40 lb electric drive group is 246 lb before any cells, leaving 8 lb of pack against the 254 lb empty cap. 0.6 kWh, four minutes. Batteries count toward empty weight (FAA Chief Counsel, 2012). Not a weight-reduction problem. |
| Ducted fans | Two 16 in fans have one seventh the disc area of a 60 in prop. Propulsive efficiency 0.50 against 0.78, and static thrust 121 lb against 205. Ground roll would go from 180 ft to about 470. |
| Wing-mounted motors | Distributed propulsion exists to let you shrink a wing. At 3.8 lb/ft² there is no wing to shrink. Two 54 in discs over 40% of span buys maybe 8 ft of takeoff roll, and puts a 150A connection across a joint you mate every flight. |
| Series hybrid | Generator, rectifier, inverter, motor is 0.82 end to end against 0.97 for a belt redrive. 18% more fuel for the same thrust, plus a third machine. |
| Aluminum C-channel bonded to birch spar | Aluminum expands 23.6 µm/m/°C, fir 4. Over a 19 ft spar with a 100°F swing the aluminum grows a quarter inch more than the wood it is glued to, absorbed in shear at the bond line, peaking at the ends. |
| Inflated ram-air wing | Dynamic pressure at 37 mph is 0.024 psi. An inflated 6 in beam carries about 2 in-lb; the tail boom alone needs 37,800. The Goodyear Inflatoplane used about 25 psi with a blower running continuously in flight. |
| Heavy duty aluminum foil as sandwich skin | 0.8–1 mil in O temper at 90–120 MPa, against 0.020 in 6061-T6 at 310. Roughly two hundredths of the strength. |
| Solid foam core wing | 39 ft³ of enclosed volume, so 39 lb of foam in 1 lb/ft³ EPS before any skin. Rutan gets away with it on smaller, thinner wings. |
| Amphibious conversion | The prop kills it first: 60-in disc tips at 10 in AGL sit in the bow-spray zone on any float geometry — the Aventura solves this with a pylon pusher, a fiberglass hull, and 328–390 lb empty, i.e. by not being Part 103. The stall gate leaves ~0 lb for floats at 456 lb gross (floats are excluded from *empty* weight, not from stall), and the 103 engine can't climb the hump. Water is a first requirement, not a feature. See [trades/amphibious.md](trades/amphibious.md). |
| V-tail | NACA equal-projected-area rule: needs the same 45 ft² as the cruciform surfaces it replaces, so no weight saved — the only honest win is two boom junctions instead of four, worthless at a 55 kt cap. Costs a ruddervator mixer, routine saturation when the −19.3° flare meets crosswind rudder on the same two surfaces, and instantaneous adverse roll that fights the rudder-then-dihedral steering this two-axis aircraft turns with. See [trades/v-tail.md](trades/v-tail.md). |

## 19. Fabrication method: digital tooling, not digital parts

Worked in [trades/digital-fabrication.md](trades/digital-fabrication.md). Estimated
**90–160 adjusted hours** across the build, taking 693 to between 537 and 607. The
largest single block is the 85-hour *remakes and learning curve* line, which is
what accuracy upstream actually buys.

**The rule that decides every case: use CNC, laser, and printing for tooling, not
for flight parts.** Tooling has no weight penalty, no fatigue life, and no
airworthiness argument, and a jig that is wrong gets reprinted for two dollars.
§6's tip cap analysis already showed what happens the other way — every printed
option came out 2 to 3× heavier than the laminate it replaced.

Four interventions carry most of it. **One laser-cut 4130 sheet package** for every
flat steel part on the aircraft, which is worth more in symmetry than in hours —
§9 already says roll authority is adequate rather than crisp, and an asymmetric
airframe spends control travel it does not have. **Printed tube coping saddles**,
which apply to the 130-hour fuselage and the 55-hour tail together. **CNC-cut
plywood jigs**, both a fuselage eggcrate and a rib board that makes 31 genuinely
identical ribs, which is what constant chord was chosen for in §6. And **printed
drill jigs with hardened bushings** for the wing joint holes.

Three process notes that belong on the drawings. **Do not laser-cut holes to final
size** — the heat affected zone lands in the bearing surface, and §13 establishes
that bolt bearing governs the entire joint design. Undersize on the laser, ream
after. **Do not laser-cut structural plywood** — char is a weak boundary layer
adhesive cannot bond through, so rout the rib gussets or sand every glue face back
to clean wood. **Print jigs in PLA, not ASA**: it is the most dimensionally stable
common filament, jigs never see sun, and printed fixtures cannot go within a couple
of inches of a tack weld anyway.

**The best use of printing here is not a part, it is a process.** §10 says slat
gap, chord, overlap, and droop decide whether a slat works, at millimetre
resolution, and should be copied rather than derived. Printed bracket sets make
that a measurable parameter — print a set, fly it, change one dimension, print
another. Then the printed brackets end their life as weld fixtures holding the slat
while the real 4130 brackets are tacked. Print to find it, machine to fly it.

**And it does nothing for covering**, which at 120 raw hours is the largest task on
the aircraft. The lever there is material, not method: §14 already prices Oratex at
about 75 hours against Stewart. **That single unresolved decision is worth more
time than every tooling intervention combined.**

**The shop already has five printers, a desktop laser, a desktop CNC, and a Maslow
4 × 8 router**, which removes tooling acquisition from the estimate and makes the
optimistic column the realistic one. Three consequences. The **Maslow enables a
full-size digital loft** — draw once, then cut every template, jig, form and
former at full scale, including the fuselage side-truss layout boards the 130-hour
line currently assumes you improvise. **The desktop laser cannot cut 4130**, so the
sheet package in the trade stays the one outside order. And **five printers make
the coping saddles obviously worth it**, where at one printer the print time merely
competes with coping the tubes by hand.

Two gaps worth closing. There is no lathe for §13's joint rods and sleeves — do not
buy one, **buy precision-ground rod and honed tube stock** instead, since §13 only
needs close tolerance in the last two inches near each bolt. And the carbon tip cap
weight case in §6 depends on vacuum bagging, which needs a $150–300 pump; bagged is
0.54 lb per tip against 1.13 wet-laid, so that pump is the difference between
weight-neutral and a penalty.

**Verify the Maslow's calibration before it cuts the rib jig.** That board defines
the airfoil on all 31 ribs. At a 50 in chord ±1 mm is 0.08% of chord and fine — but
only if it is ±1 mm.

## 20. The common airframe: one structure, both configurations

Worked in [trades/common-airframe.md](trades/common-airframe.md), on top of the
weight scrub. The requirement: the airframe must not change between the Part 103
build and the EAB build — only the powerplant and small additions do.

**It closes.** The invariant airframe is **212 lb** with the full safety package.
The 103 kit (Thor-DS-class engine, 53 in compliance prop) lands at **253.2 lb**;
the EAB kit (F-33 + belt, 60 in prop, windshield, tablet) at **275.7 lb**. Both
balance at 27–34% MAC on the **same wing position** — the engine swap moves CG
about 4% MAC and stays in band, so the wing, cabane, and gear never move.

**The load basis unifies through the absolute-strength framing.** The documented
spar is a 2,331 lb limit / 3,472 lb ultimate structure, and maximum attainable
lift depends only on q. **Placard Vne 62 mph on both kits** and the wing is
stall-protected at every gross with zero added spar weight — resolving the §12
correction (audit Finding 1) by the Vne route for the whole fleet. Load factor
then falls out per weight: 5.1 g available at the 103's 456 lb max, 4.4 g at the
EAB's 526.

**The one real cost: the EAB also lives with Vne 62 and a ~56 mph cruise
placard.** The F-33's surplus becomes climb and short-field margin, not speed.
A 69 mph EAB redline requires the 5.7 g spar on the common structure, which adds
6–10 lb and kills the 103 kit — a common airframe and a fast EAB are mutually
exclusive. If a fast EAB ever matters it is a second spar off the same drawings,
explicitly a different airframe.

Rules that follow, now design requirements: one engine-mount cluster sized for
the heavier engine at light-weight g with per-engine bolt-on adapters; nose and
gear geometry clear the 60 in disc; gear sized at the EAB max gross; all
deletable items (windshield, tablet, BRS bridle) on permanent hard points;
5 gal fuel in both kits; per-kit placards.

**§20 addendum — the fleet plan (see also §21).** Two aircraft, both built to the identical
103-compliant airframe. #1 registers EAB from the start: the stall gate caps the
103 configuration at pilot + fuel ≤ 184 lb, so a 200 lb owner is not legal on it
at any fuel load — EAB is required by the owner's weight before any add-on.
#2 stays pure 103 for the 105 lb pilot, with no N-number, DAR, or inspection.
Design pilot cap 200 lb; fleet max gross 525 for gear and fittings. The BRS tray
gets two permanent positions — sta 40 for the light-pilot aircraft, sta 55 for
the heavy-pilot one, since each fixes a different end of the CG band. Every
airframe carries the hybrid/electric provisions: a 110 lb CG-bay tray at the
carry-through, a nose-to-bay conduit channel, and a 45 lb engine-mount ceiling.
The published design's audience follows the same split: anyone builds the 103;
the EAB kit is the documented growth path on the same structure.

## 21. Owner decisions, 2026-08-09

Five open items closed in one sitting; each points at the trade that priced it.

- **Flaps replace the slats (Path B adopted).** [trades/flaps.md](trades/flaps.md).
  Single-lever plain flap, ~60% span inboard, Johnson bar 0/25/40°, one-piece
  torque tube, VFE 55 mph. 103 stall margin goes 0.1 → ~1.2 kt on
  better-verified aerodynamics; ~−1 lb net (held as margin, not banked, until
  the conversion weight is measured on a scale — the 253.2/275.7 lb ledger
  numbers stand until then). §10's slat arguments superseded per its addendum.
  Escape clause: a wing drop on the quarter-scale model reverts this.
- **Covering: Oratex.** §14 addendum. 75 hours and 8 lb bought for ~$1,400.
- **Second aircraft: deferred until #1 proves out.** The first steel order is
  sized for one aircraft; the DXF nesting is paid regardless, so a second 4130
  set later costs only a repeat shop setup. Revisit after Phase I.
- **Plans are for publication, and the CAD outputs cut files.** The drafting
  standard is set before the first drawing, as
  [trades/digital-fabrication.md](trades/digital-fabrication.md) required:
  3D-first CAD from which DXF and STL fall out, full-size rib templates, a
  materials list with sizes and sources, and an assembly sequence. The
  roughly-triple drafting effort is accepted; this design ships cut files,
  which no other aircraft in its class does.
- **Spoileron servo provision (Junco).** The spoilerons remain the roll/
  crosswind control, manually actuated on this aircraft. Design requirement
  recorded now, while the linkage is undrawn: the spoileron circuit gets a
  **servo attachment provision** so the EAB's Junco tablet can later parallel
  the manual linkage for wing-leveling in crosswind — same pattern as the
  hybrid provisions (grams of bracket now, capability later). The manual
  linkage must always override or back-drive the servo; fail-safe analysis
  joins the EAB autopilot work, not this airframe's critical path.

- **Symmetric spoiler mode: adopted** (owner decision, same date). The
  spoilers get two functions: differential for roll (as designed) and
  **symmetric both-up for glidepath control** — the audit's ~720 → ~480 ft
  improvement on the over-the-trees landing. **Mechanization is deliberately
  open**: the owner may want individual control per side, possibly two
  separate levers. Recorded engineering position for the rigging study:
  differential should stay on the lateral stick motion and symmetric on one
  dedicated lever with a mechanical sum, because the flare needs a hand on
  the stick — two independent spoiler levers puts three controls in two
  hands at the worst moment. Whatever wins, the §9 fail-safe stands:
  spring-return to closed on release, and the symmetric path must never be
  able to hold one side up alone. Decide the lever arrangement before the
  spoileron rigging is drawn; it shares linkage with the Junco servo
  provision above.

Still open after this batch: the spoiler lever arrangement (above), and where
Phase I flight testing happens (needed before the EAB airworthiness
application, not before drawing).

**§21 addendum — controls mechanization decided (owner, same date):** one
stick — elevator fore/aft, spoilerons lateral, **rudder on a twist grip** —
plus the left-hand symmetric spoiler lever; **rudder pedals deleted**. On a
two-axis aircraft this is coherent (rudder-then-dihedral is the turn, and
both roll-producing controls live on independent motions of one wrist), but
it closes physically only with a **~45% horn-balanced rudder and 2.4:1
gearing**: unbalanced, full rudder at 35 mph is ~85 in-lb at the wrist.
Deleting pedals nets ~−2 lb (unbanked), kills the adjustable-pedal
requirement for the 105–200 lb pilot range (seat-only adjustment), and
empties the rev D crush bay's footwell — nothing left to trap feet. Gates:
horn balance sized before the tail freezes; grip/centering-spring behavior
and brake-lever placement verified on the full-size seating mockup. Worked in
[trades/controls-mechanization.md](trades/controls-mechanization.md).

**§21 addendum 2 — seat decided (owner, same date): mesh sling.**
Hammock-style sling mesh between cage rails replaces the framed pan + Confor
foam: cooler, more comfortable, and ~1.8 lb lighter (unbanked). The crash
property is kept, not deleted — a sling alone is a spring, so a 2 in
crushable pad sits ~1.5 in below the 1-g sag point: normal sitting never
touches it, a hard impact crushes it without rebound. Sling carries the
9.6 g × 200 lb case at ~98 lb/in edge tension (~1.5× margin after seam
derate); **static proof test to 1,920 lb required before first flight**.
Harness stays anchored to the cage, never the sling. Worked in
[trades/seat.md](trades/seat.md).

## 22. Borrowed optimizations: what the ultralight world still has to offer

Survey of what this design has *not* mined from the rest of the ultralight
and STOL world, worked in
[trades/borrowed-optimizations.md](trades/borrowed-optimizations.md) with
`analysis/borrowed-optimizations.py`. Six items; none adopted here except
where noted, because five are owner decisions and one is a hole.

- **Vortex generators, as the flaps decision's safety net.** §10 justified
  slats on roll control, not stall speed — *"spoilerons need attached flow
  over the outer panel"* — and §21 deleted the slats. VGs are the STOL
  world's standard active fix for exactly that, weigh ounces, bond to
  Oratex, and are tunable on the flight line. **They cost nothing to hold
  open and they change the escape-clause economics**: a wing drop on the
  quarter-scale model currently reverts the airframe to slats (6 lb, and the
  103 margin with it); with VGs, the first response is a strip of vanes and
  slats become the fallback behind that. Keep the outer-panel leading edge
  accessible and bondable; do not let the tip cap preclude it.
- **The 80% of drag nobody has attacked.** The audit found housekeeping is
  3.94 of 4.84 ft² of flat plate and filed it as housekeeping. Wheel covers
  on the mains (not the castoring nose — side area on a castoring wheel is a
  weathervane), faired legs, and a footwell closeout the deleted pedals just
  made free, total ≈ −0.95 ft²: **cruise L/D +15%, cruise power −13%**, for
  ~1.6 lb. Largest performance number left in the design, and yesterday's
  ~4.8 lb of freed margin is exactly what should buy it.
- **There is no pitch trim system — a hole, not an upgrade.** Elevator stick
  force runs 2.5–2.7 lb across the envelope, and the twist-grip decision put
  pitch and rudder on the same hand, so that force is held by the wrist that
  must also twist for yaw. Fix: bungee/spring trim at the stick base,
  ~0.4 lb, no tab and no new flutter surface. Treat as required equipment.
- **Gap seals — and the sourced answer is subtler than "don't seal the
  rudder."** NACA TN-632 (flight test) gives +20% effectiveness sealing an
  0.18c surface and +33% on 0.09c, and the real lesson is that **a sealed
  smaller surface matched an unsealed larger one at one-third the operating
  force**. So for the twist-grip rudder, sealing is *coupled to sizing* and
  is a live question to ask before the tail is drawn, not a closed one.
  Seal the elevator regardless. **The genuine enemy is friction, not hinge
  moment**: sailplane practice mandates a teflon chafe strip under the seal
  precisely to stop breakout force creeping up — mandatory here, where the
  rudder is worked by a wrist.
- **Ground-adjustable prop — and it need not cost weight.** The EAB-only
  reasoning was wrong on one fact: **GSC makes a ground-adjustable *wood*
  prop** (aluminium hub, maple blades, 36–72 in in 2 in steps, individually
  replaceable blades), which removes the composite-hub weight penalty and
  obsoletes buying two fixed props. Supporting: a nine-prop back-to-back
  test found static thrust 155–196 kg and climb 910–1,034 fpm while **cruise
  fell within 1–2 kt across every prop** — props buy climb, not cruise, which
  is what a 200 ft ground roll wants; pitch is also how a two-stroke's EGT is
  managed, and how Vh is legally set for §103.1(e)(3). **Blocked on one
  number: GSC publishes no hub weight.** If it costs more than ~1 lb over
  fixed wood, the EAB-only split stands after all.
- **The Quicksilver precedent, recorded because it is the cautionary one.**
  The MX — 28 ft span, 250 lb empty, 24 mph stall, near-identical to this
  aircraft — went two-axis with heavy dihedral, added spoilerons that proved
  *"only minimally effective,"* and the next generation moved to true
  ailerons. That is this project's core control decision, tried at this
  scale, and found wanting. The counter-evidence is stronger and the
  distinction is the whole point: Kohlman's flight tests (SAE 770441) of
  aircraft **designed around spoilers** found excellent roll, **yaw coupling
  virtually eliminated**, high roll rates with flaps down, and no deadband or
  lag. Quicksilver's were bolted onto a wing that was not. This design is in
  Kohlman's category — which is the reason to expect the good outcome, and
  the reason the quarter-scale model's roll work is the item that decides
  whether the configuration works at all. Bonus from the same history: the MX
  deployed **both spoilerons symmetrically off the rudder pedals to kill lift
  for short fields** — §21's symmetric mode is recovered practice, not
  invention.
- **Adjustable stabilizer incidence, decided before the tail is welded.**
  The pending gate-3 flap rerun already expects to want ~1° of tail
  incidence; three shim positions at ±0.5° turn a rebuild into a wrench.
- **Field rigging as a numeric requirement**, borrowed from Kolb/Quicksilver
  practice: one person, no helper, 15 minutes, no tools past a pin puller —
  set now so it constrains the joint design instead of being discovered
  after the joints are drawn.

**Bookkeeping catch recorded in the same trade:** the flaps decision handed
back +7.4% of L/D (slat drag deleted) and the audit's Oswald correction took
−6.1%, so the README's 10.7 survives at 10.80 **for entirely different
reasons than the repo states**. Fixing either correction without the other
introduces a real error.

## 23. Fly-by-wire and servo-augmented controls: no, except on one surface

Worked in [trades/fly-by-wire.md](trades/fly-by-wire.md) with
`analysis/fly-by-wire.py`. The question was whether full FBW is worth trying,
or servos supplementing the pilot with manual reversion by cutting power.

**Prior art points the wrong way, and the weight loophole runs backwards.**
Full-FBW ultralights do fly under Part 103 — Pivotal BlackFly (313 lb empty),
Helix (348), Jetson ONE, LIFT HEXA — but they are multirotor/tailsitter eVTOLs
that **cannot be flown by a human without computers**. **No fixed-wing
ultralight, LSA, homebuilt or certified light aircraft anywhere has full FBW
without mechanical reversion** — the closest precedent is NASA's 1972 F-8C,
with an ejection seat. They are legal at 313–348 lb because §103.1(e)(1)
**excludes the ballistic chute and flotation** — ~90+ lb of invisible
hardware. **Servos, computers, wiring and their batteries are not excluded**:
the loophole that makes FBW ultralights legal cannot be used to carry the
FBW.
There is no mechanical system to revert to because none could stabilise
them. FBW appears on ultralights exactly where the airframe is uncontrollable
without it and essentially nowhere else. This aircraft is the opposite case:
its safety is *passive* — Sky Pup stall/spin proofing, no aileron spin mode,
self-righting dihedral, a stall-limited wing. Active protection pays best on
airframes that are passively unsafe.

**Weight closes it.** On the lightest hardware that exists (Garmin GSA 28,
1.4 lb, $975): single-string 3-axis ≈ 9.2 lb, dual-redundant ≈ 17.4, triple —
what the real FBW ultralights use — ≈ 25.6. The 103 kit has 0.8 lb, out by an
order of magnitude. On the EAB single-string fits with +10.1 lb, dual is at
the edge (+1.9), triple is out (−6.3). **The architecture with room to spare
is single-string — precisely the one that must not carry a primary control.**
Power is a second gate: servos draw ~2 A each moving, and many Part 103
engines have a tiny alternator or none, so a control-critical battery needs
full-duration sizing and then a second pack. Every FBW ultralight is an
*electric* aircraft for exactly this reason.

**Hardover, and the twist grip made it worse.** Elevator hardover is
overpowerable — 34 lb of stick at Vne, and a slip clutch limiting authority
to ~11° of 25° keeps override under 15 lb. **The rudder is the problem and it
is self-inflicted**: a pedal rudder lets a pilot push back with a *leg*
(100+ lb); the twist grip caps override at a *wrist* (10–15 in-lb sustained).
A rudder hardover demands 19 in-lb on approach and 61 at Vne. §18 simplified
the cockpit by removing the strongest muscle the pilot had for fighting a
runaway.

**Manual reversion is right; the friction objection became an architecture
rule.** A permanently-coupled slip clutch must sit between normal load and
pilot override — on the twist grip a 9-to-19 in-lb window — so power-off
back-drive leaves ~14 in-lb of dead friction against a 9 in-lb budget. But
the de-clutch escape is **not hypothetical**: the **Garmin GSA 28 uses a
solenoid engagement clutch** that decouples the motor when unpowered, for
"virtually no control system friction with the autopilot turned off", shear
pin deleted. So **engagement-clutch servos mandatory, slip-clutch servos
(Dynon/Trio/TruTrak) disqualified.** The ratio still bites — gear friction is
fixed in in-lb while this aircraft's control forces are unusually small, the
worst ratio of any airframe these products target — and EPS practice warns
that friction compensation runs on the *powered* motor, so a power cut hands
back raw friction plus rotor inertia.

**The Baron, which is the argument that should stick.** A Beech E55 (2019)
suffered pitch-trim runaway with a correctly designed manual override: the
clutch fastener had been overtightened to **45 lb breakaway against a
13 ± 2 lb spec**, and NTSB found the pilot could not physically override it.
The pilot died — and so did a person on the ground inside their own home.
**A slip clutch is not a feature you install, it is one you maintain forever
with a calibrated measurement** — and a Part 103 aircraft has no annual, no
A&P and no mandatory inspection of it, ever. §103.9 (no operation "in a
manner that creates a hazard to other persons or property") is exactly the
rule that fact pattern reaches. Certification arithmetic agrees: Part 23
assumes a 3-second recognition delay (1 on low approach) and operating rules
want twice the altitude loss — at 50 mph that is 220 ft of travel before the
pilot reacts, against 500–800 ft pattern altitude. **A servo with meaningful
authority has no legal operating altitude band in a Part 103 mission.**

**The one exception, and it is already in the plan.** §9 made the spoilerons
single-acting, spring-return-to-closed, because *"a stuck-open spoiler is the
one control failure with no good answer."* That physics does not care whether
the tension came from a cable or a servo — kill power and the surface closes
itself — and a spoileron hardover is the mildest available here, overpowered
by the rudder (and spoilers do not suffer aileron reversal near the stall).
**The §21 spoileron servo provision is not a first step toward FBW; it is the
only surface whose existing fail-safe already covers a servo.** **Caveat from
the sourced pass:** every surveyed autopilot assumes roughly linear aileron
response, and spoilerons are strongly nonlinear with §9's ~30% deadband —
expect PIO or limit-cycle behaviour on the first tuning attempt. Still the
right option; not the easy one.

**There was never a force problem**: elevator 2.6 lb, rudder ~9 in-lb steady,
both solved by the 0.4 lb spring trim and the horn balance already specified.

**What to do instead, in order:** (1) **AoA annunciation, not protection** —
it delivers most of stall protection's benefit with no actuator, no authority
question and nothing that can fail inside the control circuit. Two honest
caveats: **no controlled study quantifies accident-rate reduction from AoA
indicators** (the GAJSC position is a reasoned recommendation, not a measured
outcome), and a complete system is *"not quite two pounds"* — **which the 103
kit cannot afford**, so this is an EAB item (the Junco already supplies the
display and plumbing) and the 103 keeps its stall margin the hard way;
(2) the spoileron servo already planned; (3) electric *trim* if wanted — Ray
Allen T2/T3 actuators weigh **2.5 oz**, *lighter than the 0.4 lb spring*, and
the jackscrew locks rather than flops when power is cut. Trim runaway is
tolerated where surface runaway is not because of four properties that must
all hold — slow, low authority, stops instantly on power cut, residual force
holdable by muscle — and **property four is what failed in the Baron**. The
vendor's "cannot run away" claim is contradicted by builder reports of stuck
switches, chafed wires and welded relays: budget a 1 A breaker, a guarded
switch and a limiting controller; (4) nothing in pitch or yaw. On open-source
autopilots: ArduPilot's own Code of Conduct forbids developers from assisting
manned-aircraft projects — no legal bar for a Part 103 builder, but no bug
triage or peer review either, and there is **no published flight-test report
and no accident report** for a manned ultralight on Pixhawk/ArduPilot, which
is a data void rather than a safety record. The EAB may experiment at altitude as the declared development
platform — it can never make such a system a control the pilot depends on.

## 24. Rev F: the cage, the all-steel airframe, and the frame that does three jobs

Worked in [trades/cockpit-cage.md](trades/cockpit-cage.md) with
`analysis/cage-design.py`; drawn on `drawings/sheets/ST-001.png`.

**The boom returns to steel** (see the §5 addendum): +2.2 lb net, one
material, no transition joint, and 4130's endurance limit against 6061's
absence of one. Rev E's aluminium choice was right on the number it scored
and wrong on the two it did not.

**The cage runs sta 30 to 96 on four longerons**, and its geometry is set by
a convergence rather than by a layout preference. Three independent
requirements land within 2.5 in of each other:

| | Station |
|---|---|
| CG, 30% MAC | 63.0 |
| Front spar, 25% chord | 60.5 |
| Rollover hoop clearing the pilot's head | ~62 |

So they become **one frame at sta 61.5**, which then does three jobs at once:
carries **88% of wing lift** (3,038 lb ultimate, 1,519 per side) straight
into the cage; is the rollover structure over the pilot's head; and sits
**at the CG**, so wing lift feeds essentially no pitching couple into the
fuselage. That last property is the weight saver — a wing pickup offset from
the CG has to react a moment through the longerons, and that is how fuselages
get heavy. The rear frame at sta 80.5 sees only 434 lb and so doubles as the
seat-back and harness-anchor frame for free. Front-spar pickups at z = 64,
±8 in, joined by a cross tube that *is* the carry-through; fittings are
bearing-critical, not bolt-critical.

**The pod is now shaped rather than wrapped** — max section at sta 56 at the
pilot's shoulders, smooth run-out into a visually slimmer 3.5 in boom. One
honest finding recorded: the aft-body closure reaches **21.8° and 26.6°** in
the last two bays against the ~12–15° attached-flow limit, and closing at 12°
would need the taper to start at sta 40, forward of the shoulders. **Some
aft-body separation is inherent to a pod-and-boom with a seated pilot**; it
is already inside the audit's f = 0.45, so it is not a new penalty, but it
fixes the honest moves: start the closure as far forward as the shoulders
allow, keep the run-out unkinked, and do not chase a fully closed teardrop.

**Ledger warning.** All-steel (−2.2) plus the §22 drag cleanup (−1.6) spends
3.8 of the 4.8 lb that flaps, the twist grip and the sling seat freed.
**The margin is now spoken for**; nothing further joins the 103 kit without
finding new weight.

## 25. Rev G: reclined pilot, enclosed cabin, and the wing brought down onto it

Worked in [trades/enclosed-cockpit.md](trades/enclosed-cockpit.md) with
`analysis/enclosed-cockpit.py`. Owner objection: the wing attachment was not
aerodynamic or efficient, the pilot should recline, the windshield should run
from the nose up to the wing, and the cabin should be enclosed with doors.

**The objection was right.** Rev F left **15 in of open air** between the pod
top and the wing underside, with cabane struts crossing it at the widest
station on the aircraft.

**Reclining 35°** drops the head 6.5 in (56 → 49.5). It also swings pilot CG
**5.7 in aft** — +4.3% MAC, at the aft limit — so the **seat moves forward
~6 in** (hip sta 57 → 51) and aircraft CG never moves. The room exists only
because §21 deleted the rudder pedals and emptied the footwell: two decisions
paid for each other without either knowing.

**The wing comes down from chord line 64 to 58** (underside 55, giving 5.5 in
over the head). **The cabane is deleted entirely** — the main hoop at sta 61.5
picks the front spar up directly at the cabin roof, so the load path gets
shorter as well as cleaner.

**Drag: −1.17 ft², f 4.84 → 3.68, L/D max 10.8 → 12.4 (+15%)**; stacked with
the §22 cleanup, **f → 3.08 and L/D 13.6 (+25%)**, glide 2.05 → 2.57 miles
from 1,000 ft. The largest single performance change in the project, and it
came from a shape wanted for looks.

**Weight, and the fleet rule survives:** the cabane deletion is an *airframe*
change worth **−5.5 lb to both aircraft**, taking the **103 kit from 253.2 to
247.7 — margin 0.8 → 6.3 lb**, which more than covers the all-steel boom
(−2.2) and the drag cleanup (−1.6) that had just spoken for everything. The
**enclosure (+7.5 lb net) is an EAB kit item**, exactly like the windshield
and tablet: hard points are permanent grams in the cage, doors bolt on or
stay home. **Aircraft #2 flies open under the same wing on the same cage.**

**Three honest costs recorded.** Roll: the high-wing pendulum arm drops
37 → 31 in above CG, **−16%**, on the aircraft whose roll control *is*
dihedral — expect to put 0.5–1° back, and re-run the aero model before
drawing. Entry: ducking under a 55 in wing is a regression from the 26 in
step-over; doors fix it on the EAB, the open 103 gets a duck-and-sit.
Ventilation: an enclosed cabin in a Tennessee summer is a greenhouse, so
NACA ducts and an openable panel become required equipment — which partly
undercuts the sling seat's cooling rationale (§21 addendum 2). Plus a new
question the open cockpit never had: **egress from an enclosed cabin under a
BRS**, possibly inverted, through doors that share structure with the
rollover hoop.

**§25 addendum — thin-film glazing and ram-air ventilation** (owner
direction; worked in [trades/enclosed-cockpit.md §6](trades/enclosed-cockpit.md)
with `analysis/glazing-ventilation.py`). Glazing is **isinglass-class clear
PVC film, ~20 mil, stretched on the steel frame** rather than Lexan: **3.0 lb
against 8.2**, and the saving compounds because film needs only an edge to
pull against where Lexan needs a frame stiff enough not to crack it. The
enclosure kit drops from 17.0 lb gross to **10.0**, which changes a verdict —
**the Part 103 aircraft can now carry a windshield and vents (no doors) at
250.8 lb, 3.2 lb of margin**, instead of flying open.

**The vents and the film help each other, which was not planned.** A
stretched membrane drums in an airstream unless tensioned; ram air
pressurises the cabin and tensions it from the inside, the inflatable trick.
At 55 mph a 20 in panel bulging 1 in carries **1.34 lb/in** against vinyl's
20+. Design requirement that falls out: **the outlet must be smaller than the
inlet**, or there is no pressurisation and the film flaps.

**Duct sizing is small:** two NACA inlets of ~2 × 2 in (8 in² total) give
**202 CFM at 55 mph**, against the 136 CFM needed to hold the cabin within
10 °F of ambient at ~1,500 BTU/hr. Put them in **rigid structure, not the
film** — a submerged inlet needs a precise 7° ramp it cannot hold in a
membrane.

**Winter, honestly:** film has no R-value, so the cabin gives **still air at
ambient**, not warmth. What it deletes is 55 mph of wind chill — **19 °F at
30 °F ambient, 23 °F at 20 °F**. Two requirements: **a defog trickle that
never fully closes** (a warm pilot inside cold film fogs it instantly), and
**cold-crack-rated vinyl** — ordinary clear PVC embrittles at 20–30 °F where
marine grades go to −20 °F.

**The frangibility claim is corrected.** The intent — push straight through
in an accident — answers the egress question rev G opened, but the mechanism
does not work: plasticised PVC elongates **200–400% before breaking**, so a
shoulder **balloons it like a trampoline** and can be trapped by it. Thin
vinyl is *extensible*, not frangible. **Make the attachment frangible
instead**: bead-in-track or twist fasteners sized to release under a shoulder
push, a zip pullable from inside, and a 2 oz hook knife on the harness. Then
the claim is testable — **proof-test egress on the mockup, both sides, in a
harness.**

**§25 addendum 2 — egress decided: cutters, not a release panel** (owner
decision). A **seatbelt cutter and a film cutter carried in the cab**, with
the film **positively attached** and no release mechanism at all. Better than
the edge-release the trade first proposed, for two reasons: "push through it"
never worked (PVC elongates 200–400% and balloons like a trampoline), and the
release-force window was narrow — a panel must hold ~25 lb of cabin pressure
plus gusts yet let go under a shoulder, and fasteners that satisfy both drift
wrong as UV ages them, while a door departing in flight on a two-axis
aircraft is its own emergency.

**The detail that decides the design: a seatbelt cutter has a shielded hook
blade and cannot puncture.** Against a taut membrane with no edge it does
nothing. So the airframe must supply the start — **a small pre-slit at each
panel's top corner under a tab**, and the cut runs **along the bead track,
not across the middle** (one pass releases the panel; carving a hole in the
middle is slower and needs a point). Carry both tools: hook for webbing and
long runs, a small pointed blade as the backup that can start anywhere.

**Timing:** 86 in of cut releases a door in ~5.7 s at ~15 in/s, plus 2–3 s to
reach and deploy — **7–10 s total.** Fine for ditching or a post-crash exit,
**marginal for fire**, which is the case that sets the standard. Requirements:
**two cutters, one per side; mounted not stowed, findable by feel, retained;
reachable in gloves** (this aircraft flies in winter); and a **timed proof
test** from a fully assembled panel, in a harness, both sides. It does not
cover unconscious or pinned — nothing in this weight class does; the BRS
covers in-flight and the cage covers impact. ~0.3 lb, and it deletes the zip
and the release-force tuning.

**§25 addendum 3 — egress timing corrected, and the hazard it exposes.**
The 7–10 s figure in addendum 2 was wrong: it assumed cutting the whole panel
out. For a thin film **tear propagation is far cheaper than initiation** —
20 mil flexible PVC runs at roughly **10 lbf** of steady pull once a cut
exists — so the real method is **one diagonal cut from a corner, grab the
flap, tear**: about **2 s of work, 4–5 s including reach**. That moves the
fire case from marginal to acceptable, which was the only case in question.
It also settles the tooling: **the pointed film cutter is the primary tool**
(a shielded hook blade cannot puncture a taut membrane and does nothing
without an edge), and the hook cutter earns its place on **webbing**.

**The same property is a flight hazard, and this is the new finding.** A
membrane that tears at 10 lbf once nicked will tear *in flight* once nicked,
and the addendum-1 decision to tension it with cabin pressure primes it. A
stone off the nosewheel, an abrasion at a frame edge, a UV-hardened spot in
year three — any of them can run; at Vne a lifted flap edge peels at well
over 10 lbf. **Mitigation is free, because it is only panel layout: the bead
track is the ripstop.** A tear runs to the edge of its own panel and is
arrested at the frame, so **divide the glazing at every existing cage member**
rather than spanning two big sheets per side, and put the **smallest panels
low and forward** where nicks are likeliest. Explicitly **do not** switch to
scrim-reinforced mesh vinyl: it would stop tears and equally stop the egress
plan — the sling seat uses that material precisely because it must not tear.
Film is a consumable; a nicked panel is replaced, not flown.

**§25 addendum 4 — glazing split: thin Lexan windshield, film doors only.**
Owner refinement, and the right division. **Windshield + upper sides in
0.040 Lexan (3.0 lb), the two doors in 20 mil film (1.4 lb) — 4.3 lb total**,
against 3.0 all-film and 8.2 all-0.060-Lexan. The **+1.4 lb over all-film**
buys two things: the forward view goes through optical-grade rigid panel,
which **deletes the distortion problem a 14–17° raked film screen would have
had**; and the windshield — the one panel actually exposed to stones off the
nosewheel — **cannot propagate a tear at all**, because polycarbonate crazes
locally rather than running like a tensioned membrane.

**That also shrinks addendum 3's tear-arrest requirement.** Film is now only
the doors, which sit high on the sides at sta 40–78, out of the spray, and
are already individually bounded panels. So "subdivide the glazing at every
cage member" **relaxes to: keep each door a single bounded panel**, which it
already is. Scrim-reinforced mesh is still explicitly out — it would defeat
egress.

**Three Lexan-specific requirements that film did not have:** **thermal
float** — polycarbonate expands ~6× steel, so a 40 in screen moves 0.15 in
through a 120 °F swing and needs oversized holes or a floating channel,
**never a hard clamp**; **oil-canning** — 0.040 is thin for a 12 ft² wrapped
panel and may want an intermediate frame member or 0.060 (+1.5 lb), a mockup
check before the frame is welded; and **solvent crazing** — keep it off the
fuel path and specify the cleaning method.

**Fleet consequence:** the split costs the 103 about 1.9 lb, taking its
windshield-and-vents configuration from 3.2 lb of margin to 1.3. Clean
answer: **glazing is a kit item either way.** The EAB takes the Lexan screen,
being the aircraft flown fast, far and in weather; **Avery's 103 can keep a
film screen and hold 3.2 lb** — same cage, same frame, same bead track,
different sheet. The doors stay film in both, so **the egress plan is
identical: the doors are the escape path in either build.**

### Addendum 5 — the glazing becomes geometry, and a shaded render of it

Everything above was carried as prose and a weight line. It is now in the
mesh: `analysis/geometry-mesh.py` **cuts the glazing out of the fabric pod**
and carries it as its own surfaces, so the split is geometry rather than a
note. The pod skin is lofted on a fine grid and masked by station and by
`phi`, the angle around the section from the top centreline:

| Surface | Station | phi from top | Material |
|---|---|---|---|
| `glass` — windshield + upper sides | 14 → 48 (wing LE) | ≤ 45° | 0.040 Lexan |
| `film` — the two doors | 40 → 78 | 48° → 116° | 20 mil PVC |
| `fuse` — fabric | everything else to sta 96 | — | Oratex |
| `boom` — the tail boom | 96 → 184 | — | painted 4130 |

The 3° strip between the two masks is the door header, left as fabric.

**One thing the mesh was missing turned up while cutting the hole**: there was
**no member along the glazing boundary** for the windshield to attach to. The
cage ran longerons and hoops but nothing followed the `phi` = 45° line. Added
as `wsframe` — light tube from sta 14 to 48 both sides plus a bow across the
front. That is the **"windshield frame / floating channel"** line already
carried in the enclosure ledger at 1.0 lb, so **no weight change** — the
ledger was ahead of the geometry, not the other way round.

**`analysis/render-hero.py`** shades that mesh: Lambert + Blinn-Phong,
sky-dome ambient, **Fresnel-weighted transparency** so the glazing goes white
at grazing angles and clear head-on (which is what makes the cage and the
seated pilot visible through it), smoothed vertex normals, projected soft
shadow, and a filmic highlight roll-off. Rib scalloping at the true 11 in
pitch and the paint scheme are **shading only — there are no ribs and no paint
in the mesh.** The pilot figure is built in the render script, not in
`geometry-mesh.py`: he is a prop and does not belong in the STL or on the
drawings.

Outputs `drawings/renders/hero-{ramp,cockpit,air}.png`. **They are renderings
of the design geometry. They are not photographs, and this aircraft has not
been built** — every image carries that on its face.

## 26. Rev H: the whole front is windshield, and the first number for visibility

**Owner direction: "the sight lines and visibility are terrible in these
renderings. The entire front should be a windshield. The engine cowling is the
only thing that's not transparent."**

That is a correct reading of rev G, and the repo deserved a worse verdict than
it got: **there was no visibility number anywhere in it.** Twenty-five sections
of trades, and the enclosure was justified on drag, weight, wind chill and
egress — never on what the pilot can see. Fixed here, and the analysis is what
decides the shape. Script: `analysis/visibility.py`.

### What changed in the geometry

`phi` is the angle around the fuselage section from the top centreline.

| Surface | Station | phi | rev G | rev H |
|---|---|---|---|---|
| cowl | 2 → 22 | all | fabric, and *glazed* above 14 | **opaque, its own group** |
| windshield | 22 → 48 | ≤ **136°** | glazed only to 45° | **glazed to the lower longeron** |
| side lights | 48 → 78 | 20°–46° | fabric | **glazed** |
| doors | 40 → 78 | 48°–116° | film | film, unchanged |

The 136° lower edge is not arbitrary: **the cage's own lower longeron already
sits at phi ≈ 135°**, so the glazing runs down to a member that exists. Nothing
was added to carry its bottom edge.

### Ray-cast from the pilot's eye

Möller–Trumbore against the real mesh, from the eye at sta 58 / z 45.5, over
the whole sphere. Every triangle is tagged by its group, so a ray comes back
glazed, blocked, or clear. Same mesh and same eye for both revisions — only
the masks differ.

| Sector | rev G sees out | rev H | change |
|---|---|---|---|
| whole sphere | 40.0% | **61.3%** | **+21.3%** |
| forward hemisphere | 45.3% | 67.9% | +22.6% |
| abeam, both sides | 51.1% | 73.9% | +22.9% |
| the approach window | 48.9% | 74.7% | +25.8% |
| **ahead and down, ±30°** | **4.2%** | **41.9%** | **+37.7%** |

That last row is the one that matters. **Rev G could see 4% of the sector a
pilot actually uses to land.**

How far down the view reaches, by azimuth (fan test — a 3/8 in tube is not a
wall, so it takes half a ±6° fan going dark to count as blocked):

| Azimuth | rev G | rev H |
|---|---|---|
| straight ahead | −8° | **blocked at the horizon** |
| 10° off the nose | −3° | −5° |
| 20° off | blocked | **−21°** |
| 30° off | −13° | **−47°** |
| 45° and outboard | −41° | −41° |

### Two findings, and one of them is not good news

**1. Straight ahead, rev H is worse on paper — and that is a correction, not a
regression.** Rev G's windshield started at sta 14, so it drew glass across
sta 14–22. **That is where the engine is.** Rev G was crediting the pilot with
a view straight through the powerplant. The cowl now runs 2 → 22 and takes the
fiction away. The straight-ahead view was never there; the model stopped
claiming it.

**2. The cowl is the limit, and glass cannot fix it.** The cowl crown is at
z 47.3 and the eye at 45.5 — **the crown sits 1.8 in above the eye, so the
pilot must look 2.9° UP to clear the nose.** The thrustline is at z = 40
because the propeller has to clear the ground; the engine sits around the
thrustline; the cowl has to cover the engine. There is an **engine** in the
way, not a fairing.

**And the cowl may not even be tall enough.** A crown at 47.3 gives the engine
7.3 in above the crank centreline. **A Hirth F-33's cylinder standing upright
is taller than that.** So either the engine gets clocked or tilted to fit under
this line, or the cowl grows — and if it grows the forward view gets *worse*.
**This is now the open item that decides the forward view, and it is a
powerplant question, not a glazing one.** Nothing is settled until an engine is
on the bench and measured.

What rev H genuinely buys is everything *either side* of the cowl: the aiming
point, the runway edge and the flare picture arrive over the **side** of the
nose, through continuous glazing from the centreline round to the door. Same
technique a Cub pilot uses, without the S-turn, because nothing is opaque
between the two.

### The wraparound is not developable — this is what it costs

Flat sheet cold-forms into **single** curvature only, and the pod's forward
sections are doubly curved. So the screen cannot be one piece: it is a **centre
panel and two side panels per side**, meeting on frame rails at phi 45° and
95°, with bows at the cowl joint (22) and the wing leading edge (48). Same
reason a Champ or a Cub has a split screen.

**Measured off the mesh**, not assumed:

| Line | rev G | rev H |
|---|---|---|
| glass, 0.040 Lexan | 12.0 ft², 3.0 lb | 12.8 ft², **3.2 lb** |
| film doors, 20 mil | 10.0 ft², 1.4 lb | 11.1 ft², **1.5 lb** |
| glazing frame | 1.0 lb (assumed) | **2.6 lb** (303 in of 3/8 × .028 measured) |
| **enclosure kit gross** | **12.4 lb** | **14.4 lb** |

**The frame, not the glass, is the whole delta.** Open item: it has had no
materials pass — aluminium extrusion, a smaller tube, or deleting the phi = 95
rail if 0.060 sheet proves stiff enough are all live.

### What it costs the Part 103 aircraft

| 103, windshield + vents, no doors | Weight | Margin |
|---|---|---|
| rev G, film screen | 250.8 | +3.2 |
| rev G, 0.040 Lexan | 252.7 | +1.3 |
| rev H, film screen | 253.1 | **+0.9** |
| rev H, 0.040 Lexan | 254.5 | **−0.5** |

**The 103 can no longer afford the Lexan nose.** The fleet answer §24 reached
for optical reasons is now load-bearing: **glazing is a kit item.** The EAB
gets Lexan; **Avery's 103 gets film in the same frame and the same bead track**
and holds +0.9 lb. If the 103 wants Lexan, 1.5 lb has to come off that airframe
first.

`drawings/visibility.png` plots the field of view. `drawings/renders/hero-eye.png`
renders it — from the eye, on short final, with the cowl the only thing in the
way.

## 27. The frame becomes data, and the data fails its first check

**Owner direction: CAD files, to start reconfiguring the steel tube layout.**

The useful deliverable here is not a file. It is that the frame stops being
thirty hard-coded `strut()` calls buried in the mesh generator and becomes
**`analysis/frame.py`: a node table, a member table and a stock table** — which
every other script now reads. Move a node and the STL, the drawings, the cut
list, the weight, the renders and the visibility numbers all follow. That is
what makes a layout reconfigurable; a DXF on its own does not.

### What ships

`analysis/cad-export.py` writes, into `cad/`:

| File | What it is |
|---|---|
| `nuthatch-frame-3d.dxf` | 3D wireframe of every tube centreline, layered by structure group, with node markers, labels and datum/station reference lines. R12 ASCII on purpose — everything reads it |
| `nuthatch-views-2d.dxf` | side / top / front on one flat sheet with a station grid and waterlines |
| `nuthatch-frame.scr` | an AutoCAD script that draws the same wireframe with `LINE` commands, for when a DXF import argues |
| `tube-schedule.csv` | cut list: stock, centreline length, weight, and **the tightest joint angle at each end**, because that is what sets the fishmouth |
| `nodes.csv` | every node, mirrored, with the members landing on it |

Inches, aircraft datum, ground at z = 0. And it reads back: `cad-export.py
--from-dxf FILE` parses `LINE` entities out of an edited DXF, diffs them
against `frame.py`, and prints a node table to paste in. Positions only — a DXF
line cannot tell you what stock it is meant to be.

**Recommended CAD: Onshape on the free plan**, whose *Frames* tool sweeps tube
profiles down a wireframe and generates a cut list with miter angles. Its free
tier requires public documents, which for a CERN-OHL-S project is where the CAD
belongs anyway. FreeCAD if it has to be offline and open source; SolidWorks
Weldments is still the best tool for this specific job if it is available.
AutoCAD does what was asked — the DXF is native `LINE` geometry on sensible
layers — it just will not give a cut list back, which is what the round trip is
for. `cad/README.md` carries the workflow.

### And then the check failed

Because the frame is now a graph, a question can be asked that the tube mesh
could not answer: **do these tubes actually meet?** Overlapping cylinders look
welded. `frame.check()` tests degree, connected components, and nodes that sit
*near* a member without being on it.

**The frame is in six disconnected pieces.** Only the 14-node cage box is one
structure. The **rear frame** — rear spar carry-through, seat back and harness
anchor — is an island whose feet sit **2.70 in** off the lower longeron. The
**tail boom** floats 3.00 in between the aft-frame crosses. All three **gear
legs** are islands. The **nose bow is a U, not a hoop** — there is a crown and
no lower cross member — so the nose leg has nothing to attach to at all. And
inside the cage box, **the main hoop feet miss the longerons by 3.44 in** — on
the frame that carries 88% of wing lift and is the rollover structure.

None of this is new damage. It has been in the geometry since rev F and it was
invisible because the only view of it was a picture. **A drawing cannot tell
you whether two tubes meet; a graph can.** That is the whole argument for the
refactor, and it paid for itself on the first run.

**Nothing was moved.** The coordinates are exactly what rev G carried — fixing
this is a design decision about which joints want to be welded and which want
to be bolted fittings, and it is the owner's to make. `frame.py` will re-check
whatever comes back. Listed member by member in `docs/open-questions.md`.

**Also recorded honestly:** the tube schedule totals **48.4 lb** (27.5 cage,
13.2 boom, 7.7 gear) with no gussets, no fittings and no weld metal, against
40 lb in a build-log CSV that predates the pod-and-boom architecture. Those do
not reconcile, and *workbook reconciliation* was already on the list.

**And the visibility numbers moved, by a little.** §26 was computed before the
frame carried real tube stock; the cage members now have their schedule
diameters and the boom is constant-section, so the ray-cast sees slightly more
steel. Whole sphere 61.8 → **61.3%**, ahead-and-down 42.3 → **41.9%**. The
tables in §26 have been restated. Nothing about the argument changes, but the
number in the repo should be the number the script prints.

**One correction fell out of the refactor:** the mesh had been drawing the tail
boom as a **taper**, 7 in deep at the pod junction down to 3.5 at the tail,
while the design of record is a **constant-section 3.50 × .049 tube**. The loft
now takes its radius from `frame.TUBE["boom"]`, so the picture and the schedule
cannot disagree again.
