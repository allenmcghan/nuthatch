# Trades

Twenty-one worked configuration trades. Each one closes with a *"what this does
not settle"* section, and the ones that lost are written up as carefully as the
ones that won — drawings exist for a dozen aircraft in this class, reasoning
does not.

The narrative order and the decisions live in
[../design-log.md](../design-log.md). This is the index.

## Configuration

| Trade | Outcome |
|---|---|
| [pusher-vs-tractor](pusher-vs-tractor.md) | **Tractor.** Efficiency is a wash; balance diverges and the unblown tail loses authority at rotation. A pusher, if ever, arrives with an electric conversion |
| [propeller-blade-count](propeller-blade-count.md) | **Two blades**, comfortable to ~1750 rpm — 3–4 dB free. Don't shrink the 60 in disc |
| [winglets](winglets.md) | **No winglets.** Span isn't constrained, and the Oswald uncertainty is wider than the benefit |
| [wingtip-caps](wingtip-caps.md) | **Moulded carbon tip caps** instead — weight-neutral, and a shape fabric cannot hold |
| [v-tail](v-tail.md) | **Rejected.** Same area for no weight saved, plus a mixer, routine saturation in the flare, and adverse roll fighting the steering |
| [amphibious](amphibious.md) | **Rejected.** Properly sized floats put their bows forward of the prop disc |
| [fly-by-wire](fly-by-wire.md) | **Rejected**, except the spoileron servo — the only surface whose fail-safe already covers one |

## Structure

| Trade | Outcome |
|---|---|
| [fuselage-architecture](fuselage-architecture.md) | **Pod and boom**, not a full-length truss — ~80 fishmouth joints and the aft jig deleted. *(Its aluminium boom was reversed — see below)* |
| [cockpit-cage](cockpit-cage.md) | **All-steel.** CG, front spar and rollover hoop converge within 2.5 in, so **one frame at sta 61.5 does three jobs**. A thin-wall boom is buckling-limited, so steel wins it back |
| [enclosed-cockpit](enclosed-cockpit.md) | **Reclined pilot, wing onto the cabin roof, cabane deleted.** L/D 10.8 → 12.4, and −5.5 lb that paid for the steel boom |
| [seat](seat.md) | **Mesh sling over a crushable pad** — ~1.8 lb, and the energy absorption survives. Proof test to 1,920 lb |
| [landing-gear](landing-gear.md) | **Trailing arms on MTB coil-overs, bicycle wheels, raked nose leg.** Nose-over protection 17.9° → 35.5° |

## Aerodynamics and loads

| Trade | Outcome |
|---|---|
| [design-audit](design-audit.md) | The end-to-end audit that **broke the load basis** — slats broke the stall-limit argument, no negative-g case existed, and level flight exceeded Vne |
| [flaps](flaps.md) | **Single-lever plain flaps replace the fixed slats.** Escape clause: a wing drop on the quarter-scale demo reverts it |
| [trim-tail](trim-tail.md) | **Tail confirmed as drawn.** The elevator commands stall at every speed and CG; the flare passes at forward CG in ground effect |
| [borrowed-optimizations](borrowed-optimizations.md) | What the rest of the ultralight world has that this design should take — VGs, gap seals, drag cleanup, a ground-adjustable **wood** prop |

## Fleet, weight and process

| Trade | Outcome |
|---|---|
| [common-airframe](common-airframe.md) | **One airframe, two kits.** Vne 62 mph fleet-wide makes the spar stall-protected at every gross for free |
| [weight-scrub-103](weight-scrub-103.md) | The two weight statements disagree; line-by-line scrub finds −41 lb. **Reconciliation is currently parked** — see [../specs.md](../specs.md) |
| [digital-fabrication](digital-fabrication.md) | **Tooling, not flight parts.** No laser holes at final size, no laser-cut structural ply |
| [second-build](second-build.md) | 370–460 hours with tooling in hand. **Aircraft #2 deferred until #1 proves out** |

## Superseded, and marked as such

- **[fuselage-architecture](fuselage-architecture.md)** chose a **6061-T6
  aluminium boom**. Rev F reversed it to 4130 steel — the architecture stands,
  the material does not. The banner is at the top of the file, and
  `analysis/fuselage-boom.py` carries the same warning.
- The **fixed slats** in the early sections of the design log were replaced by
  flaps. The **cabane** was deleted by rev G. Both survive in the log because
  the reasoning that retired them is the useful part.
