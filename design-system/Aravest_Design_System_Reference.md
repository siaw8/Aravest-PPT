# Aravest Presentation Design System — Reference
**Version 1.0 · Approved direction: Calibration V4-final**
Companion files: `Aravest_Master_Template.pptx` (technical layouts T01–T18 + disclaimers + closing) · `Aravest_Sample_Deck.pptx` (the locked Board narrative through the system) · `ARCHETYPE_CATALOGUE.md` (36 documented archetypes) · `Aravest_Author_QuickReference.md`.

---

## 1 · Character
Quiet confidence · institutional and premium · values-led and value-focused · precise and disciplined · suitable for Japanese shareholders and global institutional investors · distinctly Asia-Pacific without cultural literalism · contemporary without being fashionable · understated rather than promotional.

The deck is **a premium institutional Board document, not a minimalist brochure**: calm, readable, substantive, authoritative.

## 2 · Colour system

### 2.1 Palette of record
| Colour | Hex | Functional role |
|---|---|---|
| Aravest Navy | `#002B5C` | Brand primary — headings, first data series |
| **Deep Navy** | `#002147` | **Structural** — dark fields, major conclusions, governing principles, section transitions, primary cards |
| **Graphite** | `#35464F` | **Secondary structure** — body text, row/column labels, restrained panels |
| Slate | `#869397` | Quiet furniture only — footnotes, page numbers, sources |
| **Teal** | `#008080` | **Pathway 1** — Diversified Track Record Building, repeatability, portfolio development |
| **Steel Blue** | `#4682B4` | **Pathway 2** — Institutional-Scale Opportunities, acceleration, institutional relevance |
| Gold | `#C8A951` | Rare Board-level signal only |
| Mist | `#E8E8E8` | Hairlines, light rules |
| White | `#FFFFFF` | Default field |

**The visual language:** *teal builds the record; steel blue can accelerate scale.* Neither pathway is preferred: equal card weight, equal type, symmetrical placement.

### 2.2 Tints (projector-calibrated)
Pathway card fills **7%** over white (teal `#EDF6F6`, steel `#F2F6FA`); utility graphite **4.5%** (`#F4F5F6`); tonal borders **40%** of accent (teal `#99CCCC`, steel `#B5CDE1`), graphite border 25% (`#CDD1D3`). On Deep Navy: light teal `#8FC6C6`, light steel `#A9C6E2`, dimmed white `#D5DDE6`, tonal card fill = Deep Navy +7% white, border +22% white.

### 2.3 Guardrails
Max **two active accents** per working slide · light tints, never heavy colour boxes · never colour every label or paragraph · no gradients, bevels or glow · **gold appears only as**: the cover hairline, a section-divider rule, and the single "For decision" marker — never in working-slide hierarchy · dense tables use **pathway markers (3pt left bar), not row tints**.

### 2.4 Deck rhythm
≈**70%** predominantly white slides · ≈**20%** slides with meaningful coloured structure or light tints · ≈**10%** dark-field slides, reserved for covers, section dividers, Board decisions and major conclusions.

## 3 · Typography

**Core faces (all working content): Aptos Display / Aptos.**
**Secondary display face: Spectral Light / Light Italic** — the website's serif (SIL OFL 1.1, `fsType=0` installable embedding; self-hosted at aravest.com; fallback Georgia → Times New Roman). Reserved for: cover titles, section dividers, pull quotes/major propositions, agenda numerals, and **one italic phrase inside an important headline**. Budget ≤5–10% of deck text (system delivers ≈3%). Never for body, tables, charts, KPI labels, decision lists, footnotes or working headings. Suppress the italic for CJK text (as the website does).

### 3.1 Type scale — Board / IC mode (default; the two decks demonstrate it)
| Element | Spec |
|---|---|
| Slide title | 24pt Aptos Display, Navy, ≤2 lines |
| Kicker/eyebrow | 10pt Aptos bold, Graphite, +16% tracking, caps — **not on every slide** |
| Card title | 14–15pt Aptos Display, Navy |
| Card body / matrix values | **min 13pt** Aptos, Graphite, 1.2 line spacing |
| Narrative body | 13.5pt, 1.3 spacing, ≤110 words/slide |
| Table text | 12–13pt (12 floor for dense tables) |
| Row/column labels | 9–9.5pt bold caps, Graphite |
| KPI figure | 34pt Aptos Display |
| Decision verbs | 15pt Aptos Display caps, Deep Navy |
| Governing principle | 13pt White on Deep Navy |
| Footnotes/sources | 8.5–9pt Slate italic |
| Cover title | 42–46pt Spectral Light (+italic phrase) |
| Divider numeral/title | 60pt / 30pt Spectral Light on Deep Navy |
| Dark-field proposition | 15–16pt White, 1.4 spacing |

**Investor / corporate mode:** titles 30–36pt, body 15–18pt, labels 11–13pt, footnotes 8–9pt; more whitespace; photographic covers and imagery prominent.

## 4 · Card system

- **Form:** rounded corners ≈8pt radius (0.09″; PowerPoint roundRect adjustment = 0.09″/min-dimension). Internal padding ≈0.24–0.28″; inter-card gap 0.15–0.16″. Geometry precise and architectural — no pill shapes.
- **Borders:** 0.75pt tonal (40% accent tint, or 25% graphite tint for neutral cards).
- **Shadow (one spec, used consistently):** Deep Navy `#002147` @16% alpha, 2pt offset 90°, 5pt blur (`outerShdw blurRad=63500 dist=25400 dir=5400000`). Dark-field cards and utility bands carry **no** shadow. Nothing else ever carries a shadow.
- **Tiers:** **Primary** — Deep Navy fill, white text: the main conclusion, major KPI, governing principle. **Supporting** — white or 7% pathway tint: pathways, pillars, decision items, analytical content. **Utility** — 4.5% graphite tint, shadowless: proof points, basis notes, context.
- **Density:** 2–4 meaningful cards per slide (row-card layouts up to 3 rows; decision grid 4 compact cards). Never one card per paragraph; keep typography-led and table-led slides in the mix. Cards must not always form identical grids — vary count, proportion and emphasis.

## 5 · Grid, furniture, structure

- Canvas 13.333″ × 7.5″. Working margin 0.7″ (11.93″ content width); editorial slides indent to 1.0″.
- Title band: kicker 0.48″, title 0.80″; content from ≈1.55–1.70″; footer baseline 7.06″.
- **Fixed furniture:** logo top-right (0.38″ high at 11.90″, white version on dark), "Private and Confidential" bottom-left 8.5pt, page number bottom-right. Covers/dividers carry entity line instead of page number.
- Hairlines: 0.75pt Mist; strong rules 1.5pt Navy (table header, principle band top).
- Headline positions and eyebrows **must vary** across a deck (see §7).

## 6 · Charts, tables, numbers, imagery

- **Charts:** flat bars/lines only; no 3D, gridlines minimal or none in schematics; series colours by *meaning* (teal P1, steel P2, Navy neutral); pre-step values at 38% tint with full accent for emphasis; every schematic labelled *"Illustrative profile only — not a forecast"*; source bottom-left 8.5pt.
- **Tables:** rule-led — 1.5pt Navy header rule, 0.75pt Mist row hairlines, 1pt Navy closing rule; no vertical rules; **no alternating fills**; pathway markers for row categorisation; numbers right-aligned; one gold cell maximum (rare).
- **Numbers:** `US$300m` / `S$1.25bn` conventions; bps for small deltas; negatives in parentheses; dates `14 July 2026`.
- **Imagery:** editorial architecture/skyline, cool dusk tonality, ≥1920px (≥3000px for covers — commission/licence for production); navy overlay ≤66% live rectangle; no clip-art, no stock cliché. **Facet motif**: covers/dividers only, single tonal outline.

## 7 · Sequencing & anti-repetition rules (deck level)

1. Never the same fundamental composition more than **twice consecutively**.
2. Never the same card count/arrangement on consecutive slides.
3. Alternate typography-led / card-led / chart-led / table-led / image-led.
4. Vary dominant axis: horizontal, vertical, centred, asymmetrical, full-width.
5. Alternate white pages with tinted pages; dark-field only at strategic moments (§2.4 ratio).
6. No eyebrow on every slide (editorial and statement slides drop it); vary headline position.
7. Dark-field slides are earned: covers, dividers, the pivotal decision or closing synthesis — once per section at most.
8. Review the deck as a *sequence* (flip the sorter) before circulation.

The sample deck demonstrates the rules across 24 slides: cover → agenda → statement → timeline cards → divider → pillar cards → twin cards → process → divider → twin matrix → marker table → cause/effect cards → dashboard → case study → row cards → divider → band cards → table+gate → structure flow → decision grid → dark synthesis → appendix → notice → closing.

## 8 · Layout selection logic (for authors and the authoring skill)

Choose by, in order: **(1) communication objective** (decide → T13; compare → T07/T11; prove → T16/T12; quantify → T08/T09/T10; orient → T03/T05; assert → T04/T14; explain → T15/T17) · **(2) content structure** (pairs → twin; rows of entities → row cards; label+value matrix → table; sequence → process; single figure → anchor) · **(3) importance** (pivotal messages earn Deep Navy or dark-field; routine content stays white) · **(4) audience** (Board/IC mode vs investor mode) · **(5) density** (≥6 rows → table, not cards; ≤25 words/element → cards) · **(6) what the previous two slides used** — apply §7 before finalising. Never select a layout merely because it can accommodate the content.

## 9 · Governance of the system
- Disclaimer wording (SG / AU / KR / KR-REF) and the closing entity/address are **preserved verbatim** in both files; the L&C schedule (7 flagged items) remains with Legal — no legal text changes without approval.
- Cover Option B (navy institutional) = default Board cover; Option A (full-image) = investor/marketing.
- Decision slide: light treatment default; dark-field is an emphasis variant, used sparingly.
- The 8 layout families and 36 archetypes are documented in `ARCHETYPE_CATALOGUE.md`; new archetypes should be composed from existing primitives (cards, rules, markers, bands) rather than new visual devices.
