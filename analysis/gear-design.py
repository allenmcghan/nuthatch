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

print("\n=== GEOMETRY (rev D: raked nose leg, wheel just aft of the prop) ===")
MAIN_STA = 70.5
NOSE_STA = 15.0        # was 32.0 (rev B/C vertical leg) - see raked-gear section below
TRACK = 56.0
wb = MAIN_STA - NOSE_STA
aft = MAIN_STA - CG_STA
print(f"  mains sta {MAIN_STA} = {aft/50*100:.0f}% MAC aft of CG (target band 12-16%)")
print(f"  nose sta {NOSE_STA}, wheelbase {wb:.1f} in, track {TRACK:.0f} in")
print(f"  static nose load: {(aft)/(wb)*100:.0f}% (castoring-nosewheel band 8-15%)")
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
print("  mains: 29x2.4 MTB alloy/carbon wheelsets, boost 12x148 hubs, 6-bolt disc,")
print("         tubeless + CushCore at 22-28 psi (rev C decision, unchanged)")
print("  nose:  20x2.4 BMX/junior-MTB wheel (rev D) - same bike parts bin as the mains,")
print("         castoring +/-60 with steering stops, castor trail + friction damper")
print("         REQUIRED (shimmy risk on a light castoring bike wheel is real)")
print("  EAB kit option: wider 29x2.8 tires on the same rims (+1-2 lb, kit item,")
print("         never on the 103 aircraft - the 0.8 lb margin cannot afford it)")

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

print("\n=== RAKED NOSE LEG (rev D): wheel just aft of the prop ===")
# 20x2.4 BMX wheel: R = 10 in. Axle at sta 15, z=10 -> tire front face at sta 5.
NOSE_R = 10.0
NOSE_Z = NOSE_R
gap = (NOSE_STA - NOSE_R) - 2.0   # prop plane occupies sta 0-2
print(f"  20x2.4 BMX/junior-MTB nosewheel, R={NOSE_R:.0f} in; axle sta {NOSE_STA:.0f}, z={NOSE_Z:.0f}")
print(f"  tire front face sta {NOSE_STA-NOSE_R:.0f} -> {gap:.1f} in axial gap behind the prop disc")
print(f"  (an axle at sta 10 would put the tire front AT sta 0, inside the prop plane - no)")
old_sta = 32.0
for name, sta in (("rev C vertical leg", old_sta), ("rev D raked leg", NOSE_STA)):
    wb_i = MAIN_STA - sta
    nl = aft/wb_i*100
    # nose-over prop protection: rotation about the nose axle before a 60-in
    # prop (tip bottom z=10 at sta 0-2) reaches the ground
    prot = math.degrees(math.atan(NOSE_Z/(sta-1.0))) if sta > 1 else 90.0
    print(f"  {name}: wheelbase {wb_i:.1f}, nose load {nl:.1f}%, "
          f"nose-over prop-protection angle {prot:.1f} deg")
print(f"  -> protection angle roughly DOUBLES (17.9 -> 35.5 deg); nose load {aft/wb*100:.1f}%")
print(f"     sits in the 8-15% castoring-nosewheel band (was 19% - slightly heavy)")
brake = math.degrees(math.atan((CG_STA-NOSE_STA)/CG_H))
print(f"  braking pitch-over margin atan({CG_STA-NOSE_STA:.0f}/{CG_H:.0f}) = {brake:.1f} deg - huge")
print(f"  flat-nose-tire prop clearance: tip bottom z=10 minus ~3 in tire collapse")
print(f"     -> ~7 in remaining (rev C vertical leg had ~4.6) - better")
print("  leg: triangulated bay, main raked member (30,0,17)->(15,0,10) at ~63 deg rake,")
print("       near-axial to the rut-strike resultant (the genuine structural win);")
print("       second member (14,0,30)->(15.5,0,10.5) closes the triangle.")
print("       The triangle doubles as ~15 in of crush structure ahead of the")
print("       pilot's feet - progressive collapse before the cockpit sees the load.")
Pn = aft/wb*GROSS          # static nose reaction
Pb = 0.35*GROSS*CG_H/wb    # braking weight transfer at ~0.35 g
print(f"  nose gear limit load ~ static {Pn:.0f} lb + braking transfer {Pb:.0f} lb = {Pn+Pb:.0f} lb")
print("  members ~1.0 x .049 4130 carry that with margin (gate-4 detail with fittings)")
print("  weight: added tube length ~offsets the lighter 20-in bike wheel vs 6-in")
print("          pneumatic assembly - call it a wash, WEIGH IT on the bench")
print("  verify at gate 4: castor-swing prop clearance >= 2.5 in at full +/-60 deg")
