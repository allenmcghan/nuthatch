# The Cockpit Cage, an All-Steel Airframe, and Where the Wing Attaches

**The proposal:** a steel tube cage around the pilot; and since the cage is
steel anyway, make the boom and tail steel too, with fabric over everything —
designed to be genuinely aerodynamic and to attach the wing directly to the
cage. Script: `analysis/cage-design.py`. Drawing: `drawings/sheets/ST-001.png`.

**Adopted as rev F**, including the part that reverses a decision made two
revisions ago. Rev E chose a **6061-T6 aluminium** boom on weight. Re-run
fairly, that margin is much smaller than it looked, and steel wins on grounds
rev E never scored.

## 1. The steel boom, re-opened honestly

Required: **38,034 in-lb ultimate** over the 86 in from cage to tail post.

| Tube | S in³ | Fb ksi | M allow | Margin | Weight |
|---|---|---|---|---|---|
| 6061-T6 5.00 × .065 *(rev E)* | 1.227 | 39.0 | 47,867 | +26% | **8.5 lb** |
| **4130 3.50 × .049** | 0.452 | 95.0 | 42,940 | **+13%** | **12.9 lb** |
| 4130 4.00 × .035 | 0.428 | 76.1 | 32,613 | −14% | fails |
| 4130 4.50 × .035 | 0.544 | 67.7 | 36,797 | −3% | fails |
| 4130 5.00 × .035 | 0.673 | 60.9 | 40,981 | +8% | 13.3 lb |
| 4130 4.00 × .049 | 0.593 | 95.0 | 56,382 | +48% | 14.8 lb |

**Raw steel penalty: +4.4 lb** — not the doubling one might expect, and the
reason is worth understanding. **A thin-wall boom is limited by local
buckling, not by material strength.** Steel's stiffness is 2.9× aluminium's
and its density is 2.89× — those very nearly cancel, which is exactly why
both materials appear on real booms. Steel never gets to use its 95 ksi here;
at these wall thicknesses it buckles first. (The one exception, 4130 4.00 ×
.049, *is* material-limited — and pays 14.8 lb for a margin nobody needs.)

### What steel buys back

| Credit | lb |
|---|---|
| Boom-root fitting: a welded cluster instead of a machined, bonded/bolted sleeve into the steel cage | −1.2 |
| Tail-post fittings: welded instead of bolted brackets | −0.8 |
| No dissimilar-metal isolation or galvanic detail | −0.2 |

**Net steel penalty: +2.2 lb.**

Both of those fittings were flagged in the rev E trade as *"copy
dimension-for-dimension from a Kolb installation"* — precisely because an
aluminium-boom-to-steel-cage joint is the fiddly, unfamiliar part of the
design. **All-steel deletes that joint entirely.** The boom root becomes four
welds into the aft cage frame: the same skill, the same jig, the same filler
rod already required for the cage. The gate that said "copy Kolb's fittings"
retires with it.

### The argument nobody had made yet: fatigue

**4130 has a true endurance limit** — roughly 45–50% of Ftu — below which
life is effectively infinite. **6061-T6 has none.** Every load cycle consumes
life, forever, and the S-N curve keeps falling.

This boom carries a two-stroke's vibration spectrum plus tail buffet at the
end of an 86 in cantilever. Kolb has flown aluminium booms for forty years,
so this is not disqualifying — but an aluminium boom is a **fatigue-managed
part** needing a defined inspection interval, and a correctly sized steel one
is not. On an aircraft whose flutter analysis does not yet exist, and whose
owner wants an airframe that lasts, that asymmetry is worth 2.2 lb.

**Decision: 4130 3.50 × .049 boom, welded to the cage.** Same load basis,
+13% margin, one material, one process, no transition joint.

## 2. The cage, and the convergence that should set it

Cage runs **sta 30 to 96**, four longerons, welded 4130.

| Station | Frame | Job |
|---|---|---|
| 30 | Nose bow | Crush structure aft of the rev D gear bay; forward cage closure |
| **61.5** | **Main hoop** | **Rollover + front spar carry-through + at the CG** |
| 80.5 | Rear frame | Rear spar pickup, seat back, harness anchors |
| 96 | Aft frame | Boom pickup, four welds |

**The convergence is the whole design.** Three independent requirements land
within 2.5 inches of each other:

- **CG (30% MAC): sta 63.0**
- **Front spar (25% chord): sta 60.5**
- **Rollover hoop, clearing the pilot's head: sta ~62**

They should therefore be **one frame**, and that single heavy hoop at
sta 61.5 then does three jobs at once:

1. Carries **88% of wing lift** straight into the cage over the shortest
   possible path.
2. Is the rollover structure over the pilot's head.
3. Sits **at the CG**, so wing lift feeds essentially **no pitching couple**
   into the fuselage and the cabane carries no fore-and-aft kick.

That third point is the one that matters structurally: a wing pickup offset
from the CG has to react a moment through the longerons, which is how
fuselages get heavy. Putting the pickup on the CG deletes the moment instead
of carrying it.

The rear frame at sta 80.5 is then genuinely light — it sees only 434 lb
ultimate — so it can double as the seat-back frame and harness anchor without
growing.

## 3. Wing attachment loads

Ultimate wing lift **3,472 lb** (both wings), resultant at 30% chord, front
spar at 25%, rear at 65%:

| Spar | Station | Share | Ultimate | Per-side fitting |
|---|---|---|---|---|
| Front | 60.5 | 88% | 3,038 lb | **1,519 lb** |
| Rear | 80.5 | 12% | 434 lb | 217 lb |

At 1,519 lb ultimate in double shear, a **3/8 in AN bolt** carries roughly
7,950 lb — five times what is needed. **The fitting is bearing-critical, not
bolt-critical**, which is the same conclusion the wing-joint work reached for
the spar splices, and it means the design effort belongs in plate thickness
and edge distance rather than in bolt diameter.

The pickups sit at **z = 64, ±8 in** either side of centreline, joined by a
cross tube — that cross tube *is* the front spar carry-through, and the outer
panels bolt to it through the existing three-piece wing joint.

## 4. Is it actually aerodynamic?

The fabric pod is now shaped, not just wrapped: maximum section at **sta 56**
(the pilot's shoulders — the widest thing in the aircraft), then a smooth
run-out into the boom.

One honest finding. The aft-body closure angle:

| Run | Closure |
|---|---|
| sta 56 → 66 | 5.7° |
| sta 66 → 78 | 14.0° |
| sta 78 → 88 | **21.8°** |
| sta 88 → 96 | **26.6°** |

Attached flow wants **≤ 12–15°**. Closing 12 in of half-height at 12° would
need 56 in of run — taper starting at sta 40, forward of the pilot's
shoulders, which is impossible.

**So some aft-body separation is inherent to a pod-and-boom with a seated
pilot**, and every aircraft in this class lives with it. It is already inside
the f = 0.45 the audit back-solved, so this is not a new penalty — but it
does set what the honest moves are:

- Start the closure **as far forward as the shoulders allow**.
- Keep the run-out a **smooth curve with no kink** — a kink separates far
  worse than a steady taper.
- **Do not chase a fully closed teardrop.** A slightly fuller base with the
  boom exiting cleanly beats a forced steep taper, and it is also easier to
  build in fabric over stringers.

For "looks right" the same shape rules apply, which is convenient: the
proportion that reads correctly on a pod-and-boom — fat forward, long clean
run aft, slender boom — is the one that also flies best. The 3.50 in steel
boom is visually slimmer than rev E's 5.00 in aluminium, which helps.

## 5. Ledger — and it competes with the drag cleanup

| | lb |
|---|---|
| Freed by recent decisions (flaps −1, twist grip −2, sling seat −1.8) | **4.8** |
| Already proposed: drag cleanup (borrowed-optimizations §2) | −1.6 |
| **All-steel boom, net** | **−2.2** |
| Remaining | **1.0** |

**It fits — but only because three decisions this week went the right way,
and it directly competes with the drag cleanup.** Both together spend 3.8 of
the 4.8 lb freed. Nothing further may be added to the 103 kit without finding
new weight, and this should be treated as the margin now being spoken for.

## 6. What this does not settle

- Longeron and diagonal tube sizes. The cage is drawn as an architecture;
  member sizing needs the crash cases (nose bow, rollover) and the gear and
  engine mount reactions worked properly.
- Rollover load basis — no standard was chosen. Glider and racing practice
  differ; pick one and size the hoop to it.
- Whether the hoop should pick up the front spar at ±8 in or wider. Wider
  reacts rolling moment better and fouls the pilot's shoulders sooner; this
  is a seating-mockup question.
- The welded boom-to-cage cluster geometry — copying a Kolb *fitting* is now
  moot, but copying a Kolb *cluster layout* is still the cheapest way to get
  the weld geometry right.
- Fabric attachment to a 3.5 in boom (stringers vs direct) and whether the
  boom is faired at all.
- The measured-weights CSV still carries the rev E boom line; it re-baselines
  at the workbook reconciliation along with the flap, twist-grip and sling
  numbers.
