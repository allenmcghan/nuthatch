#!/usr/bin/env python3
"""Rev H: what the pilot can actually see.

The complaint that started this was "the sight lines and visibility are
terrible", and the repo had no number for visibility at all - only an assertion
that the cabin was enclosed. So: ray-cast from the pilot's eye against the real
mesh, in a grid over the whole sphere, and classify what each ray hits first.

Method. Eye point from the reclined-pilot geometry (trades/enclosed-cockpit.md
§2). For each direction, walk every triangle in the mesh with Moller-Trumbore
and keep the nearest hit. Triangles are tagged by the group they came from, so
a hit is one of: GLAZED (you see through it), BLOCKED (fabric, cowl, wing,
structure), or CLEAR (nothing in the way at all - the ray leaves the aircraft).

What this does NOT model: the frame tubes are drawn at their true diameter so
they block honestly, but a 3/8 in tube at 30 in reads as 0.7 deg and the grid
here is 1.5 deg, so thin structure is under-counted. Distortion, tint, reflection
and dirt are not modelled: a glazed ray is treated as a perfect view. Read the
glazed numbers as an upper bound.

Compares rev G (windshield = top 45 deg only, sta 14-48) against rev H (whole
front glazed, cowl the only opaque thing forward of the pilot).

Outputs drawings/visibility.png
"""
import json, os, sys
import numpy as np

SP = sys.argv[1] if len(sys.argv) > 1 else "."
m = json.load(open(os.path.join(SP, "nuthatch-mesh.json")))
V = np.array(m["v"], float)
F = np.array(m["f"], int)
GRP = {g[0]: (g[1], g[2]) for g in m["groups"]}

# Eye: reclined 35 deg, head centre sta 60 / z 45 (render-hero.py builds the same
# figure). Eyes sit ~2 in forward of and level with the head centre.
EYE = np.array([58.0, 0.0, 45.5])

GLAZED = {"glass", "film"}
IGNORE = {"prop"}                      # you see through a turning propeller
kind = np.empty(len(F), dtype=object)
for name, a, b in m["groups"]:
    kind[a:b] = "skip" if name in IGNORE else \
                ("glazed" if name in GLAZED else "blocked")

P0 = V[F[:, 0]]; E1 = V[F[:, 1]] - P0; E2 = V[F[:, 2]] - P0
AREA = 0.5*np.linalg.norm(np.cross(E1, E2), axis=1)
CENT = V[F].mean(axis=1)

# Rev G classification of the same triangles, so the comparison is like for
# like: identical mesh, identical eye, only the glazing masks differ. Every
# pod-skin face is re-tested against rev G's rules (windshield = the top 45 deg
# from sta 14 to 48; doors unchanged); everything else keeps its class.
FU = np.array([[2, 40, 3.5, 3.5], [12, 33, 11, 6], [24, 33, 15, 9],
               [36, 34.5, 18.5, 10.8], [48, 35.5, 19.5, 11.5],
               [60, 36, 19, 11.5], [72, 36, 18, 10.5], [84, 33, 12, 7],
               [96, 27.5, 3.5, 3.2], [184, 27, 1.75, 1.75]])
skinf = np.zeros(len(F), bool)
for g in ("fuse", "cowl", "glass", "film"):
    a, b = GRP[g]; skinf[a:b] = True
cx, cy, cz = CENT.T
_z = np.interp(cx, FU[:, 0], FU[:, 1]); _h = np.interp(cx, FU[:, 0], FU[:, 2])
_w = np.interp(cx, FU[:, 0], FU[:, 3])
phif = np.degrees(np.arctan2(np.abs(cy)/np.maximum(_w, 1e-6),
                             (cz-_z)/np.maximum(_h, 1e-6)))
revG = ((cx >= 14) & (cx <= 48) & (phif <= 45)) | \
       ((cx >= 40) & (cx <= 78) & (phif >= 48) & (phif <= 116))
kindG = kind.copy()
kindG[skinf] = np.where(revG[skinf], "glazed", "blocked")

keep = (kind != "skip") & (AREA > 1e-9)
P0, E1, E2 = P0[keep], E1[keep], E2[keep]
GLZ = {"H": kind[keep] == "glazed", "G": kindG[keep] == "glazed"}
isglaze = GLZ["H"]


def cast(dirs):
    """Nearest-hit classification for a batch of unit directions from EYE."""
    out = np.zeros(len(dirs), dtype=np.int8)          # 0 clear, 1 glazed, 2 blocked
    T = EYE - P0
    for i, d in enumerate(dirs):
        pv = np.cross(d, E2)
        det = (E1*pv).sum(1)
        ok = np.abs(det) > 1e-9
        inv = np.where(ok, 1.0/np.where(ok, det, 1.0), 0.0)
        u = (T*pv).sum(1)*inv
        ok &= (u >= 0) & (u <= 1)
        qv = np.cross(T, E1)
        v = (d*qv).sum(1)*inv
        ok &= (v >= 0) & (u + v <= 1)
        t = (E2*qv).sum(1)*inv
        ok &= t > 0.5                                  # ignore self-hits at the eye
        if not ok.any(): continue
        j = np.argmin(np.where(ok, t, np.inf))
        out[i] = 1 if isglaze[j] else 2
    return out


# --- direction grid: azimuth 0 = straight ahead (-x), positive to the right ---
AZ = np.arange(-180, 180, 3.0)
EL = np.arange(-84, 85, 3.0)
A, E = np.meshgrid(AZ, EL)
ca, sa = np.cos(np.radians(A)), np.sin(np.radians(A))
ce, se = np.cos(np.radians(E)), np.sin(np.radians(E))
D = np.stack([-ca*ce, sa*ce, se], axis=-1).reshape(-1, 3)
isglaze = GLZ["H"]; RH = cast(D).reshape(A.shape)
isglaze = GLZ["G"]; RG = cast(D).reshape(A.shape)
isglaze = GLZ["H"]; R = RH
W = ce                                         # solid-angle weight, cos(elevation)

fwd = np.abs(A) <= 90
side = (np.abs(A) > 45) & (np.abs(A) <= 135)
down = (E < 0) & (np.abs(A) <= 90)
print("=== 1. HOW MUCH OF THE VIEW GETS OUT ===")
print("  Solid-angle weighted, from the pilot's eye. 'sees out' = the ray")
print("  leaves the aircraft, through glazing or through nothing at all.")
print(f"  {'sector':28s}{'rev G':>9s}{'rev H':>9s}{'change':>10s}")
for msk, lab in ((np.ones_like(R, bool), "whole sphere"),
                 (fwd, "forward hemisphere"),
                 (down, "forward and below"),
                 (side, "abeam, both sides"),
                 ((np.abs(A) <= 30) & (E < 0), "ahead and down, +/-30 deg"),
                 ((np.abs(A) <= 60) & (E < -3) & (E > -25), "the approach window")):
    tot = W[msk].sum()
    g = W[msk & (RG != 2)].sum()/tot
    h = W[msk & (RH != 2)].sum()/tot
    print(f"  {lab:28s}{g:8.1%}{h:9.1%}{h-g:+10.1%}")

# --- 2. the angles that matter on approach --------------------------------
print()
print("=== 2. HOW FAR DOWN YOU CAN SEE, BY AZIMUTH ===")


def limit(az, which="H", lo=-85.0, hi=12.0, step=1.0, fan=6.0, thresh=0.5):
    """Walk down from +12 deg and return the elevation at which the view shuts.

    Not a single ray: a 3/8 in frame tube at arm's length subtends about a
    degree, so a single-ray test calls every panel joint a wall. Instead take
    a +/-6 deg fan of 9 rays at each elevation and call the view open while
    at least half of the fan gets out - a pilot looks past a tube, not at it."""
    global isglaze
    isglaze = GLZ[which]
    els = np.arange(hi, lo, -step)
    azs = az + np.linspace(-fan, fan, 9)
    E2_, A2_ = np.meshgrid(els, azs, indexing="ij")
    ce2, se2 = np.cos(np.radians(E2_)), np.sin(np.radians(E2_))
    caz, saz = np.cos(np.radians(A2_)), np.sin(np.radians(A2_))
    d = np.stack([-caz*ce2, saz*ce2, se2], axis=-1).reshape(-1, 3)
    open_ = (cast(d) != 2).reshape(E2_.shape).mean(axis=1)
    for k in range(len(els)-1):
        if open_[k] < thresh and open_[k+1] < thresh:
            return els[k]
    return lo


print(f"  {'azimuth':26s}{'rev G':>10s}{'rev H':>10s}")
for az, what in ((0, "straight ahead"), (10, "10 deg off the nose"),
                 (20, "20 deg off the nose"), (30, "30 deg off the nose"),
                 (45, "45 deg off the nose"), (60, "60 deg, over the sill"),
                 (90, "abeam")):
    g, h = limit(az, "G"), limit(az, "H")
    fg = "blocked at horizon" if g >= 0 else f"{g:.0f} deg"
    fh = "blocked at horizon" if h >= 0 else f"{h:.0f} deg"
    print(f"  {what:26s}{fg:>10s}{fh:>10s}")
isglaze = GLZ["H"]

GS = 5.0
print("""
  On a 5 deg approach the aiming point sits 5 deg below the horizon.
  Rev G could not see it anywhere inside 30 deg of the nose. Rev H sees it
  from about 20 deg outboard - which is where a pilot's eyes go in the flare
  anyway, because that is where the runway edge is.

  READ THE FIRST ROW HONESTLY: straight ahead, rev H is WORSE on paper.
  That is not a regression, it is a correction. Rev G's windshield started at
  sta 14, so it drew glass across sta 14-22 - which is where the ENGINE is.
  Rev G was crediting the pilot with a view straight through the powerplant.
  Rev H's cowl runs 2 to 22 and takes that fiction away. The straight-ahead
  view was never there; the model just stopped claiming it.""")

# --- 3. what the cowl costs, and why -----------------------------------------
print()
print("=== 3. THE COWL IS THE LIMIT, NOT THE GLAZING ===")
ca_, cb = GRP["cowl"]
cowl = V[F[ca_:cb]].reshape(-1, 3)
print(f"  cowl runs sta {cowl[:,0].min():.0f} to {cowl[:,0].max():.0f}, "
      f"crown z = {cowl[:,2].max():.1f}")
print(f"  eye at sta {EYE[0]:.0f}, z {EYE[2]:.1f}  ->  the crown sits "
      f"{cowl[:,2].max()-EYE[2]:.1f} in ABOVE the eye")
xc = cowl[np.argmax(cowl[:, 2]), 0]
ang = np.degrees(np.arctan2(cowl[:, 2].max()-EYE[2], EYE[0]-xc))
print(f"  so the pilot must look {ang:.1f} deg UP to clear the nose, and there")
print("  is no depression angle over the top of the cowl at all.")
print("""
  This is the finding. The thrustline is at z=40 because the propeller has to
  clear the ground (trades/landing-gear.md), the engine sits around it, and the
  cowl has to cover the engine - so the cowl crown lands within a couple of
  inches of eye level no matter what the glazing does. Glass cannot fix it:
  there is an ENGINE in the way, not a fairing.

  What rev H does fix is everything either side of that: the whole forward
  section, down to the cage's lower longeron, is now transparent, so the
  aiming point, the runway edge and the flare picture come in over the SIDE
  of the cowl rather than over the top of it. That is the same technique a
  Cub pilot uses, except here it does not need an S-turn because the view is
  glazed continuously from the centreline round to the door.

  AND THE COWL MAY NOT EVEN BE TALL ENOUGH. A crown at z=47.3 allows the
  engine 7.3 in above the crank centreline. A Hirth F-33's cylinder standing
  upright is taller than that. So either the engine gets clocked or tilted to
  fit under this line, or the cowl grows - and if it grows, the over-the-nose
  view gets WORSE, not better. Nothing here is settled until an engine is on
  the bench and measured. This is now the open item that decides the forward
  view, and it is a powerplant question, not a glazing one.""")

# --- 4. glazed area, straight off the mesh ----------------------------------
print()
print("=== 4. GLAZED AREA, MEASURED OFF THE MESH ===")


def area(gname):
    a, b = GRP[gname]
    p = V[F[a:b]]
    return 0.5*np.linalg.norm(np.cross(p[:, 1]-p[:, 0], p[:, 2]-p[:, 0]),
                              axis=1).sum()/144.0


A_GL, A_FI = area("glass"), area("film")
RHO_PC, RHO_PVC = 0.0433, 0.047        # lb/in^3
w_gl = 0.040*RHO_PC*144.0*A_GL
w_fi = 0.020*RHO_PVC*144.0*A_FI
print(f"  glass (0.040 Lexan)   {A_GL:6.1f} ft^2   {w_gl:5.2f} lb")
print(f"  film  (20 mil PVC)    {A_FI:6.1f} ft^2   {w_fi:5.2f} lb")
print(f"  cowl                  {area('cowl'):6.1f} ft^2")
print(f"  rev G glazing was 12.0 + 10.0 ft^2 at 3.0 + 1.4 = 4.3 lb")
print(f"  rev H glazing is  {A_GL:.1f} + {A_FI:.1f} ft^2 at "
      f"{w_gl:.1f} + {w_fi:.1f} = {w_gl+w_fi:.1f} lb   "
      f"(delta {w_gl+w_fi-4.3:+.1f} lb)")

# frame: measure the tube actually drawn, then weigh it as 3/8 x .028 4130
fa, fb = GRP["wsframe"]
p = V[F[fa:fb]]
tube_area = 0.5*np.linalg.norm(np.cross(p[:, 1]-p[:, 0], p[:, 2]-p[:, 0]),
                               axis=1).sum()
L = tube_area/(2*np.pi*0.28)            # lateral area / circumference
A_T = np.pi*(0.375-0.028)*0.028
w_fr = L*A_T*0.283
print(f"\n  glazing frame drawn: {L:.0f} in of tube")
print(f"  as 3/8 x .028 4130 ({A_T:.4f} in^2): {w_fr:.2f} lb, "
      f"against 1.0 lb carried in the ledger  (delta {w_fr-1.0:+.2f} lb)")

D_GL = w_gl + w_fi + w_fr - (4.3 + 1.0)
print(f"\n  TOTAL rev H enclosure delta: {D_GL:+.1f} lb")

# --- 5. what it does to the two aircraft ------------------------------------
print()
print("=== 5. THE FLEET LEDGER ===")
KIT_G, MARGIN_G = 12.4, 6.3            # rev G enclosure kit, 103 airframe margin
print(f"  rev G enclosure kit gross      {KIT_G:5.1f} lb")
print(f"  rev H enclosure kit gross      {KIT_G + D_GL:5.1f} lb")
print(f"  103 airframe margin (rev G)    {MARGIN_G:5.1f} lb")
print()
print("  103 with windshield and vents, no doors:")
for lab, w in (("rev G, 0.040 Lexan screen", 5.0),
               ("rev G, film screen", 3.1)):
    print(f"    {lab:32s} 247.7 + {w:4.1f} = {247.7+w:6.1f}  "
          f"margin {254.0-247.7-w:+5.1f}")
# rev H screen: the whole forward section, so the 103 pays the full glass bill
w_h_lex = w_gl + w_fr + 1.0            # glass + frame + vents/defog
w_h_film = 0.020*RHO_PVC*144.0*A_GL + w_fr + 1.0
for lab, w in (("rev H, 0.040 Lexan screen", w_h_lex),
               ("rev H, 20 mil film screen", w_h_film)):
    print(f"    {lab:32s} 247.7 + {w:4.1f} = {247.7+w:6.1f}  "
          f"margin {254.0-247.7-w:+5.1f}")
print("""
  Read that honestly: the full-glass nose is affordable on the EAB and it is
  NOT free on the 103. The 103 keeps the same cage, the same frame and the same
  bead track - it just gets film in it instead of Lexan, which is the answer
  §24 already reached for a different reason. If the 103 wants the Lexan
  screen, the weight has to come from somewhere else on that airframe.""")

# --- chart ------------------------------------------------------------------
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
fig, ax = plt.subplots(figsize=(13, 5.6))
cmap = ListedColormap([(0.62, 0.80, 0.95), (0.78, 0.90, 0.72), (0.42, 0.44, 0.47)])
ax.pcolormesh(AZ, EL, RH, cmap=cmap, vmin=-0.5, vmax=2.5, shading="nearest")
ax.axhline(0, color="k", lw=0.8, alpha=0.6)
ax.axhline(-GS, color="#b03020", lw=1.4, ls="--")
ax.text(-176, -GS-4.5, "5° approach path — the aiming point lives on this line",
        color="#b03020", fontsize=9)
ax.axvline(0, color="k", lw=0.6, alpha=0.4)
ax.set_xticks(np.arange(-180, 181, 30))
ax.set_yticks(np.arange(-80, 81, 20))
ax.set_xlabel("azimuth from the nose, deg  (negative = left, ±180 = dead astern)")
ax.set_ylabel("elevation, deg")
ax.set_title("Nuthatch rev H — pilot's field of view from the design mesh\n"
             "blue = clear · green = through glazing · grey = blocked",
             fontsize=12)
for lab, x, y in (("cowl / engine", 0, -22), ("wing overhead", 0, 66),
                  ("door film", 100, -6), ("boom and tail", 165, 2),
                  ("floor", 0, -70)):
    ax.annotate(lab, (x, y), color="white", fontsize=9, ha="center", va="center")
fig.tight_layout()
os.makedirs("drawings", exist_ok=True)
fig.savefig("drawings/visibility.png", dpi=140)
print("\nwrote drawings/visibility.png")
