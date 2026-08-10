#!/usr/bin/env python3
"""Flaps trade: single-lever plain flaps on the free trailing edge of a
two-axis wing. Stall/field-length gains, the VFE spar-protection placard,
the flare-margin catch, and the two integration paths (add vs replace slats).
Baseline numbers scale off the workbook's 23.9 kt slatted stall at 456 lb.
"""
import math

rho = 0.002377; S = 129.0
GROSS_103 = 456.0; GROSS_EAB = 525.0
SPAR_LIMIT = 2331.0          # lb, absolute-strength load basis
VS_BASE_KT = 23.9            # workbook: slats CL 1.8 at 456 lb

# Plain flap, 25% chord, hinged TE. Section dCLmax ~0.9 at 40 deg; the
# spoilerons live on the top surface so the flap can run ~60% span inboard.
D_CLMAX_40 = 0.9 * 0.62      # ~0.55 aircraft increment at full deflection
D_CLMAX_25 = 0.7 * D_CLMAX_40

print("=== CONFIGURATIONS (stall at 456 lb, scaled off the workbook 23.9 kt) ===")
configs = [
    ("clean 4412 (no slats, no flaps)",           1.40),
    ("slats only (current aircraft)",             1.80),
    ("flaps 40 only  - Path B landing",           1.40 + D_CLMAX_40),
    ("slats + flaps 40 - Path A landing",         1.80 + D_CLMAX_40),
    ("flaps 25 only  - Path B takeoff",           1.40 + D_CLMAX_25),
]
for name, cl in configs:
    v = VS_BASE_KT * math.sqrt(1.8/cl)
    print(f"  {name:44s} CLmax {cl:.2f}  stall {v:.1f} kt ({v*1.151:.1f} mph)")
print(f"  103 stall gate is 24 kt in landing configuration (AC 103-7 practice).")
print(f"  Path A margin ~3.0 kt, Path B margin ~1.2 kt - both vs today's 0.1 kt")

print("\n=== VFE: THE SPAR-PROTECTION PLACARD ===")
# Vne 62 was set so slatted CLmax 1.8 cannot exceed the spar limit. A higher
# flapped CLmax must not break that; flaps retract, so a VFE placard restores it.
for name, cl in (("Path B (CLmax 1.95)", 1.95), ("Path A (CLmax 2.35)", 2.35)):
    v = math.sqrt(2*SPAR_LIMIT/(rho*S*cl))/1.467
    print(f"  {name}: max-lift = spar limit at {v:.0f} mph -> VFE placard 55 mph covers both")
print("  Unlike the fixed slats, flap overspeed is pilot-dependent - the one place")
print("  the 'protected by physics' load basis gains a placard. VFE 55 vs Vne 62")
print("  is a gentle placard; the 103 kit cannot reach 55 mph level anyway.")

print("\n=== FIELD LENGTHS (design-log table, already computed there) ===")
print("  CLmax 1.8 slats:          stall 28.8 mph, takeoff 140 ft, landing 84 ft")
print("  CLmax 2.3 slats+flaps:    stall 25.5 mph, takeoff 110 ft, landing 65 ft")
print("  CLmax ~2.0 flaps-only:    interpolates to ~ takeoff 125 ft, landing ~72 ft")
print("  Plus flaps + symmetric spoilers together: steep AND slow over the trees -")
print("  the audit's 480 ft over-50-ft-obstacle case improves further (quantify at gate 3).")

print("\n=== THE FLARE-MARGIN CATCH (the real engineering gate) ===")
# Gate 3: flare at fwd CG in ground effect uses -19.3 of -25 deg elevator.
dcm_d = -0.008               # per deg deflection, 25%c plain flap, section
span_frac = 0.60
dcm40 = dcm_d*40*span_frac   # aircraft pitching-moment increment
cbar, lt = 50/12, 10.1
dCLt = -dcm40*cbar/lt*(S/30.0)      # extra tail CL demand (tail area 30 ft2)
delev = dCLt/0.035                   # ~deg at 0.035 CL/deg elevator power
print(f"  flaps 40: dCm ~ {dcm40:.2f} -> ~{delev:.0f} deg more elevator before the")
print(f"  downwash offset; gate-3 flare margin is only 5.7 deg. Full-flap flare at")
print(f"  forward CG MAY SATURATE. Mitigations, in order of preference:")
print(f"    - land at flaps 25 (keeps ~70% of the CLmax gain, ~half the moment)")
print(f"    - re-run gate 3 with flap downwash before widening elevator throw")
print(f"  This is a required gate-3 rerun, not a redesign.")

print("\n=== WEIGHT: THE DECISION ===")
print("  Flap conversion of the fixed TE: hinges, one-piece torque tube (asymmetric")
print("  deployment impossible by construction), Johnson bar w/ 3 notches, TE")
print("  stiffening: +4 to +6 lb.")
print("  Path A (add to slatted wing):  103 kit 253.2 + ~5 = ~258 lb - BUSTS 254.")
print("     -> Path A is EAB-only, and the airframe-invariant rule kills kit-able")
print("        flaps (a hinged TE is not a bolt-on). Path A dies for the fleet.")
print("  Path B (flaps REPLACE slats):  -6 lb slats + ~5 lb flaps = net ~-1 lb.")
print("     103 kit ~252, stall margin 0.1 -> ~1.2 kt, slat cruise drag deleted,")
print("     and the scariest legality item (unverified slatted CLmax 1.8 with 0.1 kt")
print("     margin) is replaced by a NeuralFoil-verified clean 1.4 (1.45 computed)")
print("     plus a textbook plain-flap increment.")
print("  Path B's real price: the slats' docile high-alpha stall character goes.")
print("     Washout 2.5 deg + inboard flaps keep tips flying, but GENTLENESS MUST BE")
print("     DEMONSTRATED - quarter-scale model stall tests before committing.")
