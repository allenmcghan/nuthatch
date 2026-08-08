# Trade: Wingtip Winglets

**Question asked:** carbon fibre winglets on the tips?

**Answer:** they work — about +3 to +4% L/D for a realistic size — but they are the
wrong lever on this aircraft, for three reasons that stack:

1. **Span is not constrained here.** The wing is already three-piece removable, so
   the 22 ft garage and 16 ft trailer bound the *panel*, not the span. A plain span
   extension gives the same benefit or better, and adds wing area on the way past.
   Winglets exist to buy span efficiency when you cannot buy span. You can.
2. **The tip shape has not been spent yet, and it is free.** The whole calculation
   rests on a baseline span efficiency `e = 0.85` that is an assumption, not a
   measurement. The uncertainty band on that number is wider than the winglet's
   benefit. **Fix the tip first, measure, then decide.**
3. **Tip mass is the worst mass on the aircraft.** A winglet is simultaneously a
   mass and a lifting surface at the wingtip, on an 11.5 ft removable panel that
   carries spoilerons.

Status: analysis only. Nothing in the design has been changed.

---

## 1. How much drag is even available to attack

A winglet acts only on induced drag. On Nuthatch at 496 lb, slats installed:

| Speed | Parasite | Induced | Induced share |
|---|---|---|---|
| 35 mph | 1218 W | 2131 W | **64%** |
| 40 mph | 1818 W | 1864 W | 51% |
| 45 mph | 2588 W | 1657 W | 39% |
| **50 mph (cruise)** | 3550 W | 1491 W | **30%** |
| 55 mph | 4725 W | 1356 W | 22% |
| 60 mph | 6134 W | 1243 W | 17% |

At cruise you are attacking **a third of the drag**. A 10% cut in induced drag is
3% of cruise power. The leverage is limited before you start.

## 2. What a winglet actually returns

A well-designed vertical winglet of height `h` behaves roughly like an effective
span increase of `0.45·h` per side. Adding wetted area at `Cf = 0.006`:

| Height | Effective span | Junction | Added f | L/D | vs 10.72 |
|---|---|---|---|---|---|
| 1.0 ft | 31.90 ft | perfect fillet | 0.0018 m² | 11.01 | **+2.7%** |
| 1.0 ft | 31.90 ft | realistic homebuilt | 0.0032 m² | 10.99 | +2.6% |
| **1.5 ft** | **32.35 ft** | perfect fillet | 0.0040 m² | 11.14 | **+4.0%** |
| 1.5 ft | 32.35 ft | realistic homebuilt | 0.0072 m² | 11.11 | +3.6% |
| 2.0 ft | 32.80 ft | perfect fillet | 0.0071 m² | 11.26 | +5.1% |
| 2.0 ft | 32.80 ft | realistic homebuilt | 0.0128 m² | 11.20 | +4.5% |

So **+3 to +4.5% L/D** for something buildable. That is a real number, not a
rounding error, and it is the honest case *for* winglets. In glide terms, 1.5 ft
winglets take the 1,000 ft glide from 2.03 to 2.10 miles — about 370 ft of extra
reach.

Note how little the junction quality changes the answer. That is because the
winglet's own wetted area is small; the risk in a homebuilt winglet is not
parasite drag, it is getting the *cant, toe, and twist* wrong, which is not
modelled above and can turn the whole benefit negative. Winglet toe-out of a
couple of degrees is enough to do it.

## 3. The alternative that is never costed: more span

The wing comes apart into an 8 ft centre section and two 11.5 ft panels. **The
storage constraint binds the panel, not the span.** Nothing stops the span
growing except spar weight.

| | Span | Area | L/D | vs base | Stall |
|---|---|---|---|---|---|
| baseline | 31.0 ft | 130.0 ft² | 10.72 | — | 28.8 mph |
| +1 ft | 32.0 | 134.2 | 11.01 | **+2.8%** | 28.3 |
| +2 ft | 33.0 | 138.3 | 11.30 | **+5.5%** | 27.9 |
| +3 ft | 34.0 | 142.5 | 11.59 | +8.2% | 27.5 |

**One foot of span beats a 1.0 ft winglet. Two feet beats a 2.0 ft winglet.** And
a 1.35 ft span extension matches the effective span of a 1.5 ft winglet while
adding 5.6 ft² of wing — which the winglet does not — lowering stall speed,
takeoff roll, and landing roll along with it.

The counter-argument is root bending moment, and it is legitimate: span extension
puts lift further outboard and drives spar weight, whereas a winglet's side force
contributes less to vertical root bending. But §6 already priced this trade at
"cantilever costs about 9 lb of cap," and §7 sized the spar with published
allowables and a taper schedule that has not been drawn yet. **The spar is not
frozen, so the cheap version of this decision is still available.**

There is also a direct conflict with §6, which chose 130 ft² over 150 specifically
because *"you cannot shrink a wing later and the 20 ft² is the difference between a
Part 103 configuration being reachable and not."* Any span growth has to be checked
against that, and it is a genuine reason a winglet might be preferred — winglets
add effective span without adding *area*, so they do not move the Part 103 empty
weight the way 2 ft of wing does. **That is the one argument for winglets on this
aircraft that actually holds**, and it is a Part 103 argument, not an efficiency one.

## 4. The number the whole thing rests on

Every figure above assumes `e = 0.85`. That is a placeholder. Move it and the
winglet disappears into the noise:

| Tip treatment | e | L/D |
|---|---|---|
| square-cut tip, poor | 0.75 | 10.07 |
| *assumed baseline* | 0.85 | 10.72 |
| well-shaped Hoerner tip | 0.90 | 11.03 |

A properly shaped tip is worth **+2.9%** off the assumed baseline, and **+9.5%** if
the tips would otherwise have been square-cut. That is larger than any winglet in
§2, it costs **zero weight and zero structure**, and it falls out of tip-bow work
already on the build list.

**You do not currently know where on that table you are.** The uncertainty on `e`
is roughly ±0.05, and the winglet's entire benefit is equivalent to about +0.04.
Fitting winglets before measuring glide is tuning below the noise floor of the
model — and §7's own philosophy applies: *"spend margin where manufacturing
variability actually lives."*

`flight-test/phase-1-plan.md` already has "Glide ratio, measured by timed descent"
as item 7. That measurement is what turns this from a guess into a decision.

## 5. Weight, and where it sits

| Per side | Total | Where |
|---|---|---|
| 2 lb | 4 lb | wingtip |
| 3 lb | 6 lb | wingtip |
| 4 lb | 8 lb | wingtip |

**Tip mass is the worst mass on the aircraft for flutter.** Wing bending-torsion
flutter speed falls as mass is added at the tip aft of the elastic axis, and a
winglet is both a mass *and* an aerodynamic surface out there. §12 argues the wing
is stall-limited so it *"cannot be aerodynamically overstressed."* That argument is
about load factor and **says nothing about flutter**, which is a stiffness and mass
distribution problem and is not currently analysed anywhere in this project.

On an aircraft with Vne 69 mph, a wood wing, and no flutter analysis, adding
cantilevered tip mass is the change most likely to move a margin nobody has
calculated.

## 6. What else it touches

**The outer panel is removable and carries the spoilerons.** A winglet's side load
and torsion feed through the tip rib into an 11.5 ft cantilevered panel and then
through a joint sized in §13 for *bending* — two bolts per cap, 108% margin. The
winglet adds **torsion** at that joint, which the §13 analysis does not cover.

**§10 requires attached flow over the outer panel** for spoileron authority. A
winglet changes the tip flow field where the spoilerons work. This is a handling
question on a two-axis aircraft, not a drag question, and it argues for measuring
roll authority before and after rather than assuming neutrality.

**The slats are full span.** How a full-span slat terminates into a winglet root is
a real detail problem, and §10 already says slat geometry should be copied
dimension-for-dimension from a known installation rather than derived. There is no
known installation to copy for a slat-to-winglet junction.

**Asymmetric loss is a roll upset.** Losing one winglet in flight puts a roll on an
aircraft whose roll authority is already described in §9 as *"adequate rather than
crisp."* This is the one place the §7 anti-carbon logic partly transfers.

**Handling damage.** Two 20 lb panels carried by hand every flight, now with a
projecting surface at the far end. Ask anyone who has hangar-rashed a winglet.

## 7. On carbon specifically

Carbon is a **better** choice here than §7's spar reasoning would suggest, and the
distinction is worth drawing:

- §7 rejected carbon for the spar because *"a wet-layup void is both unsurvivable
  and undetectable."* A winglet is not a primary structure in that sense — its
  failure is a roll upset, which is serious but survivable, not a wing separation.
- The CTE argument that killed the aluminium-to-birch bond does **not** apply.
  Carbon is near zero µm/m/°C and Douglas fir is about 4, so a carbon-to-wood
  joint is a far better thermal match than the aluminium-to-wood one that was
  rejected. This is the rare place where carbon is the *conservative* material.

The real objection to carbon winglets is not the material. It is that the project
has no composite tooling, no mould, and a wood-and-fabric wing — so a carbon
winglet means a plug, a mould, a layup, and a metal-to-wood-to-composite joint at
the tip, for a 3–4% return that a shaped wooden tip bow may already have collected
for free.

---

## 8. Conclusion

**Not on version one.** In order:

1. **Shape the tips properly.** It is free, it is worth as much or more than a
   winglet, and it is inside work already scheduled.
2. **Measure the glide in Phase I.** Item 7 of the test plan. That gives the real
   `e` and turns this into arithmetic instead of assumption.
3. **If more span efficiency is still wanted, add span.** The wing already comes
   apart, so nothing is stopping it. Check it against §6's Part 103 area argument
   first.
4. **Revisit winglets only if the Part 103 configuration turns out to need
   effective span without added area** — that is the single argument here that
   survives scrutiny — or if a hard span constraint appears later.

If they are built anyway, the things that decide whether they work are **cant, toe
angle, and twist**, none of which are in the estimate above, and a couple of
degrees of toe-out will erase the entire benefit.

## 9. What this does not settle

- The real `e` of the chosen airfoil and planform. Everything here scales off it,
  and it is the same unknown that `open-questions.md` already lists as blocking.
- Flutter. **No flutter analysis exists for this wing at any configuration.** That
  is a gap independent of winglets, and adding tip mass is what makes it urgent.
- Whether span growth is compatible with the Part 103 area and weight targets.
- Winglet cant, toe, and twist, which are the parameters that actually decide the
  outcome and cannot be estimated the way area and span can.
- **The quarter-scale model cannot answer any of this.** At Re 161,000 against
  1,280,000 the tip flow and the junction behaviour do not scale, exactly as
  `model/README.md` already warns for the slats.

---

*Same assumptions as the rest of `analysis/`: 31 ft span, 130 ft², f = 0.519 m²
with slats, e = 0.85, 496 lb gross, Cf = 0.006 on added wetted area.*
