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

## 6. Wing: constant chord, cantilever, 130 ft²

**Constant chord** because 31 identical ribs need one template and one jig.
Tapering costs about 40 hours and saves roughly 3% in induced drag.

**Cantilever, not strut-braced.** Struts drop L/D from 12 to about 10, which is a
20% power penalty. Cantilever costs about 9 lb of cap. Cantilever wins by 8x.

**130 ft², not 150.** The larger wing is better for stall speed and takeoff, but
you cannot shrink a wing later and the 20 ft² is the difference between a Part 103
configuration being reachable and not. Cost is 24 ft of takeoff roll.

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

**No winglets on the prop.** Tip acceleration is about 3,000g. A tenth-pound
winglet three inches off the blade axis generates 77 ft-lb of bending at the most
heavily loaded point on the blade. Swept or anhedral tips keep the mass in the disc
plane and are worth 3–6% plus a few dB, but they are molded parts, not carved.

**Cut tip speed instead.** Noise goes roughly as the fifth power of tip speed, so
dropping from 1,900 to 1,600 rpm is about 8 dB and costs nothing but a taller
reduction and more pitch. Nothing else on the list comes close.

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
