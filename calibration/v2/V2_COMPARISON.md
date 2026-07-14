# Calibration Set v2 — What changed and why
*One-page comparison: typography and gold. Content remains verbatim from the Locked Board Strategy Narrative v8.*

---

## 1 · Typography — the website-aligned secondary face

Inspected directly from the live site's CSS (`aravest.com/assets/fonts.css`, `styles.css`):

| Question | Finding |
|---|---|
| **Exact typeface** | **Spectral** — the site's display serif (`--serif: 'Spectral', Georgia, 'Times New Roman', serif`). Weights self-hosted: 300 (Light — the primary display weight), 400, 500, 600, plus **true italics at 300/400**. Sans is Archivo (nav/labels only). |
| **The italic treatment** | Spectral Light **Italic applied to one emphasised phrase inside a headline** (`.hero__tag em`, `.statement__big .accent`, `.pillar__t em`). The site suppresses these italics for Korean/Japanese text — synthesised CJK italics are avoided, which aligns with our Japanese-shareholder constraint. |
| **Source & licensing** | Designed by Production Type for Google Fonts. **SIL Open Font License 1.1** — free, no per-seat cost, redistributable, embedding permitted. |
| **PowerPoint / Windows availability** | **Not pre-installed** on Windows, macOS or Office. Requires a one-time install (free TTFs) — a small IT package for Aravest machines. |
| **Fallback behaviour** | On a machine without Spectral, PowerPoint substitutes a default serif (Times New Roman-class). Layout holds (similar metrics); the light editorial character is lost until the font is installed or embedded. The website's own declared fallback is Georgia → Times New Roman. |
| **Embedding / distribution** | Font files carry `fsType = 0` (**installable embedding** — the most permissive flag). PowerPoint's *Embed fonts in file* works, and the OFL allows distribution of the TTFs internally. The final master template will ship with embedding on. |

**Usage rule applied in v2** — Spectral appears in exactly three places: the two cover titles (roman + one italic phrase, mirroring the website hero) and one italic phrase in the executive-summary headline (*institution-building*). Everything else — body, tables, charts, KPI figures, decision lists, footnotes, working-slide headings — remains **Aptos Display / Aptos**. Measured share of Spectral text in v2: **≈3%** (limit: 5–10%).

---

## 2 · Gold — from hierarchy colour to rare signal

| Location | v1 | v2 |
|---|---|---|
| Cover(s) | Gold seam rule + gold facet triangle + gold-tinted eyebrow | **One** short gold rule above the eyebrow — nothing else |
| Executive summary | Gold underline + gold numerals 01–04 | **None** — numerals slate, spine hairline mist |
| Two-pathway strategy | Gold "PATHWAY 2" label + gold top border (implied preference) | **None** — both pathways identical navy treatment, roles in steel blue |
| Capital & AUM | Gold accent strip on the US$300m tile | **None** — navy rule anchor, tonal navy/steel schematics |
| Board decision | Gold kicker + gold accent strip on principle card | **One** small gold square marking "FOR DECISION" — the only gold on any working slide, reserved for a true Board decision |
| Pipeline table | (navy header band, no gold) | **None** — rule-led table, steel pathway tags |
| **Total gold elements** | ~8 across 6 slides | **3 across 7 slides** — two covers + the decision marker |

## 3 · Generic-treatment removal

- **No cards or floating boxes** — panels replaced by hairline-ruled rows, rule-anchored blocks and typography-led hierarchy; alternating grey fills removed from tables.
- **No shadows, no accent strips, no heavy outlines**; the facet cluster is gone — Option B carries a single subtle tonal facet line, covers only.
- **Three distinct rhythms** so the deck no longer repeats one eyebrow-title-box formula:
  **Editorial** (covers, executive summary — Spectral moments, asymmetry, no kicker) · **Analysis** (pathways matrix, AUM schematics, pipeline — kicker + hairline discipline) · **Governance** (decision — action-verb architecture ENDORSE / SUPPORT / ENDORSE / AGREE, rule-bound governing principle, single gold signal).

## 4 · Covers

- **Option A** — full-bleed Marina Bay image under a controlled Deep Navy overlay (66%, live and adjustable in PowerPoint), editorial Spectral headline, no triangles, one gold rule.
- **Option B** — predominantly navy; vertical architectural crop on the right edge; generous whitespace; one subtle tonal facet outline; one gold rule.
- The v1 horizontal photo band is retired as the default cover. *Production note: current imagery is reused from the template at its native resolution; final covers warrant commissioned/licensed photography at ≥3000px.*
