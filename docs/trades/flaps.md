# Flaps: Yes — and They May Want the Slats' Job

**The question:** can a single flap lever shorten takeoff and landing and cut
stall speed without much added complexity? Script: `analysis/flaps.py`.

**Short answer: yes, and this airframe is unusually well suited to them** —
but the 103 weight margin turns "add flaps" into a sharper question: *add them
to the slatted wing* (busts the 103 kit) *or let them replace the slats* (nets
slightly lighter and multiplies the stall legality margin by ten). The second
path is the interesting one, and it is a real design decision, left open below.

## 1. Why this wing takes flaps more easily than most

- **The whole trailing edge is free.** A two-axis aircraft has no ailerons;
  roll comes from the top-surface spoilerons. A plain hinged flap can run
  ~60% of span inboard with no control-surface real estate fight — most
  designs never get that.
- **The single-lever claim is true.** One piece of torque tube across the
  fuselage, a Johnson bar with three notches (0° / 25° / 40°), four to six
  hinges on a false spar. The one-piece tube makes asymmetric deployment
  impossible by construction — no split-flap failure mode to analyze.
- **The overspeed placard is nearly free.** Vne 62 was chosen so the slatted
  wing's maximum lift equals the spar limit. A higher flapped CLmax needs a
  flap-extension limit: max-lift meets the spar limit at 55–60 mph, so
  **VFE 55 mph IAS** covers every configuration — a 7 mph gap below Vne on an
  aircraft whose 103 kit can't reach 55 level anyway. (Honesty note: fixed
  slats were protected by physics; a VFE placard is pilot procedure. It is the
  one soft spot flaps introduce into the load basis, and it is a gentle one.)

## 2. What flaps buy (numbers scaled off the workbook's 23.9 kt baseline)

| Configuration | CLmax | Stall @ 456 lb | Takeoff | Landing roll |
|---|---|---|---|---|
| Clean 4412 | 1.40 | 27.1 kt | 180 ft | 108 ft |
| Slats (today) | 1.80 | 23.9 kt — **0.1 kt margin** | 140 ft | 84 ft |
| Flaps 40° only (Path B) | ~1.95 | 22.9 kt — **~1.2 kt margin** | ~125 ft | ~72 ft |
| Slats + flaps 40° (Path A) | ~2.35 | 20.9 kt — ~3 kt margin | 110 ft | 65 ft |

And the combination nobody else gets: **flaps (slow) plus the symmetric
spoileron mode (steep) together** — the audit's binding 480 ft
over-the-trees case improves further. Quantify in the gate-3 rerun.

## 3. The catch that is not weight: flare margin

Gate 3 passed the forward-CG ground-effect flare with **5.7° of elevator to
spare** (−19.3° of −25°). Flaps 40° adds a nose-down ΔCm ≈ −0.19, which is
roughly **10° more elevator demand before the flap downwash offset** is
counted. Full flap at forward CG may saturate the elevator exactly at
touchdown. Mitigations, in order:

1. **Land at flaps 25°** — keeps ~70% of the CLmax gain at roughly half the
   pitching moment (and 25° is the takeoff notch anyway).
2. Re-run gate 3 with flap downwash modeled before considering more elevator
   throw or a tail-incidence tweak.

This is a required gate-3 rerun, not a redesign — but it is *the* engineering
gate for flaps, tighter than anything structural.

## 4. Weight forces the real decision

Converting the fixed trailing edge to a flap costs **+4 to 6 lb** (hinges,
torque tube, lever, TE stiffening).

**Path A — add flaps to the slatted wing.** 253.2 + ~5 = **~258 lb: busts the
254 cap.** And the airframe-invariant rule closes the escape hatch: a hinged
trailing edge is not a bolt-on kit item, so "flaps on the EAB only" means two
different wings — the one thing the fleet plan forbids. Path A is dead for
this fleet unless 5 lb appears elsewhere, and the weight scrub already took
the easy 41.

**Path B — flaps replace the slats.** Slats −6 lb, flaps +5 lb: **net ~−1 lb,
103 kit ~252.** Landing-configuration stall 22.9 kt. Three things get better
at once:

- **The scariest legality item largely retires.** Today the 103 stall gate
  hangs on an unverified slatted CLmax 1.8 with 0.1 kt of margin. Path B
  hangs it on a NeuralFoil-verified clean 1.45 plus a textbook plain-flap
  increment, with ~1.2 kt of margin — twelve times the cushion, built from
  better-known aerodynamics.
- The slats' cruise drag is deleted (they were carried as fixed, always-out).
- One less fabrication system: slat brackets and their rigging go away;
  flap hinges and a torque tube arrive. Roughly a wash in build hours.

**Path B's real price is stall character.** The slats were chosen to make the
stall gentle at high alpha — the student-proof, daughter-proof property. A
plain-flap 4412 wing with 2.5° washout and inboard-only flaps keeps the tips
flying and should stall straight ahead, but *should* is not the standard this
project uses for safety properties. **Path B is gated on demonstrated stall
behavior on the quarter-scale model** (which was already tasked with dynamic
roll work): straight-ahead break, no wing drop, flaps up and down. Note the
tail-strike geometry also eases — the flapped wing stalls at lower alpha than
the slatted one, so the 19°-attitude full-stall touchdown case relaxes toward
the 13.4° skid geometry.

## 5. Recommendation and status

**Flaps: yes — as Path B, flaps-for-slats, pending two gates:**

1. Quarter-scale model demonstrates docile stall, flaps up and down.
2. Gate-3 trim rerun with flap moments and downwash; expect to land at 25°
   or adjust tail incidence ~1°.

Until both pass, the slatted wing remains the design of record. This is
recorded as an open decision, not a change — the wing drawings are not yet
frozen (gate 5), so the decision costs nothing to hold open until the model
flies.

## 6. What this does not settle

- Flap increment verification at Re ~1M (NeuralFoil the flapped section the
  same way the clean sections were done).
- Hinge/false-spar detail and the actual conversion weight on a scale.
- Flap-notch speeds and the placard card; VFE 55 confirmation once the real
  CLmax lands.
- Whether the symmetric-spoiler landing mode remains necessary with flaps, or
  becomes the backup (keep both — spoilers are already paid for).
