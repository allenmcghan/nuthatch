# The Common Airframe: One Structure, Two Configurations

**Requirement:** the airframe must be identical whether the aircraft flies as
Part 103 or as EAB. Only the powerplant and small additions change. This
document defines that invariant and proves it closes on loads, weight, and
balance. Script: `analysis/common-airframe.py` (extends the weight scrub).

**Verdict: it works, with one real cost.** The common airframe is **212 lb**,
both configurations balance inside 25–35% MAC with the **same wing position**,
and both live on the **same load basis with zero added spar weight** — provided
**both accept Vne 62 mph**. That is the price of commonality, and it is the only
price.

---

## 1. The invariant: 212 lb of airframe

Everything except the power package, windshield, and tablet — per the
[weight-scrub](weight-scrub-103.md) configuration, full safety package intact:

wing (78 lb incl. slats and Oratex) + fuselage structure (55) + tail (18.5) +
gear with brakes (29.5) + controls incl. symmetric-spoiler lever (15.5) + fuel
system, logger, wiring, BRS points, hardware (15.5) = **212.2 lb**.

This structure never changes. Every attach point for configuration items —
windshield sockets, tablet mount boss, aux provisions — is a **permanent
airframe feature** weighing grams; the contents bolt in or stay home.

## 2. The two delta kits

| | Part 103 kit | EAB kit |
|---|---|---|
| Engine | Thor-DS-class, ~31 lb w/ integral redrive* | Hirth F-33 35 lb + belt 10 lb |
| Prop | 53 in, compliance pitch | 60 in, cruise pitch |
| Mount adapter | 4.5 lb, to the **common cluster** | 4.5 lb, to the same cluster |
| Windshield | — | 4 lb |
| Junco tablet | — | 3 lb |
| **Empty weight** | **253.2 lb** | **275.7 lb** |

*catalogue weight — verify on a scale before committing the mount adapter design.

Swapping kits is an engine change and a fabric-free afternoon, not a rebuild.
Going 103 → EAB is an ordinary EAB certification of an existing airframe; going
back means removing the additions and re-establishing 103 compliance (weigh it).

## 3. Balance: both kits fly on the same wing position

Datum = prop plane, wing LE 48, target band 25–35% MAC:

| Config | Empty | Empty CG | Loaded CG range (130–220 lb pilot, 0–5 gal) |
|---|---|---|---|
| Part 103 | 253.2 | sta 69.5 | **30.6 – 33.7% MAC** — in band |
| EAB | 275.7 | sta 65.5 | **26.9 – 29.3% MAC** — in band |

The heavier nose engine plus windshield/tablet pulls the EAB about 4% MAC
forward of the 103 config — both stay inside the band, so **the wing never
moves and the cabane never changes**. Two notes:

- The 103 config at a light pilot with no fuel sits at 33.7% — near the aft
  edge. Gate-3 static margin (~20–25% at 30% CG) says ~16–21% remains there:
  stable, but make 35% the hard aft placard and re-check after first weighing.
- The EAB config is the *forward*-critical one for flare; gate-3 already passed
  flare at 25% MAC in ground effect, which bounds it.

## 4. Loads: one placard makes one spar serve every weight

The documented spar is an **absolute-strength** structure: 2,331 lb limit /
3,472 lb ultimate. Maximum attainable lift depends only on dynamic pressure —
q(V)·S·CLmax — not on weight. Solving q·S·1.8·1.5 ≤ 3,472:

> **Vne = 62 mph, on both configurations, forever.** At 62 mph the wing can
> generate at most 2,299 lb — under the 2,331 lb limit — so the airframe is
> stall-protected at *every* gross weight with **zero added spar weight**.

Load factor available then falls out per configuration automatically:

| Condition | Gross | n available at Vne 62 |
|---|---|---|
| 103, light | 413 | 5.6 g |
| 103, max declared (456) | 456 | 5.1 g |
| EAB, 170 lb pilot | 476 | 4.9 g |
| EAB, 220 lb pilot | 526 | 4.4 g |

All comfortably above the 3.8 g normal-category reference. This **resolves
audit Finding 1 by option 1** for the common airframe, and the compliance prop
already resolves Finding 3 on the 103 kit.

**The cost, stated plainly:** the EAB kit also lives with Vne 62, so its cruise
placard is ~0.9 · Vne ≈ **56 mph**, and the F-33's speed surplus becomes climb
and short-field margin instead of cruise. The alternative — EAB at Vne 69 —
needs the 5.7 g spar (+6–10 lb) **on the common structure**, which pushes the
103 kit to ~260 lb and fails both compliance gates. **A common airframe and a
69 mph EAB redline are mutually exclusive. Choose commonality.** (If a fast EAB
ever matters, that is a second spar layup off the same drawings — explicitly a
different airframe, priced at +6–10 lb.)

The EAB prop should be pitched so the engine rev-limits near 62, exactly as the
103 prop is pitched for 55 kt — same method, different number.

## 5. Design-for-both rules (write these on the drawings)

1. **Engine mount cluster**: one welded fitting geometry, sized for the
   *heavier* engine (45 lb F-33+belt) at the *light-weight* load factor
   (5.6 g × 1.5). Each engine gets its own bolt-on mount adapter.
2. **Nose and gear geometry clear the 60 in disc** (EAB prop). The 53 in
   compliance prop then clears trivially.
3. **Gear and its fittings sized at the EAB max gross** (~526 lb at the
   structural n for landing cases), since gear loads scale with weight.
4. **Negative case** (−1.9 g limit / −2.85 ultimate, audit Finding 2) applies
   to the common spar once — it is weight-independent in the same absolute
   sense.
5. **All deletable items attach to permanent hard points**: windshield sockets,
   tablet boss, BRS bridle channel. Nothing is drilled later.
6. **Fuel stays 5 gal in both kits** (the tank is airframe). An EAB aux tank,
   if ever wanted, is a kit item on a pre-provisioned mount at the CG.
7. **Placards are per-kit**: 103 kit — max weight 456 lb, Vne 62, level max
   55 kt by prop pitch; EAB kit — Vne 62, Vc 56, gross per W&B.

## 6. Compliance summary for the 103 kit on this airframe

| Gate | Requirement | This aircraft | Margin |
|---|---|---|---|
| 103.1(e)(1) | < 254 lb empty | 253.2 lb | **0.8 lb** |
| 103.1(g) | stall ≤ 24 kt at max wt | 23.9 kt at 456 lb | **0.1 kt** |
| 103.1(f) | ≤ 55 kt max level | prop-pitch limited | by design |
| 103.1(d) | ≤ 5 gal fuel | 5 gal tank | exact |

Both live margins rest on estimates (empty weight) and one assumption (slatted
CLmax 1.8). **Weigh every part before installation, and nail the slat geometry
early** — those are the two compliance instruments. The BRS chute, when
installed, is excluded from the 254 count under 103.1(e)(1).

## 7. The light-pilot case: a 105 lb pilot on the 103 kit

The fleet decision is now: **fast EAB abandoned, Vne 62 fleet-wide; the EAB is
the heavy-pilot/add-on aircraft, and the 103 kit must fly a 105 lb pilot.**
That pilot is lighter than any case above, and it finds two things:

**Found: an aft-CG bust.** At 105 lb and low fuel the CG walks aft as fuel
burns — 33.8% MAC at full fuel, **36.3% at empty tank, aft of the 35% limit.**

**The fix is the parachute.** Mount the BRS canister **forward, at ~station
40** (bridle channel to the carry-through unchanged). Its 19 lb — excluded from
the 254 lb count under 103.1(e)(1) but very much real for balance — pulls the
whole fuel range back into band:

| 103 kit + forward chute | Gross | CG | Stall |
|---|---|---|---|
| 105 lb pilot, full fuel | 407 | 31.4% | 22.7 kt |
| 105 lb pilot, empty tank | 377 | **33.6%** | 21.8 kt |
| 154 lb pilot, full fuel | **456 (max)** | 30.2% | **24.0 kt** |

One installation solves the light-pilot balance problem *and* puts a ballistic
chute over the lightest, least-experienced pilot in the family. If the chute is
ever not fitted, the fallback is **5–8 lb of nose ballast at ~station 20,
placarded for pilots under ~125 lb.** Either way, the airframe provisions both:
the forward canister tray and a ballast boss are permanent hard points.

**Pilot-weight placards on the 103 kit** (declared max weight 456 lb for the
24 kt gate): pilot + fuel ≤ 184 lb with the chute — a 105 lb pilot with full
fuel carries **49 lb of margin**; a 154 lb pilot is the ceiling. Heavier pilots
fly the EAB kit, which has no stall gate. The family division of duties falls
straight out of the regulation.

**Rule 1 updated:** the lightest flight case is now ~360–380 lb, where the wing
can pull **6.1–6.4 g** at Vne 62. Size all fixed-mass fittings (engine mount,
seat, harness anchors, chute tray) at **6.4 g limit / 9.6 g ultimate** — up
from the 5.6 g of the 130 lb case.

**Cockpit note for the open questions:** the seat and pedals must now fit a
105–220 lb, presumably different-stature pilot set. Adjustable pedals (three
positions) cost ounces and belong in the drawings from the start.

## 8. The fleet plan: two airframes, both built 103-compliant

Decided: **two aircraft, both built to the identical 103-compliant airframe
spec.** Aircraft #1 is the owner's — it registers EAB and becomes the
experiment platform (autopilot, Junco, larger engine, hybrid propulsion).
Aircraft #2 is the 105 lb pilot's — it stays pure Part 103. Design pilot cap:
**200 lb** (structural and W&B design case; placards may read lower).

**Why #1 is EAB regardless of add-ons — stated honestly:** the stall gate caps
the 103 kit at pilot + fuel ≤ 184 lb (with chute). A 200 lb pilot is not legal
on the 103 configuration at any fuel load; a 170 lb pilot gets 14 lb of fuel.
The owner's aircraft must be EAB *because of the owner's weight*, before a
single add-on goes aboard. The add-ons (autopilot + Junco, ~4–7 lb; larger
engine) then cost nothing extra regulatorily. Register #1 EAB from the start —
flying it "as 103" over 456 lb would satisfy neither rule set.

**What building both airframes 103-compliant buys:** aircraft #2 needs no
N-number, no DAR, no inspection — the save-time-on-compliance goal lands on the
second aircraft and on every future copy. It also defines the published
design's audience: anyone can build the 103 aircraft; the EAB kit is the
documented growth path on the same structure. The
[second-build economics](second-build.md) now apply for real: ~370–460 hours
for airframe #2, order **two nested laser-cut 4130 sets on the first order**,
and Oratex (chosen in the scrub) is doubly justified at 27% of build #2.

**The chute tray is a two-position fitting, and the position is per-aircraft:**

| | Chute at sta 40 | Chute at sta 55 |
|---|---|---|
| 103 kit, 105 lb pilot, empty tank | **33.6% ✓** | 35.1% — out |
| EAB kit, 200 lb pilot, full fuel | 25.7% — thin | **26.7% ✓** |

Forward slot for the light-pilot aircraft, aft slot for the heavy-pilot one.
Both positions are permanent hard points on the common airframe; the tray bolts
to either. Fleet max gross for gear and fitting sizing: **525 lb** (unchanged
in practice from the 220 lb case).

**Hybrid and electric provisions, built into every airframe now:**

- The **CG-bay tray** (carry-through bay, sta ~62–70) rated for **110 lb** —
  the battery-pack station from the [pusher trade](pusher-vs-tractor.md), where
  mass is a trim tool. A hybrid genset or pack lives here, not at the nose.
- A **conduit channel** nose-to-CG-bay for HV cable or fuel line, closed out
  with a cover strip until used.
- The **engine mount cluster limit is 45 lb** at the nose (F-33 + belt is the
  ceiling; already sized at 6.4 g light-weight). Any heavier engine or a
  nose-mounted genset is a re-analysis, not a bolt-on. The series-hybrid
  efficiency numbers in the design-log losers table still stand — the platform
  supports the *experiment*; it does not promise the experiment wins.

## 9. What this does not settle

- Real engine weights on a scale — the mount adapter and the whole 103 margin
  hang on the ~31 lb figure.
- Slatted CLmax, now a legality item (see weight-scrub §5).
- ~~Whether a 56 mph cruise placard on the EAB is acceptable~~ **Decided:
  fast EAB abandoned. Vne 62 fleet-wide is final.**
- Landing-gear load cases at 525 lb — not yet analysed anywhere.
- Actual chute canister mass and dimensions for the two-position tray design.
- The workbook reconciliation from the weight scrub still applies.
