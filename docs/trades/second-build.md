# How Long Does the Second One Take?

**Question asked:** with all the same templates, jigs, and tooling already built,
how many hours is aircraft number two?

**Answer: 370 to 460 adjusted hours, against 575 for the first one** — somewhere
between half and two-thirds. Call it **7 to 9 months at 12 hours a week**, against
about 11 months for the first.

The single largest line item that disappears is not a manufacturing task. It is
the 85-hour *remakes and learning curve* budget, which drops by roughly 85%.

Status: estimate. Everything here sits on top of the Hours sheet in
`analysis/weight-cost-hours.xlsx`, which already carries its own 0.7 correction.

---

## 1. Line by line

Build 1 column is the raw estimate less the digital-fabrication savings from
[digital-fabrication.md](digital-fabrication.md). Retention is the fraction of
that work which survives into a second aircraft with the tooling already in hand.

| Task | Raw | Build 1 | Retention | Build 2 |
|---|---|---|---|---|
| Weld jig and fuselage structure | 130 | 103 | 0.60 | 62 |
| Nose bow, rollover hoop, seat frame | 40 | 34 | 0.70 | 24 |
| Tail surfaces, weld and assemble | 55 | 44 | 0.70 | 31 |
| Spar: cut, drill, rivet | 90 | 76 | 0.70 | 53 |
| Cut and jig 31 fir truss ribs | 45 | 30 | 0.75 | 22 |
| D-tube leading edge | 45 | 38 | 0.70 | 27 |
| Wing assembly, TE, tips, dihedral | 50 | 44 | 0.65 | 29 |
| Spoilerons, hinges, springs | 30 | 26 | 0.70 | 18 |
| Wing joint fittings and fit-up | 35 | 26 | 0.60 | 16 |
| Main gear, nose gear, steering | 50 | 43 | 0.70 | 30 |
| Brakes, rotor adapters, bleed | 20 | 17 | 0.65 | 11 |
| Elevator and rudder runs | 40 | 33 | 0.70 | 23 |
| Spoileron cables, pulleys, rigging | 25 | 21 | 0.65 | 14 |
| Engine mount, install, fuel, exhaust | 55 | 48 | 0.60 | 29 |
| **Cover and finish, 430 ft²** | 120 | 119 | **0.85** | **101** |
| Final assembly, rigging, weigh, debug | 75 | 66 | 0.50 | 33 |
| **Remakes and learning curve** | 85 | 53 | **0.15** | **8** |
| **RAW TOTAL** | **990** | **821** | | **530** |

| | Adjusted (×0.7) | At 12 hr/week |
|---|---|---|
| Original estimate, no tooling | 693 hr | 1.11 yr |
| **Build 1**, with digital tooling | **575 hr** | 0.92 yr |
| **Build 2**, same tooling and templates | **371 hr** | **0.59 yr (7 months)** |

## 2. Sanity check, and an honest range

That bottom-up result implies a **65% learning curve** for unit two. Aerospace
manufacturing normally uses 80–85%.

Landing steeper than the industry norm is defensible here, because the standard
curve assumes you are *also* building tooling and refining process as you go —
both of which are already paid for. But 65% is on the optimistic side of
defensible, so the honest answer is a range rather than a number:

| Method | Build 2 |
|---|---|
| Bottom-up, per task (above) | **371 hr** |
| Textbook 80% curve on 575 | **460 hr** |
| Textbook 85% curve on 575 | 489 hr |

**Use 370–460 hours.** Anything under 350 is wishful; anything over 500 means the
tooling was not actually reused.

If it ever went further, on the same bottom-up curve: unit 3 about 287 hr, unit 4
about 239, unit 5 about 208 — with the covering line increasingly dominating,
because it barely improves.

## 3. Why covering becomes the whole problem

At **101 of the 371 hours — 27% of the second aircraft — covering is by far the
largest single task**, and it is the one thing on the list that digital
fabrication, jigs, and experience all fail to touch. It is 430 ft² of hand work
and it takes what it takes.

This changes the weight of the §14 decision considerably. Oratex buys roughly 75
hours over Stewart for about $1,400, and on a second build that is **20% of the
entire aircraft**. §14 currently leans Stewart on weight grounds. **If a second
aircraft is genuinely on the table, that conclusion should be revisited**, because
the hours case for Oratex roughly doubles when the covering is 27% of the build
rather than 17%.

## 4. What is not in either number

**Design and CAD.** The Hours sheet excludes design time entirely, and the
clean-sheet estimate in §4 of the design log put it at roughly 300 hours. Build 1
pays that plus the time to build every jig, fixture, and printed saddle. **Build 2
pays none of it.** So the real gap between the two aircraft is wider than the
table shows — the table is comparing only the parts that were ever counted.

**Tooling wear.** Printed PLA jigs, plywood fixtures, and CNC-cut boards will not
be pristine after one aircraft. Budget a few hours to reprint saddles and re-cut
anything that has been drilled through, and store the CAD and cut files somewhere
they will still open in five years. That last one is not a joke — the tooling that
matters most on build 2 is the file, not the jig.

## 5. Cost, which changes less than hours

Materials do not learn. Most of the BOM repeats in full. What does not:

| | |
|---|---|
| Tooling line, jig sheet goods, filament, vacuum pump | **does not repeat** (~$550–950) |
| Laser-cut 4130 sheet package | repeats — but nesting and setup are already paid |
| DAR inspection and N-number, $755 | repeats for EAB, **$0 for Part 103** |
| Everything else | repeats in full |

**One actionable thing: order two sets of laser-cut 4130 on the first order.** The
DXF is done either way, and the marginal cost of a second nested set is far below
the first. The same logic applies to spar cap stock and any minimum-order material.
If a second aircraft is even plausible, decide it before that first order goes out.

## 6. The regulatory difference is larger than the hours difference

**Part 103 has no airworthiness certificate, no inspection, no N-number, and no
builder rule.** A second Part 103 aircraft is regulatorily free.

**EAB is not.** Each aircraft needs its own airworthiness certificate and DAR
inspection, and the amateur-built major portion rule applies to each one
separately. Two aircraft built for your own education and recreation is ordinary;
a pattern of building and selling starts to look like manufacturing, and the
repairman certificate that lets the builder sign condition inspections is issued
per aircraft to one builder and does not transfer with a sale.

**None of that is a ruling and it should not be treated as one.** If a second EAB
aircraft is a real plan rather than a thought experiment, ask a DAR before the
first one is finished, not after — it is a cheap conversation and the answer may
change what gets documented during build 1.

## 7. What this does not settle

- Retention factors are judgement, not data. The `build-log/` directory exists to
  replace them with measurements — **log actual hours per task on build 1** and
  this estimate becomes arithmetic instead of a guess.
- Whether the same engine, covering system, and configuration are used twice. Any
  change resets part of the learning curve for that subsystem.
- Whether build 2 is the same configuration at all. An EAB first aircraft and a
  Part 103 second one share drawings but not weights, and the strip-down work in
  the `103 Strip` column is not costed here.
