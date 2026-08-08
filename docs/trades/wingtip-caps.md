# Carbon Wingtip Caps

Resolution of [winglets.md](winglets.md), which concluded that tip *shape* is
worth more than a winglet and costs nothing. This is how to actually get it.

**Verdict: do it.** A moulded carbon tip cap is the rare change that is
weight-neutral, buys real aerodynamic benefit, buys durability, and buys a shape
that cannot be built any other way. It is not the winglet trade with a different
name — it is the thing the winglet trade recommended.

**One correction to the obvious build plan:** wrapping carbon *around* a printed
plug gives a flawless surface on the wrong side. See §3.

Status: recommended, not yet drawn. No dimensions committed.

---

## 1. Why this is worth doing, beyond finish

**The shape that works is one fabric cannot hold.** The standard answer for a
constant-chord wing is a Hoerner tip, and its defining feature is a **sharp lower
outboard corner** that forces the tip vortex outboard and up. Fabric over a
laminated wood bow physically cannot hold a sharp edge — it wants to shrink into a
radius, and it will. A moulded part holds it exactly.

So the mould is not just about surface finish. **It enables a geometry that is
otherwise unbuildable on this wing.** That is the real argument, and it is
stronger than the one about layer lines.

**Symmetry is a handling item here, not cosmetics.** §9 describes spoileron roll
authority as *"adequate rather than crisp,"* with roughly 30% of stick travel as
deadband. Left-right tip asymmetry costs trim authority this aircraft does not
have a surplus of. Two parts off two mirrored moulds are identical by
construction. Two hand-carved wood bows are not, and the difference is not
visible — it shows up as a wing that drops in the cruise and eats spoileron
travel to hold level.

**Durability where damage actually happens.** The wing is three-piece, and two
20 lb panels get handled by hand every flight. The tip is the part that meets
hangar walls, trailer rails, and door frames. Fabric over a wood bow is the least
durable thing on the aircraft in exactly the place that gets hit most.

**And it can be made removable**, which fabric cannot. Screws into a hardwood tip
block give inspection access into the outer bay and let a damaged cap be replaced
in an evening instead of re-covering a panel.

## 2. Weight — it is free if you are disciplined

Wetted area for a cap wrapping the tip, 50 in chord, per tip:

| Inboard extent | Area per tip |
|---|---|
| 4 in | 4.31 ft² |
| **6 in** | **5.73 ft²** |
| 8 in | 7.15 ft² |
| 12 in | 10.00 ft² |

Layup weight for a 6 in cap:

| Layup | Per tip | Both tips |
|---|---|---|
| **2 ply 3.7 oz plain weave, vacuum bagged** | **0.54 lb** | **1.07 lb** |
| 2 ply 5.7 oz 3k twill, vacuum bagged | 0.82 lb | 1.65 lb |
| 2 ply 5.7 oz twill, hand layup wet | 1.13 lb | 2.27 lb |
| 3 ply 5.7 oz twill, bagged | 1.36 lb | 2.72 lb |

Against a laminated wood tip bow with fabric and tapes at roughly **0.65 lb per
tip**:

> **Two plies of 3.7 oz cloth, vacuum bagged, is weight-neutral against wood and
> fabric.** Two plies of 5.7 oz twill wet-laid by hand is +1.9 lb over both tips,
> at the tip, for no benefit.

The resin fraction is what decides this, not the fibre. A wet hand layup runs
~40% fibre by weight; bagged runs ~55%. **That single difference is the whole
weight budget.** If you are not going to bag it, use the lighter cloth and accept
a slightly softer part — do not use heavy twill wet.

This is also why the flutter objection from the winglet trade mostly evaporates:

| | Mass | Where |
|---|---|---|
| 1.5 ft winglet | 4–6 lb | cantilevered outboard on a lever arm |
| Carbon tip cap | +0.1 lb over wood | wrapped onto the existing tip |

Same category of concern, roughly 40× less of it. It does not remove the need for
a flutter analysis — `open-questions.md` still carries that as its own gap — but a
weight-neutral cap does not meaningfully move the problem.

## 3. The mould: print it female, not male

> **"Wrap the carbon right around the printed plug" gives a perfect *inner*
> surface and a rough *outer* surface.** The air only touches the outside.

Laying up against a male plug puts the tool surface on the inside of the part.
The outside is whatever the last ply and the peel ply left, and getting it fair
then means fill, sand, prime, and sand — which is the work the mould was supposed
to eliminate, done on a curved compound surface, twice, symmetrically.

**Print the mould as a female cavity and lay up inside it.** The tool surface
becomes the outer aerodynamic surface, straight off the mould.

### The undercut problem

A cap that wraps the tip covers upper surface, tip end, and lower surface. An
airfoil is convex on both sides, so **a single female cavity traps the part** — it
cannot be drawn out.

Two ways around it, in order of preference:

1. **Split mould at the chord plane.** Two cavities meeting at the maximum
   thickness line. Lay up upper and lower shells, join wet-on-wet with an internal
   joggle and a bonding strip, or clamp the halves and lay up as one part with an
   internal seam tape. The parting line sits at the widest point, which is
   aerodynamically benign and easy to fair.
2. **Design the undercut out.** Make the cap an end fairing that draws in one
   direction only. Simpler tooling, less of the tip covered, less benefit.

Whichever you choose, **the two tips are mirror images.** Mirror the model, do not
try to use one mould for both.

### Print bed reality

A 50 in chord does not fit on any hobby printer:

| Bed | Sections along chord |
|---|---|
| 256 mm (10.1 in) | 5 |
| 350 mm (13.8 in) | 4 |
| 500 mm (19.7 in) | 3 |

Times two halves, times two mirrored tips — **12 to 20 printed sections.** Design
alignment features (dowel pins and pockets, or a keyed puzzle joint) into the CAD
rather than aligning by eye. Bond the sections, then fill and fair the seams
before any surface prep. Section joints are where "flawless" is won or lost, and
they run spanwise across the airflow, which is the worst orientation for a step.

### Print material

Room-temperature epoxy on a thin 2-ply layup exotherms modestly, so the mould only
needs to survive perhaps 40 °C — but a post-cure to develop full resin properties
runs 50–60 °C, and that is where mould material decides things:

| Material | Approx Tg | Verdict |
|---|---|---|
| PLA | 55–60 °C | marginal at room cure, **fails any post-cure** |
| PETG | ~80 °C | fine for room-temperature cure |
| ASA / ABS | ~100 °C | good, and ASA is dimensionally stable |
| PC | ~145 °C | more than needed |

**PETG or ASA.** Print solid-ish at the surface — 4+ perimeters and high infill
near the cavity — so sanding does not break into voids.

### Surface prep is the step that decides the outcome

Printed surfaces are porous and layered. Straight off the printer they will
telegraph every layer line into the part and mechanically key the epoxy so it will
not release.

1. Seal the cavity — epoxy skim coat or high-build filler primer
2. Sand progressively to 600, then polish
3. Release agent: paste wax with PVA over it, or a semi-permanent release

Skip step 1 and the part locks into the mould. That is the common failure.

## 4. The one thing that could actually bite: galvanic corrosion

**Carbon is strongly cathodic to aluminium.** §7 puts 6061-T6 spar caps in this
wing, and they run out to the tip — exactly where this part goes. Carbon in
direct contact with aluminium, with any moisture present, drives aggressive
corrosion of the aluminium, and it happens inside a closed wing bay where nobody
will see it until an inspection that may never happen.

**Isolate them.** Standard practice, and it is not optional:

- A ply of **fibreglass** between any carbon and any aluminium — never carbon
  directly against the cap, a fitting, or a fastener
- Sealant at the interface
- Non-metallic or isolated fasteners; if steel screws go through carbon into a
  tip block, keep them out of contact with the spar caps

This is the one item in this document that is a safety and longevity issue rather
than a preference. It should go on the drawing, not in a build note.

## 5. Detail items

**Attachment.** Screws into a hardwood tip block laminated into the outer rib bay,
not a bond. Removable means inspectable and replaceable. Use enough screws that
the edge does not oil-can in the slipstream.

**Fabric termination.** The covering has to end somewhere and be sealed. Terminate
the fabric at the outboard rib with a proper taped edge, then let the cap overlap
it. Do not rely on the cap to retain the fabric.

**Slat termination.** §10 specifies full-span slats. Where the slat ends relative
to the cap is an unresolved geometry problem, and §10 already says slat dimensions
should be copied from a known installation rather than derived. **There is no
known installation to copy for a slat-to-moulded-tip junction.** Resolve the slat
end before finalising the cap shape, not after.

**Do not freelance the shape.** Copy a documented Hoerner tip. The parameters that
matter are the lower-surface cut-off angle and how far outboard the upper surface
is carried, and both are published.

## 6. What this does not settle

- The actual tip geometry. Copy it, do not derive it.
- Where the full-span slat terminates, which constrains the cap.
- Flutter, still unanalysed anywhere in this project. A weight-neutral cap does
  not move it, but it does not excuse it either.
- Whether the real `e` improvement matches the +2.9% estimate in
  [winglets.md](winglets.md). Phase I item 7 measures glide; that is the check.
- Vacuum bagging capability. The weight case depends on it. Without a bag, use
  3.7 oz cloth and accept the result — do not substitute heavier twill.

---

*Weights assume 2.05 × chord airfoil perimeter, 55% fibre by weight bagged and
40% wet, and 0.65 lb per tip for a laminated wood bow with fabric and tapes.*
