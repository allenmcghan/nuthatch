# Amphibious: What the Aventura Actually Does, and Why This Airframe Can't Follow It

**The question:** the Aventura UL appears to do everything this project wants
— in a tractor configuration — while also being amphibious. What are they
doing differently, and could the Nuthatch ever be converted?

## 1. Correcting the premise: the Aventura is a pusher, and it isn't 103

Two facts from the record change the framing:

- **The Aventura is a pusher.** The whole family (Bob Bailey design, 1995)
  are high-wing flying boats with the engine on a pylon above the hull and a
  **pusher propeller — specifically to keep the prop out of water spray**,
  which is the first structural fact of seaplane design. There is no tractor
  Aventura; a photo of the pylon engine from the wrong angle reads as tractor.
- **The "UL" is not Part 103.** The Aventura UL's empty weight is
  **328–390 lb** — 74 to 136 lb over the 254 cap. It is marketed
  ultralight-style but flies as a registered experimental (or as a fat
  ultralight, which this project's compliance-first rule forbids). It is not
  evidence that a 103 amphibian of this capability exists; it is evidence
  that even a company that wanted one badly couldn't hit the number.

## 2. What they do differently — and why each choice is water-driven

| Aventura choice | Why water forces it |
|---|---|
| Fiberglass planing hull *as* the fuselage | The hull is the float — no separate float weight, and fiberglass doesn't care about immersion |
| Engine on a pylon, pusher prop | Prop sits high and behind the cabin, above the bow spray that eats propellers at hump speed |
| Anodized aluminum tube + polyethylene tip floats | Every material survives dunking; nothing rusts or soaks |
| 40–65+ hp engines | Getting over the displacement drag hump needs roughly twice the thrust margin of a grass takeoff |
| Repositionable gear + retractable tailwheel | The amphibious part — wheels up for water, down for pavement |

The lesson isn't a trick to copy — it's that **every major configuration
decision flows from the water requirement**. Amphibian is not a feature you
add; it's the first requirement, and it picks the hull material, the engine
location, the prop direction, and the weight class before anything else gets
a vote.

## 3. Could the Nuthatch convert? The conflicts, in order of severity

**The prop kills it first.** The Nuthatch's tractor prop is at the nose with
the thrustline at 40 in and the 60-in disc's tips reaching down to **10 in
AGL** — a geometry chosen for grass stance and now protected by the rev D
raked nose gear. On floats, those tips sit perhaps 20 in above the water,
directly above the float bows, exactly where bow spray goes at hump speed.
Cubs survive on floats because their prop tips are ~3 ft up behind spray
rails; ours would be sandblasted (wood prop: destroyed) every takeoff. Fixing
it means raising the thrustline a foot or more or moving the engine to a
pylon — either way it is a different airplane.

**The stall gate leaves no weight for floats — almost.** Part 103 has a gift
here: §103.1 **excludes floats from the 254 lb empty weight**. But the 24 kt
stall gate still applies at gross, and that gate caps gross at 456 lb: 253 lb
aircraft + 170 lb pilot + fuel ≈ 453 lb. **Zero pounds available for the
~50–70 lb a float set weighs.** The one crack in this wall is the flaps trade
([trades/flaps.md](flaps.md)): Path B's CLmax ~1.95 raises the stall-limited
gross to ~494 lb — room for a light float set *on paper*. The prop-spray
problem stands regardless, which is why this stays a footnote and not a path.

**Power.** The hump drag of floats or a hull wants roughly twice the static
thrust margin of a grass roll. The 103 kit's ~22–28 hp paramotor-class engine
is sized to a 0.8 lb weight margin, not a water takeoff. The EAB's F-33 might
crawl over the hump on a calm day; "might" is not a design basis.

**Materials.** A wood-gusset airframe, birch ply, and 4130 steel all fly off
water in vintage practice — with marine sealing schedules and corrosion
programs that consume exactly the build-hour and weight budgets this project
spent elsewhere. Not impossible; expensive in the two currencies the project
has none of.

**Handling.** A rudder-rolls two-axis aircraft on the step in a crosswind,
with spoilerons for roll and no water rudder, is a handling experiment nobody
has run. The Aventura has three axes.

## 4. Verdict

**No amphibious conversion — recorded as rejected in the losers table.** The
Aventura succeeds *because* it was designed around water from the first line;
its configuration (hull fuselage, pylon pusher, waterproof materials, 40+ hp,
328+ lb) is the price of that requirement, and it pays the price by not being
Part 103. The Nuthatch made the opposite choices for the opposite mission —
low tractor prop for grass stance and crush protection, wood for cost and
buildability, 254 lb for legality — and each of those choices is
load-bearing.

If water flying ever becomes a real requirement: that is a second design (or
an Aventura-class kit purchase), not a Nuthatch modification. The honest
crumb this trade leaves behind: if flaps Path B is adopted, the stall-gate
arithmetic would no longer be the binding constraint against floats — the
propeller would be. It always was.

## 5. Follow-up: inflatable floats and a gear-for-floats swap

The refined proposal — high-pressure inflatable floats replacing the entire
wheel gear, plus "a structure that moves the prop out of the spray" — splits
into a half that genuinely works and a half that has no answer.

**The floats half works, and better than expected.** Inflatable floats are
proven ultralight equipment (the Full Lotus line has flown on ultralights for
decades — segmented low-pressure bladders in fabric; modern drop-stitch
"high-pressure" construction is the same idea, stiffer). And the accounting
is friendly: §103.1 excludes floats from empty weight, while the *removed*
wheel gear (~29.5 lb) comes off for real. Ledger: 253.2 − 29.5 gear
+ ~18 lb of float-attach structure (not excluded) = **241.7 lb for 103
purposes — legal with 12.3 lb of margin**, the most empty-weight room any
configuration in this project has ever had. Actual flying mass ≈ 302 lb with
a Full-Lotus-class 60 lb pair.

But the stall gate is merciless: gross ≈ 496 lb with pilot and fuel.
Slats at CLmax 1.8 stall at **24.9 kt — fails**. Flaps Path B at ~1.95
squeaks through at **23.9 kt** — the water version *requires* the
flaps-for-slats swap, and lands right back on a 0.1 kt razor edge.

**The prop half has no structure that fixes it.** The prop is bolted to the
engine; "moving the prop" means moving the engine or raising the whole
aircraft. The geometry that kills both:

- Floats sized for this gross (180% buoyancy → ~14 ft³, an 11 ft pair) put
  the step under the CG and the **bows ~16 in FORWARD of the prop plane**.
  The prop disc literally overhangs the bows — every wave crest and all of
  the bow spray root is inside the disc. A Cub survives on floats because its
  prop sits several feet *aft* of the bows and ~30 in up; ours is the
  forwardmost point of the aircraft.
- Raising the fuselage on a strut tower to get the tips 30 in above the
  waterline needs the thrustline at ~60 in — a **~30 in tower** that adds
  ~15–20 lb (not excluded), puts the CG ~50 in above the water (poor roll
  stability on the step, tip floats mandatory), destroys the low-entry
  stance, and *still* leaves the disc directly over the bows where hump
  spray fans upward.
- Power seals it: **19 lb/hp on the hump** with the 103 engine (seaplane
  practice wants ≤14); the EAB F-33 at ~14.8 is marginal on a calm day.

**Verdict unchanged, now with the accounting done:** the floats insight is
real and recorded — gear-for-floats plus the float exclusion makes the empty
weight *better*, and flaps Path B makes stall barely close. What cannot be
bought back is the nose propeller over the float bows. Getting the prop out
of the spray means getting the engine out of the nose, and the pusher trade
already showed where that balance divergence leads: a different airplane.
If a water sister-ship ever happens, it reuses this project's wing, tail,
and tooling on a new fuselage with a pylon engine — designed around water
from line one, like every amphibian that works.

## 6. What this does not settle

- Nothing structural — no provision is added to the airframe for this.
- The FAA's float-exclusion language (floats vs hull flotation) was not
  chased to a Chief Counsel interpretation, because the verdict doesn't
  turn on it.
