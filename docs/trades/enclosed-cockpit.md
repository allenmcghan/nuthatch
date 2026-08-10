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

*(Revised in §6 — the glazing is thin film, not Lexan, which changes these
numbers substantially in the right direction.)*

| | lb |
|---|---|
| Clear film, 20 mil, ~22 ft² | +3.0 |
| Two door frames, light tube | +3.0 |
| Bead track and fasteners (positive, no release) | +0.8 |
| Two mounted cutters + brackets | +0.3 |
| NACA ducts, closable valves, defog | +1.0 |
| Cabin closeout and sills in the cage | +2.0 |
| **Enclosure kit, gross** | **+10.0** *(was 17.0 with Lexan)* |
| Existing EAB Lexan windshield superseded | −4.0 |
| **Enclosure kit, net (EAB)** | **+6.0** |
| **Cabane deleted — airframe change, both aircraft** | **−5.5** |

| | Empty | Verdict |
|---|---|---|
| **103 kit, cabane deleted** | 253.2 → **247.7** | **margin 0.8 → 6.3 lb** |
| 103 with the *full* enclosure | 257.7 | over the cap by 3.7 lb |
| **103 with windshield + vents, no doors** | **250.8** | **margin 3.2 lb — this works** |
| EAB with the full enclosure | 270.2 (all-up ~500 of 525) | **fits** |

**This splits exactly along the existing fleet architecture:**

- **Wing-onto-cabin and cabane deletion are an AIRFRAME change**, so both
  aircraft get them — and the 103 kit's margin goes from a terrifying 0.8 lb
  to **6.3 lb**, which more than covers the all-steel boom (−2.2) and the
  drag cleanup (−1.6) that had just spoken for everything.
- **The enclosure is an EAB KIT ITEM**, exactly like the windshield and
  tablet already are. Door hard points live in the cage as permanent grams;
  the doors and glazing bolt on or stay home.
- **Aircraft #2, the pure 103, gets a windshield and vents but no doors** —
  the classic ultralight arrangement, and a real improvement over the "flies
  open" that the Lexan version forced. Two configurations, one airframe: the
  common-airframe rule is unchanged, and this is precisely the "deletable
  items on permanent hard points" pattern it already specifies.

## 5. Shape: does it actually look and fly right?

The upper line now sweeps from the spinner up to the wing underside at the
leading edge — roughly **14–17° from horizontal**, which is sailplane-canopy
rake. Maximum section moved to the shoulders and the belly is held at 16 in,
so the pod is a proper teardrop with the wing growing out of its back rather
than floating above it on sticks.

Two notes:

- **Windshield optics.** At 14–17° any screen has real reflection and
  distortion issues, and §6's thin film is optically worse than Lexan — but
  it also conforms to compound curvature instead of fighting it, which a
  flat-wrapped rigid panel cannot. Check it on the mockup before the frame
  is welded.
- **The aft-body closure problem from [cockpit-cage.md §4](cockpit-cage.md)
  is unchanged** — the cabin still has to neck down to a 3.5 in boom, and
  that closure is still steeper than attached flow likes. Enclosing the front
  does not fix the back.

## 6. Thin-film glazing and ram-air ventilation

**Owner direction: extremely thin clear plastic — isinglass-class film or
thinner — stretched across the steel frame, with NACA ducts forcing air up
through the cabin, closable for winter.** Script:
`analysis/glazing-ventilation.py`. Three findings, one of them a correction.

### It is much lighter, and the saving compounds

| Glazing | Thickness | lb/ft² | ~22 ft² |
|---|---|---|---|
| Clear PVC film | 12 mil | 0.081 | 1.8 lb |
| **Clear PVC film** | **20 mil** | **0.135** | **3.0 lb** |
| Lexan | 0.060 in | 0.374 | 8.2 lb |
| Lexan | 0.093 in | 0.580 | 12.8 lb |

**−5.3 lb against 0.060 Lexan**, and it compounds: film needs only an edge to
pull against, where Lexan needs a frame stiff enough not to crack it. That is
what takes the enclosure kit from 17.0 lb gross to 10.0, and what puts a
windshield on the Part 103 aircraft for the first time.

### The ducts hold the film taut — an accident that works out

A stretched membrane in an airstream drums and flutters unless tensioned. The
ventilation fixes that for free: **ram air pressurises the cabin and tensions
the film from the inside**, the same trick that makes an inflatable rigid. At
55 mph, cabin at half of ram is 0.027 psi; a 20 in panel bulging 1 in runs
**1.34 lb/in of edge tension** against vinyl's 20+ lb/in. The panels go
drum-taut in flight and slack on the ground, which is the right way round.

**Corollary, and it is a design requirement: the outlet must be smaller than
the inlet.** Equal or larger and there is no pressurisation, and the film
flaps. Size the spill vent deliberately.

### Duct sizing — smaller than you would guess

| Inlet area | CFM @ 35 mph | CFM @ 55 mph |
|---|---|---|
| 4 in² | 64 | 101 |
| **8 in²** | **128** | **202** |
| 12 in² | 193 | 303 |

Against ~1,500 BTU/hr (pilot ~500 plus solar through the glazing ~1,000),
holding the cabin within 10 °F of ambient needs **136 CFM**. So **two NACA
ducts of about 2 × 2 in** cover it at cruise with margin.

Two practical notes: **put the ducts in rigid structure, not in the film** —
a NACA submerged inlet depends on a precise 7° ramp and sharp diverging lips
and cannot hold that shape in a membrane. And at 55 mph a plain scoop is
nearly as good; NACA is worth it for cleanliness and looks, not for
measurable drag at this speed.

### Winter: it removes wind chill, it does not make you warm

| Ambient | Open at 55 mph | Enclosed | Gain |
|---|---|---|---|
| 50 °F | 40 °F | 50 °F | 10 °F |
| 40 °F | 25 °F | 40 °F | 15 °F |
| 30 °F | 11 °F | 30 °F | **19 °F** |
| 20 °F | −3 °F | 20 °F | **23 °F** |

That is the honest framing: thin film has essentially no R-value, so what you
get is **still air at ambient** — dress for that. The prize is deleting
55 mph of wind chill, worth about 20 °F, which is the difference between
flying in December and not.

Two winter requirements fall out:

- **You cannot close everything.** A warm pilot inside cold film fogs it
  instantly. Keep a **small defog trickle on the windshield at all times** —
  which is why every closed aircraft has a defrost duct.
- **Specify cold-crack-rated vinyl.** Ordinary clear PVC embrittles and
  cracks around 20–30 °F; marine grades are rated to −20 °F and below. For an
  aircraft meant to fly in winter this is a specification, not a preference.

### Egress: cutters, and the cut path they force

**Owner decision: a seatbelt cutter and a film cutter carried in the cab**,
rather than the edge-release panel this trade first proposed. That is
defensible, and probably better than the alternative:

- **"Push through it" was never going to work.** Plasticised PVC elongates
  **200–400% before it breaks** — a shoulder driven into it *balloons* it like
  a trampoline and can be trapped by it. Thin vinyl is *extensible*, not
  frangible. A blade is the honest way through it.
- **The release-force window was uncomfortably narrow.** A panel must hold
  ~0.027 psi of cabin pressure (about 25 lb spread over a door) plus gusts,
  yet let go under a shoulder. Fasteners that satisfy both **drift toward the
  wrong end as UV ages them**, and a door departing in flight on a two-axis
  aircraft is its own emergency.
- So: **attach the film positively, with no release mechanism to fail or
  drift, and cut out.**

**Timing.** A 38 × 24 in door panel: three sides releases it entirely (86 in,
~5.7 s at a hook blade's ~15 in/s along a track); two sides folds it back
(62 in, ~4.1 s). Plus 2–3 s to reach and deploy — **call it 7–10 seconds.**
Fine for a ditching or a post-crash exit. **Marginal for fire, which is the
case that sets the requirement.**

**The detail that decides the design: a seatbelt cutter has a shielded hook
blade and cannot puncture.** Facing a taut membrane with no edge, it does
nothing. So the airframe has to provide the start:

- **A small pre-slit at the top corner of each panel**, under a tab, sized
  for the hook to enter — or a pull-tab that opens one.
- **Cut along the edge track, not across the middle.** Running the hook down
  the bead groove releases the whole panel in one pass; carving a
  person-sized hole in the middle is slower and needs a pointed blade.
- **Carry both tools**: the hook for webbing and long runs, a small pointed
  blade as the backup that can start a cut anywhere.

**Requirements, so this is a plan and not a hope:**

- **Two cutters, one each side**, so a jammed or blocked side does not matter.
- **Mounted, not stowed** — fixed brackets within reach of a harnessed pilot,
  findable **by feel**, and retained. A dropped cutter in a rolled cabin is
  gone.
- **Reachable in gloves.** This aircraft is meant to fly in winter, and
  gloves are exactly when fumbling for a small tool fails.
- **Proof test, replacing the shove test:** timed egress from a fully
  assembled panel, in a harness, both sides, wearing gloves.

**What it does not cover, honestly:** unconscious or pinned. Nothing in this
weight class does — the BRS covers the in-flight case and the cage covers
impact. Weight is ~0.3 lb for two cutters and brackets, and it *deletes* the
zip and the release-force tuning from the kit.

## 7. What this does not settle

- **The dihedral re-run.** −16% of pendulum arm on the aircraft whose roll
  control is dihedral. Re-run `aero-model.py` for Clβ and the rudder-roll
  ratio before anything is drawn; expect +0.5–1°.
- **Egress — mechanism decided, execution unproven.** §6 settles it: positive
  attachment, cut out with mounted cutters. What remains is physical — the
  pre-slit detail and tab, the bracket positions that are reachable by feel
  and in gloves, and a **timed proof test** from a fully assembled panel,
  both sides. The fire case is the one that sets the standard, and 7–10 s is
  marginal against it.
- **Optical quality of film in the forward view.** Vinyl distorts, and it is
  being asked to work at a 14–17° rake. A small optical-grade panel directly
  ahead (~1 ft², ~0.4 lb) with film everywhere else is the obvious hedge if
  the mockup shows it matters. Film is also a consumable — it yellows and
  hardens in UV over a few seasons, which is fine at $40 a panel.
- Whether 35° is the right recline, or 30° (easier entry, less CG shift) or
  40° (lower head, more drag saved). A mockup question, and it moves the
  seat station.
- Door hinge line (forward, gull, or removable pin), latch, and the sill
  height that decides whether "sit in" actually works.
- Head clearance is now 5.5 in on paper with a 6'0" pilot. Check it on the
  mockup with a helmet and the sling at full sag.
- The measured-weights CSV still carries the cabane line; it retires at the
  workbook reconciliation along with everything else queued there.
