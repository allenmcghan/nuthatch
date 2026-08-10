#!/usr/bin/env python3
"""Gate 3: trim and tail analysis.

Classic wing+tail trim equations, parameters from the repo and from
aero-model.py's VLM/NeuralFoil results. Answers, in order:
  1. Tail incidence for hands-off cruise
  2. Elevator deflection to trim, across speed and CG range
  3. Flare authority at forward CG in ground effect
  4. Whether the elevator can command slatted CLmax at Vne (audit Finding 1c)
  5. Rudder-roll authority and crosswind capability (two-axis handling)
Everything is linear aero - treat results as gate-3 sizing, not certification.
"""
import numpy as np

# ---- geometry & aero parameters ----
S, b, c = 130.0, 31.0, 50/12          # ft^2, ft, ft
AR = b*b/S
a_w = 4.42                            # /rad, wing alone (aero-model.py)
CM0_W = -0.10                         # NACA 4412 section cm; slat/washout delta noted in doc
X_AC = 0.25                           # wing AC, fraction MAC
IW_ZL = np.radians(2.0 + 4.0)         # wing zero-lift line vs fuselage line (incidence 2 + 4412 alpha0 -4)
CLMAX_SLATS = 1.8

S_h, b_h = 30.0, 10.0                 # ft^2, ft
AR_h = b_h*b_h/S_h
a_t = 5.7/(1 + 5.7/(np.pi*AR_h*0.85))  # /rad
ETA_H = 0.90                          # power-off tail efficiency
TAU_E = 0.63                          # elevator effectiveness, ce/c = 0.45
DE_MAX = np.radians(25)               # elevator throw, both ways
K_EPS = 2/(np.pi*AR)                  # deps/dCL_w, rad

S_v, b_v = 15.0, 5.0
LE_WING = 48.0                        # station, in
TAIL_AC = 182 + 0.25*36               # in
RHO = 0.002377                        # slug/ft^3

def q_of(V_mph): return 0.5*RHO*(V_mph*5280/3600)**2

def trim(V_mph, W_lb, cg_frac, ge=False, it=None):
    """Solve alpha_fus, delta_e for L=W and Cm=0. Returns degrees, CLs."""
    aw = a_w*(1.10 if ge else 1.0)
    keps = K_EPS*(0.5 if ge else 1.0)
    lh = (TAIL_AC - (LE_WING + cg_frac*50))/12          # ft, tail arm from CG
    Vh = S_h*lh/(S*c)
    xbar = cg_frac - X_AC
    CL_need = W_lb/(q_of(V_mph)*S)
    # unknowns u = [alpha_fus(rad), de(rad)]
    # CL_w = aw*(alpha + IW_ZL); eps = keps*CL_w
    # CL_t = a_t*(alpha + it - eps) + a_t*TAU_E*de
    # L: CL_w + ETA_H*(S_h/S)*CL_t = CL_need
    # M: CM0_W + CL_w*xbar - ETA_H*Vh*CL_t = 0
    A = np.zeros((2,2)); r = np.zeros(2)
    caw = aw; ct_a = a_t*(1 - keps*aw)      # dCL_t/dalpha
    A[0,0] = caw + ETA_H*S_h/S*ct_a
    A[0,1] = ETA_H*S_h/S*a_t*TAU_E
    A[1,0] = caw*xbar - ETA_H*Vh*ct_a
    A[1,1] = -ETA_H*Vh*a_t*TAU_E
    CL_w0 = caw*IW_ZL
    CL_t0 = a_t*(it - keps*CL_w0)
    r[0] = CL_need - CL_w0 - ETA_H*S_h/S*CL_t0
    r[1] = -(CM0_W + CL_w0*xbar - ETA_H*Vh*CL_t0)
    alpha, de = np.linalg.solve(A, r)
    CL_w = caw*(alpha + IW_ZL)
    eps = keps*CL_w
    CL_t = a_t*(alpha + it - eps) + a_t*TAU_E*de
    return np.degrees(alpha), np.degrees(de), CL_w, CL_t

def max_CL_command(V_mph, cg_frac, it):
    """Full-up elevator: solve Cm=0 for alpha; return commanded CL_w."""
    lh = (TAIL_AC - (LE_WING + cg_frac*50))/12
    Vh = S_h*lh/(S*c); xbar = cg_frac - X_AC
    de = -DE_MAX
    ct_a = a_t*(1 - K_EPS*a_w)
    # CM0 + a_w(al+IWZL)xbar - ETA*Vh*[a_t(al+it-K*a_w(al+IWZL)) + a_t*TAU*de]=0
    kA = a_w*xbar - ETA_H*Vh*ct_a
    kB = (CM0_W + a_w*IW_ZL*xbar
          - ETA_H*Vh*(a_t*(it - K_EPS*a_w*IW_ZL) + a_t*TAU_E*de))
    alpha = -kB/kA
    return a_w*(alpha + IW_ZL), np.degrees(alpha)

# ---- 1. tail incidence: de = 0 at 50 mph cruise, 496 lb, CG 30% ----
from scipy.optimize import brentq
it_trim = brentq(lambda it: trim(50, 496, 0.30, it=it)[1], np.radians(-12), np.radians(6))
print("1. TAIL INCIDENCE for hands-off 50 mph cruise at 30%% CG: i_t = %.1f deg"
      % np.degrees(it_trim))
IT = it_trim

# ---- 2. trim map ----
print("\n2. ELEVATOR TO TRIM, 1 g, 496 lb  (+down, -up; limit ±25)")
print("   %-8s" % "V mph", end="")
cgs = [0.25, 0.283, 0.308, 0.35]
for cg in cgs: print("  CG %2.0f%%" % (cg*100), end="")
print()
for V in (29, 33, 38, 45, 50, 55, 60, 69):
    print("   %-8d" % V, end="")
    for cg in cgs:
        _, de, _, _ = trim(V, 496, cg, it=IT)
        print("  %+6.1f" % de, end="")
    print()

# ---- 3. flare at forward CG in ground effect ----
print("\n3. FLARE: trim to 0.95 CLmax (CL 1.71) in ground effect, forward CG 25%")
for W, lbl in ((496, "design"), (426, "light")):
    Vs = np.sqrt(W/(q_of(1)*S*CLMAX_SLATS))   # mph since q_of(1)*V^2 scaling
    Vf = 1.05*Vs
    # solve V such that CL_need = 1.71
    Vneed = np.sqrt(W/(q_of(1)*S*1.71))
    al, de, clw, clt = trim(Vneed, W, 0.25, ge=True, it=IT)
    tail_stall = abs(clt) > 0.85
    print("   %s %d lb: V %.1f mph  de %+.1f deg (limit -25) %s | tail CL %+0.2f%s"
          % (lbl, W, Vneed, de, "<-- INSUFFICIENT" if de < -25 else "OK", clt,
             "  <-- TAIL NEAR STALL" if tail_stall else ""))

# ---- 4. Finding 1c: can full-up elevator reach CLmax at speed? ----
print("\n4. MAX COMMANDABLE CL, full-up elevator (-25 deg), free air")
print("   %-10s %-10s %-14s %-10s" % ("V mph", "CG", "CL commanded", "vs CLmax 1.8"))
for V in (50, 62, 69):
    for cg in (0.283, 0.308, 0.35):
        clw, al = max_CL_command(V, cg, IT)
        verdict = "REACHES CLmax" if clw >= CLMAX_SLATS else "elevator-limited"
        print("   %-10d %-10s CL %-11.2f %s (alpha %.0f deg)" % (V, "%.0f%%"%(cg*100), clw, verdict, al))
n = max_CL_command(69, 0.308, IT)[0]*q_of(69)*S/496
print("   -> at Vne, aft normal CG: n available = %.2f g  (limit 4.7)" % n)

# ---- 5. rudder-roll authority ----
print("\n5. RUDDER-ROLL (two-axis handling), from aero-model.py derivatives")
Clb, Cnb = -0.082, 0.107
lv = (TAIL_AC - (LE_WING + 0.30*50))/12
Vv = S_v*lv/(S*b)
a_v = 2.8; TAU_R = 0.65; DR = np.radians(25)
Cndr = ETA_H*Vv*a_v*TAU_R
beta_ss = Cndr*DR/Cnb
Cl_r = -Clb*beta_ss
Clp = -0.50
Cl_spoiler = 0.020
for V in (38, 50):
    Vf = V*5280/3600
    p_r = Cl_r/(-Clp)*2*Vf/b
    p_s = Cl_spoiler/(-Clp)*2*Vf/b
    print("   V %d mph: rudder-only steady roll %4.1f deg/s | + spoileron %4.1f deg/s | t(30 deg bank) ~%.1f s"
          % (V, np.degrees(p_r), np.degrees(p_r+p_s), 30/np.degrees(p_r+p_s)+0.7))
print("   steady sideslip at full rudder: %.1f deg -> crosswind ~%.0f mph at 37 mph approach"
      % (np.degrees(beta_ss), 37*np.sin(beta_ss)))

# ---- static margin, classic ----
NP = X_AC + ETA_H*(S_h*(TAIL_AC-(LE_WING+X_AC*50))/12/(S*c))*(a_t/a_w)*(1-K_EPS*a_w)
print("\nStatic margin (classic): NP at %.0f%% MAC -> SM %.0f%% at 30%% CG, %.0f%% at 35%%"
      % (NP*100, (NP-0.30)*100, (NP-0.35)*100))
