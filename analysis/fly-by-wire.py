#!/usr/bin/env python3
"""Fly-by-wire / servo-augmented controls on this airframe.
Four questions with numbers: (1) does it fit the weight, (2) can the pilot
overpower a hardover, (3) what does manual reversion actually feel like -
the back-drive friction problem, and (4) which surface, if any, has a
fail-safe that already covers a servo failure.
Geometry: elevator 45% of 30 ft^2 tail, rudder 50% of 15 ft^2 VT, twist grip
2.4:1 after a 45% horn balance, stick gearing 4.5 deg/in.
"""
import math

RHO = 0.002377
def q(mph): return 0.5*RHO*(mph*1.4667)**2

S_E, C_E = 30.0*0.45, 3.0*0.45        # elevator area, mean chord
S_R, C_R = 15.0*0.50, 1.5             # rudder
CH_D = 0.008                           # hinge moment coeff per deg
STICK_GEAR = math.radians(4.5)         # rad/in
HORN, WRIST_GEAR = 0.55, 2.4           # 45% horn balance, twist gearing

def hm(S, c, mph, defl): return CH_D*defl*q(mph)*S*c*12.0

print("=== 1. WEIGHT: DOES IT EVEN FIT ===")
print("  real servo weights: Garmin GSA 28 = 1.4 lb ($975 exp), Dynon SV32 = 2.17 lb.")
print("  Using the LIGHTEST available (GSA 28) - the most favourable case for the idea.")
rows = [("single-string 3-axis", 3*1.4, 1.0, 1.0, 3.0),
        ("dual-redundant (a PRIMARY control minimum)", 6*1.4, 2.0, 2.0, 5.0),
        ("triple-redundant (what real FBW ULs use)", 9*1.4, 3.0, 3.0, 7.0)]
print("  %-46s %7s %7s %7s %7s %8s" % ("architecture", "servos", "ctrl", "wiring", "batt", "TOTAL"))
tot = {}
for n, s, c, w, b in rows:
    t = s+c+w+b; tot[n] = t
    print("  %-46s %7.1f %7.1f %7.1f %7.1f %8.1f" % (n, s, c, w, b, t))

EMPTY_103, CAP_103 = 253.2, 254.0
EMPTY_EAB, GROSS = 275.7, 525.0
FUEL, PILOT_MAX = 30.0, 200.0
print(f"\n  103 kit: {CAP_103-EMPTY_103:.1f} lb of empty-weight margin.")
for n, t in tot.items():
    print(f"    {n:46s} needs {t:5.1f} -> OVER BY {t-(CAP_103-EMPTY_103):5.1f} lb")
print(f"\n  EAB: empty {EMPTY_EAB}, gross {GROSS:.0f}, max pilot {PILOT_MAX:.0f}, fuel {FUEL:.0f}")
for n, t in tot.items():
    allup = EMPTY_EAB + t + PILOT_MAX + FUEL
    print(f"    {n:46s} all-up {allup:6.1f} -> {'FITS' if allup <= GROSS else 'OVER'}"
          f" ({GROSS-allup:+.1f} lb)")
print("""
  Verdict: the 103 aircraft cannot carry ANY of it - over by an order of
  magnitude on a 0.8 lb margin. On the EAB, single-string fits easily and
  dual-redundant is right at the edge at max pilot; triple - what the real
  FBW ultralights actually use - is out. And the fit that matters is the
  wrong one: single-string is the architecture you must not use for a
  primary control, and it is the one with room to spare.

  The Part 103 weight-exclusion trap, which runs the WRONG WAY here:
  BlackFly is 313 lb empty and Helix 348, yet both operate under Part 103 -
  because 103.1(e)(1) excludes 'floats and safety devices intended for
  deployment in a potentially catastrophic situation'. Their ballistic
  chute and flotation are ~90+ lb of legally invisible hardware.
  Servos, flight computers, wiring and their batteries are NOT excluded.
  The loophole that makes FBW ultralights legal cannot be used to carry
  the FBW.""")

print("=== 1b. ELECTRICAL POWER - THE GATING ITEM NOBODY PLANS FOR ===")
SERVO_A, VOLTS = 2.03, 12.0           # Dynon SV42 moving at 100% torque
n_srv, hours = 3, 2.0
watts = n_srv*SERVO_A*VOLTS + 5.0
print(f"  {n_srv} servos moving under load ~{SERVO_A} A each + controller = ~{watts:.0f} W")
print(f"  over {hours:.0f} h = {watts*hours:.0f} Wh; at 150 Wh/kg usable that is "
      f"~{watts*hours/150*2.2:.1f} lb of cells before BMS, case, or a second one")
print("""  Many Part 103 engines (Hirth, Polini, Vittorazi class) have a very small
  alternator or none - often under 100 W, sometimes only enough for ignition.
  If the servos are load-bearing for control, the battery becomes FLIGHT
  CRITICAL: engine-out must not mean control-out, so it needs its own pack
  sized for full duration, and then a second pack because one is a single
  point of failure. This is why every FBW ultralight is an ELECTRIC aircraft
  - they already own a large, redundant, monitored battery system.
  VERIFY the chosen engine's actual charging surplus before anything else.""")

print("=== 2. HARDOVER: CAN THE PILOT WIN? ===")
print("  %-34s %8s %10s %12s" % ("surface / case", "defl", "HM in-lb", "pilot must"))
for label, mph in [("elevator, approach 35 mph", 35), ("elevator, cruise 50 mph", 50),
                   ("elevator, Vne 62 mph", 62)]:
    h = hm(S_E, C_E, mph, 25)
    print("  %-34s %7.0f%s %10.0f %9.1f lb" % (label, 25, chr(176), h, h*STICK_GEAR))
for label, mph in [("rudder, approach 35 mph", 35), ("rudder, Vne 62 mph", 62)]:
    h = hm(S_R, C_R, mph, 25)*HORN
    print("  %-34s %7.0f%s %10.0f %6.0f in-lb wrist" % (label, 25, chr(176), h, h/WRIST_GEAR))

f_vne = hm(S_E, C_E, 62, 25)*STICK_GEAR
LIMIT_LB = 15.0
d_ok = LIMIT_LB/(hm(S_E, C_E, 62, 1)*STICK_GEAR)
print(f"""
  Elevator: a full hardover is {f_vne:.0f} lb of stick at Vne - overpowerable,
  but not while the same hand is twisting for yaw. Standard fix is a slip
  clutch limiting servo authority: for override <= {LIMIT_LB:.0f} lb at Vne the servo
  may command at most ~{d_ok:.0f} deg of the 25 deg throw ({d_ok/25:.0%} authority).

  RUDDER IS THE REAL PROBLEM, and it is self-inflicted. A pedal rudder lets a
  pilot push back with a LEG (100+ lb available). The twist grip caps the
  override at a WRIST: ~10-15 in-lb sustained, ~50-90 in-lb brief maximum.
  A rudder hardover demands {hm(S_R,C_R,35,25)*HORN/WRIST_GEAR:.0f} in-lb held at approach speed and
  {hm(S_R,C_R,62,25)*HORN/WRIST_GEAR:.0f} in-lb at Vne - at or past sustainable wrist capability, in
  the phase of flight with the least altitude to spare.""")

print("=== 3. MANUAL REVERSION: THE BACK-DRIVE PROBLEM ===")
NORMAL_WRIST, PEAK_WRIST = 9.0, 19.0
print(f"""  'Cut power and fly it manually' is the right instinct, and it is where
  the scheme dies on this particular aircraft.

  A slip clutch must sit ABOVE the largest normal aerodynamic load (or it
  slips in normal flight) and BELOW pilot override (or the pilot cannot win).
  On the twist grip that band is {NORMAL_WRIST:.0f} to {PEAK_WRIST:.0f} in-lb at the wrist - a
  {PEAK_WRIST-NORMAL_WRIST:.0f} in-lb window. Set the clutch mid-band at ~{(NORMAL_WRIST+PEAK_WRIST)/2:.0f} in-lb and, with the
  power off, the pilot back-drives the gearbox through that clutch on EVERY
  input: ~{(NORMAL_WRIST+PEAK_WRIST)/2:.0f} in-lb of dead friction against a {NORMAL_WRIST:.0f} in-lb comfortable budget.

  Manual reversion would be HEAVIER THAN THE UNASSISTED AIRCRAFT.

  And the controls trade already identified breakout friction as the one
  thing that must not creep into this circuit - it is why the gap-seal note
  makes a teflon chafe strip mandatory. A geared servo is the largest
  possible source of exactly that.

  CORRECTION, from the sourced pass: the 'true de-clutch' escape is not
  hypothetical. The Garmin GSA 28 uses a SOLENOID ENGAGEMENT CLUTCH that
  decouples the motor from the control when unpowered - Garmin's stated
  purpose is 'virtually no control system friction with the autopilot turned
  off', and they deleted the shear pin entirely. 1.4 lb, $975 experimental.
  Dynon / Trio / TruTrak instead use a PERMANENTLY COUPLED slip clutch.

  So the architecture rule is sharp: an engagement-clutch servo is mandatory
  here and slip-clutch servos are DISQUALIFIED - because the friction penalty
  is roughly fixed in in-lb while this aircraft's control forces are unusually
  small, so the RATIO is the worst of any airframe these products target.
  A builder calls Dynon friction 'low enough in percentage compared to the
  control forces' on an RV-12 - an aircraft with several times the stick force
  of this one.""")

print("=== 3b. WHAT A 3-SECOND RECOGNITION DELAY COSTS AT 50 MPH ===")
for delay, phase in [(3.0, "cruise/climb/descent (Part 23 practice)"),
                     (1.0, "low approach (Part 23 practice)")]:
    print(f"  {delay:.0f} s at 50 mph = {50*1.4667*delay:.0f} ft of travel   [{phase}]")
print("""  Operating rules (121.579 / 135.93) require autopilot use no lower than
  TWICE the AFM altitude loss for a malfunction. Ultralight pattern work
  happens at 500-800 ft AGL. A hardover plus a 3 s delay plus a 2x factor
  plausibly consumes more altitude than this aircraft ever has beneath it:
  by the certification world's own arithmetic, a servo with meaningful
  authority has NO legal operating altitude band in a Part 103 mission.""")

print("=== 4. THE ONE SURFACE WHERE A SERVO IS ALREADY FAIL-SAFE ===")
print("""  Design-log SS9: the spoilerons are single-acting, tension-only, SPRING
  RETURN TO CLOSED - 'airflow and spring both push them shut, so a broken or
  disconnected cable retracts rather than floats,' because 'a stuck-open
  spoiler is the one control failure with no good answer.'

  That physics does not care whether the tension came from a cable or a
  servo. Kill power to a spoileron servo and the surface closes itself.
  A spoileron hardover is also the mildest hardover available here: one wing
  drops slowly, and the rudder - the primary roll control - overpowers it.

  Elevator and rudder have no such property. A hardover there holds the
  surface deflected AGAINST spring and airflow, which is precisely the
  failure mode SS9 refused to accept on the spoilerons.

  Conclusion: the spoileron servo provision already in the plan (SS21, Junco
  wing-leveling) is not a smaller version of fly-by-wire. It is the ONLY
  place on this airframe where the existing fail-safe covers a servo, and
  that is why it is the one that should exist.""")

print("=== 5. WHAT THE FORCES ACTUALLY ARE (is there a problem to solve?) ===")
print("  %-30s %12s" % ("control", "steady force"))
print("  %-30s %12s" % ("elevator, cruise trimmed", "2.6 lb"))
print("  %-30s %12s" % ("rudder, cruise (twist)", "~9 in-lb"))
print("""  Neither is a strength problem; both are ENDURANCE problems, and the fix
  already identified is a 0.4 lb spring trim plus a horn-balanced rudder.
  Servos would be solving a problem that 0.4 lb of spring already solves.""")
