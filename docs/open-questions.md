# Open Questions

Nothing in this project is drawn yet. These are the items that block drawing,
in the order they need resolving.

## Blocking everything

**The two weight statements disagree.** The workbook Weight sheet omits the slats
(6 lb) and the cabane (6 lb) that `build-log/measured-weights.csv` carries:
honest EAB empty is ~308 lb, and the 103 strip is ~262 — **8 lb over the limit,
not 4 under**. Reconcile the workbook before quoting it. Full scrub and a
single-build path to ~253 lb in
[trades/weight-scrub-103.md](trades/weight-scrub-103.md).

**The engine, if the first build chases Part 103.** The scrub shows the airframe
can reach ~224 lb less power package, but the F-33 + belt (45 lb) cannot land
under 254 — a ~31 lb dual-spark paramotor-class engine (Polini Thor 250 DS
class, integral redrive) can, at ~253 lb and 23.9 kt stall. §15's 300-hr TBO
objection is mission-dependent at ~40 hr/yr. Verify actual engine weights on a
scale; keep the F-33 as the documented EAB upgrade path on the same mount.

**Airfoil section and its real CLmax.** Everything downstream hangs on it: stall
speed, slat geometry, spar depth, rib templates. Current numbers assume the Sky
Pup section at CLmax 1.4 clean, which is an assumption, not a measurement.
*First numbers now exist*: NeuralFoil at Re 1.12 M puts NACA 4412 at 2-D CLmax
1.61 (≈1.45 on the wing), so 1.4 is sound and slightly conservative. **4412 is the
working candidate** — see the addendum in
[trades/design-audit.md](trades/design-audit.md). Confirm against the true Sky Pup
section if it can be obtained.

**Dihedral and washout.** On a two-axis aircraft dihedral *is* roll control. Too
little means no authority, too much means dutch roll. Current placeholder is 4-6
degrees per side and 2-3 degrees washout. Needs the original design's actual
values or a defensible derivation.

**Slat geometry.** Chord, gap, overlap, droop angle. Millimeters decide whether a
slat produces CLmax or just drag. Intent is to copy a known installation
dimension-for-dimension (CH701, Highlander) rather than derive it.

## Then, in order

- Full V-n diagram — **with the load basis re-set first**. The audit
  ([trades/design-audit.md](trades/design-audit.md)) shows fixed slats break the
  §12 stall-limit argument: g available at Vne is 5.74 at design weight, so
  either limit load rises to ~5.7 (+6–10 lb of cap, recommended) or Vne drops to
  ~62 mph — the tail-authority escape is closed: gate-3 trim analysis shows the
  elevator commands stall at every speed and CG. **Include the negative
  branch** (−1.9 g gust at Vc exists and no negative case does), and size
  fixed-mass fittings at the light-weight load factor
- Spar cap taper schedule, web thickness, stiffener spacing
- Wing carry-through and cabane geometry, which sets the wing LE station that
  trims CG to 30% MAC
- Gear geometry — **resolved** ([trades/landing-gear.md](trades/landing-gear.md)):
  mains sta 70.5 (15% MAC aft of CG), nose sta 32, track 56 in, seat 20 in AGL,
  8 fps / N=3 energy basis, 13×5.00-6 mains at 8–10 psi, tail skid. Remaining:
  leg curve/spring rate in gate 4, nose-leg spring detail, steering stops, and a
  456 lb drop test before first flight
- Tail sizing — **gate-3 analysis done** ([trades/trim-tail.md](trades/trim-tail.md)):
  keep 30 + 15 ft², i_t = −1.1°, elevator 45% chord ±25° (consider −30/+20),
  gearing ~4.5°/in, SM ~20–25%. Flare passes at forward CG in ground effect with
  23% margin. Remaining: re-run with the measured slat pitching-moment increment
  once slat geometry is copied from the donor installation
- **Symmetric spoiler deployment mode.** Landing over the mission's own 50 ft
  trees at L/D 10.7 with no glidepath control uses ~720 of the 1,000 ft field,
  and a two-axis aircraft cannot slip. Both-spoilers-up (separate lever,
  spring-return fail-safe per §9) cuts it to ~480 ft. Cheapest meaningful
  improvement the audit found; decide before the spoileron rigging is drawn
- Cockpit geometry from actual seated dimensions — now for a **105–220 lb
  pilot range** (common-airframe §7): adjustable pedals, and seat geometry that
  fits both the EAB owner and a 105 lb Part 103 pilot
- Every fitting, detailed

## Verify before committing

- **The Part 103 engine's actual power rating — and more importantly its prop
  diameter.** The audit shows a direct-drive two-stroke is tip-speed limited to a
  35–42 in prop, giving ~96–114 lb static and a **240–340 ft ground roll**, not
  the ~160 ft claimed. The deleted 10 lb redrive is worth ~140 ft of runway.
  Either the 103 keeps a lightened redrive or the README's 103 field numbers get
  rewritten.
- **Spoileron aerodynamic close direction.** Tape a panel on and measure with a
  spring scale at 25 and 35 mph before trusting that airflow shuts it.
- **Whether the 24 kt power-off stall is actually met with slats.** Calculated at
  23.8 kt, which is 0.8 kt of margin on an estimated CLmax. **Upgraded by the
  weight scrub: this is now a legality item, not performance** — the stall gate
  caps gross at 456 lb, which independently enforces the 254 lb empty limit.
  If real slatted CLmax is 1.7 instead of 1.8, the compliance equation breaks.
- **Battery capital cost, currently carried as $500/kWh in design-log §3.** That
  single figure decides the electric argument and has never been re-verified
  against current DIY 21700 pack prices. Check it before citing §3 again.
- **Whether the tail can give adequate roll authority unblown.** Gates any future
  pusher configuration, since the rudder is the roll control. The quarter-scale
  model cannot answer it — it is a full-scale, power-on question.
- **Propeller rpm, which decides blade count.** Two blades is comfortable to about
  1,750 rpm and cannot carry 1,600. Pick the rpm against an actual available belt
  redrive ratio, then the blade count follows. Do not pick blade count first.
- **The tip-speed noise exponent in §16.** The 8 dB claim reproduces only under a
  pressure ∝ V⁵ law; a power-based reading gives about 3.7 dB. Worth a measurement
  or a cited model before a redrive ratio is bought to chase it.
- **Wingtip shape.** Free L/D, and currently unspecified. Worth +2.9% off the
  assumed span efficiency and +9.5% against a square-cut tip — more than any
  winglet, at zero weight. Decide it with the tip bow, not after. Direction is
  moulded carbon caps to a copied Hoerner geometry — see
  [trades/wingtip-caps.md](trades/wingtip-caps.md).
- **Where the full-span slat terminates at the tip.** Constrains the tip cap
  geometry, and §10's "copy a known installation" rule has nothing to copy for a
  slat-to-moulded-tip junction. Resolve before the cap shape is frozen.

## Not analysed anywhere, and should be

**Flutter.** No flutter analysis exists for this wing, tail, or control surfaces at
any configuration. §12 establishes the wing is stall-limited and therefore cannot
be aerodynamically overstressed, which is a load-factor argument and says nothing
about flutter. This gates Vne, mass balance on the elevator and rudder, and any
future decision to hang mass at the wingtips.

## Not technical, but decide early

**Drafting for yourself or for publication.** Publishable plans need full-size rib
templates, a materials list with sizes and sources, and an assembly sequence.
Roughly triple the drafting effort.

**Whether the CAD is built to output cut files.** This has to be decided before
the first drawing, not after — see [trades/digital-fabrication.md](trades/digital-fabrication.md).
Drawing in 3D so that DXF and STL fall out is nearly free now and expensive to
retrofit, and it is worth an estimated 90–160 adjusted hours across the build.
It also decides whether published plans can ship cut files, which no other design
in this class does.

**The covering system, which is worth more hours than any tooling decision.**
§14 prices Oratex at roughly 75 hours against Stewart for about $1,400. Covering
is the single largest task on the build at 120 raw hours and digital fabrication
does essentially nothing for it. If hours bind harder than dollars, settle this
first.

It gets worse on a repeat. [trades/second-build.md](trades/second-build.md) puts
covering at **27% of a second aircraft** — everything else improves with tooling
and experience and covering does not. If a second build is plausible, §14's lean
toward Stewart should be revisited before the first order.

**Whether there is ever a second aircraft, decided before the first steel order.**
The marginal cost of a second nested set of laser-cut 4130 is far below the first,
since the DXF and nesting are already paid for. Same for spar cap stock and any
minimum-order material. And if a second EAB aircraft is a real plan, ask a DAR
early — the major portion rule and the repairman certificate both apply per
aircraft, and the answer may change what gets documented during build 1.

**Where Phase I happens.** The test area goes into the operating limitations as a
radius and altitude block. It needs to be somewhere 40 hours can actually be flown
without fighting airspace, and first flight of a modified one-off does not belong
in a backyard.
