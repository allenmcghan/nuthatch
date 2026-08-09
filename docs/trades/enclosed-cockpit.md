# Rev G: Reclined Pilot, Enclosed Cabin, and the Wing Brought Down Onto It

**The objection:** the wing attachment doesn't look aerodynamic or efficient.
The pilot should sit **reclined**, with a **windshield running from the nose
all the way up to the wing**, and the cabin **fully enclosed with doors on
both sides**. Script: `analysis/enclosed-cockpit.py`.

**The objection is correct, and the fix pays for itself twice.** Rev F left
**15 inches of open air** between the pod top (~46) and the wing underside
(61), with the cabane struts crossing that gap at the aircraft's widest
station. That is the worst possible place to put a hole and some tubes.

The result of closing it is better than expected: **the 103 kit gains 5.5 lb
of margin** — more than the steel boom and the drag cleanup were about to
spend between them.

## 1. Reclining the pilot

| Recline | Head top z | Head station | vs upright |
|---|---|---|---|
| 0° (rev F) | 56.0 | 57 | — |
| 30° | 51.2 | 75.0 | −4.8 in |
| **35° (selected)** | **49.5** | **77.6** | **−6.5 in** |
| 40° | 47.6 | 80.1 | −8.4 in |

**35° drops the head 6.5 in**, which is what lets the roofline come down to
meet the wing.

**The catch is CG**, and it is not small. Reclining swings the trunk, head
and arms aft about the hip — **pilot CG moves aft 5.7 in**, which at a 170 lb
pilot on 456 lb gross is **+2.1 in of aircraft CG, or +4.3% MAC**. That would
push a 30% MAC design to 34%, at the aft limit.

**Fix: move the seat forward ~6 in** (hip station 57 → 51) so pilot CG stays
put and aircraft CG never moves at all. The room exists precisely because
deleting the rudder pedals emptied the footwell — the twist-grip decision
paid for the reclined seat without either decision knowing about the other.

## 2. The wing comes down onto the cabin

Head top 49.5 + **5.5 in of clearance** → wing underside **55**, chord line
**58** (from 64). *(First pass used 4 in of clearance and put the underside at
53; 3 in over a head you can hit is not enough, so the wing went back up 2.)*

The cabane struts are **deleted entirely** — the wing root now sits on and
fairs into the cabin roof, and the main hoop at sta 61.5 picks the front spar
up directly at z = 55. The load path gets shorter, not longer.

**Honest costs:**

- **Roll authority.** The high-wing pendulum arm above CG goes 37 → 31 in,
  **−16%**. On a two-axis aircraft dihedral *is* roll control, so expect to
  put **~0.5–1° of geometric dihedral back**. The aero model must be re-run —
  this is a real gate, not a footnote, and it interacts with the Quicksilver
  precedent already flagged as decisive.
- **Entry gets worse.** Ducking under a wing at 55 in is a step back from the
  26 in step-over the gear trade prized. Doors fix it on the EAB — you open a
  door and sit in. **The open 103 gets a duck-and-sit**, which is a genuine
  regression for Avery's aircraft and should be checked on the mockup.
- **Ventilation becomes mandatory**, not optional. An enclosed cabin with a
  large windshield in a Tennessee summer is a greenhouse. This partly
  undercuts the sling seat's cooling rationale (it still breathes better than
  a solid pan, but it is no longer sitting in the breeze): NACA ducts and an
  openable storm window or door are now required equipment.

## 3. The drag prize — this is why it is worth doing

| | Open, upright | Enclosed, reclined |
|---|---|---|
| Pod frontal area | 3.76 ft² | 3.26 ft² |
| Effective Cd | ~0.40 (bluff opening, head in the breeze) | ~0.15 (faired) |
| **f_pod** | **1.51 ft²** | **0.49 ft²** |

Plus the cabane struts deleted (−0.15 ft²):

**Total −1.17 ft² → f 4.84 → 3.68, L/D max 10.8 → 12.4 (+15%).**

Stacked with the [borrowed-optimizations §2](borrowed-optimizations.md)
cleanup, net of the overlap already counted: **f → 3.08, L/D max 13.6
(+25%)**, and glide from 1,000 ft goes **2.05 → 2.57 miles**.

That is the largest single performance change in the project's history, and
it comes from a shape the owner wanted for looks.

## 4. Weight — and the fleet rule survives intact

| | lb |
|---|---|
| Windshield, nose to wing, Lexan | +5.0 |
| Two doors: frames, glazing, hinges, latches | +8.0 |
| Door sills, posts, cabin closeout in the cage | +3.0 |
| Ventilation: NACA ducts + storm window | +1.0 |
| Cabane struts and fittings **deleted** | −5.5 |
| Existing EAB windshield superseded | −4.0 |
| **Enclosure kit, net (EAB)** | **+7.5** |
| **Airframe change alone (both aircraft)** | **−5.5** |

| | Empty | Verdict |
|---|---|---|
| **103 kit, cabane deleted** | 253.2 → **247.7** | **margin 0.8 → 6.3 lb** |
| 103 kit *with* the enclosure | 260.7 | **over the cap by 6.7 lb** |
| EAB with the enclosure | 277.7 (all-up 507.7 of 525) | **fits** |

**This splits exactly along the existing fleet architecture:**

- **Wing-onto-cabin and cabane deletion are an AIRFRAME change**, so both
  aircraft get them — and the 103 kit's margin goes from a terrifying 0.8 lb
  to **6.3 lb**, which more than covers the all-steel boom (−2.2) and the
  drag cleanup (−1.6) that had just spoken for everything.
- **The enclosure is an EAB KIT ITEM**, exactly like the windshield and
  tablet already are. Door hard points live in the cage as permanent grams;
  the doors and glazing bolt on or stay home.
- **Aircraft #2, the pure 103, flies open under the same wing on the same
  cage.** Two configurations, one airframe — the common-airframe rule is
  unchanged, and this is precisely the "deletable items on permanent hard
  points" pattern it already specifies.

## 5. Shape: does it actually look and fly right?

The upper line now sweeps from the spinner up to the wing underside at the
leading edge — roughly **14–17° from horizontal**, which is sailplane-canopy
rake. Maximum section moved to the shoulders and the belly is held at 16 in,
so the pod is a proper teardrop with the wing growing out of its back rather
than floating above it on sticks.

Two notes:

- **Windshield optics.** At 14–17° a flat-wrapped screen has real reflection
  and distortion issues. Sailplanes manage it with a blown canopy; a
  flat-wrapped Lexan screen at that rake will want checking on the mockup
  before the frame is welded.
- **The aft-body closure problem from [cockpit-cage.md §4](cockpit-cage.md)
  is unchanged** — the cabin still has to neck down to a 3.5 in boom, and
  that closure is still steeper than attached flow likes. Enclosing the front
  does not fix the back.

## 6. What this does not settle

- **The dihedral re-run.** −16% of pendulum arm on the aircraft whose roll
  control is dihedral. Re-run `aero-model.py` for Clβ and the rudder-roll
  ratio before anything is drawn; expect +0.5–1°.
- **Egress.** A fully enclosed cabin with a BRS raises a question the open
  cockpit never had: getting out, in a hurry, possibly inverted. Door
  jettison or a frangible panel needs deciding, and it interacts with the
  rollover hoop that now doubles as the wing pickup.
- Whether 35° is the right recline, or 30° (easier entry, less CG shift) or
  40° (lower head, more drag saved). A mockup question, and it moves the
  seat station.
- Door hinge line (forward, gull, or removable pin), latch, and the sill
  height that decides whether "sit in" actually works.
- Head clearance is now 5.5 in on paper with a 6'0" pilot. Check it on the
  mockup with a helmet and the sling at full sag.
- The measured-weights CSV still carries the cabane line; it retires at the
  workbook reconciliation along with everything else queued there.
