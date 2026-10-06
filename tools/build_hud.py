"""Builds hud.html (artifact source) and hud-standalone.html: ten static screens testing on-image HUDs and borderless views."""
import pathlib, math
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / 'concepts.html').read_text()
paint = src[src.index('(function paint(g){'):src.index("})(scene.getContext('2d'));") + len("})(scene.getContext('2d'));")]

C = {'AURUM 200':['#d9a441','#b8432f','#2e3b4e'],'VERANO 400':['#e58b6b','#f3d3a8','#4f7a6a'],'LUMEN 100':['#2f5fd0','#e8eef9','#d23b2a'],
     'NOCTA 800T':['#1e6f7a','#c9473a','#0e1b2c'],'KINO 250D':['#c0362c','#e7d9bf','#3d4a3a'],'ARGENT 400':['#e9e9e9','#8a8a8a','#1a1a1a'],
     'GRAFIT 3200':['#4a4a4a','#c8c8c8','#d02a1f'],'PASTEL 160':['#9fd3bd','#f2c6d3','#f4e9b8'],'INSTA 600':['#efe6d2','#6fb3c9','#e2735a'],
     'MERIDIAN XP':['#7b4fa0','#3fbf9b','#f0c43a']}
FILT = {'AURUM 200':'sepia(.25) saturate(1.25) contrast(1.05) hue-rotate(-8deg) brightness(1.03)','NOCTA 800T':'hue-rotate(-20deg) saturate(1.1) contrast(1.06) brightness(.96)',
 'KINO 250D':'saturate(.85) contrast(1.1) sepia(.08) hue-rotate(6deg)','LUMEN 100':'saturate(1.6) contrast(1.22) hue-rotate(-4deg) brightness(.97)',
 'MERIDIAN XP':'saturate(1.5) hue-rotate(25deg) contrast(1.25) sepia(.1)','VERANO 400':'sepia(.12) saturate(.9) contrast(.94) brightness(1.06)',
 'ARGENT 400':'grayscale(1) contrast(1.15)','PASTEL 160':'saturate(.65) contrast(.85) brightness(1.12) sepia(.15)','INSTA 600':'sepia(.3) saturate(.8) contrast(.9) brightness(1.08) hue-rotate(-10deg)',
 'GRAFIT 3200':'grayscale(1) contrast(1.45) brightness(.92)'}
SB = '<div class="island"></div><div class="sb"><span>9:41</span><i class="bat"></i></div>'
def at(x, y, html, cls=''): return f'<div class="at {cls}" style="left:{x}px;top:{y}px">{html}</div>'
def bars(f, cls='bars'): return f'<span class="{cls}">' + ''.join(f'<i style="background:{c}"></i>' for c in C[f]) + '</span>'
def img(f, x, y, w, h, extra='', cls='img'): return f'<div class="{cls}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><div class="scene" style="filter:{FILT[f]}"></div>{extra}</div>'
def pair(l, v, cls=''): return f'<span class="pr {cls}"><small>{l}</small><b>{v}</b></span>'
def hudrow(f, items=None):
    items = items or [('SHUTTER','1/250'),('ISO','200'),('EV','+0.0'),('LENS','35')]
    return ''.join(pair(l, v) for l, v in items)
H = [3,4,6,9,12,15,17,18,16,14,13,15,19,24,28,26,22,18,14,12,13,16,21,27,30,24,16,10,7,5,4,6,9,6,3]
def hist(w=64, h=26):
    n = len(H); pts = ' '.join(f'{i*w/(n-1):.1f},{h - v/30*h:.1f}' for i, v in enumerate(H))
    return f'<svg class="hist" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><polygon points="0,{h} {pts} {w},{h}"/></svg>'
def meter(w=84, pos=.56, label=True):
    lab = '<span class="ml">−3</span><span class="ml c">0</span><span class="ml r">+3</span>' if label else ''
    return f'<span class="meter" style="width:{w}px"><i class="tk"></i><b style="left:{pos*100:.0f}%"></b>{lab}</span>'
def shutter(cx, cy, d=70): return f'<span class="shutter" style="left:{cx-d/2}px;top:{cy-d/2}px;width:{d}px;height:{d}px"></span>'
def roll(x, y, w=40, h=52, t='12/36'): return f'<span class="roll" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><span>{t}</span></span>'
def key(t, cls=''): return f'<span class="key {cls}">{t}</span>'
LENS = '<span class="lens"><span>26</span><span class="on">35</span><span>50</span></span>'
def film(f): return f'<span class="film"><b>{f}</b>{bars(f)}</span>'
def phone(cls, inner, land=False): return f'<div class="phone{" land" if land else ""}"><div class="screen {cls}">{inner}</div></div>'
def progress(f, used=12, total=36, w=90):
    return f'<span class="prog" style="width:{w}px"><i style="width:{used/total*100:.0f}%;background:linear-gradient(90deg,{C[f][0]},{C[f][1]})"></i></span>'

S = []
# 01 Overlay, framed
S.append(('Overlay', 'The black margin stays, but the readouts move onto the image like a cinema camera\'s monitor: labelled values along the top edge, a histogram bottom left and the needle meter bottom right. Below the frame there are only controls.', 'framed',
 phone('ov', SB + at(16,44,film('AURUM 200')) + at(234,44,'<span class="dim">12/36</span>')
   + img('AURUM 200',14,62,258,344, f'<div class="scrim t"></div><div class="scrim b"></div>' + at(10,8,hudrow('AURUM 200'),'row') + at(10,304,hist()) + at(160,312,meter()) + '<i class="cross"></i>')
   + at(16,420,key('FLASH · A')) + at(100,416,LENS) + at(230,420,key('FLIP'))
   + roll(28,488) + shutter(143,514) + at(214,500,key('FILM ▸','tall')))))

# 02 Borderless
S.append(('Borderless', 'Full bleed: the image runs under the status bar to every edge. Information sits on soft scrims at the top and bottom, and the controls float over the image. It is the most immersive of the ten and the least like a "frame".', 'borderless',
 phone('bl', img('KINO 250D',0,0,286,626, '<i class="cross"></i>','img full') + '<div class="scrim full t"></div><div class="scrim full b"></div>' + SB
   + at(18,44,film('KINO 250D')) + at(232,44,'<span class="dim">12/36</span>')
   + at(18,64,hudrow('KINO 250D'),'row')
   + at(18,440,hist()) + at(106,446,progress('KINO 250D',12,36,70)) + at(190,446,meter(78))
   + at(98,478,LENS) + roll(26,526) + shutter(143,552) + at(206,512,'<div class="stack">' + key('FILM ▸') + key('FLASH · A') + key('FLIP') + '</div>'))))

# 03 Edge labels
S.append(('Edge Labels', 'A thin border sits a few pixels outside the image, and the readouts are set into the border line itself, like the legend breaking a frame on a technical drawing. Film and frames run along the top, shutter and ISO down the sides, and the meter along the bottom.', 'framed',
 phone('el', SB + '<div class="edge" style="left:16px;top:58px;width:254px;height:352px"></div>'
   + img('AURUM 200' if False else 'NOCTA 800T',22,64,242,340,'<i class="cross"></i>')
   + at(24,51,'<span class="gap">' + film('NOCTA 800T') + '</span>') + at(212,51,'<span class="gap dim">12/36</span>')
   + at(8,170,'<span class="gap vert">S 1/250</span>') + at(266,170,'<span class="gap vert r">ISO 800</span>')
   + at(84,404,'<span class="gap">' + meter(90,.6,False) + '<span class="redt">+0.3</span></span>')
   + at(98,430,LENS) + roll(28,498) + shutter(143,524) + at(206,486,'<div class="stack">' + key('FILM ▸') + key('FLASH · A') + key('FLIP') + '</div>'))))

# 04 Corner HUD
S.append(('Corners', 'Borderless, with the information pushed into four corner blocks like an instrument display: film top left, frames top right, exposure bottom left and the meter bottom right. The middle of the image stays completely clean.', 'borderless',
 phone('cn', img('LUMEN 100',0,0,286,626,'','img full') + '<div class="scrim full b"></div>' + SB
   + '<i class="cb tl"></i><i class="cb tr"></i><i class="cb bl"></i><i class="cb br"></i>'
   + at(22,58,'<div class="blk">' + film('LUMEN 100') + '<small>36 EXP · SLIDE</small></div>') + at(206,58,'<div class="blk r"><b class="big">12</b><small>OF 36</small></div>')
   + at(22,398,'<div class="blk">' + pair('S','1/250') + pair('ISO','100') + '</div>') + at(184,404,'<div class="blk r">' + meter(80) + '</div>')
   + at(98,458,LENS) + roll(26,520) + shutter(143,546) + at(206,506,'<div class="stack">' + key('FILM ▸') + key('FLASH · A') + key('FLIP') + '</div>'))))

# 05 Frame lines
S.append(('Frame Lines', 'The preview fills the screen, but the area that will be captured is marked with thin frame lines and everything outside is dimmed, like the guides on a cinema monitor. The readouts are printed in the dimmed zone, so the black margin comes back as a translucent one.', 'hybrid',
 phone('fl', img('VERANO 400',0,0,286,626,'','img full') + '<div class="cap" style="left:14px;top:66px;width:258px;height:344px"><i class="cross"></i></div>' + SB
   + at(16,46,film('VERANO 400')) + at(232,46,'<span class="dim">12/36</span>')
   + at(14,418,hudrow('VERANO 400',[('S','1/250'),('ISO','400'),('EV','+0.0')]),'row') + at(186,422,meter(84))
   + at(98,460,LENS) + roll(26,520) + shutter(143,546) + at(206,506,'<div class="stack">' + key('FILM ▸') + key('FLASH · A') + key('FLIP') + '</div>'))))

# 06 Scope
wave = ' '.join(f'{x},{22 - 14*abs(math.sin(x/9)) * (0.6 + 0.4*math.sin(x/23)) - 3:.1f}' for x in range(0, 243, 3))
S.append(('Scope', 'The meter is a waveform scope laid across the bottom of the image, as on a cinema monitor. A faint trace shows the brightness across the scene, and a red hairline marks where highlights would clip.', 'framed',
 phone('sc', SB + at(16,44,film('MERIDIAN XP')) + at(234,44,'<span class="dim">12/36</span>')
   + img('MERIDIAN XP',14,62,258,344, '<div class="scrim t"></div>' + at(10,8,hudrow('MERIDIAN XP'),'row')
       + f'<svg class="wave" viewBox="0 0 243 30" preserveAspectRatio="none"><polyline points="{wave}"/><line x1="0" y1="3" x2="243" y2="3"/></svg><span class="clip">CLIP</span><i class="cross"></i>')
   + at(16,420,key('FLASH · A')) + at(100,416,LENS) + at(230,420,key('FLIP'))
   + roll(28,488) + shutter(143,514) + at(214,500,key('FILM ▸','tall')))))

# 07 Counter
S.append(('Counter', 'Borrowing the large timecode from cinema cameras, but counting frames: a big outlined frame number sits at the top of a borderless view, with small readouts on each side. On a roll of 36, the count is the most "film" number there is.', 'borderless',
 phone('ct', img('INSTA 600',0,0,286,626,'<i class="cross"></i>','img full') + '<div class="scrim full t"></div><div class="scrim full b"></div>' + SB
   + at(18,46,film('INSTA 600')) + at(18,70,pair('S','1/125')) + at(18,96,pair('ISO','600'))
   + at(0,58,'<span class="count">12<small>/36</small></span>','ctr') + at(232,70,pair('EV','+0.0','r')) + at(232,96,pair('LENS','35','r'))
   + at(100,440,meter(86)) + at(98,474,LENS) + roll(26,526) + shutter(143,552) + at(206,512,'<div class="stack">' + key('FILM ▸') + key('FLASH · A') + key('FLIP') + '</div>'))))

# 08 Signature HUD
f8 = 'PASTEL 160'
items8 = [('S','1/250',C[f8][0]),('ISO','160',C[f8][1]),('EV','+0.0',C[f8][2]),('LENS','35','#5f6167')]
row8 = ''.join(f'<span class="pr ul" style="--u:{u}"><small>{l}</small><b>{v}</b></span>' for l, v, u in items8)
S.append(('Signature HUD', 'The film\'s colors become the HUD itself. Each value along the top is underlined in one of the film\'s colors, and a thin stripe runs down the edge of the image. Change film and the whole interface retints, while red stays reserved for the meter needle.', 'framed',
 phone('sh', SB + at(16,44,'<span class="film"><b>PASTEL 160</b></span>') + at(234,44,'<span class="dim">12/36</span>')
   + img(f8,14,62,258,344, '<div class="scrim t"></div>' + at(10,8,row8,'row') + '<span class="stripe">' + ''.join(f'<i style="background:{c}"></i>' for c in C[f8]) + '</span>' + at(160,312,meter()) + '<i class="cross"></i>')
   + at(16,420,key('FLASH · A')) + at(100,416,LENS) + at(230,420,key('FLIP'))
   + roll(28,488) + shutter(143,514) + at(214,500,key('FILM ▸','tall')))))

# 09 Split monitor
S.append(('Split Monitor', 'The image runs borderless across the top two-thirds, and the bottom is a solid instrument panel modelled on a cinema camera\'s status bar: histogram, roll progress shown in the film\'s colors, and the meter, with one row of controls below.', 'hybrid',
 phone('sm', img('ARGENT 400',0,0,286,412,'<i class="cross"></i>','img full') + '<div class="scrim full t"></div>' + SB
   + at(18,46,film('ARGENT 400')) + at(18,66,hudrow('ARGENT 400',[('S','1/250'),('ISO','400'),('EV','+0.0'),('LENS','35')]),'row')
   + '<div class="panel"></div>'
   + at(14,424,'<div class="cell">' + hist(70,28) + '</div>') + at(100,424,'<div class="cell"><small>ROLL</small><b>12 / 36</b>' + progress('ARGENT 400',12,36,70) + '</div>') + at(186,424,'<div class="cell">' + meter(76) + '</div>')
   + at(98,484,LENS) + roll(26,530) + shutter(143,556) + at(206,516,'<div class="stack">' + key('FILM ▸') + key('FLASH · A') + key('FLIP') + '</div>'))))

# 10 Landscape (wide)
S.append(('Landscape', 'The closest to the Blackmagic layout, held sideways. The image runs borderless to the left edge. Labelled values sit along the top with the frame count in the middle, and histogram, roll progress and meter sit along the bottom. A solid control column on the right holds flash, flip, the shutter, the lens and the roll.', 'borderless',
 phone('ls', img('NOCTA 800T',0,0,520,286,'<i class="cross"></i>','img full') + '<div class="scrim lt"></div><div class="scrim lb"></div>' + '<div class="island land-island"></div>'
   + at(44,14,'<span class="pr"><small>FILM</small><b class="fb">NOCTA 800T ' + bars('NOCTA 800T') + '</b></span>' + pair('SHUTTER','1/250') + pair('ISO','800') + '<span class="count sm">12<small>/36</small></span>' + pair('EV','+0.0') + pair('LENS','35'),'row wide')
   + at(44,236,hist(70,28)) + at(210,246,progress('NOCTA 800T',12,36,100)) + at(400,240,meter(84))
   + '<div class="col">' + key('FLASH · A') + key('FLIP') + '<span class="shutter in"></span>' + key('FILM ▸') + '<span class="lens v"><span>26</span><span class="on">35</span><span>50</span></span>' + '</div>', land=True)))

cards = '\n'.join(f'''<figure class="card{" wide" if n=="Landscape" else ""}"><div class="ph">{html}</div><figcaption><span class="no">{i:02d} · {kind}</span><h3>{n}</h3><p>{d}</p></figcaption></figure>'''
                  for i, (n, d, kind, html) in enumerate(S, 1))

CSS = r"""
/* Layout: dark gallery of ten static screens; nine portrait in a grid, one landscape across a full row. Single dark look by design. */
:root{--bg:#070708;--ink:#e9eaec;--dim:#7a7c82;--line:#1f2023;--red:#e2231a;
  --sans:'Archivo',system-ui,-apple-system,'Segoe UI',sans-serif;--mono:'JetBrains Mono',ui-monospace,Menlo,monospace;color-scheme:dark}
*{box-sizing:border-box}
html,body{background:var(--bg);color:var(--ink)}
body{font-family:var(--sans);font-size:15px;line-height:1.55;padding-inline:clamp(16px,4vw,56px);padding-block:0 80px}
.wrap{max-width:1180px;margin:0 auto}
.hero{padding-block:72px 32px;display:grid;gap:16px;border-bottom:1px solid var(--line);margin-bottom:56px}
.eyebrow{font:500 11px var(--mono);letter-spacing:.16em;text-transform:uppercase;color:var(--dim)}
h1{margin:0;font-weight:600;font-size:clamp(30px,5vw,54px);line-height:1.02;letter-spacing:-.03em;text-wrap:balance}
h1 span{display:inline-block;width:.9em;height:2px;background:var(--red);vertical-align:.25em;margin-left:.2em}
.lede{margin:0;color:#a8aab0;max-width:68ch}
.kept{display:flex;flex-wrap:wrap;gap:8px}
.kept span{font:500 11px var(--mono);color:#cfd0d4;border:1px solid #2a2b2e;border-radius:3px;padding:4px 9px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:72px 32px}
.card{margin:0;display:grid;gap:18px;justify-items:center;align-content:start}
.card.wide{grid-column:1/-1}
.card .ph{max-width:100%;overflow-x:auto}
.card figcaption{max-width:300px;display:grid;gap:5px}
.card.wide figcaption{max-width:640px}
.no{font:500 11px var(--mono);color:var(--dim);letter-spacing:.06em;text-transform:uppercase}
.card h3{margin:0;font-weight:600;font-size:19px;letter-spacing:-.01em}
.card p{margin:0;font-size:14px;color:#a8aab0}
footer{margin-top:72px;padding-top:18px;border-top:1px solid var(--line);color:var(--dim);font-size:13.5px;max-width:70ch}

/* ---- phone ---- */
.phone{width:300px;height:640px;border-radius:50px;padding:7px;flex:none;background:linear-gradient(140deg,#3a3b3f,#151618 40%,#2a2b2e 70%,#111);box-shadow:0 0 0 1px #000,0 30px 55px -20px rgba(0,0,0,.85)}
.phone.land{width:640px;height:300px}
.screen{position:relative;width:100%;height:100%;border-radius:43px;overflow:hidden;background:#000;color:#e9eaec;font-family:var(--sans);--ink:#e9eaec;--dim:#8a8c92}
.island{position:absolute;top:10px;left:50%;width:84px;height:24px;border-radius:14px;background:#000;transform:translateX(-50%);z-index:9}
.land-island{top:50%;left:10px;width:24px;height:84px;transform:translateY(-50%)}
.sb{position:absolute;left:0;right:0;top:0;height:42px;display:flex;align-items:center;justify-content:space-between;padding:6px 26px 0;font:600 12px system-ui,sans-serif;z-index:5}
.bat{display:inline-block;width:22px;height:10px;border:1px solid currentColor;border-radius:3px;position:relative}
.bat::before{content:'';position:absolute;inset:1.5px 6px 1.5px 1.5px;background:currentColor;border-radius:1px}
.at{position:absolute;display:flex;align-items:center;gap:8px;white-space:nowrap;z-index:4}
.at.row{gap:14px}
.at.row.wide{gap:24px;align-items:flex-end}
.at.ctr{left:0!important;right:0;justify-content:center}
.img{position:absolute;overflow:hidden;background:#111}
.img.full{z-index:0}
.scene{position:absolute;inset:0;background:var(--scene) center/cover}
.cross{position:absolute;left:50%;top:50%;width:16px;height:16px;transform:translate(-50%,-50%);z-index:2}
.cross::before,.cross::after{content:'';position:absolute;background:rgba(255,255,255,.85)}
.cross::before{left:50%;top:0;bottom:0;width:1px}.cross::after{top:50%;left:0;right:0;height:1px}
.scrim{position:absolute;left:0;right:0;pointer-events:none;z-index:1}
.scrim.t{top:0;height:48px;background:linear-gradient(rgba(0,0,0,.55),transparent)}
.scrim.b{bottom:0;height:60px;background:linear-gradient(transparent,rgba(0,0,0,.6))}
.scrim.full.t{height:130px;background:linear-gradient(rgba(0,0,0,.7),transparent)}
.scrim.full.b{height:250px;background:linear-gradient(transparent,rgba(0,0,0,.82) 45%)}
.scrim.lt{top:0;left:0;width:520px;height:70px;background:linear-gradient(rgba(0,0,0,.65),transparent)}
.scrim.lb{bottom:0;left:0;width:520px;height:80px;top:auto;background:linear-gradient(transparent,rgba(0,0,0,.7))}
.dim{font:500 9.5px var(--mono);color:var(--dim)}
.film{display:inline-flex;align-items:center;gap:7px}
.film b{font:600 10px var(--mono);letter-spacing:.08em}
.bars{display:inline-flex;gap:1.5px}
.bars i{width:9px;height:3px}
.pr{display:grid;gap:0;line-height:1.15}
.pr small{font:500 6.5px var(--sans);letter-spacing:.12em;color:rgba(255,255,255,.62)}
.pr b{font:500 11px var(--sans);letter-spacing:.01em}
.pr.r{text-align:right}
.pr.ul b{box-shadow:inset 0 -2px 0 var(--u);padding-bottom:2px}
.hist{display:block;background:rgba(0,0,0,.35);border:1px solid rgba(255,255,255,.18);border-radius:2px}
.hist polygon{fill:rgba(255,255,255,.55)}
.meter{position:relative;display:block;height:20px}
.meter .tk{position:absolute;left:0;right:0;top:2px;height:7px;background:repeating-linear-gradient(90deg,rgba(255,255,255,.75) 0 1px,transparent 1px calc((100% - 1px)/18));
  -webkit-mask:linear-gradient(#000 0 0) top/100% 3px no-repeat,repeating-linear-gradient(90deg,#000 0 1px,transparent 1px calc((100% - 1px)/6));mask:linear-gradient(#000 0 0) top/100% 3px no-repeat,repeating-linear-gradient(90deg,#000 0 1px,transparent 1px calc((100% - 1px)/6))}
.meter b{position:absolute;top:-3px;width:1px;height:14px;background:var(--red)}
.ml{position:absolute;bottom:-1px;left:0;font:500 6.5px var(--mono);color:rgba(255,255,255,.6)}
.ml.c{left:50%;transform:translateX(-50%)}.ml.r{left:auto;right:0}
.redt{font:500 8px var(--mono);color:var(--red);letter-spacing:.06em}
.lens{display:flex;gap:4px}
.lens span{font:500 11px var(--mono);color:rgba(255,255,255,.5);padding:4px 9px;border-bottom:1px solid transparent}
.lens span.on{color:#fff;border-bottom-color:#fff}
.lens.v{flex-direction:column;gap:0}
.lens.v span{padding:1px 4px;border-bottom:0;border-left:1px solid transparent;font-size:10px}
.lens.v span.on{border-left-color:#fff}
.shutter{position:absolute;border-radius:50%;box-shadow:inset 0 0 0 1.5px #e9eaec;z-index:4}
.shutter::after{content:'';position:absolute;inset:6px;border-radius:50%;background:#e9eaec}
.shutter.in{position:relative;display:block;width:58px;height:58px;flex:none}
.roll{position:absolute;border-radius:3px;overflow:hidden;border:1px solid rgba(255,255,255,.45);background:var(--scene) center/cover;z-index:4}
.roll>span{position:absolute;left:0;right:0;bottom:0;font:500 7px var(--mono);text-align:center;padding:6px 0 2px;background:linear-gradient(transparent,rgba(0,0,0,.85))}
.key{display:inline-grid;place-items:center;font:500 8.5px var(--mono);letter-spacing:.08em;color:#e9eaec;padding:6px 9px;border:1px solid rgba(255,255,255,.28);border-radius:3px;background:rgba(0,0,0,.35);-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px)}
.key.tall{padding:16px 9px}
.stack{display:grid;gap:6px}
.prog{display:block;height:3px;background:rgba(255,255,255,.18);border-radius:2px;overflow:hidden}
.prog i{display:block;height:100%}

/* 03 edge labels */
.edge{position:absolute;border:1px solid #55575c}
.gap{display:inline-flex;align-items:center;gap:6px;background:#000;padding:0 6px;font:500 9.5px var(--mono)}
.gap.vert{writing-mode:vertical-rl;transform:rotate(180deg);padding:6px 0}
.gap.vert.r{transform:none}
.el .gap .meter{width:90px}
/* 04 corners */
.cb{position:absolute;width:18px;height:18px;border:0 solid rgba(255,255,255,.75);z-index:4}
.cb.tl{left:12px;top:52px;border-left-width:1px;border-top-width:1px}.cb.tr{right:12px;top:52px;border-right-width:1px;border-top-width:1px}
.cb.bl{left:12px;top:424px;border-left-width:1px;border-bottom-width:1px}.cb.br{right:12px;top:424px;border-right-width:1px;border-bottom-width:1px}
.blk{display:grid;gap:3px}
.blk.r{justify-items:end;text-align:right}
.blk small{font:500 6.5px var(--mono);letter-spacing:.12em;color:rgba(255,255,255,.65)}
.blk .big{font:300 26px/1 var(--sans);letter-spacing:-.02em}
.cn .blk .pr{display:inline-grid;margin-right:12px}
.cn .at:has(.pr) .blk{display:flex;gap:14px}
/* 05 frame lines */
.cap{position:absolute;box-shadow:0 0 0 1px rgba(255,255,255,.85),0 0 0 999px rgba(0,0,0,.62);z-index:1}
/* 06 scope */
.wave{position:absolute;left:8px;right:8px;bottom:8px;height:34px;width:calc(100% - 16px);background:rgba(0,0,0,.35);border:1px solid rgba(255,255,255,.15);z-index:2}
.wave polyline{fill:none;stroke:rgba(255,255,255,.75);stroke-width:1;vector-effect:non-scaling-stroke}
.wave line{stroke:var(--red);stroke-width:1;vector-effect:non-scaling-stroke}
.clip{position:absolute;right:12px;bottom:44px;font:500 6.5px var(--mono);color:var(--red);letter-spacing:.12em;z-index:2}
/* 07 counter */
.count{font:200 72px/1 var(--sans);letter-spacing:-.03em;color:transparent;-webkit-text-stroke:1px rgba(255,255,255,.95)}
.count small{font-size:16px;-webkit-text-stroke:0;color:rgba(255,255,255,.7);margin-left:2px}
.count.sm{font-size:30px;align-self:center}
.count.sm small{font-size:10px}
/* 08 signature hud */
.stripe{position:absolute;left:0;top:60px;width:3px;height:90px;display:flex;flex-direction:column;z-index:2}
.stripe i{flex:1}
/* 09 split */
.panel{position:absolute;left:0;right:0;top:412px;bottom:0;background:#060607;border-top:1px solid #1d1e20;z-index:2}
.cell{display:grid;gap:4px;align-content:center;height:46px;padding:0 8px;border:1px solid #1d1e20;border-radius:4px;width:82px}
.cell small{font:500 6.5px var(--mono);letter-spacing:.12em;color:var(--dim)}
.cell b{font:500 10px var(--mono)}
.sm .cell .hist{width:64px}
/* 10 landscape */
.ls .col{position:absolute;right:0;top:0;bottom:0;width:106px;background:#060607;border-left:1px solid #1d1e20;display:flex;flex-direction:column;align-items:center;justify-content:space-evenly;z-index:4}
.ls .col .key{width:78px;padding:5px 0}
.fb{display:inline-flex;align-items:center;gap:6px}
"""

body = f"""<title>Film Camera UI · On-Image HUD</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@200;300;400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap">
<style>{CSS}</style>
<div class="wrap">
  <header class="hero">
    <span class="eyebrow">Working title pending · Round 10 · Static mockups</span>
    <h1>Information on the image<span></span></h1>
    <p class="lede">Ten screens testing the cinema-camera idea of putting information on the image itself, in three families: framed (black margin, readouts on the image), borderless (full bleed) and hybrid. Everything from earlier rounds still applies.</p>
    <div class="kept"><span>simple, tiny details</span><span>red only as hairlines or text</span><span>film color signatures</span><span>film name at the top · FILM ▸ key</span><span>analog meter</span><span>lens · flash · flip · roll · shutter</span></div>
  </header>
  <div class="grid">
{cards}
  </div>
  <footer>Round 10. Earlier rounds are unchanged on their own pages.</footer>
</div>
<script>
(() => {{
const scene = document.createElement('canvas'); scene.width = 600; scene.height = 800;
{paint}
document.documentElement.style.setProperty('--scene', 'url(' + scene.toDataURL('image/jpeg', .85) + ')');
}})();
</script>
"""
(root / 'hud.html').write_text(body)
head = '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
i = body.index('</style>') + len('</style>')
(root / 'hud-standalone.html').write_text(head + body[:i] + '\n</head><body>\n' + body[i:] + '</body></html>\n')
print('ok', len(body))
