#!/usr/bin/env python3
"""
Aravest Board Strategy Discussion Paper — "Aravest's Next Phase"
Built 1:1 from the LOCKED Board Strategy Narrative v8 following its own §16
slide architecture (16 sections; the densest split across two slides so no
message is lost at Board-readable type). Each slide carries the narrative's
"suggested narrative" verbatim as speaker notes. Discussion paper: no decision
slide; closes on the v8 proposition.
"""
from aravest_ds import *

prs=new_pres()
ENTITY="Aravest Fund Management Pte. Ltd.      Private and Confidential"
SUBTITLE=("From integration to institution-building: establishing the post-SMFL track record, "
          "defining the near-term investment focus and developing the pathways for sustainable "
          "long-term growth.")
LX=Inches(0.7); RW=Inches(11.93)
pg=0

def notes(s,text):
    s.notes_slide.notes_text_frame.text=text

# ============================================================ 1 · COVER
s=add_slide(prs)
cover_B(s,"Aravest’s ","Next Phase",SUBTITLE,
        "Private & Confidential  ·  Board Strategy Meeting  ·  September 2026",ENTITY)
notes(s,"Board discussion paper. Locked Board Strategy Story v8 — the agreed strategic "
        "narrative; not to be reopened or materially changed unless specifically directed.")

# ============================================================ 2 · §01 PURPOSE
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
s.shapes.add_picture(A+"/logo_navy.png",Inches(11.90),Inches(0.36),height=Inches(0.38))
kicker(s,Inches(1.0),Inches(0.72),"01 · Purpose")
tb,tf=textbox(s,Inches(1.0),Inches(1.30),Inches(11.0),Inches(1.6))
p=para(tf,first=True); p.line_spacing=1.16; p.space_after=Pt(0)
r=p.add_run(); set_run(r,"Aravest is moving from integration into ",29,SERIF,NAVY)
r=p.add_run(); set_run(r,"institution-building",29,SERIF,NAVY,italic=True)
r=p.add_run(); set_run(r,".",29,SERIF,NAVY)
rect(s,Inches(1.02),Inches(2.42),Pt(28),Pt(1.5),fill=GOLD)
tb,tf=textbox(s,Inches(1.0),Inches(2.66),Inches(11.0),Inches(1.35))
line(tf,"The initial integration into SMFL has been substantially completed. Aravest has maintained "
        "continuity across the platform, strengthened governance and begun building a visible record "
        "of execution under the new sponsor. The next phase is to develop the institutional foundations "
        "and investment record required for sustainable long-term growth.",
     13.5,color=GRAPHITE,first=True,ls=1.32,sa=0)
card(s,Inches(1.0),Inches(4.45),Inches(11.33),Inches(1.55),fill=DEEP_NAVY,line=None)
tb,tf=textbox(s,Inches(1.3),Inches(4.62),Inches(10.7),Inches(1.25))
line(tf,"TODAY’S DISCUSSION",9.5,color=WHITE_D,bold=True,first=True,track=1.3,sa=6)
line(tf,"Management’s perspective on Aravest’s next phase: the institution we are building, the track "
        "record we need to establish, and the two parallel pathways through which the platform can develop.",
     14.5,color=WHITE,ls=1.3,sa=0)
pg=1; furniture(s,pg)
notes(s,"“The first phase of Aravest under SMFL ownership was focused on integration and continuity. "
        "As that work progresses, our focus is increasingly on the next phase: building the institutional "
        "foundations, investment record and investor confidence required for Aravest’s long-term development.”")

# ============================================================ 3 · §02 DEVELOPMENT PATHWAY
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"02 · Development pathway")
title(s,LX,Inches(0.80),"The proof-building process has begun and will become the principal focus from 2027 to 2029.")
tb,tf=textbox(s,LX,Inches(1.62),RW,Inches(0.55))
line(tf,"Aravest’s development should be viewed as an overlapping journey rather than a sequence of "
        "separate initiatives. The emphasis changes over time as the platform moves from integration, "
        "to institutional identity, to a broader body of investment proof and ultimately to scale.",
     12.5,color=GRAPHITE,first=True,ls=1.24,sa=0)
phases=[("2025","Integrate and begin proving",
         "Complete the initial integration, maintain platform continuity and begin demonstrating execution under SMFL ownership.",False),
        ("2026","Establish institutional identity",
         "Introduce The Aravest Way, deepen governance and investment discipline, and continue building visible post-SMFL evidence.",False),
        ("2027–2029","Build and compound the record",
         "Execute selected opportunities, demonstrate outcomes, establish repeatable strategies and deepen investor relationships.",True),
        ("Around 2030 onward","Convert proof into scale",
         "Use the accumulated track record to pursue larger and increasingly repeatable institutional capital.",False)]
n=len(phases); cw=Inches(2.80); gapx=(RW-cw*n)/(n-1); cy=Inches(2.42); ch=Inches(2.95)
for i,(yr,h,b,emph) in enumerate(phases):
    x=LX+i*(cw+gapx)
    card(s,x,cy,cw,ch,fill=(TEAL_T if emph else WHITE),line=(TEAL_B if emph else GRAPH_B))
    rect(s,x+Inches(0.2),cy,cw-Inches(0.4),Pt(2.5),fill=(TEAL if emph else GRAPH_B))
    tb,tf=textbox(s,x+Inches(0.2),cy+Inches(0.16),cw-Inches(0.4),ch-Inches(0.32))
    line(tf,yr.upper(),9.5,color=(TEAL if emph else GRAPHITE),bold=True,first=True,track=1.0,sa=5)
    line(tf,h,14.5,font=HEAD,color=NAVY,sa=6,ls=1.05)
    line(tf,b,13,color=GRAPHITE,ls=1.22,sa=0)
    if i<n-1:
        tb,tf=textbox(s,x+cw,cy+Inches(1.15),gapx,Inches(0.4),anchor=MSO_ANCHOR.MIDDLE)
        line(tf,"→",15,color=GRAPHITE,align=PP_ALIGN.CENTER,first=True,sa=0)
conclusion_band(s,LX,Inches(5.72),RW,"Around 2030","is a realistic point at which a broader body of "
                "institutional capital may become more achievable, subject to the pace of execution and "
                "market conditions.")
pg+=1; furniture(s,pg)
notes(s,"“The process of building a post-SMFL track record has already started. From 2027 to 2029, that "
        "becomes the central strategic focus. Around 2030 is a realistic point at which a broader body of "
        "institutional capital may become more achievable, subject to the pace of execution and market conditions.”")

# ============================================================ 4 · §03(i) THE ARAVEST WAY — values
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"03 · The Aravest Way")
title(s,LX,Inches(0.80),"The Aravest Way provides the institutional foundation for how Aravest conducts its business and invests.")
tb,tf=textbox(s,LX,Inches(1.66),RW,Inches(0.60))
line(tf,"Long-term growth cannot be built on transactions alone. Institutional capital is entrusted to "
        "managers that demonstrate consistency of judgement, conduct and responsibility over time. These "
        "principles should remain constant as the platform grows, enters new strategies and works with a "
        "wider range of investors and partners.",12.5,color=GRAPHITE,first=True,ls=1.24,sa=0)
vals=[("EXCELLENCE","The quality of our thinking",
       "Excellence guides how Aravest analyses, prepares, executes, communicates and continuously raises its standards."),
      ("TRUST","The way we behave",
       "Trust guides how Aravest deals with investors, shareholders, partners, lenders and colleagues, particularly when circumstances are difficult."),
      ("ACCOUNTABILITY","How we take ownership",
       "Accountability requires Aravest to own its decisions and outcomes, act when circumstances change and remain responsible through the full investment lifecycle.")]
cy=Inches(2.52); ch=Inches(2.55); cwv=Inches(3.87); gapx=Inches(0.16)
for i,(tag_,h,b) in enumerate(vals):
    x=LX+i*(cwv+gapx)
    card(s,x,cy,cwv,ch,fill=WHITE,line=GRAPH_B)
    tb,tf=textbox(s,x+Inches(0.24),cy+Inches(0.20),cwv-Inches(0.48),ch-Inches(0.4))
    line(tf,tag_,9.5,color=GRAPHITE,bold=True,first=True,track=1.3,sa=6)
    line(tf,h,15,font=HEAD,color=NAVY,sa=7,ls=1.05)
    line(tf,b,13,color=GRAPHITE,ls=1.26,sa=0)
conclusion_band(s,LX,Inches(5.34),RW,"Our first principle.",
                "Investment management is a responsibility before it is a business.",h=Inches(0.62))
tb,tf=textbox(s,LX,Inches(6.18),RW,Inches(0.6))
line(tf,"Every investment, partnership and decision should be tested against the responsibility Aravest "
        "accepts when capital and trust are entrusted to the platform. These values are equal and "
        "inseparable; strategies will evolve and markets will change — the values should remain constant.",
     11.5,color=GRAPHITE,first=True,ls=1.22,sa=0)
pg+=1; furniture(s,pg)
notes(s,"“The Aravest Way separates what should remain constant from what may evolve. Our values define how "
        "we conduct our business. Our investment philosophy explains how those values are applied to "
        "investing. Together, they create the consistency and trust required to build a larger institution "
        "without losing the standards on which that institution depends.”")

# ============================================================ 5 · §03(ii) INVESTMENT PHILOSOPHY
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"03 · The Aravest Way · Investment philosophy")
title(s,LX,Inches(0.80),"Our investment philosophy applies the values to investing.")
HY=Inches(1.52)
for x,w,h in [(Inches(1.02),Inches(3.0),"Investment principle"),(Inches(4.35),Inches(8.2),"How Aravest applies it")]:
    tb,tf=textbox(s,x,HY,w,Inches(0.3))
    line(tf,h.upper(),9.5,color=GRAPHITE,bold=True,first=True,track=1.1,sa=0)
rect(s,LX,HY+Inches(0.30),RW,Pt(1.5),fill=NAVY)
phil=[("Recognising Value","Look beyond transaction activity to identify genuine value gaps, form an independent judgement and understand how value can be responsibly realised."),
      ("Partnership","Understand where Aravest creates the greatest value, identify where complementary capabilities are required and assemble the best combination of expertise for the investment."),
      ("Stewardship of Capital","Manage capital through the full life of the investment with a clear purpose, disciplined ownership and responsibility for both value creation and capital preservation."),
      ("Risk & Resilience","Understand risk, accept it deliberately, build resilience before it is needed and adapt when the facts require it."),
      ("Fit for Purpose","Keep the principles constant while tailoring the structure, strategy and solution to the purpose and circumstances of each investment.")]
ry=HY+Inches(0.40)
for i,(k,v) in enumerate(phil):
    if i>0: hrule(s,LX,ry,RW,weight=0.75,color=MIST)
    tb,tf=textbox(s,Inches(1.02),ry+Inches(0.08),Inches(3.0),Inches(0.55))
    line(tf,k,12.5,font=HEAD,color=NAVY,first=True,ls=1.08,sa=0)
    tb,tf=textbox(s,Inches(4.35),ry+Inches(0.09),Inches(8.2),Inches(0.55))
    line(tf,v,12,color=GRAPHITE,first=True,ls=1.15,sa=0)
    ry+=Inches(0.58)
rect(s,LX,ry,RW,Pt(1.0),fill=NAVY)
# why it matters — three compact columns
wy=ry+Inches(0.20)
why=[("Consistency as the platform grows","A common constitution enables teams across countries and strategies to apply the same standards as the business becomes larger and more complex."),
     ("Trust with investors and partners","A clearer understanding of how Aravest will act — not only when investments perform well, but also when decisions become difficult."),
     ("Repeatability without dilution","Codified principles allow Aravest to repeat and scale successful strategies without diluting the standards or identity of the institution.")]
cww=Inches(3.87)
for i,(h,b) in enumerate(why):
    x=LX+i*(cww+Inches(0.16))
    tb,tf=textbox(s,x,wy,cww,Inches(1.55))
    line(tf,"WHY IT MATTERS" if i==0 else " ",8.5,color=SLATE,bold=True,first=True,track=1.2,sa=4)
    line(tf,h,12.5,font=HEAD,color=NAVY,sa=4,ls=1.05)
    line(tf,b,11,color=GRAPHITE,ls=1.18,sa=0)
pg+=1; furniture(s,pg)
notes(s,"“The Aravest Way separates what should remain constant from what may evolve. Our values define how "
        "we conduct our business. Our investment philosophy explains how those values are applied to investing.”")

# ============================================================ 6 · §04 VALUES-LED. VALUE-FOCUSED.
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"04 · Values-led. Value-focused.")
title(s,LX,Inches(0.80),"The Aravest Way defines how we invest; value creation determines where we deploy.")
CY=Inches(1.70); CH=Inches(4.30); CWD=Inches(5.80); X2=Inches(6.83)
panels=[
 (LX,"Values-led","The standards remain constant",TEAL,TEAL_T,TEAL_B,
  "The Aravest Way guides how Aravest exercises judgement, conducts itself and stewards capital through the full investment lifecycle.",
  ["Excellence: disciplined thinking, underwriting and execution.",
   "Trust: alignment, transparency and institutional governance.",
   "Accountability: ownership of decisions, risks and investment outcomes."]),
 (X2,"Value-focused","Deployment follows identifiable value",STEEL,STEEL_T,STEEL_B,
  "Aravest deploys only where it can establish a genuine value opportunity and a credible path to realisation.",
  ["A genuine value gap, mispricing or market dislocation.",
   "A clear and executable value-creation plan.",
   "Complete capabilities, internally or through secured partners.",
   "A credible route to stabilisation, capital recycling or exit."]),
]
for X,tag_,h,acc,fillc,bord,intro,points in panels:
    card(s,X,CY,CWD,CH,fill=fillc,line=bord)
    rect(s,X+Inches(0.22),CY,CWD-Inches(0.44),Pt(2.5),fill=acc)
    tb,tf=textbox(s,X+Inches(0.26),CY+Inches(0.18),CWD-Inches(0.52),CH-Inches(0.36))
    line(tf,tag_.upper(),9.5,color=acc,bold=True,first=True,track=1.2,sa=4)
    line(tf,h,15,font=HEAD,color=NAVY,sa=6,ls=1.04)
    line(tf,intro,12,color=GRAPHITE,ls=1.2,sa=7)
    for pt_ in points:
        line(tf,pt_,12.5,color=GRAPHITE,ls=1.2,sa=6)
card(s,LX,Inches(6.14),RW,Inches(0.58),fill=DEEP_NAVY,line=None)
tb,tf=textbox(s,LX+Inches(0.28),Inches(6.14),RW-Inches(0.56),Inches(0.58),anchor=MSO_ANCHOR.MIDDLE)
p=para(tf,first=True); p.space_after=Pt(0)
r=p.add_run(); set_run(r,"Sector-flexible, but not strategy-neutral.  ",13,HEAD,WHITE)
r=p.add_run(); set_run(r,"Every investment must have an identifiable value opportunity, a credible "
                        "value-creation plan and the capabilities required to execute it.",12.5,BODY,WHITE_D)
pg+=1; furniture(s,pg)
notes(s,"“The Aravest Way defines the standards by which we invest. Within those standards, we remain "
        "flexible in where we seek opportunities. We do not invest simply because an asset falls within a "
        "preferred sector. We invest where we can identify value, establish a credible plan to realise that "
        "value and assemble all the capabilities required for execution.”")

# ============================================================ 7 · §05(i) TRACK RECORD — lifecycle
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"05 · Building the post-SMFL track record")
title(s,LX,Inches(0.80),"A credible track record is built through the full investment lifecycle, not through acquisitions alone.")
tb,tf=textbox(s,LX,Inches(1.66),RW,Inches(0.6))
line(tf,"At Aravest’s current stage, third-party capital is likely to be opportunity-led before it becomes "
        "strategy-led or discretionary. Investors will first seek evidence that Aravest can source, execute, "
        "manage and complete investments successfully under SMFL ownership.",
     12.5,color=GRAPHITE,first=True,ls=1.24,sa=0)
steps=["Recognise and underwrite value","Secure and execute","Manage and create value",
       "Deliver and realise outcomes","Repeat across a strategy"]
n=len(steps); sw=Inches(2.12); gapx=(RW-sw*n)/(n-1); sy=Inches(2.62)
for i,st in enumerate(steps):
    x=LX+i*(sw+gapx)
    emph=(i==n-1)
    card(s,x,sy,sw,Inches(1.42),fill=(TEAL_T if emph else WHITE),line=(TEAL_B if emph else GRAPH_B))
    tb,tf=textbox(s,x+Inches(0.16),sy+Inches(0.15),sw-Inches(0.32),Inches(1.15))
    line(tf,f"{i+1:02d}",10.5,color=(TEAL if emph else SLATE),bold=True,first=True,track=1.2,sa=4)
    line(tf,st,13,font=HEAD,color=NAVY,ls=1.08,sa=0)
    if i<n-1:
        tb,tf=textbox(s,x+sw,sy+Inches(0.5),gapx,Inches(0.4),anchor=MSO_ANCHOR.MIDDLE)
        line(tf,"→",15,color=GRAPHITE,align=PP_ALIGN.CENTER,first=True,sa=0)
conclusion_band(s,LX,Inches(4.55),RW,"The objective:",
                "move investor confidence from the individual opportunity, to the repeat relationship, "
                "and ultimately to the Aravest strategy.")
tb,tf=textbox(s,LX,Inches(5.48),RW,Inches(0.8))
line(tf,"The track record Aravest needs is not simply a record of acquisitions: it is a record of judgement, "
        "execution, stewardship, performance, realisation and repeatability under SMFL ownership — the six "
        "forms of evidence set out on the next page.",12.5,color=GRAPHITE,first=True,ls=1.26,sa=0)
pg+=1; furniture(s,pg)
notes(s,"“The track record we need to build is not simply a record of acquisitions. It is a record of "
        "judgement, execution, stewardship, performance, realisation and repeatability under SMFL ownership. "
        "As that evidence accumulates, investor confidence can move from individual opportunities to repeat "
        "participation and ultimately to broader strategy-level capital.”")

# ============================================================ 8 · §05(ii) WHAT INVESTORS NEED TO SEE
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"05 · Building the post-SMFL track record · Evidence")
title(s,LX,Inches(0.80),"What investors need to see.")
proofs=[("Judgement","Independent sourcing, disciplined underwriting and evidence that Aravest can recognise value rather than merely participate in transactions."),
        ("Execution","Ability to complete transactions, implement business plans and work effectively with partners under the current sponsor."),
        ("Stewardship","Responsible asset management, risk management, governance and communication through changing market conditions."),
        ("Performance","Evidence that the investment thesis translates into value creation during the hold period."),
        ("Realisation","Evidence that created value can be converted into actual investor returns."),
        ("Repeatability","A body of evidence across more than one transaction, capable of supporting confidence in a repeatable Aravest strategy.")]
cwp=Inches(3.87); chp=Inches(1.90); gx=Inches(0.16); gy=Inches(0.16)
for i,(h,b) in enumerate(proofs):
    x=LX+(i%3)*(cwp+gx); y=Inches(1.62)+(i//3)*(chp+gy)
    emph=(i==5)
    card(s,x,y,cwp,chp,fill=(TEAL_T if emph else WHITE),line=(TEAL_B if emph else GRAPH_B))
    tb,tf=textbox(s,x+Inches(0.22),y+Inches(0.16),cwp-Inches(0.44),chp-Inches(0.32))
    p=para(tf,first=True); p.space_after=Pt(4)
    r=p.add_run(); set_run(r,f"{i+1:02d}  ",10.5,BODY,(TEAL if emph else SLATE),bold=True,track=1.0)
    r=p.add_run(); set_run(r,h,14,HEAD,NAVY)
    line(tf,b,12,color=GRAPHITE,ls=1.2,sa=0)
conclusion_band(s,LX,Inches(5.86),RW,"As the evidence accumulates,","investor confidence moves from "
                "individual opportunities to repeat participation and ultimately to broader strategy-level capital.")
pg+=1; furniture(s,pg)
notes(s,"“The track record we need to build is not simply a record of acquisitions. It is a record of "
        "judgement, execution, stewardship, performance, realisation and repeatability under SMFL ownership.”")

# ============================================================ 9 · §06 TWO PARALLEL PATHWAYS
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"06 · Two parallel pathways")
title(s,LX,Inches(0.80),"Aravest will build the platform through two complementary pathways.")
prow=[("Primary purpose",
       "Build multiple proof points and a repeatable post-SMFL investment record.",
       "Accelerate AUM, institutional relevance and market visibility — each opportunity presented to the Board for decision case-by-case."),
      ("Typical opportunity",
       "Selected small and medium transactions across repeatable themes.",
       "Selected large transactions capable of creating meaningful scale."),
      ("Capital profile",
       "Existing US$300 million support can be diversified across several investments.",
       "May require materially greater transaction-specific capital."),
      ("Risk profile",
       "More diversified, with lower single-asset concentration.",
       "Higher single-asset concentration and liquidity exposure."),
      ("Expected AUM effect",
       "Gradual and potentially uneven.",
       "Potential step-change growth.")]
CY=Inches(1.54); CH=Inches(4.42); CWD=Inches(5.80); X2=Inches(6.83)
off=[Inches(1.04),Inches(1.90),Inches(2.62),Inches(3.30),Inches(3.94)]
for X,name,role,acc,fillc,bord in [
    (LX,"Pathway 1 — Diversified Track Record Building","The principal programme — builds the record",TEAL,TEAL_T,TEAL_B),
    (X2,"Pathway 2 — Institutional-Scale Opportunities","Case-by-case — can accelerate scale",STEEL,STEEL_T,STEEL_B)]:
    card(s,X,CY,CWD,CH,fill=fillc,line=bord)
    rect(s,X+Inches(0.22),CY,CWD-Inches(0.44),Pt(2.5),fill=acc)
    tb,tf=textbox(s,X+Inches(0.26),CY+Inches(0.14),CWD-Inches(0.52),Inches(0.85))
    line(tf,name,14.5,font=HEAD,color=NAVY,first=True,ls=1.04,sa=3)
    line(tf,role.upper(),9,color=acc,bold=True,track=1.1,sa=0)
    vals=[r[1] if X==LX else r[2] for r in prow]
    for o,(lab,v) in zip(off,[(r[0],v) for r,v in zip(prow,vals)]):
        tb,tf=textbox(s,X+Inches(0.26),CY+o,CWD-Inches(0.52),Inches(0.85))
        line(tf,lab.upper(),9,color=GRAPHITE,bold=True,first=True,track=0.8,sa=2)
        line(tf,v,12.5,color=GRAPHITE,ls=1.13,sa=0)
card(s,LX,Inches(6.14),RW,Inches(0.58),fill=DEEP_NAVY,line=None)
tb,tf=textbox(s,LX+Inches(0.28),Inches(6.14),RW-Inches(0.56),Inches(0.58),anchor=MSO_ANCHOR.MIDDLE)
p=para(tf,first=True); p.space_after=Pt(0)
r=p.add_run(); set_run(r,"RUN IN PARALLEL   ",10,BODY,WHITE_D,bold=True,track=1.4)
r=p.add_run(); set_run(r,"Pathway 1 builds the record",13,BODY,TEAL_LT,bold=True)
r=p.add_run(); set_run(r,";  ",13,BODY,WHITE_D)
r=p.add_run(); set_run(r,"Pathway 2 can accelerate scale",13,BODY,STEEL_LT,bold=True)
r=p.add_run(); set_run(r,".",13,BODY,WHITE_D)
pg+=1; furniture(s,pg)
notes(s,"“The two pathways are intended to run in parallel. Diversified Track Record Building is the "
        "principal programme for establishing the investment record and repeatability required for Aravest’s "
        "long-term franchise. Institutional-Scale Opportunities provide the possibility of accelerating AUM "
        "and institutional relevance when suitable opportunities arise. Each such opportunity will be brought "
        "to the Board for consideration and decision on a case-by-case basis.”")

# ============================================================ 10 · §07 PATHWAY 1
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"07 · Pathway 1 · Diversified Track Record Building",color=TEAL)
title(s,LX,Inches(0.80),"Use the existing US$300 million support across selected small and medium transactions to build multiple proof points and diversify risk.")
tb,tf=textbox(s,LX,Inches(1.90),RW,Inches(0.6))
line(tf,"The primary objective is to establish a diversified body of post-SMFL investment evidence. Capital "
        "recycling remains important because the sponsor capital is finite, but the immediate priority is to "
        "create the investment record from which longer-term capital efficiency can develop.",
     12.5,color=GRAPHITE,first=True,ls=1.24,sa=0)
steps=["Execute several investments","Build diversified proof","Create and realise value",
       "Recycle at asset or portfolio level","Redeploy and repeat"]
n=len(steps); sw=Inches(2.12); gapx=(RW-sw*n)/(n-1); sy=Inches(2.90)
for i,st in enumerate(steps):
    x=LX+i*(sw+gapx)
    card(s,x,sy,sw,Inches(1.42),fill=TEAL_T,line=TEAL_B,shadow=(i==0))
    tb,tf=textbox(s,x+Inches(0.16),sy+Inches(0.15),sw-Inches(0.32),Inches(1.15))
    line(tf,f"{i+1:02d}",10.5,color=TEAL,bold=True,first=True,track=1.2,sa=4)
    line(tf,st,13,font=HEAD,color=NAVY,ls=1.08,sa=0)
    if i<n-1:
        tb,tf=textbox(s,x+sw,sy+Inches(0.5),gapx,Inches(0.4),anchor=MSO_ANCHOR.MIDDLE)
        line(tf,"→",15,color=GRAPHITE,align=PP_ALIGN.CENTER,first=True,sa=0)
tb,tf=textbox(s,LX,Inches(4.85),RW,Inches(0.6))
line(tf,"For each investment, capital may be recycled at the individual asset level or after aggregation "
        "into a larger portfolio — the two routes compared on the next page.",
     12.5,color=GRAPHITE,first=True,ls=1.24,sa=0)
conclusion_band(s,LX,Inches(5.72),RW,"Finite capital, compounding proof.",
                "Several diversified investments convert one pool of sponsor support into a repeatable record.")
pg+=1; furniture(s,pg)
notes(s,"“The first pathway is designed to use the existing capital support to build several proof points "
        "while diversifying risk. For each investment, we will consider whether capital is best recycled at "
        "the individual asset level or after aggregation into a larger portfolio. Asset-level recycling may "
        "be faster; portfolio aggregation may be more relevant to institutional investors but may require more time.”")

# ============================================================ 11 · §07/§08 RECYCLING ROUTES (arch slide 8)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"08 · Pathway 1 · Two routes to capital recycling",color=TEAL)
title(s,LX,Inches(0.80),"Asset-level recycling releases capital earlier; portfolio aggregation builds institutional scale.")
HY=Inches(1.64)
tcols=[(Inches(1.02),Inches(2.2),""),(Inches(3.40),Inches(4.45),"Asset-level recycling"),
       (Inches(8.10),Inches(4.4),"Portfolio-level recycling through aggregation")]
for x,w,h in tcols[1:]:
    tb,tf=textbox(s,x,HY,w,Inches(0.3))
    line(tf,h.upper(),9.5,color=GRAPHITE,bold=True,first=True,track=0.9,sa=0)
rect(s,LX,HY+Inches(0.32),RW,Pt(1.5),fill=NAVY)
trows=[("Approach","Sell, recapitalise or introduce third-party capital into an individual asset.",
        "Combine related assets into a coherent portfolio before introducing third-party capital."),
       ("Timing","Potentially earlier where there is sufficient demand for the individual asset.",
        "Usually requires more time to assemble sufficient scale."),
       ("Investor relevance","The individual ticket may be too small for larger institutions.",
        "The portfolio can provide a more meaningful ticket and greater diversification."),
       ("Strategic benefit","Releases capital earlier and creates a realised proof point.",
        "Creates a scalable strategy or platform, rather than a single investment."),
       ("Sponsor capital duration","Potentially shorter.",
        "Potentially longer while the portfolio is assembled."),
       ("AUM implication","A full disposal may reduce AUM; a partial sell-down may retain it.",
        "Can create larger and more durable portfolio-level AUM.")]
ry=HY+Inches(0.42)
for i,(lab,v1,v2) in enumerate(trows):
    if i>0: hrule(s,LX,ry,RW,weight=0.75,color=MIST)
    pathway_marker(s,LX,ry+Inches(0.10),Inches(0.48),TEAL)
    tb,tf=textbox(s,Inches(1.02),ry+Inches(0.10),Inches(2.2),Inches(0.62))
    line(tf,lab.upper(),9,color=GRAPHITE,bold=True,first=True,track=0.7,ls=1.1,sa=0)
    for (x,w,_),v in zip(tcols[1:],[v1,v2]):
        tb,tf=textbox(s,x,ry+Inches(0.08),w,Inches(0.62))
        line(tf,v,12,color=GRAPHITE,first=True,ls=1.14,sa=0)
    ry+=Inches(0.68)
rect(s,LX,ry,RW,Pt(1.0),fill=NAVY)
tb,tf=textbox(s,LX,ry+Inches(0.10),RW,Inches(0.45))
line(tf,"Asset-level recycling may be faster; portfolio aggregation may be more relevant to institutional "
        "investors but may require more time.",12,color=GRAPHITE,first=True,ls=1.2,sa=0)
pg+=1; furniture(s,pg)
notes(s,"“For each investment, we will consider whether capital is best recycled at the individual asset "
        "level or after aggregation into a larger portfolio. Asset-level recycling may be faster; portfolio "
        "aggregation may be more relevant to institutional investors but may require more time.”")

# ============================================================ 12 · §08 PATHWAY 2 (arch slide 9)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"09 · Pathway 2 · Institutional-Scale Opportunities",color=STEEL)
title(s,LX,Inches(0.80),"Continue to source selected large opportunities that may materially accelerate AUM, institutional relevance and market visibility.")
tb,tf=textbox(s,LX,Inches(1.86),RW,Inches(0.62))
line(tf,"Institutional-scale opportunities are not a replacement for the diversified pathway; they serve a "
        "different strategic purpose. One large transaction can create an increase in AUM that would "
        "otherwise require several years of smaller transactions, while providing a more meaningful "
        "opportunity for large institutional investors.",12.5,color=GRAPHITE,first=True,ls=1.24,sa=0)
CY=Inches(2.78); CH=Inches(2.60); CWD=Inches(5.80); X2=Inches(6.83)
for X,tag_,acc,fillc,bord,points in [
    (LX,"Strategic benefits",STEEL,STEEL_T,STEEL_B,
     ["Faster AUM growth — a single transaction can create a material increase in AUM.",
      "Greater institutional relevance — meaningful ticket sizes for institutional investors.",
      "Stronger external profile — visible execution of significant investments under SMFL ownership.",
      "Accelerated platform development — visibility supports future fundraising, partnerships and recognition."]),
    (X2,"Capital and risk implications",None,WHITE,GRAPH_B,
     ["Higher capital requirement — may be materially beyond the ordinary diversified programme.",
      "Higher concentration — more capital exposed to one asset, market and business plan.",
      "Greater liquidity and holding exposure — the full investment may need to be held for longer than initially expected.",
      "Board consideration — each opportunity presented separately, to determine whether the strategic benefits justify the capital and concentration involved."])]:
    card(s,X,CY,CWD,CH,fill=fillc,line=bord)
    rect(s,X+Inches(0.22),CY,CWD-Inches(0.44),Pt(2.5),fill=(acc or GRAPH_B))
    tb,tf=textbox(s,X+Inches(0.26),CY+Inches(0.16),CWD-Inches(0.52),CH-Inches(0.32))
    line(tf,tag_.upper(),9.5,color=(acc or GRAPHITE),bold=True,first=True,track=1.2,sa=6)
    for pt_ in points:
        line(tf,pt_,12,color=GRAPHITE,ls=1.18,sa=6)
conclusion_band(s,LX,Inches(5.66),RW,"Not part of the ordinary programme.",
                "Each opportunity is presented separately to the Board — investment merits, strategic "
                "relevance, capital requirement and risk profile — for decision case-by-case.")
tb,tf=textbox(s,LX,Inches(6.50),RW,Inches(0.4))
line(tf,"A meaningful ticket size does not necessarily mean external capital is introduced more quickly — "
        "the capital required is also larger. The principal strategic value is the potential to accelerate "
        "AUM growth and strengthen Aravest’s institutional profile.",10.5,color=GRAPHITE,first=True,ls=1.2,sa=0)
pg+=1; furniture(s,pg)
notes(s,"“The second pathway preserves Aravest’s ability to pursue opportunities that can materially change "
        "the scale and visibility of the platform. These transactions may be more relevant to large "
        "institutional investors, but they also involve a materially different capital and concentration "
        "profile. Management will therefore bring each opportunity to the Board separately for consideration and decision.”")

# ============================================================ 13 · §09(i) WAREHOUSING — the timing gap
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"10 · Warehousing as an execution enabler")
title(s,LX,Inches(0.80),"Warehousing bridges the timing gap between securing a transaction and forming third-party capital.")
tb,tf=textbox(s,LX,Inches(1.66),RW,Inches(0.4))
line(tf,"In principle, transaction closing and third-party capital formation can be matched. In practice, "
        "the two timetables often do not align.",12.5,color=GRAPHITE,first=True,ls=1.24,sa=0)
CY=Inches(2.30); CH=Inches(2.10); CWD=Inches(5.80); X2=Inches(6.83)
for X,tag_,h,b in [
    (LX,"INVESTOR TIMETABLE","Investors generally require a specific and sufficiently secured opportunity",
     "Institutional investors need time to assess the asset, business plan, manager, structure and risk "
     "before committing capital. Many will not provide a firm commitment until the opportunity is "
     "sufficiently advanced or secured."),
    (X2,"TRANSACTION TIMETABLE","Sellers require certainty and speed",
     "Competitive transactions require committed funding, execution certainty and the ability to close "
     "within the seller’s timetable — often before an institutional fundraising process can be completed.")]:
    card(s,X,CY,CWD,CH,fill=WHITE,line=GRAPH_B)
    rect(s,X+Inches(0.22),CY,CWD-Inches(0.44),Pt(2.5),fill=GRAPH_B)
    tb,tf=textbox(s,X+Inches(0.26),CY+Inches(0.17),CWD-Inches(0.52),CH-Inches(0.34))
    line(tf,tag_,9.5,color=GRAPHITE,bold=True,first=True,track=1.2,sa=5)
    line(tf,h,14,font=HEAD,color=NAVY,sa=6,ls=1.08)
    line(tf,b,12.5,color=GRAPHITE,ls=1.22,sa=0)
card(s,LX,Inches(4.66),RW,Inches(0.74),fill=DEEP_NAVY,line=None)
tb,tf=textbox(s,LX+Inches(0.28),Inches(4.66),RW-Inches(0.56),Inches(0.74),anchor=MSO_ANCHOR.MIDDLE)
line(tf,"Without the ability to bridge this timing gap, Aravest may be unable to secure opportunities "
        "at the point they are available.",14,font=HEAD,color=WHITE,first=True,ls=1.22,sa=0)
tb,tf=textbox(s,LX,Inches(5.66),RW,Inches(0.85))
line(tf,"This has a direct bearing on Aravest’s long-term development: if the platform executes too few "
        "transactions, it cannot build the post-SMFL track record required by institutional investors — and "
        "a limited track record in turn makes it harder to attract third-party capital for future opportunities.",
     12.5,color=GRAPHITE,first=True,ls=1.26,sa=0)
pg+=1; furniture(s,pg)
notes(s,"“In theory, investor commitments and transaction closing can be aligned. In practice, the processes "
        "often move on different timetables. Warehousing provides the bridge. Without that bridge, Aravest "
        "may execute too few transactions to establish the post-SMFL record required for future fundraising.”")

# ============================================================ 14 · §09(ii) WAREHOUSING — the chain
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"10 · Warehousing as an execution enabler · Why it matters")
title(s,LX,Inches(0.80),"Execution builds the record; the record supports long-term capital formation.")
CY=Inches(1.66); CH=Inches(2.10); CWD=Inches(5.80); X2=Inches(6.83)
for X,tag_,h,b,fillc,bord,acc in [
    (LX,"WITHOUT WAREHOUSING","The record cannot form",
     "Limited advance third-party commitments → fewer secured transactions → insufficient post-SMFL proof "
     "→ continued difficulty attracting third-party capital.",WHITE,GRAPH_B,GRAPHITE),
    (X2,"WITH WAREHOUSING","Execution builds the record",
     "Secure and execute transactions → demonstrate the full investment lifecycle → establish investor "
     "confidence → introduce or raise third-party capital → repeat.",TEAL_T,TEAL_B,TEAL)]:
    card(s,X,CY,CWD,CH,fill=fillc,line=bord)
    rect(s,X+Inches(0.22),CY,CWD-Inches(0.44),Pt(2.5),fill=acc)
    tb,tf=textbox(s,X+Inches(0.26),CY+Inches(0.17),CWD-Inches(0.52),CH-Inches(0.34))
    line(tf,tag_,9.5,color=(TEAL if acc==TEAL else GRAPHITE),bold=True,first=True,track=1.2,sa=5)
    line(tf,h,14,font=HEAD,color=NAVY,sa=6,ls=1.08)
    line(tf,b,12.5,color=GRAPHITE,ls=1.24,sa=0)
tb,tf=textbox(s,LX,Inches(4.05),RW,Inches(0.85))
line(tf,"Warehousing is relevant to both pathways. For Diversified Track Record Building, the existing "
        "US$300 million support can be spread across several small and medium investments, allowing risk to "
        "be diversified. For Institutional-Scale Opportunities, the capital requirement and single-asset "
        "concentration are materially greater.",12.5,color=GRAPHITE,first=True,ls=1.26,sa=0)
card(s,LX,Inches(5.20),RW,Inches(1.0),fill=DEEP_NAVY,line=None)
tb,tf=textbox(s,LX+Inches(0.28),Inches(5.20),RW-Inches(0.56),Inches(1.0),anchor=MSO_ANCHOR.MIDDLE)
p=para(tf,first=True); p.space_after=Pt(0); p.line_spacing=1.3
r=p.add_run(); set_run(r,"Warehousing enables transaction execution.  ",13.5,HEAD,WHITE)
r=p.add_run(); set_run(r,"Transaction execution builds the track record.  ",13.5,HEAD,TEAL_LT)
r=p.add_run(); set_run(r,"The track record supports long-term third-party capital formation.",13.5,HEAD,WHITE)
pg+=1; furniture(s,pg)
notes(s,"“In theory, investor commitments and transaction closing can be aligned. In practice, the processes "
        "often move on different timetables. Warehousing provides the bridge.”")

# ============================================================ 15 · §10 EXPECTED AUM PROFILE (arch 11)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"11 · Expected AUM profile")
title(s,LX,Inches(0.80),"The two pathways are expected to produce different AUM profiles.")
hrule(s,LX,Inches(1.54),RW,weight=0.75,color=MIST)
tb,tf=textbox(s,LX,Inches(1.66),RW,Inches(0.40),anchor=MSO_ANCHOR.MIDDLE)
line(tf,"Closing AUM  =  Opening AUM  +  New investments  −  Realisations  ±  Valuation and FX movements",
     14.5,font=HEAD,color=NAVY,align=PP_ALIGN.CENTER,first=True,sa=0)
hrule(s,LX,Inches(2.18),RW,weight=0.75,color=MIST)
AY=Inches(2.42); AH=Inches(3.90); CWD=Inches(5.80); X2=Inches(6.83)
def aum_card(X,title_,tc,heights,lo,hi=None,step=None,bullets=()):
    card(s,X,AY,CWD,AH,fill=WHITE,line=GRAPH_B)
    tb,tf=textbox(s,X+Inches(0.26),AY+Inches(0.16),CWD-Inches(0.52),Inches(0.4))
    line(tf,title_,14,font=HEAD,color=tc,first=True,ls=1.03,sa=0)
    bars(s,X+Inches(0.26),AY+Inches(1.78),CWD-Inches(0.52),heights,lo,fill_hi=hi,step_idx=step,maxh=0.95,bw=Inches(0.42))
    tb,tf=textbox(s,X+Inches(0.26),AY+Inches(1.92),CWD-Inches(0.52),Inches(1.9))
    first=True
    for b in bullets:
        p=para(tf,first=first); first=False
        p.space_after=Pt(4); p.line_spacing=1.16
        r=p.add_run(); set_run(r,"·  ",12,BODY,tc,bold=True)
        r=p.add_run(); set_run(r,b,12,BODY,GRAPHITE)
    line(tf,"Illustrative profile only — not a forecast.",8.5,color=SLATE,italic=True,sb=4,sa=0)
aum_card(LX,"Pathway 1 — Diversified Track Record Building",TEAL,
         [0.42,0.55,0.47,0.62,0.52,0.70,0.63],TEAL,
         bullets=["AUM growth is likely to be gradual and uneven.",
                  "AUM may remain flat where new investments broadly replace realised assets.",
                  "AUM may decline temporarily following successful disposals or sell-downs.",
                  "The platform may nevertheless improve through stronger realised returns, profitability, investor confidence and repeatability."])
aum_card(X2,"Pathway 2 — Institutional-Scale Opportunities",STEEL,
         [0.36,0.38,0.40,0.93,0.95,1.0,1.0],STEEL_MID,hi=STEEL,step=3,
         bullets=["Potential for a material or step-change increase in AUM.",
                  "Creates more meaningful institutional ticket sizes.",
                  "Strengthens visibility and fundraising credibility.",
                  "May accelerate the pathway from proof-building to institutional scale."])
tb,tf=textbox(s,LX,Inches(6.48),RW,Inches(0.35))
line(tf,"Source: Locked Board Strategy Narrative v8. Financial figures to be populated by Finance before "
        "Board circulation.",8.5,color=SLATE,italic=True,first=True,sa=0)
pg+=1; furniture(s,pg)
notes(s,"“Under the diversified pathway, AUM may grow gradually, remain flat or decline temporarily as "
        "investments are realised and capital is recycled. Institutional-scale opportunities provide the "
        "potential to change that AUM profile, although they involve a materially different capital and "
        "concentration requirement.”")

# ============================================================ 16 · §11 CONRAD SEOUL (arch 12)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"12 · Conrad Seoul illustration")
title(s,LX,Inches(0.80),"Conrad Seoul illustrates the sequencing of warehousing, execution and institutional capital formation.")
tb,tf=textbox(s,LX,Inches(1.66),RW,Inches(0.6))
line(tf,"Sponsor-supported capital enabled the transaction to be secured and completed. Following "
        "acquisition, Aravest brought in institutional investors, including GIC and M&G, allowing capital "
        "to be recycled while the platform retained the management relationship and strengthened its "
        "investment record.",12.5,color=GRAPHITE,first=True,ls=1.24,sa=0)
steps=["Secure opportunity","Warehouse with sponsor support","Execute and establish confidence",
       "Introduce institutional capital","Recycle capital and build proof"]
n=len(steps); sw=Inches(2.12); gapx=(RW-sw*n)/(n-1); sy=Inches(2.62)
for i,st in enumerate(steps):
    x=LX+i*(sw+gapx)
    emph=(i>=3)
    card(s,x,sy,sw,Inches(1.30),fill=(TEAL_T if emph else WHITE),line=(TEAL_B if emph else GRAPH_B))
    tb,tf=textbox(s,x+Inches(0.16),sy+Inches(0.13),sw-Inches(0.32),Inches(1.05))
    line(tf,f"{i+1:02d}",10,color=(TEAL if emph else SLATE),bold=True,first=True,track=1.2,sa=3)
    line(tf,st,12.5,font=HEAD,color=NAVY,ls=1.08,sa=0)
    if i<n-1:
        tb,tf=textbox(s,x+sw,sy+Inches(0.45),gapx,Inches(0.4),anchor=MSO_ANCHOR.MIDDLE)
        line(tf,"→",14,color=GRAPHITE,align=PP_ALIGN.CENTER,first=True,sa=0)
CY2=Inches(4.20); CH2=Inches(2.25); CWD=Inches(5.80); X2=Inches(6.83)
for X,tag_,acc,fillc,bord,points in [
    (LX,"What the case demonstrates",TEAL,TEAL_T,TEAL_B,
     ["Warehousing can provide the transaction certainty required to secure a significant opportunity.",
      "A secured and executed transaction gives institutional investors a more tangible basis for participation.",
      "Subsequent institutional capital can release sponsor capital and strengthen the post-SMFL track record.",
      "The management relationship and institutional credibility can extend beyond the initial capital deployment."]),
    (X2,"How the example should be understood",None,WHITE,GRAPH_B,
     ["The sequence demonstrates an available model, not an assured timetable for every transaction.",
      "The sponsor may need to retain the investment for longer if external capital takes time to form.",
      "The case illustrates why transaction execution can precede, rather than follow, institutional capital formation."])]:
    card(s,X,CY2,CWD,CH2,fill=fillc,line=bord)
    rect(s,X+Inches(0.22),CY2,CWD-Inches(0.44),Pt(2.5),fill=(acc or GRAPH_B))
    tb,tf=textbox(s,X+Inches(0.26),CY2+Inches(0.15),CWD-Inches(0.52),CH2-Inches(0.3))
    line(tf,tag_.upper(),9.5,color=(acc or GRAPHITE),bold=True,first=True,track=1.1,sa=6)
    for pt_ in points:
        line(tf,pt_,11.5,color=GRAPHITE,ls=1.16,sa=5)
pg+=1; furniture(s,pg)
notes(s,"“Conrad Seoul is a useful illustration of the model. Sponsor-supported capital provided acquisition "
        "certainty. Once the transaction was secured and execution was visible, institutional capital was "
        "introduced. This allowed capital to be recycled and gave Aravest a stronger proof point under SMFL ownership.”")

# ============================================================ 17 · §12 CURRENT PIPELINE (arch 13)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"13 · Current pipeline")
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
line(tf,"Private credit is excluded as a core Aravest growth strategy, as it is an agreed SMDAM strategy "
        "with Aravest providing support where relevant. Transaction names, figures and status to be "
        "refreshed by the relevant transaction teams before Board circulation.",
     9,color=SLATE,italic=True,first=True,ls=1.22,sa=0)
pg+=1; furniture(s,pg)
notes(s,"“The pipeline illustrates how the strategy translates into current opportunities. Some transactions "
        "provide diversified proof points and portfolio building blocks. Others may materially change the "
        "scale of the platform. Together, they show how the two pathways can develop in parallel.”")

# ============================================================ 18 · §13 2027 FOCUS (arch 14)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"14 · 2027 investment focus")
title(s,LX,Inches(0.80),"Our near-term focus combines established capabilities with selected areas of current market opportunity.")
B1,B1W=Inches(1.02),Inches(3.3); B2,B2W=Inches(4.6),Inches(3.6); B3,B3W=Inches(8.5),Inches(3.9)
HY=Inches(1.66)
for x,w,h in [(B1,B1W,"Focus"),(B2,B2W,"2027 strategic role"),(B3,B3W,"How we will approach them")]:
    tb,tf=textbox(s,x,HY,w,Inches(0.3))
    line(tf,h.upper(),9.5,color=GRAPHITE,bold=True,first=True,track=1.1,sa=0)
bands=[("Established sectors","Office, logistics and selective retail or mixed-use",None,WHITE,GRAPH_B,
        "Remain the principal investment base, supported by Aravest’s existing experience, local market "
        "knowledge and asset-management capabilities.",
        "Prioritise opportunities where repositioning, lease-up, AEI, redevelopment or market dislocation "
        "can create a clear and defensible value proposition."),
       ("Current target priorities","Hospitality and living",TEAL,TEAL_T,TEAL_B,
        "Focus origination and capability development where current demand, market conditions and Aravest’s "
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
    line(tf,role,12,color=GRAPHITE,first=True,ls=1.16,sa=0)
    tb,tf=textbox(s,B3,ry+Inches(0.16),B3W,rh-Inches(0.32))
    line(tf,how,12,color=GRAPHITE,first=True,ls=1.16,sa=0)
    ry+=rh+Inches(0.14)
tb,tf=textbox(s,LX,ry+Inches(0.03),RW,Inches(0.5))
line(tf,"These priorities guide origination and capability development for 2027. They are not fixed capital "
        "allocations and may evolve with market conditions, investor demand and demonstrated investment outcomes.",
     11,color=GRAPHITE,first=True,ls=1.2,sa=0)
pg+=1; furniture(s,pg)
notes(s,"“For 2027, our principal focus will remain in sectors where we have established investment and "
        "asset-management experience, particularly office, logistics and selected retail or mixed-use "
        "opportunities. Hospitality and living will be current target priorities. Other sectors, including "
        "data centres, will be considered opportunistically where the investment case is compelling and the "
        "required specialist capability has been secured.”")

# ============================================================ 19 · §14 VALUE CREATION (arch 15)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"15 · How Aravest creates value")
title(s,LX,Inches(0.80),"Sector selection identifies where we invest; the value-creation plan determines why we invest.")
HY=Inches(1.72)
for x,w,h in [(Inches(1.02),Inches(3.6),"Value-creation playbook"),(Inches(5.0),Inches(7.6),"Typical application")]:
    tb,tf=textbox(s,x,HY,w,Inches(0.3))
    line(tf,h.upper(),9.5,color=GRAPHITE,bold=True,first=True,track=1.1,sa=0)
rect(s,LX,HY+Inches(0.30),RW,Pt(1.5),fill=NAVY)
plays=[("Repositioning and lease-up","Improve occupancy, tenant mix, rental performance and market positioning."),
       ("Asset enhancement and conversion","Undertake refurbishment, AEI, change of use or physical repositioning."),
       ("Development and redevelopment","Create value through ground-up development or material redevelopment where the development capability and risk controls are established."),
       ("Operational improvement","Improve performance through stronger management, branding, service delivery or specialist operating partners."),
       ("Market or capital dislocation","Invest where pricing, ownership constraints, refinancing pressure or capital scarcity create an attractive entry point."),
       ("Aggregation and portfolio formation","Combine related investments into portfolios or repeatable strategies capable of attracting institutional capital.")]
ry=HY+Inches(0.40)
for i,(k,v) in enumerate(plays):
    if i>0: hrule(s,LX,ry,RW,weight=0.75,color=MIST)
    tb,tf=textbox(s,Inches(1.02),ry+Inches(0.07),Inches(3.6),Inches(0.5))
    line(tf,k,12.5,font=HEAD,color=NAVY,first=True,ls=1.08,sa=0)
    tb,tf=textbox(s,Inches(5.0),ry+Inches(0.08),Inches(7.6),Inches(0.5))
    line(tf,v,12,color=GRAPHITE,first=True,ls=1.14,sa=0)
    ry+=Inches(0.52)
rect(s,LX,ry,RW,Pt(1.0),fill=NAVY)
GYY=ry+Inches(0.14)
card(s,LX,GYY,RW,Inches(1.04),fill=DEEP_NAVY,line=None)
tb,tf=textbox(s,LX+Inches(0.28),GYY+Inches(0.11),RW-Inches(0.56),Inches(0.85))
line(tf,"CAPABILITY COVERAGE IS AN INVESTMENT GATE",9,color=WHITE_D,bold=True,first=True,track=1.2,sa=4)
line(tf,"Aravest will proceed only where all capabilities required for origination, underwriting, financing, "
        "development, operations, asset management and realisation are covered internally or through secured "
        "partners. For capability-intensive activities — development, hospitality operations, data centres — "
        "the relevant partner should generally be identified and sufficiently secured before investment commitment.",
     11,color=WHITE,ls=1.18,sa=0)
tb,tf=textbox(s,LX,GYY+Inches(1.14),RW,Inches(0.4))
p=para(tf,first=True); p.space_after=Pt(0); p.line_spacing=1.15
r=p.add_run(); set_run(r,"Aravest does not need to perform every function internally. ",11.5,BODY,NAVY,bold=True)
r=p.add_run(); set_run(r,"It must ensure that the complete capability set is in place and remain accountable "
                        "for the investment outcome.",11.5,BODY,GRAPHITE)
pg+=1; furniture(s,pg)
notes(s,"“Our strategy is not defined by sector alone. For every opportunity, we must be able to explain "
        "where the value gap exists, how we intend to close that gap and who will execute each part of the "
        "business plan. Aravest does not need to perform every function internally, but we must ensure that "
        "the full capability set is in place and remain accountable for the investment outcome.”")

# ============================================================ 20 · §15(i) STRUCTURING STANDARD — structure
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"16 · Institutional structuring standard")
title(s,LX,Inches(0.80),"Every fund and investment must be structured to standards acceptable to institutional investors.")
tb,tf=textbox(s,LX,Inches(1.62),RW,Inches(0.42))
line(tf,"Investment discipline extends beyond asset selection to the legal, financing and governance "
        "structure through which capital is deployed and risk is contained.",
     12.5,color=GRAPHITE,first=True,ls=1.22,sa=0)
nodes=["Institutional investors and approved co-investors","Fund vehicle","Investment SPV / borrower","Underlying asset"]
n=len(nodes); nw=Inches(2.62); gapx=(RW-nw*n)/(n-1); nyy=Inches(2.28)
for i,nd in enumerate(nodes):
    x=LX+i*(nw+gapx)
    card(s,x,nyy,nw,Inches(1.02),fill=WHITE,line=GRAPH_B)
    tb,tf=textbox(s,x+Inches(0.14),nyy,nw-Inches(0.28),Inches(1.02),anchor=MSO_ANCHOR.MIDDLE)
    line(tf,nd,12.5,font=HEAD,color=NAVY,align=PP_ALIGN.CENTER,first=True,ls=1.1,sa=0)
    if i<n-1:
        tb,tf=textbox(s,x+nw,nyy+Inches(0.3),gapx,Inches(0.4),anchor=MSO_ANCHOR.MIDDLE)
        line(tf,"→",15,color=GRAPHITE,align=PP_ALIGN.CENTER,first=True,sa=0)
card(s,LX,Inches(3.62),RW,Inches(0.92),fill=GRAPH_T,line=GRAPH_B,shadow=False)
tb,tf=textbox(s,LX+Inches(0.26),Inches(3.62),RW-Inches(0.52),Inches(0.92),anchor=MSO_ANCHOR.MIDDLE)
line(tf,"RISK AND LIABILITIES ARE GENERALLY RING-FENCED WITHIN THE RELEVANT FUND AND ASSET-LEVEL STRUCTURE",
     9,color=NAVY,bold=True,first=True,track=0.9,sa=4)
line(tf,"Financing should generally have recourse only to the relevant borrower, secured assets and "
        "expressly agreed credit support.",12.5,color=GRAPHITE,ls=1.2,sa=0)
tris=["Committed capital is exposed to investment performance",
      "Wider fund and asset liabilities are ring-fenced",
      "Manager or shareholder recourse is not automatic"]
tw_=Inches(3.85); tgap=(RW-tw_*3)/2; tyy=Inches(4.80)
for i,t in enumerate(tris):
    x=LX+i*(tw_+tgap)
    card(s,x,tyy,tw_,Inches(0.86),fill=DEEP_NAVY,line=None,shadow=False)
    tb,tf=textbox(s,x+Inches(0.2),tyy,tw_-Inches(0.4),Inches(0.86),anchor=MSO_ANCHOR.MIDDLE)
    line(tf,t,12.5,color=WHITE,align=PP_ALIGN.CENTER,first=True,ls=1.15,sa=0)
tb,tf=textbox(s,LX,Inches(5.92),RW,Inches(0.8))
line(tf,"Where Aravest or SMFL has separately approved an equity or co-investment commitment, that committed "
        "capital is at risk. This does not mean that the wider liabilities of the fund or investment "
        "automatically become liabilities of Aravest or SMFL.",12.5,color=GRAPHITE,first=True,ls=1.26,sa=0)
pg+=1; furniture(s,pg)
notes(s,"“Our funds and investments should be structured in accordance with standards expected by "
        "institutional investors. The relevant fund and asset-level vehicles contain the investment risks and "
        "liabilities, while financing is generally non-recourse or limited recourse to the relevant borrower "
        "and secured assets.”")

# ============================================================ 21 · §15(ii) STANDARDS TABLE + EXCEPTIONS
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=WHITE)
kicker(s,LX,Inches(0.48),"16 · Institutional structuring standard · The standards")
title(s,LX,Inches(0.80),"Six standards applied to every fund and investment.")
HY=Inches(1.52)
for x,w,h in [(Inches(1.02),Inches(3.4),"Institutional standard"),(Inches(4.8),Inches(7.8),"Aravest approach")]:
    tb,tf=textbox(s,x,HY,w,Inches(0.3))
    line(tf,h.upper(),9.5,color=GRAPHITE,bold=True,first=True,track=1.1,sa=0)
rect(s,LX,HY+Inches(0.30),RW,Pt(1.5),fill=NAVY)
stds=[("Ring-fenced structure","Assets, liabilities and obligations are generally contained within the relevant fund, investment vehicle and asset-level entities."),
      ("Non-recourse or limited-recourse financing","Financing should generally have recourse only to the relevant borrower, secured assets and expressly agreed transaction-level credit support."),
      ("Defined investor exposure","Investors’ exposure is generally limited to their committed capital and customary obligations under the applicable fund documents."),
      ("No automatic manager or shareholder recourse","The role of Aravest as manager, or SMFL as shareholder, does not by itself create recourse to either party."),
      ("Institutional governance","Each structure should provide appropriate decision rights, reserved matters, conflicts management, reporting, valuation and oversight."),
      ("Responsible capital structure","Leverage, liquidity, risk allocation and the route to capital recycling or exit should be appropriate to the investment strategy.")]
ry=HY+Inches(0.40)
for i,(k,v) in enumerate(stds):
    if i>0: hrule(s,LX,ry,RW,weight=0.75,color=MIST)
    tb,tf=textbox(s,Inches(1.02),ry+Inches(0.07),Inches(3.4),Inches(0.55))
    line(tf,k,12,font=HEAD,color=NAVY,first=True,ls=1.08,sa=0)
    tb,tf=textbox(s,Inches(4.8),ry+Inches(0.08),Inches(7.8),Inches(0.55))
    line(tf,v,11.5,color=GRAPHITE,first=True,ls=1.14,sa=0)
    ry+=Inches(0.60)
rect(s,LX,ry,RW,Pt(1.0),fill=NAVY)
GYY=ry+Inches(0.14)
card(s,LX,GYY,RW,Inches(1.06),fill=DEEP_NAVY,line=None)
tb,tf=textbox(s,LX+Inches(0.28),GYY+Inches(0.12),RW-Inches(0.56),Inches(0.85))
line(tf,"EXCEPTIONS MUST BE EXPLICIT AND SEPARATELY APPROVED",9,color=WHITE_D,bold=True,first=True,track=1.2,sa=4)
line(tf,"Any guarantee, keepwell, completion support, cost-overrun undertaking, indemnity or other manager- "
        "or shareholder-level obligation must be specifically identified, assessed, quantified and expressly "
        "approved through the applicable governance process.",11.5,color=WHITE,ls=1.2,sa=0)
pg+=1; furniture(s,pg)
notes(s,"“Where an investor, Aravest or SMFL commits equity, that approved capital is exposed to the "
        "performance of the investment. This does not mean that the wider liabilities of the fund or asset "
        "automatically become liabilities of the manager or shareholder. Any additional manager- or "
        "shareholder-level support must be made explicit and separately approved.”")

# ============================================================ 22 · CLOSING SYNTHESIS (dark)
s=add_slide(prs)
rect(s,0,0,SW,SH,fill=DEEP_NAVY)
tb,tf=textbox(s,LX,Inches(0.52),Inches(9),Inches(0.28))
line(tf,"The v8 proposition",10,color=WHITE_D,bold=True,first=True,track=1.6,caps=True,sa=0)
title(s,LX,Inches(0.86),"One coherent proposition for Aravest’s next phase.",color=WHITE)
card(s,LX,Inches(2.0),RW,Inches(3.1),fill=NAVY_CARD_L,line=NAVY_CARD_B,shadow=False)
tb,tf=textbox(s,LX+Inches(0.34),Inches(2.28),RW-Inches(0.68),Inches(2.6))
line(tf,"Aravest is values-led in how it invests and value-focused in where it deploys. It will remain "
        "sector-flexible within a defined 2027 investment focus, pursue opportunities only where there is a "
        "clear value-creation plan and complete capability coverage, and structure every fund and investment "
        "to institutional standards.",15,color=WHITE,first=True,ls=1.4,sa=10)
line(tf,"Committed equity is exposed to investment performance, but wider liabilities are generally "
        "ring-fenced, with no automatic recourse to Aravest as manager or SMFL as shareholder.",
     15,color=WHITE,ls=1.4,sa=0)
tb,tf=textbox(s,LX,Inches(5.5),RW,Inches(0.4))
p=para(tf,first=True); p.space_after=Pt(0)
r=p.add_run(); set_run(r,"Pathway 1 builds the record",12.5,BODY,TEAL_LT,bold=True)
r=p.add_run(); set_run(r,"   ·   ",12.5,BODY,WHITE_D)
r=p.add_run(); set_run(r,"Pathway 2 can accelerate scale",12.5,BODY,STEEL_LT,bold=True)
pg+=1; furniture(s,pg,dark=True)
notes(s,"For discussion. The v8 proposition in one paragraph — the locked strategic narrative’s closing synthesis.")

# ============================================================ 23 · DISCLAIMER (SG, verbatim)
D=load_disclaimers()
s=add_slide(prs)
pg+=1
disclaimer_slide(s,"Singapore",D["SG"],pg)
notes(s,"Important notice — wording preserved verbatim from the approved Aravest template; not to be amended "
        "without Legal and Compliance approval.")

# ============================================================ 24 · CLOSING
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

prs.save("Aravest_Next_Phase_Board_Discussion_Paper.pptx")
print("saved Aravest_Next_Phase_Board_Discussion_Paper.pptx,",len(prs.slides._sldIdLst),"slides")
