# Digital Fabrication: Where CNC, Laser, and Printing Actually Pay

**Question asked:** where can 3D printing, laser cutting, or CNC improve time,
quality, and efficiency across the whole project?

**Answer:** roughly **90 to 160 adjusted hours**, taking the build from 693 to
somewhere between 537 and 607. The largest single block of it is not a
manufacturing task at all — it is the 85-hour *remakes and learning curve* line,
which is what accuracy upstream buys you.

**The organizing principle, and it decides every case below:**

> **Use digital fabrication for tooling, not for flight parts.**

Tooling has no weight penalty, no airworthiness argument, no fatigue life, and no
UV exposure. A printed jig that is wrong gets reprinted for two dollars. A printed
flight part costs weight forever — [wingtip-caps.md](wingtip-caps.md) already
worked one case and every printed option landed 2 to 3× heavier than the laminate
it replaced. That result generalises.

**And the timing is right.** `open-questions.md` opens with *"Nothing in this
project is drawn yet."* Everything here has to be drawn anyway. **Drawing it so
that it also outputs DXF and STL is nearly free at this stage and expensive to
retrofit.** This is a decision to make before the first drawing, not after.

Status: recommendation. No drawings committed.

---

## 1. Where the hours are, and what can be taken out

Raw hours from the Hours sheet of `analysis/weight-cost-hours.xlsx`, with the
project's own 0.7 experience factor applied at the end.

| Task | Raw hr | Conservative | Optimistic | Intervention |
|---|---|---|---|---|
| Weld jig and fuselage structure | 130 | **−20** | **−35** | CNC ply eggcrate jig; printed tube coping saddles; laser 4130 gussets |
| Nose bow, rollover hoop, seat frame | 40 | −4 | −8 | printed bend formers, laser-cut tabs |
| Tail surfaces, weld and assemble | 55 | −8 | −15 | same coping saddles; laser-cut hinge and horn set |
| Spar: cut, drill, rivet | 90 | −10 | −18 | printed cap-separation spacers, drill templates, CNC web |
| Cut and jig 31 fir truss ribs | 45 | **−12** | **−18** | CNC rib jig board, routed ply gussets |
| D-tube leading edge | 45 | −5 | −10 | CNC-cut ply developments, printed bend forms |
| Wing assembly, TE, tips, dihedral | 50 | −4 | −8 | printed dihedral and incidence setting fixtures |
| Spoilerons, hinges, springs | 30 | −3 | −6 | laser-cut hinge and horn set |
| Wing joint fittings and fit-up | 35 | −6 | −12 | CNC rods and sleeves, printed reaming jigs |
| Main gear, nose gear, steering | 50 | −5 | −10 | printed bend formers, laser-cut mount plates |
| Brakes, rotor adapters, bleed | 20 | −2 | −4 | CNC rotor-to-hub adapters (already planned in §11) |
| Elevator and rudder runs | 40 | −5 | −9 | laser-cut bellcranks, horns, brackets |
| Spoileron cables, pulleys, rigging | 25 | −3 | −5 | laser-cut brackets, printed pulley cages |
| Engine mount, install, fuel, exhaust | 55 | −5 | −10 | printed mock-up engine, laser-cut mount tabs |
| **Cover and finish, 430 ft²** | **120** | **0** | −3 | **almost nothing — see §5** |
| Final assembly, rigging, weigh | 75 | −6 | −12 | better upstream fit-up |
| **Remakes and learning curve** | **85** | **−25** | **−40** | **the big one — accuracy moves into CAD** |
| **TOTAL** | **990** | **−123** | **−223** | |

| | Raw | Adjusted (×0.7) | At 12 hr/week |
|---|---|---|---|
| Baseline | 990 | **693 hr** | 1.11 yr |
| Conservative | 867 | **607 hr** | 0.97 yr |
| Optimistic | 767 | **537 hr** | 0.86 yr |

The 750-hour target was already being met at 693. This is not about hitting the
target — it is about **quality and margin**, and about the fact that a fifth of
the saving comes from simply not making parts twice.

Treat these as estimates of estimates. The Hours sheet already applies a 0.7
factor described as *"your estimate of my estimates,"* and this table sits on top
of that.

## 2. The four that matter most

### A. One laser-cut 4130 sheet package

**The single highest quality-per-dollar move in the project.** Every flat steel
part on the aircraft — cluster gussets, bracket tabs, bellcranks, control horns,
hinge plates, gear mount plates, seat and harness anchor plates, engine mount
tabs, tail attach fittings — is a 2D profile in sheet. Nest them all on one or two
sheets, send one DXF, and every one comes back identical, symmetric, and to
drawing.

This is worth more in **quality** than in hours. Hand-cut and filed steel brackets
are where a one-off airframe accumulates asymmetry, and §9 already flags that
spoileron roll authority is *"adequate rather than crisp"* — an aircraft that is
not symmetric spends control travel it does not have.

**Caveat, and it is not optional.** Laser-cut 4130 has a hardened, brittle heat
affected zone at the edge, typically 0.005–0.015 in deep. Two consequences:

- Dress the edges of any fatigue-loaded part.
- **Do not laser-cut holes to final size.** Laser holes are slightly tapered and
  put HAZ directly in the bearing surface. §13 establishes that **bolt bearing in
  the tube wall governs the entire wing joint design** — undersize every hole on
  the laser and ream to final size afterward.

### B. Printed tube coping saddles

The fuselage is welded 4130 and every tube end has to be fishmouthed to fit the
tube it meets. Hand coping with a hole saw or grinder is slow, and it is where
fit-up error compounds into a fuselage that is out of square.

Model the joint in CAD, generate the intersection, and print a **clamp-on saddle
that wraps the tube and guides the cut**. Cheap, reusable across identical joints,
and it converts a skilled eyeballing task into a tracing task.

This is the biggest single hour saving in the table because it applies to the
130-hour fuselage and the 55-hour tail both.

**Print jigs in PLA, not ASA.** PLA is the most dimensionally stable of the common
filaments (~0.2–0.3% shrink against 0.5–0.8% for ASA and ABS), stiffer, and
cheaper. Jigs live indoors and never see sun or heat, so ASA's advantages are
irrelevant. The ASA guidance in [wingtip-caps.md](wingtip-caps.md) is for parts
that fly.

**But printed jigs cannot go near a weld.** Tack welding radiates enough heat to
soften PLA within an inch or two. Printed saddles are for **cutting and drilling
only** — the weld jig itself needs steel or plywood locators.

### C. CNC-cut plywood jigs: the fuselage eggcrate and the rib board

Two separate jobs, same technology.

**Fuselage jig.** Cut station profiles from plywood on a router, slot them onto a
spine, and the fuselage is located in three dimensions by geometry rather than by
measurement. This is the classic eggcrate jig, it is a natural CNC job, and it
replaces a substantial part of the 130-hour line that is *building the jig* rather
than building the aircraft.

**Rib jig.** §8 specifies 31 Douglas fir truss ribs at 75 minutes each. A CNC-cut
baseboard with a locating pocket for every truss member turns each rib into
drop-in-and-glue. Combined with pre-cut gussets this is realistically 75 minutes
down to 45–50, and — more valuable — **31 ribs that are actually identical**,
which is what a constant-chord wing was chosen for in §6.

**Caveat: do not laser-cut structural plywood.** A laser leaves a charred edge,
and char is a weak boundary layer that adhesive cannot bond through. For the ply
gussets that carry rib shear, **CNC rout them** — or laser them and sand every
glue face back to clean wood, which gives the hours back. Laser is fine for
non-structural templates, patterns, and jig parts.

### D. Printed drill and reaming jigs

The highest-consequence holes on this aircraft are the wing joint bolts. §13 sizes
them on **bolt bearing in the tube wall**, and notes the internal rod's job is
*"preventing the tube from ovalizing at the bolt hole, which is what makes the
published bearing allowable actually apply."* That allowable assumes a clean,
round, correctly located hole.

Printed drill jigs with pressed-in hardened steel bushings are cheap and turn hole
location and squareness from a skill into a fixture. Apply to the spar cap bolt
patterns, the rib-to-spar locations, and every fitting pattern that has to match
across a joint mated every flight.

## 3. The special case: slat geometry

§10 says slats are mandatory and that *"slat gap, chord, overlap, and droop should
be copied dimension-for-dimension from a known installation rather than derived.
Millimetres decide whether a slat works or is pure drag."*

**This is the best use of printing in the project, and it is not a part — it is a
process.** Print bracket sets that hold the slat at a known gap, overlap, and
droop. Change one dimension, print another set, compare. It converts a parameter
nobody wants to derive into something that can be measured on the aircraft.

**Print to find the geometry. Machine or weld it to fly it.** Slats carry
substantial load at high alpha, and the loss of one on a two-axis aircraft is a
roll upset against roll authority §9 already calls adequate rather than crisp. The
printed brackets should end their life as **weld fixtures** that hold the slat in
position while the real 4130 brackets are tacked.

Same pattern applies to the cockpit geometry open question — print or CNC a
full-size seating mock-up rather than deriving stick, pedal, and throttle
positions on paper.

## 4. Straightforward printed flight parts

Small, non-structural, and genuinely fine to print in ASA:

- Junco tablet mount and instrument pod
- Cable fairleads, pulley cages, cable exit fairings
- Inspection covers and access hatches
- Vent scoops, tank fittings, fuel line clamps
- Wire looms and standoffs
- Control stick grip
- Placards
- Wingtip caps — worked separately in [wingtip-caps.md](wingtip-caps.md)

The rule that keeps this safe: **nothing in a primary load path, and nothing whose
failure removes a control.** A printed fairlead that cracks is a nuisance. A
printed pulley bracket that lets a spoileron cable jump its sheave is not, so that
one is laser-cut steel.

## 5. Where it does not help, and this is worth saying

**Covering is 120 hours — the single largest task — and digital fabrication does
essentially nothing for it.** Printed rib-stitch spacing guides are worth a couple
of hours and that is all.

The lever on covering is **material choice, not fabrication method.** §14 already
prices it: Oratex buys about 75 hours for roughly $1,400 against Stewart. That one
decision is worth more time than every intervention in §2 combined, and it is
already sitting in the design log unresolved.

If hours genuinely bind harder than dollars, **settle the covering system before
buying a CNC router.**

## 6. Given the shop that actually exists

The shop is **five 3D printers, a desktop laser cutter, a desktop CNC, and a
Maslow 4 × 8 CNC router.** That removes the tooling-acquisition question entirely
and changes three of the conclusions above.

### The Maslow is the one that changes the workflow, not just a task

A 4 × 8 work area is larger than every part on this aircraft except the spar. That
makes a **full-size digital loft** possible: draw once in CAD, then cut every
template, jig, form, and former at full scale from sheet goods. That replaces the
traditional mylar-lofting workflow rather than accelerating it, and it is the
single biggest capability in the list.

What it should cut:

- **Fuselage side-truss layout boards.** The fuselage is about 190 in, so two
  spliced sheets. Pocket or engrave the truss geometry full size, pin the tubes to
  it, and tack. This is how tube fuselages get built accurately, and it is the
  method the 130-hour line assumes you improvise.
- **The fuselage eggcrate station jig.** Two to three sheets.
- **The rib jig board.** Entire jig on one sheet.
- **D-tube bending forms**, and the developed 1/16 birch ply shapes themselves.
- **Gear leg bend formers**, wing assembly cradles, tail rib templates.

**Verify the calibration before trusting it.** A Maslow is a belt-and-sled machine
with accuracy in the region of 1/32 in over a sheet, which is fine for jigs and
templates and not fine for fittings. Cut a large test rectangle and measure the
diagonals before cutting the rib jig, because that jig defines the airfoil on all
31 ribs. At a 50 in chord, ±1 mm is 0.08% of chord and acceptable — but only if it
is ±1 mm and not ±4.

**Thin ply needs hold-down.** 1/16 in birch on a router wants a sacrificial board,
a downcut bit, and either vacuum or tape-and-CA, plus tabs. Otherwise it lifts.

### The desktop laser cannot do the part that matters most

A desktop laser does thin plywood, templates, patterns, and marking. **It does not
cut 4130 sheet.** The single highest-value intervention in §2A therefore stays an
outside order — a laser, plasma, or waterjet service — and it is the only thing on
this list that has to leave the shop.

Everything in §2C's caveat still applies to the laser: it chars plywood, and char
is a weak adhesive boundary. **Rout the structural rib gussets on the desktop CNC;
use the laser for non-structural templates and patterns.**

### Five printers changes throughput, which changes what is worth printing

The 12–20 mould sections in [wingtip-caps.md](wingtip-caps.md), and the hundred-odd
tube coping saddles in §2B, stop being a month of printing and become a few
overnight runs. Two consequences:

- **Coping saddles become obviously worth it.** At one printer the print time
  competes with just coping the tubes by hand. At five it does not.
- **The tip cap decision gets cheaper on both branches.** Print the ASA tips for
  Phase I *and* print the female mould, because neither is now a scheduling
  problem. The measure-then-decide sequence stands, but nothing is gated on print
  time.

### The desktop CNC covers the fittings, with one substitution

It should do the **rotor-to-hub adapters** (§11, currently "machine yourself"),
bracket blanks, spacers, and drill-jig bushing plates.

**What is missing is a lathe**, for §13's internal joint rods and external sleeves.
Do not buy one for this. §13 only requires close tolerance *"in the last two inches
near each bolt"* — so **buy precision-ground rod and honed tube stock**, which
arrives round and on-size, and machine nothing but the chamfer and the holes. That
removes the lathe from the critical path entirely.

**Also missing: a vacuum pump.** The carbon tip cap weight case in
[wingtip-caps.md](wingtip-caps.md) depends on bagging — 0.54 lb per tip bagged
against 1.13 lb wet-laid. A pump is $150–300 and it is the difference between the
cap being weight-neutral and being a penalty.

## 7. Cost, revised

| | |
|---|---|
| Laser-cut 4130 sheet package (**the only outside order**) | $300–600 |
| Sheet goods for jigs — MDF and ply, 5–8 sheets | $120–250 |
| Filament, tooling only | $80–200 |
| Vacuum pump and bagging consumables | $150–300 |
| Precision-ground rod and honed tube stock (replaces lathe work) | in BOM |
| Machined rotor adapters, bracket blanks | in BOM, now in-house |
| **Net add** | **$650–1,350** |

The BOM carries a 30% contingency line, roughly $3,300. This fits inside it, and
some of it returns as material not wasted on remakes.

The $150–400 CNC jig line from the first version of this estimate is now sheet
goods only. The machines are already paid for, which means **the optimistic column
in §1 is the more realistic one** — most of the gap between conservative and
optimistic was tooling access and print throughput, and neither is a constraint
here.

## 8. The strategic argument, for an open-hardware aircraft

The README licenses this under CERN-OHL-S and says the two files worth reading
first are the design log and the measured weights, because *"drawings exist for a
dozen aircraft in this class. Reasoning does not."*

**The same gap exists in fabrication data. Nobody in this class ships DXF and STL.**

If the CAD is built to output cut files, then publishing them costs nothing and
gives a builder something no other Part 103 design offers: send one file to a
laser service and every bracket on the aircraft arrives correct. That directly
addresses the open question about *"drafting for yourself or for publication"* —
cut files are worth more to a second builder than full-size rib templates, and
they are a by-product of drawing it this way rather than extra work.

It also makes the *"you are the manufacturer"* disclaimer more honest, not less:
a builder reproducing geometry from a file is far less likely to introduce the
silent asymmetries that hand fabrication produces.

## 9. What this does not settle

- Every hour figure here is an estimate applied on top of estimates that already
  carry a 0.7 correction factor. Treat the *ranking* as more reliable than the
  totals.
- Maslow calibration. The rib jig defines the airfoil on all 31 ribs, so the
  machine's real accuracy over a full sheet needs measuring before it cuts that
  board — not assuming from the specification.
- CAD hours. This assumes the aircraft gets drawn in 3D, which is not obviously
  the plan — the Hours sheet excludes design time entirely, and the clean-sheet
  estimate in §4 of the design log put design work at about 300 hours.
- Which parts are structural enough to need HAZ removal after laser cutting.
  That is a per-fitting call and belongs on the drawings.
- Whether laser-cut covering fabric is viable. Polyester edges seal under a laser,
  which is interesting, but there is no precedent in aircraft covering and this is
  not the project to establish one.
