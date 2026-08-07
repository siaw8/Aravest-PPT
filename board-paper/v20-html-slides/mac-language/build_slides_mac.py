#!/usr/bin/env python3
"""Aravest 'Next Phase' v20 — HTML 16:9 slide deck, restyled to the attached
MAC Paper design language: all-sans (Aptos), top-accent cards, navy-header
banded tables, navy left-rule statement blocks, skyline photo cover/dividers,
no serif, no gold. Self-contained: images + logos embedded as base64."""
import json

A=json.load(open("assets_b64.json"))
LOGO_NAVY=f"data:image/png;base64,{A['navy']}"
LOGO_WHITE=f"data:image/png;base64,{A['white']}"
HERO=f"data:image/jpeg;base64,{A['hero']}"     # Singapore / Marina Bay
SEOUL=f"data:image/jpeg;base64,{A['seoul']}"    # Seoul skyline

# ---- palette (reconciled Aravest) ----
NAVY="#002B5C"; DEEP="#002147"; GRAPH="#35464F"; SLATE="#869397"
TEAL="#008080"; STEEL="#4682B4"; MIST="#E8E8E8"; BAND="#F4F5F6"

# functional colour — matched to the attached deck:
#   Pathway 1 Track Record Building  -> STEEL / blue
#   Pathway 2 Scale Acceleration     -> TEAL

# ================= AUM build chart (stepped line + 3 track-record paths) =================
def aum_chart():
    W,H=1180,410; L,R,T,B=66,262,40,50
    ymax=3000
    x0=L; x1=W-R; xMid=x0+(x1-x0)*0.60
    def Y(v): return T+(H-T-B)*(1-v/ymax)
    def XY(i): return x0+(xMid-x0)*i/5
    lv=[0,600,1000,1400,1700,2000]
    labs=["US$600m","US$1.0bn","US$1.4bn","US$1.7bn","c.US$2.0bn"]
    gap=(xMid-x0)/5; plat=gap*0.46
    s=[f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Illustrative AUM build and track-record outcomes">']
    for gv in (0,600,1000,1400,2000,2400,3000):
        y=Y(gv)
        s.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="#eceef1" stroke-width="1"/>')
        s.append(f'<text x="{x0-10}" y="{y+4:.1f}" text-anchor="end" font-size="12" fill="{SLATE}">{gv:,}</text>')
    s.append(f'<text x="16" y="{(T+H-B)/2:.0f}" font-size="11" fill="{SLATE}" transform="rotate(-90 16 {(T+H-B)/2:.0f})" text-anchor="middle">Illustrative cumulative AUM (US$m)</text>')
    for i in range(6):
        lab="Start" if i==0 else f"Year {i}"
        s.append(f'<text x="{XY(i):.1f}" y="{H-B+22:.1f}" text-anchor="middle" font-size="12.5" fill="{GRAPH}">{lab}</text>')
    # divider "Around Year 5"
    s.append(f'<line x1="{xMid:.1f}" y1="{Y(3000):.1f}" x2="{xMid:.1f}" y2="{Y(0):.1f}" stroke="{GRAPH}" stroke-width="1.1" stroke-dasharray="5 5" opacity=".55"/>')
    s.append(f'<text x="{xMid:.1f}" y="{Y(3000)-10:.1f}" text-anchor="middle" font-size="12.5" font-weight="700" fill="{GRAPH}">Around Year 5</text>')
    s.append(f'<text x="{xMid-8:.1f}" y="{Y(250):.1f}" text-anchor="end" font-size="11.5" fill="{SLATE}">30% retained co-investment capacity reached</text>')
    # build staircase (navy)
    pts=[(x0,Y(0))]
    for i in range(1,6):
        pts.append((XY(i),Y(lv[i])))
        if i<5: pts.append((XY(i)+plat,Y(lv[i])))
    d="M "+" L ".join(f"{x:.1f} {y:.1f}" for x,y in pts)
    s.append(f'<path d="{d}" fill="none" stroke="{NAVY}" stroke-width="2.6" stroke-linejoin="round"/>')
    for i in range(1,6):
        cx,cy=XY(i),Y(lv[i])
        s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="4.5" fill="#fff" stroke="{NAVY}" stroke-width="2.2"/>')
        s.append(f'<text x="{cx:.1f}" y="{cy-12:.1f}" text-anchor="middle" font-size="12.5" font-weight="700" fill="{NAVY}">{labs[i-1]}</text>')
    s.append(f'<text x="{XY(1)+plat/2:.1f}" y="{Y(430):.1f}" font-size="12" font-style="italic" fill="{SLATE}">AUM may plateau for 12&ndash;24 months while warehoused</text>')
    # three divergence paths — single-hue depth, direct-labelled (no gold)
    paths=[(3000,NAVY,"","20% retained &middot; c.US$3.0bn","Deeper track record and investor demand"),
           (2000,STEEL,"6 3","30% retained &middot; c.US$2.0bn","No further scale from the same capital base"),
           (1500,SLATE,"2 3","40% retained &middot; c.US$1.5bn","Higher alignment remains required")]
    for v,col,dash,lab,sub in paths:
        da=f'stroke-dasharray="{dash}"' if dash else ''
        s.append(f'<path d="M {xMid:.1f} {Y(2000):.1f} L {x1:.1f} {Y(v):.1f}" fill="none" stroke="{col}" stroke-width="2.4" {da}/>')
        s.append(f'<circle cx="{x1:.1f}" cy="{Y(v):.1f}" r="5" fill="#fff" stroke="{col}" stroke-width="2.4"/>')
        s.append(f'<text x="{x1+12:.1f}" y="{Y(v)-2:.1f}" font-size="13" font-weight="700" fill="{col}">{lab}</text>')
        s.append(f'<text x="{x1+12:.1f}" y="{Y(v)+15:.1f}" font-size="11.5" fill="{SLATE}">{sub}</text>')
    s.append(f'<circle cx="{x0:.1f}" cy="{Y(0):.1f}" r="4" fill="{NAVY}"/>')
    s.append('</svg>')
    return "".join(s)

# ================= proportion bars (transaction mix) =================
RAMP=[DEEP,"#17416b","#35618f","#6d8bab"]
def mix_bar(title, segs):
    total=sum(v for _,v,_ in segs)
    bar='<div class="pbar">'
    for i,(name,v,pct) in enumerate(segs):
        w=v/total*100
        bar+=f'<div class="pseg" style="width:{w:.2f}%;background:{RAMP[i]}"></div>'
    bar+='</div>'
    leg='<div class="pleg">'
    for i,(name,v,pct) in enumerate(segs):
        leg+=(f'<span class="pchip"><i style="background:{RAMP[i]}"></i>{name} '
              f'<b>US${v}m</b> &middot; {pct}</span>')
    leg+='</div>'
    return f'<div class="mixrow"><div class="mixt">{title}</div>{bar}{leg}</div>'

MIX = (
  mix_bar("By country",[("Singapore",366,"67%"),("South Korea",105,"19%"),("Australia",74,"14%")])+
  mix_bar("By sector",[("Living &amp; Lodging",369,"68%"),("Office",118,"22%"),("Private Credit",50,"9%"),("Logistics",8,"1%")])+
  mix_bar("By strategy",[("Value Add",340,"62%"),("Core Plus",155,"28%"),("Private Credit",50,"9%")])
)

# ================= deployment table =================
DEPLOY_ROWS=[
 ("Conrad Seoul","Acquired &middot; M&amp;G in discussion","45.0","350","29.8%","30.0","10.0%"),
 ("345 Queen Street","Acquired / funded","10.0","315","12.0%","&mdash;","12.0%"),
 ("SAREC","Committed","50.0","165","30.3%","&mdash;","30.3%"),
 ("Robin","Committed","16.0","34","100.0%","&mdash;","100.0%"),
 ("ARA-NH Domestic Fund","Committed","16.0","326","12.8%","&mdash;","12.8%"),
 ("Project Eagles","PDM approved","33.0","72","100.0%","26.4","20.0%"),
 ("Project Falcon","Priority","100.0","730","33.0%","50.0","16.7%"),
 ("Project Guardians","PDM approved","100.0","340","60.0%","50.0","30.0%"),
 ("Project Braves","Priority","25.0","144","40.0%","&mdash;","40.0%"),
 ("Project Slingers","Priority / preliminary","150.0","468","50.0%","50.0","16.7%"),
]
def deploy_table():
    th=('<tr><th class="l">Transaction</th><th class="l">Status</th><th>Aravest capital</th>'
        '<th>AUM</th><th>Initial co-inv.</th><th>To recycle</th><th>Post-recycle</th></tr>')
    body=""
    for r in DEPLOY_ROWS:
        body+=('<tr>'+f'<td class="l tn">{r[0]}</td><td class="l st">{r[1]}</td>'
               +"".join(f'<td>{c}</td>' for c in r[2:])+'</tr>')
    tot=('<tr class="tot"><td class="l">Current transaction set</td><td class="l"></td>'
         '<td>545.0</td><td>2,944</td><td>c.47%</td><td>206.4</td><td>c.19%</td></tr>')
    return f'<table class="deploy">{th}{body}{tot}</table>'

# ================= slide shell =================
def slide(inner, cls=""):
    return f'<section class="slide {cls}"><div class="stage">{inner}</div></section>'

LOGO_D=f'<img class="logo" src="{LOGO_NAVY}" alt="Aravest"/>'
LOGO_W=f'<img class="logo wht" src="{LOGO_WHITE}" alt="Aravest"/>'
FOOT='<div class="foot">Private and Confidential</div>'

def head(kick, sub, title, accent=""):
    ac=f' {accent}' if accent else ''
    return (f'<div class="kick{ac}">{kick}</div>'
            f'<div class="ksub">{sub}</div>'
            f'<h3 class="ti">{title}</h3>')

# 1 COVER — skyline photo, navy scrim
cover=slide(f'''
  <div class="cv-photo" style="background-image:url({HERO})"></div>
  <div class="cv-scrim"></div>
  <img class="cv-logo" src="{LOGO_WHITE}" alt="Aravest"/>
  <div class="cv-body">
    <div class="cv-ey">Private &amp; Confidential &middot; Board Strategy Discussion Paper</div>
    <div class="cv-bar"></div>
    <h1 class="cv-h1">Aravest&rsquo;s Next Phase</h1>
    <p class="cv-sub">Building the post-SMFL record into repeatable third-party capital formation and sustainable AUM growth.</p>
    <div class="cv-meta">Aravest Pte Ltd &middot; August 2026</div>
  </div>
''',"cover")

# 2 CHAPTER DIVIDER — skyline photo, navy scrim
divider=slide(f'''
  <div class="cv-photo" style="background-image:url({HERO})"></div>
  <div class="dv-scrim"></div>
  <img class="cv-logo" src="{LOGO_WHITE}" alt="Aravest"/>
  <div class="dv-body">
    <div class="dv-no">Chapter 01</div>
    <div class="dv-bar"></div>
    <h2 class="dv-h">Institutional Foundation</h2>
    <p class="dv-note">The institution Aravest is building, and the principles that govern every investment.</p>
    <div class="dv-list"><span>01&nbsp;&nbsp;Development journey</span><span>02&nbsp;&nbsp;The Aravest Way</span></div>
  </div>
''',"divider")

# 3 THE ARAVEST WAY
vals=''.join(f'''<div class="card"><div class="clab">{t}</div><div class="ch">{h}</div><p>{b}</p></div>'''
  for t,h,b in [
    ("Excellence","The quality of our thinking","Apply disciplined analysis, preparation, execution and communication, and continually raise the standard expected of the platform."),
    ("Trust","The way we behave","Act with integrity, transparency and fairness toward investors, shareholders, partners, lenders and colleagues &mdash; particularly when circumstances are difficult."),
    ("Accountability","How we take ownership","Own decisions and outcomes, respond when the facts change, and remain responsible through the full investment lifecycle."),
  ])
phil=''.join(f'<tr><td class="l tn">{k}</td><td>{v}</td></tr>' for k,v in [
    ("Recognising Value","Identify a genuine value gap and a responsible route to realise it."),
    ("Partnership","Define Aravest&rsquo;s role and secure the complementary capabilities required."),
    ("Stewardship of Capital","Protect and create value through the full lifecycle."),
    ("Risk &amp; Resilience","Accept risk deliberately, build resilience and adapt when facts change."),
    ("Fit for Purpose","Keep the principles constant while tailoring each structure and strategy."),
])
way=slide(f'''
  {LOGO_D}
  {head("01 Institutional foundation &ndash; the Aravest way",
        "The Aravest Way sets the standards for how Aravest conducts its business and invests.",
        "Transactions establish the investment record. Consistent judgement, conduct and accountability establish the institution.")}
  <div class="fp"><span>Our first principle</span>Investment management is a responsibility before it is a business.</div>
  <div class="way-grid">
    <div>
      <div class="pk">Our values &ndash; how we conduct our business</div>
      <div class="vrow">{vals}</div>
    </div>
    <div class="phil">
      <div class="pk">The investment philosophy &ndash; how the values are applied</div>
      <table class="mini">{phil}</table>
    </div>
  </div>
  {FOOT}<div class="pg">05</div>
''',"light")

# 4 AUM BUILD CHART
aum=slide(f'''
  {LOGO_D}
  {head("02 Proofing &ndash; how AUM builds over time",
        "The first five years build toward the 30% co-investment capacity; the track record then sets the level.",
        "Deploy, build proof, sell down and redeploy &mdash; then the track record determines the scale of the next phase.")}
  <div class="chartwrap">{aum_chart()}</div>
  <div class="statement"><span>Illustrative only &mdash; not a forecast.</span> Assumes US$300m sponsor capital, 50% project-level LTV, full redeployment of released capital and no valuation, FX, fee or disposal effects.</div>
  {FOOT}<div class="pg">09</div>
''',"light")

# 5 DEPLOYMENT TABLE
deploy=slide(f'''
  {LOGO_D}
  {head("02 Proofing &ndash; deploying and recycling the US$300 million",
        "The US$300m is deployed across the transaction set, then recycled through targeted sell-downs.",
        "Deployment and recycling create US$551.7m of capacity against US$545m of transaction requirements.")}
  {deploy_table()}
  <div class="src">US$300m SMFL support + US$251.7m completed and planned recycling = US$551.7m capacity for US$545m of requirements. Each transaction remains subject to standalone underwriting and approval. Amounts in US$m.</div>
  {FOOT}<div class="pg">13</div>
''',"light")

# 6 DEAL SLIDE — Marina One / Falcon (Pathway 2 Scale Acceleration -> TEAL)
deal=slide(f'''
  {LOGO_D}
  {head("02 Proofing &ndash; Pathway 2 &middot; Scale Acceleration",
        "Marina One can create a major institutional office proof point in an established sector.",
        "Marina One can create a major institutional office proof point.", accent="teal")}
  <div class="deal">
    <div class="deal-l">
      <div class="card tealbar">
        <div class="clab tealt">Project Falcon &middot; Marina One</div>
        <div class="ch">Potential joint venture with Hongkong Land</div>
        <p>A landmark integrated development in Singapore&rsquo;s Marina Bay CBD, anchored by two prime Grade-A office towers of approximately 1.88 million sq ft and a retail podium.</p>
      </div>
      <div class="drole"><b>Strategic role.</b> Create a major post-SMFL proof point in an established sector; demonstrate the ability to execute and manage an institutional-quality Singapore office investment; add material AUM; and deepen a strategic partnership with an established owner-operator.</div>
      <div class="dgov"><b>Governance.</b> Any capital commitment will be presented separately to the Board and remain subject to the agreed approval process.</div>
    </div>
    <div class="deal-r">
      <div class="metric"><span class="mv">US$100m</span><span class="ml">Potential capital support</span></div>
      <div class="metric"><span class="mv">33%</span><span class="ml">Indicative co-investment</span></div>
      <div class="metric hi"><span class="mv">US$730m</span><span class="ml">Indicative AUM</span></div>
      <div class="tag">Priority opportunity</div>
    </div>
  </div>
  {FOOT}<div class="pg">14</div>
''',"light")

# 7 TRANSACTION MIX
mix=slide(f'''
  {LOGO_D}
  {head("02 Proofing &ndash; resulting transaction mix",
        "The mix reflects where Aravest currently sees value &mdash; not fixed country or sector quotas.",
        "The transaction mix reflects current conviction, not target weights.")}
  <div class="mixwrap">{MIX}</div>
  <div class="statement"><span>Current outcomes, not targets.</span> Weights reflect the US$545m transaction set. Source: SMFL US$300m support model as at 6 August 2026.</div>
  {FOOT}<div class="pg">18</div>
''',"light")

SLIDES=[cover,divider,way,aum,deploy,deal,mix]

CSS=f'''
:root{{--navy:{NAVY};--deep:{DEEP};--graph:{GRAPH};--slate:{SLATE};--teal:{TEAL};--steel:{STEEL};--mist:{MIST};--band:{BAND}}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#4a5560;font-family:"Aptos",-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif;color:var(--graph);-webkit-font-smoothing:antialiased}}
.deck{{padding:26px 0 60px}}
.slide{{display:flex;justify-content:center;margin:0 auto 26px}}
.stage{{position:relative;width:1280px;height:720px;background:#fff;overflow:hidden;
  box-shadow:0 20px 60px rgba(0,0,0,.35);flex:0 0 auto}}
.logo{{position:absolute;top:30px;right:44px;height:40px;width:auto}}
.foot{{position:absolute;left:60px;bottom:26px;font-size:12px;color:var(--slate)}}
.pg{{position:absolute;right:44px;bottom:26px;font-size:12px;color:var(--slate);letter-spacing:.04em}}

/* ---- cover / divider photo ---- */
.cv-photo{{position:absolute;inset:0;background-size:cover;background-position:center}}
.cv-scrim{{position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,25,55,.92) 0%,rgba(0,33,71,.78) 42%,rgba(0,33,71,.30) 100%)}}
.dv-scrim{{position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,25,55,.94) 0%,rgba(0,33,71,.80) 46%,rgba(0,33,71,.34) 100%)}}
.cv-logo{{position:absolute;top:46px;left:60px;height:52px;width:auto;z-index:3}}
.cv-body{{position:absolute;left:60px;top:300px;right:120px;z-index:3;color:#fff}}
.cv-ey{{font-size:13px;letter-spacing:.15em;text-transform:uppercase;color:rgba(255,255,255,.78);font-weight:700}}
.cv-bar{{width:64px;height:3px;background:var(--steel);margin:16px 0 20px}}
.cv-h1{{font-size:70px;line-height:1.02;font-weight:700;letter-spacing:-.01em;color:#fff}}
.cv-sub{{margin-top:22px;max-width:720px;font-size:21px;line-height:1.5;color:rgba(255,255,255,.9);font-weight:300}}
.cv-meta{{margin-top:28px;font-size:14px;letter-spacing:.04em;color:rgba(255,255,255,.66)}}

.dv-body{{position:absolute;left:60px;top:250px;right:120px;z-index:3;color:#fff}}
.dv-no{{font-size:15px;letter-spacing:.18em;text-transform:uppercase;color:rgba(255,255,255,.7);font-weight:700}}
.dv-bar{{width:56px;height:3px;background:var(--steel);margin:16px 0 20px}}
.dv-h{{font-size:56px;font-weight:700;letter-spacing:-.01em;line-height:1.04;color:#fff}}
.dv-note{{margin-top:20px;max-width:620px;font-size:19px;line-height:1.5;color:rgba(255,255,255,.85);font-weight:300}}
.dv-list{{margin-top:44px;display:flex;gap:34px;font-size:13.5px;letter-spacing:.05em;color:rgba(255,255,255,.82)}}
.dv-list span{{border-top:2px solid rgba(255,255,255,.42);padding-top:11px;font-weight:600}}

/* ---- content-slide header ---- */
.kick{{position:absolute;top:44px;left:60px;font-size:15px;font-weight:600;color:var(--graph)}}
.kick.teal{{color:var(--teal)}}
.ksub{{position:absolute;top:70px;left:60px;right:200px;font-size:14.5px;color:var(--slate);font-weight:400}}
.ti{{position:absolute;top:104px;left:60px;width:1000px;font-size:27px;line-height:1.2;font-weight:700;color:var(--navy);letter-spacing:-.005em}}

/* ---- generic top-accent card ---- */
.card{{position:relative;background:#fff;border:1px solid var(--mist);border-top:3px solid var(--navy);
  border-radius:9px;padding:18px 20px;box-shadow:0 6px 16px rgba(0,33,71,.06)}}
.card .clab{{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--slate)}}
.card .ch{{font-size:17px;font-weight:700;color:var(--navy);margin:7px 0 9px;line-height:1.22}}
.card p{{font-size:13.5px;line-height:1.45;color:var(--graph)}}
.card.tealbar{{border-top-color:var(--teal)}}
.clab.tealt{{color:var(--teal)}}

/* ---- first-principle left-rule block ---- */
.fp{{position:absolute;top:186px;left:60px;right:60px;border-left:4px solid var(--navy);padding:6px 0 6px 22px}}
.fp span{{display:block;font-size:12px;letter-spacing:.15em;text-transform:uppercase;color:var(--slate);font-weight:700;margin-bottom:8px}}
.fp{{font-size:27px;line-height:1.16;font-weight:700;color:var(--navy)}}

/* ---- the aravest way grid ---- */
.way-grid{{position:absolute;top:290px;left:60px;right:60px;display:grid;grid-template-columns:1.55fr 1fr;gap:34px}}
.pk{{font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--slate);margin-bottom:12px}}
.vrow{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}
.way-grid .card{{padding:14px 15px}}
.way-grid .card .ch{{font-size:15px;margin:6px 0 7px}}
.way-grid .card p{{font-size:12px;line-height:1.4}}
table.mini{{width:100%;border-collapse:collapse;font-size:12.5px}}
table.mini td{{padding:8px 10px;border-bottom:1px solid var(--mist);vertical-align:top;color:var(--graph);line-height:1.34}}
table.mini tr:nth-child(even) td{{background:var(--band)}}
table.mini td.tn{{font-weight:700;color:var(--navy);width:42%}}

/* ---- chart ---- */
.chartwrap{{position:absolute;top:180px;left:52px;right:52px}}
.chartwrap svg{{display:block}}

/* ---- navy left-rule takeaway statement ---- */
.statement{{position:absolute;left:60px;right:60px;bottom:56px;border-left:4px solid var(--navy);
  padding:2px 0 2px 18px;font-size:13.5px;line-height:1.5;color:var(--graph)}}
.statement span{{color:var(--navy);font-weight:700}}

/* ---- deployment table ---- */
table.deploy{{position:absolute;top:168px;left:56px;right:56px;border-collapse:collapse;font-size:13px;width:auto}}
table.deploy th,table.deploy td{{padding:7.5px 11px;text-align:right;color:var(--graph)}}
table.deploy th{{background:var(--navy);color:#fff;font-weight:600;font-size:11.5px;letter-spacing:.01em}}
table.deploy th.l,table.deploy td.l{{text-align:left}}
table.deploy tbody tr:nth-child(even) td{{background:var(--band)}}
table.deploy td.tn{{font-weight:700;color:var(--navy)}}
table.deploy td.st{{color:var(--slate);font-size:12px}}
table.deploy tr.tot td{{border-top:2px solid var(--navy);font-weight:700;color:var(--navy);background:#eef2f6}}
.src{{position:absolute;bottom:52px;left:60px;right:60px;font-size:11.5px;color:var(--slate);line-height:1.4}}

/* ---- deal ---- */
.deal{{position:absolute;top:176px;left:60px;right:60px;display:grid;grid-template-columns:1.7fr 1fr;gap:26px}}
.deal-l .card{{margin-bottom:16px}}
.deal-l .card p{{margin-top:2px}}
.drole,.dgov{{font-size:13px;line-height:1.5;color:var(--graph);margin-bottom:10px}}
.drole b,.dgov b{{color:var(--navy)}}
.deal-r{{display:flex;flex-direction:column;gap:13px}}
.metric{{background:var(--band);border:1px solid var(--mist);border-radius:10px;padding:15px 18px}}
.metric.hi{{background:var(--navy);border:none}}
.metric .mv{{display:block;font-size:32px;font-weight:700;color:var(--navy);line-height:1;letter-spacing:-.01em}}
.metric.hi .mv{{color:#fff}}
.metric .ml{{display:block;font-size:12px;color:var(--slate);margin-top:6px}}
.metric.hi .ml{{color:rgba(255,255,255,.78)}}
.tag{{align-self:flex-start;background:var(--teal);color:#fff;font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;padding:6px 13px;border-radius:4px}}

/* ---- mix ---- */
.mixwrap{{position:absolute;top:186px;left:60px;right:60px}}
.mixrow{{margin-bottom:24px}}
.mixt{{font-size:12.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--navy);margin-bottom:9px}}
.pbar{{display:flex;height:32px;border-radius:5px;overflow:hidden;gap:2px;background:#fff}}
.pseg{{height:100%}}
.pleg{{display:flex;flex-wrap:wrap;gap:18px;margin-top:9px}}
.pchip{{font-size:13px;color:var(--graph);display:inline-flex;align-items:center}}
.pchip i{{width:11px;height:11px;border-radius:2px;margin-right:7px;display:inline-block}}
.pchip b{{color:var(--navy);margin:0 3px 0 5px;font-weight:700}}

/* ---- nav ---- */
.navbar{{position:fixed;bottom:16px;left:50%;transform:translateX(-50%);z-index:50;background:rgba(0,33,71,.92);
  color:#fff;border-radius:30px;padding:8px;display:flex;align-items:center;gap:4px;box-shadow:0 8px 24px rgba(0,0,0,.3)}}
.navbar button{{background:none;border:0;color:#fff;font-size:16px;cursor:pointer;width:34px;height:34px;border-radius:50%}}
.navbar button:hover{{background:rgba(255,255,255,.15)}}
.navbar .ct{{font-size:13px;min-width:52px;text-align:center;color:rgba(255,255,255,.85);letter-spacing:.05em}}

@media print{{
  @page{{size:1280px 720px;margin:0}}
  body{{background:#fff}}.deck{{padding:0}}.navbar{{display:none}}
  .slide{{margin:0;page-break-after:always}}
  .stage{{box-shadow:none}}
}}
'''

HTML=f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Aravest&rsquo;s Next Phase — Slide Design (v20, MAC language)</title>
<style>{CSS}</style></head><body>
<div class="deck">{''.join(SLIDES)}</div>
<div class="navbar"><button id="prev">&larr;</button><span class="ct" id="ct">1 / {len(SLIDES)}</span><button id="next">&rarr;</button></div>
<script>
const slides=[...document.querySelectorAll('.slide')];let i=0;
function fit(){{const s=Math.min(1,(window.innerWidth-40)/1280);
  document.querySelectorAll('.stage').forEach(st=>{{st.style.transform='scale('+s+')';st.style.transformOrigin='top center';
    st.parentElement.style.height=(720*s)+'px';}});}}
function go(n){{i=Math.max(0,Math.min(slides.length-1,n));slides[i].scrollIntoView({{behavior:'smooth',block:'center'}});
  document.getElementById('ct').textContent=(i+1)+' / '+slides.length;}}
document.getElementById('prev').onclick=()=>go(i-1);
document.getElementById('next').onclick=()=>go(i+1);
addEventListener('keydown',e=>{{if(e.key==='ArrowRight'||e.key==='PageDown')go(i+1);if(e.key==='ArrowLeft'||e.key==='PageUp')go(i-1);}});
addEventListener('resize',fit);fit();
const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{i=slides.indexOf(e.target);document.getElementById('ct').textContent=(i+1)+' / '+slides.length;}}}}),{{threshold:.5}});
slides.forEach(s=>io.observe(s));
</script></body></html>'''

open("Aravest_Next_Phase_v20_MAC.html","w").write(HTML)
print("wrote Aravest_Next_Phase_v20_MAC.html", len(HTML),"bytes,",len(SLIDES),"slides")
