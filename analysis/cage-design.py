#!/usr/bin/env python3
"""Cockpit cage architecture, wing attachment, and the steel-vs-aluminium
boom question re-opened fairly.
(1) all-steel boom options against the rev E aluminium choice, over the tube
sizes actually stocked; (2) where the wing loads enter the cage and what the
fittings carry; (3) the station convergence that lets one frame do three
jobs; (4) what an all-steel airframe costs in the 103 ledger.
Load basis: spar limit 2,331 lb / 3,472 ult; tail loads at Vne 62.
"""
import math

# ---------------- boom: steel options vs the rev E aluminium ----------------
ROOT, TAIL = 96.0, 182.0
ARM = TAIL - ROOT
M_REQ = 38034.0                       # in-lb ultimate, from fuselage-boom.py

def tube(D, t, Ftu, E, rho, knock=0.25):
    d = D - 2*t
    I = math.pi/64*(D**4 - d**4)
    S = 2*I/D
    Fb = min(Ftu, knock*0.6*E*t/(D/2))
    A = math.pi*(D - t)*t
    w = A*ARM*rho
    return I, S, Fb, Fb*S, w

AL = (42000, 10.0e6, 0.098)
ST = (95000, 29.0e6, 0.283)

print("=== 1. BOOM: ALL-STEEL OPTIONS vs THE REV E ALUMINIUM ===")
print("  required %.0f in-lb ultimate over a %.0f in arm\n" % (M_REQ, ARM))
print("  %-26s %7s %8s %10s %7s %8s" % ("tube", "S in3", "Fb ksi", "M all", "M.S.", "wt lb"))
cands = [("6061-T6 5.00 x .065  <-REV E", 5.00, 0.065, AL),
         ("4130   3.50 x .049", 3.50, 0.049, ST),
         ("4130   4.00 x .035", 4.00, 0.035, ST),
         ("4130   4.00 x .049", 4.00, 0.049, ST),
         ("4130   4.50 x .035", 4.50, 0.035, ST),
         ("4130   5.00 x .035", 5.00, 0.035, ST)]
best_steel = None
for name, D, t, mat in cands:
    I, S, Fb, Mall, w = tube(D, t, *mat)
    ms = Mall/M_REQ - 1
    flag = "" if ms > 0 else "  FAILS"
    print("  %-26s %7.3f %8.1f %10.0f %+6.0f%% %8.1f%s" % (name, S, Fb/1000, Mall, ms*100, w, flag))
    if "4130" in name and ms > 0.05 and (best_steel is None or w < best_steel[1]):
        best_steel = (name, w, ms)

_, _, _, _, w_al = tube(5.00, 0.065, *AL)
print(f"\n  lightest steel that clears with margin: {best_steel[0].strip()} at {best_steel[1]:.1f} lb ({best_steel[2]:+.0%})")
print(f"  rev E aluminium bare tube: {w_al:.1f} lb")
print(f"  STEEL PENALTY ON THE BOOM ITSELF: {best_steel[1]-w_al:+.1f} lb")
print("""
  Why it is only a few pounds, not double: a thin-wall boom is limited by
  LOCAL BUCKLING, not material strength, and steel's E is 2.9x aluminium's
  while its density is 2.89x. Those very nearly cancel - which is exactly
  why both materials show up on real booms. Steel does NOT get to use its
  95 ksi; at these wall thicknesses it buckles first.""")

# ---------------- joint credit: what steel buys back ----------------
print("=== 2. WHAT THE ALL-STEEL AIRFRAME BUYS BACK ===")
credits = [("boom-root fitting: welded cluster instead of a machined,\n     bonded/bolted sleeve joint into the steel cage", 1.2),
           ("tail-post fittings: welded instead of bolted brackets", 0.8),
           ("no dissimilar-metal isolation or galvanic detail", 0.2)]
tot_credit = sum(v for _, v in credits)
for n, v in credits: print(f"    -{v:.1f} lb  {n}")
net = best_steel[1] - w_al - tot_credit
print(f"    ----\n    joint credit {tot_credit:.1f} lb -> NET STEEL PENALTY {net:+.1f} lb")
print("""  Both fittings were flagged as 'copy dimension-for-dimension from a Kolb
  installation' precisely because an aluminium-boom-to-steel-cage joint is
  the fiddly part of the design. All-steel deletes that joint: the boom root
  becomes four welds into the aft cage frame, which is the same skill, the
  same jig and the same rod already required for the cage.""")

# ---------------- fatigue ----------------
print("=== 3. THE ARGUMENT NOBODY HAS MADE YET: FATIGUE ===")
print("""  4130 steel has a true ENDURANCE LIMIT (~45-50% of Ftu): below it, life
  is effectively infinite. 6061-T6 has NONE - every load cycle consumes life,
  forever, and the S-N curve keeps falling.
  This boom carries a two-stroke's vibration spectrum plus tail buffet at the
  end of an 86 in cantilever. Kolb has flown aluminium booms for 40 years, so
  this is not disqualifying - but an aluminium boom is a FATIGUE-MANAGED part
  needing a defined inspection interval, and a steel one, correctly sized,
  is not. On an aircraft whose flutter analysis does not yet exist and whose
  owner wants a lifetime airframe, that asymmetry is worth real weight.""")

# ---------------- wing attachment into the cage ----------------
print("=== 4. WHERE THE WING LOADS ENTER THE CAGE ===")
ULT = 3472.0                          # lb, both wings, ultimate
LE, CHORD = 48.0, 50.0
X_FS, X_RS = 0.25, 0.65               # spar positions, fraction chord
X_CP = 0.30                           # resultant lift, fraction chord
f_front = (X_RS - X_CP)/(X_RS - X_FS)
F_front, F_rear = ULT*f_front, ULT*(1 - f_front)
sta_fs, sta_rs = LE + X_FS*CHORD, LE + X_RS*CHORD
print(f"  ultimate wing lift {ULT:.0f} lb, resultant at {X_CP:.0%} chord")
print(f"  FRONT spar sta {sta_fs:.1f}: carries {f_front:.0%} = {F_front:5.0f} lb ult "
      f"({F_front/2:.0f} lb per side fitting)")
print(f"  REAR  spar sta {sta_rs:.1f}: carries {1-f_front:.0%} = {F_rear:5.0f} lb ult "
      f"({F_rear/2:.0f} lb per side fitting)")
print(f"""
  Sizing note: at {F_front/2:.0f} lb ultimate in double shear, a 3/8 in AN bolt
  (~{2*math.pi/4*0.375**2*36000:.0f} lb dbl shear in 4130 fittings) carries the front pin with margin.
  The fitting is bearing-critical, not bolt-critical - which is the same
  conclusion the wing-joint section reached for the spar splices.""")

# ---------------- the station convergence ----------------
CG, HOOP_STA = 63.0, 62.0
print("=== 5. THE CONVERGENCE THAT SHOULD SET THE CAGE ===")
print(f"  CG (30% MAC)                sta {CG:.1f}")
print(f"  front spar (25% chord)      sta {sta_fs:.1f}")
print(f"  rollover hoop, behind head  sta ~{HOOP_STA:.0f}")
print(f"  spread: {max(CG, sta_fs, HOOP_STA)-min(CG, sta_fs, HOOP_STA):.1f} in")
print("""
  Those three want to be the SAME FRAME. One heavy transverse hoop at
  sta ~61-63 then does three jobs at once:
    - carries 87% of wing lift straight into the cage
    - is the rollover structure over the pilot's head
    - puts the lift reaction at the CG, so wing load feeds no pitching couple
      into the fuselage and the cabane carries no fore-aft kick
  The rear spar frame at sta ~{0:.0f} is then a light frame - it only sees
  {1:.0f} lb ultimate - and can double as the seat-back / harness anchor frame.""".format(sta_rs, F_rear))

# ---------------- ledger ----------------
print("=== 6. LEDGER: CAN THE 103 KIT AFFORD ALL-STEEL? ===")
freed = {"flaps for slats": 1.0, "twist grip, pedals deleted": 2.0, "sling seat": 1.8}
spent = {"drag cleanup (SS21 proposal)": 1.6}
avail = sum(freed.values()) - sum(spent.values())
print(f"  freed by recent decisions: {sum(freed.values()):.1f} lb "
      f"({', '.join(f'{k} {v:.1f}' for k, v in freed.items())})")
print(f"  already proposed to spend: {sum(spent.values()):.1f} lb ({list(spent)[0]})")
print(f"  unspent margin: {avail:.1f} lb   |   steel boom net cost: {net:+.1f} lb")
print(f"  after an all-steel boom: {avail-net:.1f} lb left of the freed margin")
print("""
  So it fits - but it is not free, and it competes directly with the drag
  cleanup. Both together is {0:.1f} lb against {1:.1f} lb freed: affordable only
  because three decisions this week went the right way. Nothing else may be
  added without finding more.""".format(net + sum(spent.values()), sum(freed.values())))

# ---------------- pod aerodynamics: the closure angle ----------------
print("=== 7. IS THE POD ACTUALLY AERODYNAMIC? THE CLOSURE ANGLE ===")
secs = [(56, 15.0), (66, 14.0), (78, 11.0), (88, 7.0), (96, 3.0)]
print("  fabric pod run-out, half-height vs station:")
for i in range(len(secs)-1):
    (x1, h1), (x2, h2) = secs[i], secs[i+1]
    ang = math.degrees(math.atan((h1-h2)/(x2-x1)))
    flag = "  <- separates" if ang > 15 else ""
    print(f"    sta {x1:3.0f} -> {x2:3.0f}: {h1:4.1f} -> {h2:4.1f} in, closure {ang:4.1f} deg{flag}")
drop, run = 15.0-3.0, 96.0-56.0
print(f"  overall: {drop:.0f} in of closure in {run:.0f} in = {math.degrees(math.atan(drop/run)):.1f} deg")
print(f"  attached flow wants <= ~12-15 deg; to close at 12 deg would need "
      f"{drop/math.tan(math.radians(12)):.0f} in, i.e. taper starting at sta {96-drop/math.tan(math.radians(12)):.0f}")
print("""  which is forward of the pilot's shoulders - impossible. So:
  SOME AFT-BODY SEPARATION IS INHERENT to a pod-and-boom with a seated
  pilot, and every aircraft in this class lives with it. It is already
  inside the f = 0.45 the audit back-solved, so nothing here is a new
  penalty - but it does mean the honest moves are (a) start the closure as
  far forward as the shoulders allow, (b) keep the run-out a smooth curve
  with no kink, and (c) do NOT chase a fully closed teardrop: a slightly
  fuller base with the boom exiting cleanly beats a forced steep taper.""")
