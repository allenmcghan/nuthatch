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
print("  aviation-grade autopilot servo ~2.0-3.0 lb installed (GSA 28 / Trio class)")
rows = [("single-string 3-axis", 3*2.5, 1.5, 1.5, 2.0),
        ("dual-redundant (what a PRIMARY control needs)", 6*2.5, 3.0, 3.0, 4.0)]
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
  Verdict: the 103 aircraft cannot carry ANY of this - it is over by more
  than an order of magnitude on a 0.8 lb margin. The EAB fits a SINGLE-STRING
  system and cannot fit a redundant one at max pilot. That is the whole
  problem in one line: the only architecture that fits is the only
  architecture you must not use for a primary control.""")

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

  The escape is a true de-clutch (electromagnetic, fully disengaging on
  power loss) - which works, costs weight, and introduces its own single
  point of failure: a clutch that fails to release leaves a jammed control.""")

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
