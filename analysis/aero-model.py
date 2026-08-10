#!/usr/bin/env python3
"""Nuthatch parametric aero model.

Geometry from the repo's own dimensions (weight sheet stations, README spec).
Outputs:
  - airfoil candidate polars at the real Reynolds numbers (NeuralFoil)
  - VLM check of the whole aircraft: trim, static margin, Oswald e, dihedral effect
  - model/nuthatch.stl           (3D mesh, also usable to scale the RC model)
  - drawings/general-arrangement.png  (three-view + isometric)
  - scratch JSON mesh for the interactive viewer

Requires: pip install aerosandbox neuralfoil
"""
import numpy as np, json, struct, os, sys
import aerosandbox as asb
import aerosandbox.numpy as anp

IN = 0.0254
# ---------------- geometry, from the repo ----------------
SPAN = 372 * IN            # 31 ft
CHORD = 50 * IN
WING_LE = 48 * IN          # station, datum = prop plane
WING_Z = 26 * IN           # high wing above fuselage mid-line
DIHEDRAL = 5.0             # deg, placeholder 4-6 in open-questions
WASHOUT = 2.5              # deg, placeholder 2-3
INCIDENCE = 2.0
HTAIL_S = 30.0             # ft^2
HTAIL_SPAN = 10.0          # ft
VTAIL_S = 15.0
VTAIL_H = 5.0
TAIL_STA = 182 * IN
CG_STA = (48 + 0.30 * 50) * IN   # 30% MAC
GROSS = 496 * 4.44822            # N

AF = {}
def airfoil(name):
    if name not in AF: AF[name] = asb.Airfoil(name)
    return AF[name]

wing_af = airfoil("naca4412")   # candidate; Sky Pup section is open question #1
tail_af = airfoil("naca0009")

wing = asb.Wing(name="wing", symmetric=True, xsecs=[
    asb.WingXSec(xyz_le=[WING_LE, 0, WING_Z], chord=CHORD, twist=INCIDENCE, airfoil=wing_af),
    asb.WingXSec(xyz_le=[WING_LE, SPAN/2*np.cos(np.radians(DIHEDRAL)),
                         WING_Z + SPAN/2*np.sin(np.radians(DIHEDRAL))],
                 chord=CHORD, twist=INCIDENCE - WASHOUT, airfoil=wing_af)])
hc = HTAIL_S / HTAIL_SPAN * 0.3048  # chord m
htail = asb.Wing(name="htail", symmetric=True, xsecs=[
    asb.WingXSec(xyz_le=[TAIL_STA, 0, 0], chord=hc, twist=-1.5, airfoil=tail_af),
    asb.WingXSec(xyz_le=[TAIL_STA + 0.15*hc, HTAIL_SPAN/2*0.3048, 0], chord=0.85*hc,
                 twist=-1.5, airfoil=tail_af)])
vc = VTAIL_S / VTAIL_H * 0.3048
vtail = asb.Wing(name="vtail", symmetric=False, xsecs=[
    asb.WingXSec(xyz_le=[TAIL_STA - 0.3*vc, 0, 0], chord=vc, airfoil=tail_af),
    asb.WingXSec(xyz_le=[TAIL_STA + 0.25*vc, 0, VTAIL_H*0.3048], chord=0.6*vc, airfoil=tail_af)])
fuse = asb.Fuselage(name="fuselage", xsecs=[
    asb.FuselageXSec(xyz_c=[x*IN, 0, z*IN], radius=r*IN)
    for x, z, r in [(6,4,3),(20,3,8),(40,2,11),(58,0,12),(80,0,11),(100,2,8),
                    (125,3,5),(150,4,3.5),(178,5,2.5),(184,5,2.0)]])
plane = asb.Airplane(name="Nuthatch", xyz_ref=[CG_STA, 0, WING_Z*0.5],
                     wings=[wing, htail, vtail], fuselages=[fuse])

def vlm(alpha, beta=0.0, V=22.35):
    op = asb.OperatingPoint(velocity=V, alpha=alpha, beta=beta)
    return asb.VortexLatticeMethod(airplane=plane, op_point=op,
                                   spanwise_resolution=24, chordwise_resolution=8).run()

if __name__ == "__main__":
    print("=== NEURALFOIL: candidate sections at the real Reynolds numbers ===")
    # cruise 50 mph: Re 1.94M ; stall 28.8 mph: Re 1.12M ; model 16.5 mph quarter-scale: 161k
    for re_lbl, Re in [("stall  1.12M", 1.12e6), ("cruise 1.94M", 1.94e6), ("RC model 161k", 1.61e5)]:
        row = f"  Re {re_lbl}: "
        for name in ["naca4412", "naca2412", "naca4415", "naca6409"]:
            af = airfoil(name)
            alphas = np.arange(-4, 20.5, 0.5)
            aero = af.get_aero_from_neuralfoil(alpha=alphas, Re=Re, mach=0.05, model_size="xlarge")
            clmax = float(np.max(aero["CL"]))
            cd06 = float(np.interp(0.60, aero["CL"][:20], aero["CD"][:20]))
            row += f"{name}: CLmax {clmax:.2f} cd@0.6 {cd06*1e4:.0f}ct | "
        print(row)

    print("\n=== VLM: whole aircraft ===")
    CL_cruise = GROSS / (0.5*1.225*22.35**2*12.077)
    r0, r5 = vlm(0.0), vlm(5.0)
    a_slope = (r5["CL"]-r0["CL"])/np.radians(5)
    alpha_trim = np.degrees((CL_cruise - r0["CL"])/a_slope)
    rt = vlm(alpha_trim)
    # static margin from Cm slope
    dCm = (r5["Cm"]-r0["Cm"])/(r5["CL"]-r0["CL"])
    print(f"  CL needed at 50 mph, 496 lb: {CL_cruise:.3f} -> trims at alpha {alpha_trim:+.1f} deg")
    print(f"  CLa {a_slope:.2f}/rad | dCm/dCL {dCm:+.3f} -> static margin {-dCm*100:.0f}% MAC at 30% CG")
    print(f"  trim: CL {rt['CL']:.3f}  CDi {rt['CD']:.5f}  Cm {rt['Cm']:+.4f}")
    e = rt["CL"]**2/(np.pi*(31**2/130)*rt["CD"])
    print(f"  Oswald e from VLM: {e:.2f}   (workbook assumes 0.85)")
    rb = vlm(alpha_trim, beta=5.0)
    print(f"  beta=5: Cl {rb['Cl']:+.4f} (dihedral effect)  Cn {rb['Cn']:+.4f} (weathercock)")
    print(f"  Clb {rb['Cl']/np.radians(5):+.3f}/rad  Cnb {rb['Cn']/np.radians(5):+.3f}/rad")
