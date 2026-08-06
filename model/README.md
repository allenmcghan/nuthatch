# Quarter-Scale Validation Model

Built before the full-size airframe to prove the handling before committing to a
garage build.

## Why quarter scale and not eighth

Reynolds number is the whole issue and scale is the only lever on it. For Froude
similarity, weight goes as scale cubed and speed as the square root:

| Scale | Span | Froude weight | Froude speed | Re |
|---|---|---|---|---|
| 1/8 | 46 in | 0.97 lb | 12 mph | 57,000 |
| 1/4 | 7.75 ft | 7.75 lb | 16.5 mph | 161,000 |
| Full | 31 ft | 496 lb | 33 mph | 1,280,000 |

Quarter scale is three times the Reynolds number and still an ordinary large RC
aircraft at 15 oz/ft². It is also big enough that the wing joint and the spoileron
linkage are real mechanisms rather than miniatures.

**Practical note:** at Re 161,000 the section's CLmax is nearer 1.1 than 1.4, so
the model will not fly at exact Froude weight. Build to 5 to 6 lb and fly at 18 to
22 mph. Dynamic frequencies come out slightly faster than scale, so it will feel
twitchier than the full-size. That is the conservative direction.

## What this model can validate

- Pitch stability and usable CG range
- Spiral and dutch roll tendency
- **Roll authority from dihedral plus spoilerons**, which is the single biggest
  open handling question on a two-axis aircraft
- Spoileron versus rudder control power balance
- Trim
- Wing joint concept, assembly, and fit

## What it cannot validate

- CLmax and stall speed
- **Slat effectiveness or geometry.** A slat re-energizes a turbulent boundary
  layer, and at Re 161,000 the boundary layer is largely laminar. Slat dimensions
  that work at 1.28 million read as pure drag on the model.
- L/D and drag numbers
- Stall behavior, which can reverse from root-first to tip-first at low Re
- Structural loads, since Froude scaling makes model loads nothing like full size

**Do not let the model talk you out of the slats, and do not let it size them.**

## Construction

Foamboard fuselage and tail. **Hot-wired XPS wing cores**, not foamboard, because
foamboard bends into a rough approximation of an airfoil and the point is to learn
how this specific section behaves.

## Power and cost

At 5.5 lb and 70 W/lb, level flight needs about 70W; a 400W system gives climb and
wind margin with 15 to 20 minutes per pack.

| | |
|---|---|
| XPS cores, foamboard, carbon tube spars | $140 |
| Balsa and ply for ribs, formers, hardpoints | $50 |
| Adhesives | $40 |
| 400-500W outrunner, 40-60A ESC, two 4S 4000mAh, props | $170 |
| Five servos and receiver | $80 |
| Gear, wheels, linkage, horns, hinges | $60 |
| Tape, paint, hardware | $70 |
| **Total** | **~$610** |

Add a transmitter and charger if not already owned.

## Instrumentation

Runs Junco: ESP32 with an IMU, pitot, and SD logging. That converts "the roll felt
sluggish from 200 ft away" into logged roll rate against stick position.

The model doubles as the Junco development airframe, where a crash costs $600.
