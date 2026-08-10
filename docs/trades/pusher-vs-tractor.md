# Trade: Pusher vs Tractor

**Question asked:** is a pusher propeller more efficient, and should Nuthatch be
one?

**Answer:** efficiency is a wash — somewhere between zero and five percent in the
pusher's favour, which is inside the error bar on the drag estimate the number is
built from. **Efficiency is not a reason to switch.** The reasons to consider a
pusher are noise, ground safety, and visibility. The reasons not to are the
unblown tail, debris ingestion, and balance.

The balance finding is the one that matters, and it is not what you would expect:
**a gasoline pusher is a different airframe, an electric pusher is a
modification.** That asymmetry is the most useful thing in this document.

Status: analysis only. **Nothing in the design has been changed.** The baseline
remains a nose-mounted tractor with the Hirth F-33.

---

## 1. The efficiency question

Both configurations move the same air with the same disc. The difference is what
the slipstream touches on its way past, and what the disc has to breathe.

### What a tractor loses: slipstream scrubbing

A tractor blows accelerated air over everything behind it. At 50 mph cruise the
numbers on this airframe are:

| | |
|---|---|
| Thrust required | 53 lb (238 N) |
| Induced velocity at the disc | 2.17 m/s |
| Velocity ratio at the disc | 1.10, so q ratio 1.20 |
| Velocity ratio mid-fuselage | 1.14, so **q ratio 1.29** |
| Velocity ratio far field | 1.19, so q ratio 1.43 |

Drag on wetted area inside that tube goes up with the q ratio. The open cockpit
is what makes this bite: the pilot is a large fraction of the flat-plate area on
an aircraft like this, and on a tractor the pilot sits directly in the slipstream
along with the forward fuselage, the wing root, and the entire tail.

| Fraction of flat-plate area in the slipstream | Parasite penalty | Share of cruise power |
|---|---|---|
| 40% | +12% | **+7.8%** |
| 55% | +16% | **+10.7%** |

So the tractor is giving away roughly **8 to 11 percent of cruise power** to
scrubbing. That is a bigger number than the 2–5% usually quoted for light
aircraft, and the reason is specific to this design: Nuthatch is
parasite-dominated (parasite is about two thirds of cruise power at 50 mph) and
the slipstream covers an unusually large share of the wetted area.

### What a pusher pays back

The pusher recovers that scrubbing loss, then spends it in three places:

| Penalty | Cost |
|---|---|
| Prop efficiency 0.75 → 0.72, wing and pylon wake inflow | **+4.2%** shaft power |
| Prop efficiency 0.75 → 0.70, heavy distortion | +7.1% shaft power |
| Pylon: ~5 ft² wetted plus interference, ≈ +0.020 m² of f | **+3.9%** parasite |

A pusher's disc runs in the wake of whatever it sits behind. The inflow is
non-uniform, so each blade sees a varying angle of attack once per revolution.
That costs propulsive efficiency, and it is also the reason pushers are
characteristically noisier — blade-wake interaction is a tonal noise source that a
tractor in clean air does not have. That is worth flagging against design-log §16,
where noise is treated as a first-class objective.

### Net

**Roughly 0 to +5% for the pusher at cruise.** The equivalent flat plate area
`f = 0.45 m²` this is all built on was back-solved from the Sky Pup's published
12:1 glide, so it carries an uncertainty comfortably wider than 5%. The honest
conclusion is that the two configurations are indistinguishable on cruise
efficiency at this level of analysis, and anyone claiming otherwise for an
aircraft in this class is reading their own noise.

### Where the pusher clearly loses, and it is not efficiency

**The tail is not blown.** A tractor's empennage sits in accelerated flow, so
elevator and rudder authority at low airspeed and high power is far better than
freestream would give. On Nuthatch this is not a minor comfort item: **the rudder
is doing the rolling.** Losing slipstream over the tail costs authority precisely
at rotation, in the go-around, and in the low-and-slow regime the aircraft exists
for. On a two-axis aircraft this is the strongest single argument against a
pusher, and it does not appear in any efficiency calculation.

**The wing is not blown.** The tractor gets extra dynamic pressure over the
inboard wing at low speed, which is lift during the takeoff roll. Small — a few
percent of ground roll — but it points the same direction against the 140 ft
target.

**Debris.** A nosewheel on grass throws stones and turf rearward into a pusher
disc. The stated mission is a 300 × 1000 ft grass backyard. This is the classic
way pusher installations eat propellers, and it argues for a metal-leading-edge
or composite prop rather than the carved wood of §16.

**Cooling is manageable, not free.** The Hirth F-33 is free-air cooled via
propeller slipstream (§15). A pusher engine sits *ahead* of the disc and is drawn
through rather than blown over, at roughly V+v instead of V+1.5v, and in the
fuselage wake with poor pressure recovery. Plenty of free-air two-strokes run as
pushers — Quicksilver and Challenger both do — so this is a design-attention item
needing a proper plenum and baffling, not a blocker.

### Where the pusher wins

- Prop is behind the pilot, not in front. No disc between the occupant and the
  crash structure, and nobody walks into it at the front of the aircraft.
- No exhaust, oil mist, or engine noise directly upstream of an open cockpit.
- Unobstructed forward visibility, which matters for a 300 ft-wide strip with
  trees at one end.

---

## 2. The balance finding

This is where the analysis stops being a wash and starts being decisive.

Datum is the prop plane, wing LE at station 48, chord 50 in, target CG 30% MAC.

### Gasoline pusher: does not close

The gas power group — engine 35 lb, redrive 10 lb, mount 5 lb — has to move aft
**as a unit**, because the engine must be at the propeller.

| | Empty CG | Wing LE must move to | Wing TE | Disc LE vs wing TE | Tail arm |
|---|---|---|---|---|---|
| Tractor baseline | sta 66.5 | 48 | 98 | — | 121 in |
| Pusher, disc at sta 118 | **sta 85.4** | **60.4** | 110.4 | **−22.4 in** | 109 in (−10%) |

Moving 58 lb aft by roughly 95 in shifts the empty CG aft **19 inches**. To
rebalance, the wing has to move 12 in aft — which drives the trailing edge into
the space the propeller disc needs. The disc and the wing want the same volume.
Push the prop further aft to make room and the CG moves aft again, and the tail
arm keeps shrinking, so the tail has to grow, which adds more aft weight. It is a
divergent loop.

**A gasoline pusher is not a modification of this fuselage. It is a different
aircraft** — specifically the Quicksilver/Challenger/Minifox layout, with the
pilot moved well forward of the wing leading edge rather than under it. That is a
new fuselage, a new cabane, new gear geometry, and a new tail. It is not 100 hours
and $1,900.

### Electric pusher: closes

Electric breaks the loop, and the reason is worth stating plainly:

> **An electric drivetrain decouples the mass of the powerplant from the location
> of the thrust.** Only the motor has to be at the propeller. The pack, the
> controller, and the HV gear can go wherever balance wants them.

Of a ~68 lb electric drive group, only about 38 lb (motor, prop, mount, pylon) is
forced aft. The controller and HV gear stay in the cabin bay, and the pack — the
single heaviest item — becomes a **balance tool** rather than a balance problem.

With the prop on a pylon at station 150 (about 32 in aft of the wing TE) and the
pack on the carry-through:

| Pilot station | Loaded CG | Wing LE | Disc clearance aft of TE |
|---|---|---|---|
| 58 (unchanged) | 72.5 | 57.5 | +12.5 in ✓ |
| 46 | 69.0 | 54.0 | +16.0 in ✓ |
| 38 | 66.6 | 51.6 | +18.4 in ✓ |

It converges at the existing seat station, and moving the pilot forward relaxes it
further. Cost is the wing moving ~9 in aft, a pylon or boom extension, and a tail
arm down about 8%.

**A fixed pack is also better for CG travel than fuel.** Fuel burns off in flight
and moves the CG; a pack does not. Across a 130–220 lb pilot range the loaded CG
stays inside 29–31% MAC with no ballast.

---

## 3. Why the e-Minifox gets 20 minutes and the Part 103 sketch got four

This is the question that prompted the trade, and the answer is entirely
regulatory. **It is the rule, not the airplane.**

| | FAR Part 103 | French ULM classe 3, monoplace |
|---|---|---|
| What is capped | **254 lb empty**, batteries included | **330 kg (728 lb) gross**, +15 kg with a parachute |
| Empty weight limit | 254 lb | **none** |
| Implied allowable empty | 254 lb | 330 − 86 kg std pilot = 244 kg = **538 lb** |

A Minifox-class ULM may be **284 lb heavier empty** than anything Part 103 will
allow. That is the whole gap.

The Part 103 electric sketch runs out of weight before it runs out of anything
else. The 103 airframe less propulsion is 206 lb; a 15 kW direct-drive electric
group adds about 40 lb; that is **246 lb before a single cell**, leaving 8 lb of
pack budget against the 254 lb cap.

| Allowed empty | Cells | Pack | Endurance at 50 mph |
|---|---|---|---|
| 254 lb (Part 103 cap) | 8 lb | 0.62 kWh | **4 min** |
| 300 lb | 54 lb | 4.2 kWh | 27 min |
| 350 lb | 104 lb | 8.0 kWh | 50 min |
| 400 lb | 154 lb | 11.9 kWh | 69 min |

The four-minute figure is an artifact of one number in one regulation. Relax the
empty weight by 46 lb and it becomes 27 minutes.

### Head to head on the same pack

The e-Minifox is reported as a ~35 kW motor on a **~5 kWh pack** on the Eurofly
Minifox airframe. Giving Nuthatch the same 5 kWh (about 65 lb at 170 Wh/kg pack
level):

| | L/D | Gross | 45 mph | 50 mph | 55 mph |
|---|---|---|---|---|---|
| **Nuthatch EAB electric** | **10.7** | 533 lb | 36 min | **30 min** | 25 min |
| Minifox-class ULM (est.) | 7.9 | 545 lb | 25 min | **20 min** | 17 min |

*Usable energy taken as 90% depth of discharge × 88%, holding 12% back for taxi,
climb, and a go-around.*

**Nuthatch is not behind. On the same pack it is roughly 50% ahead**, and the
reason is the thing the project already decided to spend weight on: a cantilever
wing at L/D 10.7 against a strut-braced tube-and-fabric ULM at about 8. Every
point of L/D is endurance you do not have to buy in cells.

The Minifox comparison is worth keeping for the noise result, though — FlyingOhm
report 57 dB at 500 ft against 65 dB for the two-stroke. That is the *motor*
being quiet, not the pusher, and it is consistent with §16's conclusion that tip
speed and power source dominate the noise budget.

---

## 4. Conclusions

1. **Efficiency does not justify a pusher.** Net 0 to +5% at cruise, inside the
   uncertainty of the drag model. Do not switch for efficiency.
2. **The two-axis configuration argues against a pusher** more strongly than
   anything else here. The rudder is the roll control, and an unblown tail loses
   authority exactly where the mission needs it. This deserves its own answer
   before a pusher is considered seriously.
3. **A gasoline pusher is off the table** as a modification. It does not close on
   balance — it needs a different fuselage with the pilot forward of the wing.
4. **An electric pusher closes** and is the natural configuration if the aircraft
   ever goes electric, because electric decouples powerplant mass from thrust
   location. If a pusher is wanted, it arrives with the electric conversion, not
   before.
5. **The Part 103 electric configuration is not viable** and should not be
   pursued. Part 103 stays gasoline. Electric is an EAB-only path.
6. **Nuthatch is a better electric airframe than the aircraft it was being
   compared against**, by about 50% on the same pack. The glide ratio the project
   already bought is what pays for it.

## 4a. Follow-up: "just move the engine up" and the remote belt drive

Two refinements proposed after the amphibious discussion — mount the whole
engine on a pylon the way ultralight pushers do, or leave the engine low and
run a long belt up to a pusher prop shaft. Both are real techniques; neither
survives this airframe's invariants.

**Why the pylon works for Quicksilvers and Aventuras but not here.** Those
aircraft hang the engine at the wing with the prop just behind the trailing
edge — and balance, because their **pilot sits well forward of the wing as
the counterweight**. The Nuthatch deliberately does the opposite: the pilot
sits *at* the CG. That placement is not a styling choice — it is the fleet
plan's load-bearing invariant, the reason a 105 lb pilot and a 170 lb pilot
fly the same airplane with nothing but an 8 lb ballast placard. Pilot-at-CG
means the pilot cannot be the counterweight for anything; the engine at the
nose is what balances the boom and tail. The arithmetic with no forward
pilot: a pusher prop must clear the wing TE (sta 98), putting the 58 lb
power group at ~sta 99 — 36 in aft of the CG. Countering 58 × 36 ≈ 2,100
in-lb from the nose (~55 in arm) takes **~38 lb of permanent nose ballast**
on an airframe with a 0.8 lb margin. The alternative — move the wing aft —
drags the TE, and therefore the prop and engine, aft with it: the divergence
§1 already documented ("chasing it aft shrinks the tail arm and grows the
tail"). The pylon doesn't escape the trade; it *is* the trade.

**The remote belt drive attacks the right problem and picks up a worse one.**
Engine low in the CG bay, belt up and aft to a prop shaft behind the wing:
the mass problem genuinely dissolves — this is the gas-powered version of
what electric does for free. What it costs:

- **Center distance ~45–60 in** (CG bay to a shaft above the TE), against
  the 6–10 in of every proven ultralight belt redrive (including the F-33's
  own). Long spans need idlers and a tensioner; belt flap on a 4–5 ft run
  is its own aeroelastic problem.
- **Two-stroke torque pulses through a long compliant drive** is the
  BD-5's disease: torsional resonance between engine pulses, belt
  compliance, and prop inertia. Solvable with a tuned cush drive and a
  development program; fatal to a 750-hour wood airplane that must not
  carry a development program in its propulsion.
- The run crosses **flexing wood structure** (fuselage to pylon/wing);
  belt alignment across a joint that moves is a maintenance item forever.
- **+12–18 lb** of shaft, bearings, pylon, idlers, and guards — EAB-only
  on weight, before any of the above is solved.

**And the unblown tail stands regardless of how the mass is solved.** The
rudder is the roll control, and it flies in prop wash today. Every pusher
variant — pylon, belt, or electric — removes that wash at rotation and
low speed, and §5's gating question (adequate roll authority unblown, a
full-scale power-on question) applies to all of them equally.

**Net:** for gasoline, the pylon and the belt are both ways to spend weight
and risk arriving at the same two unsolved problems (balance-or-ballast, and
the unblown tail). The clean pusher path remains the electric conversion on
the EAB — motor light enough to need no counterweight, batteries on the CG
tray the airframe already carries — with the unblown-tail question as its
gate.

## 4b. Follow-up: the high tractor — keep it a tractor, lift the whole engine

The third variant: engine stays in front of the wing, still a tractor, but
raised on a mast so the prop clears water spray. This one has real
precedent — the PBY Catalina, the Grumman Goose, and the AirCam are all
high-thrustline tractors — and it fixes the two problems the other variants
couldn't: **the mast can sit at the nose station, so balance is preserved**
(no 38 lb ballast), and a prop at z ≈ 75 puts the tips ~40 in above the
waterline, which combined with height over the float bows starts to look
like real seaplane geometry.

**What kills it is the thrust line itself.** Thrust acts where the prop is;
raising the prop raises the thrust line above the CG, and every power change
becomes a pitch moment the tail must cancel. The arithmetic at 180 lb of
takeoff thrust:

| Thrustline | Offset above CG (z 27) | Power pitch moment | Tail ΔCL needed at 30 mph | Elevator |
|---|---|---|---|---|
| 40 in (today) | 13 in | 2,340 in-lb | 0.28 | ~8° — inside the trim analysis |
| 60 in | 33 in | 5,940 in-lb | 0.72 | **~21° of the ±25° throw** |
| 75 in (spray-clear) | 48 in | 8,640 in-lb | **1.05** | **~30° — MORE than the tail has** |

At rotation speed, the spray-clearing thrustline demands more than the
tail's entire authority just to hold the nose against full power — before
rotating, before flaring, before gusts. Even the modest 60 in raise leaves
4° of elevator for everything else. The big flying boats live with this by
carrying proportionally larger tails, higher speeds (q rescues the tail),
and three-axis controls; the Aventura's known power-pitch coupling is the
same physics accepted as a handling signature. A two-axis aircraft whose
flare already uses all but 5.7° of elevator has no room to accept it.

Secondary costs, each real: the horizontal tail leaves the prop wash (the
blown-tail rudder-roll advantage §1 credits to the tractor is partially
forfeited), the mast is +8–12 lb of structure and an engine-vibration
fatigue problem (EAB-only on weight), and a 58 lb engine on a mast above
the forward cockpit is a crash-path regression from the rev D layout, which
deliberately keeps the engine ahead of the crush bay.

**There is no "just high enough."** The minimum raise is set by *where* the
disc sits over the floats, not by a generic spray number. Properly sized
floats put their bows ~16 in forward of the prop plane
([amphibious.md §5](amphibious.md)), so the disc hangs over the **bow root**
— the single wettest station on the rig, where the bow blister originates
and where plow-phase green water rides 12–18 in above the static waterline.
The Cub-style "30 in of clearance is plenty" rule applies five feet *aft* of
the bows over clean water between the floats; over the bows, light-chop
sanity wants tips 36–48 in up, which is thrustline 66–78 — the
exceeds-the-tail case above. A modest raise (46–50 in) buys the worst of
both: still inside the bow fan, *and* deep into the pitch budget.

And the pitch budget has a water-specific corner that closes early: the
**skip/bounce recovery**, which combines full power with flare-level
elevator as routine seaplane technique, not an emergency. Flare alone uses
−19.3° of the −25° throw (power off). Full power at 35 mph adds +6.0° of
demand at today's 13 in offset — a combination land operations never visit
(ground flares happen at idle) but water operations visit weekly. At a
46 in thrustline the combination needs 28°; at 50 in, 30°; the throw is 25.
Every inch of raise deepens a corner that water flying makes routine.

**Net:** the high tractor is the best gasoline water idea yet — it genuinely
solves balance and spray — and it fails on a third, harder wall: at this
aircraft's speeds and tail size, thrust that high overpowers the elevator,
and the raises small enough to spare the elevator are too small to leave
the bow spray.
The pattern across 4a and 4b is now clear: gasoline's 58 lb can sit low and
forward (balanced, spray-doomed), aft (spray-clear, balance-doomed), or high
(both solved, pitch-doomed). The mass has nowhere legal to go — which is
the original §1 conclusion, reached from the third direction. Electric up
high shares the pitch-coupling physics but at 12 lb of motor the *installation*
problems (mast structure, crash path, vibration) shrink to manageable, and
the thrust offset becomes a design variable (smaller disc, lower pylon)
instead of a fixed consequence of hauling an engine into the air.

## 5. What this does not settle

- Whether the tail can be sized to give adequate roll authority unblown. This is
  the gating question for any pusher, and the quarter-scale model cannot answer
  it (unpowered-tail effects are a full-scale power-on question).
- The design-log §3 cost basis of **$500/kWh** for battery capital cost. That
  figure decides the electric argument and has not been re-verified against
  current DIY 21700 pack costs. It should be, before §3 is cited again.
- Pack-level 170 Wh/kg is an assumption, not a quote. Real builds land anywhere
  from 140 to 200 depending on how much box and BMS the design carries.
- Prop material. A pusher on grass wants a metal leading edge or composite, which
  conflicts with the carved wood prop of §16.

---

*Calculations in this document use the same drag model as
`analysis/weight-cost-hours.xlsx` (Performance sheet): b = 31 ft, S = 130 ft²,
f = 0.45 m² clean and 0.519 m² with slats, e = 0.85, prop efficiency 0.75,
motor + controller efficiency 0.90.*
