# ---- the two weight statements in the repo ----
# measured-weights.csv (group,item,est)
CSV=[("Wing","Spar",22),("Wing","Ribs",8),("Wing","D-tube",12),("Wing","Rear spar",5),
("Wing","TE stock",3),("Wing","Spoilerons",4),("Wing","SLATS",6),("Wing","Joints",7),
("Wing","Fabric wing",14),("Wing","Misc hw",4),
("Fus","Longerons+",31),("Fus","Nose bow",5),("Fus","Rollover hoop",4),("Fus","CABANE",6),
("Fus","Seat",5),("Fus","Harness",3),("Fus","Turtledeck",3),("Fus","Fabric fus",5.5),("Fus","Windshield",4),
("Tail","HStab+elev",12),("Tail","Fin+rudder",6),("Tail","Fittings",2),
("Gear","Main legs",8),("Gear","Wheels/tires",12),("Gear","Brakes",2),("Gear","Nose gear",12),("Gear","Mounts",4),
("Ctl","Stick/elev",7),("Ctl","Pedals",5),("Ctl","Spoileron rig",4),
("Pwr","Hirth F-33",35),("Pwr","Redrive",10),("Pwr","Prop",8),("Pwr","Mount",5),("Pwr","Fuel sys",8),
("Sys","Junco+tablet",4),("Sys","Wiring",3),("Sys","BRS hardpts",3),("Sys","AN/paint",8)]
# workbook Weight sheet (est, 103strip)
XLSX=[("Spar",22,22),("Ribs",8,8),("D-tube",12,12),("Rear spar",5,5),("TE",3,3),("Joints",7,7),
("Spoilerons",4,4),("Fabric wing",14,11.5),("Wing misc",4,4),
("Longerons",28,28),("Gussets",3,3),("Nose bow",4,4),("Hoop",4,4),("Seat",6,6),("Harness",4,4),
("Turtledeck",3,3),("Fabric fus",6,5),("Windshield",4,0),
("HStab",12,11),("Fin",6,5.5),("Tail fittings",2,2),
("Main legs",8,7),("Wheels",12,8),("Brakes",3,3),("Nose gear",12,9),("Gear mounts",3,3),
("Stick",7,7),("Pedals",5,5),("Spoileron rig",4,4),
("Hirth",35,28),("Redrive",10,0),("Prop",8,7),("Mount",5,4),("Fuel",8,5),
("Junco",4,0),("Wiring",2,0),("BRS",3,3),("AN/paint",6,5)]
csv_t=sum(x[2] for x in CSV); x_e=sum(x[1] for x in XLSX); x_s=sum(x[2] for x in XLSX)
print("=== RECONCILIATION FIRST =================================================")
print("measured-weights.csv EAB total:   %.1f lb"%csv_t)
print("workbook Weight sheet EAB total:  %.1f lb  (this is the README's 296)"%x_e)
print("workbook 103 strip total:         %.1f lb  (claimed margin to 254: %.1f)"%(x_s,254-x_s))
print()
print("Delta csv - workbook = %.1f lb. Items in the CSV that the WORKBOOK OMITS:"%(csv_t-x_e))
print("  SLATS (6 lb)  and  CABANE / wing carry-through (6 lb)")
print("  (small offsets elsewhere: longerons 31 vs 28+3, nose bow 5v4, seat 5v6,")
print("   harness 3v4, fus fabric 5.5v6, brakes 2v3, mounts 4v3, wiring 3v2, AN 8v6)")
print()
print("With slats+cabane restored, honest totals:")
print("  EAB empty:   %.1f lb (not 296)"%(x_e+12))
print("  103 strip:   %.1f lb -> %+.1f lb vs the 254 limit: OVER, not 4 under"%(x_s+12,254-(x_s+12)))
import math
# 103-FIRST BUILD: one aircraft, F-33 kept, every line scrubbed.
# (item, honest baseline lb, scrubbed lb, station, note)
C=[
("Spar, 1.25 sch40 caps + web",22,22,72,"KEEP. Vne 62 placard instead of +6-10 lb of cap (audit F1 option 1)"),
("Ribs, 31 fir truss",8,8,74,"KEEP - already beats foam by 6.5 lb"),
("D-tube LE, 1/16 birch",12,10.5,60,"1/32 ply outboard of the joint, 1/16 inboard; shear falls with span"),
("Rear spar / spoileron spar",5,5,86,"KEEP"),
("TE stock",3,2.5,100,"smaller section, CNC-cut"),
("Slats, full span",6,6,58,"KEEP - they ARE the 24 kt compliance"),
("Wing joints, rods+sleeves+bolts",7,7,68,"KEEP - bearing-governed, do not thin"),
("Spoilerons + springs",4,4,82,"KEEP"),
("Wing fabric: Stewart->Oratex",14,9.5,74,"Oratex 600: -4.5 lb AND -50 hr on the wing"),
("Wing misc hw",4,3.5,72,"laser-cut brackets replace hand-cut + stock"),
("Longerons+gussets 4130",31,29,84,"wall-by-member optimization w/ laser gusset pkg; -2 honest"),
("Nose bow",5,4,30,"as workbook"),
("Rollover hoop",4,4,54,"KEEP - safety package is the point"),
("Cabane / carry-through",6,5,68,"machined lugs vs welded clusters"),
("Seat + Confor",5,5,58,"KEEP"),
("5-pt harness",3,3,58,"KEEP"),
("Turtledeck",3,1.5,110,"fabric over 3 stringers, no formers aft of hoop"),
("Fus fabric: Oratex",5.5,3.7,84,"-1.8"),
("Windshield",4,0,42,"DELETE (103 strip already does)"),
("HStab+elevator",12,11,184,"Oratex + gauge check; tail arm loves every pound"),
("Fin+rudder",6,5.5,180,"same"),
("Tail fittings",2,2,182,"KEEP"),
("Main gear legs",8,8,80,"KEEP - sprung 4130 is the crash structure"),
("Main wheels/tires 5.00-5 -> 13in",12,7,80,"lighter rims+tires; grass field ok at 424 gross"),
("Bicycle discs",2,2.5,80,"KEEP - brakes are a design win"),
("Nose gear",12,9,36,"as 103 strip: smaller wheel, simpler steering"),
("Gear mounts",4,3,60,""),
("Stick + elevator run",7,6.5,60,"CNC bellcranks"),
("Pedals + cables",5,4.5,100,""),
("Spoileron rig + symmetric lever",4,4.5,74,"+0.5: the both-up landing mode from the audit"),
("Hirth F-33 w/ exhaust",35,35,14,"KEEP - dual CDI is the safety case"),
("Belt redrive",10,10,10,"KEEP - audit F4: direct drive cannot fly the field"),
("Prop, 60in COMPLIANCE PITCH",8,7,2,"flat pitch = 55kt cap + monster climb; carve later"),
("Engine mount",5,4.5,18,"laser-cut tabs"),
("Fuel tank 5gal + lines",8,5,50,"rotomolded poly + minimal plumbing; 5 gal IS the 103 limit"),
("Junco: ESP32 logger only",4,1,44,"no tablet/mount on the compliance aircraft"),
("Wiring/master",3,1.5,50,"one battery, one bus"),
("BRS hardpoints",3,3,70,"KEEP - and the CHUTE ITSELF is excluded from 254 by 103.1(e)(1)"),
("AN hw, placards; NO PAINT",8,5,78,"Oratex needs no paint - that was ~2-3 lb of the 8"),
]
base=sum(r[1] for r in C); scrub=sum(r[2] for r in C)
mom=sum(r[2]*r[3] for r in C)
print("%-38s %6s %6s  %s"%("item","base","scrub","note"))
for r in C:
    d=r[2]-r[1]
    print("%-38s %6.1f %6.1f  %s%s"%(r[0],r[1],r[2],("[%+.1f] "%d if abs(d)>0.01 else ""),r[4][:52]))
print("-"*100)
print("%-38s %6.1f %6.1f   saved %.1f lb"%("TOTAL EMPTY",base,scrub,base-scrub))
print()
print("vs 254 limit: %+.1f lb"%(scrub-254))
cg=mom/scrub
print("empty CG station %.1f (%.0f%% MAC) - baseline was 66.5, F-33 stays forward: OK"%(cg,(cg-48)/50*100))
print()
# compliance checks at this weight
LB=4.44822;rho=1.225;S=12.077;b=9.449
def vs(W,CL=1.8): return math.sqrt(2*W*LB/(rho*S*CL))*2.23694
for W,lbl in ((scrub+170+30,"170 lb pilot + 5 gal"),(scrub+220+30,"220 lb pilot + 5 gal")):
    v=vs(W)
    print("gross %.0f (%s): power-off stall %.1f mph = %.1f kt vs 24.0 limit %s"
          %(W,lbl,v,v/1.15078,"OK" if v/1.15078<=24 else "OVER"))
# climb at 424ish with 28hp flat prop (eta climb 0.72 still)
W=scrub+170+30
Vy=vs(W)/2.23694*1.15
P=0.5*rho*Vy**3*0.519+2*(W*LB)**2/(rho*Vy*math.pi*b*b*0.85)
roc=(28*745.7*0.72-P)/(W*LB)*196.85
print("climb at %.0f lb, F-33, climb prop: ~%.0f fpm ; ground roll ~%.0f ft"
      %(W,roc, (vs(W)/2.23694*1.15)**2/(2*9.81*(0.85*230/W-0.1))*3.28084))
print()
print("Remaining gap options if the scrub lands over:")
print("  carbon spar caps    -12 lb   (design-log 7 rejected: uninspectable - NOT recommended)")
print("  drop main brakes    -2.5 lb  (fights the safety package)")
print("  smaller Hstab       -1-2 lb  (gate-3 says SM has margin; needs re-run)")
print("  actual BRS chute:   +18-20 lb INSTALLED but EXCLUDED from the 254 count")
