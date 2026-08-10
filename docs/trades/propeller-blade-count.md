# Trade: Propeller Blade Count

**Question asked:** what happens at three, four, or five blades?

**Answer:** blade count is not a free-standing decision. It is downstream of the
diameter and the tip speed, and once those are fixed there is usually only one
right answer. §16 gets the right answer for the design point it states — and then
recommends a tip-speed reduction in the next paragraph that invalidates it.

**The finding: §16 contradicts itself.** Two blades is correct at 60 in and
1900 rpm. But §16 also recommends dropping to 1600 rpm for about 8 dB, and at
1600 rpm a two-blade prop has run out of solidity. **You cannot have both the
two-blade prop and the full noise reduction.** Pick one, or split the difference.

Status: analysis only. Nothing in the design has been changed.

---

## 1. Why lowering rpm forces blade area

A propeller absorbs power as `P = Cp · ρ · n³ · D⁵`. Hold the power and the
diameter, and the power coefficient the blades must generate goes as `1/n³`:

| 60 in prop | Tip speed | Mach | Cp | J |
|---|---|---|---|---|
| 1900 rpm | 497 ft/s | 0.45 | 0.0653 | 0.463 |
| 1800 rpm | 471 ft/s | 0.42 | 0.0768 | 0.489 |
| 1700 rpm | 445 ft/s | 0.40 | 0.0912 | 0.518 |
| **1600 rpm** | **419 ft/s** | **0.38** | **0.1093** | **0.550** |

Going 1900 → 1600 rpm means the same blades must produce **1.67× the power
coefficient**. That comes from pitch, from chord, or from more blades. Pitch runs
into blade stall; chord runs into aspect ratio. Blade count is the third lever.

## 2. Does a two-blade prop still fit?

Using `Cp/σ` as a blade-loading proxy, where `σ = B·c/(πR)`. Reference point is
two blades, 4.0 in mean chord, 60 in, 1900 rpm — a known-good ultralight prop —
which gives **Cp/σ = 0.77**.

**At 1900 rpm (the current design point):**

| Blades | σ | Cp/σ | Verdict |
|---|---|---|---|
| **2** | 0.085 | **0.77** | **in band** |
| 3 | 0.127 | 0.51 | under-loaded, carrying dead blade area |
| 4 | 0.170 | 0.38 | under-loaded |
| 5 | 0.212 | 0.31 | under-loaded |

**At 1600 rpm (what §16's noise paragraph asks for):**

| Blades | σ | Cp/σ | Verdict |
|---|---|---|---|
| 2 | 0.085 | **1.29** | **over-loaded — cannot carry it** |
| **3** | 0.127 | **0.86** | **in band** |
| 4 | 0.170 | 0.64 | under-loaded |
| 5 | 0.212 | 0.52 | under-loaded |

The chord a two-blade prop would need to stay at reference loading:

| | 2 blades | 3 blades | 4 blades | 5 blades |
|---|---|---|---|---|
| at 1900 rpm | **4.0 in** | 2.7 in | 2.0 in | 1.6 in |
| at 1600 rpm | **6.7 in** | 4.5 in | 3.3 in | 2.7 in |

A 6.7 in chord on a 30 in blade is an aspect ratio of 4.5 — a paddle, with the
induced losses that implies. This is the real constraint, and it is geometric
rather than subtle.

## 3. Where two blades actually runs out

The useful number is not "1600 rpm needs 3 blades." It is **where the two-blade
prop stops working**, because everything above that line is free noise reduction
with no configuration change:

| rpm | Cp/σ | Chord needed | Blade AR | Noise vs 1900 |
|---|---|---|---|---|
| 1900 | 0.77 | 4.0 in | 7.5 | — |
| 1850 | 0.83 | 4.3 in | 6.9 | −1.2 dB |
| **1800** | **0.90** | **4.7 in** | **6.4** | **−2.3 dB** |
| **1750** | **0.98** | **5.1 in** | **5.9** | **−3.6 dB** |
| 1700 | 1.07 | 5.6 in | 5.4 | −4.8 dB |
| 1650 | 1.17 | 6.1 in | 4.9 | −6.1 dB |
| 1600 | 1.29 | 6.7 in | 4.5 | −7.5 dB |

**A two-blade prop is comfortable to about 1750 rpm and marginal by 1700.** So
roughly **half of §16's noise claim — 3 to 4 dB of the 8 — is available without
touching the blade count.** That is the cheapest result in this document.

Below 1700 rpm you need the third blade. Three blades then has its own floor at
about 1450–1500 rpm, where the same aspect-ratio wall reappears.

## 4. What four and five blades cost

Held to reference blade loading at 1600 rpm, so chord shrinks as blades are
added, the profile-drag penalty at cruise is:

| Blades | Chord | Profile power | % of shaft power | vs 2 blades |
|---|---|---|---|---|
| 2 | 6.7 in | 992 W | 14.0% | — |
| **3** | 4.5 in | 1075 W | 15.2% | **+1.2%** |
| 4 | 3.3 in | 1139 W | 16.1% | +2.1% |
| 5 | 2.7 in | 1191 W | 16.8% | +2.8% |

Two effects are fighting here. More blades at constant total area is roughly
neutral on profile drag and slightly *better* on tip losses. But narrower blades
run at lower Reynolds number, and `Cd0` climbs — on a prop this small, chord is
already only a few inches, so the Re penalty dominates and more blades lose.

**Four and five blades are strictly worse on this aircraft.** At 1600 rpm they
are under-loaded — carrying blade area the engine cannot use — and paying 2–3%
in profile drag plus hub weight and cost for it. They only start winning when
diameter is constrained, which brings us to the next section.

This bounds §16's stated "3 costs 1–3%, 4 costs 3–5%" as about right, and the
mechanism is now explicit rather than asserted.

## 5. Shrinking the disc to justify more blades

The tempting move is to trade diameter for blade count and bank the lower
thrustline that §16 wants. It does not pay:

| Diameter | Ideal η | Static thrust | Ground roll | Thrustline |
|---|---|---|---|---|
| 66 in | 0.925 | 247 lb | 129 ft | ~43 in |
| **60 in** | **0.911** | **232 lb** | **140 ft** | **~40 in** |
| 54 in | 0.895 | 216 lb | 154 ft | ~37 in |
| 48 in | 0.873 | 200 lb | 172 ft | ~34 in |

Dropping to 48 in buys 6 in of thrustline and costs **32 ft of takeoff roll** —
against a 200 ft target with 140 ft currently in hand. That spends most of the
margin to fix a trim problem §16 already priced at 30 lb of tail load. Disc area
is the most valuable thing on this aircraft and should not be traded for blade
count.

**60 in stays.**

## 6. The arguments that are not aerodynamic

**Buildability, and this is the strong one.** A two-blade wood prop is a single
carved piece — laminate a blank, carve it, balance it, done. Three or more blades
requires a bolted hub with individually rooted blades: a machined component with
clamping loads, blade-retention geometry, and tracking adjustment. That is a part
you buy, not a part you carve. It directly contradicts §16's plan to *"buy a
cheap ground adjustable for Phase I, then carve wood once the pitch is known."*
**Going to three blades quietly deletes the carved-wood endgame.**

**Vibration favours three.** A two-blade propeller is not axisymmetric in its
inertia, and it produces a once-per-revolution-squared (2P) excitation in pitch
and yaw that three or more blades do not. On an engine with a belt redrive and a
welded tube mount, that is a fatigue input worth something. It is the one
genuine engineering argument for three blades independent of solidity.

**Redrive ratio bounds it from the other side.** The Hirth F-33 makes its power
in the 6000+ rpm range. At 1900 prop rpm that is roughly 3.2:1; at 1600 rpm it is
closer to 3.9:1. Belt drives get large and lossy as ratio climbs, so the redrive
is a real constraint on how far the tip speed can be cut regardless of blade
count. Whatever rpm is chosen has to be checked against an actual available
redrive ratio before it means anything.

**Blade passage frequency is a red herring.** 2 blades at 1900 rpm is 63 Hz;
3 at 1600 is 80 Hz; 5 at 1600 is 133 Hz. All far below the 1–4 kHz band where
hearing is most sensitive. The perceived benefit comes from the tip speed
reduction and its harmonics, not from moving the fundamental. Blade count does
not buy noise directly — **the rpm does, and blade count is only what permits the
rpm.**

---

## 7. Conclusions

1. **Two blades is correct at 60 in and 1900 rpm.** §16's headline call stands.
2. **§16's own noise recommendation breaks it.** At 1600 rpm a two-blade prop
   needs a 6.7 in chord — aspect ratio 4.5 — and is over-loaded at Cp/σ = 1.29.
   The two paragraphs cannot both be satisfied.
3. **Take the free part: 1750–1800 rpm, still two blades, 3–4 dB.** About half
   the claimed noise benefit with no change to blade count, hub, or the carved
   wood plan. This is the recommendation.
4. **Go to three blades only if the full 8 dB is genuinely wanted**, and accept
   that it costs about 1.2% cruise efficiency, a bought hub instead of a carved
   prop, and a taller redrive ratio. It does buy smoother running.
5. **Four and five blades never pay here.** Under-loaded at any rpm the engine
   can turn, 2–3% in profile drag, more hub weight and cost, and no compensating
   benefit while diameter is unconstrained.
6. **Do not shrink the disc to justify blades.** 48 in costs 32 ft of takeoff
   roll to save 6 in of thrustline.

## 8. What this does not settle

- `Cp/σ` is a **screening proxy**, not a design criterion. It is good for "two
  blades has run out of room," which is a geometric argument, and not good for
  predicting efficiency to a percent. Before committing, run a blade-element or
  vortex code, or take the numbers off manufacturer charts for a real blade.
- The −8 dB in §16 assumes sound pressure scaling as tip speed to the fifth.
  Reproduced here as −7.5 dB, so the two agree — but the result is very sensitive
  to that exponent, and a `V⁶` law or a power-based `10·log₁₀` reading gives a
  materially different answer. Worth pinning to a measurement or a cited model.
- Mean chord of 4.0 in for the reference two-blade prop is assumed, not measured.
  Every loading number here scales directly off it.
- The available belt redrive ratios have not been checked. That may cap the tip
  speed reduction before aerodynamics does.

---

*Same assumptions as the rest of `analysis/`: 28 hp Hirth F-33, 60 in disc,
50 mph cruise, 496 lb gross, Cd0 = 0.012 for a wood blade, figure of merit 0.75.*
