#!/usr/bin/env python3
"""Landing gear design: grass field, easy entry for a 6'0" pilot, strong and
forgiving. Fleet max gross 525 lb, loaded CG sta 63 (30% MAC), datum = prop
plane. Outputs the geometry that goes into geometry-mesh.py and the drawings.
"""
import math

GROSS = 525.0          # fleet max, lb
CG_STA = 63.0          # in
CG_H = 27.0            # in AGL, low-slung stance (belly 16 in)
SINK = 8.0             # fps design sink - "forgiving": FAR-23-ish is ~7
N_GEAR = 3.0           # gear reaction factor at limit
ETA = 0.60             # energy efficiency of tube-spring + tire

print("=== STANCE (drives entry and everything else) ===")
BELLY = 16.0
SEAT_PAN = BELLY + 4.0
print(f"  belly at cockpit {BELLY:.0f} in AGL -> seat pan ~{SEAT_PAN:.0f} in = kitchen-chair height")
print(f"  step-over sill ~{BELLY+10:.0f} in (bathtub wall); grab the cabane strut")
print(f"  seated head top (6'0\" pilot) ~ {SEAT_PAN+36:.0f} in -> wing underside at 64 in clears by ~{64-(SEAT_PAN+36):.0f} in")
print(f"  thrustline 40 in AGL -> 60 in prop static tip clearance {40-30:.0f} in")
print(f"    worst case (full gear stroke 4.5 + flat tire 3): {40-30-7.5:.1f} in  - positive, per the flat-tire rule")

print("\n=== ENERGY AND STROKE (the 'forgiving' requirement) ===")
v = SINK
E = 0.5*(GROSS/32.2)*v*v
print(f"  {GROSS:.0f} lb at {SINK:.0f} fps: {E:.0f} ft-lb to absorb (lift carries weight during stroke)")
s_tot = v*v/(2*32.2*ETA*N_GEAR)*12
print(f"  total stroke at N={N_GEAR:.1f}, eta={ETA}: {s_tot:.1f} in")
print(f"  budget: soft tire at 8 psi ~2.0 in + sprung leg ~{s_tot-2:.1f} in vertical at the axle")
print(f"  loads: total reaction {N_GEAR*GROSS:.0f} lb limit; per main (2-point) {N_GEAR*GROSS/2:.0f} lb;")
print(f"         ultimate {1.5*N_GEAR*GROSS/2:.0f} lb per leg. Size the leg, its fitting, AND the")
print(f"         longeron cluster it feeds - the cluster is where gear failures actually start.")

print("\n=== GEOMETRY ===")
MAIN_STA = 70.5
NOSE_STA = 32.0
TRACK = 56.0
wb = MAIN_STA - NOSE_STA
aft = MAIN_STA - CG_STA
print(f"  mains sta {MAIN_STA} = {aft/50*100:.0f}% MAC aft of CG (target band 12-16%)")
print(f"  nose sta {NOSE_STA}, wheelbase {wb:.1f} in, track {TRACK:.0f} in")
print(f"  static nose load: {(aft)/(wb)*100:.0f}% (target 15-20%)")
tip_back = math.degrees(math.atan(aft/CG_H))
print(f"  tip-back angle atan({aft:.1f}/{CG_H:.0f}) = {tip_back:.1f} deg (want >=15)")
# overturn angle: CG height vs perpendicular distance to nose-main ground line
half_t = TRACK/2
theta = math.atan(half_t/wb)
d = (CG_STA-NOSE_STA)*math.sin(theta)
ot = math.degrees(math.atan(CG_H/d))
print(f"  overturn angle {ot:.1f} deg (want < 60; lower is better on grass with crosswind)")
tail_h = 27.0; tail_sta = 184.0
ts = math.degrees(math.atan(tail_h/(tail_sta-MAIN_STA)))
print(f"  tail-strike attitude atan({tail_h:.0f}/{tail_sta-MAIN_STA:.0f}) = {ts:.1f} deg")
print(f"    normal touchdown is 8-12 deg; a full-stall (19 deg with slats) WILL touch the")
print(f"    boom first - protect it with a small steel skid at the tail post, ~0.3 lb")

print("\n=== WHEELS AND TIRES ===")
print("  mains: 13x5.00-6 at 8-10 psi on 6 in rims - the low pressure IS the damping;")
print("         a tube-spring leg has almost none, and rebound is what causes bounce")
print("  nose:  4.10/3.50-6, castoring +/-60 with steering stops per open questions,")
print("         rubber-disc or bungee springing - the nose leg sees the ruts first")
print("  EAB kit option: 16x6.5 low-pressure tires on the same 6 in rims (+3-4 lb,")
print("         kit item, never on the 103 aircraft - the 0.8 lb margin cannot afford it)")

print("\n=== LEG SIZING START POINT (gate-4 detail, not final) ===")
P = 1.5*N_GEAR*GROSS/2   # ultimate per leg
arm = 18.0               # bending arm, in (leg sweep)
M = P*arm
for od, w in ((1.5,0.120),(1.625,0.120),(1.75,0.120)):
    i_d = od-2*w
    I = math.pi/64*(od**4-i_d**4)
    S = I/(od/2)
    print(f"  {od:.3f} x {w:.3f} 4130: sigma_ult = {M/S/1000:.0f} ksi "
          f"({'needs heat treat to ~180 ksi' if M/S/1000>90 else 'normalized ok'})")
print("  -> 1.625-1.75 x .120, heat-treated after welding, or increase sweep to cut the arm.")
print("  Deflection check comes with the real leg curve in gate 4.")
