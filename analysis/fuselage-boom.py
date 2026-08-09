#!/usr/bin/env python3
"""Fuselage architecture: size a single straight tail boom against the tail
loads, and compare it to the full-length welded truss the digital-fabrication
plan assumed. Basis: tail loads at Vne 62 mph (the fleet load basis), boom
root at the aft cage bulkhead, sta 96; tail post sta 182 (skid 184).
"""
import math

# ---- load basis
VNE_MPH = 62.0
q = 0.5*0.002377*(VNE_MPH*1.4667)**2          # psf
S_H, S_V = 30.0, 15.0                          # ft^2
CLT = 1.0                                      # max tail lift coeff, flat-plate-ish surface
ROOT_STA, TAIL_STA = 96.0, 182.0
ARM = TAIL_STA - ROOT_STA                      # in
ULT = 1.5

P_h = q*S_H*CLT                                # lb limit, horizontal tail
P_v = q*S_V*CLT                                # lb limit, vertical tail side load
M_h = P_h*ARM*ULT                              # in-lb ultimate, vertical bending
M_v = P_v*ARM*ULT                              # in-lb ultimate, lateral bending
Z_VT = 30.0                                    # in, VT center of pressure above boom axis
T = P_v*Z_VT*ULT                               # in-lb ultimate torsion

print("=== TAIL LOADS AT VNE 62 MPH (boom root sta %.0f, arm %.0f in) ===" % (ROOT_STA, ARM))
print(f"  q = {q:.2f} psf")
print(f"  H-tail load  {P_h:6.0f} lb limit -> bending {M_h:8.0f} in-lb ult")
print(f"  V-tail load  {P_v:6.0f} lb limit -> lateral  {M_v:8.0f} in-lb ult, torsion {T:6.0f} in-lb ult")
print(f"  (design-log losers table carried the boom requirement as 37,800 in-lb — consistent)")

# ---- candidate booms: 6061-T6 drawn tube (Ftu 42 ksi, E 10.0e6) and one 4130 option
# Bending allowable = min(Ftu, 0.25 * 0.6*E*t/R): classical thin-shell buckling
# with a 0.25 empirical knockdown — conservative (Bruhn-style modulus of rupture
# for these D/t runs a little higher).
def tube(D, t, Ftu, E, rho):
    d = D - 2*t
    I = math.pi/64*(D**4 - d**4)
    S = 2*I/D
    scr = 0.25*0.6*E*t/(D/2)
    Fb = min(Ftu, scr)
    A = math.pi*(D - t)*t
    return I, S, Fb, Fb*S, A*ARM*rho + A*2.0*rho*10  # +10 in equiv for fittings overlap

print("\n=== BOOM CANDIDATES (root sta 96 to tail post 182) ===")
print("  %-22s %7s %7s %8s %10s %7s %7s" % ("tube", "I in4", "S in3", "Fb ksi", "Mall inlb", "M.S.", "wt lb"))
for name, D, t, Ftu, E, rho in [
    ("6061-T6 5.00 x .058", 5.0, 0.058, 42000, 10.0e6, 0.098),
    ("6061-T6 5.00 x .065", 5.0, 0.065, 42000, 10.0e6, 0.098),
    ("6061-T6 5.50 x .058", 5.5, 0.058, 42000, 10.0e6, 0.098),
    ("6061-T6 6.00 x .058", 6.0, 0.058, 42000, 10.0e6, 0.098),
    ("4130    4.00 x .049", 4.0, 0.049, 95000, 29.0e6, 0.283),
]:
    I, S, Fb, Mall, wt = tube(D, t, Ftu, E, rho)
    ms = Mall/M_h - 1
    print("  %-22s %7.2f %7.2f %8.1f %10.0f %+6.0f%% %7.1f" % (name, I, S, Fb/1000, Mall, ms*100, wt))

# ---- selected boom: 5.00 x .065 6061-T6
D, t = 5.0, 0.065
I, S, Fb, Mall, wt = tube(D, t, 42000, 10.0e6, 0.098)
J = 2*I
tau = T*(D/2)/J
EI = 10.0e6*I
delta = (P_h)*ARM**3/(3*EI)                    # tip deflection at limit load
m_eff = (18.5 + 0.23*wt)/386.0                 # tail mass + participating boom mass
k = 3*EI/ARM**3
f_n = math.sqrt(k/m_eff)/(2*math.pi)
print(f"\n=== SELECTED: 6061-T6 5.00 x .065 ===")
print(f"  ultimate bending margin {Mall/M_h-1:+.0%}; torsional shear {tau/1000:.1f} ksi (trivial)")
print(f"  tip deflection at limit H-load: {delta:.1f} in; first vertical bending mode ~{f_n:.1f} Hz")
print(f"  boom + root/tail fittings ~{wt:.1f} lb")

# ---- what it replaces: the aft half of the welded truss (sta 96-182)
# 4 longerons 3/4 x .035 4130 + ~40 diagonal/vertical members at ~60% of
# longeron weight + stringers/formers to carry fabric to a fuselage shape.
A_lon = math.pi*(0.75 - 0.035)*0.035
w_lon = 4*A_lon*ARM*0.283
w_diag = 0.6*w_lon
w_form = 2.0
w_truss = w_lon + w_diag + w_form
n_cope = 40*2                                  # fishmouthed ends, aft bays alone
print(f"\n=== AFT TRUSS IT REPLACES (est.) ===")
print(f"  longerons {w_lon:.1f} + diagonals {w_diag:.1f} + stringers/formers {w_form:.1f} = {w_truss:.1f} lb")
print(f"  ~{n_cope} fishmouthed tube ends deleted; aft fuselage jig deleted (a drawn tube is straight by manufacture)")
print(f"  net weight {wt - w_truss:+.1f} lb vs truss aft bay — call it 'about even to -4'; ledger keeps 55 lb unbanked")
