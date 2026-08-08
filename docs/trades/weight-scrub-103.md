# Weight Scrub: One Build, As Close to Part 103 As Possible

**Goal restated:** build a single aircraft whose first configuration is as close
to FAR 103 compliance as possible, accepting a deliberately flat-pitched
("poor") propeller to hold the 55 kt level-speed limit.

Script: `analysis/weight-scrub.py`. Three results, in order of importance:

1. **The repo's two weight statements disagree, and the honest numbers are
   worse than published.** The workbook omits the slats and the cabane.
2. **A line-by-line scrub with the Hirth F-33 lands at ~269 lb — 15 lb over —
   and the stall limit independently forbids being over.** The two Part 103
   gates converge on the same number; there is no heavy-but-legal loophole.
3. **The engine is the decision.** Swap the F-33 + belt (45 lb) for a ~31 lb
   dual-spark paramotor-class engine with integral redrive and the scrub lands
   at **~253 lb and 23.9 kt stall — compliant on both gates, with almost zero
   margin on either.**

---

## 1. Reconciliation first: the workbook is missing 12 lb of airplane

`build-log/measured-weights.csv` and the Weight sheet of
`analysis/weight-cost-hours.xlsx` do not agree:

| | CSV | Workbook |
|---|---|---|
| EAB empty | **309.5 lb** | 296.0 lb |
| Items only in the CSV | **slats 6 lb, cabane 6 lb** | — |

The workbook — the document the README's 296 lb and the "103 strip = 250 lb, 4 lb
under" claims come from — **has no line for the slats and no line for the
carry-through**. Both are real parts (§10 makes the slats mandatory; the cabane
is in the CSV at 6 lb). Small offsets elsewhere (longerons, seat, harness, brakes,
AN hardware) account for the remaining 1.5 lb.

**Honest baseline: EAB empty ≈ 308 lb, and the 103 strip ≈ 262 lb — 8 lb OVER
the 254 limit, not 4 under.** Every derived number in the README's spec table
inherits this. Reconcile the workbook (add the two missing rows) before anything
else is computed from it.

## 2. Why "a bit heavy but call it 103" cannot work: the gates converge

Two of the four Part 103 gates bind weight, and they bind at the same place:

- **103.1(e)(1):** empty weight < 254 lb (excluding floats and *safety devices
  intended for deployment in a potentially catastrophic situation* — a ballistic
  chute does not count against the limit; its hard points do).
- **103.1(g):** power-off stall ≤ 24 kt CAS at max weight. At CLmax 1.8 on
  130 ft², 24 kt is exactly **456 lb gross**. With a 170 lb pilot and 5 gal
  (30 lb), that caps empty at **~256 lb**.

So the stall gate independently enforces the weight gate. An overweight
"103-style" aircraft is doubly non-compliant, and every pound of empty weight
above ~256 comes directly out of the allowable pilot.

The other two gates are cheap here: 5 gal is already the tank size, and the
55 kt max level speed is exactly what the flat-pitched compliance prop delivers
(and it retires audit Finding 3, since the aircraft can no longer out-run its
Vne). Set **Vne 62 mph** on this configuration — audit Finding 1's option 1 —
and the load basis closes with **zero added spar weight**: at Vne 62 the maximum
lift the wing can generate (q·S·CLmax ≈ 2,300 lb) sits inside the 4.7 g × 496 lb
absolute design load. The compliance prop and the compliance placard solve two
structural/operational findings for free. That is the deep synergy in this
configuration.

## 3. The line-by-line scrub (F-33 retained)

Full table in `analysis/weight-scrub.py`. Principles: **nothing from the safety
package is cut** (nose bow, hoop, 5-point, seat, brakes, spoiler fail-safe, BRS
points all stay); slats stay because they *are* the stall compliance; the joint
stays because it is bearing-governed. What moves:

| Change | Δ lb | Basis |
|---|---|---|
| Covering Stewart → **Oratex**, all surfaces | **−8.3** | §14's own table; also −75 build hours and no paint |
| No paint (in AN/finish line) | −3.0 | Oratex is finished off the roll |
| Windshield deleted | −4.0 | as the 103 strip already assumed |
| Main wheels/tires 5.00-5 → light 13 in | −5.0 | grass field at ~455 gross; keep the discs |
| Nose gear simplified | −3.0 | as the 103 strip |
| Fuel system: rotomolded 5 gal + minimal lines | −3.0 | 5 gal is the legal max anyway |
| Junco → bare ESP32 logger, no tablet | −3.0 | compliance aircraft still logs |
| D-tube 1/32 ply outboard of the joint | −1.5 | shear falls with span; keep 1/16 inboard |
| Turtledeck → 3 stringers + fabric | −1.5 | no formers aft of the hoop |
| Wiring, one battery one bus | −1.5 | |
| Steel: laser gusset pkg + wall-by-member | −2.0 | honest, not heroic |
| Misc (TE, tail gauge, mounts, bellcranks, prop) | −5.0 | several half-pounds |
| Symmetric-spoiler landing lever | **+0.5** | audit Finding 5; cheap and it earns its place |
| **Total scrub** | **−40.8** | |

**Result: 268.7 lb empty with the F-33 + belt redrive. 15 lb over, and stall at
469 lb gross is 24.3 kt — over on both gates.** The airframe is now lean; what
is left is not airframe.

## 4. The engine is the decision

Of the 269 lb, **52 lb is the power package** (F-33 35 + belt 10 + mount 4.5 +
prop 7... minus the fuel system). §15 chose the F-33 for dual CDI and 1,000-hour
TBO, and rejected paramotor engines on TBO. But the numbers now look like this
(*all engine weights are catalogue figures — verify on a scale before deciding*):

| Engine | Empty | Gross (170 + 5 gal) | Stall | Gates |
|---|---|---|---|---|
| Hirth F-33 + belt, 60 in prop | 268.7 | 469 | 24.3 kt | **fails both** |
| **Polini Thor 250 DS class** (~31 lb w/ integral redrive, dual spark, ~53 in prop) | **253.2** | 453 | **23.9 kt** | **passes both** |
| Vittorazi Moster 185 class (~29 lb, ~51 in prop) | 250.7 | 451 | 23.9 kt | passes; single-plug versions lose §15's ignition case |

Field performance does not suffer — a Thor-class 36 hp on a 53 in disc makes
roughly 230 lb static, for a **~100 ft ground roll** and four-digit climb at
453 lb, flat-pitched to hold 55 kt.

**And §15's TBO objection is mission-dependent in a way it wasn't before.** At
the ~40 hr/yr this mission implies, a 300-hour TBO is seven-plus years of
flying. The objection was written for an aircraft meant to cruise for hours; the
compliance aircraft is not that. The dual-spark requirement survives — which is
why the Thor DS class is the candidate and single-plug engines are not.

**Recommended decision:** build the airframe per this scrub — it is engine-
agnostic — and hang the dual-spark paramotor-class engine on it for the Part 103
configuration. The F-33 + belt remains the documented EAB upgrade path on the
same mount geometry if TBO or thrust ever disappoint: same aircraft, +16 lb,
re-registered EAB. That is the two-configurations-one-drawings promise of the
README, pointed in the direction that saves compliance time first.

## 5. The margins, stated plainly

- **Weight margin: ~1 lb** on a 253 lb estimate built from estimates. The
  build-log's measure-every-part discipline is not optional bookkeeping on this
  aircraft — it is the compliance instrument. Weigh parts *before* installing.
- **Stall margin: ~0.1 kt**, and it rests entirely on **CLmax 1.8 with slats**,
  which is still an assumption (§10 copies slat geometry precisely because
  millimetres decide it). If real CLmax is 1.7, the 24 kt gross is 430 lb and
  the equation breaks. This is now the single highest-value number to nail —
  before it was performance, now it is legality.
- **The chute exclusion is real leverage**: an installed BRS (~18–20 lb) does
  not count toward 254, so the compliance aircraft can carry the full safety
  package *plus* a chute at no regulatory weight cost. Its hard points (3 lb)
  are already in the table.
- Heavier pilots trade against fuel on this aircraft: at 253 lb empty the
  456 lb stall-gate gross leaves 203 lb for pilot + fuel.

## 6. What this does not settle

- The workbook reconciliation (add slats + cabane rows) — do it before quoting
  any more numbers from it.
- Actual scale weights for the candidate engines, with exhaust and ignition.
- Real slat CLmax — now a compliance item, not a performance item.
- Whether AC 103-7's speed-compliance method is satisfied by the chosen prop
  pitch; document the pitch and rpm limits for the inspector conversation.
- The −2 lb steel line assumes the laser-cut gusset package actually lands;
  measured weights will say.
