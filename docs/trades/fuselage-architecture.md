# Fuselage Architecture: Steel Cockpit Cage + One Straight Boom

**The question:** can the fuselage be designed to actually be easy to
construct — a single straight boom to the tail and a simple, aerodynamic
cockpit — instead of what the drawings have been showing?
Script: `analysis/fuselage-boom.py`.

**Short answer: yes, and this is adopted as the architecture (rev E).** The
drawings were wrong, not the idea. What the record actually called for
(design-log §5) was a welded 4130 tube fuselage — but the digital-fabrication
plan silently assumed that truss ran the *full ~190 in* to the tail post, and
the 3D mesh drew a fat continuous body over it. Neither was ever a decided
requirement. The architecture that matches both the mission and the
easy-to-build goal is the one Kolb has used on Part 103-class aircraft for
forty years: a **welded 4130 cockpit cage** carrying everything that needs
steel, and a **single straight aluminum tube boom** carrying the tail.

## 1. What went wrong with the drawings

The mesh lofted one continuous fuselage from the nose to sta 184 with a
cockpit-depth cross-section fading out gradually — it read as a big
slab-sided monocoque. That was a rendering choice, not a structural one; no
trade ever chose that shape. The structure behind it (per
[digital-fabrication](digital-fabrication.md)) would have been a 190-in
welded truss: 130 build hours, a full-length eggcrate jig, and the
out-of-square risk that comes from ~160 hand-coped fishmouth joints. This
trade replaces the aft half of that plan and the drawings both.

## 2. The two architectures

| | Full welded truss (old assumption) | Cage + boom (rev E) |
|---|---|---|
| Aft structure | 4 longerons + ~40 diagonals, sta 96–182 | one 6061-T6 drawn tube |
| Aft weight | ~14 lb + fabric stringers | ~10.5 lb incl. fittings |
| Weld joints aft of cockpit | ~80 fishmouthed ends | zero |
| Aft jig | eggcrate stations, ~90 in of it | none — a drawn tube is straight by manufacture |
| Torsion (rudder loads) | truss must be diagonally braced in all four planes | closed round tube: best torsion section there is; shear works out at 2.7 ksi, trivial |
| Precedent | Airbike, Legal Eagle | **Kolb Firefly (a Part 103 aircraft), Firestar, and the whole Kolb line** |

## 3. Boom sizing

Load basis is the fleet's Vne 62 mph, boom root at the aft cage bulkhead
(sta 96), tail post at 182 — an 86 in arm:

- H-tail max load 295 lb limit → **38,000 in-lb ultimate** bending (matches
  the 37,800 figure the losers table has carried since the inflatable-wing
  trade — good sign the numbers agree with themselves).
- V-tail 147 lb limit → 19,000 in-lb lateral + 6,600 in-lb torsion.

**Selected: 6061-T6, 5.00 in OD × 0.065 wall.** Allowable set by thin-wall
local buckling with a conservative 0.25 knockdown, not by material strength:
47,900 in-lb ultimate → **+26% margin**. The 0.058 wall technically closes at
+1% but that is no margin at all for a tube that will get hangar rash; the
extra 1 lb buys the margin. Tip deflection at limit load is 2.0 in and the
first bending mode is ~8 Hz — both recorded as inputs to the flutter item,
which remains open. Control cables and wiring run *inside* the boom, Kolb
style, which also tidies the aerodynamics for free.

## 4. What stays steel, and why

Design-log §5's argument for steel was never about the aft fuselage — it was
about the concentrated-load hardware: **nose bow, rollover hoop, harness
anchors, gear mounts, engine mount cluster**. All of that lives forward of
sta 96, in the cockpit cage. The cage keeps every crash-structure property
already committed (rev D crush bay, 15 in ahead of the rudder pedals,
included). The cage-to-boom joint is a machined/bolted sleeve collar at the
aft bulkhead; per the project's copy-a-known-installation rule, the boom root
and tail-post fittings get **copied dimension-for-dimension from a Kolb
installation**, not derived.

## 5. The cockpit pod: simple *because* it is not structure

With the cage doing all the work, the pod is pure fairing — windshield line,
a teardrop in plan, closing at the boom junction: four to six wood or
aluminum stringers off the cage, fabric over them, done. No compound-curve
fiberglass unless it is wanted for looks. Shape is free to be aerodynamic
because nothing structural constrains it, and it can change after first
flight without touching a load path.

## 6. Ledger

- **Weight:** boom + fittings ~10.5 lb vs ~14 lb of aft truss and stringers —
  about even to −4 lb. The 55 lb fuselage-structure line in the
  [common-airframe](common-airframe.md) ledger is unchanged; any saving is
  margin, not banked.
- **Hours:** the 130-hour weld-jig-and-fuselage line loses its aft half:
  ~80 fishmouths and the aft jig are deleted. Estimate **35–45 hours saved**,
  and — worth more than the hours — the aft fuselage can no longer be built
  out of square, because it is one bought tube.
- **Airframe invariant:** unaffected. The cage + boom is the same on the 103
  and EAB aircraft; nothing about the kits changes.

## 7. Verdict and gates

**Adopted: welded 4130 cockpit cage (nose to sta 96) + 6061-T6 5.00 × .065
straight boom (sta 96–182), rev E of the geometry.** Gates before drawings
freeze:

1. Copy the Kolb boom-root and tail-post fitting dimensions from a real
   installation (photos and measurements, not the general idea).
2. The flutter item inherits the boom stiffness numbers above (2.0 in tip
   deflection at limit, ~8 Hz first mode) as inputs.
3. Verify 5.00 × .065 6061-T6 drawn tube is actually purchasable in an 88 in
   length (it is a stock Wicks/Aircraft Spruce size class; confirm before
   the structure is drawn around it).
