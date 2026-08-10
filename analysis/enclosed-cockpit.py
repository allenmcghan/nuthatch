#!/usr/bin/env python3
"""Reclined pilot, wing lowered onto the cabin, full enclosure with doors.
(1) how far reclining drops the head and what it does to CG; (2) where the
wing then sits and what deleting the cabane is worth; (3) the drag prize;
(4) what the enclosure weighs and which aircraft can carry it.
Basis: 6'0" pilot, sling seat 1-g sag z=20, CG sta 63 must hold, wing chord
50 in at 12% thick, current wing chord line z=64.
"""
import math

# ---------------- 1. reclining ----------------
HIP_Z, HIP_STA = 20.0, 57.0
TRUNK, HEAD = 24.0, 12.0              # hip->shoulder, shoulder->head top
SIT = TRUNK + HEAD
print("=== 1. RECLINING THE PILOT ===")
print("  %-10s %10s %10s %12s" % ("recline", "head top z", "head sta", "vs upright"))
for th in (0, 25, 30, 35, 40):
    r = math.radians(th)
    ztop = HIP_Z + SIT*math.cos(r)
    xh = HIP_STA + SIT*math.sin(r)
    print("  %-10s %10.1f %10.1f %12s" % (f"{th} deg", ztop, xh,
          "-" if th == 0 else f"{ztop-(HIP_Z+SIT):+.1f} in"))

TH = 35.0
r = math.radians(TH)
head_z = HIP_Z + SIT*math.cos(r)
print(f"\n  Selected {TH:.0f} deg: head top z {head_z:.1f} (was {HIP_Z+SIT:.0f}) - "
      f"{HIP_Z+SIT-head_z:.1f} in lower.")

# CG: trunk + head swing aft about the hip; legs do not move
SEG = [("trunk", 0.50, 12.0), ("head+neck", 0.08, 32.0), ("arms", 0.10, 14.0)]
aft = sum(f*d*math.sin(r) for _, f, d in SEG)
print(f"  pilot CG moves aft {aft:.1f} in (trunk/head/arms swing, legs fixed)")
for W, G in ((170.0, 456.0), (200.0, 525.0)):
    print(f"    {W:.0f} lb pilot at {G:.0f} lb gross -> aircraft CG {W*aft/G:+.1f} in "
          f"= {W*aft/G/50*100:+.1f}% MAC")
print(f"""  FIX: move the seat FORWARD ~{aft:.0f} in (hip sta {HIP_STA:.0f} -> {HIP_STA-aft:.0f}) so pilot CG
  stays put and the aircraft CG never moves. The footwell is empty now that
  the rudder pedals are gone, so the room exists.""")

# ---------------- 2. wing height ----------------
ROOF_CLR = 5.5                        # head to cabin roof: 3 in was too tight to sit under
THICK = 0.12*50.0
z_lower = head_z + ROOF_CLR
z_chord = z_lower + THICK/2
Z_OLD = 64.0
print("=== 2. THE WING COMES DOWN ONTO THE CABIN ===")
print(f"  head top {head_z:.1f} + {ROOF_CLR:.0f} in clearance -> wing underside {z_lower:.1f}")
print(f"  chord line z {z_chord:.1f} (round to 58) vs {Z_OLD:.0f} today = {58-Z_OLD:.0f} in lower")
print(f"  old gap between pod top (~46) and wing underside (61): 15 in of open air")
print(f"  with cabane struts crossing it at the widest station. That is the")
print(f"  part that looks wrong, and it is wrong.")
CG_Z = 27.0
print(f"\n  Costs, honestly:")
print(f"   - roll: high-wing pendulum arm {Z_OLD-CG_Z:.0f} -> {58-CG_Z:.0f} in above CG, "
      f"{(58-CG_Z)/(Z_OLD-CG_Z)-1:+.0%}")
print(f"     On a two-axis aircraft dihedral IS roll control, so expect to add")
print(f"     ~0.5-1 deg of geometric dihedral back. Re-run the aero model.")
print(f"   - entry: ducking under a wing at {z_lower:.0f} in is worse than the 26 in")
print(f"     step-over the gear trade prized. Doors fix it for the EAB; the")
print(f"     open 103 gets a duck-and-sit.")
print(f"  Gains: cabane deleted entirely, thrust-to-wing offset shrinks, and the")
print(f"  wing root fairs straight into the cabin roof instead of standing off it.")

# ---------------- 3. drag ----------------
S, B, E = 130.0, 31.0, 0.75
AR = B*B/S
f_now = 0.45*10.7639
def ldm(f): return 0.5*math.sqrt(math.pi*E*AR/(f/S))
h_open, w_pod = 15.0, 11.5
h_recl = 13.0
A_open = math.pi*h_open*w_pod/144.0
A_recl = math.pi*h_recl*w_pod/144.0
CD_OPEN, CD_ENCL = 0.40, 0.15
f_open, f_encl = A_open*CD_OPEN, A_recl*CD_ENCL
print("=== 3. THE DRAG PRIZE - THIS IS WHY IT IS WORTH DOING ===")
print(f"  pod frontal: open/upright {A_open:.2f} ft^2, reclined {A_recl:.2f} ft^2")
print(f"  effective Cd: open cockpit w/ head in the breeze ~{CD_OPEN}, faired+enclosed ~{CD_ENCL}")
print(f"  f_pod {f_open:.2f} -> {f_encl:.2f} ft^2   ({f_encl-f_open:+.2f})")
d_cabane = 0.15
tot = (f_encl - f_open) - d_cabane
print(f"  cabane struts deleted: {-d_cabane:+.2f}")
print(f"  TOTAL {tot:+.2f} ft^2  ->  f {f_now:.2f} -> {f_now+tot:.2f}")
print(f"  L/D max {ldm(f_now):.1f} -> {ldm(f_now+tot):.1f}  ({ldm(f_now+tot)/ldm(f_now)-1:+.0%})")
f_both = f_now + tot - 0.60          # plus SS21 cleanup, less the overlap already counted
print(f"\n  stacked with the SS21 cleanup (net of overlap): f -> {f_both:.2f}, "
      f"L/D max {ldm(f_both):.1f} ({ldm(f_both)/ldm(f_now)-1:+.0%})")
print(f"  glide from 1,000 ft: {ldm(f_now)*1000/5280:.2f} -> {ldm(f_both)*1000/5280:.2f} miles")

# ---------------- 4. weight, and who can carry it ----------------
print("=== 4. WHAT IT WEIGHS, AND WHO CAN CARRY IT ===")
add = [("windshield, nose to wing, Lexan", 5.0),
       ("two doors: frames, glazing, hinges, latches", 8.0),
       ("door sills, posts, cabin closeout in the cage", 3.0),
       ("ventilation: NACA ducts + storm window", 1.0)]
rem = [("cabane struts and fittings deleted", 5.5),
       ("existing EAB windshield superseded", 4.0)]
a, rm = sum(v for _, v in add), sum(v for _, v in rem)
for n, v in add: print(f"    +{v:4.1f}  {n}")
for n, v in rem: print(f"    -{v:4.1f}  {n}")
print(f"    ----\n    enclosure kit net (EAB): {a-rm:+.1f} lb")
print(f"    airframe change alone (cabane deleted, both aircraft): {-5.5:+.1f} lb")

E103, CAP = 253.2, 254.0
EAB, GROSS, PILOT, FUEL = 275.7, 525.0, 200.0, 30.0
e103_new = E103 - 5.5
print(f"\n  103 kit: {E103:.1f} -> {e103_new:.1f} lb with the cabane gone "
      f"-> margin {CAP-e103_new:.1f} lb (was {CAP-E103:.1f})")
enc_103 = e103_new + (a - 4.0)        # 103 never had a windshield to supersede
print(f"  103 WITH the enclosure: {enc_103:.1f} lb -> OVER the cap by {enc_103-CAP:.1f} lb")
eab_new = EAB - 5.5 + (a - rm)
print(f"  EAB with enclosure: empty {eab_new:.1f}, all-up {eab_new+PILOT+FUEL:.1f} of {GROSS:.0f} "
      f"-> {'FITS' if eab_new+PILOT+FUEL <= GROSS else 'OVER'}")
print(f"""
  VERDICT, and it keeps the fleet rule intact:
   - WING ONTO THE CABIN + CABANE DELETED is an AIRFRAME change, so BOTH
     aircraft get it, and the 103 kit gains {CAP-e103_new:.1f} lb of margin - which is more
     than the steel boom and the drag cleanup were about to spend.
   - THE ENCLOSURE (doors + full windshield) is an EAB KIT ITEM, exactly like
     the windshield and tablet already are. Door hard points live in the cage
     as permanent grams; the doors bolt on or stay home.
   - Aircraft #2 (the pure 103) therefore flies OPEN under the same wing,
     with the same cage. Two configurations, one airframe - unchanged rule.""")
