#!/usr/bin/env python3
"""Generate the Nuthatch 3D mesh from the repo's dimensions.
Outputs: model/nuthatch.stl (binary, inches), drawings/general-arrangement.png,
and a JSON mesh for the interactive viewer. Pure numpy - no CAD kernel needed.
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

V, F = [], []
def add_loft(sections):
    """sections: list of (N,3) arrays with identical N; skins between them."""
    base = len(V)
    n = len(sections[0])
    for s in sections: V.extend(s.tolist())
    for i in range(len(sections)-1):
        for j in range(n-1):
            a, b = base+i*n+j, base+i*n+j+1
            c, d = base+(i+1)*n+j, base+(i+1)*n+j+1
            F.append((a, c, b)); F.append((b, c, d))

def wing_section(y, z0, chord, le_x, twist_deg, xf, zf):
    tw = np.radians(twist_deg)
    xr = xf*chord; zr = zf*chord
    x = le_x + xr*np.cos(tw) + zr*np.sin(tw)
    z = z0 - xr*np.sin(tw)*0 + zr*np.cos(tw) - np.sin(tw)*(xr-0.25*chord)*0
    # rotate about quarter chord
    xq = le_x + 0.25*chord
    xx = xq + (xr-0.25*chord)*np.cos(tw) + zr*np.sin(tw)
    zz = z0 - (xr-0.25*chord)*np.sin(tw) + zr*np.cos(tw)
    return np.stack([xx, np.full_like(xx, y), zz], axis=1)

# ---- wing: 31 ft, 50 in chord, LE sta 48, dihedral 5, washout 2.5, incidence 2
xf, zf = naca4(0.04, 0.4, 0.12)
CH = 50.0; LE = 48.0; Z0 = 78.0   # wing root height above ground
DIH = np.radians(5.0)
for side in (+1, -1):
    secs = []
    for eta in np.linspace(0, 1, 9):
        y = side*186.0*eta*np.cos(DIH)
        z = Z0 + 186.0*eta*np.sin(DIH)
        tw = 2.0 - 2.5*eta
        secs.append(wing_section(y, z, CH, LE, tw, xf, zf))
    add_loft(secs)
# ---- horizontal tail: 30 ft2, 10 ft span, sta 182
xt, zt = naca4(0, 0, 0.09)
hc = 30.0/10*12
for side in (+1, -1):
    secs = [wing_section(side*60*eta, 40.0, hc*(1-0.15*eta), 182+0.15*hc*eta, -1.5, xt, zt)
            for eta in np.linspace(0, 1, 3)]
    add_loft(secs)
# ---- vertical tail: 15 ft2, 5 ft tall
vc = 15.0/5*12
secs = []
for eta in np.linspace(0, 1, 3):
    ch = vc*(1-0.4*eta)
    lex = 182 - 0.3*vc + (0.55*vc)*eta
    pts = np.stack([lex + xt*ch, zt*ch, np.full_like(xt, 40.0+60*eta)], axis=1)
    secs.append(pts)
add_loft(secs)
# ---- fuselage pod + boom (station, z-center above ground, half-height, half-width)
fu = [(4,52,3,3),(14,52,8,7),(30,54,12,10),(48,56,14,11),(62,54,14,11),
      (80,52,12,10),(100,52,9,7),(125,48,6,4.5),(150,44,4,3),(170,42,3,2.2),(184,40,2.5,2)]
th = np.linspace(0, 2*np.pi, 17)
secs = [np.stack([np.full_like(th, x), w*np.sin(th), z + h*np.cos(th)], axis=1)
        for x, z, h, w in fu]
add_loft(secs)
# ---- prop disc ring at sta 2 (60 in) + spinner
th2 = np.linspace(0, 2*np.pi, 33)
ring = [np.stack([np.full_like(th2, 2.0), r*np.sin(th2), 52 + r*np.cos(th2)], axis=1)
        for r in (29.5, 30.0)]
add_loft(ring)
# ---- gear: nose sta 34, mains sta 78; 5.00-5 tires ~ 13 in dia
def wheel(x, y, r=6.5, w=3.0):
    a = np.linspace(0, 2*np.pi, 17)
    s1 = np.stack([x + r*np.cos(a), np.full_like(a, y-w/2), r + r*np.sin(a)], axis=1)
    s2 = s1.copy(); s2[:,1] = y + w/2
    add_loft([s1, s2])
wheel(34, 0); wheel(78, 24); wheel(78, -24)
def strut(p1, p2, r=1.0):
    a = np.linspace(0, 2*np.pi, 9)
    d = np.array(p2)-np.array(p1); d = d/np.linalg.norm(d)
    u = np.cross(d, [1,0,0]);  u = np.cross(d, [0,1,0]) if np.linalg.norm(u)<1e-6 else u
    u /= np.linalg.norm(u); v = np.cross(d, u)
    s1 = np.array([p1 + r*np.cos(t)*u + r*np.sin(t)*v for t in a])
    s2 = np.array([p2 + r*np.cos(t)*u + r*np.sin(t)*v for t in a])
    add_loft([s1, s2])
strut([34,0,42],[34,0,6],1.2); strut([70,0,46],[78,24,6],1.2); strut([70,0,46],[78,-24,6],1.2)
# cabane struts wing-to-fuselage
strut([55,10,66],[58,8,Z0],1.0); strut([55,-10,66],[58,-8,Z0],1.0)

V = np.array(V); F = np.array(F, dtype=np.int64)
print(f"mesh: {len(V)} vertices, {len(F)} triangles")

os.makedirs("model", exist_ok=True)
with open("model/nuthatch.stl", "wb") as f:
    f.write(b"Nuthatch general arrangement, inches".ljust(80, b"\0"))
    f.write(struct.pack("<I", len(F)))
    for tri in F:
        p = V[tri]
        n = np.cross(p[1]-p[0], p[2]-p[0]); ln = np.linalg.norm(n)
        n = n/ln if ln > 0 else n
        f.write(struct.pack("<3f", *n))
        for pt in p: f.write(struct.pack("<3f", *pt))
        f.write(struct.pack("<H", 0))
print("wrote model/nuthatch.stl (%.0f KB)" % (os.path.getsize("model/nuthatch.stl")/1024))

# JSON for the viewer (decimated floats)
out = {"v": np.round(V, 1).tolist(), "f": F.tolist()}
sp = sys.argv[1] if len(sys.argv) > 1 else "."
json.dump(out, open(os.path.join(sp, "nuthatch-mesh.json"), "w"))
print("wrote mesh json")

# ---- three-view
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig, axs = plt.subplots(2, 2, figsize=(13, 8.5))
views = [("Top", 0, 1, 1), ("Side", 0, 2, 0), ("Front", 1, 2, 2)]
for ax, (name, i, j, _) in zip([axs[0][0], axs[1][0], axs[1][1]], views):
    for tri in F[::1]:
        p = V[tri]
        ax.fill(p[:, i], p[:, j], facecolor="#d7dde4", edgecolor="#8494a6", lw=0.15)
    ax.set_aspect("equal"); ax.set_title(name + " view", fontsize=11)
    ax.set_axisbelow(True); ax.grid(True, lw=0.3, alpha=0.5)
ax = axs[0][1]
c, s = np.cos(np.radians(-35)), np.sin(np.radians(-35))
c2, s2 = np.cos(np.radians(22)), np.sin(np.radians(22))
Vx = V[:, 0]*c + V[:, 1]*s
Vy2 = (-V[:, 0]*s + V[:, 1]*c)*s2 + V[:, 2]*c2
order = np.argsort([np.mean((-V[t, 0]*s + V[t, 1]*c)*c2 - V[t, 2]*s2) for t in F])
for k in order:
    p = F[k]
    ax.fill(Vx[p], Vy2[p], facecolor="#e3e8ee", edgecolor="#8494a6", lw=0.1)
ax.set_aspect("equal"); ax.set_title("Isometric", fontsize=11); ax.axis("off")
fig.suptitle("Nuthatch — general arrangement (dimensions from weight sheet; airfoil candidate NACA 4412)", fontsize=12)
fig.tight_layout()
os.makedirs("drawings", exist_ok=True)
fig.savefig("drawings/general-arrangement.png", dpi=140)
print("wrote drawings/general-arrangement.png")
