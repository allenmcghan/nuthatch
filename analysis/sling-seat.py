#!/usr/bin/env python3
"""Mesh sling seat: fabric tension at the crash load case, weight ledger,
and the bottom-out crush pad that keeps the energy-absorbing-seat property.
Load basis: common-airframe rule 1 - fixed-mass fittings at 6.4 g limit /
9.6 g ultimate, 200 lb structural pilot cap.
"""
G_ULT = 9.6
PILOT = 200.0
W = G_ULT*PILOT                     # lb, ultimate vertical through the seat

# sling geometry: rails ~18 in apart on the cage, static sag ~3.5 in,
# loaded depth of the seat panel ~16 in fore-aft
SPAN, SAG, DEPTH = 18.0, 3.5, 16.0
q = W/(DEPTH*SPAN)                   # lb/in^2 uniform pressure on the panel
H = q*SPAN**2/(8.0*SAG)              # horizontal tension per inch of rail (parabolic strip)
V = q*SPAN/2.0                       # vertical reaction per inch of rail, each side
import math
T = math.hypot(H, V)                 # resultant edge tension per inch of rail

print("=== SLING AT 9.6 g ULT x 200 LB PILOT = %.0f LB ===" % W)
print(f"  rails {SPAN:.0f} in apart, static sag {SAG:.1f} in, panel depth {DEPTH:.0f} in")
print(f"  edge tension ~{T:.0f} lb/in of rail")
print(f"  vinyl-coated polyester sling mesh (Phifertex-Plus class) breaking ~300-400 lb/in warp")
print(f"  margin before seam/lacing derate ~{300/T:.1f}x; with 50% seam derate ~{150/T:.1f}x")
print(f"  -> REQUIRED: doubled hems around the rails, and a static proof test of the")
print(f"     finished sling to {W:.0f} lb (sandbags) before first flight")

# crash energy: the sling is elastic (bad alone - stores and returns energy).
# Keep the energy-absorbing property with a crushable pad the sling bottoms
# onto: 2 in Confor/foam block on a light pan at the bay floor, positioned
# ~1.5 in below the 1-g sag point.
print("""
=== ENERGY ABSORPTION ===
  A sling alone is a spring: it stores vertical crash energy and gives it
  back (rebound), which is the opposite of what a spine wants. Keep the
  'energy-absorbing seat' property with a 2 in crushable pad (Confor/foam,
  ~0.7 lb) under the bottom-out point, ~1.5 in below the 1-g sag. Normal
  sitting never touches it; a hard impact strokes the sling into the pad,
  which crushes and does not rebound. Gear remains the primary absorber
  (8 fps / 6.6 in); the pad covers the beyond-gear case.
""")

print("=== WEIGHT ===")
items = [("mesh panel + hems (seat+back, ~1.3 yd^2)", 1.3),
         ("lacing / attachment hardware", 0.4),
         ("crush pad + light pan", 0.9),
         ("extra cage cross tube (1x, if rails not already present)", 0.6)]
tot = sum(x for _, x in items)
for n, x in items: print(f"  {n:52s} {x:4.1f} lb")
print(f"  {'total':52s} {tot:4.1f} lb  vs 5.0 lb pan+frame+Confor -> ~{5.0-tot:.1f} lb saved (unbanked)")
