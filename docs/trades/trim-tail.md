# Gate 3: Trim and Tail Analysis

Classic wing-plus-tail trim equations over the full speed and CG range, with
parameters from `analysis/aero-model.py` (wing a = 4.42/rad, NACA 4412
Cm₀ ≈ −0.10) and the repo geometry. Script: `analysis/trim-tail.py`.

**The headline: the elevator has authority to spare everywhere — including the
one place it would have been convenient not to.** Full-up elevator commands the
wing past stall at every speed in the envelope, so **audit Finding 1's option
(c) is closed: the aircraft cannot be saved from the Vne overstress case by
tail-authority limits. The structural fix is required** — raise the limit load
to ~5.7 g (+6–10 lb of cap) or lower Vne to ~62 mph.

## Gate-3 outputs

| Item | Value |
|---|---|
| Tail incidence, hands-off at 50 mph, 30% CG | **i_t = −1.1°** (placeholder was −1.5°) |
| Horizontal tail | **keep 30 ft²**, 10 ft span |
| Elevator | **45% chord, ±25°** — sufficient, see flare margin |
| Vertical tail / rudder | **keep 15 ft²**, rudder ~45% chord, ±25° |
| Static margin (classic) | NP at 51% MAC → **21% at 30% CG**, 16% at 35% |
| Stick gearing (suggested) | ±25° elevator over ±5.5 in stick → **4.5°/in** |

Static margin cross-check: classic 21%, VLM 24%, component buildup 40% (the
buildup over-counts the fuselage here). Call it **~20–25%** — high for GA norms
(5–15%) but deliberate on a two-axis aircraft, and the flare check below proves
it is not too high to land.

## 1. Trim across the envelope

Elevator to trim, 1 g, 496 lb (+down / −up, limit ±25°):

| V mph | CG 25% | CG 28% | CG 31% | CG 35% |
|---|---|---|---|---|
| 29 (stall) | −16.6 | −13.5 | −11.1 | −7.2 |
| 38 | −7.2 | −5.3 | −4.0 | −1.7 |
| 50 (cruise) | −1.6 | −0.5 | +0.3 | +1.6 |
| 60 | +0.7 | +1.5 | +2.0 | +2.9 |
| 69 (Vne) | +2.0 | +2.6 | +3.0 | +3.7 |

Everything is comfortably inside the throw, the gradient is stable (more up
elevator as speed falls) at every CG, and cruise sits near zero deflection —
which is what the −1.1° incidence buys: minimum trim drag where the aircraft
lives.

## 2. Flare authority — passes with real margin

Trim to 0.95 CLmax (CL 1.71) in **ground effect** (lift slope +10%, downwash
halved — both make flare harder) at the **forward CG limit**:

| Weight | Speed | Elevator needed | Margin | Tail CL |
|---|---|---|---|---|
| 496 lb | 29.5 mph | **−19.3°** | 5.7° (23%) | −0.18, far from tail stall |
| 426 lb | 27.4 mph | −19.3° | 5.7° | −0.18 |

The high static margin does **not** cost the landing. 23% deflection margin is
adequate rather than generous; if the slats' pitching-moment increment turns out
more nose-down than the 4412 section value (see caveats), the cheap insurance is
**asymmetric throw: −30° up / +20° down**, which is free at the bellcrank.

## 3. Finding 1c — closed, and the structural decision is now forced

Full-up elevator (−25°), free air, solving the pitch balance for the commanded
wing CL (linear model, no stall):

| V | CG 28% | CG 31% | CG 35% |
|---|---|---|---|
| any speed | CL 2.83 | CL 3.18 | CL 4.05 |

Commanded CL is **1.6 to 2.2× the slatted CLmax** at every CG including the
forward limit. The wing stalls long before the elevator runs out. There is no
tail-authority protection at Vne, at any loading — **the aircraft is
stall-limited, exactly as §12 intended, which means the stall-limited g at Vne
(5.74 at design weight, audit Finding 1) is physically reachable with a pull.**

So the options remaining from the audit are:

1. **Raise limit load to 5.74 g / ultimate 8.6 — about +6–10 lb of cap.
   Recommended.** It restores §12's "cannot be overstressed" honestly.
2. Lower Vne to ~62 mph. Free but thins cruise-to-Vne margin to almost nothing,
   and Finding 3 (Vmax level ≈ 80) makes a lower Vne *harder* to respect, not
   easier.

Deliberately *reducing* elevator throw to create protection is not recommended:
the flare needs −19.3°, and a throw low enough to protect the structure at Vne
(roughly −11° by these equations) cannot land the airplane.

## 4. Rudder-roll authority — §9's "adequate rather than crisp," now with numbers

Using the VLM derivatives (Clβ −0.082, Cnβ +0.107 /rad), rudder Cnδr ≈
−0.062/rad, roll damping Clp ≈ −0.50, spoileron ΔCl ≈ 0.020:

| V | Rudder-only roll | Rudder + spoileron | Time to 30° bank |
|---|---|---|---|
| 38 mph | 9.0°/s | **17.2°/s** | ~2.4 s |
| 50 mph | 11.8°/s | **22.6°/s** | ~2.0 s |

- Full rudder holds a steady sideslip of **15°**, which at a 37 mph approach is
  roughly a **10 mph crosswind** capability. Placard accordingly.
- The spoilerons carry **half the roll authority**. Rudder-only (a spoileron
  cable failure) still rolls, at glider-like rates — consistent with §9's
  fail-safe argument, now quantified.
- ~2 s to 30° bank is ultralight-normal and matches the Sky Pup's reputation.
  It will not feel crisp. It is not supposed to.

## 5. Caveats, honestly

- **Linear aero throughout.** Commanded CL 2.8–4.0 means "far past stall," not
  a real lift number. The conclusion (stall-limited, not elevator-limited) is
  robust to that; the exact alphas are not.
- **The slat pitching-moment increment is not in Cm₀.** Fixed slats typically
  shift Cm slightly nose-up (helpful for flare margin) but the slat literature
  varies; re-run `trim-tail.py` with the measured increment once slat geometry
  is copied from the donor installation. The trim map moves a degree or two;
  the Finding-1c conclusion does not move.
- Elevator effectiveness τ = 0.63 assumes a plain 45%-chord elevator with
  sealed gaps. An unsealed gap costs ~10% — seal it.
- Tail efficiency 0.90 is power-off, which is the critical case for flare. With
  power the tractor slipstream only adds authority.
- Downwash by lifting-line estimate; ground-effect factors are handbook values.

## What this unlocks

Gate 3 is done pending the slat-Cm check: **tail sizes confirmed as drawn in
the weight sheet (30 + 15 ft²), i_t = −1.1°, throws ±25° (consider −30/+20),
gearing ~4.5°/in.** Gate 1 (load basis) now has its decision forced — option 2,
the +6–10 lb of cap — and gate 4 (spar package) can proceed against 5.7 g limit
/ 8.6 ultimate plus the −1.9/−2.85 negative case.
