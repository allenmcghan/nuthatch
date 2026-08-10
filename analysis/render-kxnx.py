#!/usr/bin/env python3
"""Synthetic renderings: Nuthatch rev G lifting off runway 35 at Music City
Executive Airport (KXNX), Gallatin TN — 6,300 x 100 ft asphalt, elev 583 ft.
Sun-shaded painter render of the actual mesh with cast shadow. These are
renderings of the design geometry, not photographs.
Outputs drawings/renders/kxnx-takeoff-{1,2}.png
"""
import json, os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Ellipse
from matplotlib.collections import PolyCollection

sp = sys.argv[1] if len(sys.argv) > 1 else "."
m = json.load(open(os.path.join(sp, "nuthatch-mesh.json")))
V0 = np.array(m["v"], float)/12.0          # feet
F = np.array(m["f"]); GROUPS = m["groups"]

MAT = {  # base RGB per group (fabric cream, steel graphite, black rubber...)
 "wing":(0.93,0.90,0.82),"tail":(0.93,0.90,0.82),"fuse":(0.88,0.86,0.80),
 "prop":(0.25,0.22,0.20),"tire_n":(0.13,0.13,0.14),"gear":(0.30,0.33,0.36),
 "cage":(0.34,0.37,0.40),
 "wheel_m":(0.15,0.15,0.17),"struts":(0.30,0.33,0.36),
 "doors":(0.55,0.62,0.68),
 "boom":(0.76,0.77,0.78),"glass":(0.62,0.70,0.76),"film":(0.66,0.71,0.74),
 "wsframe":(0.38,0.40,0.42)}
fcol = np.zeros((len(F),3))
for name,a,b in GROUPS: fcol[a:b] = MAT.get(name,(0.6,0.6,0.6))
# accent: rudder + wingtips in a warm orange
fcol[[i for n,a,b in GROUPS if n=="tail" for i in range(a,b)
      if V0[F[i]].mean(axis=0)[2] > 5.2]] = (0.79,0.44,0.12)

def render(fname, cam, look, pitch_deg, alt_ft, sunaz=250, sunel=18, fov=8.5,
           W=1800, H=1012, warm=1.0):
    # aircraft: pitch about main axle, then lift to alt
    Vc = V0.copy()
    ax_pt = np.array([70.5/12, 0, 14.5/12])
    th = np.radians(pitch_deg)
    R = np.array([[np.cos(th),0,np.sin(th)],[0,1,0],[-np.sin(th),0,np.cos(th)]])
    Vc = (Vc-ax_pt)@R.T + ax_pt
    Vc[:,2] += alt_ft
    sun = np.array([np.cos(np.radians(sunel))*np.cos(np.radians(sunaz)),
                    np.cos(np.radians(sunel))*np.sin(np.radians(sunaz)),
                    np.sin(np.radians(sunel))])
    cam = np.array(cam,float); look = np.array(look,float)
    fwd = look-cam; fwd/=np.linalg.norm(fwd)
    right = np.cross(fwd,[0,0,1]); right/=np.linalg.norm(right)
    up = np.cross(right,fwd)
    def project(P):
        d = P-cam
        z = d@fwd; x = d@right; y = d@up
        s = 1.0/np.tan(np.radians(fov))
        return np.stack([s*x/z, s*y/z], axis=1), z
    fig = plt.figure(figsize=(W/100, H/100), dpi=100)
    ax = fig.add_axes([0,0,1,1]); ax.set_xlim(-1.6,1.6); ax.set_ylim(-0.9,0.9); ax.axis("off")
    # true horizon height on screen: far point at ground level along view azimuth
    fh = fwd.copy(); fh[2]=0; fh/=np.linalg.norm(fh)
    hpt,_ = project((cam + fh*50000).reshape(1,3) * np.array([1,1,0]) + np.array([0,0,0]))
    hy = float(np.clip(hpt[0,1], -0.5, 0.6))
    # sky gradient down to horizon
    for i in range(60):
        t = i/59
        col = (0.55+0.38*t*warm, 0.62+0.20*t, 0.78-0.28*t*warm)
        y0 = 0.9-(0.9-hy)*(i+1)/60
        ax.add_patch(plt.Rectangle((-1.6, y0), 3.2, (0.9-hy)/60+0.003,
                     fc=np.clip(col,0,1), ec="none", zorder=0))
    ax.add_patch(plt.Rectangle((-1.6,-0.9),3.2,hy+0.9+0.002,fc=(0.36,0.42,0.28),ec="none",zorder=0))
    # ground plane items (feet, world): runway 100 ft wide along +X
    def gquad(x1,x2,y1,y2,color,z=1):
        P = np.array([[x1,y1,0.02],[x2,y1,0.02],[x2,y2,0.02],[x1,y2,0.02]])
        pts,zz = project(P)
        if (zz>1).all(): ax.add_patch(Polygon(pts,fc=color,ec="none",zorder=z))
    for x0 in range(-5800,600,150):                     # asphalt, tiled; departure = -X
        gquad(x0,x0+150,-50,50,(0.33,0.33,0.35))
        gquad(x0,x0+150,50,90,(0.31,0.37,0.25),1)
        gquad(x0,x0+150,-90,-50,(0.31,0.37,0.25),1)
    for x0 in range(-5600,400,160): gquad(x0,x0+70,-1.6,1.6,(0.85,0.83,0.78),2)
    # tree lines: near row (far side) and far row, receding to the vanishing point
    for tx in range(-5400,700,180):
        h=26+((tx*7)%15); dg=0.02*((tx//180)%3)
        P=np.array([[tx,640,0],[tx+150,640,0],[tx+150,640,h+14],[tx,640,h+11]])
        pts,zz=project(P)
        if (zz>2).all(): ax.add_patch(Polygon(pts,fc=(0.19+dg,0.27+dg,0.15),ec="none",zorder=1))
    for tx in range(-5400,700,260):
        P=np.array([[tx,-700,0],[tx+230,-700,0],[tx+230,-700,42],[tx,-700,39]])
        pts,zz=project(P)
        if (zz>2).all(): ax.add_patch(Polygon(pts,fc=(0.23,0.31,0.18),ec="none",zorder=1))
    # clouds
    for cx,cy,cw in ((-0.9,0.55,0.5),(0.4,0.62,0.7),(1.1,0.48,0.4)):
        ax.add_patch(Ellipse((cx,cy),cw,0.07,fc=(1,1,1,0.35),ec="none",zorder=0.5))
        ax.add_patch(Ellipse((cx+0.15,cy+0.03),cw*0.6,0.05,fc=(1,1,1,0.28),ec="none",zorder=0.5))
    # cast shadow (project along sun to z=0)
    t = Vc[:,2]/max(sun[2],0.15)
    Sh = Vc - np.outer(t, sun); Sh[:,2]=0.05
    pts2,zz2 = project(Sh)
    tris = pts2[F]
    keep = (zz2[F].min(axis=1)>1)
    ax.add_collection(PolyCollection(tris[keep],facecolors=(0.10,0.11,0.10),
                                     edgecolors="none",alpha=0.35,zorder=3))
    # aircraft, painter-sorted, lambert + rim
    pts,zz = project(Vc)
    ctr = zz[F].mean(axis=1)
    order = np.argsort(-ctr)
    P3 = Vc[F]
    n = np.cross(P3[:,1]-P3[:,0], P3[:,2]-P3[:,0])
    nl = np.linalg.norm(n,axis=1,keepdims=True); n = n/np.maximum(nl,1e-9)
    lam = np.abs(n@sun)
    shade = (0.35+0.75*lam)[:,None]*fcol
    shade += (0.10*np.maximum(n@np.array([0,0,1]),0))[:,None]*np.array([0.9,0.7,0.5])*warm
    shade = np.clip(shade,0,1)
    tris = pts[F]
    keep = zz[F].min(axis=1)>1
    ax.add_collection(PolyCollection(tris[order][keep[order]],
        facecolors=shade[order][keep[order]], edgecolors="none", zorder=5))
    # prop blur disc
    hub = np.array([[2/12,0,40/12]])@R.T + (ax_pt - ax_pt@R.T@np.eye(3))  # approx
    hubw = (np.array([2/12,0,40/12])-ax_pt)@R.T+ax_pt; hubw[2]+=alt_ft
    ph,zh = project(hubw[None,:])
    if zh[0]>1:
        r = 2.5/zh[0]*(1/np.tan(np.radians(fov)))
        ax.add_patch(Ellipse(ph[0], r*0.5, r*2, angle=8, fc=(0.9,0.9,0.9,0.14),
                             ec=(0.85,0.85,0.85,0.3), lw=1, zorder=6))
    fig.text(0.012,0.02,"NUTHATCH rev G — synthetic rendering of the design mesh · "
             "runway 35, Music City Executive (KXNX), Gallatin TN · not a photograph",
             fontsize=8, color="white", alpha=0.85, family="monospace")
    os.makedirs("drawings/renders", exist_ok=True)
    fig.savefig(fname, dpi=100); plt.close(fig)
    print("wrote", fname)

# Shot 1: low 3/4 front-right of path, just lifted off, golden hour, runway to horizon
render("drawings/renders/kxnx-takeoff-1.png",
       cam=(95,-38,8), look=(4,6,15), pitch_deg=-9, alt_ft=9, sunaz=250, sunel=13, fov=11)
# Shot 2: side profile climbing, cooler light
render("drawings/renders/kxnx-takeoff-2.png",
       cam=(50,-150,26), look=(0,-4,30), pitch_deg=-11, alt_ft=28, sunaz=215, sunel=40,
       fov=7.5, warm=0.45)
