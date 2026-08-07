#!/usr/bin/env python3
"""Aravest 'Next Phase' v20 — HTML 16:9 slide deck, core design archetypes.
Self-contained: embedded Spectral display face, inline SVG charts, no external assets."""
import json

F=json.load(open("fonts_b64.json"))
def face(name,style,weight,key):
    return (f"@font-face{{font-family:'{name}';font-style:{style};font-weight:{weight};"
            f"font-display:swap;src:url(data:font/woff2;base64,{F[key]}) format('woff2');}}")
FONTS="\n".join([
    face("Spectral","normal",300,"spectral-300-lat.woff2"),
    face("Spectral","italic",300,"spectral-300i-lat.woff2"),
    face("Spectral","normal",400,"spectral-400-lat.woff2"),
])

# ---- palette ----
NAVY="#002B5C"; DEEP="#002147"; GRAPH="#35464F"; SLATE="#869397"
TEAL="#008080"; STEEL="#4682B4"; GOLD="#C8A951"; MIST="#E8E8E8"

# ================= AUM build chart (SVG) =================
def aum_chart():
    W,H=1120,338; L,R,T,B=70,158,16,40
    ymax=3000
    def X(i,n): return L+(W-L-R)*(i+0.5)/n
    def Y(v): return T+(H-T-B)*(1-v/ymax)
    stages=[("Y1",600),("Y2",1000),("Y3",1400),("Y4",1700),("Y5",2000)]
    n=len(stages); bw=(W-L-R)/n*0.52
    s=[f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Illustrative AUM build">']
    # gridlines
    for gv in (0,1000,2000,3000):
        y=Y(gv)
        s.append(f'<line x1="{L}" y1="{y:.1f}" x2="{W-R}" y2="{y:.1f}" stroke="#e7e9ec" stroke-width="1"/>')
        s.append(f'<text x="{L-10}" y="{y+4:.1f}" text-anchor="end" font-size="12" fill="{SLATE}">{gv:,}</text>')
    # outcome reference lines (sustainable level by track record)
    outc=[(1500,"40%","US$1.5bn",SLATE),(2000,"30%","US$2.0bn",GOLD),(3000,"20%","US$3.0bn",SLATE)]
    for v,pct,lab,col in outc:
        y=Y(v)
        dash='' if col==GOLD else 'stroke-dasharray="4 4"'
        s.append(f'<line x1="{L}" y1="{y:.1f}" x2="{W-R}" y2="{y:.1f}" stroke="{col}" stroke-width="{2 if col==GOLD else 1.2}" {dash} opacity="{1 if col==GOLD else .6}"/>')
        s.append(f'<text x="{W-R+8}" y="{y-3:.1f}" font-size="12.5" font-weight="700" fill="{col if col==GOLD else GRAPH}">{pct} co-inv</text>')
        s.append(f'<text x="{W-R+8}" y="{y+13:.1f}" font-size="11.5" fill="{SLATE}">{lab}</text>')
    # bars
    for i,(lb,v) in enumerate(stages):
        x=X(i,n)-bw/2; y=Y(v); h=Y(0)-y
        s.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{h:.1f}" rx="3" fill="{NAVY}"/>')
        s.append(f'<text x="{X(i,n):.1f}" y="{y-7:.1f}" text-anchor="middle" font-size="12" font-weight="700" fill="{NAVY}">{v:,}</text>')
        s.append(f'<text x="{X(i,n):.1f}" y="{H-B+20:.1f}" text-anchor="middle" font-size="12.5" fill="{GRAPH}">{lb}</text>')
    s.append(f'<text x="{L-46}" y="{T+2}" font-size="11.5" fill="{SLATE}" transform="rotate(-90 {L-46} {(H)/2})">Illustrative cumulative AUM (US$m)</text>')
    s.append('</svg>')
    return "".join(s)

# ================= proportion bars (transaction mix) =================
RAMP=[DEEP,"#17416b","#35618f","#6d8bab"]  # sequential navy, dark->light
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
              f'<b>US${v}m</b> · {pct}</span>')
    leg+='</div>'
    return f'<div class="mixrow"><div class="mixt">{title}</div>{bar}{leg}</div>'

MIX = (
  mix_bar("By country",[("Singapore",366,"67%"),("South Korea",105,"19%"),("Australia",74,"14%")])+
  mix_bar("By sector",[("Living &amp; Lodging",369,"68%"),("Office",118,"22%"),("Private Credit",50,"9%"),("Logistics",8,"1%")])+
  mix_bar("By strategy",[("Value Add",340,"62%"),("Core Plus",155,"28%"),("Private Credit",50,"9%")])
)

# ================= deployment table =================
DEPLOY_ROWS=[
 ("Conrad Seoul","Acquired · M&amp;G in discussion","45.0","350","29.8%","30.0","10.0%"),
 ("345 Queen Street","Acquired / funded","10.0","315","12.0%","—","12.0%"),
 ("SAREC","Committed","50.0","165","30.3%","—","30.3%"),
 ("Robin","Committed","16.0","34","100.0%","—","100.0%"),
 ("ARA-NH Domestic Fund","Committed","16.0","326","12.8%","—","12.8%"),
 ("Project Eagles","PDM approved","33.0","72","100.0%","26.4","20.0%"),
 ("Project Falcon","Priority","100.0","730","33.0%","50.0","16.7%"),
 ("Project Guardians","PDM approved","100.0","340","60.0%","50.0","30.0%"),
 ("Project Braves","Priority","25.0","144","40.0%","—","40.0%"),
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

# ================= slide shells =================
def slide(inner, cls="", n=""):
    pg=f'<div class="pg">{n}</div>' if n else ''
    return f'<section class="slide {cls}"><div class="stage">{inner}{pg}</div></section>'

LOGO_D='<div class="logo">ARAVEST</div>'
FOOT='<div class="foot">Private and Confidential</div>'

# 1 COVER
cover=slide(f'''
  <div class="cv-brand">ARAVEST</div>
  <div class="cv-rule"></div>
  <div class="cv-ey">Private &amp; Confidential · Board Strategy Discussion Paper</div>
  <h1 class="cv-h1">Aravest&rsquo;s <em>Next Phase</em></h1>
  <p class="cv-sub">Building the post-SMFL record into repeatable third-party capital formation and sustainable AUM growth.</p>
  <div class="cv-meta">Aravest Pte Ltd · August 2026</div>
''',"cover")

# 2 CHAPTER DIVIDER
divider=slide(f'''
  {LOGO_D}
  <div class="dv-no">Chapter I</div>
  <h2 class="dv-h">Institutional Foundation</h2>
  <div class="dv-gold"></div>
  <p class="dv-note">The institution Aravest is building and the principles that govern every investment.</p>
  <div class="dv-list">
     <span>01 · Development journey</span><span>02 · The Aravest Way</span>
  </div>
  <div class="foot light">Private and Confidential</div>
''',"divider")

# 3 THE ARAVEST WAY (values + philosophy)
vals=''.join(f'''<div class="vcard"><div class="vt">{t}</div><div class="vh">{h}</div><p>{b}</p></div>'''
  for t,h,b in [
    ("Excellence","Quality of thinking","Disciplined analysis, preparation, execution and communication."),
    ("Trust","How we behave","Integrity, transparency and fairness — especially when circumstances are difficult."),
    ("Accountability","How we take ownership","Ownership of decisions, risks and outcomes through the full lifecycle."),
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
  <div class="ky">02 · The Aravest Way</div>
  <h3 class="ti">The Aravest Way defines how Aravest behaves, invests and creates value.</h3>
  <div class="way-grid">
    <div>
      <div class="fp"><span>Our first principle</span>Investment management is a responsibility before it is a business.</div>
      <div class="vrow">{vals}</div>
    </div>
    <div class="phil">
      <div class="pk">The investment philosophy — how the values are applied</div>
      <table class="mini">{phil}</table>
    </div>
  </div>
  {FOOT}<div class="pg">5</div>
''',"light")

# 4 AUM BUILD CHART
aum=slide(f'''
  {LOGO_D}
  <div class="ky">05 · How AUM builds over time</div>
  <h3 class="ti">The first five years build toward the 30% co-investment capacity; the track record then sets the level.</h3>
  <div class="chartwrap">{aum_chart()}</div>
  <div class="assume">Assumes US$300m sponsor capital, 50% project-level LTV, full redeployment of released capital and no valuation, FX, fee or disposal effects. <b>Illustrative only; not a forecast.</b></div>
  {FOOT}<div class="pg">9</div>
''',"light")

# 5 DEPLOYMENT TABLE
deploy=slide(f'''
  {LOGO_D}
  <div class="ky">11 · Deploying and recycling the US$300 million</div>
  <h3 class="ti">The US$300m is deployed across the transaction set, then recycled through targeted sell-downs.</h3>
  {deploy_table()}
  <div class="src">US$300m SMFL support + US$251.7m completed and planned recycling = US$551.7m capacity for US$545m of requirements. Each transaction remains subject to standalone underwriting and approval. Amounts in US$m.</div>
  {FOOT}<div class="pg">13</div>
''',"light")

# 6 DEAL SLIDE — Marina One / Falcon
deal=slide(f'''
  {LOGO_D}
  <div class="ky steel">08 · Office · Scale Acceleration</div>
  <h3 class="ti">Marina One can create a major institutional office proof point.</h3>
  <div class="deal">
    <div class="deal-l">
      <div class="dpw">Project Falcon · Marina One</div>
      <div class="djv">Potential joint venture with Hongkong Land</div>
      <p>A landmark integrated development in Singapore&rsquo;s Marina Bay CBD, anchored by two prime Grade-A office towers of approximately 1.88 million sq ft and a retail podium.</p>
      <div class="drole"><b>Strategic role.</b> Create a major post-SMFL proof point in an established sector; demonstrate the ability to execute and manage an institutional-quality Singapore office investment; add material AUM; and deepen a strategic partnership with an established owner-operator.</div>
      <div class="dgov"><b>Governance.</b> Any capital commitment will be presented separately to the Board and remain subject to the agreed approval process.</div>
    </div>
    <div class="deal-r">
      <div class="metric"><span class="mv">US$100m</span><span class="ml">Potential capital support</span></div>
      <div class="metric"><span class="mv">33%</span><span class="ml">Indicative co-investment</span></div>
      <div class="metric hi"><span class="mv">US$730m</span><span class="ml">Indicative AUM</span></div>
      <div class="tagp2">Priority opportunity</div>
    </div>
  </div>
  {FOOT}<div class="pg">14</div>
''',"light")

# 7 TRANSACTION MIX
mix=slide(f'''
  {LOGO_D}
  <div class="ky">14 · Resulting transaction mix</div>
  <h3 class="ti">The mix reflects where Aravest currently sees value — not fixed country or sector quotas.</h3>
  <div class="mixwrap">{MIX}</div>
  <div class="src">Current outcomes of the US$545m transaction set, not target weights. Source: SMFL US$300m support model as at 6 August 2026.</div>
  {FOOT}<div class="pg">18</div>
''',"light")

SLIDES=[cover,divider,way,aum,deploy,deal,mix]

CSS=f'''
{FONTS}
:root{{--navy:{NAVY};--deep:{DEEP};--graph:{GRAPH};--slate:{SLATE};--teal:{TEAL};--steel:{STEEL};--gold:{GOLD};--mist:{MIST}}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#4a5560;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Aptos",Arial,sans-serif;color:var(--graph)}}
.deck{{padding:26px 0 60px}}
.slide{{display:flex;justify-content:center;margin:0 auto 26px}}
.stage{{position:relative;width:1280px;height:720px;background:#fff;overflow:hidden;
  box-shadow:0 20px 60px rgba(0,0,0,.35);flex:0 0 auto}}
.slide.cover .stage,.slide.divider .stage{{background:linear-gradient(135deg,#002147 0%,#002B5C 60%,#0b3a63 100%);color:#fff}}
.logo{{position:absolute;top:34px;right:44px;font-family:Georgia,serif;letter-spacing:.3em;font-size:15px;color:var(--navy)}}
.foot{{position:absolute;left:44px;bottom:30px;font-size:12.5px;color:var(--slate)}}
.foot.light{{color:rgba(255,255,255,.7)}}
.pg{{position:absolute;right:44px;bottom:30px;font-size:12.5px;color:var(--slate)}}

/* cover */
.cover .cv-brand{{position:absolute;top:40px;left:60px;font-family:Georgia,serif;letter-spacing:.34em;font-size:16px;color:#fff}}
.cv-rule{{position:absolute;top:300px;left:62px;width:74px;height:2px;background:var(--gold)}}
.cv-ey{{position:absolute;top:322px;left:62px;font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:#ded0ad;font-weight:700}}
.cv-h1{{position:absolute;top:352px;left:60px;font-family:'Spectral',Georgia,serif;font-weight:300;font-size:88px;line-height:1;color:#fff}}
.cv-h1 em{{font-style:italic}}
.cv-sub{{position:absolute;top:494px;left:62px;width:760px;font-size:22px;line-height:1.5;color:rgba(255,255,255,.85)}}
.cv-meta{{position:absolute;bottom:52px;left:62px;font-size:14px;color:rgba(255,255,255,.6);letter-spacing:.03em}}
.cover .stage:after{{content:"";position:absolute;right:-150px;bottom:-220px;width:560px;height:560px;border:1px solid rgba(200,169,81,.28);transform:rotate(20deg)}}

/* divider */
.divider .logo{{color:#fff;font-family:Georgia,serif}}
.dv-no{{position:absolute;top:250px;left:62px;font-family:'Spectral',Georgia,serif;font-size:34px;color:rgba(255,255,255,.55)}}
.dv-h{{position:absolute;top:296px;left:60px;font-family:'Spectral',Georgia,serif;font-weight:300;font-size:60px;color:#fff}}
.dv-gold{{position:absolute;top:400px;left:62px;width:60px;height:2px;background:var(--gold)}}
.dv-note{{position:absolute;top:424px;left:62px;width:640px;font-size:19px;line-height:1.5;color:rgba(255,255,255,.82)}}
.dv-list{{position:absolute;bottom:120px;left:62px;display:flex;gap:30px;color:rgba(255,255,255,.7);font-size:14px;letter-spacing:.04em}}
.dv-list span{{border-top:1px solid rgba(255,255,255,.3);padding-top:10px}}

/* working slide furniture */
.ky{{position:absolute;top:52px;left:60px;font-size:13px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--graph)}}
.ky.steel{{color:var(--steel)}}
.ti{{position:absolute;top:80px;left:60px;width:1050px;font-family:'Spectral',Georgia,serif;font-weight:400;font-size:31px;line-height:1.18;color:var(--navy)}}

/* the aravest way */
.way-grid{{position:absolute;top:186px;left:60px;right:60px;display:grid;grid-template-columns:1.15fr 1fr;gap:34px}}
.fp{{background:linear-gradient(135deg,#002147,#002B5C);color:#fff;border-radius:12px;padding:22px 26px;font-family:'Spectral',Georgia,serif;font-size:24px;line-height:1.3}}
.fp span{{display:block;font-family:inherit;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#ded0ad;font-weight:700;margin-bottom:8px;font-style:normal}}
.vrow{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:18px}}
.vcard{{background:#fff;border:1px solid var(--mist);border-radius:10px;padding:16px}}
.vt{{font-size:11.5px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--teal)}}
.vh{{font-family:'Spectral',Georgia,serif;font-size:17px;color:var(--navy);margin:6px 0 8px}}
.vcard p{{font-size:13px;line-height:1.4;color:var(--graph)}}
.phil .pk{{font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--slate);margin-bottom:8px}}
table.mini{{width:100%;border-collapse:collapse;font-size:13px}}
table.mini td{{padding:9px 10px;border-bottom:1px solid var(--mist);vertical-align:top;color:var(--graph);line-height:1.35}}
table.mini td.tn{{font-family:'Spectral',Georgia,serif;color:var(--navy);width:38%}}

/* chart */
.chartwrap{{position:absolute;top:196px;left:56px;right:56px}}
.chartwrap svg{{display:block}}
.assume{{position:absolute;top:560px;left:60px;right:60px;font-size:12.5px;color:var(--slate);line-height:1.4}}
.assume b{{color:var(--graph)}}

/* deploy table */
table.deploy{{position:absolute;top:176px;left:56px;right:56px;border-collapse:collapse;font-size:13px;width:auto}}
table.deploy th,table.deploy td{{padding:7.5px 10px;border-bottom:1px solid var(--mist);text-align:right;color:var(--graph)}}
table.deploy th{{background:var(--navy);color:#fff;font-weight:600;font-size:11.5px;border-bottom:none}}
table.deploy th.l,table.deploy td.l{{text-align:left}}
table.deploy td.tn{{font-family:'Spectral',Georgia,serif;color:var(--navy)}}
table.deploy td.st{{color:var(--slate);font-size:12px}}
table.deploy tr.tot td{{border-top:2px solid var(--navy);border-bottom:none;font-weight:700;color:var(--navy);background:#f5f8fb}}
.src{{position:absolute;bottom:60px;left:60px;right:60px;font-size:11.5px;color:var(--slate);line-height:1.4}}

/* deal */
.deal{{position:absolute;top:184px;left:60px;right:60px;display:grid;grid-template-columns:1.7fr 1fr;gap:26px}}
.deal-l .dpw{{font-size:12.5px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--steel)}}
.deal-l .djv{{font-family:'Spectral',Georgia,serif;font-size:22px;color:var(--navy);margin:4px 0 12px}}
.deal-l p{{font-size:15px;line-height:1.5;color:var(--graph);margin-bottom:14px}}
.drole,.dgov{{font-size:13.5px;line-height:1.5;color:var(--graph);margin-bottom:10px}}
.drole b,.dgov b{{color:var(--navy)}}
.deal-r{{display:flex;flex-direction:column;gap:14px}}
.metric{{background:#f4f7fa;border:1px solid #e2ebf3;border-radius:11px;padding:16px 18px}}
.metric.hi{{background:linear-gradient(135deg,#002147,#002B5C);border:none}}
.metric .mv{{display:block;font-family:'Spectral',Georgia,serif;font-size:34px;color:var(--navy);line-height:1}}
.metric.hi .mv{{color:#fff}}
.metric .ml{{display:block;font-size:12.5px;color:var(--slate);margin-top:6px}}
.metric.hi .ml{{color:rgba(255,255,255,.75)}}
.tagp2{{align-self:flex-start;background:var(--steel);color:#fff;font-size:11.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;padding:6px 12px;border-radius:20px}}

/* mix */
.mixwrap{{position:absolute;top:196px;left:60px;right:60px}}
.mixrow{{margin-bottom:26px}}
.mixt{{font-size:13px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;color:var(--navy);margin-bottom:9px}}
.pbar{{display:flex;height:34px;border-radius:6px;overflow:hidden;gap:2px;background:#fff}}
.pseg{{height:100%}}
.pleg{{display:flex;flex-wrap:wrap;gap:18px;margin-top:9px}}
.pchip{{font-size:13px;color:var(--graph);display:inline-flex;align-items:center}}
.pchip i{{width:11px;height:11px;border-radius:2px;margin-right:7px;display:inline-block}}
.pchip b{{color:var(--navy);margin:0 3px 0 5px;font-weight:700}}

/* nav */
.navbar{{position:fixed;bottom:16px;left:50%;transform:translateX(-50%);z-index:50;background:rgba(0,33,71,.92);
  color:#fff;border-radius:30px;padding:8px 8px;display:flex;align-items:center;gap:4px;box-shadow:0 8px 24px rgba(0,0,0,.3)}}
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
<title>Aravest&rsquo;s Next Phase — Slide Design (v20 draft)</title>
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

open("Aravest_Next_Phase_v20_Slides.html","w").write(HTML)
print("wrote Aravest_Next_Phase_v20_Slides.html", len(HTML),"bytes,",len(SLIDES),"slides")
