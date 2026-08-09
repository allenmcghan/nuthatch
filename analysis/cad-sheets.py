#!/usr/bin/env python3
"""Dimensioned CAD sheet set from the rev E mesh (pod-and-boom fuselage).
Outputs drawings/sheets/GA-001.png, LG-001.png, CP-001.png and
drawings/nuthatch-sheets.pdf. Dimensions in inches, datum = prop plane.
"""
import json, os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

sp = sys.argv[1] if len(sys.argv) > 1 else "."
m = json.load(open(os.path.join(sp, "nuthatch-mesh.json")))
V = np.array(m["v"]); F = np.array(m["f"])

INK = "#1d2733"; FILL = "#dfe5ea"; EDGE = "#8494a6"; DIM = "#b23a2f"

def draw_proj(ax, i, j, fc=FILL):
    for tri in F:
        p = V[tri]
        ax.fill(p[:, i], p[:, j], facecolor=fc, edgecolor=EDGE, lw=0.12, zorder=2)

def dim_h(ax, x1, x2, y, label, off=0):
    ax.annotate("", (x1, y), (x2, y), arrowprops=dict(arrowstyle="<->", color=DIM, lw=1))
    ax.text((x1+x2)/2, y+2+off, label, ha="center", color=DIM, fontsize=8.5,
            bbox=dict(fc="white", ec="none", pad=0.5))
def dim_v(ax, x, y1, y2, label):
    ax.annotate("", (x, y1), (x, y2), arrowprops=dict(arrowstyle="<->", color=DIM, lw=1))
    ax.text(x+3, (y1+y2)/2, label, va="center", color=DIM, fontsize=8.5, rotation=90,
            bbox=dict(fc="white", ec="none", pad=0.5))
def title_block(fig, dwg, title, rev):
    fig.text(0.99, 0.015, f"NUTHATCH  ·  {dwg}  ·  {title}  ·  REV {rev}  ·  UNITS: IN  ·  DATUM: PROP PLANE  ·  2026-08-09",
             ha="right", fontsize=8, color=INK, family="monospace")

os.makedirs("drawings/sheets", exist_ok=True)
pdf = PdfPages("drawings/nuthatch-sheets.pdf")

# ---------- Sheet GA-001: three-view ----------
fig, axs = plt.subplots(2, 2, figsize=(15, 10))
ax = axs[0][0]; draw_proj(ax, 0, 1)
dim_h(ax, 48, 98, -215, "CHORD 50.0"); dim_v(ax, 240, -186, 186, "SPAN 372.0 (31.0 FT)")
dim_h(ax, 0, 219, 205, "LENGTH 219")
ax.axvline(48, color=DIM, lw=0.4, ls=":"); ax.text(48, 195, "WING LE STA 48.0", fontsize=7, color=DIM)
ax.axvline(182, color=DIM, lw=0.4, ls=":"); ax.text(160, 195, "TAIL STA 182.0", fontsize=7, color=DIM)
ax.set_title("TOP VIEW"); ax.set_aspect("equal"); ax.grid(lw=0.25, alpha=0.4)
ax = axs[1][0]; draw_proj(ax, 0, 2)
dim_v(ax, 226, 0, 87, "HEIGHT 87"); dim_v(ax, -14, 0, 40, "THRUSTLINE 40.0")
dim_h(ax, 15, 70.5, -10, "WHEELBASE 55.5")
ax.axvline(63, color=DIM, lw=0.5, ls="--"); ax.text(63, 92, "CG 30% MAC STA 63.0", fontsize=7, color=DIM, ha="center")
ax.annotate("TAIL BOOM 6061-T6 5.00 x .065\nSTA 96-182 · CABLES INSIDE", (135, 27), (108, 8), fontsize=7.5, color=INK,
            arrowprops=dict(arrowstyle="->", color=INK, lw=0.8))
ax.set_title("SIDE VIEW"); ax.set_aspect("equal"); ax.grid(lw=0.25, alpha=0.4)
ax = axs[1][1]; draw_proj(ax, 1, 2)
dim_h(ax, -28, 28, -10, "TRACK 56.0"); dim_v(ax, -200, 0, 30, "PROP TIP CLR 10.0")
dim_h(ax, -186, 186, 100, "SPAN 372.0")
ax.set_title("FRONT VIEW"); ax.set_aspect("equal"); ax.grid(lw=0.25, alpha=0.4)
ax = axs[0][1]
c, s = np.cos(np.radians(-35)), np.sin(np.radians(-35))
c2, s2 = np.cos(np.radians(22)), np.sin(np.radians(22))
Vx = V[:, 0]*c+V[:, 1]*s; Vy2 = (-V[:, 0]*s+V[:, 1]*c)*s2+V[:, 2]*c2
order = np.argsort([np.mean((-V[t, 0]*s+V[t, 1]*c)*c2-V[t, 2]*s2) for t in F])
for k in order: ax.fill(Vx[F[k]], Vy2[F[k]], facecolor="#e8edf1", edgecolor=EDGE, lw=0.08)
ax.set_aspect("equal"); ax.axis("off"); ax.set_title("ISOMETRIC")
fig.suptitle("GENERAL ARRANGEMENT — Vne 62 MPH FLEET · 103 KIT 253 LB / EAB KIT 276 LB", fontsize=13)
title_block(fig, "GA-001", "GENERAL ARRANGEMENT", "E")
fig.tight_layout(rect=[0, 0.03, 1, 0.97])
fig.savefig("drawings/sheets/GA-001.png", dpi=150); pdf.savefig(fig); plt.close(fig)

# ---------- Sheet LG-001: landing gear ----------
fig, axs = plt.subplots(1, 2, figsize=(15, 8))
ax = axs[0]
sel = (V[F].mean(axis=1)[:, 0] > 2) & (V[F].mean(axis=1)[:, 0] < 100) & (V[F].mean(axis=1)[:, 2] < 46)
for tri in F[sel]:
    p = V[tri]; ax.fill(p[:, 0], p[:, 2], facecolor=FILL, edgecolor=EDGE, lw=0.15)
ax.axhline(0, color=INK, lw=1.2)
for x in range(3, 105, 6): ax.plot([x, x-3], [0, -2.5], color=INK, lw=0.5)
dim_h(ax, 15, 70.5, -8, "WHEELBASE 55.5")
dim_v(ax, 92, 0, 14.5, "AXLE 14.5"); dim_v(ax, 34, 0, 16, "BELLY 16.0")
dim_v(ax, 104, 0, 29, "TIRE 29 OD")
ax.axvline(2, color=DIM, lw=0.5, ls=":"); ax.text(2, 44, "PROP PLANE", fontsize=7.5, color=DIM, ha="center")
ax.annotate("RAKED NOSE LEG ~63°\n20x2.4 BMX WHEEL\nTIRE FACE STA 5 · 3.0 IN AFT OF PROP\nNOSE-OVER PROTECTION 35.5°\nCASTOR ±60° + FRICTION DAMPER", (17, 12), (5, 30), fontsize=7.5, color=INK,
            arrowprops=dict(arrowstyle="->", color=INK, lw=0.8))
ax.axvline(63, color=DIM, lw=0.5, ls="--"); ax.text(63, 44, "CG STA 63", fontsize=8, color=DIM, ha="center")
ax.axvline(70.5, color=DIM, lw=0.5, ls=":"); ax.text(70.5, 41, "MAINS STA 70.5 (15% MAC AFT)", fontsize=7.5, color=DIM, ha="center")
ax.annotate("MTB COIL-OVER\n2.3 IN STROKE @ 2:1", (67, 24), (40, 34), fontsize=8, color=INK,
            arrowprops=dict(arrowstyle="->", color=INK, lw=0.8))
ax.annotate("TRAILING ARM\nPIVOT STA 58", (62, 16), (34, 6), fontsize=8, color=INK,
            arrowprops=dict(arrowstyle="->", color=INK, lw=0.8))
ax.annotate("29x2.4 BICYCLE MAIN\nALLOY RIM · BOOST 148 HUB\nNATIVE 6-BOLT DISC\n22-28 PSI PLACARD", (78, 20), (95, 34), fontsize=8, color=INK,
            arrowprops=dict(arrowstyle="->", color=INK, lw=0.8))
ax.set_title("SIDE — TRAILING ARM MAIN GEAR"); ax.set_aspect("equal"); ax.grid(lw=0.25, alpha=0.4)
ax = axs[1]
sel2 = (V[F].mean(axis=1)[:, 0] > 25) & (V[F].mean(axis=1)[:, 0] < 100)
for tri in F[sel2]:
    p = V[tri]; ax.fill(p[:, 1], p[:, 2], facecolor=FILL, edgecolor=EDGE, lw=0.15)
ax.axhline(0, color=INK, lw=1.2)
dim_h(ax, -28, 28, -8, "TRACK 56.0")
dim_v(ax, 42, 0, 20, "SEAT PAN 20")
ax.text(0, 50, "DESIGN: 8 FPS SINK @ 525 LB · N=3.0 · 788 LB LIMIT / 1181 ULT PER LEG\n"
               "STROKE 6.6 IN TOTAL (TIRE ~2 + ARM 4.6) · DROP TEST 456 LB / 12 IN REQ'D\n"
               "LATERAL PROOF 400 LB AT RIM REQ'D · TIP-BACK 15.5° · OVERTURN 51°\n"
               "NOSE LOAD 13.5% STATIC · NOSE LIMIT ~160 LB (STATIC + 0.35g BRAKING)",
        ha="center", fontsize=8.5, color=INK, family="monospace",
        bbox=dict(fc="#f2f5f7", ec=EDGE))
ax.set_title("FRONT — TRACK AND STANCE"); ax.set_aspect("equal"); ax.grid(lw=0.25, alpha=0.4)
fig.suptitle("LANDING GEAR — GRASS / EASY ENTRY / DAMPED  (trades/landing-gear.md)", fontsize=13)
title_block(fig, "LG-001", "MAIN + NOSE GEAR", "C")
fig.tight_layout(rect=[0, 0.03, 1, 0.96])
fig.savefig("drawings/sheets/LG-001.png", dpi=150); pdf.savefig(fig); plt.close(fig)

# ---------- Sheet CP-001: cockpit / entry ----------
fig, ax = plt.subplots(figsize=(15, 8))
sel3 = (V[F].mean(axis=1)[:, 0] < 130)
for tri in F[sel3]:
    p = V[tri]; ax.fill(p[:, 0], p[:, 2], facecolor=FILL, edgecolor=EDGE, lw=0.12)
ax.axhline(0, color=INK, lw=1.2)
# 6'0" pilot silhouette, seated: seat pan at (58, 20)
hx, hz = 55, 51
ax.add_patch(plt.Circle((hx, hz), 4.2, fc="#b7c3cd", ec=INK, lw=1, zorder=5))
ax.plot([hx, 57, 57], [hz-4, 34, 20.5], color=INK, lw=7, solid_capstyle="round", zorder=5)   # torso
ax.plot([57, 44, 42], [21, 22, 12], color=INK, lw=6, solid_capstyle="round", zorder=5)       # thigh+shin
ax.plot([57, 47, 43.5], [34, 30, 26], color=INK, lw=4, solid_capstyle="round", zorder=5)     # arm to stick
dim_v(ax, 20, 0, 20, "SEAT PAN 20.0")
dim_v(ax, 128, 0, 26, "STEP-OVER 26")
dim_v(ax, 8, 0, 40, "THRUSTLINE 40")
dim_v(ax, 100, 55.5, 64, "HEAD CLR ~8")
ax.text(70, 74, "6'0\" / 170 LB PILOT SHOWN · PEDALS ADJUSTABLE 3 POS (105-200 LB PILOT RANGE)\n"
                "BALLAST BOSS STA 20 (8 LB REQ'D < 135 LB PILOT) · GRAB: CABANE STRUT",
        ha="center", fontsize=9, color=INK, family="monospace",
        bbox=dict(fc="#f2f5f7", ec=EDGE))
ax.set_title("COCKPIT & ENTRY — SIDE"); ax.set_aspect("equal"); ax.grid(lw=0.25, alpha=0.4)
title_block(fig, "CP-001", "COCKPIT / ENTRY / PILOT RANGE", "B")
fig.tight_layout(rect=[0, 0.03, 1, 0.97])
fig.savefig("drawings/sheets/CP-001.png", dpi=150); pdf.savefig(fig); plt.close(fig)

pdf.close()
print("wrote drawings/sheets/{GA-001,LG-001,CP-001}.png + drawings/nuthatch-sheets.pdf")
