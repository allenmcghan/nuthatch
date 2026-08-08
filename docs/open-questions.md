# Open Questions

Nothing in this project is drawn yet. These are the items that block drawing,
in the order they need resolving.

## Blocking everything

**Airfoil section and its real CLmax.** Everything downstream hangs on it: stall
speed, slat geometry, spar depth, rib templates. Current numbers assume the Sky
Pup section at CLmax 1.4 clean, which is an assumption, not a measurement.

**Dihedral and washout.** On a two-axis aircraft dihedral *is* roll control. Too
little means no authority, too much means dutch roll. Current placeholder is 4-6
degrees per side and 2-3 degrees washout. Needs the original design's actual
values or a defensible derivation.

**Slat geometry.** Chord, gap, overlap, droop angle. Millimeters decide whether a
slat produces CLmax or just drag. Intent is to copy a known installation
dimension-for-dimension (CH701, Highlander) rather than derive it.

## Then, in order

- Full V-n diagram at 4.7g limit, 7.0g ultimate
- Spar cap taper schedule, web thickness, stiffener spacing
- Wing carry-through and cabane geometry, which sets the wing LE station that
  trims CG to 30% MAC
- Gear geometry: main gear 12-16% MAC aft of CG, track, wheelbase, nose steering
  stops and travel
- Tail sizing, with a generous rudder since it is doing the rolling
- Cockpit geometry from actual seated dimensions
- Every fitting, detailed

## Verify before committing

- **The Part 103 engine's actual power rating.** The 103 configuration leans on a
  direct-drive engine around 16 hp at 28 lb. If the rating is lower than assumed,
  climb margin goes with it.
- **Spoileron aerodynamic close direction.** Tape a panel on and measure with a
  spring scale at 25 and 35 mph before trusting that airflow shuts it.
- **Whether the 24 kt power-off stall is actually met with slats.** Calculated at
  23.8 kt, which is 0.8 kt of margin on an estimated CLmax.
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
  winglet, at zero weight. Decide it with the tip bow, not after.

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

**Where Phase I happens.** The test area goes into the operating limitations as a
radius and altitude block. It needs to be somewhere 40 hours can actually be flown
without fighting airspace, and first flight of a modified one-off does not belong
in a backyard.
