# Seat: Mesh Sling, With the Crash Property Kept

**Owner decision 2026-08-09: mesh sling seat adopted** — hammock-style
vinyl-coated polyester mesh (Phifertex-Plus class, outdoor-sling-chair
material) stretched between rails on the cockpit cage, replacing the framed
pan with Confor foam. Script: `analysis/sling-seat.py`.

## 1. Why it's right for this aircraft

- **Comfort:** a sling conforms to the pilot; there is no pan edge and no
  pressure point, which matters more than padding on a 2–3 hour endurance
  aircraft with no cabin to shift around in.
- **Cooling:** open mesh breathes through the back and seat — an open-cockpit
  Tennessee-summer aircraft spends its whole life in exactly the conditions
  sling furniture was designed for.
- **Weight:** mesh panel + hems 1.3 lb, lacing 0.4, crush pad + light pan
  0.9, one added cage cross tube 0.6 → **~3.2 lb vs the 5.0 lb
  pan/frame/Confor line — ~1.8 lb saved** (unbanked until weighed; on an
  airframe with a ~1 lb legality margin, that is potentially the whole
  margin doubled).
- **Precedent:** sling seats are standard practice in this exact class —
  Quicksilvers and Kolbs have flown fabric slings for decades.

## 2. Structure: the sling carries the crash case fine

Load basis is the fleet rule: fixed-mass fittings at 6.4 g limit / 9.6 g
ultimate with the 200 lb structural pilot — **1,920 lb through the seat**.
With rails 18 in apart and ~3.5 in of static sag, the membrane runs at
**~98 lb/in of edge tension** at ultimate. Sling mesh breaks at ~300–400
lb/in in the warp: **3× raw margin, ~1.5× after a 50% seam/lacing derate.**
Requirements that follow:

1. Doubled hems around the rails (the fabric is not the weak point; the
   sewn attachment is).
2. Warp direction runs rail-to-rail.
3. **Static proof test of the finished sling to 1,920 lb** (sandbags, cheap,
   before first flight) — the derate above is an estimate and this test
   replaces it with a fact.
4. UV: vinyl-coated polyester is outdoor-rated but not immortal — sling
   inspection joins the condition checklist, and replacement is a $40 panel.

## 3. The catch, and its cheap fix: a sling is a spring

The README promises an **energy-absorbing seat**, and a hammock alone is the
opposite: it stores vertical crash energy elastically and gives it back as
rebound — bad for spines. The fix keeps both properties:

- Position the sling so the 1-g sag point sits ~1.5 in above a **2 in
  crushable pad** (Confor or aluminum-honeycomb block, ~0.7 lb, on a light
  pan at the bay floor).
- Normal sitting never touches the pad — full mesh comfort and airflow.
- A hard vertical impact strokes the sling down into the pad, which crushes
  and does not rebound. The landing gear remains the primary absorber
  (8 fps, 6.6 in of stroke); the pad covers the beyond-gear case that the
  Confor pan used to cover.

The 5-point harness continues to anchor to the cage, never to the sling —
unchanged, and now worth stating explicitly since the sling is fabric.

## 4. Fit and adjustment

With the pedals gone (controls-mechanization trade), accommodation for the
105–200 lb pilot set is seat-and-footrest. A sling makes the seat side of
that nearly free: lacing tension tunes sag to the pilot, and the footrest
takes the stature adjustment. The full-size seating mockup (already gated
for the twist-grip and brake-lever questions) adds one more check: sling sag
and hip position across the pilot range, so the eye line and stick reach
stay in band from 105 to 200 lb.

## 5. What this does not settle

- Actual fabric choice and its measured strip strength (spec sheet, then the
  proof test).
- Rail spacing and back-panel geometry — set at the mockup.
- Whether the crush pad is Confor or honeycomb (pick by measured crush
  stress once the pad area is drawn; target ~15–20 psi crush for a
  50th-percentile pelvis footprint).
- The measured-weights CSV row ("Seat frame, pan, Confor foam", 5.0 lb)
  re-titles at the workbook reconciliation.
