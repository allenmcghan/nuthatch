import math
LB=4.44822;rho=1.225;S=12.077;b=9.449
# scrubbed AIRFRAME (no power package, no windshield/tablet): item, lb, station
AIR=[("Spar",22,72),("Ribs",8,74),("D-tube",10.5,60),("Rear spar",5,86),("TE",2.5,100),
("Slats",6,58),("Joints",7,68),("Spoilerons",4,82),("Wing fabric",9.5,74),("Wing misc",3.5,72),
("Longerons",29,84),("Nose bow",4,30),("Hoop",4,54),("Cabane",5,68),("Seat",5,58),
("Harness",3,58),("Turtledeck",1.5,110),("Fus fabric",3.7,84),
("HStab",11,184),("Fin",5.5,180),("Tail fit",2,182),
("Main legs",8,80),("Wheels",7,80),("Brakes",2.5,80),("Nose gear",9,36),("Gear mounts",3,60),
("Stick",6.5,60),("Pedals",4.5,100),("Spoileron rig",4.5,74),
("Fuel sys",5,50),("Logger",1,44),("Wiring",1.5,50),("BRS pts",3,70),("AN hw",5,78)]
airframe=sum(a[1] for a in AIR); m_air=sum(a[1]*a[2] for a in AIR)
print("COMMON AIRFRAME (everything but power, windshield, tablet): %.1f lb"%airframe)

P103=[("Thor DS engine w/ redrive",31,14),("Prop 53in",5.5,2),("Mount adapter",4.5,18)]
EAB =[("Hirth F-33",35,14),("Belt redrive",10,10),("Prop 60in",7,2),("Mount adapter",4.5,18),
      ("Windshield",4,42),("Junco tablet",3,44)]
for pkg,lbl in ((P103,"PART 103 config"),(EAB,"EAB config")):
    w=airframe+sum(p[1] for p in pkg); m=m_air+sum(p[1]*p[2] for p in pkg)
    print("\n%s: empty %.1f lb, empty CG sta %.1f"%(lbl,w,m/w))
    for pil,fu in ((130,30),(170,30),(220,30),(170,0)):
        g=w+pil+fu; cg=(m+pil*58+fu*50)/g
        mac=(cg-48)/50*100
        vs=math.sqrt(2*g*LB/(rho*S*1.8))*2.23694
        n_lim=2331.0/g
        print("   pilot %3d fuel %2d: gross %3.0f  CG %4.1f%% MAC %s | Vs %4.1f mph (%4.1f kt) | n_lim(abs) %.2f g"
              %(pil,fu,g,mac,"OK" if 25<=mac<=35 else "OUT",vs,vs/1.15078,n_lim))
print()
print("COMMON LOAD BASIS: wing as documented = 2,331 lb limit / 3,472 lb ultimate ABSOLUTE.")
print("Max attainable lift depends only on q: q(V)*S*1.8*1.5 <= 3472  ->  Vne <= %.1f mph"
      %(math.sqrt(2*(3472/1.5)*LB/(rho*S*1.8))*2.23694))
for V in (62,):
    L=0.5*rho*(V/2.23694)**2*S*1.8/LB
    print("At Vne %d: max attainable lift %.0f lb <= 2331 limit -> stall-protected AT EVERY GROSS."%(V,L))
print("Same placard, both configs, zero added spar weight. EAB cruise placard ~0.9*Vne = 56 mph.")
print()
print("If instead the EAB keeps Vne 69 (cruise 60): spar +6-10 lb ON THE COMMON AIRFRAME")
print("  -> 103 config %.1f + 7 = %.1f lb: fails 254, and stall gate fails too. Not available."
      %(airframe+41,airframe+41+7))
