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
speed, flap geometry, spar depth, rib templates. Current numbers assume the Sky
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

**Flap geometry.** Chord fraction (25%c working number), span (~60% inboard),
hinge/false-spar detail, torque-tube diameter, Johnson-bar geometry and notch
loads. Plain flaps are far more forgiving than slats were — no
millimeter-critical gap — but the increment still wants verification:
NeuralFoil the flapped section at Re ~1M the same way the clean sections were
done. (Replaced the slat-geometry item: flaps-for-slats adopted, design-log
§21, with the quarter-scale stall demo as the escape clause.)

## Then, in order

- Full V-n diagram — **with the load basis re-set first**. The audit
  ([trades/design-audit.md](trades/design-audit.md)) shows fixed slats break the
  §12 stall-limit argument: g available at Vne is 5.74 at design weight, so
  either limit load rises to ~5.7 (+6–10 lb of cap, recommended) or Vne drops to
  ~62 mph — the tail-authority escape is closed: gate-3 trim analysis shows the
  elevator commands stall at every speed and CG. **Include the negative
  branch** (−1.9 g gust at Vc exists and no negative case does), and size
  fixed-mass fittings at the light-weight load factor
- **Pitch trim system — currently absent entirely, and required.** Elevator
  stick force is 2.5–2.7 lb across the envelope and the twist-grip decision
  put pitch and rudder on the same hand.
  [trades/borrowed-optimizations.md §3](trades/borrowed-optimizations.md)
  gives two options: **spring/bungee trim** at the stick base (lightest, no
  tab, no new flutter surface — AeroConversions' two-opposing-spring unit is
  $95, weight unpublished), or a **jackscrew-trimmable stabilizer**, which is
  heavier but solves trim, the incidence item below, and — critically —
  **preserves full elevator travel at every trim setting**, which a tab does
  not. That third property is not academic on an aircraft whose flare is its
  tightest control case. **Evaluate both in the gate-3 flap rerun** rather
  than defaulting to the lighter one; decide before the stick base is drawn
- **Adjustable stabilizer incidence — decide before the tail is welded.**
  The pending gate-3 flap rerun already expects to want ~1°; three shim
  positions at ±0.5° cost grams and turn a rebuild into a wrench. RV practice
  documents real post-first-flight corrections worth 2–3 kt of trim drag —
  a larger share of *excess power* on 22–31 hp than on their engines. On a
  welded cage with a single boom, retrofitting means cutting and re-welding.
  A jackscrew stabilizer (above) delivers this and the trim system together
- Spar cap taper schedule, web thickness, stiffener spacing
- **Cage member sizing — the architecture is decided, the tubes are not.**
  [trades/cockpit-cage.md](trades/cockpit-cage.md) fixes the rev F layout:
  all-steel, cage sta 30–96 on four longerons, **4130 3.50 × .049 boom welded
  to the aft frame** (the Kolb-fitting gate retires with the transition
  joint). Still open: longeron and diagonal sizes against the crash, gear and
  engine-mount reactions; **a rollover load basis, which no standard has been
  chosen for**; whether the front-spar pickups stay at ±8 in (wider reacts
  rolling moment better and fouls shoulders sooner — a mockup question); and
  the welded boom-to-cage cluster layout, still worth copying from Kolb even
  though the fitting is gone
- **Wing carry-through — cabane DELETED (rev G,
  [trades/enclosed-cockpit.md](trades/enclosed-cockpit.md)).** The wing sits
  on the cabin roof at chord line 58 and the sta 61.5 main hoop picks the
  front spar up directly at z=55. Remaining: **re-run `aero-model.py` for
  dihedral** — the high-wing pendulum arm drops 16% and this aircraft's roll
  control *is* dihedral, so expect +0.5–1°; and confirm the wing LE station
  still trims CG to 30% MAC with the seat moved forward 6 in for the recline
- **Egress — mechanism decided, execution unproven.** Positive film
  attachment plus **two mounted cutters** (design-log §25 addendum 2). What
  is left is physical: the **pre-slit and tab** at each panel's top corner
  (a shielded hook blade cannot puncture a taut membrane), bracket positions
  reachable **by feel and in gloves**, and a **timed proof test** from a
  fully assembled panel, in a harness, both sides. **~4–5 s** by the
  diagonal-cut-and-tear method, which clears the fire case
- **Glazing panel layout — a tear-arrest requirement, not a styling choice.**
  Film that tears at ~10 lbf for egress tears at ~10 lbf from a stone chip
  too, and cabin pressure keeps it primed. **The bead track is the ripstop:**
  divide the glazing at every cage member so a tear is arrested at the panel
  edge, and put the smallest panels low and forward in the spray zone. Do
  **not** substitute scrim-reinforced mesh — it would defeat the egress plan
- **Recline angle and seat station — mockup items.** 35° is the working
  number (head top z 49.5, hip sta 51); 30° eases entry and CG, 40° saves
  more drag. Also check head clearance (5.5 in on paper) with a helmet and
  the sling at full sag, and whether "open a door and sit in" actually works
  at the chosen sill height
- Gear geometry — **resolved** ([trades/landing-gear.md](trades/landing-gear.md)):
  mains sta 70.5 (15% MAC aft of CG), nose sta 32, track 56 in, seat 20 in AGL,
  8 fps / N=3 energy basis, 13×5.00-6 mains at 8–10 psi, tail skid. Remaining:
  leg curve/spring rate in gate 4, nose-leg spring detail, steering stops, and a
  456 lb drop test before first flight
- Tail sizing — **gate-3 analysis done** ([trades/trim-tail.md](trades/trim-tail.md)):
  keep 30 + 15 ft², i_t = −1.1°, elevator 45% chord ±25° (consider −30/+20),
  gearing ~4.5°/in, SM ~20–25%. Flare passes at forward CG in ground effect with
  23% margin. Remaining: **re-run with flap pitching moment and downwash**
  (flaps adopted, [trades/flaps.md](trades/flaps.md)) — full-flap flare at
  forward CG may saturate the elevator; expect a 25° landing notch or ~1° of
  tail incidence
- **Controls mechanization — DECIDED (design-log §21 + addendum,
  [trades/controls-mechanization.md](trades/controls-mechanization.md)):**
  one stick (elevator / lateral spoilerons / twist-grip rudder), left-hand
  symmetric spoiler lever (spring-return closed), rudder pedals deleted.
  Symmetric mode's payoff stands: ~720 → ~480 ft over the 50 ft trees.
  Remaining engineering, not decisions: **horn balance ~45% on the rudder**
  (the wrist-torque numbers do not close without it — size before the tail
  drawings freeze), grip centering/breakout behavior and brake-lever
  placement at the full-size seating mockup, no single-side hang-up from the
  symmetric path, Junco servo compatibility
- Cockpit geometry from actual seated dimensions — now for a **105–220 lb
  pilot range** (common-airframe §7): **mesh sling seat**
  ([trades/seat.md](trades/seat.md)) with lacing-tuned sag + adjustable
  footrest (the pedals are deleted with the twist-grip decision); mockup
  checks eye line and stick reach across the pilot range; sling **proof test
  to 1,920 lb** before first flight; crush-pad stroke clearance under the
  1-g sag point
- **Drag cleanup on the 80%** — open decision, the largest performance number
  left ([trades/borrowed-optimizations.md §2](trades/borrowed-optimizations.md)):
  wheel covers on the **mains only** (never the castoring nose — side area
  makes a weathervane), faired legs and cabane, and the footwell closeout the
  deleted pedals made free. ≈ −0.95 ft² of flat plate → **cruise L/D +15%,
  cruise power −13%** for ~1.6 lb, which the flaps/twist-grip/sling savings
  already cover. Decide with the pod shape, not after
- **Gap seals — seal the elevator; on the rudder, couple sealing to sizing.**
  NACA TN-632 measured a **sealed smaller surface matching an unsealed larger
  one at one-third the operating force**. First-order pass: a sealed rudder
  at cf/c ~0.29 (from 0.50) holds the same authority at **~57% less hinge
  moment** — twist-grip peak ~19 → ~8 in-lb, enough that **the 45% horn
  balance could become optional rather than mandatory**. Estimate only —
  but it means **rudder chord and sealing must be traded together, before
  the tail is drawn**, while both are still free. Friction, not hinge
  moment, is the real enemy: a teflon chafe strip under the seal is
  mandatory. Measure breakout with a spring scale on the built surfaces
- **Field rigging time as a numeric requirement** — proposed: one person, no
  helper, 15 minutes, no tools past a pin puller. Free if it constrains the
  wing-joint design now, expensive to retrofit after the joints are drawn
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
- **The ASI will lie during stall testing, and this project cannot afford
  that.** A Belite (Part 103) builder found his airspeed indicator failed
  completely at high alpha because the **pitot was micro-stalling** in
  oblique flow — 28–32.5 mph indicated against 29.1 calculated — fixed by
  bending the pitot into the local flow. This design chases a 23 kt stall
  with ~1 kt of regulatory margin: **plan pitot alignment and a calibration
  method (GPS three-leg or trailing cone) before first stall testing**, not
  after the numbers disagree.
- **Three weights nobody publishes, each blocking a decision** (see
  [trades/borrowed-optimizations.md](trades/borrowed-optimizations.md)): VG
  kit weight, GSC/Warp Drive ground-adjustable hub weight (**this one decides
  whether the 103 kit can use a re-pitchable prop**), and the
  AeroConversions trim system. All three want a phone call and a scale.
- **BRS package type against the pod-and-boom architecture.** §103.1 excludes
  the chute from the 254 lb empty weight, but an open cockpit with a single
  tail boom has nowhere to bury a softpack — which is why BRS catalogues
  vertical-launch (VLS) units specifically for the Kolb FireFly/FireStar.
  Confirm the BRS tray suits a VLS or canister unit before the cage is drawn.
- **Whether the 24 kt power-off stall is actually met in landing
  configuration.** Still a **legality item** — the stall gate caps gross at
  456 lb, which independently enforces the 254 lb empty limit. Much improved by
  the flaps decision: margin is now ~1.2 kt on a NeuralFoil-verified clean 1.45
  plus a textbook plain-flap increment, versus 0.1 kt on the unverified slatted
  1.8 it replaced. Verify the flapped section at Re ~1M, then on the
  quarter-scale model, then full-scale in Phase I.
- **Angle-of-attack annunciation — an EAB item, not a 103 one.**
  [trades/fly-by-wire.md §8](trades/fly-by-wire.md) concludes that telling the
  pilot the AoA delivers most of the benefit of active stall protection with
  **no actuator, no authority question and nothing that can fail inside the
  control circuit**, aimed at the accident category (LOC-I) behind ~40% of
  fatal GA accidents. Two caveats kept honest: **no controlled study
  quantifies accident-rate reduction from AoA indicators**, and a complete
  system is *"not quite two pounds"* — **the 103 kit cannot afford that**, so
  it rides on the EAB where the Junco already supplies display and plumbing.
  Resolve probe location and calibration **together with the pitot alignment
  item above** — both are air-data sensors in a flow field nobody has mapped,
  and the stall numbers depend on both
- **Battery capital cost, currently carried as $500/kWh in design-log §3.** That
  single figure decides the electric argument and has never been re-verified
  against current DIY 21700 pack prices. Check it before citing §3 again.
- **Whether the tail can give adequate roll authority unblown.** Gates any future
  pusher configuration, since the rudder is the roll control. The quarter-scale
  model cannot answer it — it is a full-scale, power-on question.
- **Ground-adjustable composite hub weights on a scale (EAB only).** The
  fleet currently buys two fixed wood props; a re-pitchable hub is what the
  ultralight world uses and what a two-engine, Phase-I-measured programme
  wants — but the 103's ~1 lb margin cannot carry the extra weight, so wood
  stays there regardless. See
  [trades/borrowed-optimizations.md §5](trades/borrowed-optimizations.md)
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
- **Flap conversion weight on a scale.** The ~−1 lb net for flaps-for-slats
  (now adopted — design-log §21) is an estimate; hinges, torque tube, lever,
  and TE stiffening get weighed before the 253.2/275.7 lb ledger re-baselines.
- **Docile stall on the quarter-scale model, flaps up and down.** The
  flaps decision's escape clause: straight-ahead break, no wing drop, or the
  decision reverts to slats. **Vortex generators are now the first-line
  remedy ahead of that reversion**
  ([trades/borrowed-optimizations.md §1](trades/borrowed-optimizations.md)):
  ounces, bondable to Oratex, flight-line tunable, and aimed at exactly the
  outer-panel attached-flow property the slats used to provide. Keep the
  outer leading edge accessible and do not let the tip cap preclude them. (The slat-tip-termination item retired with the
  slats — the moulded tip cap is now unconstrained at the leading edge.)

## Not analysed anywhere, and should be

**Flutter.** No flutter analysis exists for this wing, tail, or control surfaces at
any configuration. §12 establishes the wing is stall-limited and therefore cannot
be aerodynamically overstressed, which is a load-factor argument and says nothing
about flutter. This gates Vne, mass balance on the elevator and rudder, and any
future decision to hang mass at the wingtips.

## Not technical, but decide early

**~~Drafting for yourself or for publication~~ — DECIDED (design-log §21):
for publication.** Full-size rib templates, a materials list with sizes and
sources, an assembly sequence; roughly triple the drafting effort, accepted.

**~~Whether the CAD is built to output cut files~~ — DECIDED (design-log §21):
yes.** 3D-first CAD from which DXF and STL fall out, per
[trades/digital-fabrication.md](trades/digital-fabrication.md). Published
plans ship cut files, which no other design in this class does.

**~~The covering system~~ — DECIDED (design-log §14 addendum): Oratex.**
75 hours and 8 lb bought for ~$1,400. The second-build caveat (covering is 27%
of aircraft #2 and Oratex pays its premium twice) was acknowledged and
accepted, because:

**~~Whether there is ever a second aircraft~~ — DEFERRED, deliberately
(design-log §21): decided after #1 proves out.** The first steel order is
sized for one aircraft. The DXF nesting is paid regardless, so a second 4130
set later costs only a repeat shop setup — that is the price of deferring, and
it is small. If #2 becomes real, ask a DAR early (major-portion rule and
repairman certificate apply per aircraft).

**Where Phase I happens — still open, and fine to hold until the build is well
along.** Phase I is the FAA's initial flight-test period for the EAB aircraft:
its operating limitations assign a test area (a radius and altitude block) in
which the required hours — typically 40 for a non-certified engine — must be
flown before passengers or ordinary cross-country flying. So the question
means: *which airport or large field hosts the initial test flying?* It needs
somewhere those hours can be flown without fighting airspace, and first flight
of a modified one-off does not belong in a backyard. (The pure-103 sister ship
has no formal Phase I, but its shakedown flying wants the same big field.)
Needs deciding before the EAB airworthiness application, not before drawing.

## Cowl height, and the forward view (rev H, §26)

The over-the-nose view is set by the engine, not the glazing. The cowl crown is
at z 47.3, **1.8 in above the pilot's eye**, so there is no depression angle
over the top of the nose at all — the pilot looks 2.9° *up* to clear it.

That crown allows the engine 7.3 in above the crank centreline, and **an
upright Hirth F-33 cylinder is taller than that.** So one of these has to give:

- the engine gets **clocked or tilted** to fit under the line;
- the **cowl grows**, and the forward view gets worse than the numbers in §26;
- the **thrustline drops**, which the propeller ground clearance in
  `trades/landing-gear.md` does not currently allow;
- the **eye rises**, which costs wing height and gives back the rev G drag win.

**Blocked on a physical measurement: an engine on the bench, with a tape on
it.** Nothing else settles this, and it decides the shape of the nose.

## Glazing frame materials (rev H, §26)

The wraparound screen is not developable, so it is three panels per side on
frame rails — 303 in of tube, **2.6 lb** as drawn in 3/8 × .028 4130 against
the 1.0 lb the ledger carried. That 1.6 lb is what pushes the Part 103 aircraft
off a Lexan nose. Untried: aluminium extrusion, a smaller tube, or deleting the
phi = 95° rail if 0.060 sheet proves stiff enough to span unsupported.

## The frame is in six disconnected pieces (rev H, §27)

`analysis/frame.py` turned the cage from thirty hard-coded `strut()` calls into
a node/member graph, and the graph answers a question the tube mesh could not:
**do these tubes actually meet?** Overlapping cylinders look welded. They are
not. `python3 analysis/frame.py` prints the list; this is what it finds.

Only the **14-node cage box** — nose bow, longerons, main hoop, diagonals, aft
frame — is one connected structure. Everything else floats:

| Island | What it is | What it needs |
|---|---|---|
| `RF_L RF_R RP_L RP_R` | the **rear frame**: rear spar carry-through, seat back, harness anchor | `RF` sits **2.70 in** off the lower longeron. Either drop `RF` onto the longeron line, or add a member from `RF` to it. **A harness anchor that is not welded to the cage is not a harness anchor.** |
| `BM_C TP_C` | the **tail boom** | `BM_C` floats **3.00 in** between the two aft-frame crosses. The boom picks up on the aft frame through a fitting that is not modelled. Either model the fitting or move the crosses to meet the tube. |
| `NGU_C NGF_C NAX_C` | the **nose leg** | `NGU_C` is meant to land on the nose bow, but the nose bow is a **U, not a hoop** — there is a crown at `NT_L`–`NT_R` and no lower cross member. Nothing exists at `(30, 0, 17)` to weld to. And `NGF_C` still floats at station 14 (below). |
| `MGF_R MAX_R MGS_R` ×2 | the **main gear** | the trailing-arm pivot `MGF` is 2.4 in outboard and 3.5 in below the lower longeron at that station. Same question: fitting, or move it onto the tube. |

Two more near misses inside the cage box itself, which are the serious ones:

- **The main hoop feet do not land on the longerons.** `MH` is **3.44 in** from
  the lower longeron at 47% along it. That frame carries **88% of wing lift —
  1,519 lb per side fitting** — and is the rollover structure. Its feet have to
  tie into the longerons or into a fitting that does.
- **`NGF_C` attaches to nothing.** Station 14, sixteen inches forward of where
  the cage starts. It came in with the rev D raked nose leg as *"closes the
  crush-bay triangle"* and was never tied to a node. Either it lands on the
  nose bow, or it lands on the engine mount, or the member goes away.

**Nothing has been moved to fix this.** The coordinates are exactly what rev G
carried; all that changed is that they can now be checked. Fixing it is a
design decision — how much of it wants a welded joint and how much wants a
bolted fitting — and `analysis/frame.py` will re-check whatever comes back.

Related: the frame's own tube schedule comes to **48.4 lb** (27.5 cage, 13.2
boom, 7.7 gear) with **no gussets, no fittings and no weld metal**. The build
log CSV carries 31 + 5 + 4 = 40 lb for a cage that predates the pod-and-boom
architecture. Those two do not reconcile yet, and that is already on the list
as **workbook reconciliation**.

