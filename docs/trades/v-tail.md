# V-Tail — and the Tail-Dihedral Question

Two questions arrived together: "weren't we adding dihedral to the tail for
better steering?" and "what about a V-tail?" The first is a mix-up worth
untangling because it points at the second. Both resolve to: **keep the
cruciform tail, keep the dihedral in the wing.**

## 1. Clearing up the tail-dihedral question

No tail dihedral was ever in the plan. The steering mechanism on this two-axis
aircraft is **wing dihedral — 5°, already in the design**: rudder yaws the
nose, the 5° dihedral converts the resulting sideslip into roll (Clβ −0.082),
and the aircraft banks into the turn. That is the "dihedral for steering," and
it lives in the wing because that's where it works:

- The wing has **31 ft of span and 129 ft²**; the H-tail has 10 ft and 30 ft².
  Dihedral effect scales with span and area — tail dihedral of any sane angle
  adds only **~3–5% to the total rolling moment from sideslip**. It is not a
  steering knob; it's a rounding error.
- What tail dihedral *does* cost is pitch authority: effective horizontal-tail
  area falls as cos²Γ, and the trim analysis (gate 3) already needs −19.3° of
  elevator to flare at forward CG. Giving away tail area to buy a 3% roll
  change is the wrong trade in both directions.

If turn response ever needs improvement, the real knobs are: more **wing**
dihedral (costs crosswind capability — 15° of sideslip currently covers a
10 mph direct crosswind, and that margin shrinks as dihedral grows), a larger
rudder (the Vv 0.038 tail is already deliberately rudder-heavy), or faster
spoileron actuation. Tail dihedral is on none of those paths — except taken to
its logical extreme, where it becomes a V-tail. Hence the second question.

## 2. V-tail: the actual trade

**The NACA equal-projected-area rule kills the headline benefit.** NACA TN 1478
(and every V-tail since) found a V-tail needs roughly the **same total area as
the horizontal + vertical surfaces it replaces** for equivalent stability. Here
that is 30 + 15 = 45 ft² at a dihedral of atan(√(Sv/Sh)) = atan(√(15/30)) ≈
**35°**. Same area → same structure, same covering, essentially the **same
weight**. The Bonanza's V-tail was never lighter than the 33's cruciform; Beech
kept it for marketing.

What's genuinely gained:

- **Two tail-boom junctions instead of four.** Real, but this is an
  interference-drag refinement worth single-digit ounces of drag at a 55 kt
  speed cap. On a 62 mph Vne airframe it buys nothing measurable.
- Better prop-blast clearance and a tail less likely to catch tall grass on a
  full-stall touchdown. Minor, and the tail skid already covers the boom.

What it costs on *this specific aircraft*:

- **A ruddervator mixer.** Every stick/pedal input passes through a mechanical
  mixing linkage — more joints, more slop, more failure modes, and a
  single-point mechanism in both axes at once. The build philosophy everywhere
  else (§ fail-safe, bicycle parts bin, student-proof) runs exactly opposite.
- **Control saturation is routine, not a corner case.** The flare needs
  −19.3° of equivalent elevator; a crosswind flare on a rudder-steered
  two-axis aircraft adds large rudder at the same moment. In a V-tail those
  demands land on the *same two surfaces* — one ruddervator runs out of throw
  and the aircraft loses part of both axes precisely at touchdown, the
  highest-workload second of the flight. A cruciform tail cannot cross-couple
  this way.
- **Adverse roll fights the steering.** V-tail rudder deflection produces an
  immediate rolling moment *opposite* the intended turn (the surfaces are
  tilted, so differential lift has a roll component). On a three-axis aircraft
  the ailerons mask it. Here, turns are *made* by rudder-then-dihedral — the
  wrong-way roll arrives instantly, the dihedral's right-way roll arrives
  ~1 s later through the sideslip buildup, and the aircraft (17–23°/s roll
  authority with spoilerons) wags before it banks. That is a direct hit on the
  one flying quality the whole control system is built around.
- Combined loads at the two root fittings and a mixer to fabricate — more
  gate-4 engineering for a net-zero weight change.

## 3. Verdict

**Rejected.** The V-tail's one honest win (two junctions) is irrelevant at
this speed; its costs land squarely on this aircraft's control philosophy —
rudder-driven steering, saturation-free flare, minimum mechanism. The
cruciform tail with 30 ft² horizontal + 15 ft² vertical stands, with the
dihedral staying in the wing at 5° where the steering actually happens.

Added to the losers table in the design log.
