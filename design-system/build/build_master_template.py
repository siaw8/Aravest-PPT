#!/usr/bin/env python3
"""Aravest Master Template — technical layout library (T01–T18) + jurisdiction
disclaimers (wording verbatim) + closing slide. Each slide is one technical
layout exemplar carrying generic guidance content; authors duplicate the slide
they need. Theme: V4-final approved system."""
from aravest_ds import *

prs=new_pres()

def tag(s,code,name,dark=False):
    tb,tf=textbox(s,Inches(4.2),Inches(7.06),Inches(5),Inches(0.3),anchor=MSO_ANCHOR.MIDDLE)
    line(tf,f"{code} · {name}",8.5,color=(WHITE_D if dark else SLATE),
         align=PP_ALIGN.CENTER,first=True,track=1.0,sa=0)

ENTITY="Aravest Fund Management Pte. Ltd.      Private and Confidential"

# T01 — Cover, dark institutional (DEFAULT Board cover)
s=add_slide(prs)
cover_B(s,"Presentation ","Title","One-sentence framing of the presentation's purpose and scope, "
        "written as a complete thought.","Meeting type  ·  Month Year",ENTITY)
tag(s,"T01","Cover — dark institutional (Board default)",dark=True)

# T02 — Cover, full-image (investor/marketing variant)
s=add_slide(prs)
cover_A(s,"Presentation ","Title","One-sentence framing of the presentation's purpose and scope, "
        "written as a complete thought.","Audience context  ·  Month Year",ENTITY)
tag(s,"T02","Cover — full image (investor/marketing)",dark=True)

# T03 — Section divider, typographic dark
s=add_slide(prs)
divider_typographic(s,"01","Section title set in Spectral Light",
                    "Optional one-line orientation for the section that follows.")
tag(s,"T03","Section divider — typographic dark",dark=True)

# T04 — Editorial statement / pull quote
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
s.shapes.add_picture(A+"/logo_navy.png",Inches(11.90),Inches(0.36),height=Inches(0.38))
tb,tf=textbox(s,Inches(1.6),Inches(2.4),Inches(10.1),Inches(2.2))
p=para(tf,first=True); p.line_spacing=1.18; p.space_after=Pt(0)
r=p.add_run(); set_run(r,"A single strategic statement set in Spectral Light, with ",30,SERIF,NAVY)
r=p.add_run(); set_run(r,"one emphasised phrase",30,SERIF,NAVY,italic=True)
r=p.add_run(); set_run(r,", carrying the argument of the section.",30,SERIF,NAVY)
rect(s,Inches(1.62),Inches(4.85),Pt(28),Pt(1.5),fill=GOLD)
tb,tf=textbox(s,Inches(1.6),Inches(5.1),Inches(9.5),Inches(0.8))
line(tf,"Optional supporting sentence in Aptos that grounds the statement in evidence.",
     13.5,color=GRAPHITE,first=True,ls=1.3,sa=0)
furniture(s,"n")
tag(s,"T04","Editorial statement / pull quote")

# T05 — Agenda / contents
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
title(s,Inches(1.0),Inches(0.72),"Agenda",size=30,w=Inches(6))
items=["Section one title","Section two title","Section three title",
       "Section four title","Section five title","Section six title"]
yy=Inches(2.0)
for i,it in enumerate(items,1):
    hrule(s,Inches(1.0),yy,Inches(11.3),weight=0.75,color=MIST)
    tb,tf=textbox(s,Inches(1.0),yy+Inches(0.10),Inches(0.9),Inches(0.5))
    line(tf,f"{i:02d}",14,font=SERIF,color=SLATE,first=True,sa=0)
    tb,tf=textbox(s,Inches(1.9),yy+Inches(0.10),Inches(9.0),Inches(0.5))
    line(tf,it,15,font=HEAD,color=NAVY,first=True,sa=0)
    yy+=Inches(0.72)
furniture(s,"n")
tag(s,"T05","Agenda / contents")

# T06 — Card framework: 1×4 progression + conclusion band
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
LX=Inches(1.0); CW=Inches(11.33)
title(s,LX,Inches(0.66),"Conclusion-led headline states the takeaway in one or two lines.",size=26,w=CW)
tb,tf=textbox(s,LX,Inches(1.66),Inches(11.0),Inches(0.7))
line(tf,"Optional lead paragraph that frames the four elements below (14pt Aptos, Graphite).",
     14,color=GRAPHITE,first=True,ls=1.26,sa=0)
CY=Inches(2.62); CH=Inches(2.95); colw=Inches(2.72); gap=Inches(0.15)
accs=[(TEAL,TEAL_T,TEAL_B),(None,WHITE,GRAPH_B),(STEEL,STEEL_T,STEEL_B),(None,WHITE,GRAPH_B)]
for i,(acc,fillc,bord) in enumerate(accs):
    x=LX+i*(colw+gap)
    card(s,x,CY,colw,CH,fill=fillc,line=bord)
    tb,tf=textbox(s,x+Inches(0.20),CY+Inches(0.18),colw-Inches(0.40),CH-Inches(0.36))
    line(tf,f"{i+1:02d}",10.5,color=(acc or SLATE),bold=True,first=True,track=1.2,sa=5)
    line(tf,"Card title",14.5,font=HEAD,color=NAVY,sa=6,ls=1.03)
    line(tf,"Lead point of the card at minimum 13pt Aptos in Graphite.",13,color=GRAPHITE,ls=1.22,sa=6)
    line(tf,"Supporting sentence, kept brief.",12.5,color=GRAPHITE,ls=1.22,sa=0)
conclusion_band(s,LX,Inches(5.90),CW,"Conclusion.","Full-width Deep Navy band carrying the synthesis.")
furniture(s,"n")
tag(s,"T06","Card framework — 1×4 + conclusion band")

# T07 — Twin comparison cards + connector
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
LX=Inches(0.7); RW=Inches(11.93)
kicker(s,LX,Inches(0.48),"Section · Topic")
title(s,LX,Inches(0.80),"Headline states the comparison's conclusion.")
CY=Inches(1.66); CH=Inches(4.30); CWD=Inches(5.80); X2=Inches(6.83)
for X,name,role,acc,fillc,bord in [
    (LX,"Option A — name","Role descriptor",TEAL,TEAL_T,TEAL_B),
    (X2,"Option B — name","Role descriptor",STEEL,STEEL_T,STEEL_B)]:
    card(s,X,CY,CWD,CH,fill=fillc,line=bord)
    rect(s,X+Inches(0.22),CY,CWD-Inches(0.44),Pt(2.5),fill=acc)
    tb,tf=textbox(s,X+Inches(0.26),CY+Inches(0.16),CWD-Inches(0.52),Inches(0.8))
    line(tf,name,15,font=HEAD,color=NAVY,first=True,ls=1.04,sa=3)
    line(tf,role.upper(),9.5,color=acc,bold=True,track=1.2,sa=0)
    for j in range(4):
        oy=CY+Inches(1.05)+j*Inches(0.78)
        tb,tf=textbox(s,X+Inches(0.26),oy,CWD-Inches(0.52),Inches(0.72))
        line(tf,"ROW LABEL",9,color=GRAPHITE,bold=True,first=True,track=0.8,sa=2)
        line(tf,"Aligned comparable value at 13pt.",13,color=GRAPHITE,ls=1.15,sa=0)
card(s,LX,Inches(6.14),RW,Inches(0.58),fill=DEEP_NAVY,line=None)
tb,tf=textbox(s,LX+Inches(0.28),Inches(6.14),RW-Inches(0.56),Inches(0.58),anchor=MSO_ANCHOR.MIDDLE)
p=para(tf,first=True); p.space_after=Pt(0)
r=p.add_run(); set_run(r,"RELATIONSHIP   ",10,BODY,WHITE_D,bold=True,track=1.4)
r=p.add_run(); set_run(r,"How A relates",13,BODY,TEAL_LT,bold=True)
r=p.add_run(); set_run(r,"  to  ",13,BODY,WHITE_D)
r=p.add_run(); set_run(r,"B, stated plainly",13,BODY,STEEL_LT,bold=True)
r=p.add_run(); set_run(r,".",13,BODY,WHITE_D)
furniture(s,"n")
tag(s,"T07","Twin comparison cards + connector")

# T08 — Anchor dashboard
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
LX=Inches(0.7); RW=Inches(11.93)
kicker(s,LX,Inches(0.48),"Section · Topic")
title(s,LX,Inches(0.80),"Headline states what the numbers show.")
hrule(s,LX,Inches(1.56),RW,weight=0.75,color=MIST)
tb,tf=textbox(s,LX,Inches(1.68),RW,Inches(0.40),anchor=MSO_ANCHOR.MIDDLE)
line(tf,"Optional identity or defining equation set as typography",14.5,font=HEAD,color=NAVY,
     align=PP_ALIGN.CENTER,first=True,sa=0)
hrule(s,LX,Inches(2.20),RW,weight=0.75,color=MIST)
AY=Inches(2.44); AH=Inches(3.42)
card(s,LX,AY,Inches(3.05),AH,fill=DEEP_NAVY,line=None)
tb,tf=textbox(s,LX+Inches(0.26),AY+Inches(0.22),Inches(2.55),AH-Inches(0.44))
line(tf,"ANCHOR LABEL",9,color=WHITE_D,bold=True,first=True,track=1.0,sa=8)
line(tf,"KPI",34,font=HEAD,color=WHITE,sa=9,ls=1.0)
line(tf,"Supporting context for the anchor figure at 13pt.",13,color=WHITE_D,ls=1.26,sa=0)
for x,w,t,c in [(Inches(3.95),Inches(4.28),"Supporting measure — teal",TEAL),
                (Inches(8.43),Inches(4.20),"Supporting measure — steel",STEEL)]:
    card(s,x,AY,w,AH,fill=WHITE,line=GRAPH_B)
    tb,tf=textbox(s,x+Inches(0.24),AY+Inches(0.18),w-Inches(0.48),Inches(0.5))
    line(tf,t,13.5,font=HEAD,color=c,first=True,ls=1.03,sa=0)
    bars(s,x+Inches(0.24),AY+Inches(2.02),w-Inches(0.48),[0.45,0.6,0.5,0.7,0.62,0.8,0.72],c)
    tb,tf=textbox(s,x+Inches(0.24),AY+Inches(2.14),w-Inches(0.48),Inches(1.05))
    line(tf,"Caption interpreting the profile at 13pt Graphite.",13,color=GRAPHITE,first=True,ls=1.2,sa=3)
    line(tf,"Qualifier or basis note.",9,color=SLATE,italic=True,sa=0)
card(s,LX,Inches(6.06),RW,Inches(0.56),fill=GRAPH_T,line=GRAPH_B,shadow=False)
tb,tf=textbox(s,LX+Inches(0.26),Inches(6.06),RW-Inches(0.52),Inches(0.56),anchor=MSO_ANCHOR.MIDDLE)
p=para(tf,first=True); p.space_after=Pt(0)
r=p.add_run(); set_run(r,"UTILITY BAND   ",9.5,BODY,NAVY,bold=True,track=1.0)
r=p.add_run(); set_run(r,"Proof point, source basis or quiet contextual note at 12–13pt.",12.5,BODY,GRAPHITE)
furniture(s,"n")
tag(s,"T08","Anchor dashboard — dark KPI + supporting cards")

# T09 — KPI strip + chart frame
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
LX=Inches(0.7); RW=Inches(11.93)
kicker(s,LX,Inches(0.48),"Section · Topic")
title(s,LX,Inches(0.80),"Headline interprets the chart, not the topic.")
ky=Inches(1.66)
for i,(lab,val) in enumerate([("MEASURE ONE","0.0"),("MEASURE TWO","0.0"),
                              ("MEASURE THREE","0.0"),("MEASURE FOUR","0.0")]):
    x=LX+i*Inches(3.02)
    tb,tf=textbox(s,x,ky,Inches(2.8),Inches(1.0))
    line(tf,lab,9,color=GRAPHITE,bold=True,first=True,track=1.0,sa=4)
    line(tf,val,26,font=HEAD,color=NAVY,sa=0)
    if i: rect(s,x-Inches(0.21),ky+Inches(0.06),Pt(0.75),Inches(0.85),fill=MIST)
hrule(s,LX,Inches(2.85),RW,weight=0.75,color=MIST)
bars(s,Inches(1.1),Inches(5.9),Inches(10.9),[0.35,0.5,0.42,0.62,0.55,0.74,0.66,0.85,0.8,1.0],
     NAVY,maxh=2.4,bw=Inches(0.55))
tb,tf=textbox(s,LX,Inches(6.15),RW,Inches(0.4))
line(tf,"Source: basis note at 8.5pt Slate.",8.5,color=SLATE,italic=True,first=True,sa=0)
furniture(s,"n")
tag(s,"T09","KPI strip + chart frame")

# T10 — Chart + commentary rail
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
LX=Inches(0.7)
kicker(s,LX,Inches(0.48),"Section · Topic")
title(s,LX,Inches(0.80),"Headline states the movement the chart shows.",w=Inches(11.9))
bars(s,Inches(0.9),Inches(5.7),Inches(7.4),[0.5,0.44,0.6,0.53,0.7,0.64,0.8,0.9],NAVY,maxh=2.6,bw=Inches(0.5))
tb,tf=textbox(s,Inches(0.9),Inches(5.95),Inches(7.4),Inches(0.4))
line(tf,"Source: basis note.",8.5,color=SLATE,italic=True,first=True,sa=0)
RX=Inches(8.85); RWd=Inches(3.78)
card(s,RX,Inches(1.70),RWd,Inches(4.6),fill=GRAPH_T,line=GRAPH_B,shadow=False)
tb,tf=textbox(s,RX+Inches(0.24),Inches(1.92),RWd-Inches(0.48),Inches(4.2))
line(tf,"WHAT THIS SHOWS",9,color=GRAPHITE,bold=True,first=True,track=1.0,sa=6)
for t in ["First observation stated plainly at 13pt.",
          "Second observation with its implication.",
          "Third observation, including any caveat."]:
    line(tf,t,13,color=GRAPHITE,ls=1.24,sa=8)
furniture(s,"n")
tag(s,"T10","Chart + commentary rail")

# T11 — Full institutional table (markers, no row tints)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
LX=Inches(0.7); RW=Inches(11.93)
kicker(s,LX,Inches(0.48),"Section · Topic")
title(s,LX,Inches(0.80),"Dense tables use pathway markers, never full row tints.")
HY=Inches(1.72)
cols=[(Inches(1.02),Inches(2.9),"Column one"),(Inches(4.10),Inches(3.1),"Column two"),
      (Inches(7.40),Inches(2.4),"Column three"),(Inches(9.95),Inches(2.5),"Column four")]
for x,w,h in cols:
    tb,tf=textbox(s,x,HY,w,Inches(0.3))
    line(tf,h.upper(),9.5,color=GRAPHITE,bold=True,first=True,track=1.1,sa=0)
rect(s,LX,HY+Inches(0.32),RW,Pt(1.5),fill=NAVY)
ry=HY+Inches(0.42)
for i,acc in enumerate([STEEL,TEAL,TEAL,None,STEEL]):
    if i>0: hrule(s,LX,ry,RW,weight=0.75,color=MIST)
    if acc: pathway_marker(s,LX,ry+Inches(0.14),Inches(0.52),acc)
    for x,w,_ in cols:
        tb,tf=textbox(s,x,ry+Inches(0.14),w,Inches(0.6))
        line(tf,"Row content at 12–13pt Graphite, numbers right-aligned.",12,color=GRAPHITE,
             first=True,ls=1.15,sa=0)
    ry+=Inches(0.78)
rect(s,LX,ry,RW,Pt(1.0),fill=NAVY)
tb,tf=textbox(s,LX,ry+Inches(0.12),RW,Inches(0.4))
line(tf,"Caveat or basis note at 9pt Slate italic.",9,color=SLATE,italic=True,first=True,sa=0)
furniture(s,"n")
tag(s,"T11","Full institutional table — pathway markers")

# T12 — Horizontal row cards
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
LX=Inches(0.7); RW=Inches(11.93)
kicker(s,LX,Inches(0.48),"Section · Topic")
title(s,LX,Inches(0.80),"Row cards group one entity per row with aligned columns.")
R1,R1W=Inches(1.02),Inches(3.05); R2,R2W=Inches(4.32),Inches(4.35); R3,R3W=Inches(8.97),Inches(3.45)
HY=Inches(1.70)
for x,w,h in [(R1,R1W,"Entity"),(R2,R2W,"Detail"),(R3,R3W,"Implication")]:
    tb,tf=textbox(s,x,HY,w,Inches(0.3))
    line(tf,h.upper(),9.5,color=GRAPHITE,bold=True,first=True,track=1.1,sa=0)
ry=Inches(2.10); rh=Inches(1.34)
for tagname,acc,fillc,bord in [("MARKER A",STEEL,STEEL_T,STEEL_B),
                               ("MARKER B",TEAL,TEAL_T,TEAL_B),
                               ("MARKER B",TEAL,TEAL_T,TEAL_B)]:
    card(s,LX,ry,RW,rh,fill=fillc,line=bord)
    rect(s,LX,ry+Inches(0.18),Pt(3),rh-Inches(0.36),fill=acc)
    tb,tf=textbox(s,R1,ry+Inches(0.20),R1W,rh-Inches(0.4))
    line(tf,"Row title",14,font=HEAD,color=NAVY,first=True,ls=1.05,sa=5)
    line(tf,tagname,9.5,color=acc,bold=True,track=1.2,sa=0)
    for x,w in [(R2,R2W),(R3,R3W)]:
        tb,tf=textbox(s,x,ry+Inches(0.22),w,rh-Inches(0.4))
        line(tf,"Aligned column content at 13pt Graphite.",13,color=GRAPHITE,first=True,ls=1.22,sa=0)
    ry+=rh+Inches(0.16)
furniture(s,"n")
tag(s,"T12","Horizontal row cards")

# T13 — Decision (light, DEFAULT)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
LX=Inches(0.7); RW=Inches(11.93)
decision_kicker(s,LX,Inches(0.48))
title(s,LX,Inches(0.82),"The decision asked of the Board, stated as the headline.")
DCW=Inches(5.86); DCH=Inches(1.34); GX=[LX,Inches(6.77)]; GY_=[Inches(2.02),Inches(3.52)]
for i,verb in enumerate(["Endorse","Support","Endorse","Agree"]):
    x=GX[i%2]; y=GY_[i//2]
    card(s,x,y,DCW,DCH,fill=WHITE,line=GRAPH_B)
    tb,tf=textbox(s,x+Inches(0.24),y+Inches(0.15),DCW-Inches(0.48),DCH-Inches(0.3))
    p=para(tf,first=True); p.space_after=Pt(4)
    r=p.add_run(); set_run(r,f"{i+1:02d}   ",11,BODY,SLATE,bold=True,track=1.0)
    r=p.add_run(); set_run(r,verb.upper(),15,HEAD,DEEP_NAVY,track=1.0)
    line(tf,"The matter for decision at 13pt Graphite, one to three lines.",13,color=GRAPHITE,ls=1.18,sa=0)
GYY=Inches(5.10)
card(s,LX,GYY,RW,Inches(1.06),fill=DEEP_NAVY,line=None)
tb,tf=textbox(s,LX+Inches(0.28),GYY+Inches(0.13),RW-Inches(0.56),Inches(0.85))
line(tf,"GOVERNING PRINCIPLE",9,color=WHITE_D,bold=True,first=True,track=1.2,sa=5)
line(tf,"The principle that governs the decision, in white at 13pt on Deep Navy.",13,color=WHITE,ls=1.22,sa=0)
tb,tf=textbox(s,LX,Inches(6.40),RW,Inches(0.3))
line(tf,"Footnote on the status of resolutions at 8.5pt.",8.5,color=SLATE,italic=True,first=True,sa=0)
furniture(s,"n")
tag(s,"T13","Decision — light (default)")

# T14 — Dark-field emphasis (variant)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=DEEP_NAVY)
decision_kicker(s,LX,Inches(0.48),"Emphasis variant — reserve for the pivotal moment",dark=True)
title(s,LX,Inches(0.82),"Dark-field slide reserved for the deck's most consequential message.",color=WHITE)
card(s,LX,Inches(2.3),RW,Inches(2.4),fill=NAVY_CARD_L,line=NAVY_CARD_B,shadow=False)
tb,tf=textbox(s,LX+Inches(0.3),Inches(2.55),RW-Inches(0.6),Inches(2.0))
line(tf,"THE PROPOSITION",9.5,color=STEEL_LT,bold=True,first=True,track=1.2,sa=8)
line(tf,"A substantial statement or synthesis set at 15–16pt in white, given room to breathe. "
        "Use once per deck — for the closing synthesis, the pivotal decision, or the single "
        "message the Board must retain.",15,color=WHITE,ls=1.35,sa=0)
tb,tf=textbox(s,LX,Inches(5.2),RW,Inches(0.4))
line(tf,"Supporting note in dimmed white.",11,color=WHITE_D,first=True,sa=0)
furniture(s,"n",dark=True)
tag(s,"T14","Dark-field emphasis (variant)",dark=True)

# T15 — Process / timeline
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"Section · Topic")
title(s,LX,Inches(0.80),"Process headline states where the sequence leads.")
steps=["Stage one","Stage two","Stage three","Stage four","Stage five"]
n=len(steps); sw=Inches(2.12); gap=(Inches(11.93)-sw*n)/(n-1)
sy=Inches(2.6)
for i,st in enumerate(steps):
    x=LX+i*(sw+gap)
    card(s,x,sy,sw,Inches(1.5),fill=WHITE,line=GRAPH_B)
    tb,tf=textbox(s,x+Inches(0.16),sy+Inches(0.16),sw-Inches(0.32),Inches(1.2))
    line(tf,f"{i+1:02d}",10.5,color=SLATE,bold=True,first=True,track=1.2,sa=4)
    line(tf,st,13.5,font=HEAD,color=NAVY,ls=1.05,sa=0)
    if i<n-1:
        tb,tf=textbox(s,x+sw,sy+Inches(0.55),gap,Inches(0.4),anchor=MSO_ANCHOR.MIDDLE)
        line(tf,"→",16,color=GRAPHITE,align=PP_ALIGN.CENTER,first=True,sa=0)
tb,tf=textbox(s,LX,Inches(4.6),Inches(11.93),Inches(0.9))
line(tf,"Optional narrative paragraph beneath the process at 13.5pt, interpreting the sequence "
        "rather than repeating it.",13.5,color=GRAPHITE,first=True,ls=1.3,sa=0)
conclusion_band(s,LX,Inches(5.75),Inches(11.93),"Where it leads.","One-line consequence of the process.")
furniture(s,"n")
tag(s,"T15","Process / timeline")

# T16 — Case study / asset profile
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"Case study")
title(s,LX,Inches(0.80),"Case headline states what the example demonstrates.")
s.shapes.add_picture(A+"/hero_seoul.jpg",LX,Inches(1.70),width=Inches(4.4),height=Inches(3.87))
rect(s,LX,Inches(1.70),Inches(4.4),Inches(3.87),fill=None,line=MIST,line_w=Pt(0.75))
RX=Inches(5.45); RWd=Inches(7.18)
tb,tf=textbox(s,RX,Inches(1.74),RWd,Inches(3.9))
line(tf,"THE SEQUENCE",9.5,color=GRAPHITE,bold=True,first=True,track=1.2,sa=8)
for i,step in enumerate(["First step of the case narrative at 13pt.",
                         "Second step with the decisive action.",
                         "Third step and the observable outcome.",
                         "What the case proves for the strategy."],1):
    p=para(tf); p.space_after=Pt(9); p.line_spacing=1.25
    r=p.add_run(); set_run(r,f"{i:02d}  ",11,BODY,SLATE,bold=True,track=1.0)
    r=p.add_run(); set_run(r,step,13.5,BODY,GRAPHITE)
card(s,RX,Inches(5.15),RWd,Inches(0.9),fill=GRAPH_T,line=GRAPH_B,shadow=False)
tb,tf=textbox(s,RX+Inches(0.24),Inches(5.15),RWd-Inches(0.48),Inches(0.9),anchor=MSO_ANCHOR.MIDDLE)
line(tf,"HOW TO READ THE CASE",9,color=NAVY,bold=True,first=True,track=1.0,sa=4)
line(tf,"Qualifier — a model demonstrated, not an assured timetable.",12.5,color=GRAPHITE,ls=1.2,sa=0)
furniture(s,"n")
tag(s,"T16","Case study / asset profile")

# T17 — Text + rail working slide
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"Section · Topic")
title(s,LX,Inches(0.80),"Working headline for narrative content.")
tb,tf=textbox(s,LX,Inches(1.78),Inches(7.6),Inches(4.8))
for i,t in enumerate(["Narrative paragraph at 13.5pt with 1.3 line spacing, holding to roughly "
                      "one hundred and ten words per slide.",
                      "Second paragraph developing the argument, each paragraph a single thought.",
                      "Third paragraph closing the reasoning and pointing to the consequence."]):
    line(tf,t,13.5,color=GRAPHITE,first=(i==0),ls=1.32,sa=10)
card(s,Inches(8.85),Inches(1.78),Inches(3.78),Inches(3.4),fill=GRAPH_T,line=GRAPH_B,shadow=False)
tb,tf=textbox(s,Inches(9.09),Inches(1.98),Inches(3.3),Inches(3.0))
line(tf,"IN BRIEF",9,color=GRAPHITE,bold=True,first=True,track=1.0,sa=6)
for t in ["Key point distilled.","Second key point.","Third key point."]:
    line(tf,t,13,color=GRAPHITE,ls=1.25,sa=8)
furniture(s,"n")
tag(s,"T17","Text + rail")

# T18 — Appendix divider
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=GRAPH_T)
s.shapes.add_picture(A+"/logo_navy.png",Inches(11.90),Inches(0.36),height=Inches(0.38))
tb,tf=textbox(s,Inches(1.0),Inches(3.0),Inches(10),Inches(1.2))
line(tf,"Appendix",34,font=SERIF,color=NAVY,first=True,sa=6)
line(tf,"Supporting analysis and reference material.",13,color=GRAPHITE,sa=0)
hrule(s,Inches(1.02),Inches(2.86),Inches(0.85),weight=1.5,color=NAVY)
tb,tf=textbox(s,Inches(1.0),Inches(7.06),Inches(5),Inches(0.3))
line(tf,"Private and Confidential",8.5,color=SLATE,first=True,sa=0)
tag(s,"T18","Appendix divider")

# ---- Jurisdiction disclaimers (wording preserved verbatim) ----
D=load_disclaimers()
for code,jur in [("SG","Singapore"),("AU","Australia"),("KR","Korea"),("KRREF","Korea (REF)")]:
    s=add_slide(prs)
    disclaimer_slide(s,jur,D[code],"D·"+code)

# ---- Closing slide (entity/address verbatim from original) ----
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

prs.save("Aravest_Master_Template.pptx")
print("saved Aravest_Master_Template.pptx,",len(prs.slides._sldIdLst),"slides")
