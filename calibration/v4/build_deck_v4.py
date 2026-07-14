#!/usr/bin/env python3
"""
Aravest Presentation Design System — Calibration Set v4
Content verbatim/near-verbatim from the LOCKED Board Strategy Narrative v8 (unchanged from v3).

v4 vs v3 — functional colour + institutional card language:
- Colour roles: Deep Navy structural · Graphite secondary/body · TEAL = Pathway 1
  (builds the record) · STEEL = Pathway 2 (accelerates scale). Max two active accents
  per working slide; tints ~4-6%; gold only as the rare Board-level signal.
- Cards: rounded ~8pt radius, thin tonal borders (0.75pt), one consistent subtle
  shadow spec; three tiers (primary dark / supporting tinted-white / utility quiet).
- Six distinct compositions across the working slides + one dark-field decision
  alternative. Covers unchanged from v3.
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
from lxml import etree

A="assets"

# ---------- palette & roles ----------
NAVY      = RGBColor(0x00,0x2B,0x5C)   # brand primary (headings)
DEEP_NAVY = RGBColor(0x00,0x21,0x47)   # structural / dark fields / conclusions
GRAPHITE  = RGBColor(0x35,0x46,0x4F)   # secondary structure & body text
SLATE     = RGBColor(0x86,0x93,0x97)
STEEL     = RGBColor(0x46,0x82,0xB4)   # Pathway 2 — acceleration
TEAL      = RGBColor(0x00,0x80,0x80)   # Pathway 1 — the record
GOLD      = RGBColor(0xC8,0xA9,0x51)
MIST      = RGBColor(0xE8,0xE8,0xE8)
WHITE     = RGBColor(0xFF,0xFF,0xFF)
WHITE_D   = RGBColor(0xD5,0xDD,0xE6)

def _tint(c,p):  # p = colour share over white
    return RGBColor(round(255*(1-p)+c[0]*p), round(255*(1-p)+c[1]*p), round(255*(1-p)+c[2]*p))
def _shade_on(base,c,p):  # mix c into base
    return RGBColor(round(base[0]*(1-p)+c[0]*p), round(base[1]*(1-p)+c[1]*p), round(base[2]*(1-p)+c[2]*p))

TEAL_T   = _tint(TEAL,0.05)     # card fill tint ~5%
STEEL_T  = _tint(STEEL,0.05)
TEAL_B   = _tint(TEAL,0.35)     # tonal borders
STEEL_B  = _tint(STEEL,0.35)
GRAPH_B  = _tint(GRAPHITE,0.25)
GRAPH_T  = _tint(GRAPHITE,0.045) # utility fill
TEAL_L   = _tint(TEAL,0.45)      # not used on white; light accents on navy
STEEL_L  = _tint(STEEL,0.50)
TEAL_LT  = RGBColor(0x8F,0xC6,0xC6)   # pathway names on deep navy
STEEL_LT = RGBColor(0xA9,0xC6,0xE2)
NAVY_CARD_L = _shade_on(DEEP_NAVY,WHITE,0.07)  # tonal card on dark field
NAVY_CARD_B = _shade_on(DEEP_NAVY,WHITE,0.22)

HEAD="Aptos Display"; BODY="Aptos"
SERIF="Spectral Light"

SW,SH=Inches(13.333),Inches(7.5)
prs=Presentation(); prs.slide_width,prs.slide_height=SW,SH
BLANK=prs.slide_layouts[6]
def slide(): return prs.slides.add_slide(BLANK)

def rect(s,x,y,w,h,fill=None,line=None,line_w=None,shape=MSO_SHAPE.RECTANGLE,alpha=None):
    sp=s.shapes.add_shape(shape,x,y,w,h); sp.shadow.inherit=False
    if fill is None: sp.fill.background()
    else:
        sp.fill.solid(); sp.fill.fore_color.rgb=fill
        if alpha is not None:
            clr=sp.fill._xPr.find(qn('a:solidFill')).find(qn('a:srgbClr'))
            a=clr.makeelement(qn('a:alpha'),{'val':str(int(alpha*100000))}); clr.append(a)
    if line is None: sp.line.fill.background()
    else: sp.line.color.rgb=line; sp.line.width=line_w or Pt(1)
    return sp

def card(s,x,y,w,h,fill=WHITE,line=None,line_w=Pt(0.75),radius=Inches(0.09),shadow=True):
    """Institutional card: moderate rounded corners, thin tonal border, one subtle shadow spec."""
    sp=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,x,y,w,h)
    sp.shadow.inherit=False
    try: sp.adjustments[0]=float(radius)/float(min(w,h))
    except Exception: pass
    sp.fill.solid(); sp.fill.fore_color.rgb=fill
    if line is None: sp.line.fill.background()
    else: sp.line.color.rgb=line; sp.line.width=line_w
    if shadow:
        el=sp._element.spPr.find(qn('a:effectLst'))
        o=etree.SubElement(el,qn('a:outerShdw'),
            {'blurRad':'63500','dist':'25400','dir':'5400000','rotWithShape':'0'})
        c=etree.SubElement(o,qn('a:srgbClr'),{'val':'002147'})
        etree.SubElement(c,qn('a:alpha'),{'val':'16000'})
    return sp

def hrule(s,x,y,w,weight=0.75,color=MIST): return rect(s,x,y,w,Pt(weight),fill=color)

def _set(r,text,size,font,color,bold=False,italic=False,track=None,caps=False):
    r.text=text; r.font.size=Pt(size); r.font.name=font
    r.font.bold=bold; r.font.italic=italic; r.font.color.rgb=color
    rPr=r._r.get_or_add_rPr()
    for tag in ("a:latin","a:cs"):
        e=rPr.find(qn(tag))
        if e is None: e=rPr.makeelement(qn(tag),{}); rPr.append(e)
        e.set("typeface",font)
    if track is not None: rPr.set("spc",str(int(track*100)))
    if caps: rPr.set("cap","all")

def textbox(s,x,y,w,h,anchor=MSO_ANCHOR.TOP):
    tb=s.shapes.add_textbox(x,y,w,h); tf=tb.text_frame
    tf.word_wrap=True; tf.vertical_anchor=anchor
    tf.margin_left=0; tf.margin_right=0; tf.margin_top=0; tf.margin_bottom=0
    return tb,tf
def para(tf,first=False):
    return tf.paragraphs[0] if first and not tf.paragraphs[0].runs else tf.add_paragraph()
def line(tf,text,size,font=BODY,color=GRAPHITE,bold=False,italic=False,align=PP_ALIGN.LEFT,
         sb=0,sa=6,first=False,track=None,caps=False,ls=None):
    p=para(tf,first=first); p.alignment=align
    p.space_before=Pt(sb); p.space_after=Pt(sa)
    if ls: p.line_spacing=ls
    r=p.add_run(); _set(r,text,size,font,color,bold=bold,italic=italic,track=track,caps=caps)
    return p

def furniture(s,page,dark=False):
    fg=WHITE_D if dark else SLATE
    tb,tf=textbox(s,Inches(0.7),Inches(7.06),Inches(5),Inches(0.3),anchor=MSO_ANCHOR.MIDDLE)
    line(tf,"Private and Confidential",8.5,color=fg,first=True,sa=0)
    tb,tf=textbox(s,Inches(11.6),Inches(7.06),Inches(1.03),Inches(0.3),anchor=MSO_ANCHOR.MIDDLE)
    line(tf,str(page),8.5,color=fg,align=PP_ALIGN.RIGHT,first=True,sa=0)
    s.shapes.add_picture(A+("/logo_white.png" if dark else "/logo_navy.png"),
                         Inches(11.90),Inches(0.36),height=Inches(0.38))

def kicker(s,x,y,text,color=GRAPHITE):
    tb,tf=textbox(s,x,y,Inches(9),Inches(0.28))
    line(tf,text,10,color=color,bold=True,first=True,track=1.6,caps=True,sa=0)

SUBTITLE=("From integration to institution-building: establishing the post-SMFL track record, "
          "defining the near-term investment focus and developing the pathways for sustainable "
          "long-term growth.")
def cover_title(s,x,y,w,size=44):
    tb,tf=textbox(s,x,y,w,Inches(1.05))
    p=para(tf,first=True); p.alignment=PP_ALIGN.LEFT; p.space_after=Pt(0)
    r=p.add_run(); _set(r,"Aravest’s ",size,SERIF,WHITE)
    r=p.add_run(); _set(r,"Next Phase",size,SERIF,WHITE,italic=True)

# ============ SLIDE 1 — COVER A (unchanged from v3) ============
s=slide()
s.shapes.add_picture(A+"/coverA_full.jpg",0,0,width=SW,height=SH)
rect(s,0,0,SW,SH,fill=DEEP_NAVY,alpha=0.66)
s.shapes.add_picture(A+"/logo_white.png",Inches(1.0),Inches(0.75),height=Inches(0.58))
hrule(s,Inches(1.0),Inches(2.98),Inches(0.85),weight=1.5,color=GOLD)
tb,tf=textbox(s,Inches(1.0),Inches(3.16),Inches(10.5),Inches(0.32))
line(tf,"Board Strategy Meeting  ·  September 2026",11,color=WHITE_D,bold=True,first=True,track=1.8,caps=True,sa=0)
cover_title(s,Inches(0.98),Inches(3.56),Inches(11.4),size=46)
tb,tf=textbox(s,Inches(1.0),Inches(4.78),Inches(8.7),Inches(1.0))
line(tf,SUBTITLE,14.5,color=WHITE_D,first=True,ls=1.32,sa=0)
tb,tf=textbox(s,Inches(1.0),Inches(6.95),Inches(11.3),Inches(0.32))
line(tf,"Aravest Fund Management Pte. Ltd.      Private and Confidential",9,color=WHITE_D,first=True,sa=0)

# ============ SLIDE 2 — COVER B (unchanged from v3) ============
s=slide()
rect(s,0,0,SW,SH,fill=DEEP_NAVY)
rect(s,Inches(-2.1),Inches(4.15),Inches(6.4),Inches(4.6),fill=None,
     line=_shade_on(DEEP_NAVY,WHITE,0.12),line_w=Pt(1.0),shape=MSO_SHAPE.ISOSCELES_TRIANGLE)
s.shapes.add_picture(A+"/coverB_strip.jpg",Inches(9.36),0,width=Inches(3.973),height=SH)
s.shapes.add_picture(A+"/logo_white.png",Inches(1.0),Inches(0.75),height=Inches(0.58))
hrule(s,Inches(1.0),Inches(2.86),Inches(0.85),weight=1.5,color=GOLD)
tb,tf=textbox(s,Inches(1.0),Inches(3.04),Inches(8),Inches(0.32))
line(tf,"Board Strategy Meeting  ·  September 2026",11,color=SLATE,bold=True,first=True,track=1.8,caps=True,sa=0)
cover_title(s,Inches(0.98),Inches(3.44),Inches(8.2),size=42)
tb,tf=textbox(s,Inches(1.0),Inches(4.58),Inches(7.5),Inches(1.1))
line(tf,SUBTITLE,13.5,color=WHITE_D,first=True,ls=1.32,sa=0)
tb,tf=textbox(s,Inches(1.0),Inches(6.95),Inches(8),Inches(0.32))
line(tf,"Aravest Fund Management Pte. Ltd.      Private and Confidential",9,color=WHITE_D,first=True,sa=0)

# ============ SLIDE 3 — EXECUTIVE SUMMARY ============
# Composition 1: editorial headline → four differentiated strategic cards → navy conclusion band
s=slide()
rect(s,0,0,SW,SH,fill=WHITE)
LX=Inches(1.0); CW=Inches(11.33)
tb,tf=textbox(s,LX,Inches(0.56),CW,Inches(1.35))
p=para(tf,first=True); p.alignment=PP_ALIGN.LEFT; p.space_after=Pt(0); p.line_spacing=1.06
r=p.add_run(); _set(r,"Aravest is moving from integration",30,HEAD,NAVY)
p=tf.add_paragraph(); p.alignment=PP_ALIGN.LEFT; p.space_after=Pt(0); p.line_spacing=1.06
r=p.add_run(); _set(r,"into ",30,HEAD,NAVY)
r=p.add_run(); _set(r,"institution-building",30,SERIF,NAVY,italic=True)
r=p.add_run(); _set(r,".",30,HEAD,NAVY)
tb,tf=textbox(s,LX,Inches(1.92),Inches(11.1),Inches(0.8))
line(tf,"The initial integration into SMFL has been substantially completed. The next phase "
        "is to develop the institutional foundations and investment record required for "
        "sustainable long-term growth.",14,color=GRAPHITE,first=True,ls=1.26,sa=0)

concl=[
 ("01","The Aravest Way",TEAL,TEAL_T,TEAL_B,
  "Values-led in how it invests; value-focused in where it deploys.",
  "Investment management is a responsibility before it is a business — sector-flexible, but not strategy-neutral."),
 ("02","The post-SMFL record",None,WHITE,GRAPH_B,
  "Judgement, execution, stewardship, performance, realisation and repeatability.",
  "Confidence moves from the individual opportunity, to the repeat relationship, to the Aravest strategy."),
 ("03","Two parallel pathways",STEEL,STEEL_T,STEEL_B,
  "Diversified track-record building on the existing US$300 million.",
  "Institutional-scale opportunities, case-by-case, can accelerate AUM, relevance and visibility."),
 ("04","Institutional standards",None,WHITE,GRAPH_B,
  "Committed equity bears performance; wider liabilities are ring-fenced.",
  "No automatic recourse to Aravest or SMFL; every fund structured to institutional standards."),
]
CY=Inches(2.86); CH=Inches(2.98); colw=Inches(2.72); gap=Inches(0.15)
for i,(no,h,acc,fillc,bord,b1,b2) in enumerate(concl):
    x=LX+i*(colw+gap)
    card(s,x,CY,colw,CH,fill=fillc,line=bord)
    tb,tf=textbox(s,x+Inches(0.20),CY+Inches(0.18),colw-Inches(0.40),CH-Inches(0.36))
    line(tf,no,10.5,color=(acc or SLATE),bold=True,first=True,track=1.2,sa=5)
    line(tf,h,14.5,font=HEAD,color=NAVY,sa=6,ls=1.03)
    line(tf,b1,12,color=GRAPHITE,ls=1.22,sa=6)
    line(tf,b2,11.5,color=GRAPHITE,ls=1.22,sa=0)
card(s,LX,Inches(6.10),CW,Inches(0.60),fill=DEEP_NAVY,line=None)
tb,tf=textbox(s,LX+Inches(0.28),Inches(6.10),CW-Inches(0.56),Inches(0.60),anchor=MSO_ANCHOR.MIDDLE)
p=para(tf,first=True); p.space_after=Pt(0)
r=p.add_run(); _set(r,"One strategy.  ",13,HEAD,WHITE)
r=p.add_run(); _set(r,"The standards stay constant while the record, the pathways and the structure "
                     "compound into an institution.",13,BODY,WHITE_D)
furniture(s,2)

# ============ SLIDE 4 — TWO PATHWAYS ============
# Composition 2: twin equal tinted pathway cards + deep-navy parallel connector
s=slide()
rect(s,0,0,SW,SH,fill=WHITE)
LX=Inches(0.7); RW=Inches(11.93)
kicker(s,LX,Inches(0.48),"Strategy · Two parallel pathways")
tb,tf=textbox(s,LX,Inches(0.80),Inches(11.9),Inches(0.6))
line(tf,"Aravest will build the platform through two complementary pathways.",
     24,font=HEAD,color=NAVY,first=True,ls=1.02,sa=0)

prow=[("Primary purpose",
       "Build multiple proof points and a repeatable post-SMFL investment record.",
       "Accelerate AUM, institutional relevance and market visibility."),
      ("Typical opportunity",
       "Selected small and medium transactions across repeatable themes.",
       "Selected large transactions capable of creating meaningful scale."),
      ("Capital profile",
       "The existing US$300 million support, diversified across several investments.",
       "May require materially greater transaction-specific capital."),
      ("Risk profile",
       "More diversified, with lower single-asset concentration.",
       "Higher single-asset concentration and greater liquidity exposure."),
      ("Expected AUM effect",
       "Gradual and potentially uneven growth.",
       "Potential step-change growth.")]
CY=Inches(1.54); CH=Inches(4.42); CWD=Inches(5.80)
X1=LX; X2=Inches(6.83)
off=[Inches(1.06),Inches(1.78),Inches(2.50),Inches(3.22),Inches(3.90)]
for X,name,role,acc,fillc,bord,accL in [
    (X1,"Pathway 1 — Diversified Track Record Building","Builds the record",TEAL,TEAL_T,TEAL_B,TEAL),
    (X2,"Pathway 2 — Institutional-Scale Opportunities","Can accelerate scale",STEEL,STEEL_T,STEEL_B,STEEL)]:
    card(s,X,CY,CWD,CH,fill=fillc,line=bord)
    rect(s,X+Inches(0.22),CY,CWD-Inches(0.44),Pt(2.5),fill=acc)     # top rule inside card
    tb,tf=textbox(s,X+Inches(0.26),CY+Inches(0.16),CWD-Inches(0.52),Inches(0.85))
    line(tf,name,15,font=HEAD,color=NAVY,first=True,ls=1.04,sa=3)
    line(tf,role.upper(),9.5,color=accL,bold=True,track=1.2,sa=0)
    vals=[r[1] if X==X1 else r[2] for r in prow]
    for o,(lab,v) in zip(off,[(r[0],v) for r,v in zip(prow,vals)]):
        tb,tf=textbox(s,X+Inches(0.26),CY+o,CWD-Inches(0.52),Inches(0.70))
        line(tf,lab.upper(),9,color=GRAPHITE,bold=True,first=True,track=0.8,sa=2)
        line(tf,v,12.5,color=GRAPHITE,ls=1.15,sa=0)
card(s,LX,Inches(6.14),RW,Inches(0.58),fill=DEEP_NAVY,line=None)
tb,tf=textbox(s,LX+Inches(0.28),Inches(6.14),RW-Inches(0.56),Inches(0.58),anchor=MSO_ANCHOR.MIDDLE)
p=para(tf,first=True); p.space_after=Pt(0)
r=p.add_run(); _set(r,"RUN IN PARALLEL   ",10,BODY,WHITE_D,bold=True,track=1.4)
r=p.add_run(); _set(r,"Pathway 1 builds the record",13,BODY,TEAL_LT,bold=True)
r=p.add_run(); _set(r,";  ",13,BODY,WHITE_D)
r=p.add_run(); _set(r,"Pathway 2 can accelerate scale",13,BODY,STEEL_LT,bold=True)
r=p.add_run(); _set(r,".",13,BODY,WHITE_D)
furniture(s,3)

# ============ SLIDE 5 — CAPITAL & AUM ============
# Composition 3: dark anchor card + two pathway-coloured profile cards + utility proof band
s=slide()
rect(s,0,0,SW,SH,fill=WHITE)
LX=Inches(0.7); RW=Inches(11.93)
kicker(s,LX,Inches(0.48),"Capital & AUM")
tb,tf=textbox(s,LX,Inches(0.80),Inches(11.9),Inches(0.6))
line(tf,"The two pathways are expected to produce different AUM profiles.",
     24,font=HEAD,color=NAVY,first=True,ls=1.02,sa=0)
hrule(s,LX,Inches(1.56),RW,weight=0.75,color=MIST)
tb,tf=textbox(s,LX,Inches(1.68),RW,Inches(0.40),anchor=MSO_ANCHOR.MIDDLE)
line(tf,"Closing AUM  =  Opening AUM  +  New investments  −  Realisations  ±  Valuation and FX movements",
     14.5,font=HEAD,color=NAVY,align=PP_ALIGN.CENTER,first=True,sa=0)
hrule(s,LX,Inches(2.20),RW,weight=0.75,color=MIST)

AY=Inches(2.44); AH=Inches(3.42)
card(s,LX,AY,Inches(3.05),AH,fill=DEEP_NAVY,line=None)          # primary anchor card
tb,tf=textbox(s,LX+Inches(0.26),AY+Inches(0.22),Inches(2.55),AH-Inches(0.44))
line(tf,"SPONSOR CAPITAL SUPPORT",9,color=WHITE_D,bold=True,first=True,track=1.0,sa=8)
line(tf,"US$300m",34,font=HEAD,color=WHITE,sa=9,ls=1.0)
line(tf,"Existing support, diversified across several Pathway 1 investments.",12.5,color=WHITE_D,ls=1.26,sa=6)
line(tf,"Warehousing bridges transaction execution and third-party capital formation.",12.5,color=WHITE_D,ls=1.26,sa=0)

def profile_card(x,w,title,titlec,heights,bars_fill,step_idx=None,step_fill=None,caption=""):
    card(s,x,AY,w,AH,fill=WHITE,line=GRAPH_B)
    tb,tf=textbox(s,x+Inches(0.24),AY+Inches(0.18),w-Inches(0.48),Inches(0.5))
    line(tf,title,13.5,font=HEAD,color=titlec,first=True,ls=1.03,sa=0)
    base=AY+Inches(2.02); maxh=1.18
    n=len(heights); bw=Inches(0.38); ix=x+Inches(0.24); iw=w-Inches(0.48)
    gp=(iw-bw*n)/(n-1)
    for i,hh in enumerate(heights):
        bh=Inches(hh*maxh)
        fillc=step_fill if (step_idx is not None and i>=step_idx) else bars_fill
        rect(s,ix+i*(bw+gp),base-bh,bw,bh,fill=fillc)
    hrule(s,ix,base,iw,weight=1.0,color=GRAPH_B)
    tb,tf=textbox(s,x+Inches(0.24),base+Inches(0.10),w-Inches(0.48),Inches(1.1))
    line(tf,caption,11.5,color=GRAPHITE,first=True,ls=1.2,sa=3)
    line(tf,"Illustrative profile only — not a forecast.",9,color=SLATE,italic=True,sa=0)

profile_card(Inches(3.95),Inches(4.28),"Pathway 1 — gradual and uneven",TEAL,
             [0.42,0.55,0.47,0.62,0.52,0.70,0.63],TEAL,
             caption="AUM may grow gradually, remain flat where new investments replace "
                     "realisations, or decline temporarily after disposals or sell-downs.")
profile_card(Inches(8.43),Inches(4.20),"Pathway 2 — potential step-change",STEEL,
             [0.36,0.38,0.40,0.93,0.95,1.0,1.0],_tint(STEEL,0.38),step_idx=3,step_fill=STEEL,
             caption="A single institutional-scale transaction can create a material or "
                     "step-change increase in AUM and more meaningful ticket sizes.")

card(s,LX,Inches(6.06),RW,Inches(0.56),fill=GRAPH_T,line=GRAPH_B,shadow=False)  # utility proof band
tb,tf=textbox(s,LX+Inches(0.26),Inches(6.06),RW-Inches(0.52),Inches(0.56),anchor=MSO_ANCHOR.MIDDLE)
p=para(tf,first=True); p.space_after=Pt(0); p.line_spacing=1.15
r=p.add_run(); _set(r,"PROOF POINT — CONRAD SEOUL   ",9.5,BODY,NAVY,bold=True,track=1.0)
r=p.add_run(); _set(r,"Sponsor-supported acquisition; institutional capital subsequently introduced "
                     "(GIC, M&G), recycling capital while retaining the management relationship.",12,BODY,GRAPHITE)
tb,tf=textbox(s,LX,Inches(6.72),RW,Inches(0.3))
line(tf,"Source: Locked Board Strategy Narrative v8. Financial figures to be populated by Finance "
        "before Board circulation.",8.5,color=SLATE,italic=True,first=True,sa=0)
furniture(s,4)

# ============ SLIDE 6 — BOARD DECISION (light) ============
# Composition 4: 2×2 compact decision cards + deep-navy governing-principle card
DECS=[
 ("Endorse","the two parallel pathways as the basis for building the Aravest platform — "
            "diversified track-record building alongside selective institutional-scale opportunities."),
 ("Support","deployment of the existing US$300 million across Pathway 1 to build multiple "
            "proof points and diversify risk."),
 ("Endorse","warehousing as an execution enabler, bridging the timing gap between securing "
            "a transaction and forming third-party capital."),
 ("Agree","that each Institutional-Scale Opportunity is brought to the Board separately — with its "
          "investment merits, capital requirement and risk profile — for decision case-by-case."),
]
GOV=("Committed equity is exposed to investment performance; wider fund and asset liabilities "
     "are generally ring-fenced, with no automatic recourse to Aravest as manager or SMFL as "
     "shareholder. Any exception must be explicit and separately approved.")
FOOT=("Formal resolutions to be confirmed by management and the company secretary; this slide "
      "reflects the locked Board Strategy Narrative v8 and does not itself constitute a resolution.")

s=slide()
rect(s,0,0,SW,SH,fill=WHITE)
LX=Inches(0.7); RW=Inches(11.93)
rect(s,LX,Inches(0.53),Inches(0.11),Inches(0.11),fill=GOLD)
tb,tf=textbox(s,LX+Inches(0.24),Inches(0.48),Inches(9),Inches(0.28))
line(tf,"For decision",10,color=NAVY,bold=True,first=True,track=1.6,caps=True,sa=0)
tb,tf=textbox(s,LX,Inches(0.82),Inches(12.0),Inches(0.95))
line(tf,"The Board is asked to endorse the two-pathway strategy and the basis on which "
        "capital is committed.",24,font=HEAD,color=NAVY,first=True,ls=1.05,sa=0)
DCW=Inches(5.86); DCH=Inches(1.34); GX=[LX,Inches(6.77)]; GY_=[Inches(2.02),Inches(3.52)]
for i,(verb,rest) in enumerate(DECS):
    x=GX[i%2]; y=GY_[i//2]
    card(s,x,y,DCW,DCH,fill=WHITE,line=GRAPH_B)
    tb,tf=textbox(s,x+Inches(0.24),y+Inches(0.15),DCW-Inches(0.48),DCH-Inches(0.3))
    p=para(tf,first=True); p.space_after=Pt(4)
    r=p.add_run(); _set(r,f"{i+1:02d}   ",11,BODY,SLATE,bold=True,track=1.0)
    r=p.add_run(); _set(r,verb.upper(),15,HEAD,DEEP_NAVY,track=1.0)
    line(tf,rest,12,color=GRAPHITE,ls=1.18,sa=0)
GYY=Inches(5.10)
card(s,LX,GYY,RW,Inches(1.06),fill=DEEP_NAVY,line=None)
tb,tf=textbox(s,LX+Inches(0.28),GYY+Inches(0.13),RW-Inches(0.56),Inches(0.85))
line(tf,"GOVERNING PRINCIPLE",9,color=WHITE_D,bold=True,first=True,track=1.2,sa=5)
line(tf,GOV,13,color=WHITE,ls=1.22,sa=0)
tb,tf=textbox(s,LX,Inches(6.40),RW,Inches(0.3))
line(tf,FOOT,8.5,color=SLATE,italic=True,first=True,sa=0)
furniture(s,5)

# ============ SLIDE 7 — BOARD DECISION (dark-field alternative) ============
# Composition 5: dark field, tonal cards, single gold marker
s=slide()
rect(s,0,0,SW,SH,fill=DEEP_NAVY)
rect(s,LX,Inches(0.53),Inches(0.11),Inches(0.11),fill=GOLD)
tb,tf=textbox(s,LX+Inches(0.24),Inches(0.48),Inches(9),Inches(0.28))
line(tf,"For decision — alternative treatment",10,color=WHITE,bold=True,first=True,track=1.6,caps=True,sa=0)
tb,tf=textbox(s,LX,Inches(0.82),Inches(12.0),Inches(0.95))
line(tf,"The Board is asked to endorse the two-pathway strategy and the basis on which "
        "capital is committed.",24,font=HEAD,color=WHITE,first=True,ls=1.05,sa=0)
for i,(verb,rest) in enumerate(DECS):
    x=GX[i%2]; y=GY_[i//2]
    card(s,x,y,DCW,DCH,fill=NAVY_CARD_L,line=NAVY_CARD_B,shadow=False)
    tb,tf=textbox(s,x+Inches(0.24),y+Inches(0.15),DCW-Inches(0.48),DCH-Inches(0.3))
    p=para(tf,first=True); p.space_after=Pt(4)
    r=p.add_run(); _set(r,f"{i+1:02d}   ",11,BODY,STEEL_LT,bold=True,track=1.0)
    r=p.add_run(); _set(r,verb.upper(),15,HEAD,WHITE,track=1.0)
    line(tf,rest,12,color=WHITE_D,ls=1.18,sa=0)
rect(s,LX,Inches(5.16),RW,Pt(1.5),fill=WHITE)
tb,tf=textbox(s,LX,Inches(5.30),RW,Inches(0.85))
line(tf,"GOVERNING PRINCIPLE",9,color=WHITE_D,bold=True,first=True,track=1.2,sa=5)
line(tf,GOV,13,color=WHITE,ls=1.22,sa=0)
tb,tf=textbox(s,LX,Inches(6.44),RW,Inches(0.3))
line(tf,FOOT,8.5,color=WHITE_D,italic=True,first=True,sa=0)
furniture(s,"5A",dark=True)

# ============ SLIDE 8 — PIPELINE ============
# Composition 6: three horizontal row cards with pathway markers and whisper tints
s=slide()
rect(s,0,0,SW,SH,fill=WHITE)
LX=Inches(0.7); RW=Inches(11.93)
kicker(s,LX,Inches(0.48),"Investment case · Current pipeline")
tb,tf=textbox(s,LX,Inches(0.80),Inches(11.9),Inches(0.6))
line(tf,"Current opportunities illustrate how the two pathways may develop in practice.",
     24,font=HEAD,color=NAVY,first=True,ls=1.02,sa=0)
R1=Inches(1.02); R2=Inches(4.32); R3=Inches(8.97)          # column x inside cards
R1W=Inches(3.05); R2W=Inches(4.35); R3W=Inches(3.45)
HY=Inches(1.70)
for x,w,h in [(R1,R1W,"Strategic role"),(R2,R2W,"Illustrative opportunities"),(R3,R3W,"Connection to the pathway")]:
    tb,tf=textbox(s,x,HY,w,Inches(0.3))
    line(tf,h.upper(),9.5,color=GRAPHITE,bold=True,first=True,track=1.1,sa=0)
prows=[
 ("Institutional-scale opportunity","PATHWAY 2",STEEL,STEEL_T,STEEL_B,
  "Marina One and other selected large opportunities.",
  "Potential to create a material increase in AUM, institutional relevance and market visibility."),
 ("Portfolio building block","PATHWAY 1",TEAL,TEAL_T,TEAL_B,
  "Project Guardian / PBSA and subsequent PBSA opportunities.",
  "Build a repeatable strategy through aggregation into a portfolio of institutional scale."),
 ("Track-record proof point","PATHWAY 1",TEAL,TEAL_T,TEAL_B,
  "Courtyard by Marriott Suwon, ARA-NH Fund 2, Aberdeen / Shinyoung recapitalisation and "
  "other relevant transactions.",
  "Deepen post-SMFL execution evidence and create additional realisation or recycling pathways."),
]
ry=Inches(2.10); rh=Inches(1.34); rgap=Inches(0.16)
for role,tag,acc,fillc,bord,opp,conn in prows:
    card(s,LX,ry,RW,rh,fill=fillc,line=bord)
    rect(s,LX,ry+Inches(0.18),Pt(3),rh-Inches(0.36),fill=acc)
    tb,tf=textbox(s,R1,ry+Inches(0.20),R1W,rh-Inches(0.4))
    line(tf,role,14,font=HEAD,color=NAVY,first=True,ls=1.05,sa=5)
    line(tf,tag,9.5,color=acc,bold=True,track=1.2,sa=0)
    tb,tf=textbox(s,R2,ry+Inches(0.22),R2W,rh-Inches(0.4))
    line(tf,opp,12.5,color=GRAPHITE,first=True,ls=1.22,sa=0)
    tb,tf=textbox(s,R3,ry+Inches(0.22),R3W,rh-Inches(0.4))
    line(tf,conn,12.5,color=GRAPHITE,first=True,ls=1.22,sa=0)
    ry+=rh+rgap
tb,tf=textbox(s,LX,ry+Inches(0.06),RW,Inches(0.55))
line(tf,"Private credit is excluded as a core Aravest growth strategy (an agreed SMDAM strategy, "
        "with Aravest providing support where relevant). Transaction names, figures and status to "
        "be refreshed by the relevant transaction teams before Board circulation.",
     9,color=SLATE,italic=True,first=True,ls=1.22,sa=0)
furniture(s,6)

prs.save("Aravest_Calibration_Set_v4.pptx")
print("saved Aravest_Calibration_Set_v4.pptx,",len(prs.slides._sldIdLst),"slides")
