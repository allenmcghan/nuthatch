#!/usr/bin/env python3
"""Can a wrist run the rudder? Hinge moments for the twist-grip control
scheme (owner decision: stick twist = rudder, stick lateral = spoilerons,
left-hand lever = symmetric spoilers, rudder pedals deleted).
VT 15 ft^2 (36 in chord x 60 in), rudder 50% chord -> 7.5 ft^2, c_r 1.5 ft.
"""
import math

S_R, C_R = 7.5, 1.5                # rudder area ft^2, mean chord ft
CH_D = 0.008                        # hinge moment coeff per deg, plain unbalanced
BAL = 0.45                          # horn/aero balance knockdown (REQUIRED, see doc)
GEAR = 60.0/25.0                    # wrist +/-60 deg to rudder +/-25 deg

def q(mph): return 0.5*0.002377*(mph*1.4667)**2

print("=== RUDDER HINGE MOMENT -> WRIST TORQUE (in-lb) ===")
print("  balance knockdown %.0f%%, gearing %.1f:1 (wrist 60 deg = rudder 25 deg)" % (BAL*100, GEAR))
print("  %-28s %8s %10s %10s" % ("case", "HM raw", "balanced", "at wrist"))
for label, mph, defl in [
    ("taxi/prop-wash steer 15", 15, 25),
    ("rotation 28, full", 28, 25),
    ("crosswind decrab 35, 12 deg", 35, 12),
    ("crosswind decrab 35, full", 35, 25),
    ("cruise 50, 10 deg", 50, 10),
    ("Vne 62, 8 deg", 62, 8),
]:
    hm = CH_D*defl*q(mph)*S_R*C_R*12.0
    print("  %-28s %8.0f %10.0f %10.1f" % (label, hm, hm*(1-BAL), hm*(1-BAL)/GEAR))

print("""
Human wrist (pronation/supination, power grip, published ergonomics ranges):
  sustained comfortable ~10-15 in-lb; brief maximum ~50-90 in-lb.
Verdict: the scheme closes ONLY with both the aerodynamic balance and the
gearing. Unbalanced + ungeared full rudder at 35 mph is ~85 in-lb - at the
edge of maximum wrist effort. Balanced and geared, the routine crosswind case
is ~8-9 in-lb sustained and full deflection ~19-20: acceptable.
""")

# ledger: pedals + cables out, twist mechanism + return spring in
print("=== WEIGHT ===")
print("  pedals + cables out: -4.5 lb (weight-scrub line)")
print("  twist grip, torque tube stub, centering spring, cable run in: ~+2.5 lb")
print("  net ~-2 lb, held as margin (unbanked) until the mechanism is weighed")
