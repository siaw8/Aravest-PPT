#!/usr/bin/env python3
"""Aravest Sample Deck — the Locked Board Strategy Narrative v8 rendered through
the design system's archetypes, sequenced to demonstrate the anti-repetition rules.
Content verbatim/near-verbatim from the locked narrative; no figures invented."""
from aravest_ds import *

prs=new_pres()
ENTITY="Aravest Fund Management Pte. Ltd.      Private and Confidential"
SUBTITLE=("From integration to institution-building: establishing the post-SMFL track record, "
          "defining the near-term investment focus and developing the pathways for sustainable "
          "long-term growth.")
pg=0
def np():
    global pg; pg+=1; return pg

# 1 · COVER (T01 — Board default)
s=add_slide(prs)
cover_B(s,"Aravest’s ","Next Phase",SUBTITLE,"Board Strategy Meeting  ·  September 2026",ENTITY)

# 2 · AGENDA (T05)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
title(s,Inches(1.0),Inches(0.72),"Agenda",size=30,w=Inches(6))
items=[("Purpose and development pathway","From integration to institution-building"),
       ("The Aravest Way","Values-led. Value-focused."),
       ("The post-SMFL track record","Two parallel pathways and warehousing"),
       ("Capital, AUM and current pipeline","Conrad Seoul illustration"),
       ("2027 investment focus and value creation","Playbooks and capability coverage"),
       ("Institutional standards and decisions","Structuring standard; matters for the Board")]
yy=Inches(1.95)
for i,(it,sub) in enumerate(items,1):
    hrule(s,Inches(1.0),yy,Inches(11.3),weight=0.75,color=MIST)
    tb,tf=textbox(s,Inches(1.0),yy+Inches(0.10),Inches(0.9),Inches(0.6))
    line(tf,f"{i:02d}",14,font=SERIF,color=SLATE,first=True,sa=0)
    tb,tf=textbox(s,Inches(1.9),yy+Inches(0.10),Inches(7.6),Inches(0.6))
    line(tf,it,15,font=HEAD,color=NAVY,first=True,sa=0)
    tb,tf=textbox(s,Inches(9.0),yy+Inches(0.14),Inches(3.3),Inches(0.6))
    line(tf,sub,11,color=GRAPHITE,first=True,sa=0)
    yy+=Inches(0.78)
furniture(s,np()+0 if False else (pg:=1) and 1)
# (page numbering starts at 1 on the agenda)

# 3 · PURPOSE — editorial statement (T04)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
s.shapes.add_picture(A+"/logo_navy.png",Inches(11.90),Inches(0.36),height=Inches(0.38))
kicker(s,Inches(1.6),Inches(1.75),"01 · Purpose")
tb,tf=textbox(s,Inches(1.6),Inches(2.25),Inches(10.1),Inches(1.9))
p=para(tf,first=True); p.line_spacing=1.16; p.space_after=Pt(0)
r=p.add_run(); set_run(r,"Aravest is moving from integration into ",30,SERIF,NAVY)
r=p.add_run(); set_run(r,"institution-building",30,SERIF,NAVY,italic=True)
r=p.add_run(); set_run(r,".",30,SERIF,NAVY)
rect(s,Inches(1.62),Inches(4.35),Pt(28),Pt(1.5),fill=GOLD)
tb,tf=textbox(s,Inches(1.6),Inches(4.6),Inches(10.0),Inches(1.2))
line(tf,"The initial integration into SMFL has been substantially completed. Aravest has maintained "
        "continuity across the platform, strengthened governance and begun building a visible record "
        "of execution under the new sponsor. The next phase is to develop the institutional foundations "
        "and investment record required for sustainable long-term growth.",
     13.5,color=GRAPHITE,first=True,ls=1.32,sa=0)
pg=2; furniture(s,pg)

# 4 · DEVELOPMENT PATHWAY — timeline (T15)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
LX=Inches(0.7); RW=Inches(11.93)
kicker(s,LX,Inches(0.48),"02 · Development pathway")
title(s,LX,Inches(0.80),"The proof-building process has begun and becomes the principal focus from 2027 to 2029.")
phases=[("2025","Integrate and begin proving",
         "Complete the initial integration, maintain platform continuity and begin demonstrating execution under SMFL ownership."),
        ("2026","Establish institutional identity",
         "Introduce The Aravest Way, deepen governance and investment discipline, and continue building visible post-SMFL evidence."),
        ("2027–2029","Build and compound the record",
         "Execute selected opportunities, demonstrate outcomes, establish repeatable strategies and deepen investor relationships."),
        ("Around 2030 onward","Convert proof into scale",
         "Use the accumulated track record to pursue larger and increasingly repeatable institutional capital.")]
n=len(phases); cw=Inches(2.80); gap=(RW-cw*n)/(n-1); cy=Inches(2.15); ch=Inches(3.15)
for i,(yr,h,b) in enumerate(phases):
    x=LX+i*(cw+gap)
    emph = (i==2)
    card(s,x,cy,cw,ch,fill=(TEAL_T if emph else WHITE),line=(TEAL_B if emph else GRAPH_B))
    rect(s,x+Inches(0.2),cy,cw-Inches(0.4),Pt(2.5),fill=(TEAL if emph else GRAPH_B))
    tb,tf=textbox(s,x+Inches(0.2),cy+Inches(0.16),cw-Inches(0.4),ch-Inches(0.32))
    line(tf,yr.upper(),9.5,color=(TEAL if emph else GRAPHITE),bold=True,first=True,track=1.0,sa=5)
    line(tf,h,14.5,font=HEAD,color=NAVY,sa=6,ls=1.05)
    line(tf,b,13,color=GRAPHITE,ls=1.24,sa=0)
    if i<n-1:
        tb,tf=textbox(s,x+cw,cy+Inches(1.2),gap,Inches(0.4),anchor=MSO_ANCHOR.MIDDLE)
        line(tf,"→",15,color=GRAPHITE,align=PP_ALIGN.CENTER,first=True,sa=0)
conclusion_band(s,LX,Inches(5.72),RW,"Around 2030","is a realistic point at which broader institutional "
                "capital may become more achievable, subject to execution and market conditions.")
pg+=1; furniture(s,pg)

# 5 · DIVIDER (T03)
s=add_slide(prs)
divider_typographic(s,"01","The Aravest Way",
                    "The institutional foundation for how Aravest conducts its business and invests.")

# 6 · THE ARAVEST WAY — three pillars (T06 1×3 variant)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
LX=Inches(1.0); CW=Inches(11.33)
title(s,LX,Inches(0.66),"The Aravest Way provides the foundation for how Aravest conducts its business and invests.",size=24,w=CW)
tb,tf=textbox(s,LX,Inches(1.58),Inches(11.0),Inches(0.5))
line(tf,"Our values are equal and inseparable. Strategies will evolve and markets will change; "
        "the values should remain constant.",13.5,color=GRAPHITE,first=True,ls=1.26,sa=0)
vals=[("EXCELLENCE","The quality of our thinking",
       "Excellence guides how Aravest analyses, prepares, executes, communicates and continuously raises its standards."),
      ("TRUST","The way we behave",
       "Trust guides how Aravest deals with investors, shareholders, partners, lenders and colleagues, particularly when circumstances are difficult."),
      ("ACCOUNTABILITY","How we take ownership",
       "Accountability requires Aravest to own its decisions and outcomes, act when circumstances change and remain responsible through the full investment lifecycle.")]
cy=Inches(2.35); ch=Inches(2.75); cw=Inches(3.67); gap=Inches(0.16)
for i,(tag_,h,b) in enumerate(vals):
    x=LX+i*(cw+gap)
    card(s,x,cy,cw,ch,fill=WHITE,line=GRAPH_B)
    tb,tf=textbox(s,x+Inches(0.24),cy+Inches(0.20),cw-Inches(0.48),ch-Inches(0.4))
    line(tf,tag_,9.5,color=GRAPHITE,bold=True,first=True,track=1.3,sa=6)
    line(tf,h,15,font=HEAD,color=NAVY,sa=7,ls=1.05)
    line(tf,b,13,color=GRAPHITE,ls=1.26,sa=0)
conclusion_band(s,LX,Inches(5.40),CW,"Our first principle.",
                "Investment management is a responsibility before it is a business.",h=Inches(0.62))
tb,tf=textbox(s,LX,Inches(6.25),CW,Inches(0.5))
line(tf,"Every investment, partnership and decision is tested against the responsibility Aravest "
        "accepts when capital and trust are entrusted to the platform.",11.5,color=GRAPHITE,
        first=True,ls=1.2,sa=0)
pg+=1; furniture(s,pg)

# 7 · VALUES-LED / VALUE-FOCUSED — twin cards (T07)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
LX=Inches(0.7); RW=Inches(11.93)
kicker(s,LX,Inches(0.48),"04 · Values-led. Value-focused.")
title(s,LX,Inches(0.80),"The Aravest Way defines how we invest; value creation determines where we deploy.")
CY=Inches(1.70); CH=Inches(4.30); CWD=Inches(5.80); X2=Inches(6.83)
panels=[
 (LX,"Values-led","The standards remain constant",TEAL,TEAL_T,TEAL_B,
  ["Excellence: disciplined thinking, underwriting and execution.",
   "Trust: alignment, transparency and institutional governance.",
   "Accountability: ownership of decisions, risks and investment outcomes."]),
 (X2,"Value-focused","Deployment follows identifiable value",STEEL,STEEL_T,STEEL_B,
  ["A genuine value gap, mispricing or market dislocation.",
   "A clear and executable value-creation plan.",
   "Complete capabilities, internally or through secured partners.",
   "A credible route to stabilisation, capital recycling or exit."]),
]
for X,tag_,h,acc,fillc,bord,points in panels:
    card(s,X,CY,CWD,CH,fill=fillc,line=bord)
    rect(s,X+Inches(0.22),CY,CWD-Inches(0.44),Pt(2.5),fill=acc)
    tb,tf=textbox(s,X+Inches(0.26),CY+Inches(0.18),CWD-Inches(0.52),CH-Inches(0.36))
    line(tf,tag_.upper(),9.5,color=acc,bold=True,first=True,track=1.2,sa=4)
    line(tf,h,15,font=HEAD,color=NAVY,sa=8,ls=1.04)
    for pt_ in points:
        line(tf,pt_,13,color=GRAPHITE,ls=1.24,sa=7)
card(s,LX,Inches(6.14),RW,Inches(0.58),fill=DEEP_NAVY,line=None)
tb,tf=textbox(s,LX+Inches(0.28),Inches(6.14),RW-Inches(0.56),Inches(0.58),anchor=MSO_ANCHOR.MIDDLE)
p=para(tf,first=True); p.space_after=Pt(0)
r=p.add_run(); set_run(r,"Sector-flexible, but not strategy-neutral.  ",13,HEAD,WHITE)
r=p.add_run(); set_run(r,"Every investment must have an identifiable value opportunity, a credible "
                        "plan and the capabilities to execute it.",12.5,BODY,WHITE_D)
pg+=1; furniture(s,pg)

# 8 · TRACK RECORD — process (T15)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"05 · Building the post-SMFL track record")
title(s,LX,Inches(0.80),"A credible track record is built through the full investment lifecycle, not through acquisitions alone.")
steps=["Recognise and underwrite value","Secure and execute","Manage and create value",
       "Deliver and realise outcomes","Repeat across a strategy"]
n=len(steps); sw=Inches(2.12); gap=(RW-sw*n)/(n-1); sy=Inches(2.30)
for i,st in enumerate(steps):
    x=LX+i*(sw+gap)
    emph=(i==n-1)
    card(s,x,sy,sw,Inches(1.42),fill=(TEAL_T if emph else WHITE),line=(TEAL_B if emph else GRAPH_B))
    tb,tf=textbox(s,x+Inches(0.16),sy+Inches(0.15),sw-Inches(0.32),Inches(1.15))
    line(tf,f"{i+1:02d}",10.5,color=(TEAL if emph else SLATE),bold=True,first=True,track=1.2,sa=4)
    line(tf,st,13,font=HEAD,color=NAVY,ls=1.08,sa=0)
    if i<n-1:
        tb,tf=textbox(s,x+sw,sy+Inches(0.5),gap,Inches(0.4),anchor=MSO_ANCHOR.MIDDLE)
        line(tf,"→",15,color=GRAPHITE,align=PP_ALIGN.CENTER,first=True,sa=0)
tb,tf=textbox(s,LX,Inches(4.05),RW,Inches(0.75))
line(tf,"Investors will first seek evidence that Aravest can source, execute, manage and complete "
        "investments successfully under SMFL ownership — judgement, execution, stewardship, "
        "performance, realisation and repeatability.",13.5,color=GRAPHITE,first=True,ls=1.3,sa=0)
conclusion_band(s,LX,Inches(5.05),RW,"The objective:",
                "move investor confidence from the individual opportunity, to the repeat relationship, "
                "and ultimately to the Aravest strategy.")
tb,tf=textbox(s,LX,Inches(5.95),RW,Inches(0.5))
line(tf,"At Aravest's current stage, third-party capital is likely to be opportunity-led before it "
        "becomes strategy-led or discretionary.",11.5,color=GRAPHITE,italic=False,first=True,ls=1.2,sa=0)
pg+=1; furniture(s,pg)

# 9 · DIVIDER
s=add_slide(prs)
divider_typographic(s,"02","Two parallel pathways",
                    "The principal programme for the record, and the possibility of acceleration — case by case.")

# 10 · TWO PATHWAYS — twin cards (T07, from V4 approved)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"06 · Strategy")
title(s,LX,Inches(0.80),"Aravest will build the platform through two complementary pathways.")
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
CY=Inches(1.54); CH=Inches(4.42); CWD=Inches(5.80); X2=Inches(6.83)
off=[Inches(1.06),Inches(1.78),Inches(2.50),Inches(3.22),Inches(3.90)]
for X,name,role,acc,fillc,bord in [
    (LX,"Pathway 1 — Diversified Track Record Building","Builds the record",TEAL,TEAL_T,TEAL_B),
    (X2,"Pathway 2 — Institutional-Scale Opportunities","Can accelerate scale",STEEL,STEEL_T,STEEL_B)]:
    card(s,X,CY,CWD,CH,fill=fillc,line=bord)
    rect(s,X+Inches(0.22),CY,CWD-Inches(0.44),Pt(2.5),fill=acc)
    tb,tf=textbox(s,X+Inches(0.26),CY+Inches(0.16),CWD-Inches(0.52),Inches(0.85))
    line(tf,name,15,font=HEAD,color=NAVY,first=True,ls=1.04,sa=3)
    line(tf,role.upper(),9.5,color=acc,bold=True,track=1.2,sa=0)
    vals=[r[1] if X==LX else r[2] for r in prow]
    for o,(lab,v) in zip(off,[(r[0],v) for r,v in zip(prow,vals)]):
        tb,tf=textbox(s,X+Inches(0.26),CY+o,CWD-Inches(0.52),Inches(0.70))
        line(tf,lab.upper(),9,color=GRAPHITE,bold=True,first=True,track=0.8,sa=2)
        line(tf,v,13,color=GRAPHITE,ls=1.14,sa=0)
card(s,LX,Inches(6.14),RW,Inches(0.58),fill=DEEP_NAVY,line=None)
tb,tf=textbox(s,LX+Inches(0.28),Inches(6.14),RW-Inches(0.56),Inches(0.58),anchor=MSO_ANCHOR.MIDDLE)
p=para(tf,first=True); p.space_after=Pt(0)
r=p.add_run(); set_run(r,"RUN IN PARALLEL   ",10,BODY,WHITE_D,bold=True,track=1.4)
r=p.add_run(); set_run(r,"Pathway 1 builds the record",13,BODY,TEAL_LT,bold=True)
r=p.add_run(); set_run(r,";  ",13,BODY,WHITE_D)
r=p.add_run(); set_run(r,"Pathway 2 can accelerate scale",13,BODY,STEEL_LT,bold=True)
r=p.add_run(); set_run(r,".",13,BODY,WHITE_D)
pg+=1; furniture(s,pg)

# 11 · RECYCLING ROUTES — institutional table (T11, markers)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"07 · Pathway 1 · Capital recycling")
title(s,LX,Inches(0.80),"Two routes to capital recycling: asset-level speed, or portfolio-level institutional scale.")
HY=Inches(1.70)
tcols=[(Inches(1.02),Inches(2.35),""),(Inches(3.55),Inches(4.35),"Asset-level recycling"),
       (Inches(8.15),Inches(4.35),"Portfolio-level recycling through aggregation")]
for x,w,h in tcols[1:]:
    tb,tf=textbox(s,x,HY,w,Inches(0.3))
    line(tf,h.upper(),9.5,color=GRAPHITE,bold=True,first=True,track=0.9,sa=0)
rect(s,LX,HY+Inches(0.34),RW,Pt(1.5),fill=NAVY)
trows=[("Approach","Sell, recapitalise or introduce third-party capital into an individual asset.",
        "Combine related assets into a coherent portfolio before introducing third-party capital."),
       ("Timing","Potentially earlier where there is sufficient demand for the individual asset.",
        "Usually requires more time to assemble sufficient scale."),
       ("Investor relevance","The individual ticket may be too small for larger institutions.",
        "The portfolio can provide a more meaningful ticket and greater diversification."),
       ("Strategic benefit","Releases capital earlier and creates a realised proof point.",
        "Creates a scalable strategy or platform, rather than a single investment."),
       ("AUM implication","A full disposal may reduce AUM; a partial sell-down may retain it.",
        "Can create larger and more durable portfolio-level AUM.")]
ry=HY+Inches(0.44)
for i,(lab,v1,v2) in enumerate(trows):
    if i>0: hrule(s,LX,ry,RW,weight=0.75,color=MIST)
    pathway_marker(s,LX,ry+Inches(0.12),Inches(0.55),TEAL)
    tb,tf=textbox(s,Inches(1.02),ry+Inches(0.12),Inches(2.35),Inches(0.7))
    line(tf,lab.upper(),9.5,color=GRAPHITE,bold=True,first=True,track=0.8,ls=1.1,sa=0)
    for (x,w,_),v in zip(tcols[1:],[v1,v2]):
        tb,tf=textbox(s,x,ry+Inches(0.10),w,Inches(0.75))
        line(tf,v,12,color=GRAPHITE,first=True,ls=1.16,sa=0)
    ry+=Inches(0.80)
rect(s,LX,ry,RW,Pt(1.0),fill=NAVY)
tb,tf=textbox(s,LX,ry+Inches(0.10),RW,Inches(0.45))
line(tf,"Capital recycling remains important because sponsor capital is finite; the immediate priority "
        "is the investment record from which longer-term capital efficiency can develop.",
     11.5,color=GRAPHITE,first=True,ls=1.2,sa=0)
pg+=1; furniture(s,pg)

# 12 · WAREHOUSING — cause/effect twin cards + quote band (T07 variant)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"09 · Warehousing as an execution enabler")
title(s,LX,Inches(0.80),"Warehousing bridges the timing gap between securing a transaction and forming third-party capital.")
CY=Inches(1.78); CH=Inches(2.30); CWD=Inches(5.80); X2=Inches(6.83)
for X,tag_,h,b,fillc,bord,acc in [
    (LX,"WITHOUT WAREHOUSING","The record cannot form",
     "Limited advance third-party commitments → fewer secured transactions → insufficient post-SMFL "
     "proof → continued difficulty attracting third-party capital.",WHITE,GRAPH_B,GRAPHITE),
    (X2,"WITH WAREHOUSING","Execution builds the record",
     "Secure and execute transactions → demonstrate the full investment lifecycle → establish investor "
     "confidence → introduce or raise third-party capital → repeat.",TEAL_T,TEAL_B,TEAL)]:
    card(s,X,CY,CWD,CH,fill=fillc,line=bord)
    rect(s,X+Inches(0.22),CY,CWD-Inches(0.44),Pt(2.5),fill=acc)
    tb,tf=textbox(s,X+Inches(0.26),CY+Inches(0.18),CWD-Inches(0.52),CH-Inches(0.36))
    line(tf,tag_,9.5,color=(acc if acc!=GRAPHITE else GRAPHITE),bold=True,first=True,track=1.2,sa=4)
    line(tf,h,15,font=HEAD,color=NAVY,sa=7,ls=1.04)
    line(tf,b,13,color=GRAPHITE,ls=1.28,sa=0)
tb,tf=textbox(s,LX,Inches(4.38),RW,Inches(0.85))
line(tf,"Institutional investors generally require a specific and sufficiently secured opportunity, "
        "while sellers require certainty and speed — the two timetables often do not align. Without "
        "the ability to bridge this gap, Aravest may be unable to secure opportunities at the point "
        "they are available.",13.5,color=GRAPHITE,first=True,ls=1.3,sa=0)
conclusion_band(s,LX,Inches(5.55),RW,"The chain:",
                "warehousing enables execution; execution builds the track record; the track record "
                "supports long-term third-party capital formation.")
pg+=1; furniture(s,pg)

# 13 · AUM DASHBOARD (T08, from V4 approved)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"10 · Capital & AUM")
title(s,LX,Inches(0.80),"The two pathways are expected to produce different AUM profiles.")
hrule(s,LX,Inches(1.56),RW,weight=0.75,color=MIST)
tb,tf=textbox(s,LX,Inches(1.68),RW,Inches(0.40),anchor=MSO_ANCHOR.MIDDLE)
line(tf,"Closing AUM  =  Opening AUM  +  New investments  −  Realisations  ±  Valuation and FX movements",
     14.5,font=HEAD,color=NAVY,align=PP_ALIGN.CENTER,first=True,sa=0)
hrule(s,LX,Inches(2.20),RW,weight=0.75,color=MIST)
AY=Inches(2.44); AH=Inches(3.42)
card(s,LX,AY,Inches(3.05),AH,fill=DEEP_NAVY,line=None)
tb,tf=textbox(s,LX+Inches(0.26),AY+Inches(0.22),Inches(2.55),AH-Inches(0.44))
line(tf,"SPONSOR CAPITAL SUPPORT",9,color=WHITE_D,bold=True,first=True,track=1.0,sa=8)
line(tf,"US$300m",34,font=HEAD,color=WHITE,sa=9,ls=1.0)
line(tf,"Existing support, diversified across several Pathway 1 investments.",13,color=WHITE_D,ls=1.26,sa=6)
line(tf,"Warehousing bridges execution and third-party capital formation.",13,color=WHITE_D,ls=1.26,sa=0)
def profile_card(x,w,title_,titlec,heights,lo,step_idx=None,hi=None,caption=""):
    card(s,x,AY,w,AH,fill=WHITE,line=GRAPH_B)
    tb,tf=textbox(s,x+Inches(0.24),AY+Inches(0.18),w-Inches(0.48),Inches(0.5))
    line(tf,title_,13.5,font=HEAD,color=titlec,first=True,ls=1.03,sa=0)
    bars(s,x+Inches(0.24),AY+Inches(2.02),w-Inches(0.48),heights,lo,fill_hi=hi,step_idx=step_idx)
    tb,tf=textbox(s,x+Inches(0.24),AY+Inches(2.14),w-Inches(0.48),Inches(1.15))
    line(tf,caption,13,color=GRAPHITE,first=True,ls=1.18,sa=3)
    line(tf,"Illustrative profile only — not a forecast.",9,color=SLATE,italic=True,sa=0)
profile_card(Inches(3.95),Inches(4.28),"Pathway 1 — gradual and uneven",TEAL,
             [0.42,0.55,0.47,0.62,0.52,0.70,0.63],TEAL,
             caption="AUM may grow gradually, remain flat where investments replace realisations, "
                     "or decline temporarily after disposals or sell-downs.")
profile_card(Inches(8.43),Inches(4.20),"Pathway 2 — potential step-change",STEEL,
             [0.36,0.38,0.40,0.93,0.95,1.0,1.0],STEEL_MID,step_idx=3,hi=STEEL,
             caption="A single institutional-scale transaction can create a material or step-change "
                     "increase in AUM and more meaningful ticket sizes.")
card(s,LX,Inches(6.06),RW,Inches(0.56),fill=GRAPH_T,line=GRAPH_B,shadow=False)
tb,tf=textbox(s,LX+Inches(0.26),Inches(6.06),RW-Inches(0.52),Inches(0.56),anchor=MSO_ANCHOR.MIDDLE)
p=para(tf,first=True); p.space_after=Pt(0); p.line_spacing=1.12
r=p.add_run(); set_run(r,"BASIS   ",9.5,BODY,NAVY,bold=True,track=1.0)
r=p.add_run(); set_run(r,"Financial figures to be populated by Finance and refreshed by transaction "
                        "teams before Board circulation. Source: Locked Board Strategy Narrative v8.",
               12,BODY,GRAPHITE)
pg+=1; furniture(s,pg)

# 14 · CONRAD SEOUL — case study (T16)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"11 · Conrad Seoul illustration")
title(s,LX,Inches(0.80),"Conrad Seoul illustrates the sequencing of warehousing, execution and institutional capital formation.")
s.shapes.add_picture(A+"/hero_seoul.jpg",LX,Inches(1.78),width=Inches(4.4),height=Inches(3.87))
rect(s,LX,Inches(1.78),Inches(4.4),Inches(3.87),fill=None,line=MIST,line_w=Pt(0.75))
RX=Inches(5.45); RWd=Inches(7.18)
tb,tf=textbox(s,RX,Inches(1.80),RWd,Inches(3.4))
line(tf,"THE SEQUENCE",9.5,color=GRAPHITE,bold=True,first=True,track=1.2,sa=7)
for i,step in enumerate(["Sponsor-supported capital enabled the transaction to be secured and completed.",
                         "Execution became visible and established confidence in the platform.",
                         "Institutional investors — including GIC and M&G — were subsequently introduced.",
                         "Capital was recycled while Aravest retained the management relationship and "
                         "strengthened its post-SMFL record."],1):
    p=para(tf); p.space_after=Pt(8); p.line_spacing=1.22
    r=p.add_run(); set_run(r,f"{i:02d}  ",11,BODY,TEAL,bold=True,track=1.0)
    r=p.add_run(); set_run(r,step,13.5,BODY,GRAPHITE)
card(s,RX,Inches(5.02),RWd,Inches(1.02),fill=GRAPH_T,line=GRAPH_B,shadow=False)
tb,tf=textbox(s,RX+Inches(0.24),Inches(5.02),RWd-Inches(0.48),Inches(1.02),anchor=MSO_ANCHOR.MIDDLE)
line(tf,"HOW THE EXAMPLE SHOULD BE UNDERSTOOD",9,color=NAVY,bold=True,first=True,track=1.0,sa=4)
line(tf,"The sequence demonstrates an available model, not an assured timetable; the sponsor may need "
        "to retain the investment for longer if external capital takes time to form.",
     12.5,color=GRAPHITE,ls=1.2,sa=0)
pg+=1; furniture(s,pg)

# 15 · PIPELINE — row cards (T12, from V4 approved)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"12 · Investment case · Current pipeline")
title(s,LX,Inches(0.80),"Current opportunities illustrate how the two pathways may develop in practice.")
R1,R1W=Inches(1.02),Inches(3.05); R2,R2W=Inches(4.32),Inches(4.35); R3,R3W=Inches(8.97),Inches(3.45)
HY=Inches(1.70)
for x,w,h in [(R1,R1W,"Strategic role"),(R2,R2W,"Illustrative opportunities"),(R3,R3W,"Connection to the pathway")]:
    tb,tf=textbox(s,x,HY,w,Inches(0.3))
    line(tf,h.upper(),9.5,color=GRAPHITE,bold=True,first=True,track=1.1,sa=0)
prows=[("Institutional-scale opportunity","PATHWAY 2",STEEL,STEEL_T,STEEL_B,
        "Marina One and other selected large opportunities.",
        "Potential to create a material increase in AUM, institutional relevance and market visibility."),
       ("Portfolio building block","PATHWAY 1",TEAL,TEAL_T,TEAL_B,
        "Project Guardian / PBSA and subsequent PBSA opportunities.",
        "Build a repeatable strategy through aggregation into a portfolio of institutional scale."),
       ("Track-record proof point","PATHWAY 1",TEAL,TEAL_T,TEAL_B,
        "Courtyard by Marriott Suwon, ARA-NH Fund 2, Aberdeen / Shinyoung recapitalisation and "
        "other relevant transactions.",
        "Deepen post-SMFL execution evidence and create additional realisation or recycling pathways.")]
ry=Inches(2.10); rh=Inches(1.34)
for role,tag_,acc,fillc,bord,opp,conn in prows:
    card(s,LX,ry,RW,rh,fill=fillc,line=bord)
    rect(s,LX,ry+Inches(0.18),Pt(3),rh-Inches(0.36),fill=acc)
    tb,tf=textbox(s,R1,ry+Inches(0.20),R1W,rh-Inches(0.4))
    line(tf,role,14,font=HEAD,color=NAVY,first=True,ls=1.05,sa=5)
    line(tf,tag_,9.5,color=acc,bold=True,track=1.2,sa=0)
    tb,tf=textbox(s,R2,ry+Inches(0.22),R2W,rh-Inches(0.4))
    line(tf,opp,13,color=GRAPHITE,first=True,ls=1.2,sa=0)
    tb,tf=textbox(s,R3,ry+Inches(0.22),R3W,rh-Inches(0.4))
    line(tf,conn,13,color=GRAPHITE,first=True,ls=1.2,sa=0)
    ry+=rh+Inches(0.16)
tb,tf=textbox(s,LX,ry+Inches(0.04),RW,Inches(0.55))
line(tf,"Private credit is excluded as a core Aravest growth strategy (an agreed SMDAM strategy, with "
        "Aravest providing support where relevant). Transaction names, figures and status to be "
        "refreshed by the relevant transaction teams before Board circulation.",
     9,color=SLATE,italic=True,first=True,ls=1.22,sa=0)
pg+=1; furniture(s,pg)

# 16 · DIVIDER
s=add_slide(prs)
divider_typographic(s,"03","2027 focus and value creation",
                    "Where we will look, and why we would invest.")

# 17 · 2027 FOCUS — three horizontal band cards (T12 variant)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"13 · 2027 investment focus")
title(s,LX,Inches(0.80),"Near-term focus combines established capabilities with selected areas of current market opportunity.")
B1,B1W=Inches(1.02),Inches(3.3); B2,B2W=Inches(4.6),Inches(3.6); B3,B3W=Inches(8.5),Inches(3.9)
HY=Inches(1.66)
for x,w,h in [(B1,B1W,"Focus"),(B2,B2W,"2027 strategic role"),(B3,B3W,"How we will approach them")]:
    tb,tf=textbox(s,x,HY,w,Inches(0.3))
    line(tf,h.upper(),9.5,color=GRAPHITE,bold=True,first=True,track=1.1,sa=0)
bands=[("Established sectors","Office, logistics and selective retail or mixed-use",None,WHITE,GRAPH_B,
        "Remain the principal investment base, supported by existing experience, local market knowledge "
        "and asset-management capabilities.",
        "Prioritise opportunities where repositioning, lease-up, AEI, redevelopment or market dislocation "
        "can create a clear and defensible value proposition."),
       ("Current target priorities","Hospitality and living",TEAL,TEAL_T,TEAL_B,
        "Focus origination and capability development where current demand, market conditions and "
        "developing experience provide attractive opportunities.",
        "Pursue repeatable strategies with strong operating partners, clear demand drivers and a credible "
        "path from individual opportunities to institutional portfolios."),
       ("Opportunistic adjacencies","Data centres and other emerging real asset sectors",None,WHITE,GRAPH_B,
        "Consider selectively rather than as a standing capital allocation or broad commitment to build "
        "every capability internally.",
        "Proceed only where there is differentiated access, a compelling value thesis and the required "
        "technical, development and operating capabilities have been secured.")]
ry=Inches(2.04); rh=Inches(1.34)
for lab,h,acc,fillc,bord,role,how in bands:
    card(s,LX,ry,RW,rh,fill=fillc,line=bord)
    if acc: rect(s,LX,ry+Inches(0.18),Pt(3),rh-Inches(0.36),fill=acc)
    tb,tf=textbox(s,B1,ry+Inches(0.16),B1W,rh-Inches(0.32))
    line(tf,lab.upper(),9,color=(acc or GRAPHITE),bold=True,first=True,track=0.9,sa=3)
    line(tf,h,13.5,font=HEAD,color=NAVY,ls=1.06,sa=0)
    tb,tf=textbox(s,B2,ry+Inches(0.16),B2W,rh-Inches(0.32))
    line(tf,role,12,color=GRAPHITE,first=True,ls=1.18,sa=0)
    tb,tf=textbox(s,B3,ry+Inches(0.16),B3W,rh-Inches(0.32))
    line(tf,how,12,color=GRAPHITE,first=True,ls=1.18,sa=0)
    ry+=rh+Inches(0.14)
tb,tf=textbox(s,LX,ry+Inches(0.03),RW,Inches(0.5))
line(tf,"These priorities guide origination and capability development for 2027. They are not fixed "
        "capital allocations and may evolve with market conditions, investor demand and demonstrated "
        "investment outcomes.",11,color=GRAPHITE,italic=False,first=True,ls=1.2,sa=0)
pg+=1; furniture(s,pg)

# 18 · VALUE-CREATION PLAYBOOKS — table + principle (T11 variant)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"14 · How Aravest creates value")
title(s,LX,Inches(0.80),"Sector selection identifies where we invest; the value-creation plan determines why.")
HY=Inches(1.80)
for x,w,h in [(Inches(1.02),Inches(3.6),"Value-creation playbook"),(Inches(5.0),Inches(7.6),"Typical application")]:
    tb,tf=textbox(s,x,HY,w,Inches(0.3))
    line(tf,h.upper(),9.5,color=GRAPHITE,bold=True,first=True,track=1.1,sa=0)
rect(s,LX,HY+Inches(0.30),RW,Pt(1.5),fill=NAVY)
plays=[("Repositioning and lease-up","Improve occupancy, tenant mix, rental performance and market positioning."),
       ("Asset enhancement and conversion","Undertake refurbishment, AEI, change of use or physical repositioning."),
       ("Development and redevelopment","Create value through ground-up development or material redevelopment where the capability and risk controls are established."),
       ("Operational improvement","Improve performance through stronger management, branding, service delivery or specialist operating partners."),
       ("Market or capital dislocation","Invest where pricing, ownership constraints, refinancing pressure or capital scarcity create an attractive entry point."),
       ("Aggregation and portfolio formation","Combine related investments into portfolios or repeatable strategies capable of attracting institutional capital.")]
ry=HY+Inches(0.40)
for i,(k,v) in enumerate(plays):
    if i>0: hrule(s,LX,ry,RW,weight=0.75,color=MIST)
    tb,tf=textbox(s,Inches(1.02),ry+Inches(0.08),Inches(3.6),Inches(0.55))
    line(tf,k,12.5,font=HEAD,color=NAVY,first=True,ls=1.08,sa=0)
    tb,tf=textbox(s,Inches(5.0),ry+Inches(0.09),Inches(7.6),Inches(0.55))
    line(tf,v,12,color=GRAPHITE,first=True,ls=1.15,sa=0)
    ry+=Inches(0.565)
rect(s,LX,ry,RW,Pt(1.0),fill=NAVY)
GYY=ry+Inches(0.14)
card(s,LX,GYY,RW,Inches(0.94),fill=DEEP_NAVY,line=None)
tb,tf=textbox(s,LX+Inches(0.28),GYY+Inches(0.11),RW-Inches(0.56),Inches(0.75))
line(tf,"CAPABILITY COVERAGE IS AN INVESTMENT GATE",9,color=WHITE_D,bold=True,first=True,track=1.2,sa=4)
line(tf,"Aravest will proceed only where all capabilities required for origination, underwriting, financing, "
        "development, operations, asset management and realisation are covered internally or through secured partners.",
     12,color=WHITE,ls=1.2,sa=0)
pg+=1; furniture(s,pg)

# 19 · STRUCTURING STANDARD — process + principle (T15 variant)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"15 · Institutional structuring standard")
title(s,LX,Inches(0.80),"Every fund and investment must be structured to standards acceptable to institutional investors.")
nodes=["Institutional investors and approved co-investors","Fund vehicle","Investment SPV / borrower","Underlying asset"]
n=len(nodes); nw=Inches(2.62); gap=(RW-nw*n)/(n-1); nyy=Inches(1.95)
for i,nd in enumerate(nodes):
    x=LX+i*(nw+gap)
    card(s,x,nyy,nw,Inches(1.02),fill=WHITE,line=GRAPH_B)
    tb,tf=textbox(s,x+Inches(0.14),nyy,nw-Inches(0.28),Inches(1.02),anchor=MSO_ANCHOR.MIDDLE)
    line(tf,nd,12.5,font=HEAD,color=NAVY,align=PP_ALIGN.CENTER,first=True,ls=1.1,sa=0)
    if i<n-1:
        tb,tf=textbox(s,x+nw,nyy+Inches(0.3),gap,Inches(0.4),anchor=MSO_ANCHOR.MIDDLE)
        line(tf,"→",15,color=GRAPHITE,align=PP_ALIGN.CENTER,first=True,sa=0)
card(s,LX,Inches(3.30),RW,Inches(0.86),fill=GRAPH_T,line=GRAPH_B,shadow=False)
tb,tf=textbox(s,LX+Inches(0.26),Inches(3.30),RW-Inches(0.52),Inches(0.86),anchor=MSO_ANCHOR.MIDDLE)
line(tf,"RISK AND LIABILITIES ARE GENERALLY RING-FENCED",9,color=NAVY,bold=True,first=True,track=1.0,sa=4)
line(tf,"Risk and liabilities are generally contained within the relevant fund and asset-level structure; "
        "financing should generally have recourse only to the relevant borrower, secured assets and "
        "expressly agreed credit support.",12.5,color=GRAPHITE,ls=1.2,sa=0)
tris=["Committed capital is exposed to investment performance",
      "Wider fund and asset liabilities are ring-fenced",
      "Manager or shareholder recourse is not automatic"]
tw_=Inches(3.85); tgap=(RW-tw_*3)/2; tyy=Inches(4.42)
for i,t in enumerate(tris):
    x=LX+i*(tw_+tgap)
    card(s,x,tyy,tw_,Inches(0.86),fill=DEEP_NAVY,line=None,shadow=False)
    tb,tf=textbox(s,x+Inches(0.2),tyy,tw_-Inches(0.4),Inches(0.86),anchor=MSO_ANCHOR.MIDDLE)
    line(tf,t,12.5,color=WHITE,align=PP_ALIGN.CENTER,first=True,ls=1.15,sa=0)
tb,tf=textbox(s,LX,Inches(5.52),RW,Inches(0.85))
p=para(tf,first=True); p.line_spacing=1.24; p.space_after=Pt(0)
r=p.add_run(); set_run(r,"Exceptions must be explicit and separately approved.  ",12.5,BODY,NAVY,bold=True)
r=p.add_run(); set_run(r,"Any guarantee, keepwell, completion support, cost-overrun undertaking, indemnity "
                        "or other manager- or shareholder-level obligation must be specifically identified, "
                        "assessed, quantified and expressly approved through the applicable governance process.",
               12.5,BODY,GRAPHITE)
pg+=1; furniture(s,pg)

# 20 · BOARD DECISION — light default (T13, from V4 approved)
DECS=[("Endorse","the two parallel pathways as the basis for building the Aravest platform — "
       "diversified track-record building alongside selective institutional-scale opportunities."),
      ("Support","deployment of the existing US$300 million across Pathway 1 to build multiple "
       "proof points and diversify risk."),
      ("Endorse","warehousing as an execution enabler, bridging the timing gap between securing "
       "a transaction and forming third-party capital."),
      ("Agree","that each Institutional-Scale Opportunity is brought to the Board separately — with its "
       "investment merits, capital requirement and risk profile — for decision case-by-case.")]
GOV=("Committed equity is exposed to investment performance; wider fund and asset liabilities "
     "are generally ring-fenced, with no automatic recourse to Aravest as manager or SMFL as "
     "shareholder. Any exception must be explicit and separately approved.")
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
decision_kicker(s,LX,Inches(0.48))
title(s,LX,Inches(0.82),"The Board is asked to endorse the two-pathway strategy and the basis on which capital is committed.")
DCW=Inches(5.86); DCH=Inches(1.34); GX=[LX,Inches(6.77)]; GY_=[Inches(2.02),Inches(3.52)]
for i,(verb,rest) in enumerate(DECS):
    x=GX[i%2]; y=GY_[i//2]
    card(s,x,y,DCW,DCH,fill=WHITE,line=GRAPH_B)
    tb,tf=textbox(s,x+Inches(0.24),y+Inches(0.15),DCW-Inches(0.48),DCH-Inches(0.3))
    p=para(tf,first=True); p.space_after=Pt(4)
    r=p.add_run(); set_run(r,f"{i+1:02d}   ",11,BODY,SLATE,bold=True,track=1.0)
    r=p.add_run(); set_run(r,verb.upper(),15,HEAD,DEEP_NAVY,track=1.0)
    line(tf,rest,13,color=GRAPHITE,ls=1.16,sa=0)
GYY=Inches(5.10)
card(s,LX,GYY,RW,Inches(1.06),fill=DEEP_NAVY,line=None)
tb,tf=textbox(s,LX+Inches(0.28),GYY+Inches(0.13),RW-Inches(0.56),Inches(0.85))
line(tf,"GOVERNING PRINCIPLE",9,color=WHITE_D,bold=True,first=True,track=1.2,sa=5)
line(tf,GOV,13,color=WHITE,ls=1.22,sa=0)
tb,tf=textbox(s,LX,Inches(6.40),RW,Inches(0.3))
line(tf,"Formal resolutions to be confirmed by management and the company secretary; this slide reflects "
        "the locked Board Strategy Narrative v8 and does not itself constitute a resolution.",
     8.5,color=SLATE,italic=True,first=True,sa=0)
pg+=1; furniture(s,pg)

# 21 · CLOSING SYNTHESIS — dark-field emphasis (T14)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=DEEP_NAVY)
tb,tf=textbox(s,LX,Inches(0.52),Inches(9),Inches(0.28))
line(tf,"16 · The v8 proposition",10,color=WHITE_D,bold=True,first=True,track=1.6,caps=True,sa=0)
title(s,LX,Inches(0.86),"One coherent proposition for Aravest's next phase.",color=WHITE)
card(s,LX,Inches(2.0),RW,Inches(3.1),fill=NAVY_CARD_L,line=NAVY_CARD_B,shadow=False)
tb,tf=textbox(s,LX+Inches(0.34),Inches(2.28),RW-Inches(0.68),Inches(2.6))
line(tf,"Aravest is values-led in how it invests and value-focused in where it deploys. It will remain "
        "sector-flexible within a defined 2027 investment focus, pursue opportunities only where there "
        "is a clear value-creation plan and complete capability coverage, and structure every fund and "
        "investment to institutional standards.",15,color=WHITE,first=True,ls=1.4,sa=10)
line(tf,"Committed equity is exposed to investment performance, but wider liabilities are generally "
        "ring-fenced, with no automatic recourse to Aravest as manager or SMFL as shareholder.",
     15,color=WHITE,ls=1.4,sa=0)
tb,tf=textbox(s,LX,Inches(5.5),RW,Inches(0.4))
p=para(tf,first=True); p.space_after=Pt(0)
r=p.add_run(); set_run(r,"Pathway 1 builds the record",12.5,BODY,TEAL_LT,bold=True)
r=p.add_run(); set_run(r,"   ·   ",12.5,BODY,WHITE_D)
r=p.add_run(); set_run(r,"Pathway 2 can accelerate scale",12.5,BODY,STEEL_LT,bold=True)
pg+=1; furniture(s,pg,dark=True)

# 22 · APPENDIX DIVIDER (T18)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=GRAPH_T)
s.shapes.add_picture(A+"/logo_navy.png",Inches(11.90),Inches(0.36),height=Inches(0.38))
hrule(s,Inches(1.02),Inches(2.86),Inches(0.85),weight=1.5,color=NAVY)
tb,tf=textbox(s,Inches(1.0),Inches(3.05),Inches(10),Inches(1.4))
line(tf,"Appendix",34,font=SERIF,color=NAVY,first=True,sa=6)
line(tf,"Important notice and registered office.",13,color=GRAPHITE,sa=0)
tb,tf=textbox(s,Inches(1.0),Inches(7.06),Inches(5),Inches(0.3))
line(tf,"Private and Confidential",8.5,color=SLATE,first=True,sa=0)

# 23 · DISCLAIMER — Singapore (verbatim)
D=load_disclaimers()
s=add_slide(prs)
pg+=1
disclaimer_slide(s,"Singapore",D["SG"],pg)

# 24 · CLOSING (entity/address verbatim)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=DEEP_NAVY)
s.shapes.add_picture(A+"/logo_white.png",Inches(5.47),Inches(2.6),height=Inches(0.95))
addr=[p for p in D["CLOSING"] if p.strip()]
tb,tf=textbox(s,Inches(0),Inches(4.05),SW,Inches(1.2))
first=True
for p_ in addr:
    line(tf,p_,11.5,color=WHITE_D,align=PP_ALIGN.CENTER,first=first,sa=2); first=False
tb,tf=textbox(s,Inches(0),Inches(6.95),SW,Inches(0.35))
line(tf,"Private and Confidential",8.5,color=WHITE_D,align=PP_ALIGN.CENTER,first=True,sa=0)

prs.save("Aravest_Sample_Deck.pptx")
print("saved Aravest_Sample_Deck.pptx,",len(prs.slides._sldIdLst),"slides")
