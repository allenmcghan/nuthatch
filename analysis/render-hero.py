#!/usr/bin/env python3
"""Photographic-style renderings of the Nuthatch rev G airframe.

These are RENDERINGS OF THE DESIGN MESH, not photographs. Nothing here has been
built. The renderer shades the same triangles `geometry-mesh.py` writes to
`model/nuthatch.stl`, with a physically-motivated (not physically correct)
shading model:

  - Lambert diffuse + Blinn-Phong specular per material
  - sky-dome ambient from above, warm ground bounce from below
  - Fresnel-weighted transparency on the glazing, so the 0.040 Lexan windshield
    and the 20 mil film doors go white at grazing angles and clear when you look
    straight through them - which is what makes the cage and the pilot visible
  - painter-sorted triangles with depth cueing, so the far wall of the pod reads
    darker than the near wall
  - fabric cues: rib scalloping on the wing and tail at the true 11 in rib pitch,
    light panel/stitch modulation on the pod. These are SHADING, not geometry -
    the mesh has no ribs in it
  - projected soft shadow (three offset passes) plus contact occlusion
  - photographic post: bloom, vignette, tone curve, grain

The pilot figure is built here rather than in `geometry-mesh.py` on purpose: he
is a rendering prop and has no business in the STL or on the drawings.

Outputs drawings/renders/hero-{ramp,cockpit,air}.png
"""
import json, os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Ellipse, Rectangle
from matplotlib.collections import PolyCollection
from scipy.ndimage import gaussian_filter
from PIL import Image, ImageDraw

SP = sys.argv[1] if len(sys.argv) > 1 else "."
m = json.load(open(os.path.join(SP, "nuthatch-mesh.json")))
V0 = np.array(m["v"], float)                    # inches, x aft, y right, z up
F = [tuple(t) for t in m["f"]]
GROUPS = [list(g) for g in m["groups"]]

# ---------------------------------------------------------------- pilot prop
Vp = V0.tolist()
def _loft(secs):
    b = len(Vp); n = len(secs[0])
    for s in secs: Vp.extend(np.asarray(s).tolist())
    for i in range(len(secs)-1):
        for j in range(n-1):
            a, bb = b+i*n+j, b+i*n+j+1
            c, d = b+(i+1)*n+j, b+(i+1)*n+j+1
            F.append((a, c, bb)); F.append((bb, c, d))

def _strut(p1, p2, r, n=12):
    a = np.linspace(0, 2*np.pi, n)
    d = np.array(p2, float) - np.array(p1, float); d /= np.linalg.norm(d)
    u = np.cross(d, [1, 0, 0])
    if np.linalg.norm(u) < 1e-6: u = np.cross(d, [0, 1, 0])
    u /= np.linalg.norm(u); v = np.cross(d, u)
    _loft([np.array([np.array(p, float) + r*np.cos(t)*u + r*np.sin(t)*v for t in a])
           for p in (p1, p2)])

def _sphere(c, r, n=16):
    _loft([np.stack([c[0] + r*np.sin(t)*np.cos(np.linspace(0, 2*np.pi, n)),
                     c[1] + r*np.sin(t)*np.sin(np.linspace(0, 2*np.pi, n)),
                     np.full(n, c[2] + r*np.cos(t))], axis=1)
           for t in np.linspace(0.001, np.pi-0.001, n)])

def _grp(name, fn):
    a = len(F); fn(); GROUPS.append([name, a, len(F)])

# Reclined ~35 deg: hips sta 48 / z 27, shoulders 57 / 41.5, head just forward of
# the sta 61.5 rollover hoop, legs running forward into the footwell that §18
# emptied when the rudder pedals went away.
def _body():
    _strut((48, 0, 27), (57, 0, 41.5), 6.0)             # torso
    _strut((57, 0, 41.5), (59, 0, 43.0), 2.6)           # neck
    for s in (1, -1):
        _strut((48, s*4.5, 27), (37, s*5.0, 24.5), 3.4)     # thigh
        _strut((37, s*5.0, 24.5), (30, s*5.0, 20), 2.4)     # shin
        _strut((30, s*5.0, 20), (26.5, s*5.0, 19.5), 2.3)   # foot
        _strut((56, s*6.5, 40), (52, s*7.0, 32), 2.2)       # upper arm
        _strut((52, s*7.0, 32), (49, s*2.5, 30), 1.9)       # forearm
    _strut((49, 0, 30), (49, 0, 21), 0.6)               # stick
_grp("pilot", _body)
_grp("helmet", lambda: _sphere((60.0, 0, 45.0), 4.7))
V0 = np.array(Vp, float)
F = np.array(F, dtype=np.int64)
GIDX = {g[0]: (g[1], g[2]) for g in GROUPS}

# ------------------------------------------------------------------ materials
# rgb, alpha, ks (specular strength), shininess
MAT = {
 "wing":   ((0.930, 0.908, 0.842), 1.0, 0.11, 15),   # Oratex, cream
 "tail":   ((0.930, 0.908, 0.842), 1.0, 0.11, 15),
 "fuse":   ((0.900, 0.878, 0.818), 1.0, 0.13, 17),
 "boom":   ((0.735, 0.748, 0.756), 1.0, 0.36, 36),   # painted 4130 boom
 "glass":  ((0.520, 0.628, 0.700), 0.20, 1.00, 95),  # 0.040 Lexan windshield
 "film":   ((0.600, 0.660, 0.690), 0.26, 0.72, 44),  # 20 mil PVC door film
 "cage":   ((0.285, 0.310, 0.335), 1.0, 0.42, 30),   # welded 4130
 "doors":  ((0.315, 0.340, 0.365), 1.0, 0.42, 30),
 "wsframe":((0.355, 0.375, 0.395), 1.0, 0.46, 34),  # windshield channel
 "gear":   ((0.285, 0.315, 0.345), 1.0, 0.42, 30),
 "struts": ((0.285, 0.315, 0.345), 1.0, 0.42, 30),
 "prop":   ((0.300, 0.196, 0.112), 1.0, 0.30, 28),   # laminated birch/maple
 "tire_n": ((0.098, 0.098, 0.108), 1.0, 0.15, 12),
 "wheel_m":((0.098, 0.098, 0.108), 1.0, 0.15, 12),
 "pilot":  ((0.155, 0.190, 0.250), 1.0, 0.17, 16),
 "helmet": ((0.790, 0.235, 0.125), 1.0, 0.58, 48),
}
DEF = ((0.6, 0.6, 0.6), 1.0, 0.2, 20)
base = np.zeros((len(F), 3)); alpha = np.ones(len(F))
ks = np.zeros(len(F)); shin = np.full(len(F), 20.0)
for name, a, b in GROUPS:
    c, al, k, s = MAT.get(name, DEF)
    base[a:b] = c; alpha[a:b] = al; ks[a:b] = k; shin[a:b] = s

CEN = V0[F].mean(axis=1)
# --- paint scheme: rudder top, wingtips, spinner and a cheatline below the
# doors, all in one orange. Nothing structural, but a blank cream airframe
# reads as a CAD model rather than a finished aeroplane.
ORANGE = (0.790, 0.235, 0.125)
ta, tb = GIDX["tail"]
base[ta:tb][CEN[ta:tb, 2] > 62] = ORANGE
wa, wb = GIDX["wing"]
base[wa:wb][np.abs(CEN[wa:wb, 1]) > 168] = ORANGE
pa, pb = GIDX["prop"]                                          # spinner only:
r_hub = np.hypot(CEN[pa:pb, 1], CEN[pa:pb, 2]-40.0)            # the blades run
base[pa:pb][r_hub < 3.0] = (0.92, 0.90, 0.86)                  # through sta 2 too
# cheatline: constant-phi band on the pod, just below the door sill. phi is
# recovered from the same station table geometry-mesh.py lofts the pod on.
FU = np.array([[2, 40, 3.5, 3.5], [12, 33, 11, 6], [24, 33, 15, 9],
               [36, 34.5, 18.5, 10.8], [48, 35.5, 19.5, 11.5],
               [60, 36, 19, 11.5], [72, 36, 18, 10.5], [84, 33, 12, 7],
               [96, 27.5, 3.5, 3.2], [184, 27, 1.75, 1.75]])
fa, fb = GIDX["fuse"]
cx, cy, cz = CEN[fa:fb].T
_z = np.interp(cx, FU[:, 0], FU[:, 1]); _h = np.interp(cx, FU[:, 0], FU[:, 2])
_w = np.interp(cx, FU[:, 0], FU[:, 3])
phi_f = np.degrees(np.arctan2(np.abs(cy)/np.maximum(_w, 1e-6),
                              (cz-_z)/np.maximum(_h, 1e-6)))
band = base[fa:fb].copy()
band[(phi_f > 121) & (phi_f < 133) & (cx > 16) & (cx < 92)] = ORANGE
base[fa:fb] = band

# --- fabric cues (shading only) ---------------------------------------------
tex = np.ones(len(F))
for g in ("wing", "tail"):                       # rib scallop at 11 in pitch
    a, b = GIDX[g]
    s = CEN[a:b, 1] if g == "wing" else CEN[a:b, 1] + CEN[a:b, 2]
    tex[a:b] = 1.0 + 0.030*np.cos(2*np.pi*s/11.0) - 0.028*np.exp(
        -((np.abs(((s/11.0) % 1.0) - 0.5) - 0.5)/0.06)**2)
for g in ("fuse", "boom"):                       # panel joints and stitch lines
    a, b = GIDX[g]
    tex[a:b] = 1.0 + 0.020*np.cos(2*np.pi*CEN[a:b, 0]/12.0) \
                   + 0.014*np.cos(2*np.pi*CEN[a:b, 2]/9.0)
RNG = np.random.default_rng(11)
tex *= 1.0 + RNG.normal(0, 0.011, len(F))        # surface variation


def _rot(P, ang, i, j, ctr):
    """Rotate columns (i,j) of P by ang degrees about ctr."""
    c, s = np.cos(np.radians(ang)), np.sin(np.radians(ang))
    Q = P.copy(); u = P[:, i]-ctr[0]; v = P[:, j]-ctr[1]
    Q[:, i] = ctr[0] + c*u - s*v; Q[:, j] = ctr[1] + s*u + c*v
    return Q


def render(fname, cam, look, fov, sunaz, sunel, W=2400, H=1350, expo=1.0,
           bank=0.0, pitch=0.0, alt=0.0, prop_ang=0.0, spin=False,
           sky_top=(0.15, 0.32, 0.62), sky_hz=(0.74, 0.81, 0.87),
           gnear=(0.24, 0.31, 0.14), scene="ramp",
           grain=0.008, bloom=0.30, caption=""):
    V = V0.copy()
    if prop_ang:
        pa, pb = GIDX["prop"]
        idx = np.unique(F[pa:pb])
        V[idx] = _rot(V[idx], prop_ang, 1, 2, (0.0, 40.0))
    if pitch: V = _rot(V, pitch, 0, 2, (70.5, 14.5))
    if bank:  V = _rot(V, bank, 1, 2, (0.0, 30.0))
    V[:, 2] += alt

    cam = np.array(cam, float); look = np.array(look, float)
    sun = np.array([np.cos(np.radians(sunel))*np.cos(np.radians(sunaz)),
                    np.cos(np.radians(sunel))*np.sin(np.radians(sunaz)),
                    np.sin(np.radians(sunel))])
    fwd = look - cam; fwd /= np.linalg.norm(fwd)
    right = np.cross(fwd, [0, 0, 1]); right /= np.linalg.norm(right)
    up = np.cross(right, fwd)
    S = 1.0/np.tan(np.radians(fov)); AR = W/H

    def project(P):
        d = np.atleast_2d(P) - cam
        z = d @ fwd
        zz = np.where(np.abs(z) < 1e-6, 1e-6, z)
        return np.stack([S*(d @ right)/zz, S*(d @ up)/zz], axis=1), z

    fig = plt.figure(figsize=(W/100, H/100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1]); ax.axis("off")
    ax.set_xlim(-AR, AR); ax.set_ylim(-1, 1)
    st, sh_, gn = np.array(sky_top), np.array(sky_hz), np.array(gnear)

    # ---- sky -------------------------------------------------------------
    hpt, _ = project((cam + np.array([fwd[0], fwd[1], 0])*4.0e5)[None, :])
    hy = float(np.clip(hpt[0, 1], -0.98, 0.98))
    N = 150
    for i in range(N):
        t = (i/(N-1))**1.4
        y0 = 1.0 - (1.0-hy)*(i+1)/N
        ax.add_patch(Rectangle((-AR, y0), 2*AR, (1.0-hy)/N + 0.005,
                     fc=np.clip(st*(1-t) + sh_*t, 0, 1), ec="none", zorder=0))
    spt, sz = project((cam + sun*4.0e5)[None, :])
    if sz[0] > 0:
        for r, al in ((1.8, 0.13), (1.0, 0.14), (0.5, 0.17), (0.18, 0.30)):
            ax.add_patch(Ellipse(spt[0], r*AR, r, fc=(1.0, 0.965, 0.87, al),
                                 ec="none", zorder=0.4))
    # ---- clouds: fractal noise as its own layer, under everything solid ----
    ch_, cw_ = H//3, W//3
    fbm = np.zeros((ch_, cw_))
    for oct_, amp in ((34, 1.0), (17, 0.55), (8, 0.30), (3.5, 0.17)):
        fbm += amp*gaussian_filter(RNG.normal(0, 1, (ch_, cw_)), oct_)*oct_**0.85
    fbm = (fbm - fbm.mean())/(fbm.std() + 1e-9)
    hrow = (1-hy)/2*ch_
    rows = np.arange(ch_)[:, None]
    band = np.clip((rows - 0.02*ch_)/(max(hrow, 1) - 0.02*ch_), 0, 1)**1.6
    ca = np.clip((fbm - (1.30 - 1.00*band))*2.0, 0, 1) \
        * np.clip((hrow - rows)/(0.09*ch_), 0, 1)
    ca = gaussian_filter(ca, 1.6)
    if sz[0] > 0:
        sc = np.array([(spt[0, 0]/AR+1)/2*cw_, (1-spt[0, 1])/2*ch_])
    else:
        sc = np.array([cw_*0.5, -ch_])
    dsun = np.hypot(np.arange(cw_)[None, :]-sc[0], rows-sc[1])/(0.9*cw_)
    lit = np.clip(1.04 - 0.28*dsun, 0.70, 1.04)
    shade = 0.17*gaussian_filter(ca, 7)
    layer = np.zeros((ch_, cw_, 4))
    layer[..., 0] = np.clip(0.99*lit - shade, 0, 1)
    layer[..., 1] = np.clip(0.985*lit - shade, 0, 1)
    layer[..., 2] = np.clip(0.985*lit - 0.85*shade, 0, 1)
    layer[..., 3] = ca
    ax.imshow(layer, extent=(-AR, AR, -1, 1), origin="upper",
              interpolation="bilinear", zorder=0.6, aspect="auto")

    # ---- ground: screen-space base, so it can never leave a hole ----------
    NG = 170
    for i in range(NG):
        y1 = hy - (hy+1)*i/NG; y0 = hy - (hy+1)*(i+1)/NG
        w = (i/NG)**0.40
        ax.add_patch(Rectangle((-AR, y0), 2*AR, (y1-y0)+0.005,
                     fc=np.clip(sh_*(1-w) + gn*w, 0, 1), ec="none", zorder=0.9))

    def gq(x1, x2, y1, y2, col, z=1.0, zh=0.0):
        P = np.array([[x1, y1, zh], [x2, y1, zh], [x2, y2, zh], [x1, y2, zh]])
        pts, zz = project(P)
        if (zz > 24).all():
            ax.add_patch(Polygon(pts, fc=np.clip(col, 0, 1), ec="none", zorder=z))

    def hazed(col, dist, scale):
        t = np.clip(dist/scale, 0, 1)**0.6
        return np.array(col)*(1-t) + sh_*t

    if scene == "air":
        for fy in np.arange(-70000, 70000, 5200.0):        # field patchwork
            for fx in np.arange(-70000, 70000, 5200.0):
                d = np.hypot(fx-cam[0], fy-cam[1])
                if d > 130000: continue
                k = RNG.random()
                c = ((0.22, 0.30, 0.13) if k < 0.45 else
                     (0.35, 0.36, 0.18) if k < 0.72 else
                     (0.44, 0.41, 0.26) if k < 0.9 else (0.20, 0.26, 0.15))
                gq(fx, fx+5150, fy, fy+5150, hazed(c, d, 90000), 1.0)
        for fy in np.arange(-70000, 70000, 20800.0):       # roads
            gq(-70000, 70000, fy, fy+320, hazed((0.42, 0.42, 0.42), 40000, 90000), 1.05)
    else:
        for x0 in np.arange(-2600, 2600, 210.0):           # mown stripes
            k = 0.030 if int(x0//210) % 2 else -0.026
            gq(x0, x0+210, -1400, 2000, gn + k, 1.0, 0.05)
        for x0 in np.arange(-3000, 3000, 300.0):           # apron beyond
            gq(x0, x0+300, 2000, 3400, (0.325, 0.325, 0.338), 1.1, 0.15)
            gq(x0, x0+300, 3400, 3448, (0.85, 0.81, 0.50), 1.15, 0.2)
        for k in range(5200):                              # grass tufts
            d = RNG.uniform(-1100, 1100); e = RNG.uniform(-420, 1400)
            s = 1.3 + 0.008*abs(e)
            gq(d, d + s*RNG.uniform(0.7, 2.6), e, e+s,
               gn*RNG.uniform(0.90, 1.11), 1.2, 0.1)
        for hx, hw, hgt in ((-4200, 2300, 400), (-1400, 1900, 380), (1500, 2700, 430)):
            P = np.array([[hx, 9000, 0], [hx+hw, 9000, 0],
                          [hx+hw, 9000, hgt], [hx, 9000, hgt]])
            pts, zz = project(P)
            if (zz > 24).all():
                ax.add_patch(Polygon(pts, fc=hazed((0.56, 0.58, 0.60), 9000, 60000),
                                     ec="none", zorder=1.3))

    # tree line: a jagged screen-space band on the horizon
    for row, drop, col, amp in ((0, 0.0, (0.28, 0.34, 0.28), 0.010),
                                (1, 0.012, (0.19, 0.26, 0.16), 0.019)):
        xs_ = np.linspace(-AR, AR, 420)
        top = hy - drop + amp*(0.55 + 0.45*np.sin(xs_*11 + row*2.1)
                               * np.sin(xs_*3.7 + row)
                               + 0.22*np.sin(xs_*47 + row*3.3)
                               + 0.16*np.sin(xs_*103 + row))
        pts = np.concatenate([np.stack([xs_, top], 1),
                              [[AR, hy-drop-0.05], [-AR, hy-drop-0.05]]])
        ax.add_patch(Polygon(pts, fc=col, ec="none", zorder=1.25+0.01*row))

    # ---- shadow ----------------------------------------------------------
    if scene != "air" and sun[2] > 0.1:
        t = V[:, 2]/sun[2]
        Sh = V - np.outer(t, sun); Sh[:, 2] = 0.3
        p2, z2 = project(Sh)
        keep = z2[F].min(axis=1) > 24
        for off, al in ((0.0, 0.21), (0.005, 0.13), (0.011, 0.07)):
            ax.add_collection(PolyCollection(p2[F][keep] + np.array([off, -off*0.4]),
                              facecolors=(0.06, 0.08, 0.07), edgecolors="none",
                              alpha=al, zorder=2))
        for cx, cy, r in ((70.5, 28, 15), (70.5, -28, 15), (15, 0, 11)):
            pts, zz = project(np.array([[cx-r, cy-r, 0.4], [cx+r, cy-r, 0.4],
                                        [cx+r, cy+r, 0.4], [cx-r, cy+r, 0.4]]))
            if (zz > 24).all():
                ax.add_patch(Polygon(pts, fc=(0.04, 0.05, 0.04), ec="none",
                                     alpha=0.32, zorder=2.1))

    # ---- aircraft --------------------------------------------------------
    pts, zz = project(V)
    P3 = V[F]
    nf = np.cross(P3[:, 1]-P3[:, 0], P3[:, 2]-P3[:, 0])
    nf /= np.maximum(np.linalg.norm(nf, axis=1, keepdims=True), 1e-9)
    ctr = P3.mean(axis=1)
    vd = cam - ctr; vd /= np.maximum(np.linalg.norm(vd, axis=1, keepdims=True), 1e-9)
    # The mesh has no consistent winding, so orient every facet toward the camera
    # first; that makes vertex-normal averaging (which is what kills the faceted
    # look) well defined, and it makes real signed Lambert usable.
    nf *= np.sign((nf*vd).sum(1))[:, None]
    vn = np.zeros_like(V)
    np.add.at(vn, F.ravel(), np.repeat(nf, 3, axis=0))
    vn /= np.maximum(np.linalg.norm(vn, axis=1, keepdims=True), 1e-9)
    n = vn[F].mean(axis=1)
    n /= np.maximum(np.linalg.norm(n, axis=1, keepdims=True), 1e-9)
    n *= np.sign((n*vd).sum(1))[:, None]

    nv = np.clip((n*vd).sum(1), 0, 1)
    lam = np.clip(n @ sun, 0, 1)
    fill = np.clip(n @ (-sun*np.array([1, 1, -0.35])), 0, 1)    # bounce fill
    hv = sun + vd; hv /= np.maximum(np.linalg.norm(hv, axis=1, keepdims=True), 1e-9)
    spec = np.clip((n*hv).sum(1), 0, 1)**shin

    up_ = n @ np.array([0, 0, 1.0])
    amb = (np.clip(up_, 0, 1)[:, None]*np.array(sky_hz)*0.50
           + np.clip(-up_, 0, 1)[:, None]*gn*0.40
           + 0.26*np.array(sky_hz)
           + (0.13*fill)[:, None]*np.array([0.85, 0.88, 0.95]))
    sunlit = np.array([1.0, 0.962, 0.885])*(0.62 + 0.55*np.clip(sunel/45.0, 0, 1))
    col = base*(amb + (1.05*lam)[:, None]*sunlit)*tex[:, None] \
        + (ks*spec*lam**0.25)[:, None]*sunlit*1.35
    col += (0.17*(1-nv)**3)[:, None]*np.array(sky_hz)          # rim
    col *= expo
    # filmic shoulder: hard-clipping the sunlit wing top to pure white is the
    # single most CG-looking thing a renderer can do, so roll it off instead
    K = 0.78
    col = np.where(col < K, col, K + (1-K)*(1-np.exp(-(col-K)/(1-K))))
    d = zz[F].mean(axis=1)
    lo, hi = np.percentile(d, [2, 98])
    col *= (1.0 - 0.34*np.clip((d-lo)/max(hi-lo, 1e-6), 0, 1))[:, None]
    col = np.clip(col, 0, 1)

    a = alpha.copy()
    glazed = np.zeros(len(F), bool)
    for g in ("glass", "film"):
        s0, s1 = GIDX[g]; glazed[s0:s1] = True
    fres = (1-nv)**2.6
    a[glazed] = np.clip(alpha[glazed] + 0.70*fres[glazed], 0, 0.95)
    col[glazed] = np.clip(col[glazed]
                          + (0.55*fres[glazed])[:, None]*np.array(sky_hz), 0, 1)

    rgba = np.concatenate([col, a[:, None]], axis=1)
    order = np.argsort(-zz[F].mean(axis=1))
    keep = zz[F].min(axis=1) > 8
    sel = order[keep[order]]
    ax.add_collection(PolyCollection(pts[F][sel], facecolors=rgba[sel],
                                     edgecolors=rgba[sel], linewidths=0.45,
                                     zorder=5))

    if spin:                                   # prop blur disc
        ph, zh = project(np.array([[2.0, 0, 40.0]]) + np.array([0, 0, alt]))
        if zh[0] > 8:
            r = 30.0/zh[0]*S
            for k in range(10):
                ax.add_patch(Ellipse(ph[0], r*2*(0.30+0.055*k), r*2*(1-k/11)+r*0.1,
                                     fc=(0.93, 0.94, 0.96, 0.030), ec="none", zorder=6))
            ax.add_patch(Ellipse(ph[0], r*0.66, r*2.02, fc="none",
                                 ec=(0.90, 0.91, 0.94, 0.28), lw=1.6, zorder=6))

    # ---- pixels, then photographic post ----------------------------------
    fig.canvas.draw()
    img = np.asarray(fig.canvas.buffer_rgba(), float)[..., :3]/255.0
    plt.close(fig)
    lum = img @ np.array([0.2126, 0.7152, 0.0722])
    bright = np.clip(lum - 0.74, 0, None)[..., None]*img
    img = np.clip(img + bloom*gaussian_filter(bright, (13, 13, 0))
                  + 0.45*bloom*gaussian_filter(bright, (46, 46, 0)), 0, 1)
    yy, xx = np.mgrid[0:img.shape[0], 0:img.shape[1]]
    r2 = ((xx/img.shape[1]-0.5)**2*1.1 + (yy/img.shape[0]-0.5)**2)
    img *= (1 - 0.33*np.clip(r2*1.85, 0, 1)**1.45)[..., None]
    # lateral chromatic aberration: red out, blue in, by a pixel at the corners
    sx = (xx/img.shape[1]-0.5); sy = (yy/img.shape[0]-0.5)
    for ch, k in ((0, 1.00055), (2, 0.99955)):
        gx = np.clip(((sx/k)+0.5)*img.shape[1], 0, img.shape[1]-1).astype(int)
        gy = np.clip(((sy/k)+0.5)*img.shape[0], 0, img.shape[0]-1).astype(int)
        img[..., ch] = img[gy, gx, ch]
    img = np.clip(img*1.05 - 0.014, 0, 1)**0.98
    img = np.clip(img + RNG.normal(0, grain, img.shape), 0, 1)

    out = Image.fromarray((img*255).astype(np.uint8))
    if caption:
        d2 = ImageDraw.Draw(out, "RGBA")
        d2.rectangle([0, out.height-32, out.width, out.height], fill=(0, 0, 0, 115))
        d2.text((16, out.height-22), caption, fill=(255, 255, 255, 225))
    os.makedirs("drawings/renders", exist_ok=True)
    out.save(fname)
    print("wrote", fname)


CAP = ("NUTHATCH rev G  ·  rendering of the design mesh (model/nuthatch.stl)  ·  "
       "0.040 Lexan windshield, 20 mil film doors, welded 4130 cage, 3.50 in boom"
       "  ·  NOT A PHOTOGRAPH — this aircraft has not been built")

# 1. Hero: low three-quarter front-left, morning sun from behind the right wing.
#    The windshield sweeps unbroken from the spinner to the wing leading edge and
#    the wing sits straight on the cabin roof - no cabane, no struts.
render("drawings/renders/hero-ramp.png",
       cam=(-232, -168, 26), look=(66, 4, 34), fov=13.0,
       sunaz=64, sunel=25, prop_ang=28, scene="ramp",
       sky_top=(0.14, 0.31, 0.61), sky_hz=(0.76, 0.82, 0.87),
       gnear=(0.23, 0.30, 0.13), caption=CAP)

# 2. Cockpit: tight three-quarter front-right, sun behind camera-left so the
#    windshield reads as a curved reflective panel and the near door reads as
#    film. Cage, seated reclined pilot and stick all visible through it.
render("drawings/renders/hero-cockpit.png",
       cam=(-168, 104, 48), look=(58, -6, 38), fov=17.0, expo=0.97,
       sunaz=286, sunel=36, prop_ang=64, scene="ramp",
       sky_top=(0.16, 0.34, 0.62), sky_hz=(0.79, 0.84, 0.88),
       gnear=(0.24, 0.31, 0.14), caption=CAP)

# 3. Air-to-air, three-quarter rear-high, banked away: the single straight boom
#    from the cage to the tail, and the wing landing flat on the cabin roof.
render("drawings/renders/hero-air.png",
       cam=(612, -388, 2588), look=(80, 10, 2452), fov=13.0, expo=0.90,
       sunaz=150, sunel=44, bank=13.0, pitch=-2.0, alt=2400, spin=True,
       scene="air", sky_top=(0.09, 0.25, 0.58), sky_hz=(0.70, 0.79, 0.88),
       gnear=(0.26, 0.32, 0.19), caption=CAP)
