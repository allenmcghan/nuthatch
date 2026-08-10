#!/usr/bin/env python3
"""Export the steel frame to CAD, and read it back after you have moved it.

Writes, into cad/:
  nuthatch-frame-3d.dxf   3D wireframe of every tube centreline, on layers by
                          structure group, plus node markers and labels. This
                          is the file to open in AutoCAD and start moving.
  nuthatch-views-2d.dxf   side / top / front orthographic projections laid out
                          on one sheet with a station grid, for drafting.
  nuthatch-frame.scr      an AutoCAD script that draws the same wireframe with
                          LINE commands, for when a DXF import argues with you.
  tube-schedule.csv       cut list: every member, its stock, centreline length,
                          weight, and the tightest joint angle at each end.
  nodes.csv               every node, mirrored, with the members on it.

Reads back:
  --from-dxf FILE         parse LINE entities out of a DXF you have edited and
                          report what moved, what appeared and what vanished,
                          against analysis/frame.py. Prints a frame.py-shaped
                          node table you can paste back in.

Everything is in INCHES, in the aircraft datum: X aft from the propeller plane,
Y right, Z up, ground at z=0. Set your CAD units to inches and it lands in the
right place with no scaling.
"""
import csv, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frame

OUT = "cad"
# layer name -> (AutoCAD colour index, the tube keys that go on it)
LAYERS = {
    "CAGE-LONGERON": (5,  ["long"]),
    "CAGE-HOOP":     (1,  ["hoop"]),
    "CAGE-DIAGONAL": (3,  ["diag"]),
    "CAGE-SPAR":     (6,  ["spar"]),
    "CAGE-FRAME":    (4,  ["frame"]),
    "BOOM":          (2,  ["boom"]),
    "GEAR":          (30, ["gear"]),
}
EXTRA = {"NODES": 7, "NODE-TEXT": 8, "REFERENCE": 8, "DIM-TEXT": 7,
         "OUTLINE": 253}
LAYER_OF = {t: name for name, (_, ts) in LAYERS.items() for t in ts}


# ----------------------------------------------------------------- DXF writer
class Dxf:
    """Minimal AutoCAD R12 ASCII DXF. R12 on purpose: every CAD package on
    earth reads it, including the ones that choke on newer entity types."""

    def __init__(self):
        self.e = []

    def line(self, p1, p2, layer):
        self.e += [(0, "LINE"), (8, layer),
                   (10, p1[0]), (20, p1[1]), (30, p1[2]),
                   (11, p2[0]), (21, p2[1]), (31, p2[2])]

    def point(self, p, layer):
        self.e += [(0, "POINT"), (8, layer),
                   (10, p[0]), (20, p[1]), (30, p[2])]

    def text(self, p, s, layer, h=0.6):
        self.e += [(0, "TEXT"), (8, layer),
                   (10, p[0]), (20, p[1]), (30, p[2]), (40, h), (1, s)]

    def write(self, path, layers):
        g = ["  0", "SECTION", "  2", "TABLES",
             "  0", "TABLE", "  2", "LAYER", " 70", str(len(layers))]
        for name, col in layers.items():
            g += ["  0", "LAYER", "  2", name, " 70", "0",
                  " 62", str(col), "  6", "CONTINUOUS"]
        g += ["  0", "ENDTAB", "  0", "ENDSEC",
              "  0", "SECTION", "  2", "ENTITIES"]
        for code, val in self.e:
            g.append("%3d" % code)
            g.append(("%.4f" % val) if isinstance(val, float) else str(val))
        g += ["  0", "ENDSEC", "  0", "EOF"]
        with open(path, "w") as f:
            f.write("\n".join(g) + "\n")
        print("wrote", path)


# --------------------------------------------------------------- the exports
def export_3d(M, N):
    d = Dxf()
    for m in M:
        d.line(m["pa"], m["pb"], LAYER_OF[m["tube"]])
    for name, p in sorted(N.items()):
        d.point(p, "NODES")
        d.text((p[0]+0.6, p[1], p[2]+0.6), name, "NODE-TEXT", 0.7)
    # datum: thrustline, waterlines and the stations that mean something
    d.line((0, 0, 40), (200, 0, 40), "REFERENCE")
    d.text((201, 0, 40), "THRUSTLINE z=40", "REFERENCE", 1.0)
    d.line((-10, 0, 0), (200, 0, 0), "REFERENCE")
    d.text((201, 0, 0), "GROUND z=0", "REFERENCE", 1.0)
    for st, lab in ((0, "PROP PLANE"), (frame.NOSE, "NOSE BOW"),
                    (63.0, "CG"), (frame.FS, "MAIN HOOP / FRONT SPAR"),
                    (frame.RS, "REAR SPAR"), (frame.AFT, "AFT FRAME"),
                    (frame.TAIL, "TAIL")):
        d.line((st, -24, 0), (st, 24, 0), "REFERENCE")
        d.text((st, 25, 0), "STA %.1f %s" % (st, lab), "REFERENCE", 1.0)
    lay = {k: v for k, (v, _) in LAYERS.items()}
    lay.update(EXTRA)
    d.write(os.path.join(OUT, "nuthatch-frame-3d.dxf"), lay)


def export_2d(M, N):
    """Three orthographic views on one sheet. Everything is drawn flat on z=0
    so it opens as a 2D drawing, laid out left to right."""
    d = Dxf()
    GAP = 40.0
    top_off = 60.0          # top view sits below the side view
    front_x = 230.0         # front view to the right

    def side(p):  return (p[0], p[2], 0.0)
    def top(p):   return (p[0], p[1] - top_off, 0.0)
    def front(p): return (front_x + p[1], p[2], 0.0)

    for proj, title, tx in ((side, "SIDE  (looking left, nose left)", (0, 70)),
                            (top, "TOP  (nose left)", (0, -top_off + 32)),
                            (front, "FRONT  (from the propeller)",
                             (front_x - 26, 70))):
        for m in M:
            d.line(proj(m["pa"]), proj(m["pb"]), LAYER_OF[m["tube"]])
        d.text((tx[0], tx[1], 0.0), title, "DIM-TEXT", 2.5)

    # station grid and ticks on the side view
    for st in range(0, int(frame.TAIL)+1, 12):
        d.line((st, -4, 0), (st, -1.5, 0), "REFERENCE")
        d.text((st-2.5, -8, 0), str(st), "DIM-TEXT", 1.6)
    d.line((0, -2.5, 0), (frame.TAIL, -2.5, 0), "REFERENCE")
    d.text((frame.TAIL+4, -8, 0), "STATION, IN", "DIM-TEXT", 1.6)
    for wl, lab in ((0, "GROUND"), (40, "THRUSTLINE"), (frame.ROOF, "CABIN ROOF")):
        d.line((-6, wl, 0), (frame.TAIL, wl, 0), "REFERENCE")
        d.text((frame.TAIL+4, wl, 0), "WL %d %s" % (wl, lab), "DIM-TEXT", 1.6)

    for name, p in sorted(N.items()):
        for proj in (side, top, front):
            q = proj(p)
            d.point(q, "NODES")
            d.text((q[0]+0.5, q[1]+0.5, 0.0), name, "NODE-TEXT", 0.9)

    d.text((0, 86, 0), "NUTHATCH rev H - STEEL FRAME CENTRELINES - "
                       "INCHES - TUBE SIZES PROVISIONAL, NOT FOR FABRICATION",
           "DIM-TEXT", 3.2)
    lay = {k: v for k, (v, _) in LAYERS.items()}
    lay.update(EXTRA)
    d.write(os.path.join(OUT, "nuthatch-views-2d.dxf"), lay)


def export_scr(M):
    """An AutoCAD .scr. Belt and braces: if a DXF import ever misbehaves, this
    draws the identical wireframe by typing LINE at the command line."""
    g = ["; Nuthatch rev H steel frame. Units: INCHES.",
         "; Run with:  SCRIPT  ->  nuthatch-frame.scr",
         "; Tube sizes are provisional - see analysis/frame.py.",
         "OSNAP", "NONE"]
    cur = None
    for m in M:
        lay = LAYER_OF[m["tube"]]
        if lay != cur:
            g += ["-LAYER", "M", lay, ""]
            cur = lay
        g += ["LINE",
              "%.4f,%.4f,%.4f" % tuple(m["pa"]),
              "%.4f,%.4f,%.4f" % tuple(m["pb"]), ""]
    g += ["ZOOM", "E", ""]
    p = os.path.join(OUT, "nuthatch-frame.scr")
    open(p, "w").write("\n".join(g) + "\n")
    print("wrote", p)


def export_csv(M, N):
    ang = frame.joint_angles()

    def tightest(node, idx):
        vals = [a for i, j, a in ang.get(node, []) if idx in (i, j)]
        return min(vals) if vals else 180.0

    idx = {id(m): k for k, m in enumerate(M)}
    p = os.path.join(OUT, "tube-schedule.csv")
    with open(p, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["#", "TUBE SIZES ARE PROVISIONAL - no member here has been"
                         " sized against a load case. Not for fabrication."])
        w.writerow(["id", "from", "to", "stock", "OD_in", "wall_in", "material",
                    "cl_length_in", "weight_lb", "side",
                    "min_joint_angle_from_deg", "min_joint_angle_to_deg",
                    "description"])
        for k, m in enumerate(M):
            od, wall, mat = frame.TUBE[m["tube"]]
            w.writerow([k+1, m["a"], m["b"], m["tube"], od, wall, mat,
                        round(m["length"], 2),
                        round(frame.tube_weight(m["tube"], m["length"]), 3),
                        m["side"],
                        round(tightest(m["a"], k), 1),
                        round(tightest(m["b"], k), 1), m["desc"]])
        tot = sum(frame.tube_weight(m["tube"], m["length"]) for m in M)
        w.writerow([])
        w.writerow(["", "", "", "", "", "", "TOTAL",
                    round(sum(m["length"] for m in M), 1), round(tot, 2)])
    print("wrote", p)

    p = os.path.join(OUT, "nodes.csv")
    on = {}
    for m in M:
        on.setdefault(m["a"], []).append(m["desc"])
        on.setdefault(m["b"], []).append(m["desc"])
    with open(p, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["node", "x_sta_in", "y_in", "z_in", "members", "meets"])
        for name, q in sorted(N.items()):
            w.writerow([name, q[0], q[1], q[2], len(on.get(name, [])),
                        " | ".join(sorted(set(on.get(name, []))))])
    print("wrote", p)


# ------------------------------------------------------------- read-back mode
def from_dxf(path):
    """Parse LINE entities and diff the result against frame.py."""
    codes = []
    with open(path) as f:
        raw = [l.rstrip("\n") for l in f]
    for i in range(0, len(raw)-1, 2):
        try: codes.append((int(raw[i].strip()), raw[i+1].strip()))
        except ValueError: pass
    lines, cur, inent = [], {}, False
    for code, val in codes:
        if code == 0:
            if cur.get("_t") == "LINE" and len(cur) >= 7:
                lines.append((cur.get(8, "?"),
                              (cur.get(10, 0.0), cur.get(20, 0.0), cur.get(30, 0.0)),
                              (cur.get(11, 0.0), cur.get(21, 0.0), cur.get(31, 0.0))))
            cur = {"_t": val}
            inent = val in ("LINE", "POINT", "TEXT")
        elif inent:
            if code == 8: cur[8] = val
            elif code in (10, 20, 30, 11, 21, 31):
                try: cur[code] = float(val)
                except ValueError: pass
    if cur.get("_t") == "LINE" and len(cur) >= 7:
        lines.append((cur.get(8, "?"),
                      (cur.get(10, 0.0), cur.get(20, 0.0), cur.get(30, 0.0)),
                      (cur.get(11, 0.0), cur.get(21, 0.0), cur.get(31, 0.0))))
    lines = [l for l in lines if l[0] in LAYERS]
    print(f"read {len(lines)} structural LINE entities from {path}\n")

    N, M = frame.nodes(), frame.members()
    TOL = 0.05

    def nearest(p):
        best, bd = None, 1e9
        for name, q in N.items():
            dd = math.dist(p, q)
            if dd < bd: best, bd = name, dd
        return best, bd

    moved, new_pts, matched = {}, [], set()
    for lay, p1, p2 in lines:
        for p in (p1, p2):
            name, dd = nearest(p)
            if dd <= TOL:
                matched.add(name)
            elif dd <= 6.0:
                cu = moved.setdefault(name, [])
                if all(math.dist(p, q) > TOL for q in cu): cu.append(p)
            else:
                if all(math.dist(p, q) > TOL for q in new_pts): new_pts.append(p)

    if moved:
        print("MOVED (an existing node is within 6 in of a new position):")
        for name, pts in sorted(moved.items()):
            for p in pts:
                o = N[name]
                print(f"  {name:7s} {o} -> ({p[0]:.2f}, {p[1]:.2f}, {p[2]:.2f})"
                      f"   moved {math.dist(o, p):.2f} in")
    if new_pts:
        print("\nNEW points (nothing in frame.py within 6 in):")
        for p in new_pts:
            print(f"  ({p[0]:.2f}, {p[1]:.2f}, {p[2]:.2f})")
    gone = sorted(set(N) - matched - set(moved))
    if gone:
        print("\nNOT FOUND in the DXF (deleted, or moved more than 6 in):")
        print("  " + ", ".join(gone))
    if not (moved or new_pts or gone):
        print("No change: the DXF matches analysis/frame.py.")
        return

    print("\n--- paste into analysis/frame.py, _N (right-hand and centreline"
          " nodes only; _L nodes are generated) ---")
    for name, q in sorted(N.items()):
        if name.endswith("_L"): continue
        p = moved.get(name, [q])[0]
        print(f'    "{name}": ({p[0]:.1f}, {p[1]:.1f}, {p[2]:.1f}),')
    print("--- then re-run geometry-mesh.py, cad-export.py, visibility.py ---")
    print("\nNOTE: this reads POSITIONS only. New members, deleted members and")
    print("changed tube sizes have to be edited in _M by hand - the DXF has no")
    print("way to tell you which stock a line is meant to be.")


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--from-dxf":
        from_dxf(sys.argv[2]); sys.exit(0)
    os.makedirs(OUT, exist_ok=True)
    N, M = frame.nodes(), frame.members()
    export_3d(M, N)
    export_2d(M, N)
    export_scr(M)
    export_csv(M, N)
    dang, isl, miss = frame.check()
    if len(isl) > 1 or miss:
        print("\n*** READ THIS BEFORE YOU DRAW FROM THESE FILES ***")
        print(f"  The frame is in {len(isl)} disconnected pieces. Only the")
        print(f"  {len(isl[0])}-node cage box is welded together; everything")
        print("  else floats. Run `python3 analysis/frame.py` for the list,")
        print("  and see docs/open-questions.md for what each one needs.")
    tot = sum(frame.tube_weight(m["tube"], m["length"]) for m in M)
    print(f"\n{len(N)} nodes, {len(M)} members, "
          f"{sum(m['length'] for m in M):.0f} in of tube, {tot:.1f} lb")
    print("Units are INCHES. Datum: X aft from the prop plane, Y right, Z up,")
    print("ground at z=0. TUBE SIZES ARE PROVISIONAL - not for fabrication.")
