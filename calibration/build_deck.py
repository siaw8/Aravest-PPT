#!/usr/bin/env python3
"""
Aravest Presentation Design System — Calibration Set (6 slides)
Content is drawn verbatim / near-verbatim from the LOCKED Board Strategy Narrative v8.
Nothing in the strategic narrative is altered or reinterpreted.
Colours reconciled per approved decisions. Two typography modes demonstrated.
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
import copy

A = "assets"

# ---------- APPROVED RECONCILED PALETTE ----------
NAVY      = RGBColor(0x00,0x2B,0x5C)  # Primary
DEEP_NAVY = RGBColor(0x00,0x21,0x47)  # Structural dark
GRAPHITE  = RGBColor(0x35,0x46,0x4F)
SLATE     = RGBColor(0x86,0x93,0x97)
STEEL     = RGBColor(0x46,0x82,0xB4)
TEAL      = RGBColor(0x00,0x80,0x80)
GOLD      = RGBColor(0xC8,0xA9,0x51)
MIST      = RGBColor(0xE8,0xE8,0xE8)
MIST_LT   = RGBColor(0xF4,0xF5,0xF6)
WHITE     = RGBColor(0xFF,0xFF,0xFF)
WHITE_D   = RGBColor(0xDD,0xE2,0xE8)  # dimmed white for dark bg body

HEAD_FONT = "Aptos Display"
BODY_FONT = "Aptos"

SW, SH = Inches(13.333), Inches(7.5)

prs = Presentation()
prs.slide_width  = SW
prs.slide_height = SH
BLANK = prs.slide_layouts[6]

# ---------------- helpers ----------------
def slide():
    return prs.slides.add_slide(BLANK)

def rect(s, x, y, w, h, fill=None, line=None, line_w=None, shape=MSO_SHAPE.RECTANGLE):
    sp = s.shapes.add_shape(shape, x, y, w, h)
    sp.shadow.inherit = False
    if fill is None:
        sp.fill.background()
    else:
        sp.fill.solid(); sp.fill.fore_color.rgb = fill
    if line is None:
        sp.line.fill.background()
    else:
        sp.line.color.rgb = line
        sp.line.width = line_w or Pt(1)
    return sp

def _set_run(r, text, size, font, color, bold=False, italic=False, track=None, caps=False):
    r.text = text
    r.font.size = Pt(size)
    r.font.name = font
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = color
    # East-Asian + latin binding for the specified font
    rPr = r._r.get_or_add_rPr()
    for tag in ("a:latin","a:cs"):
        e = rPr.find(qn(tag))
        if e is None:
            e = rPr.makeelement(qn(tag), {}); rPr.append(e)
        e.set("typeface", font)
    if track is not None:
        rPr.set("spc", str(int(track*100)))
    if caps:
        rPr.set("cap","all")

def textbox(s, x, y, w, h, anchor=MSO_ANCHOR.TOP, wrap=True):
    tb = s.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = wrap
    tf.vertical_anchor = anchor
    tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
    return tb, tf

def para(tf, first=False):
    p = tf.paragraphs[0] if first and not tf.paragraphs[0].runs else tf.add_paragraph()
    return p

def add_line(tf, text, size, font=BODY_FONT, color=GRAPHITE, bold=False, italic=False,
             align=PP_ALIGN.LEFT, space_before=0, space_after=6, first=False, track=None,
             caps=False, line_spacing=None):
    p = para(tf, first=first)
    p.alignment = align
    p.space_before = Pt(space_before)
    p.space_after = Pt(space_after)
    if line_spacing: p.line_spacing = line_spacing
    r = p.add_run()
    _set_run(r, text, size, font, color, bold=bold, italic=italic, track=track, caps=caps)
    return p

def no_grid_table(tbl):
    """Apply 'No Style, No Grid' so we fully control fills/borders."""
    tblPr = tbl._tbl.tblPr
    for child in list(tblPr):
        if child.tag == qn('a:tableStyleId'):
            tblPr.remove(child)
    sid = tblPr.makeelement(qn('a:tableStyleId'), {})
    sid.text = "{2D5ABB26-0587-4C30-8999-92F81FD0307C}"
    tblPr.append(sid)
    tblPr.set('firstRow','0'); tblPr.set('bandRow','0')

def cell_fill(cell, color):
    cell.fill.solid(); cell.fill.fore_color.rgb = color

def cell_text(cell, text, size, color=GRAPHITE, bold=False, font=BODY_FONT,
              align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.MIDDLE):
    cell.vertical_anchor = anchor
    cell.margin_left = Inches(0.10); cell.margin_right = Inches(0.10)
    cell.margin_top = Inches(0.055); cell.margin_bottom = Inches(0.055)
    tf = cell.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.alignment = align
    r = p.add_run()
    _set_run(r, text, size, font, color, bold=bold)
    return cell

def top_border(cell, color, w=1.25):
    tcPr = cell._tc.get_or_add_tcPr()
    ln = tcPr.makeelement(qn('a:lnT'), {'w':str(int(w*12700)),'cap':'flat','cmpd':'sng','algn':'ctr'})
    fill = ln.makeelement(qn('a:solidFill'), {})
    clr = fill.makeelement(qn('a:srgbClr'), {'val':'%02X%02X%02X'%(color[0],color[1],color[2])})
    fill.append(clr); ln.append(fill)
    tcPr.append(ln)

def furniture(s, page, dark=False, logo=True, confid=True):
    """Standard fixed infrastructure: logo TR, confidentiality BL, page BR."""
    fg = WHITE if dark else NAVY
    sub = WHITE_D if dark else SLATE
    if logo:
        lp = A + ("/logo_white.png" if dark else "/logo_navy.png")
        s.shapes.add_picture(lp, Inches(11.86), Inches(0.34), height=Inches(0.40))
    if confid:
        tb,tf = textbox(s, Inches(0.55), Inches(7.05), Inches(6), Inches(0.3), anchor=MSO_ANCHOR.MIDDLE)
        add_line(tf, "Private and Confidential", 8.5, color=sub, first=True, space_after=0)
    tb,tf = textbox(s, Inches(11.5), Inches(7.05), Inches(1.28), Inches(0.3), anchor=MSO_ANCHOR.MIDDLE)
    add_line(tf, str(page), 8.5, color=sub, align=PP_ALIGN.RIGHT, first=True, space_after=0)

def kicker(s, x, y, w, text, color=SLATE):
    tb,tf = textbox(s, x, y, w, Inches(0.28))
    add_line(tf, text, 10.5, color=color, bold=True, first=True, track=1.6, caps=True, space_after=0)

def gold_rule(s, x, y, w, weight=1.5, color=GOLD):
    rect(s, x, y, w, Pt(weight), fill=color)

# =========================================================
# SLIDE 1 — INSTITUTIONAL COVER  (Investor / corporate mode, cover scale)
# =========================================================
s = slide()
rect(s, 0, 0, SW, SH, fill=DEEP_NAVY)                       # navy field
# skyline band (Marina Bay, cropped to a restrained band) full width at bottom
band_h = Inches(13.333*412/1998)
band_y = SH - band_h
s.shapes.add_picture(A+"/hero_singapore_band.jpg", 0, band_y, width=SW, height=band_h)
gold_rule(s, 0, band_y, SW, weight=2.0)                     # crisp gold seam (no gradient)
# reversed logo top-left
s.shapes.add_picture(A+"/logo_white.png", Inches(0.9), Inches(0.70), height=Inches(0.60))
# facet signature — restrained ascending triad, top-right
fx, fy = Inches(11.86), Inches(0.66)
for i,(dx,col) in enumerate([(0.00,STEEL),(0.40,SLATE),(0.80,GOLD)]):
    rect(s, fx+Inches(dx), fy, Inches(0.34), Inches(0.44),
         fill=None, line=col, line_w=Pt(1.0), shape=MSO_SHAPE.ISOSCELES_TRIANGLE)
# eyebrow
tb,tf = textbox(s, Inches(0.9), Inches(2.15), Inches(10.5), Inches(0.35))
add_line(tf, "Private & Confidential  ·  Board Strategy Meeting  ·  September 2026",
         12, color=RGBColor(0xDE,0xD0,0xAD), bold=True, first=True, track=1.8, caps=True, space_after=0)
# title
tb,tf = textbox(s, Inches(0.88), Inches(2.52), Inches(11.6), Inches(1.0))
add_line(tf, "Aravest’s Next Phase", 46, font=HEAD_FONT, color=WHITE, bold=False, first=True, space_after=0)
# subtitle (kept fully within the navy field, above the gold seam)
tb,tf = textbox(s, Inches(0.9), Inches(3.72), Inches(8.9), Inches(0.9))
add_line(tf, "From integration to institution-building: establishing the post-SMFL track record, "
             "defining the near-term investment focus and developing the pathways for sustainable "
             "long-term growth.", 15.5, color=RGBColor(0xD5,0xDD,0xE6), first=True, line_spacing=1.28, space_after=0)
# footer marking on cover
tb,tf = textbox(s, Inches(0.9), Inches(7.02), Inches(11.5), Inches(0.32), anchor=MSO_ANCHOR.MIDDLE)
add_line(tf, "Aravest Fund Management Pte. Ltd.        Private and Confidential",
         9, color=WHITE, first=True, space_after=0)

# =========================================================
# SLIDE 2 — EXECUTIVE SUMMARY  (Investor / corporate mode)
# =========================================================
s = slide()
rect(s, 0, 0, SW, SH, fill=WHITE)
LX = Inches(0.9)
kicker(s, LX, Inches(0.52), Inches(8), "Executive summary")
tb,tf = textbox(s, LX, Inches(0.86), Inches(10.6), Inches(1.15))
add_line(tf, "Aravest is moving from integration into institution-building.",
         32, font=HEAD_FONT, color=NAVY, first=True, line_spacing=1.03, space_after=0)
gold_rule(s, LX, Inches(1.95), Inches(0.9), weight=2.5)
# lead
tb,tf = textbox(s, LX, Inches(2.15), Inches(11.4), Inches(0.9))
add_line(tf, "The initial integration into SMFL has been substantially completed. The next phase is to "
             "develop the institutional foundations and investment record required for sustainable "
             "long-term growth.", 16, color=GRAPHITE, first=True, line_spacing=1.3, space_after=0)
# five key messages in two-column arrangement
msgs = [
 ("01","Values-led. Value-focused.","Aravest is values-led in how it invests and value-focused in where it deploys — sector-flexible, but not strategy-neutral."),
 ("02","A track record through the full lifecycle","Built not through acquisitions alone, but through judgement, execution, stewardship, performance, realisation and repeatability."),
 ("03","Two parallel pathways","Diversified Track Record Building, supported by the existing US$300 million; and Institutional-Scale Opportunities, brought to the Board case-by-case."),
 ("04","Structured to institutional standards","Committed equity is exposed to performance; wider liabilities are ring-fenced, with no automatic recourse to Aravest or SMFL."),
]
cols = [LX, Inches(6.95)]
rowy = [Inches(3.35), Inches(5.15)]
cw = Inches(5.5)
for i,(no,h,b) in enumerate(msgs):
    x = cols[i%2]; y = rowy[i//2]
    tb,tf = textbox(s, x, y, cw, Inches(1.6))
    p = add_line(tf, no+"   ", 15, font=HEAD_FONT, color=GOLD, bold=True, first=True, space_after=3)
    r = p.add_run(); _set_run(r, h, 15, HEAD_FONT, NAVY, bold=False)
    add_line(tf, b, 12.5, color=GRAPHITE, line_spacing=1.22, space_after=0)
furniture(s, 2)

# =========================================================
# SLIDE 3 — TWO-PATHWAY STRATEGY  (Board / IC mode, two panels)
# =========================================================
s = slide()
rect(s, 0, 0, SW, SH, fill=WHITE)
LXb = Inches(0.55)
kicker(s, LXb, Inches(0.48), Inches(8), "Strategy · Two parallel pathways")
tb,tf = textbox(s, LXb, Inches(0.80), Inches(11.0), Inches(0.9))
add_line(tf, "Aravest will build the platform through two complementary pathways.",
         26, font=HEAD_FONT, color=NAVY, first=True, line_spacing=1.03, space_after=0)

panels = [
 (Inches(0.55), NAVY, "Pathway 1", "Diversified Track Record Building",
  [("Primary purpose","Build multiple proof points and a repeatable post-SMFL investment record."),
   ("Typical opportunity","Selected small and medium transactions across repeatable themes."),
   ("Capital profile","Existing US$300 million support, diversified across several investments."),
   ("Risk profile","More diversified, with lower single-asset concentration."),
   ("Expected AUM effect","Gradual and potentially uneven.")]),
 (Inches(6.86), GOLD, "Pathway 2", "Institutional-Scale Opportunities",
  [("Primary purpose","Accelerate AUM, institutional relevance and market visibility."),
   ("Typical opportunity","Selected large transactions capable of creating meaningful scale."),
   ("Capital profile","May require materially greater transaction-specific capital."),
   ("Risk profile","Higher single-asset concentration and liquidity exposure."),
   ("Expected AUM effect","Potential step-change growth.")]),
]
pw = Inches(5.92); ptop = Inches(1.72); ph = Inches(4.55)
for px, accent, tag, title, rows in panels:
    rect(s, px, ptop, pw, ph, fill=MIST_LT, line=MIST, line_w=Pt(0.75))
    rect(s, px, ptop, pw, Pt(3), fill=accent)                 # top accent rule
    tb,tf = textbox(s, px+Inches(0.28), ptop+Inches(0.22), pw-Inches(0.56), Inches(0.9))
    add_line(tf, tag.upper(), 10.5, color=(GOLD if accent==GOLD else SLATE), bold=True, first=True, track=1.5, space_after=2)
    add_line(tf, title, 16.5, font=HEAD_FONT, color=NAVY, space_after=0, line_spacing=1.0)
    yy = ptop+Inches(1.28)
    for lab,val in rows:
        tb,tf = textbox(s, px+Inches(0.28), yy, pw-Inches(0.56), Inches(0.62))
        add_line(tf, lab.upper(), 8.5, color=SLATE, bold=True, first=True, track=1.0, space_after=1)
        add_line(tf, val, 11.5, color=GRAPHITE, line_spacing=1.12, space_after=0)
        yy += Inches(0.64)
# synthesis line
tb,tf = textbox(s, Inches(0.55), Inches(6.42), Inches(12.2), Inches(0.5), anchor=MSO_ANCHOR.MIDDLE)
p = add_line(tf, "The two pathways run in parallel — ", 12.5, color=GRAPHITE, italic=True, first=True, space_after=0)
r=p.add_run(); _set_run(r,"the first builds the record; the second can accelerate scale.",12.5,BODY_FONT,NAVY,italic=True,bold=True)
furniture(s, 3)

# =========================================================
# SLIDE 4 — FINANCIAL / AUM DASHBOARD  (Board / IC mode)
# =========================================================
s = slide()
rect(s, 0, 0, SW, SH, fill=WHITE)
kicker(s, Inches(0.55), Inches(0.48), Inches(9), "Capital & AUM · Dashboard")
tb,tf = textbox(s, Inches(0.55), Inches(0.80), Inches(11.2), Inches(0.9))
add_line(tf, "The two pathways are expected to produce different AUM profiles.",
         26, font=HEAD_FONT, color=NAVY, first=True, line_spacing=1.03, space_after=0)

# KPI tiles
tiles = [
 ("SPONSOR CAPITAL SUPPORT","US$300m","Existing support available to diversify across Pathway 1", NAVY, False),
 ("OPENING AUM","—","To be populated by Finance", SLATE, True),
 ("NET INVESTMENT / (REALISATIONS)","—","To be populated by Finance", SLATE, True),
 ("CLOSING AUM","—","To be populated by Finance", SLATE, True),
]
tx = Inches(0.55); tw = Inches(2.98); gap = Inches(0.11); th = Inches(1.55); ty = Inches(1.78)
for i,(lab,fig,sub,col,ph) in enumerate(tiles):
    x = tx + i*(tw+gap)
    rect(s, x, ty, tw, th, fill=MIST_LT, line=MIST, line_w=Pt(0.75))
    rect(s, x, ty, Pt(3), th, fill=(GOLD if i==0 else MIST))
    tb,tf = textbox(s, x+Inches(0.20), ty+Inches(0.16), tw-Inches(0.35), th-Inches(0.3))
    add_line(tf, lab, 8, color=SLATE, bold=True, first=True, track=0.8, space_after=4)
    add_line(tf, fig, 30, font=HEAD_FONT, color=(NAVY if not ph else SLATE), space_after=3, line_spacing=1.0)
    add_line(tf, sub, 8.5, color=(GRAPHITE if not ph else SLATE), italic=ph, line_spacing=1.1, space_after=0)

# AUM movement identity
rect(s, Inches(0.55), Inches(3.55), Inches(12.23), Inches(0.62), fill=NAVY)
tb,tf = textbox(s, Inches(0.55), Inches(3.55), Inches(12.23), Inches(0.62), anchor=MSO_ANCHOR.MIDDLE)
add_line(tf, "Closing AUM  =  Opening AUM  +  New investments  −  Realisations  ±  Valuation and FX movements",
         14, font=HEAD_FONT, color=WHITE, align=PP_ALIGN.CENTER, first=True, space_after=0)

# two pathway-effect panels + Conrad proof
eff = [
 (Inches(0.55), "Diversified Track Record Building", TEAL,
  "AUM growth is likely to be gradual and uneven — it may remain flat where new investments replace "
  "realisations, or decline temporarily following successful disposals or sell-downs."),
 (Inches(4.66), "Institutional-Scale Opportunities", STEEL,
  "Provide the potential for a material or step-change increase in AUM and more meaningful institutional "
  "ticket sizes, strengthening visibility and fundraising credibility."),
]
for x,h,acc,b in eff:
    rect(s, x, Inches(4.42), Inches(3.96), Inches(1.72), fill=MIST_LT, line=MIST, line_w=Pt(0.75))
    rect(s, x, Inches(4.42), Inches(3.96), Pt(2.5), fill=acc)
    tb,tf = textbox(s, x+Inches(0.22), Inches(4.60), Inches(3.55), Inches(1.45))
    add_line(tf, h, 12, font=HEAD_FONT, color=NAVY, bold=False, first=True, space_after=4, line_spacing=1.0)
    add_line(tf, b, 10, color=GRAPHITE, line_spacing=1.16, space_after=0)
# Conrad proof panel
rect(s, Inches(8.77), Inches(4.42), Inches(4.01), Inches(1.72), fill=DEEP_NAVY)
tb,tf = textbox(s, Inches(8.99), Inches(4.60), Inches(3.6), Inches(1.45))
add_line(tf, "PROOF POINT — CONRAD SEOUL", 8.5, color=GOLD, bold=True, first=True, track=1.2, space_after=4)
add_line(tf, "Sponsor-supported acquisition; institutional capital subsequently introduced (GIC, M&G), "
             "recycling capital while retaining the management relationship.", 10, color=WHITE_D,
             line_spacing=1.18, space_after=0)
# source / caveat
tb,tf = textbox(s, Inches(0.55), Inches(6.42), Inches(12.2), Inches(0.4))
add_line(tf, "Source: Locked Board Strategy Narrative v8. Financial figures to be populated by Finance and "
             "refreshed by the relevant transaction teams before Board circulation.",
         8.5, color=SLATE, italic=True, first=True, line_spacing=1.1, space_after=0)
furniture(s, 4)

# =========================================================
# SLIDE 5 — BOARD DECISION REQUIRED  (Board / IC mode)
# =========================================================
s = slide()
rect(s, 0, 0, SW, SH, fill=WHITE)
kicker(s, Inches(0.55), Inches(0.48), Inches(9), "Board decision required", color=GOLD)
tb,tf = textbox(s, Inches(0.55), Inches(0.80), Inches(11.4), Inches(1.0))
add_line(tf, "The Board is asked to endorse the two-pathway strategy and the basis on which capital is committed.",
         25, font=HEAD_FONT, color=NAVY, first=True, line_spacing=1.05, space_after=0)

decs = [
 ("Endorse the two parallel pathways","as the basis for building the Aravest platform — diversified track-record building alongside selective institutional-scale opportunities."),
 ("Support deployment of the existing US$300 million","across Pathway 1 to build multiple proof points and diversify risk."),
 ("Endorse warehousing as an execution enabler","bridging the timing gap between securing a transaction and forming third-party capital."),
 ("Agree each Institutional-Scale Opportunity is brought to the Board separately","with its investment merits, capital requirement and risk profile, for decision case-by-case."),
]
yy = Inches(2.05)
for i,(h,b) in enumerate(decs,1):
    rect(s, Inches(0.55), yy, Inches(0.44), Inches(0.44), fill=NAVY)
    tb,tf = textbox(s, Inches(0.55), yy, Inches(0.44), Inches(0.44), anchor=MSO_ANCHOR.MIDDLE)
    add_line(tf, str(i), 14, font=HEAD_FONT, color=WHITE, bold=True, align=PP_ALIGN.CENTER, first=True, space_after=0)
    tb,tf = textbox(s, Inches(1.18), yy-Inches(0.02), Inches(11.4), Inches(0.75))
    p = add_line(tf, h+" ", 13.5, font=HEAD_FONT, color=NAVY, bold=False, first=True, space_after=0, line_spacing=1.1)
    r = p.add_run(); _set_run(r, b, 12.5, BODY_FONT, GRAPHITE)
    yy += Inches(0.82)

# rationale band
rect(s, Inches(0.55), Inches(5.42), Inches(12.23), Inches(0.98), fill=MIST_LT, line=MIST, line_w=Pt(0.75))
rect(s, Inches(0.55), Inches(5.42), Pt(3), Inches(0.98), fill=GOLD)
tb,tf = textbox(s, Inches(0.85), Inches(5.42), Inches(11.7), Inches(0.98), anchor=MSO_ANCHOR.MIDDLE)
add_line(tf, "BASIS OF CAPITAL COMMITMENT", 8.5, color=SLATE, bold=True, first=True, track=1.2, space_after=3)
add_line(tf, "Committed equity is exposed to investment performance; wider fund and asset liabilities are generally "
             "ring-fenced, with no automatic recourse to Aravest as manager or SMFL as shareholder. Any exception "
             "must be explicit and separately approved.", 11, color=GRAPHITE, line_spacing=1.16, space_after=0)
# footnote
tb,tf = textbox(s, Inches(0.55), Inches(6.55), Inches(12.2), Inches(0.35))
add_line(tf, "Formal resolutions to be confirmed by management and the company secretary. This slide reflects the "
             "locked Board Strategy Narrative v8 and does not itself constitute a resolution.",
         8.5, color=SLATE, italic=True, first=True, line_spacing=1.1, space_after=0)
furniture(s, 5)

# =========================================================
# SLIDE 6 — DENSE INSTITUTIONAL TABLE / INVESTMENT CASE  (Board / IC mode)
# =========================================================
s = slide()
rect(s, 0, 0, SW, SH, fill=WHITE)
kicker(s, Inches(0.55), Inches(0.48), Inches(9), "Investment case · Current pipeline")
tb,tf = textbox(s, Inches(0.55), Inches(0.80), Inches(11.6), Inches(0.9))
add_line(tf, "Current opportunities illustrate how the two pathways may develop in practice.",
         26, font=HEAD_FONT, color=NAVY, first=True, line_spacing=1.03, space_after=0)

rows = [
 ("Strategic role","Illustrative opportunities","Connection to the pathway"),
 ("Institutional-scale opportunity","Marina One and other selected large opportunities.",
  "Potential to create a material increase in AUM, institutional relevance and market visibility."),
 ("Portfolio building block","Project Guardian / PBSA and subsequent PBSA opportunities.",
  "Build a repeatable strategy through aggregation into a portfolio of institutional scale."),
 ("Track-record proof point","Courtyard by Marriott Suwon, ARA-NH Fund 2, Aberdeen / Shinyoung recapitalisation and other relevant transactions.",
  "Deepen post-SMFL execution evidence and create additional realisation or recycling pathways."),
]
tbl_x, tbl_y = Inches(0.55), Inches(1.85)
tbl_w, tbl_h = Inches(12.23), Inches(3.95)
gfx = s.shapes.add_table(len(rows), 3, tbl_x, tbl_y, tbl_w, tbl_h)
tbl = gfx.table
no_grid_table(tbl)
tbl.columns[0].width = Inches(2.9)
tbl.columns[1].width = Inches(4.9)
tbl.columns[2].width = Inches(4.43)
tbl.rows[0].height = Inches(0.5)
for ri,row in enumerate(rows):
    for ci,val in enumerate(row):
        cell = tbl.cell(ri,ci)
        if ri==0:
            cell_fill(cell, NAVY)
            cell_text(cell, val, 10.5, color=WHITE, bold=True)
        else:
            cell_fill(cell, WHITE if ri%2==1 else MIST_LT)
            cell_text(cell, val, 10 if ci>0 else 10.5,
                      color=(NAVY if ci==0 else GRAPHITE), bold=(ci==0),
                      anchor=MSO_ANCHOR.MIDDLE)
    if ri>0:
        tbl.rows[ri].height = Inches(1.12)
# caveat
tb,tf = textbox(s, Inches(0.55), Inches(6.28), Inches(12.2), Inches(0.6))
add_line(tf, "Private credit is excluded as a core Aravest growth strategy (an agreed SMDAM strategy, with Aravest "
             "providing support where relevant). Transaction names, figures and status to be refreshed by the "
             "relevant transaction teams before Board circulation.",
         8.5, color=SLATE, italic=True, first=True, line_spacing=1.15, space_after=0)
furniture(s, 6)

prs.save("Aravest_Calibration_Set_v1.pptx")
print("saved Aravest_Calibration_Set_v1.pptx with", len(prs.slides.__iter__.__self__._sldIdLst), "slides")
