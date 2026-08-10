#!/usr/bin/env python3
"""Thin-film glazing and ram-air ventilation for the rev G cabin.
(1) what film weighs against Lexan; (2) whether it stays taut at speed -
and the ducts turn out to help; (3) ram-air flow and the cooling it buys;
(4) what the enclosure actually buys in winter, in degrees; (5) egress by cutter,
and the cut path it forces.
"""
import math

RHO = 0.002377
def q(mph): return 0.5*RHO*(mph*1.4667)**2

# ---------------- 1. weight, split by material ----------------
A_RIGID, A_FILM = 12.0, 10.0           # windshield + upper sides / two doors
RHO_PC, RHO_PVC = 0.0433, 0.047
print("=== 1. GLAZING, SPLIT: LEXAN WINDSHIELD + FILM DOORS ===")
print("  %-38s %8s %9s %9s" % ("panel", "thick in", "lb/ft^2", "lb"))
for n, t, rho, a in [("windshield+upper, Lexan 0.040", 0.040, RHO_PC, A_RIGID),
                     ("windshield+upper, Lexan 0.060", 0.060, RHO_PC, A_RIGID),
                     ("windshield+upper, Lexan 0.093", 0.093, RHO_PC, A_RIGID),
                     ("two doors, PVC film 20 mil", 0.020, RHO_PVC, A_FILM)]:
    psf = t*rho*144.0
    print("  %-38s %8.3f %9.3f %9.1f" % (n, t, psf, psf*a))
w_rigid = 0.040*RHO_PC*144.0*A_RIGID
w_doors = 0.020*RHO_PVC*144.0*A_FILM
w_film = w_rigid + w_doors             # total glazing, used by the ledger below
w_lex = 0.060*RHO_PC*144.0*22.0
print(f"\n  SELECTED: 0.040 Lexan {w_rigid:.1f} + 20 mil film doors {w_doors:.1f} = {w_film:.1f} lb")
print(f"  all-film would be {0.020*RHO_PVC*144.0*22.0:.1f}; all-Lexan 0.060 would be {w_lex:.1f}")
print(f"  So the split costs {w_film - 0.020*RHO_PVC*144.0*22.0:+.1f} lb against all-film and buys:""")
print("""   - the forward view through OPTICAL-GRADE RIGID PANEL, which retires the
     distortion worry a 14-17 deg raked film windshield would have had;
   - a windshield that cannot propagate a tear at all - polycarbonate crazes
     and cracks locally, it does not RUN like a tensioned membrane.

  THREE THINGS THIN LEXAN BRINGS THAT FILM DID NOT:""")
CTE_PC, CTE_ST, SPAN, DT = 3.8e-5, 6.3e-6, 40.0, 120.0
grow = SPAN*(CTE_PC - CTE_ST)*DT
print(f"   - THERMAL FLOAT. Polycarbonate expands ~6x steel. Over a {SPAN:.0f} in")
print(f"     windshield and a {DT:.0f} F swing (winter dawn to sitting in summer sun)")
print(f"     it moves {grow:.2f} in relative to the frame. Oversized holes (+1/8 to")
print(f"     3/16) or a floating rubber channel - NEVER clamped hard, or it cracks.")
print("""   - OIL-CANNING. 0.040 is thin for a 12 ft^2 wrapped panel; it may need an
     intermediate frame member, or stepping to 0.060 (+1.5 lb). Check on the
     mockup before the frame is welded.
   - SOLVENT CRAZING. Polycarbonate is attacked by many cleaners and fuels.
     Specify the cleaning method in the manual; keep it out of the fuel path.""")

# ---------------- 2. does it stay taut? ----------------
print("=== 2. DOES IT STAY TAUT - AND THE DUCTS HELP ===")
for mph in (35, 55, 62):
    print(f"  {mph} mph: q = {q(mph):.2f} psf = {q(mph)/144:.4f} psi")
PANEL_W, BULGE = 20.0, 1.0
R = (PANEL_W/2)**2/(2*BULGE)
p_cab = 0.5*q(55)/144
T = p_cab*R
print(f"""
  A stretched film in an airstream drums and flutters unless it is tensioned.
  The vents fix that for free: ram air pressurises the cabin, and internal
  pressure puts the film into tension from the inside - the same trick that
  makes an inflatable rigid.
  cabin at 50% of ram at 55 mph = {p_cab:.4f} psi; a {PANEL_W:.0f} in panel bulging {BULGE:.0f} in
  runs radius {R:.0f} in and edge tension {T:.2f} lb/in - trivial for vinyl, which
  takes 20+ lb/in. So the panels go drum-taut in flight and slack on the
  ground, which is exactly the right way round.
  COROLLARY: the outlet must be SMALLER than the inlet, or there is no
  pressurisation and the film flaps. Size the spill vent deliberately.""")

# ---------------- 3. ram air and cooling ----------------
print("=== 3. RAM AIR: HOW BIG DO THE DUCTS NEED TO BE? ===")
RECOV = 0.75                           # NACA submerged inlet pressure recovery
def cfm(area_in2, mph): return area_in2/144.0*(mph*1.4667)*60.0*RECOV
print("  %-16s %12s %12s" % ("inlet area", "CFM @ 35", "CFM @ 55"))
for a in (4, 6, 8, 12):
    print("  %-16s %12.0f %12.0f" % (f"{a} in^2", cfm(a, 35), cfm(a, 55)))
HEAT = 1500.0                          # BTU/hr: pilot ~500 + solar through glazing ~1000
CP, RHO_A = 0.24, 0.0765
for dT in (5, 10):
    need = HEAT/(CP*dT)/60.0/RHO_A
    print(f"  to hold cabin within {dT:2.0f} F of ambient against {HEAT:.0f} BTU/hr: {need:.0f} CFM")
print(f"""  So TWO NACA ducts of ~2 x 2 in (8 in^2 total) deliver ~{cfm(8,55):.0f} CFM at cruise -
  comfortably inside the {HEAT/(CP*10)/60.0/RHO_A:.0f} CFM that holds 10 F over ambient. This is a
  small, easy inlet, not a big one.
  Put the ducts in RIGID structure, not in the film: a NACA submerged inlet
  depends on a precise 7 deg ramp and sharp diverging lips, and it cannot hold
  that shape in a stretched membrane. At 55 mph a plain scoop is nearly as
  good and far easier - NACA is worth it for looks and cleanliness, not for
  measurable drag at this speed.""")

# ---------------- 4. winter ----------------
def windchill(T, V):
    v = V**0.16
    return 35.74 + 0.6215*T - 35.75*v + 0.4275*T*v
print("=== 4. WHAT THE ENCLOSURE ACTUALLY BUYS IN WINTER ===")
print("  %-12s %14s %14s %10s" % ("ambient", "open @ 55 mph", "enclosed", "gain"))
for T in (50, 40, 30, 20):
    wc = windchill(T, 55.0)
    print("  %-12s %11.0f F %11.0f F %9.0f F" % (f"{T} F", wc, T, T-wc))
print("""
  That is the honest framing: the cabin does not make you WARM, it removes
  55 mph of wind chill - worth roughly 20 F. Thin film has essentially no
  R-value, so still-air-at-ambient is what you get, and you dress for that.
  AND YOU CANNOT CLOSE EVERYTHING. A warm pilot inside cold film fogs it
  instantly. Keep a small defog trickle onto the windshield at all times -
  standard practice, and the reason every closed aircraft has a defrost duct.
  Specify COLD-CRACK-RATED vinyl: ordinary clear PVC embrittles and cracks
  around 20-30 F, marine grades are rated to -20 F or below. This is a
  specification, not a preference, for an aircraft meant to fly in winter.""")

# ---------------- 5. egress: cutters, and the cut path ----------------
print("=== 5. EGRESS BY CUTTER (owner decision) ===")
print("""  Decision: a seatbelt cutter and a film cutter carried in the cab, rather
  than an edge-release panel. That is defensible, and probably better:

   - Plasticised PVC elongates 200-400% before it breaks, so 'push through it'
     was never going to work - a shoulder BALLOONS it like a trampoline. A
     blade is the honest way through thin vinyl.
   - The release-force window I proposed is uncomfortably narrow anyway. The
     panel must hold ~0.027 psi of cabin pressure (about 25 lb spread over a
     door) plus gusts, yet let go under a shoulder. Fasteners that satisfy
     both drift toward the wrong end as UV ages them, and a door departing in
     flight on a two-axis aircraft is its own emergency.
   - So: attach the film POSITIVELY, with no release mechanism to fail or
     drift, and cut your way out.""")

PANEL_L, PANEL_H = 38.0, 24.0          # door panel, sta 40-78 x z 27-51
TEAR_LBF = 10.0                        # ~ASTM D1004 propagation, 20 mil flexible PVC
print(f"""
  TIMING - CORRECTED DOWNWARD. My first estimate cut the whole panel out and
  came to 7-10 s. That was wrong: for a thin film, tear PROPAGATION is far
  cheaper than tear INITIATION, which is the whole principle behind a
  'tear here' notch. Once a cut exists, 20 mil flexible PVC propagates at
  roughly {TEAR_LBF:.0f} lbf of steady pull - well inside a one-handed grab.
  So: ONE DIAGONAL CUT from a corner, grab the triangular flap, and tear.""")
for lbl, cut_s in (("cut the full perimeter (my first estimate)", 5.7),
                   ("one diagonal cut, then tear", 2.0)):
    print(f"    {lbl:44s} {cut_s:4.1f} s + 2-3 s reach = {cut_s+2.5:4.1f} s")
print("""  Revised: 4-5 s. That moves the fire case from MARGINAL to ACCEPTABLE,
  which is the only case that was ever in question.""")

print(f"""
  THE SAME PROPERTY IS A FLIGHT HAZARD, and this is the part worth adding.
  A membrane that tears at {TEAR_LBF:.0f} lbf once nicked is a membrane that will tear
  IN FLIGHT once nicked - and section 2 deliberately tensions it with cabin
  pressure, which primes it. A stone off the nosewheel, an abrasion at a
  frame edge, a UV-hardened spot in year three: any of them can run.
  At Vne, q = {q(62)/144:.4f} psi and a lifted flap edge peels at more than {TEAR_LBF:.0f} lbf.

  BUT THE SPLIT IN SECTION 1 ALREADY SOLVES MOST OF IT, which is the useful
  part: film is now ONLY the two doors.
   - The windshield - the panel actually exposed to stones off the nosewheel
     and to prop wash - is rigid Lexan, which crazes locally and CANNOT run.
     The tensioned-membrane hazard leaves the forward, low, dirty zone
     entirely.
   - The doors sit high on the sides at sta 40-78, out of the spray, and are
     ALREADY individually bounded panels. The bead track around each one is
     the ripstop; a tear runs to that frame and stops.
   - So the earlier 'subdivide the glazing at every cage member' requirement
     RELAXES to: keep each door a single bounded panel, which it already is.
   - Do NOT reach for scrim-reinforced (mesh) vinyl to fix this. It would
     stop tears, and it would also stop the egress plan; the sling seat uses
     that material precisely because it must NOT tear.
   - Inspect edges at every condition check. Film is a consumable; a nicked
     panel gets replaced, not flown.
""")

print("""  Requirements, so this is a plan and not a hope:
   - TWO cutters, one each side, so a jammed or blocked side does not matter.
   - MOUNTED, not stowed: fixed brackets within reach of a harnessed pilot,
     findable BY FEEL, and retained - a dropped cutter in a rolled cabin is
     gone.
   - Reachable IN GLOVES. This aircraft is meant to fly in winter, and gloves
     are exactly when fumbling for a small tool fails.
   - PROOF TEST, replacing the shove test: timed egress from a fully
     assembled panel, in a harness, both sides, wearing gloves.
  What it does NOT cover, honestly: unconscious or pinned. Nothing in this
  weight class does - the BRS covers in-flight and the cage covers impact.""")
w_cut = 2*1.5/16 + 0.1
print(f"\n  weight: two cutters ~{2*1.5:.0f} oz + brackets = {w_cut:.1f} lb,")
print(f"  and it DELETES the zip and the release-force tuning from the kit.")

# ---------------- 6. the ledger, with the split glazing ----------------
print("=== 6. LEDGER, WITH LEXAN WINDSHIELD + FILM DOORS ===")
kit = [("windshield + upper sides, 0.040 Lexan", w_rigid),
       ("two doors, 20 mil film", w_doors),
       ("two door frames, light tube", 3.0),
       ("windshield frame / floating channel", 1.0),
       ("bead track and fasteners (positive, no release)", 0.8),
       ("two mounted cutters + brackets", 0.3),
       ("NACA ducts + closable valves + defog", 1.0),
       ("cabin closeout and sills in the cage", 2.0)]
tot = sum(v for _, v in kit)
for n, v in kit: print(f"    +{v:4.1f}  {n}")
print(f"    ----\n    enclosure kit gross {tot:.1f} lb  (17.0 if it were all 0.060 Lexan)")

E103, CAP = 247.7, 254.0               # after the rev G cabane deletion
print(f"\n  EAB kit: {tot:.1f} - 4.0 (old Lexan windshield line superseded) = {tot-4:.1f} lb net")
print(f"  103 with the FULL enclosure: {E103:.1f} + {tot:.1f} = {E103+tot:.1f} -> over by {E103+tot-CAP:.1f}")
strip_lex = w_rigid + 1.0 + 1.0        # Lexan windshield + its frame + ducts, no doors
strip_flm = 0.020*RHO_PVC*144.0*A_RIGID + 0.5 + 1.0
print(f"  103, WINDSHIELD + VENTS ONLY (no doors):")
print(f"    with the EAB's 0.040 Lexan windshield: +{strip_lex:.1f} -> {E103+strip_lex:.1f}, "
      f"margin {CAP-E103-strip_lex:.1f} lb")
print(f"    with a FILM windshield instead:        +{strip_flm:.1f} -> {E103+strip_flm:.1f}, "
      f"margin {CAP-E103-strip_flm:.1f} lb")
print(f"""
  So the split costs the 103 about {strip_lex-strip_flm:.1f} lb of its margin, and there is a
  clean fleet answer: GLAZING IS A KIT ITEM EITHER WAY. The EAB gets the
  Lexan windshield, because it is the aircraft that will be flown fast, far
  and in weather, and the optical quality is worth {strip_lex-strip_flm:.1f} lb there. Avery's
  103 can keep a FILM windshield and hold {CAP-E103-strip_flm:.1f} lb of margin - same cage,
  same frame, same bead track, different sheet in it.
  Both aircraft still carry the doors as film if fitted, and the egress plan
  is unchanged because THE DOORS ARE THE ESCAPE PATH in either build.""")
