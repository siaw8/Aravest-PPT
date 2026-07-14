# Aravest Presentation Design System
## System Architecture — for final approval

**Status:** Draft for approval · No production files built yet
**Source of truth:** `250904_Aravest_Presentation_Template_v8.pptx` (19 slides, 13 masters, 18 layouts, 15 themes)
**Canvas:** 16:9 widescreen — 13.333″ × 7.5″ (12,192,000 × 6,858,000 EMU)
**Typeface:** Aptos Display (headings) / Aptos (body) — retained
**This document delivers:** (1) final design principles · (2) authoritative colour hierarchy · (3) expanded archetype catalogue · (4) precise production specifications · (5) proposed deliverable structure · plus a separate Legal & Compliance schedule and a note on typography.

> Nothing in the source file has been altered. All findings below are read directly from the file's XML (themes, masters, layouts, placeholders, embedded media, chart definitions and disclaimer text), not from rendered screenshots.

---

## 1. Final agreed design principles

The Aravest character — quiet confidence, institutional and premium, precise and disciplined, values-led and value-focused, understated rather than promotional, distinctly Asia-Pacific but never decorative or culturally literal, contemporary without being fashionable, and legible to both Japanese shareholders and global institutional investors — is expressed through eight operating principles:

1. **Restraint is the brand.** Quiet confidence comes from what is left out. Generous whitespace, one idea per slide, and margins that never move do more work than any graphic device.
2. **Structure over decoration.** Every content archetype is built around a container — a table, a labelled data block, a defined column grid — specifically so authors cannot default to an open paragraph well. The system makes the disciplined choice the easy choice.
3. **The takeaway leads.** Titles state the conclusion, not the topic. Data and structured tables carry the argument; icons and imagery never substitute for substance.
4. **One controlled palette.** A single authoritative navy-led palette does the everyday work. Colour signals meaning (a highlight, a total, a risk), never mood.
5. **Gold is a signal, not a texture.** Gold appears rarely and deliberately — one emphasis per slide at most — to mark the single most important figure, rule or accent. It is never a fill or a routine decoration.
6. **The facet motif is a signature, not a pattern.** The angular triangulated geometry — Aravest's genuine proprietary mark, echoing the ascending "A" — is reserved for covers, section dividers and occasional framing pages. It never appears behind working content.
7. **Photography is editorial, or it is absent.** Only real, high-quality architectural and skyline photography, cool/dusk in tone. No illustration, no clip-art, no stock business cliché.
8. **Fixed infrastructure.** Logo placement, footer, confidentiality marking and page number are system furniture. They are identical on every slide and never re-negotiated per page.

**Values-led, value-focused** is expressed structurally, not with slogans: dedicated archetypes for investment thesis, value-creation plan, risks & mitigants and management recommendation ensure the *reasoning and stewardship* are always visible alongside the numbers.

---

## 2. Authoritative colour hierarchy

The visible reference (the eight-swatch table parked off-canvas in the "Main body" master) and the colours technically embedded in the 15 themes agree on only five of eight colours. The table is built revealingly: swatches 1–5 are filled with *live theme accents* (`schemeClr accent1–5`); swatches 6–8 are *hand-painted* with hard-coded hex (`srgbClr`) — i.e. declared by intent but not cleanly wired into the theme. This is the root of the drift.

### 2.1 Tier A — Approved & declared Aravest colours
The eight colours intentionally declared in the visible reference table. These are the palette of record.

| # | Hex | Proposed name | Role |
|---|------|--------------|------|
| 1 | `#002B5C` | **Aravest Navy** | Primary. Titles, primary text, headers, first data series. |
| 2 | `#869397` | **Slate** | Secondary text, captions, secondary data series, quiet rules. |
| 3 | `#35464F` | **Graphite** | Divider fields, dark UI furniture, tertiary text. |
| 4 | `#4682B4` | **Steel Blue** | Data accent (charts/diagrams). |
| 5 | `#008080` | **Teal** | Data accent (charts/diagrams). |
| 6 | `#002147` | **Deep Navy** | Structural dark — deep fields, cover overlays, near-black navy. |
| 7 | `#C8A951` | **Signature Gold** | Rare single-emphasis accent only. |
| 8 | `#2E4E48` | **Pine** | Reserved — values/ESG contexts only (see 2.4). |

### 2.2 Tier B — Colours technically embedded in the themes
Present in the theme machinery but **not** in the visible reference — functional, undeclared:

| Hex | Theme slot | Proposed name | Note |
|------|-----------|--------------|------|
| `#0E2841` | `dk2` (all themes) | **Midnight** | A third near-black navy — very close to `#002147` and `#002B5C`. |
| `#E8E8E8` | `lt2` (all themes) | **Mist** | Pale grey — table banding, light fields, hairlines. Should be formally declared; it is already in working use. |
| `#000000` / `#FFFFFF` | `dk1` / `lt1` | Black / White | Standard text/background mapping. |
| `#467886` / `#96607D` | `hlink` / `folHlink` | — | PowerPoint default hyperlink colours, never surfaced. Leave as-is. |

### 2.3 Tier C — Accidental inconsistencies and drift
Confirmed defects, not design choices:

1. **accent3 transposition.** Declared `#35464F`, but 11 of 13 Aravest themes embed `#36454F` (digits transposed). Only themes 7 and 12 carry the declared value. **Recommendation:** standardise on **`#35464F`** (the declared reference value) everywhere. Visually negligible; the point is a single source of truth.
2. **accent6 collision.** Two declared colours compete for one theme slot: `#002147` (Deep Navy) occupies accent6 in 11 themes; `#C8A951` (Gold) occupies it in only 2. **Consequence: gold is not addressable as a theme colour on most of the deck** — the exact opposite of what a signature accent needs. **Recommendation:** promote **Gold `#C8A951` to accent6 universally** so it is reliably available, and carry **Deep Navy `#002147`** as a named dark (adjacent to `dk2`) rather than an accent slot.
3. **Orphaned Pine `#2E4E48`.** Declared in the reference and hand-painted into the swatch, but wired into **no** theme accent — currently unusable as a system colour. **Recommendation:** see 2.4.
4. **Navy redundancy.** Three near-identical deep navies coexist — `#002B5C` (primary), `#0E2841` (dk2), `#002147` (declared #6). At presentation scale they are barely distinguishable. **Recommendation:** rationalise to **two** — Aravest Navy `#002B5C` as primary and one structural dark (recommend retiring `#0E2841` in favour of the declared `#002147`).
5. **Two stray Office themes.** Themes 14–15 carry PowerPoint's default accents (`#156082`, `#E97132` orange, etc.) — unrelated to Aravest. **Recommendation:** remove from the rebuilt file.

### 2.4 Proposed canonical palette (resolved)
After reconciliation — recommended, pending your confirmation:

- **Core:** Aravest Navy `#002B5C` · Deep Navy `#002147` (structural dark) · Graphite `#35464F` · Slate `#869397` · Mist `#E8E8E8` · White `#FFFFFF`
- **Data accents:** Steel Blue `#4682B4` · Teal `#008080` (+ the core navies/greys as additional series colours)
- **Signature:** Gold `#C8A951` — rare, single-emphasis only
- **Reserved:** Pine `#2E4E48` — narrow use only, for ESG / values / impact content, to avoid competing with Teal in general data use. *Alternative on request: retire from the core system entirely.*

Two open colour decisions are listed in §9 for your ruling: (a) confirm accent3 = `#35464F`; (b) confirm gold → accent6 and the treatment of Pine.

### 2.5 Gold usage rule (binding)
- **Maximum one gold element per slide** — ideally one per section.
- **Permitted:** a single highlighted KPI figure; one rule beneath a section-divider title; the single most important data point in a chart or the one key cell in a table; a thin accent line on a cover.
- **Never:** body text, large area fills, gradients, multiple gold elements, or any recurring/decorative use.

### 2.6 Permitted colour combinations
| Foreground | Background | Use | Status |
|---|---|---|---|
| Aravest Navy | White | Primary text, titles | ✓ default |
| White / Mist | Aravest Navy / Deep Navy / Graphite | Headers, dividers, table header row | ✓ |
| Slate | White | Secondary text, captions, sources | ✓ |
| Graphite | White | Tertiary text | ✓ |
| Steel Blue / Teal | White | Data marks | ✓ data only |
| Gold | White or Aravest Navy | Single emphasis | ✓ rare only |
| Teal | Navy | — | ✗ insufficient contrast |
| Gold | Slate / Graphite | — | ✗ muddy, low contrast |
| Steel Blue adjacent to Teal | — (chart series) | — | ✗ too close; separate with a neutral |

---

## 3. Cover & divider system

Technical consolidation must not flatten purposeful variety. The rebuild collapses **duplicated machinery** (11 near-identical masters that differ only by one background image) into flexible layouts with a swappable image well — while **preserving distinct archetypes that serve different communication purposes.**

**Cover archetypes (core library):**
1. **Full-image institutional cover** — full-bleed editorial photography, facet edge treatment, title over a controlled navy overlay. For flagship investor and corporate presentations.
2. **Restrained corporate cover** — predominantly white, centred logo, a single thin gold rule, minimal type. For board papers and formal/quiet contexts.
3. **Geographic / portfolio cover** — the evolved "4 Cities" multi-image facet composition, rebuilt as one reusable asset. For portfolio, market and multi-jurisdiction narratives.

**Cover archetype (optional / non-core):**
4. **US / Dallas specialist cover** — retained as an **optional legacy layout only**, outside the default core library, pending confirmation of continuing US relevance. Not offered in the standard author picker.

**Divider archetypes:**
5. **Image-led section divider** — Graphite field, single photographic accent, divider title. For narrative transitions.
6. **Typography-led section divider** — no image; large section numeral + title on white or navy, optional single gold rule. For board/IC papers where imagery would feel promotional.

The **"World" clip-art cover is retired** (illustration tier inconsistent with the system). The facet motif is rebuilt **once** as a reusable vector asset rather than ~70 hand-placed shapes per master.

---

## 4. Expanded archetype catalogue (~30)

Grouped by function and mapped to the audiences they serve (**B**oard · **I**nvestor · investment **C**ommittee · **M**anagement/internal). Foundation/utility layouts are listed separately below.

### A. Covers & dividers
| # | Archetype | Audience |
|---|-----------|----------|
| 1 | Full-image institutional cover | I · B |
| 2 | Restrained corporate cover | B · I |
| 3 | Geographic / portfolio cover | I · M |
| 4 | US / Dallas specialist cover *(optional/legacy)* | — |
| 5 | Image-led section divider | I · B |
| 6 | Typography-led section divider | B · C |

### B. Openers & narrative
| # | Archetype | Audience |
|---|-----------|----------|
| 7 | Agenda / contents | all |
| 8 | Executive summary | all |
| 9 | Single strategic thesis (one statement) | B · I |
| 10 | Investment thesis | I · C |
| 11 | Key takeaways | all |

### C. Strategy & frameworks
| # | Archetype | Audience |
|---|-----------|----------|
| 12 | Three-pillar framework | I · B |
| 13 | Two-pathway strategy | B · C |
| 14 | Strategic choices & trade-offs | B · C |
| 15 | Value-creation plan | I · C |
| 16 | Scenario comparison | B · C |
| 17 | Timeline / roadmap | all |
| 18 | Organisational / governance structure | B · C |

### D. Financial & data
| # | Archetype | Audience |
|---|-----------|----------|
| 19 | Financial dashboard | M · B |
| 20 | KPI / metrics summary | M · B |
| 21 | Actual vs budget | M · B |
| 22 | Financial bridge / waterfall | C · B |
| 23 | AUM movement | M · B · I |
| 24 | Portfolio composition | I · C |
| 25 | Capital-raising status | I · B |
| 26 | Investment pipeline | C · I |

### E. Portfolio & asset
| # | Archetype | Audience |
|---|-----------|----------|
| 27 | Asset overview / case-study profile | I · C |
| 28 | Market map / geography | I · C |

### F. Governance & decision
| # | Archetype | Audience |
|---|-----------|----------|
| 29 | Risks & mitigants | B · C |
| 30 | Management recommendation | B · C |
| 31 | Board decision required | B |

### G. Reference & appendix
| # | Archetype | Audience |
|---|-----------|----------|
| 32 | Detailed institutional table | C · B |
| 33 | Appendix divider | all |
| 34 | Appendix data slide | C · B |
| 35 | Pull-quote / testimonial | I |

### Foundation & utility layouts (system furniture, not counted as archetypes)
- Working slide (single content well, refined)
- Working slide with sub-header (the retained two-tier header pattern)
- Chart frame (bar/column · line · donut variants sharing one chart style)
- Closing / contact slide (logo lockup + short-form disclosure + registered entity/address)
- Jurisdiction disclaimer layouts — **Singapore, Australia, Korea, Korea REF** (content preserved verbatim; typography refined only)

> The catalogue exceeds the 25–30 target to give headroom; the final build may merge close siblings (e.g. KPI summary ↔ financial dashboard) after review.

---

## 5. Precise production specifications

### 5.1 Grid & margins (grounded in the file)
- **Live area:** 12.53″ × 6.8″ inside **0.40″ side margins** (existing content inset is 366,712 EMU ≈ 0.401″ — retained).
- **12-column grid**, 0.20″ gutter → column width ≈ 0.86″. Standard splits: halves (6+6), thirds (4+4+4), 8+4 (content + rail), 3+3+3+3 (four-up).
- **Vertical bands:** Title band top ≈ 0.34″ (existing 312,520 EMU); content band top ≈ 1.10″ (existing 1,004,610 EMU); footer baseline ≈ 6.89″ (existing 6,298,318 EMU). These are retained so every slide aligns.
- **Logo:** top-right, ≈1.63″ × 0.68″, ≈0.30″ from top (existing master placement retained) — rebuilt from a clean vector asset, not the current cropped raster.

### 5.2 Spacing increments
Single modular scale (points): **4 / 8 / 12 / 16 / 24 / 32 / 48**. Paragraph space-after = 6pt (existing). Block-to-block minimum = 16pt. Title-to-content = 24pt. No ad-hoc nudging.

### 5.3 Type scale (Aptos Display / Aptos)
| Style | Size | Font | Colour | Notes |
|-------|------|------|--------|-------|
| Cover title | 36 pt | Aptos Display | Navy or White | ≤ 2 lines |
| Section divider title | 32 pt | Aptos Display | White / Navy | ≤ 6 words |
| Slide title (H1) | 24 pt | Aptos Display | Aravest Navy | **1 line** |
| Kicker / eyebrow | 9 pt | Aptos | Slate | UPPERCASE, +10% tracking |
| Subtitle / sub-header | 12 pt | Aptos | Slate | optional |
| Body lead / intro | 14 pt | Aptos | Navy/Graphite | opening sentence |
| Body (standard) | 11 pt | Aptos | Graphite | line spacing 1.2–1.25 |
| Data callout / KPI | 28–40 pt | Aptos Display | Navy (gold if the one highlight) | |
| Table text | 9–10 pt | Aptos | Graphite | |
| Caption | 9 pt | Aptos | Slate | |
| Source / footnote | 8 pt | Aptos | Slate | |
| Footer (confidentiality / page no.) | 8 pt | Aptos | Navy | refined from existing 10pt |

*The existing file defaults to a 32pt title and 16pt body. The refined scale (24pt title, 11pt body) is the mechanism by which Aptos reads as premium — tighter type plus more whitespace and disciplined hierarchy, rather than large type filling the frame.*

### 5.4 Content density limits
| Slide type | Max title | Max content |
|-----------|-----------|-------------|
| Cover | 1 line | subtitle ≤ 12 words |
| Divider | ≤ 6 words | — |
| Executive summary | ~60 chars | ≤ 90 words |
| Working / body | ~60 chars | ≤ 110 words **or** ≤ 6 bullets |
| Framework (pillars/pathways) | ~60 chars | ≤ 25 words per element |
| Dashboard / data | ~60 chars | ≤ 40 words annotation |
| Pull-quote | — | ≤ 30 words |
| Recommendation / Board decision | ~60 chars | 1-sentence ask + ≤ 5 points |

**Maximum title length: ~60 characters, one line** at 24pt across the title band.

### 5.5 Number & currency formatting
- **Currency prefix:** `S$`, `A$`, `US$`, `¥` (Japanese Yen, no decimals). One convention per deck.
- **Magnitude:** `m` and `bn` suffixes — e.g. `S$1,250m` or `S$1.25bn`. Billions to 1 decimal, millions to 0.
- **Thousands separator:** comma. **Right-align** all figures in tables; align decimals.
- **Percentages:** 1 decimal (`12.3%`); use **bps** for small deltas.
- **Negatives:** parentheses `(1,250)` in financial tables — colour-neutral, not red.
- **Dates:** `14 July 2026` (DD Month YYYY). *Flag: confirm preferred format for Japanese-shareholder materials.*

### 5.6 Chart & axis conventions
- **Series order:** Aravest Navy → Slate → Steel Blue → Teal → Graphite. **Gold reserved** for the single highlighted series or point.
- **No** 3D, shadows, gradients or chart borders.
- **Gridlines:** horizontal only, thin, Mist grey; no vertical gridlines.
- **Axes:** minimal; drop axis titles where the label is self-evident; one decimal.
- **Labelling:** prefer direct labels over a legend; never show both data labels *and* an axis for the same values.
- **Pie/donut:** donut preferred; ≤ 5–6 segments; largest-first, clockwise.
- **Source** bottom-left, 8pt Slate.
- *(The two existing charts already pull brand accents rather than Office defaults — retain that discipline.)*

### 5.7 Table formatting
- **Header row:** Aravest Navy fill, White text, 9pt bold.
- **Body:** 9–10pt Graphite; **no vertical rules**; either 0.5pt Mist horizontal rules or alternate Mist banding — not both.
- **Alignment:** text left, numbers right, decimals aligned.
- **Total row:** 1pt Navy top rule, bold.
- **Emphasis:** at most **one** gold cell/figure — the single key number.
- **Row height** ≥ 0.28″; cell padding ≈ 0.06″.

### 5.8 Source & footnote treatment
- One **Source:** line per slide, 8pt Slate, bottom-left, above the footer.
- Footnote markers superscript (`¹`); note text 8pt Slate directly above the source line.
- Every external figure carries a source; every projection is labelled as such.

### 5.9 Photography rules
- Real, **editorial-grade** architecture / skyline / urban only. Cool, dusk/blue-hour tonality (consistent with the existing Singapore and Seoul covers).
- **No** illustration, clip-art or stock business cliché.
- Full-bleed or contained within the facet frame; optional Navy overlay ≤ 30% for text legibility.
- Minimum 1920px long edge; Asia-Pacific subjects preferred; avoid literal cultural motifs.

### 5.10 Icon rules
- Sparing use only. **Line icons**, 1.5pt stroke, single colour (Navy or Slate), one consistent grid size.
- **Never** multicolour, filled, 3D, or one-per-bullet. At most one coherent icon set per deck. Icons aid navigation; they never decorate.

### 5.11 Diagram rules
- Built from system primitives: rectangles, thin 1pt rules, Navy/Slate/Graphite fills, generous whitespace.
- **No** heavy shadows, gradients, or repeated rounded "cards".
- Consistent connector weight (1pt), minimal arrowheads.
- The **facet motif is not used inside diagrams.**

### 5.12 Facet motif
- **Reserved for:** covers, section dividers, occasional framing/interstitial pages, closing slide.
- **Never** on working/content slides.
- Rebuilt as a **single reusable vector asset**; tonal Navy/Slate/Steel only. One gold facet permitted as a signature. Used as edge/corner framing, not full-slide texture behind text.

### 5.13 Gold
Governed by §2.5 — one element per slide maximum; emphasis, rule, highlight or single key data point only; never a fill or routine decoration.

### 5.14 Headline-writing principles
- **State the takeaway, not the topic** — "Portfolio occupancy improved to 96%," not "Portfolio Occupancy."
- One line, ≤ ~60 characters, **sentence case**, no terminal full stop.
- Verb-led when making a claim; a noun phrase is acceptable for reference/section slides.
- The subtitle, if used, carries the nuance or the "so what."

### 5.15 Board vs investor (and IC / internal) differences
| Dimension | **Board** | **Investor** | **Investment Committee** | **Internal / Management** |
|-----------|-----------|--------------|--------------------------|---------------------------|
| Primary purpose | Decision & oversight | Persuasion & trust | Rigorous assessment | Monitoring & control |
| Lead archetypes | Board decision required; Risks & mitigants; Recommendation | Thesis; Track record; Portfolio; Photography-led covers | Pipeline; Asset profile; Waterfall; Detailed tables | Dashboard; Actual vs budget; AUM movement; KPI summary |
| Data density | Higher, candid | Restrained, curated | Highest | High, operational |
| Tone | Governance, plain | Premium, forward-looking (compliant) | Analytical, neutral | Direct, functional |
| Imagery | Minimal | Prominent | Minimal | Minimal |
| Confidentiality/disclaimer | Prominent | Prominent | Prominent | Standard |

---

## 6. Legal & Compliance schedule *(separate — for L&C review; no wording changed)*

All existing disclaimer wording is **preserved exactly**. The following possible inconsistencies are flagged for Legal & Compliance to review and rule on. **No legal text will be amended without approval.**

| # | Location | Observation | For L&C to confirm |
|---|----------|-------------|--------------------|
| L1 | Australia disclaimer (Layout 15) | Entity appears as **"Aravest Australia Pty Ltd"** in one sentence and **"ARAM Australia Pty Ltd"** later in the same passage. | Which is the correct current licensed entity? |
| L2 | Korea disclaimer (Layout 16) | Prepared by **"ARA Korea Limited"** — legacy ARA branding, not Aravest. | Confirm correct entity name and whether Aravest branding should apply. |
| L3 | Korea REF disclaimer (Layout 17) | Prepared by **"ARA Korea (REF) Limited"** — legacy ARA branding. | As above. |
| L4 | Singapore disclaimer (Layout 14) | Licensed entity given as **"Aravest Fund Management Pte. Ltd."** | Reconcile against the closing slide (below). |
| L5 | Closing slide (Slide 19) | Registered entity shown as **"Aravest Pte Ltd"** with a Capital Square, Singapore address. | Reconcile L4 vs L5 — same entity, two names. |
| L6 | All disclaimers | Copyright line reads **"© Copyright 2024."** | Confirm annual roll / current-year policy. |
| L7 | All disclaimers | Possessive rendered as **"Aravest'"** (apostrophe placement). | Confirm intended possessive form. |

---

## 7. Typography position

**For this stage: retain Aptos Display / Aptos** for maximum compatibility (they are the current MS Office default family, present on all target machines, with no licensing or embedding risk). The design system is explicitly built to prove these fonts reach a premium institutional standard **through disciplined hierarchy, spacing, weight, scale and composition** (see §5.3–5.4) rather than through the typeface alone.

Should you wish to explore a bespoke or licensed typeface later, that will be presented as a **separate proposal** with licensing, embedding and roll-out implications, and **will not be implemented without approval.**

---

## 8. Proposed structure of the final deliverables

1. **Design System Reference** — this document, finalised after approval (the authoritative specification; PDF for circulation).
2. **Legal & Compliance schedule** — §6 as a standalone document for L&C sign-off (kept separate from the design track so it does not block it).
3. **Colour & asset foundation** — one reconciled theme (`.thmx`) with drift fixed; a clean vector **logo library** (Navy · reversed/white · mono) with clear-space and minimum-size rules; the facet motif as a reusable asset; a declared swatch/token sheet.
4. **Master template** (`.potx`) — rebuilt masters/layouts implementing the catalogue: cover and divider machinery consolidated (11 masters → 2 flexible layouts) while preserving the distinct cover/divider archetypes; all ~30 archetypes plus foundation layouts; disclaimer content preserved verbatim.
5. **Populated sample deck** — every archetype shown with **realistic institutional placeholder content** (not Lorem Ipsum), for stakeholder sign-off before rollout.
6. **Author quick-reference** — a one-page do/don't card (palette, type scale, density limits, gold rule, facet rule, disclaimer-by-jurisdiction matrix).
7. **Optional / separate:** alternative-typography proposal (§7); US/Dallas specialist cover pack (non-core).

---

## 9. Open decisions — approval gate

Please rule on the following before production begins:

1. **accent3 drift** — standardise on the declared **`#35464F`** everywhere? *(Recommended.)*
2. **accent6 collision** — promote **Gold `#C8A951` to accent6 universally** (so gold is reliably addressable) and carry **Deep Navy `#002147`** as a named structural dark rather than an accent? *(Recommended.)*
3. **Pine `#2E4E48`** — **reserve narrowly for ESG/values content** (recommended), or **retire** it from the core system?
4. **Navy rationalisation** — reduce three near-identical navies (`#002B5C` / `#0E2841` / `#002147`) to **two** (primary + one structural dark)? *(Recommended.)*
5. **Dallas / US covers** — confirmed **optional/legacy, non-core**; retain pending US-relevance confirmation. Any change?
6. **Stray Office themes** (14–15) — remove from the rebuilt file? *(Recommended.)*
7. **Legal schedule** — send §6 to L&C **in parallel** with the design build, or hold?
8. **Type scale** — approve the refined 24pt-title / 11pt-body institutional scale over the file's current 32/16?

On your approval of the above, the next step is the **colour & asset foundation** and the **master template** — no PowerPoint files will be built until you confirm.
