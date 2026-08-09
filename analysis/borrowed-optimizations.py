#!/usr/bin/env python3
"""What the ultralight/STOL world does that this design hasn't mined yet.
Three quantified items: (1) drag cleanup on the 80% the audit flagged and
never attacked, (2) elevator stick force -> the missing pitch trim system,
(3) control-surface gap seals on NACA TN-632's real numbers - including the
sealed-and-smaller rudder option, which matters because the rudder is worked
by a wrist.
Basis: audit drag model f = 0.45 m^2 total, smooth airframe 0.084 m^2, e 0.75.
"""
import math

S, B = 130.0, 31.0
AR = B**2/S
E = 0.75                       # audit's corrected Oswald, not the old 0.85
F_TOT_M2, F_AIRFRAME_M2 = 0.45, 0.084
M2_FT2 = 10.7639
f_tot = F_TOT_M2*M2_FT2
f_air = F_AIRFRAME_M2*M2_FT2
f_house = f_tot - f_air
W103, W_EAB = 456.0, 525.0
RHO = 0.002377

def q(mph): return 0.5*RHO*(mph*1.4667)**2
def ld_max(f): return 0.5*math.sqrt(math.pi*E*AR/(f/S))
def cruise(f, W, mph):
    qq = q(mph); cl = W/(qq*S)
    cd = f/S + cl**2/(math.pi*AR*E)
    D = cd*qq*S
    return cl/cd, D, D*mph*1.4667/550.0

print("=== 1. THE 80% NOBODY HAS ATTACKED ===")
print(f"  AR {AR:.2f}, e {E}")
print(f"  total f {f_tot:.2f} ft^2 | smooth airframe {f_air:.2f} | "
      f"cockpit+pilot+gear+rigging {f_house:.2f} ft^2 ({f_house/f_tot:.0%})")
print()
print("  Estimated housekeeping breakdown (ENGINEERING ESTIMATE, not measured):")
items = [
    ("3 spoked bicycle wheels, bare", 3*0.48*0.65, "0.48 ft^2 frontal ea, Cd~0.65 spoked"),
    ("gear legs, cabane, exposed tubes", 0.30, "round tube Cd 1.2"),
    ("pilot head/shoulders + cockpit opening", 2.10, "back-solved remainder"),
    ("cooling + rigging + leaks", 0.60, ""),
]
tot_est = sum(v for _, v, _ in items)
for n, v, note in items:
    print(f"    {n:44s} {v:5.2f} ft^2  {note}")
print(f"    {'estimated total':44s} {tot_est:5.2f} vs {f_house:.2f} carried "
      f"-> scale factor {f_house/tot_est:.2f}")
print()
print("  Cleanup scenarios (fairings borrowed from ultralight practice):")
print("  %-34s %7s %8s %8s %9s %9s" % ("case", "f ft^2", "L/Dmax", "L/D cr", "hp @50", "glide mi"))
for label, cut in [("today", 0.0), ("wheel covers, mains only", 0.30),
                   ("+ nose wheel + leg fairings", 0.55),
                   ("+ footwell closeout, windscreen", 0.95),
                   ("aggressive (all of the above, tuned)", 1.35)]:
    f = f_tot - cut
    ldm = ld_max(f); ldc, D, hp = cruise(f, W103, 50.0)
    print("  %-34s %7.2f %8.2f %8.2f %9.2f %9.2f" % (label, f, ldm, ldc, hp, ldm*1000/5280))
print()
f_best = f_tot - 0.95
ldc0 = cruise(f_tot, W103, 50)[0]; ldc1 = cruise(f_best, W103, 50)[0]
hp0 = cruise(f_tot, W103, 50)[2]; hp1 = cruise(f_best, W103, 50)[2]
print(f"  Realistic target (-0.95 ft^2, -20% of f): cruise L/D {ldc0:.2f} -> {ldc1:.2f} (+{ldc1/ldc0-1:.0%}),")
print(f"  cruise power {hp0:.2f} -> {hp1:.2f} hp (-{1-hp1/hp0:.0%}) -> same % as climb margin or endurance.")
print(f"  Weight cost ~1.6 lb. Today's decisions freed ~4.8 lb unbanked")
print(f"  (flaps -1, twist grip -2, sling seat -1.8): the margin exists to buy this.")

print("\n=== 2. THE MISSING PITCH TRIM SYSTEM ===")
S_H, ELEV_FRAC = 30.0, 0.45
S_E = S_H*ELEV_FRAC
C_E = 3.0*ELEV_FRAC            # tail chord 3 ft
CH_D = 0.008                   # per deg, plain unbalanced
GEAR_DEG_IN = 4.5              # trim-tail gate-3 gearing
print("  elevator %.1f ft^2, chord %.2f ft, gearing %.1f deg/in" % (S_E, C_E, GEAR_DEG_IN))
print("  %-28s %6s %10s %11s" % ("condition", "defl", "HM in-lb", "stick lb"))
for label, mph, defl in [("cruise 50 mph, 1 g", 50, 3.0),
                         ("slow 35 mph, 1 g", 35, 6.0),
                         ("climb 40 mph full power", 40, 4.5),
                         ("Vne 62 descent", 62, 2.0)]:
    hm = CH_D*defl*q(mph)*S_E*C_E*12.0
    force = hm*math.radians(GEAR_DEG_IN)
    print("  %-28s %5.1f%s %10.0f %11.1f" % (label, defl, chr(176), hm, force))
print("""
  2-4 lb of continuous stick force is exactly the band that needs trim.
  It matters MORE on this aircraft than a conventional one: the twist-grip
  decision put pitch and rudder on the SAME hand, so an out-of-trim force is
  held by the wrist that must also twist precisely for yaw. There is no trim
  system anywhere in the repo - the controls ledger is stick 7 lb, pedals 5
  (now deleted), spoileron rig 4. That is a genuine hole, not an upgrade.

  Lightest workable fix (standard ultralight practice): bungee/spring trim -
  a spring to the stick base with a small ratchet lever, ~0.4 lb, no change
  to the elevator, no tab, no hinge. Uses ~8% of the 4.8 lb freed today.""")

print("=== 3. GAP SEALS: SEAL THE ELEVATOR; ON THE RUDDER, SEAL *AND SHRINK* ===")
print("""  Basis is NACA TN-632 (flight test, Fairchild 22), not a rule of thumb:
  sealing gained ~20% effectiveness on 0.18c surfaces and ~33% on 0.09c -
  smaller surfaces gain more - and the headline result was that SEALED 0.09c
  ailerons matched UNSEALED 0.18c effectiveness at about ONE-THIRD the
  operating force. So the question for a wrist-driven rudder is not 'does
  sealing cost hinge moment' but 'can a sealed smaller rudder do the same
  job for less force'. First-order answer below.""")

def tau(cf_c):
    """Ideal thin-airfoil control effectiveness. Real surfaces run ~85-90%
    of this; ratios are far less sensitive to that offset than absolutes."""
    th = math.acos(2*cf_c - 1)
    return 1 - (th - math.sin(th))/math.pi

CF_NOW = 0.50                  # rudder chord / VT chord as drawn
SEAL_GAIN = 1.25               # effectiveness multiplier, TN-632 mid-range
SEAL_HM_PEN = 1.25             # hinge-moment penalty, same order
target = tau(CF_NOW)/SEAL_GAIN
lo, hi = 0.05, 0.50
for _ in range(60):
    mid = 0.5*(lo+hi)
    if tau(mid) < target: lo = mid
    else: hi = mid
cf_new = 0.5*(lo+hi)
hm_ratio = (cf_new/CF_NOW)**2 * SEAL_HM_PEN     # HM ~ S_r * c_r ~ (cf/c)^2
print(f"  rudder as drawn: cf/c {CF_NOW:.2f}, tau {tau(CF_NOW):.3f}")
print(f"  sealed equivalent: cf/c {cf_new:.2f}, tau {tau(cf_new):.3f} x {SEAL_GAIN} seal "
      f"= {tau(cf_new)*SEAL_GAIN:.3f} (same authority)")
print(f"  hinge moment ratio {hm_ratio:.2f} -> ~{(1-hm_ratio)*100:.0f}% LESS, seal penalty included")
hm_r = 0.008*25*q(35)*7.5*1.5*12.0
peak_now = hm_r*0.55/2.4
print(f"  twist-grip peak: {peak_now:.0f} in-lb today -> ~{peak_now*hm_ratio:.0f} in-lb sealed+shrunk")
print("""  -> a sealed, smaller rudder may buy back roughly half the wrist budget,
     and could relax the 45% horn balance the twist grip currently depends on.
     ESTIMATE ONLY - ideal tau, assumed seal factors. Worth asking BEFORE the
     tail is drawn, which is the actual finding; do not size on this number.

  ELEVATOR - seal it. Authority per degree helps the tight flap flare, and
     the added stick force is what the trim system in section 2 removes.
  BOTH     - the real enemy is FRICTION, not hinge moment. Sailplane practice
     runs mylar over a teflon glass-tape chafe strip specifically to stop
     breakout force creeping up. On a wrist-driven rudder that strip is
     mandatory: breakout is what kills small precise yaw inputs.
  NOT the spoilerons - they are not hinged trailing-edge surfaces.""")
