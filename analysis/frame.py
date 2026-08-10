#!/usr/bin/env python3
"""The steel frame, as data. Single source of truth.

Everything downstream reads this file: the 3D mesh, the CAD exports, the tube
schedule, the renders. Move a node here and the drawings, the cut list and the
weight all follow. That is the point - the frame was previously 30 hard-coded
strut() calls inside the mesh generator, which is fine for drawing a picture
and useless for changing a design.

Axes: X aft from the propeller plane (station, inches), Y right, Z up.
Ground at z=0, so z is also height above the ground with the gear at static.

Naming: nodes ending _R are on the right; every _R node and every member that
touches one is mirrored automatically to _L. Nodes ending _C are on the
centreline. Mirroring is not optional - there is no way to express an
asymmetric frame here, which is deliberate.

*** TUBE SIZES ARE PROVISIONAL. ***
No member here has been sized against a load case. `docs/open-questions.md`
carries "cage member sizing + a rollover load basis" as unresolved, and no
rollover standard has been chosen. These sizes are placeholders that carry the
right geometry and a plausible weight - they are NOT a design. Do not cut steel
from this table.
"""
import math

# --- tube stock. (OD, wall, material). 4130 normalised unless noted. --------
TUBE = {
    "long":   (1.000, 0.049, "4130"),   # longerons
    "hoop":   (1.125, 0.058, "4130"),   # main hoop, rollover structure
    "diag":   (0.750, 0.035, "4130"),   # side diagonals
    "spar":   (1.250, 0.058, "4130"),   # wing spar carry-through
    "frame":  (0.875, 0.049, "4130"),   # secondary frames
    "gear":   (1.250, 0.058, "4130"),   # landing gear
    "boom":   (3.500, 0.049, "4130"),   # tail boom
    "glaze":  (0.375, 0.028, "4130"),   # glazing frame rails and bows
}
RHO_STEEL = 0.283                        # lb/in^3

# --- key stations, so the ones that carry meaning are named ----------------
NOSE = 30.0      # nose bow: forward face of the cage, ahead of the pilot's feet
FS   = 61.5      # main hoop: front spar + rollover + CG, all on one frame
RS   = 80.5      # rear frame: rear spar + seat back + harness anchor
AFT  = 96.0      # aft frame: boom pickup, aft end of the cage
ROOF = 55.0      # cabin roof = wing underside = spar pickup height
TAIL = 184.0     # tail post

# --- nodes ------------------------------------------------------------------
# Half the frame only; _R mirrors to _L. Coordinates in inches.
_N = {
    # nose bow - the crash structure forward of the footwell
    "NB_R":  (NOSE,  9.0, 18.0),      # lower corner
    "NT_R":  (NOSE,  8.0, 38.0),      # upper corner
    # main hoop at the front spar / CG / rollover station
    "MH_R":  (FS,    9.5, 18.0),      # foot, on the lower longeron
    "MS_R":  (FS,    9.5, 40.0),      # shoulder
    "MP_R":  (FS,    8.0, ROOF),      # front spar pickup, at the cabin roof
    # rear frame
    "RF_R":  (RS,    7.5, 20.0),
    "RP_R":  (RS,    8.0, ROOF),      # rear spar pickup
    # aft frame, where the boom picks up
    "AL_R":  (AFT,   6.0, 24.0),
    "AU_R":  (AFT,   6.0, 30.0),
    # boom and tail, on the centreline
    "BM_C":  (AFT,   0.0, 27.0),
    "TP_C":  (TAIL,  0.0, 27.0),
    # nose gear
    "NGU_C": (NOSE,  0.0, 17.0),      # trailing-link pivot, on the nose bow
    "NGF_C": (14.0,  0.0, 30.0),      # forward drag-strut top  *** see below
    "NAX_C": (15.0,  0.0, 10.0),      # axle, 20 in wheel, just aft of the disc
    # main gear
    "MGF_R": (58.0, 10.0, 17.0),      # trailing arm pivot
    "MAX_R": (70.5, 28.0, 14.5),      # axle
    "MGS_R": (64.0, 14.0, 30.0),      # coil-over upper mount
}

# *** NGF_C IS A KNOWN DEFECT, CARRIED DELIBERATELY. ***
# It sits at station 14, sixteen inches forward of the cage, which starts at 30.
# It attaches to nothing. It came in with the rev D raked nose leg as "closes
# the crush-bay triangle" and was never tied to a cage node. Either it lands on
# the nose bow, or it lands on the engine mount, or the member goes away - but
# it cannot float. Flagged in docs/open-questions.md; left in place so the
# geometry does not silently change under anyone who has already drawn from it.

# --- members: (node A, node B, tube key, description) ----------------------
# Written once for the right-hand side; anything touching an _R node mirrors.
_M = [
    ("NB_R",  "AL_R",  "long",  "lower longeron, nose bow to aft frame"),
    ("NT_R",  "AU_R",  "long",  "upper longeron, nose bow to aft frame"),
    ("NB_R",  "NT_R",  "long",  "nose bow post"),
    ("NB_R",  "MS_R",  "diag",  "forward side diagonal"),
    ("MH_R",  "AU_R",  "diag",  "aft side diagonal"),
    ("MH_R",  "MS_R",  "hoop",  "main hoop, lower leg"),
    ("MS_R",  "MP_R",  "hoop",  "main hoop, upper leg to the spar pickup"),
    ("RF_R",  "RP_R",  "frame", "rear frame post"),
    ("AL_R",  "AU_R",  "frame", "aft frame post"),
    ("NT_L",  "NT_R",  "frame", "nose bow crown"),
    ("MP_L",  "MP_R",  "spar",  "FRONT SPAR carry-through"),
    ("RP_L",  "RP_R",  "spar",  "REAR SPAR carry-through"),
    ("MS_L",  "MS_R",  "hoop",  "main hoop shoulder cross"),
    ("AL_L",  "AL_R",  "frame", "aft frame lower cross, boom pickup"),
    ("AU_L",  "AU_R",  "frame", "aft frame upper cross, boom pickup"),
    ("BM_C",  "TP_C",  "boom",  "tail boom"),
    ("NGU_C", "NAX_C", "gear",  "nose leg, raked"),
    ("NGF_C", "NAX_C", "gear",  "nose leg forward drag strut  (SEE NGF_C NOTE)"),
    ("MGF_R", "MAX_R", "gear",  "main trailing arm"),
    ("MAX_R", "MGS_R", "gear",  "main coil-over"),
]

# --- expansion --------------------------------------------------------------


def _mirror(name):
    if name.endswith("_R"): return name[:-2] + "_L"
    if name.endswith("_L"): return name[:-2] + "_R"
    return name


def nodes():
    """All nodes, mirrored, as {name: (x, y, z)}."""
    out = {}
    for n, p in _N.items():
        out[n] = p
        if n.endswith("_R"):
            out[_mirror(n)] = (p[0], -p[1], p[2])
    return out


def members():
    """All members, mirrored and de-duplicated.

    Returns a list of dicts: a, b, tube, desc, pa, pb, length, side."""
    N = nodes()
    seen, out = set(), []
    for a, b, t, d in _M:
        pairs = [(a, b, "R" if (a.endswith("_R") or b.endswith("_R")) else "C")]
        ma, mb = _mirror(a), _mirror(b)
        if (ma, mb) != (a, b) and {ma, mb} <= set(N):
            pairs.append((ma, mb, "L"))
        for x, y, side in pairs:
            key = tuple(sorted((x, y)))
            if key in seen: continue
            seen.add(key)
            pa, pb = N[x], N[y]
            L = math.dist(pa, pb)
            out.append(dict(a=x, b=y, tube=t, desc=d, pa=pa, pb=pb,
                            length=L, side=side))
    return out


def tube_weight(key, length):
    od, wall, _ = TUBE[key]
    area = math.pi*(od - wall)*wall
    return area*length*RHO_STEEL


def joint_angles():
    """For every node, the angle between each pair of members meeting there.

    This is what sets the fishmouth. Anything under about 20 deg is a bad
    weld joint no matter how good the notch is."""
    M = members()
    at = {}
    for i, m in enumerate(M):
        at.setdefault(m["a"], []).append((i, +1))
        at.setdefault(m["b"], []).append((i, -1))
    out = {}
    for node, lst in at.items():
        vs = []
        for i, sgn in lst:
            m = M[i]
            v = [(m["pb"][k]-m["pa"][k])*sgn for k in range(3)]
            n = math.dist((0, 0, 0), v)
            vs.append((i, [c/n for c in v]))
        pairs = []
        for p in range(len(vs)):
            for q in range(p+1, len(vs)):
                dot = sum(vs[p][1][k]*vs[q][1][k] for k in range(3))
                pairs.append((vs[p][0], vs[q][0],
                              math.degrees(math.acos(max(-1, min(1, dot))))))
        out[node] = pairs
    return out


def _pt_seg(p, a, b):
    """Distance from a point to a segment, and where along it."""
    ab = [b[k]-a[k] for k in range(3)]
    L2 = sum(c*c for c in ab)
    if L2 < 1e-9: return math.dist(p, a), 0.0
    t = max(0.0, min(1.0, sum((p[k]-a[k])*ab[k] for k in range(3))/L2))
    q = [a[k] + t*ab[k] for k in range(3)]
    return math.dist(p, q), t


def check(near=4.0):
    """Structural sanity on the graph, not the picture.

    A tube frame drawn as overlapping cylinders looks connected even when it
    is not - the mesh has no idea whether two tubes actually meet. On the
    node/member graph the question is answerable, so ask it:

      1. dangling nodes   - a node with one member is a free end
      2. islands          - sub-assemblies not welded to the main structure
      3. near misses      - a node sitting close to, but not on, a member.
                            These are the dangerous ones: they read as joints
                            on a drawing and are not joints in the steel.

    Returns (dangling, islands, near_misses)."""
    N, M = nodes(), members()
    deg, adj = {n: 0 for n in N}, {n: set() for n in N}
    for m in M:
        deg[m["a"]] += 1; deg[m["b"]] += 1
        adj[m["a"]].add(m["b"]); adj[m["b"]].add(m["a"])
    dangling = sorted(n for n in N if deg[n] < 2)

    seen, islands = set(), []
    for start in N:
        if start in seen: continue
        comp, stack = set(), [start]
        while stack:
            n = stack.pop()
            if n in comp: continue
            comp.add(n); stack += list(adj[n] - comp)
        seen |= comp
        islands.append(sorted(comp))
    islands.sort(key=len, reverse=True)

    misses = []
    for n, p in N.items():
        for k, m in enumerate(M):
            if n in (m["a"], m["b"]): continue
            d, t = _pt_seg(p, m["pa"], m["pb"])
            if 1e-6 < d <= near and 0.02 < t < 0.98:
                misses.append((n, k, d, t))
    misses.sort(key=lambda r: r[2])
    return dangling, islands, misses


def struts(groups=None):
    """(p1, p2, radius, group) for the mesh generator. Radius = OD/2."""
    GRP = {"long": "cage", "hoop": "cage", "diag": "cage", "spar": "cage",
           "frame": "cage", "gear": "gear", "boom": "boom", "glaze": "wsframe"}
    out = []
    for m in members():
        g = GRP[m["tube"]]
        if groups and g not in groups: continue
        out.append((list(m["pa"]), list(m["pb"]), TUBE[m["tube"]][0]/2.0, g))
    return out


if __name__ == "__main__":
    M = members()
    print(f"{len(nodes())} nodes, {len(M)} members\n")
    tot = 0.0
    by = {}
    for m in M:
        w = tube_weight(m["tube"], m["length"])
        tot += w
        k = m["tube"]
        by[k] = (by.get(k, (0, 0.0, 0.0))[0] + 1,
                 by.get(k, (0, 0.0, 0.0))[1] + m["length"],
                 by.get(k, (0, 0.0, 0.0))[2] + w)
    print(f"  {'stock':8s}{'OD x wall':>14s}{'off':>5s}{'length in':>11s}{'lb':>8s}")
    for k, (n, L, w) in sorted(by.items()):
        od, wall, _ = TUBE[k]
        print(f"  {k:8s}{od:7.3f} x {wall:.3f}{n:5d}{L:11.1f}{w:8.2f}")
    print(f"  {'':8s}{'':14s}{len(M):5d}{sum(v[1] for v in by.values()):11.1f}"
          f"{tot:8.2f}")
    print("\n  Centreline lengths. Deduct at each end for the fishmouth.")
    print("  TUBE SIZES ARE PROVISIONAL - see the module docstring.")

    print("\n  Tight joints (under 20 deg between members - hard to notch,")
    print("  hard to weld, and a stress raiser):")
    bad = 0
    for node, pairs in sorted(joint_angles().items()):
        for i, j, ang in pairs:
            if ang < 20.0:
                print(f"    {node:7s}{ang:6.1f} deg  {M[i]['desc']}"
                      f"  /  {M[j]['desc']}")
                bad += 1
    if not bad: print("    none")

    dangling, islands, misses = check()
    print("\n  === CONNECTIVITY ===")
    print(f"  dangling ends (one member only): "
          + (", ".join(dangling) if dangling else "none"))
    if len(islands) > 1:
        print(f"  *** {len(islands)} DISCONNECTED PIECES ***")
        for c in islands:
            print(f"    {len(c):2d} nodes: {', '.join(c)}")
    else:
        print("  the frame is one connected structure")
    print("\n  near misses (a node close to a member but not welded to it -")
    print("  these read as joints on a drawing and are not joints in steel):")
    if misses:
        for n, k, d, t in misses[:12]:
            print(f"    {n:7s}{d:6.2f} in from '{M[k]['desc']}'"
                  f"  at {100*t:.0f}% along it")
    else:
        print("    none")
