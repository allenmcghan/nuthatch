# End-to-End Design Audit

A full simulation pass over the aircraft as documented: every published
performance number re-derived from the workbook's own model, then the design
log's load, stability, and mission claims stressed against it.

**Headline: the performance numbers all reproduce. The load basis does not.**
Four real findings, one of them structural, plus one genuinely cheap improvement.

| # | Finding | Severity |
|---|---|---|
| 1 | §12's stall-limit argument fails with fixed slats — the wing **can** be aerodynamically overstressed | **structural** |
| 2 | No negative-g load case exists; gusts reach −1.9 at Vc | structural |
| 3 | Full-throttle level flight (~80 mph) exceeds Vne (69) | operational |
| 4 | The Part 103 takeoff claim doesn't survive the deleted redrive | performance |
| 5 | Landing over the mission's own trees is the binding field constraint — a symmetric-spoiler mode fixes it | improvement |

Status: analysis. Nothing changed except a correction note in design-log §12.

---

## A. What reproduces (all PASS)

Re-derived independently from the Performance-sheet model (f = 0.45/0.519 m²,
e = 0.85, ηp 0.75/0.72):

| Claim | Published | Audit | |
|---|---|---|---|
| Stall clean, 496 lb | 32.7 mph | 32.7 | PASS |
| Stall slats, 496 lb | 28.8 mph | 28.8 | PASS |
| 103 stall slats, 450 lb | 23.8 kt | 23.8 | PASS |
| EAB takeoff roll | 140 ft | 140 | PASS |
| EAB climb | 1,010 fpm | ~1,050 | PASS |
| Glide ratio | 10.7 | 10.7 | PASS |
| Range | ~150 mi | ~150 | PASS |
| Tail volumes | — | Vh 0.56, Vv 0.038 | in band, correctly rudder-heavy |
| Loaded CG | 28–31% MAC | 28.3–30.8% | PASS |

The arithmetic and the model are internally consistent. The problems are in what
was never modelled.

## B. Finding 1 — the stall-limit argument is broken by the slats (structural)

§12: *"The most g a wing can generate is (V/Vs)². At Vne 69 and a 32.7 mph
stall, that is 4.65. … The aircraft cannot be aerodynamically overstressed."*

Two problems, one small and one not.

**Small:** (69/32.7)² = **4.45**, not 4.65. The conclusion survived; the
arithmetic didn't.

**Not small:** §10 makes the slats **fixed, full-span**. CLmax 1.8 is therefore
always available — the 32.7 mph clean stall used in §12 never exists in flight.
Recomputed at the slatted CLmax:

| Condition | Vs, slats | n available at Vne | vs 4.7 limit |
|---|---|---|---|
| EAB max gross, 580 lb | 31.1 mph | 4.91 g | exceeds |
| Design point, 496 lb | 28.8 mph | **5.74 g** | **exceeds** |
| 103 gross, 450 lb | 27.4 mph | 6.33 g | exceeds |
| 130 lb pilot, no fuel, 426 lb | 26.7 mph | 6.69 g | exceeds |

In absolute terms: at Vne the wing can generate q·S·CLmax = **2,848 lb** of lift
regardless of weight. Ultimate as sized is 7.0 × 496 = 3,472 lb; pulling to CLmax
at Vne needs 2,848 × 1.5 = **4,272 lb — a 23% shortfall.**

A full-aft-stick pull at Vne — precisely the manoeuvre §12 says is safe — can
exceed limit load at every flight weight, and ultimate is not covered.

**Three fixes, cheapest first:**

1. **Lower Vne to Vs_slats·√4.7 ≈ 62 mph.** Costs nothing structurally; cruise
   is 55–60, so it thins the cruise-to-Vne margin to almost nil. Probably too
   tight to live with alone.
2. **Raise limit load to 5.74 g (ultimate 8.6).** By §12's own pricing of ~4 lb
   per 0.7 g, roughly **+6–10 lb of cap**. This restores the "cannot be
   overstressed" property *honestly* — with the slatted stall speed in the
   formula, which is the aircraft that is actually being built.
3. **Show the elevator cannot command CLmax at high speed.** Possibly true —
   slats push the stall to very high alpha, and the tail may run out of authority
   first — but it converts a structural guarantee into a tail-analysis result
   that doesn't exist yet, on an aircraft whose tail is also the roll control.

Option 2 is the recommendation. The whole point of §12 was that the envelope
protects the structure; 6–10 lb buys that property back for the aircraft as
actually configured.

**Corollary for fittings:** the g available rises as weight falls (6.7 g at
426 lb). Fixed-mass items — engine mount, seat, harness anchors, BRS hard
points — see n × (their own fixed mass), so they should be sized at the
**light-weight** load factor, not the gross-weight one. §12 already says to
spend margin on fittings; this says how much.

## C. Finding 2 — there is no negative-g case anywhere

§12 sets +4.7/+7.0 and stops. FAR 23.341-form gust analysis at the project's own
numbers (a = 4.42/rad, μ from 3.8 psf wing loading):

| Condition | Gust | n |
|---|---|---|
| Vc 60 mph, design weight | ±50 fps | **+3.69 / −1.69** |
| Vc 60 mph, light | ±50 fps | +3.90 / **−1.90** |
| Vne 69 mph | ±25 fps | +2.55 / −0.55 |

Positive gusts stay inside +4.7 — the manoeuvre case governs, good. But
**−1.9 g at Vc is a real load with no corresponding structural case.** A
conventional pairing would be −1.9 limit / −2.85 ultimate.

This matters more than usually because the spar is **asymmetric**: §7's web is
wrapped from one face down and under, riveted at the top, and the cap-to-web
riveting pattern differs top versus bottom. Reversed bending loads the web wrap
and rivet line in the direction it was not shaped for. The V-n diagram already
in open questions should carry the negative branch explicitly, and the spar
detail should be checked in reversed bending before drawings freeze.

## D. Finding 3 — the aircraft out-runs its own Vne

Solving power available = power required at full throttle, slats installed:
**Vmax level ≈ 80 mph, against Vne 69.** The margin is not small — 21 available
hp against 27.7 required at 80.

An aircraft that can exceed Vne in *level* flight at full throttle — never mind
a shallow descent — puts redline discipline entirely on the pilot. Combined with
Finding 1 (a pull at Vne already over-stresses), this is the worst corner of the
envelope: fast, full power, and a gust or a pull.

Mitigations, combinable: pitch the cruise prop so the engine runs out of rpm
near Vne (fixed-pitch props do this naturally — choose the pitch with this in
mind, not just cruise economy); placard and trim accordingly; and if Finding 1
is fixed by raising the load basis (option 2), some of this concern retires with
it because Vne itself can then be reviewed honestly.

## E. Finding 4 — the Part 103 takeoff number doesn't survive the deleted redrive

The 103 strip column deletes the belt redrive (10 lb → 0) and assumes a
direct-drive ~16 hp engine. A direct-drive two-stroke turns 5,000–6,000 rpm, and
tip speed caps the prop:

| Direct drive | Max prop (0.8 M tip) | Static thrust | Ground roll @ 424 lb |
|---|---|---|---|
| 5,800 rpm | ~35 in | ~96 lb | **~340 ft** |
| 5,000 rpm | ~42 in | ~114 lb | **~240 ft** |

The README claims ~160 ft, and the design target is under 200. **A direct-drive
prop cannot deliver either number.** The deleted 10 lb redrive — which lets the
same engine swing the 60 in disc at ~230 lb static — is worth roughly **140 ft
of runway**, on the configuration that flies from a 1,000 ft field.

Either the 103 keeps a (lightened) redrive and finds the ~8 lb somewhere else in
the strip, or the README's 103 takeoff and climb figures need rewriting around a
small direct-drive prop. The open-questions item about "the 103 engine's actual
power rating" is the wrong question — **the prop diameter the drive can turn is
what decides the field performance.**

## F. Finding 5 — the mission's binding constraint is landing over its own trees

The field: 300 × 1,000 ft with trees at one end (§0). Takeoff toward 50 ft trees
is comfortable — 140 ft roll plus ~140 ft climbing at gradient 0.36 clears them
in under 300 ft.

**Landing back over those trees is not comfortable.** At L/D 10.7 power-off with
no glidepath control: 536 ft of air from tree-crossing, plus flare, plus the
84 ft roll — **~720 of the 1,000 ft, before any error.** And a two-axis aircraft
cannot slip: spoilerons are the roll control and there is no cross-control to
slip with. Throttle is the only glidepath tool, and engine-out there is none.

The high glide ratio that is the aircraft's safety headline is, on final over an
obstacle, a liability.

**The fix is already on the aircraft.** The spoilerons exist; they are
single-acting, tension-only, spring-return (§9). Add a **symmetric deployment
mode** — both spoilers up together, on a separate lever or an over-centre detent
past full stick travel. At an effective L/D of ~6 the same landing takes
**~484 ft**, and every failure mode still resolves to spoilers-closed by the
same spring-return architecture that §9 already requires. Gliders have operated
exactly this system for ninety years.

This is the single cheapest meaningful improvement the audit found: no new
surfaces, no new structure, one cable path and one lever, and it converts the
mission's worst case from marginal to routine. It also partially retires
Finding 3 — deployed spoilers are speed brakes in a descent.

## G. Smaller observations

- **Empty-weight sums check out**: EAB 296 lb, 103 strip 250 lb against the
  254 cap. The 4 lb of 103 margin is thin but real.
- **Fuel CG shift is benign**: 29.2% → 30.8% MAC full-to-empty.
- **Spar root web shear is easy** (~7 ksi at ultimate through the double 0.020
  web); buckling and stiffener spacing remain the open item, as already listed.
- **§13's joint bearing arithmetic verifies** (0.105 in² per bolt pair, two
  bolts per cap → ~108% margin as claimed).
- **Vh 0.56 / Vv 0.038** — horizontal mid-band, vertical at the top of the band,
  which is the right place for an aircraft that rolls with its rudder.

## H. What this audit could not check

- Anything aeroelastic — flutter remains unanalysed, as open-questions now says.
- Dihedral/spoileron roll authority and dutch roll: needs the model (or the
  original Sky Pup values). The audit only confirms the tail volumes are sane.
- Slat CLmax = 1.8 is still an assumption; every stall and field number above
  inherits it, and the 103 stall margin is 0.8 kt.
- The elevator-authority question raised in Finding 1(c) — a real tail analysis
  would either retire Finding 1 cheaply or confirm the +6–10 lb.
