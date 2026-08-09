#!/usr/bin/env python3
"""Generate the Nuthatch 3D mesh, rev G: enclosed reclined cabin (welded 4130
cage, wing lowered onto the cabin roof, doors both sides, 3.5-in steel boom),
raked nose leg with 20-in bike wheel just aft of the prop, trailing-arm
mains, MTB coil-overs, 29-in bicycle mains.
Outputs: model/nuthatch.stl (binary, inches), drawings/general-arrangement.png,
and a JSON mesh (with material groups) for the interactive viewer / renderer.
Axes: X aft from prop plane (station, in), Y right, Z up. Ground at z=0.
"""
import numpy as np, struct, json, os, sys

def naca4(m, p, t, n=40):
    x = 0.5 * (1 - np.cos(np.linspace(0, np.pi, n)))
    yt = 5*t*(0.2969*np.sqrt(x) - 0.1260*x - 0.3516*x**2 + 0.2843*x**3 - 0.1036*x**4)
    yc = np.where(x < p, m/p**2*(2*p*x - x**2), m/(1-p)**2*((1-2*p) + 2*p*x - x**2)) if p > 0 else 0*x
    dyc = np.where(x < p, 2*m/p**2*(p-x), 2*m/(1-p)**2*(p-x)) if p > 0 else 0*x
    th = np.arctan(dyc)
    xu, zu = x - yt*np.sin(th), yc + yt*np.cos(th)
    xl, zl = x + yt*np.sin(th), yc - yt*np.cos(th)
    return np.concatenate([xu[::-1], xl[1:]]), np.concatenate([zu[::-1], zl[1:]])

V, F, GROUPS = [], [], []
def group(name): GROUPS.append([name, len(F), len(F)])
def endgroup(): GROUPS[-1][2] = len(F)

def add_loft(sections):
    base = len(V); n = len(sections[0])
    for s in sections: V.extend(s.tolist())
    for i in range(len(sections)-1):
        for j in range(n-1):
            a, b = base+i*n+j, base+i*n+j+1
            c, d = base+(i+1)*n+j, base+(i+1)*n+j+1
            F.append((a, c, b)); F.append((b, c, d))

def wing_section(y, z0, chord, le_x, twist_deg, xf, zf):
    tw = np.radians(twist_deg)
    xq = le_x + 0.25*chord
    xr = xf*chord; zr = zf*chord
    xx = xq + (xr-0.25*chord)*np.cos(tw) + zr*np.sin(tw)
    zz = z0 - (xr-0.25*chord)*np.sin(tw) + zr*np.cos(tw)
    return np.stack([xx, np.full_like(xx, y), zz], axis=1)

def strut(p1, p2, r=1.0):
    a = np.linspace(0, 2*np.pi, 9)
    d = np.array(p2, float)-np.array(p1, float); d = d/np.linalg.norm(d)
    u = np.cross(d, [1, 0, 0])
    if np.linalg.norm(u) < 1e-6: u = np.cross(d, [0, 1, 0])
    u /= np.linalg.norm(u); v = np.cross(d, u)
    s1 = np.array([np.array(p1)+r*np.cos(t)*u+r*np.sin(t)*v for t in a])
    s2 = np.array([np.array(p2)+r*np.cos(t)*u+r*np.sin(t)*v for t in a])
    add_loft([s1, s2])

def wheel(x, y, r=6.5, w=3.0):
    a = np.linspace(0, 2*np.pi, 17)
    s1 = np.stack([x + r*np.cos(a), np.full_like(a, y-w/2), r + r*np.sin(a)], axis=1)
    s2 = s1.copy(); s2[:, 1] = y + w/2
    add_loft([s1, s2])

def bike_wheel(x0, y0, R=14.5, rt=1.2, spokes=14):
    """29er: torus tire + spokes + hub. Axle at (x0, y0, R)."""
    secs = []
    for a in np.linspace(0, 2*np.pi, 25):
        b = np.linspace(0, 2*np.pi, 9)
        secs.append(np.stack([x0+((R-rt)+rt*np.cos(b))*np.cos(a),
                              y0+rt*np.sin(b),
                              R+((R-rt)+rt*np.sin(0))*0+((R-rt)+rt*np.cos(b))*np.sin(a)], axis=1))
    # fix: proper torus z
    secs = []
    for a in np.linspace(0, 2*np.pi, 25):
        b = np.linspace(0, 2*np.pi, 9)
        rc = (R-rt) + rt*np.cos(b)
        secs.append(np.stack([x0+rc*np.cos(a), y0+rt*np.sin(b), R+rc*np.sin(a)], axis=1))
    add_loft(secs)
    for k in range(spokes):
        a = 2*np.pi*k/spokes
        strut([x0, y0, R], [x0+(R-rt)*np.cos(a), y0, R+(R-rt)*np.sin(a)], 0.12)
    strut([x0, y0-1.6, R], [x0, y0+1.6, R], 1.0)   # hub

# ---- wing: 31 ft, 50 in chord, LE sta 48, dihedral 5, washout 2.5, incidence 2
xf, zf = naca4(0.04, 0.4, 0.12)
CH = 50.0; LE = 48.0; Z0 = 58.0   # rev G: wing lowered onto the cabin roof
DIH = np.radians(5.0)
group("wing")
for side in (+1, -1):
    secs = []
    for eta in np.linspace(0, 1, 9):
        y = side*186.0*eta*np.cos(DIH)
        z = Z0 + 186.0*eta*np.sin(DIH)
        secs.append(wing_section(y, z, CH, LE, 2.0-2.5*eta, xf, zf))
    add_loft(secs)
endgroup()
# ---- tail
xt, zt = naca4(0, 0, 0.09)
hc = 30.0/10*12
group("tail")
for side in (+1, -1):
    secs = [wing_section(side*60*eta, 27.0, hc*(1-0.15*eta), 182+0.15*hc*eta, -1.5, xt, zt)
            for eta in np.linspace(0, 1, 3)]
    add_loft(secs)
vc = 15.0/5*12
secs = []
for eta in np.linspace(0, 1, 3):
    ch = vc*(1-0.4*eta); lex = 182-0.3*vc+(0.55*vc)*eta
    secs.append(np.stack([lex+xt*ch, zt*ch, np.full_like(xt, 27.0+60*eta)], axis=1))
add_loft(secs)
endgroup()
# ---- fuselage: fabric pod faired over the welded 4130 cage to sta 96, then a
# single straight 3.50-in steel boom at z=27 (trades/cockpit-cage.md).
# Max section at sta ~56 (pilot shoulders), smooth run-out into the boom.
group("fuse")
# (station, z-centre, half-height, half-width). Upper line sweeps from the
# spinner up to the wing underside (z=55) at the LE and runs aft under the
# wing root; belly held at ~16. Enclosed cabin, doors in the sides.
fu = [(2,40,3.5,3.5),(12,33,11,6),(24,33,15,9),(36,34.5,18.5,10.8),
      (48,35.5,19.5,11.5),(60,36,19,11.5),(72,36,18,10.5),
      (84,33,12,7),(96,27.5,3.5,3.2),(184,27,1.75,1.75)]
th = np.linspace(0, 2*np.pi, 17)
add_loft([np.stack([np.full_like(th, x), w*np.sin(th), z+h*np.cos(th)], axis=1)
          for x, z, h, w in fu])
endgroup()
# ---- propeller: two blades + spinner at sta 2, thrustline 40
group("prop")
for a0 in (np.radians(80), np.radians(260)):
    ca, sa = np.cos(a0), np.sin(a0)
    bs = []
    for t in np.linspace(0.12, 1, 5):
        rr = 30*t; chb = 4.2-2.0*t
        c = np.linspace(-chb/2, chb/2, 7)
        bs.append(np.stack([2.0+c*0.35, rr*ca - c*0.55*sa, 40+rr*sa + c*0.55*ca], axis=1))
    add_loft(bs)
strut([0, 0, 40], [5, 0, 40], 2.2)   # spinner/hub
endgroup()
# ---- gear: raked nose leg (rev D, wheel just aft of prop), trailing arms, bike mains
group("tire_n")
bike_wheel(15, 0, R=10, rt=1.2, spokes=12)
endgroup()
group("gear")
strut([30, 0, 17], [15, 0, 10], 1.0)      # raked member, ~63 deg
strut([14, 0, 30], [15.5, 0, 10.5], 0.9)  # closes the crush-bay triangle
for sgn in (1, -1):
    strut([58, sgn*10, 17], [70.5, sgn*28, 14.5], 1.1)   # trailing arm
    strut([70.5, sgn*28, 14.5], [64, sgn*14, 30], 0.7)   # MTB coil-over
endgroup()
group("wheel_m")
bike_wheel(70.5, 28); bike_wheel(70.5, -28)
endgroup()
group("struts")
strut([182, 0, 26], [185, 0, 22], 0.8)          # tail skid
endgroup()

# ---- welded 4130 cockpit cage, sta 30 to 96 (trades/cockpit-cage.md).
# Main hoop at sta 61.5 is the rollover structure AND the front-spar
# carry-through AND sits at the CG (sta 63) - one frame, three jobs.
group("cage")
LON_R = 0.5
FS, RS, AFT = 61.5, 80.5, 96.0
WING_PU = 55.0            # wing underside = cabin roof = spar pickup
for s in (1, -1):
    strut([30, s*9, 18], [96, s*6, 24], LON_R)          # lower longeron
    strut([30, s*8, 38], [96, s*6, 30], LON_R)          # upper longeron
    strut([30, s*9, 18], [30, s*8, 38], LON_R)          # nose-bow post
    strut([30, s*9, 18], [FS, s*9.5, 38], 0.4)          # fwd side diagonal
    strut([FS, s*9.3, 18], [AFT, s*6, 30], 0.4)         # aft side diagonal
    # main hoop: lower longeron -> shoulder -> wing front-spar pickup at the
    # cabin roof (z=53). No cabane: the wing sits on the cabin.
    strut([FS, s*9.5, 18], [FS, s*9.5, 40], 0.55)
    strut([FS, s*9.5, 40], [FS, s*8.0, WING_PU], 0.55)
    # rear-spar frame, also the seat-back / harness anchor frame
    strut([RS, s*7.5, 20], [RS, s*8.0, WING_PU], 0.45)
    strut([AFT, s*6, 24], [AFT, s*6, 30], 0.45)         # aft frame post
strut([30, -8, 38], [30, 8, 38], 0.45)                  # nose-bow crown
strut([FS, -8, WING_PU], [FS, 8, WING_PU], 0.6)         # FRONT SPAR carry-through
strut([RS, -8, WING_PU], [RS, 8, WING_PU], 0.5)         # REAR SPAR carry-through
strut([FS, -9.5, 40], [FS, 9.5, 40], 0.45)              # hoop shoulder cross
strut([AFT, -6, 24], [AFT, 6, 24], 0.45)                # aft frame, boom pickup
strut([AFT, -6, 30], [AFT, 6, 30], 0.45)
endgroup()

# ---- door frames (EAB enclosure kit; the cage hard points are permanent)
group("doors")
D_F, D_A, D_LO, D_HI = 40.0, 78.0, 27.0, 51.0
for s2 in (1, -1):
    y = s2*11.3
    strut([D_F, y, D_LO], [D_A, y, D_LO], 0.3)      # sill
    strut([D_F, y, D_HI], [D_A, y, D_HI], 0.3)      # header
    strut([D_F, y, D_LO], [D_F, y, D_HI], 0.3)      # fwd post
    strut([D_A, y, D_LO], [D_A, y, D_HI], 0.3)      # aft post
endgroup()

V = np.array(V); F = np.array(F, dtype=np.int64)
print(f"mesh: {len(V)} vertices, {len(F)} triangles, groups: {[g[0] for g in GROUPS]}")

os.makedirs("model", exist_ok=True)
with open("model/nuthatch.stl", "wb") as f:
    f.write(b"Nuthatch rev G, inches".ljust(80, b"\0"))
    f.write(struct.pack("<I", len(F)))
    for tri in F:
        p = V[tri]
        n = np.cross(p[1]-p[0], p[2]-p[0]); ln = np.linalg.norm(n)
        n = n/ln if ln > 0 else n
        f.write(struct.pack("<3f", *n))
        for pt in p: f.write(struct.pack("<3f", *pt))
        f.write(struct.pack("<H", 0))
print("wrote model/nuthatch.stl (%.0f KB)" % (os.path.getsize("model/nuthatch.stl")/1024))

out = {"v": np.round(V, 1).tolist(), "f": F.tolist(), "groups": GROUPS}
sp = sys.argv[1] if len(sys.argv) > 1 else "."
json.dump(out, open(os.path.join(sp, "nuthatch-mesh.json"), "w"))
print("wrote mesh json")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig, axs = plt.subplots(2, 2, figsize=(13, 8.5))
views = [("Top", 0, 1), ("Side", 0, 2), ("Front", 1, 2)]
for ax, (name, i, j) in zip([axs[0][0], axs[1][0], axs[1][1]], views):
    for tri in F:
        p = V[tri]
        ax.fill(p[:, i], p[:, j], facecolor="#d7dde4", edgecolor="#8494a6", lw=0.12)
    ax.set_aspect("equal"); ax.set_title(name+" view", fontsize=11)
    ax.grid(True, lw=0.3, alpha=0.5)
ax = axs[0][1]
c, s = np.cos(np.radians(-35)), np.sin(np.radians(-35))
c2, s2 = np.cos(np.radians(22)), np.sin(np.radians(22))
Vx = V[:, 0]*c + V[:, 1]*s
Vy2 = (-V[:, 0]*s + V[:, 1]*c)*s2 + V[:, 2]*c2
order = np.argsort([np.mean((-V[t, 0]*s+V[t, 1]*c)*c2 - V[t, 2]*s2) for t in F])
for k in order:
    p = F[k]
    ax.fill(Vx[p], Vy2[p], facecolor="#e3e8ee", edgecolor="#8494a6", lw=0.1)
ax.set_aspect("equal"); ax.set_title("Isometric", fontsize=11); ax.axis("off")
fig.suptitle("Nuthatch — general arrangement rev G (enclosed reclined cabin, wing on the roof)", fontsize=12)
fig.tight_layout()
os.makedirs("drawings", exist_ok=True)
fig.savefig("drawings/general-arrangement.png", dpi=140)
print("wrote drawings/general-arrangement.png")
