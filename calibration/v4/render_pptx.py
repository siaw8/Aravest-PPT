#!/usr/bin/env python3
"""Generic pptx -> PNG renderer (walks real shapes of the generated file).
Font substitute: Liberation Sans (Aptos is not installed in this environment).
Renders fills, lines, isosceles triangles, pictures, textboxes (mixed runs,
wrap, alignment, vertical anchor, spacing) and tables."""
import sys
from pptx import Presentation
from pptx.util import Emu
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.oxml.ns import qn
from PIL import Image, ImageDraw, ImageFont, ImageFilter

DPI = 150
EMU_IN = 914400
def px(emu): return int(round((emu or 0)/EMU_IN*DPI))
def ptpx(pt): return pt*DPI/72.0

SANS = {
 (False,False):"/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
 (True,False):"/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
 (False,True):"/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf",
 (True,True):"/usr/share/fonts/truetype/liberation/LiberationSans-BoldItalic.ttf",
}
# Real website Spectral (converted from aravest.com woff2)
SPECTRAL = {
 ("light",False):"assets/fonts/spectral-300-lat.ttf",
 ("light",True):"assets/fonts/spectral-300i-lat.ttf",
 ("reg",False):"assets/fonts/spectral-400-lat.ttf",
 ("reg",True):"assets/fonts/spectral-400i-lat.ttf",
}
_cache={}
def font(sz_pt, bold=False, italic=False, name=""):
    n=(name or "").lower()
    if "spectral" in n:
        wt="light" if "light" in n else "reg"
        path=SPECTRAL[(wt,italic)]
    else:
        path=SANS[(bold,italic)]
    key=(round(sz_pt,1),path)
    if key not in _cache:
        _cache[key]=ImageFont.truetype(path, int(round(ptpx(sz_pt))))
    return _cache[key]

def rgb(c):
    if c is None: return None
    return (c[0],c[1],c[2])

def run_props(run):
    r=run._r; rPr=r.find(qn('a:rPr'))
    caps=False; spc=0; fname=""
    if rPr is not None:
        if rPr.get('cap')=='all': caps=True
        if rPr.get('spc'):
            try: spc=int(rPr.get('spc'))/100.0
            except: spc=0
        lat=rPr.find(qn('a:latin'))
        if lat is not None: fname=lat.get('typeface') or ""
    if not fname:
        try: fname=run.font.name or ""
        except Exception: fname=""

    sz = run.font.size.pt if run.font.size else 12
    bold = bool(run.font.bold)
    italic = bool(run.font.italic)
    try: col = rgb(run.font.color.rgb) if run.font.color and run.font.color.type is not None else (53,70,79)
    except: col=(53,70,79)
    txt = run.text
    if caps: txt=txt.upper()
    return dict(text=txt, size=sz, bold=bold, italic=italic, color=col, spc=spc, fname=fname)

def draw_text_run(draw, x, y, rp):
    f=font(rp['size'], rp['bold'], rp['italic'], rp.get('fname',''))
    if rp['spc']:
        step=ptpx(rp['spc'])
        for ch in rp['text']:
            draw.text((x,y), ch, font=f, fill=rp['color'])
            x += draw.textlength(ch, font=f)+step
        return x
    draw.text((x,y), rp['text'], font=f, fill=rp['color'])
    return x + draw.textlength(rp['text'], font=f)

def run_width(draw, rp):
    f=font(rp['size'], rp['bold'], rp['italic'], rp.get('fname',''))
    if rp['spc']:
        step=ptpx(rp['spc'])
        return sum(draw.textlength(ch,font=f)+step for ch in rp['text'])
    return draw.textlength(rp['text'], font=f)

def layout_paragraph(draw, runs, box_w, align, line_spacing):
    """Return list of lines; each line = (list of (rp, text_piece, width), line_h, line_w)."""
    tokens=[]  # (rp, word, is_space)
    for rp in runs:
        parts=rp['text'].split(' ')
        for i,w in enumerate(parts):
            if w: tokens.append((rp,w))
            if i<len(parts)-1: tokens.append((rp,' '))
    lines=[]; cur=[]; cur_w=0
    def tok_w(rp,t):
        r2=dict(rp); r2['text']=t; return run_width(draw,r2)
    for rp,t in tokens:
        w=tok_w(rp,t)
        if t!=' ' and cur and cur_w+w>box_w:
            lines.append(cur); cur=[]; cur_w=0
        if t==' ' and not cur:  # skip leading space on wrapped line
            continue
        cur.append((rp,t,w)); cur_w+=w
    if cur: lines.append(cur)
    out=[]
    for ln in lines:
        lh=max(ptpx(rp['size']) for rp,_,_ in ln)*1.2*(line_spacing or 1.0)
        lw=sum(w for _,_,w in ln)
        out.append((ln,lh,lw))
    return out

def render_slide(slide, W, H):
    img=Image.new("RGB",(W,H),(255,255,255))
    draw=ImageDraw.Draw(img)
    for sh in slide.shapes:
        try: render_shape(draw,img,sh)
        except Exception as e:
            sys.stderr.write(f"shape err: {e}\n")
    return img

def shape_fill_rgb(sh):
    try:
        if sh.fill.type is not None and sh.fill.type==1:  # solid
            col=rgb(sh.fill.fore_color.rgb)
            alpha=1.0
            try:
                sf=sh.fill._xPr.find(qn('a:solidFill'))
                clr=sf.find(qn('a:srgbClr'))
                a=clr.find(qn('a:alpha')) if clr is not None else None
                if a is not None: alpha=int(a.get('val'))/100000.0
            except Exception: pass
            return col if alpha>=0.999 else (col[0],col[1],col[2],alpha)
    except Exception: pass
    return None
def shape_line_rgb(sh):
    try:
        lf=sh.line.fill
        if lf.type is not None and lf.type==1:
            return rgb(sh.line.color.rgb), max(1,px(sh.line.width))
    except Exception: pass
    return None,0

def render_shape(draw,img,sh):
    st=sh.shape_type
    x,y,w,h=px(sh.left),px(sh.top),px(sh.width),px(sh.height)
    if st==MSO_SHAPE_TYPE.PICTURE:
        blob=sh.image.blob
        from io import BytesIO
        pic=Image.open(BytesIO(blob)).convert("RGBA")
        pic=pic.resize((max(1,w),max(1,h)))
        img.paste(pic,(x,y),pic)
        return
    if st==MSO_SHAPE_TYPE.TABLE:
        render_table(draw,sh,x,y); return
    # autoshape / textbox
    fill=shape_fill_rgb(sh); lc,lw=shape_line_rgb(sh)
    is_tri=False; is_round=False
    try:
        ast=str(sh.auto_shape_type) if sh.auto_shape_type is not None else ''
        is_tri='TRIANGLE' in ast
        is_round='ROUNDED_RECTANGLE' in ast
    except Exception: pass
    if is_round:
        # corner radius from avLst (fraction of min dimension; default 16.667%)
        frac=0.16667
        try:
            gd=sh._element.spPr.findall('.//'+qn('a:gd'))
            if gd: frac=int(gd[0].get('fmla').split()[1])/100000.0
        except Exception: pass
        rad=max(2,int(frac*min(w,h)))
        # subtle shadow if outerShdw present
        has_sh=False
        try:
            el=sh._element.spPr.find(qn('a:effectLst'))
            has_sh=el is not None and el.find(qn('a:outerShdw')) is not None
        except Exception: pass
        if has_sh:
            lay=Image.new('RGBA',img.size,(0,0,0,0))
            ImageDraw.Draw(lay).rounded_rectangle([x+1,y+3,x+w+1,y+h+3],radius=rad,fill=(0,33,71,34))
            lay=lay.filter(ImageFilter.GaussianBlur(5))
            img.paste(lay,(0,0),lay)
        f3=fill[:3] if (fill and len(fill)==4) else fill
        if f3 is not None or lc is not None:
            ImageDraw.Draw(img).rounded_rectangle([x,y,x+w,y+h],radius=rad,fill=f3,
                                                  outline=lc,width=lw if lc else 0)
        if sh.has_text_frame: render_tf(draw, sh.text_frame, x,y,w,h)
        return
    if is_tri:
        pts=[(x+w//2,y),(x+w,y+h),(x,y+h)]
        if fill: draw.polygon(pts,fill=fill[:3] if len(fill)==4 else fill)
        if lc: draw.line(pts+[pts[0]],fill=lc,width=lw)
    else:
        if fill is not None:
            if len(fill)==4:
                r0,g0,b0,af=fill
                region=img.crop((max(0,x),max(0,y),min(img.size[0],x+w),min(img.size[1],y+h)))
                solid=Image.new('RGB',region.size,(r0,g0,b0))
                img.paste(Image.blend(region,solid,af),(max(0,x),max(0,y)))
            else:
                draw.rectangle([x,y,x+w,y+h],fill=fill)
        if lc is not None:
            draw.rectangle([x,y,x+w,y+h],outline=lc,width=lw)
    # text
    if sh.has_text_frame:
        render_tf(draw, sh.text_frame, x,y,w,h)

def render_tf(draw, tf, x,y,w,h, lpad=0,rpad=0,tpad=0,bpad=0, valign=None):
    box_w=w-lpad-rpad
    va = tf.vertical_anchor if valign is None else valign
    paras=[]
    for p in tf.paragraphs:
        runs=[run_props(r) for r in p.runs if r.text!='']
        if not runs:
            paras.append(([], ptpx(10)*1.2, (p.space_before.pt if p.space_before else 0),
                          (p.space_after.pt if p.space_after else 0), p.alignment)); continue
        ls = p.line_spacing if isinstance(p.line_spacing,(int,float)) else None
        lines=layout_paragraph(draw,runs,box_w,p.alignment,ls)
        sb=p.space_before.pt if p.space_before else 0
        sa=p.space_after.pt if p.space_after else 0
        paras.append((lines, None, sb, sa, p.alignment))
    total=0
    for lines,eh,sb,sa,al in paras:
        total+=ptpx(sb)
        if eh: total+=eh
        else:
            for ln,lh,lw in lines: total+=lh
        total+=ptpx(sa)
    if va==MSO_ANCHOR.MIDDLE: cy=y+(h-total)/2
    elif va==MSO_ANCHOR.BOTTOM: cy=y+h-total
    else: cy=y+tpad
    for lines,eh,sb,sa,al in paras:
        cy+=ptpx(sb)
        if eh: cy+=eh; cy+=ptpx(sa); continue
        for ln,lh,lw in lines:
            if al==PP_ALIGN.CENTER: sx=x+lpad+(box_w-lw)/2
            elif al==PP_ALIGN.RIGHT: sx=x+lpad+(box_w-lw)
            else: sx=x+lpad
            # baseline: draw at top of line; use ascent offset so text sits in line box
            asc=lh/1.2
            for rp,t,tw in ln:
                f=font(rp['size'],rp['bold'],rp['italic'],rp.get('fname',''))
                yy=cy+(lh-ptpx(rp['size'])*1.2)  # bottom-align runs in line
                r2=dict(rp); r2['text']=t
                draw_text_run(draw,sx,cy+ (lh-ptpx(rp['size'])*1.0)/2 - ptpx(rp['size'])*0.15, r2)
                sx+=tw
            cy+=lh
        cy+=ptpx(sa)

def render_table(draw, sh, x0,y0):
    tbl=sh.table
    colw=[px(c.width) for c in tbl.columns]
    rowh=[px(r.height) for r in tbl.rows]
    y=y0
    for ri,row in enumerate(tbl.rows):
        x=x0
        for ci,cell in enumerate(row.cells):
            cw,ch=colw[ci],rowh[ri]
            # fill
            try:
                if cell.fill.type==1:
                    draw.rectangle([x,y,x+cw,y+ch],fill=rgb(cell.fill.fore_color.rgb))
            except Exception: pass
            # top border
            tcPr=cell._tc.find(qn('a:tcPr'))
            if tcPr is not None:
                lnT=tcPr.find(qn('a:lnT'))
                if lnT is not None:
                    sf=lnT.find(qn('a:solidFill'))
                    if sf is not None:
                        clr=sf.find(qn('a:srgbClr'))
                        if clr is not None:
                            wv=int(lnT.get('w','12700'))
                            draw.line([x,y,x+cw,y],fill=tuple(int(clr.get('val')[i:i+2],16) for i in (0,2,4)),width=max(1,int(wv/12700*DPI/72)))
            # text
            lp=px(cell.margin_left); rp=px(cell.margin_right); tp=px(cell.margin_top); bp=px(cell.margin_bottom)
            render_tf(draw, cell.text_frame, x,y,cw,ch, lpad=lp,rpad=rp,tpad=tp,bpad=bp, valign=cell.vertical_anchor)
            x+=cw
        y+=rowh[ri]

def main():
    src=sys.argv[1]; prs=Presentation(src)
    W=px(prs.slide_width); H=px(prs.slide_height)
    for i,slide in enumerate(prs.slides,1):
        im=render_slide(slide,W,H)
        out=f"slide{i}.png"; im.save(out); print("wrote",out,im.size)

if __name__=="__main__": main()
