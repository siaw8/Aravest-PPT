# Aravest Design System — Calibration Set v1

Six-slide calibration set, built for approval before the full template and archetype
library. Content is drawn **verbatim / near-verbatim** from the *Locked Board Strategy
Narrative v8*; the strategic narrative has not been altered or reinterpreted.

## Slides
| # | Slide | Mode | Narrative source |
|---|-------|------|------------------|
| 1 | Institutional cover | Investor / corporate (cover scale) | Cover block; SG entity |
| 2 | Executive summary | Investor / corporate | §01 Purpose + §16 proposition; five section-heading conclusions |
| 3 | Two-pathway strategy | Board / IC | §06 / §07 / §08 |
| 4 | Capital & AUM dashboard | Board / IC | §10 AUM profile + identity; US$300m; §11 Conrad Seoul |
| 5 | Board decision required | Board / IC | §06 / §07 / §08 / §09 decision architecture |
| 6 | Investment case — current pipeline | Board / IC | §12 pipeline table |

## Two typography modes (both demonstrated)
- **Investor / corporate** (slides 1–2): larger display type, greater whitespace and
  wider margins — screen-presented front matter.
- **Board / IC** (slides 3–6): tighter type, denser working layouts, closer reading
  distance — the working papers of a board strategy meeting.

## Approved decisions applied
- accent3 standardised on **#35464F**; Gold **#C8A951** promoted to the addressable
  signature accent; two navies only (**#002B5C** primary, **#002147** deep); undeclared
  #0E2841 dropped; Pine #2E4E48 held out of the working palette; stray Office themes
  excluded.
- Fixed infrastructure retained: logo top-right, confidentiality bottom-left, page number
  bottom-right. More generous content margins tested on the investor-mode slides.
- Gold used only as a rare signature (cover seam/facet, section rules, one KPI accent,
  the decision kicker) — never a fill.
- Facet motif appears only on the cover.

## Honest-content handling (important)
- **Slide 4** contains no invented financials. The only hard figure is the **US$300m**
  sponsor capital stated in the narrative; all other KPI tiles are explicitly marked
  *"to be populated by Finance,"* echoing the narrative's own instruction that figures be
  refreshed by the transaction teams before Board circulation.
- **Slide 5** reflects the narrative's decision architecture; a footnote states that
  formal resolutions are to be confirmed by management and the company secretary — the
  slide does not itself constitute a resolution.
- **Slide 6** reproduces the pipeline names as written in the locked narrative, carrying
  its own refresh caveat.

## Rendering caveat
The editable `.pptx` correctly specifies **Aptos Display / Aptos** (per the retained
typography decision). The PNG previews were rendered in this environment, which does not
have Aptos installed, so they use a neutral sans substitute (Liberation Sans). Layout,
hierarchy, spacing, colour and composition are faithful; exact letterforms will render as
Aptos when opened in PowerPoint.

## Files
- `Aravest_Calibration_Set_v1.pptx` — editable, native PowerPoint (build with `build_deck.py`)
- `renders/slide1–6.png` — rendered previews
- `Aravest_Calibration_ContactSheet.png` — all six at a glance
- `build_deck.py` — deck builder (python-pptx); `render_pptx.py` — preview renderer
- `assets/` — brand assets derived from the template (cropped navy + reversed logo, cover band)
