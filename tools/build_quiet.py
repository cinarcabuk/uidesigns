"""Builds quiet.html (artifact source) and quiet-standalone.html: ten static screens, restrained precision plus one bold gesture each."""
import pathlib
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
def img(f, x, y, w, h, extra='', cls='img'): return f'<div class="{cls}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><div class="scene" style="filter:{FILT[f]}"></div>{extra}</div>'
def bars(f, w=27, h=3, cls='bars'): return f'<span class="{cls}" style="width:{w}px;height:{h}px">' + ''.join(f'<i style="background:{c}"></i>' for c in C[f]) + '</span>'
def ring(cx, cy, d=64, cls=''): return f'<span class="ring {cls}" style="left:{cx-d/2}px;top:{cy-d/2}px;width:{d}px;height:{d}px"></span>'
def roll(x, y, w=36, h=46): return f'<span class="roll" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"></span>'
def t(s, cls='t'): return f'<span class="{cls}">{s}</span>'
def phone(cls, inner): return f'<div class="phone"><div class="screen {cls}">{inner}</div></div>'

Q = []
# 01 Bright lines (borderless)
f = 'AURUM 200'
Q.append(('Bright Lines', 'borderless', 'Full bleed. A projected bright-line frame floats over the image, with a rangefinder patch in the middle where a faint second image slides into place as you focus. Everything else is a whisper: one line of small numbers, a hollow shutter, and "35" in red beside the frame.',
 phone('bright', img(f,0,0,286,626,'<div class="dimmer"></div>','img full') + SB
  + '<div class="bl" style="left:34px;top:116px;width:218px;height:290px"><i></i><i></i><i></i><i></i></div>'
  + at(34,100,t('35','red s')) + '<div class="patch"><i></i></div>'
  + at(22,50,t('AURUM 200') + bars(f)) + at(240,50,t('12','s'))
  + '<div class="fade b"></div>'
  + at(0,450,'<span class="line">1/250&nbsp;&nbsp;&nbsp;ƒ1.8&nbsp;&nbsp;&nbsp;ISO 200&nbsp;&nbsp;&nbsp;<em>−·|·+</em></span>','ctr')
  + ring(143,540,62,'hollow') + roll(30,518) + at(214,532,t('FILM','s key')))))

# 02 Element
f = 'AURUM 200'
Q.append(('Element', 'framed', 'Each film is an element on its own periodic table: Au for Aurum, No for Nocta, Lu for Lumen. The tile carries the symbol in red, the speed as its atomic number and the three colors as bands along the bottom. Settings sit beside it in a ruled table.',
 phone('elem', SB + at(16,46,t('AURUM 200','s')) + at(236,46,t('12/36','s dim'))
  + img(f,16,62,254,300)
  + '<div class="tile" style="left:16px;top:376px"><span class="n">200</span><span class="m">36</span><b>Au</b><span class="nm">Aurum</span>' + bars(f,94,5,'tb') + '</div>'
  + at(126,378,'<div class="tbl"><span><small>SHUTTER</small>1/250</span><span><small>APERTURE</small>1.8</span><span><small>EXPOSURE</small>±0.0</span><span><small>LENS</small>35</span></div>')
  + at(126,470,'<span class="hair"><b></b></span>')
  + roll(22,530) + at(78,544,t('◂ FILM ▸','s key')) + ring(232,552,58))))

# 03 Engraved
f = 'NOCTA 800T'
dof = ''.join(f'<i style="left:calc(50% - {o}px);background:{c}"></i><i style="left:calc(50% + {o}px);background:{c}"></i>' for o, c in zip([18,40,64], C[f]))
Q.append(('Engraved', 'framed', 'Settings are engraved scales, the way numbers are cut into a lens barrel. The depth-of-field marks are paint-filled in the film\'s three colors, so the stock is written into the scale itself. Red is used once, for B.',
 phone('eng', SB + at(16,46,t('NOCTA 800T','s')) + at(236,46,t('12/36','s dim'))
  + img(f,16,62,254,338)
  + f'<div class="scale" style="top:414px"><div class="nums"><span>∞</span><span>10</span><span>5</span><span class="on">3</span><span>2</span><span>1.5</span><span>1</span><span>.7</span></div><div class="dof">{dof}<b></b></div></div>'
  + at(16,470,'<div class="spd"><span>1000</span><span>500</span><span class="on">250</span><span>125</span><span>60</span><span>30</span><span>15</span><span class="red">B</span></div>')
  + roll(26,526) + ring(143,552,60) + at(214,546,t('FILM','s key')))))

# 04 Striped type (borderless)
f = 'NOCTA 800T'
stripe = ','.join(f'{c} {i*6}px {i*6+4}px,transparent {i*6+4}px {i*6+6}px' for i, c in enumerate(C[f]))
Q.append(('Striped', 'borderless', 'A teal cinema grade over the full-bleed image, and the film\'s name set huge in horizontal stripes of its own three colors. Change film and the stripes change. Around it, the controls stay tiny and exact.',
 phone('striped', img(f,0,0,286,626,'<div class="teal"></div>','img full') + SB
  + at(20,50,t('800T · TUNGSTEN','s')) + at(236,50,t('12/36','s'))
  + f'<div class="sword" style="background-image:repeating-linear-gradient(180deg,{stripe})">NOCTA</div>'
  + at(20,470,'<span class="line l">1/250 · ƒ1.8 · ISO 800 · ±0</span>')
  + ring(143,552,62,'hollow') + roll(26,530) + at(214,544,t('FILM ▸','s key')))))

# 05 Segment gold
f = 'MERIDIAN XP'
Q.append(('Segment', 'framed', 'One number is allowed to be loud: the shutter speed, set huge in gold segments like an old stage display. The rest is small grey type. The film\'s colors sit as three segment blocks under the number.',
 phone('seg', SB + at(16,46,t('MERIDIAN XP','s')) + at(236,46,t('12/36','s dim'))
  + img(f,16,62,254,320)
  + at(16,392,'<span class="segnum"><small>1/</small>250</span>')
  + at(20,470,'<span class="blocks">' + ''.join(f'<i style="background:{c}"></i>' for c in C[f]) + '</span>')
  + at(110,470,'<span class="line l dim">ISO 200 · ƒ1.8 · ±0.0</span>')
  + roll(26,526) + ring(143,552,60) + at(214,546,t('FILM ▸','s key')))))

# 06 Test card
f = 'KINO 250D'
Q.append(('Test Card', 'framed', 'The control deck is a test card: orange, ruled with a black grid, with a circle and diagonals locking everything to the center. The shutter sits dead center on the crosshair, and the film\'s colors appear as calibration patches.',
 phone('card', SB + at(16,46,t('KINO 250D','s')) + at(236,46,t('12/36','s dim'))
  + img(f,16,62,254,330)
  + '<div class="deckcard"><i class="circ"></i><i class="diag"></i></div>'
  + at(18,412,'<div class="patches">' + ''.join(f'<i style="background:{c}"></i>' for c in C[f]) + '<i style="background:#fff"></i><i style="background:#777"></i><i style="background:#000"></i></div>')
  + at(18,590,t('1/250 · ISO 200 · ƒ1.8','s ink')) + at(222,590,t('±0','s ink'))
  + '<span class="cardshut"></span>' + roll(24,500,34,44) + at(222,506,t('FILM ▸','s key ink')))))

# 07 White body
f = 'VERANO 400'
Q.append(('Print', 'framed', 'A pale silver-white body with the live image set small, like a print on a gallery wall. A huge amount of quiet space, black type, and a single red rule under the film\'s name. The palette stands beside the print as three thin bars.',
 phone('white', SB + at(38,70,t('VERANO 400','s ink')) + '<i class="rule" style="left:38px;top:86px;width:60px"></i>'
  + at(214,70,t('12 / 36','s ink'))
  + img(f,38,104,200,266)
  + '<span class="vbars" style="left:248px;top:104px">' + ''.join(f'<i style="background:{c}"></i>' for c in C[f]) + '</span>'
  + at(38,384,t('1/250 &nbsp; ƒ1.8 &nbsp; ISO 400 &nbsp; ±0','s ink'))
  + at(38,404,'<span class="hair ink"><b></b></span>')
  + ring(143,520,66,'ink') + at(38,512,t('FLASH','s ink key')) + at(210,512,t('FILM ▸','s ink key')))))

# 08 Perforated
f = 'LUMEN 100'
Q.append(('Perforated', 'framed', 'The deck is perforated metal: a fine grid of holes in a dark teal panel, like a speaker grille. Three of the holes are lit from behind in the film\'s colors. The shutter is a plain white disc and the release is marked in small red letters.',
 phone('perf', SB + at(16,46,t('LUMEN 100','s')) + at(236,46,t('12/36','s dim'))
  + img(f,16,62,254,330)
  + '<div class="grille"></div>'
  + ''.join(f'<i class="lit" style="left:{x}px;top:438px;background:{c};box-shadow:0 0 8px {c}"></i>' for x, c in zip([28,40,52], C[f]))
  + at(70,432,t('1/250 · ISO 100 · ƒ1.8 · ±0','s'))
  + '<span class="disc"></span>' + at(127,598,t('REL','red s'))
  + roll(26,520) + at(214,534,t('FILM ▸','s key')))))

# 09 Red wordmark (borderless)
f = 'AURUM 200'
Q.append(('Wordmark', 'borderless', 'The image fills the screen and the film\'s name is set across it in enormous red letters, cropped by the edge as if the stock were stamped onto the scene. A thin three-color rule sits under the word, and everything else stays small.',
 phone('word', img(f,0,0,286,626,'','img full') + '<div class="fade b strong"></div>' + SB
  + at(20,50,t('12/36','s')) + at(186,50,t('ISO 200 · ƒ1.8','s'))
  + '<div class="rword">AURUM</div>' + '<span class="wbar">' + ''.join(f'<i style="background:{c}"></i>' for c in C[f]) + '</span>'
  + at(20,506,t('1/250 · ±0','s')) + ring(232,560,60,'hollow') + roll(20,540) + at(76,556,t('FILM ▸','s key')))))

# 10 Top view
f = 'ARGENT 400'
speeds = ['1000','500','250','125','60','30','15','8','4','2','1','B']
dial = ''.join(f'<span class="{"on" if s=="250" else ("red" if s=="B" else "")}" style="--a:{(i-2)*30}deg">{s}</span>' for i, s in enumerate(speeds))
collar = ''.join(f'<i style="inset:{k*3}px;border-color:{c}"></i>' for k, c in enumerate(C[f]))
Q.append(('Top Plate', 'framed', 'Below the image you look down onto the top of the camera: a shutter-speed dial with engraved numbers, the release button with three thin collars in the film\'s colors, and a small frame-counter window.',
 phone('topv', SB + at(16,46,t('ARGENT 400','s')) + at(214,46,t('ƒ1.8 · 35','s dim'))
  + img(f,16,62,254,320)
  + '<div class="plate"></div>'
  + f'<div class="dialt" style="left:30px;top:430px">{dial}<i class="cap"></i></div><i class="idx" style="left:85px;top:418px"></i>'
  + f'<span class="release" style="left:168px;top:452px">{collar}<b></b></span>'
  + '<span class="cwin" style="left:232px;top:438px">12</span>' + at(226,476,t('ISO 400','s'))
  + roll(26,560,32,40) + at(204,570,t('FILM ▸','s key')))))

cards = '\n'.join(f'''<figure class="card"><div class="ph">{html}</div><figcaption><span class="no">{i:02d} · {k}</span><h3>{n}</h3><p>{d}</p></figcaption></figure>'''
                  for i, (n, k, d, html) in enumerate(Q, 1))
pal = ''.join(f'<span class="pf"><span class="sw">{"".join(f"<i style=background:{c}></i>" for c in cols)}</span>{n}</span>' for n, cols in C.items())

CSS = r"""
/* Layout: a near-empty black page with one red rule; ten phones in a grid. Each screen: restraint plus one bold gesture, palette always visible. Single dark look by design. */
:root{--bg:#050505;--ink:#ededed;--dim:#77797e;--line:#1b1b1d;--red:#e2231a;
  --sans:'Archivo',system-ui,-apple-system,'Segoe UI',sans-serif;--mono:'JetBrains Mono',ui-monospace,Menlo,monospace;--dot:'Doto','JetBrains Mono',monospace;color-scheme:dark}
*{box-sizing:border-box}
html,body{background:var(--bg);color:var(--ink)}
body{font-family:var(--sans);font-size:15px;line-height:1.55;padding-inline:clamp(16px,4vw,56px);padding-block:0 80px}
.wrap{max-width:1180px;margin:0 auto}
.hero{padding-block:88px 36px;display:grid;gap:18px;border-bottom:1px solid var(--line);margin-bottom:56px}
.eyebrow{font:500 10.5px var(--mono);letter-spacing:.2em;text-transform:uppercase;color:var(--dim)}
h1{margin:0;font-weight:500;font-size:clamp(30px,5vw,56px);line-height:1;letter-spacing:-.035em}
.rule-h{width:56px;height:2px;background:var(--red)}
.lede{margin:0;color:#a3a5aa;max-width:60ch}
.pals{display:flex;flex-wrap:wrap;gap:10px 18px;margin-top:6px}
.pf{display:inline-flex;align-items:center;gap:8px;font:500 10px var(--mono);letter-spacing:.06em;color:#bcbdc1}
.sw{display:flex;width:30px;height:8px}
.sw i{flex:1}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:72px 32px}
.card{margin:0;display:grid;gap:18px;justify-items:center;align-content:start}
.card figcaption{max-width:300px;display:grid;gap:5px}
.no{font:500 10.5px var(--mono);color:var(--dim);letter-spacing:.1em;text-transform:uppercase}
.card h3{margin:0;font-weight:500;font-size:19px;letter-spacing:-.01em}
.card p{margin:0;font-size:14px;color:#a3a5aa}
footer{margin-top:72px;padding-top:18px;border-top:1px solid var(--line);color:var(--dim);font-size:13.5px}

/* ---- phone ---- */
.phone{width:300px;height:640px;border-radius:50px;padding:7px;background:linear-gradient(140deg,#3a3b3f,#151618 40%,#2a2b2e 70%,#111);box-shadow:0 0 0 1px #000,0 30px 55px -20px rgba(0,0,0,.85)}
.screen{position:relative;width:286px;height:626px;border-radius:43px;overflow:hidden;background:#000;color:#ededed;font-family:var(--sans)}
.island{position:absolute;top:10px;left:50%;width:84px;height:24px;border-radius:14px;background:#000;transform:translateX(-50%);z-index:9}
.sb{position:absolute;left:0;right:0;top:0;height:42px;display:flex;align-items:center;justify-content:space-between;padding:6px 26px 0;font:600 12px system-ui,sans-serif;z-index:6}
.bat{display:inline-block;width:22px;height:10px;border:1px solid currentColor;border-radius:3px;position:relative}
.bat::before{content:'';position:absolute;inset:1.5px 6px 1.5px 1.5px;background:currentColor;border-radius:1px}
.at{position:absolute;display:flex;align-items:center;gap:8px;white-space:nowrap;z-index:5}
.at.ctr{left:0!important;right:0;justify-content:center}
.img{position:absolute;overflow:hidden;background:#111}
.scene{position:absolute;inset:0;background:var(--scene) center/cover}
.t{font:500 9.5px var(--mono);letter-spacing:.1em;color:#ededed}
.s{font:500 8.5px var(--mono);letter-spacing:.12em}
.dim{color:var(--dim)}
.red{color:var(--red)}
.ink{color:#151515}
.key{padding:6px 10px;border:1px solid rgba(255,255,255,.3);border-radius:2px}
.key.ink{border-color:rgba(0,0,0,.35)}
.bars{display:inline-flex}
.bars i{flex:1}
.ring{position:absolute;border-radius:50%;background:#ededed;box-shadow:0 0 0 3px #000,0 0 0 4px #6d6f74;z-index:5}
.ring.hollow{background:transparent;box-shadow:inset 0 0 0 1.5px #ededed}
.ring.hollow::after{content:'';position:absolute;inset:7px;border-radius:50%;box-shadow:inset 0 0 0 1px rgba(255,255,255,.5)}
.ring.ink{background:transparent;box-shadow:inset 0 0 0 1.5px #151515}
.ring.ink::after{content:'';position:absolute;inset:6px;border-radius:50%;background:#151515}
.roll{position:absolute;border-radius:2px;border:1px solid rgba(255,255,255,.4);background:var(--scene) center/cover;z-index:5}
.line{font:500 9.5px var(--mono);letter-spacing:.1em;color:#ededed}
.line em{font-style:normal;color:var(--red)}
.hair{position:relative;display:block;width:140px;height:1px;background:#3a3b3e}
.hair b{position:absolute;left:54%;top:-5px;width:1px;height:11px;background:var(--red)}
.hair.ink{width:200px;background:#9a9b9e}
.fade{position:absolute;left:0;right:0;z-index:1}
.fade.b{bottom:0;height:240px;background:linear-gradient(transparent,rgba(0,0,0,.75) 55%)}
.fade.b.strong{height:300px;background:linear-gradient(transparent,rgba(0,0,0,.6) 40%,rgba(0,0,0,.9))}

/* 01 bright lines */
.dimmer{position:absolute;inset:0;background:rgba(0,0,0,.28)}
.bl{position:absolute;z-index:3}
.bl i{position:absolute;width:22px;height:22px;border:0 solid #fff6e2;filter:drop-shadow(0 0 3px rgba(255,240,210,.9))}
.bl i:nth-child(1){left:0;top:0;border-left-width:1.5px;border-top-width:1.5px}.bl i:nth-child(2){right:0;top:0;border-right-width:1.5px;border-top-width:1.5px}
.bl i:nth-child(3){left:0;bottom:0;border-left-width:1.5px;border-bottom-width:1.5px}.bl i:nth-child(4){right:0;bottom:0;border-right-width:1.5px;border-bottom-width:1.5px}
.patch{position:absolute;left:121px;top:243px;width:44px;height:30px;z-index:3;overflow:hidden;box-shadow:0 0 0 1px rgba(255,246,226,.5);background:rgba(255,240,210,.12)}
.patch i{position:absolute;left:-121px;top:-243px;width:286px;height:626px;background:var(--scene) center/cover;opacity:.45;mix-blend-mode:screen;transform:translateX(7px)}
/* 02 element */
.tile{position:absolute;width:96px;height:96px;border:1px solid #ededed;display:block;z-index:5}
.tile .n{position:absolute;left:6px;top:4px;font:500 8.5px var(--mono)}
.tile .m{position:absolute;right:6px;top:4px;font:500 7.5px var(--mono);color:var(--dim)}
.tile b{position:absolute;left:8px;top:20px;font:600 44px/1 var(--sans);letter-spacing:-.03em;color:var(--red)}
.tile .nm{position:absolute;left:8px;bottom:12px;font:500 9px var(--sans);letter-spacing:.04em}
.tb{position:absolute;left:0;right:0;bottom:0;display:flex}
.tb i{flex:1}
.tbl{display:grid;width:144px}
.tbl span{display:flex;justify-content:space-between;align-items:baseline;padding:4px 0;border-bottom:1px solid #2a2b2e;font:500 10px var(--mono)}
.tbl small{font-size:7px;letter-spacing:.12em;color:var(--dim)}
/* 03 engraved */
.scale{position:absolute;left:0;right:0;height:46px;background:linear-gradient(180deg,#0a0a0b,#151517 40%,#0a0a0b);border-top:1px solid #1e1f21;border-bottom:1px solid #1e1f21}
.nums{display:flex;justify-content:center;gap:14px;padding-top:5px;font:500 10px var(--sans);color:#bdbec2}
.nums .on{color:#fff}
.dof{position:relative;height:20px;margin-top:3px}
.dof i{position:absolute;top:3px;width:1.5px;height:12px}
.dof b{position:absolute;left:50%;top:0;width:1px;height:18px;background:#fff}
.spd{display:flex;gap:10px;font:500 10px var(--sans);color:#6d6f74}
.spd .on{color:#fff}.spd .red{color:var(--red)}
/* 04 striped */
.teal{position:absolute;inset:0;background:linear-gradient(180deg,#0d4b55,#0a2f36);mix-blend-mode:color;opacity:.55}
.sword{position:absolute;left:14px;top:330px;font:900 92px/1 var(--sans);font-stretch:62%;letter-spacing:-.02em;-webkit-background-clip:text;background-clip:text;color:transparent;z-index:4}
.line.l{color:#dcdcdc}
/* 05 segment */
.segnum{font:900 76px/1 var(--dot);color:#f2c12e;letter-spacing:.02em;text-shadow:0 0 12px rgba(242,193,46,.35)}
.segnum small{font-size:30px;color:#8d7420;vertical-align:28px}
.blocks{display:flex;gap:4px}
.blocks i{width:20px;height:8px;transform:skewX(-12deg)}
/* 06 test card */
.deckcard{position:absolute;left:0;right:0;top:404px;bottom:0;background:linear-gradient(#000 0 0) 0 0/0 0,repeating-linear-gradient(90deg,rgba(0,0,0,.75) 0 1px,transparent 1px 22px),repeating-linear-gradient(0deg,rgba(0,0,0,.75) 0 1px,transparent 1px 22px),#ea8f2a;overflow:hidden}
.circ{position:absolute;left:50%;top:50%;width:176px;height:176px;margin:-88px;border-radius:50%;border:1.5px solid #000}
.diag{position:absolute;inset:0;background:linear-gradient(to top right,transparent calc(50% - .75px),#000 calc(50% - .75px) calc(50% + .75px),transparent calc(50% + .75px)),linear-gradient(to bottom right,transparent calc(50% - .75px),#000 calc(50% - .75px) calc(50% + .75px),transparent calc(50% + .75px))}
.patches{display:flex;gap:0;border:1px solid #000}
.patches i{width:12px;height:12px}
.cardshut{position:absolute;left:111px;top:483px;width:64px;height:64px;border-radius:50%;background:#111;box-shadow:0 0 0 4px #ea8f2a,0 0 0 5.5px #000;z-index:5}
.card .roll{border-color:#000}
/* 07 white */
.white{background:linear-gradient(180deg,#ececea,#dcdcda);color:#151515}
.white .sb{color:#151515}
.white .island{background:#000}
.white .img{box-shadow:0 0 0 1px #151515,0 10px 24px rgba(0,0,0,.18)}
.rule{position:absolute;height:1.5px;background:var(--red);z-index:5}
.vbars{position:absolute;display:flex;flex-direction:column;gap:3px;z-index:5}
.vbars i{width:3px;height:30px}
/* 08 perforated */
.grille{position:absolute;left:0;right:0;top:406px;bottom:0;background:radial-gradient(circle,#03080a 1.4px,transparent 1.8px) 0 0/8px 8px,linear-gradient(180deg,#14262a,#0c1a1d)}
.lit{position:absolute;width:5px;height:5px;border-radius:50%;z-index:5}
.disc{position:absolute;left:111px;top:520px;width:64px;height:64px;border-radius:50%;background:#ededed;box-shadow:0 0 0 6px rgba(0,0,0,.6);z-index:5}
/* 09 wordmark */
.rword{position:absolute;left:-6px;top:380px;font:900 118px/.85 var(--sans);font-stretch:62%;letter-spacing:-.03em;color:var(--red);z-index:3;white-space:nowrap}
.wbar{position:absolute;left:14px;top:488px;display:flex;width:120px;height:2px;z-index:4}
.wbar i{flex:1}
/* 10 top view */
.plate{position:absolute;left:0;right:0;top:400px;height:142px;background:linear-gradient(180deg,#121214,#08080a);border-top:1px solid #2a2b2e;border-bottom:1px solid #2a2b2e}
.dialt{position:absolute;width:110px;height:110px;border-radius:50%;background:repeating-conic-gradient(#2a2b2e 0 3deg,#18191b 3deg 6deg);box-shadow:0 0 0 1px #3a3b3e;z-index:4}
.dialt::after{content:'';position:absolute;inset:8px;border-radius:50%;background:#0d0d0f}
.dialt span{position:absolute;left:50%;top:50%;font:500 7px var(--mono);color:#77797e;transform:translate(-50%,-50%) rotate(var(--a)) translateY(-40px);z-index:2}
.dialt span.on{color:#fff}.dialt span.red{color:var(--red)}
.cap{position:absolute;inset:34px;border-radius:50%;background:radial-gradient(circle at 45% 35%,#2e2f33,#0b0b0c);z-index:3}
.idx{position:absolute;width:1px;height:10px;background:var(--red);z-index:5}
.release{position:absolute;width:44px;height:44px;border-radius:50%;z-index:4}
.release i{position:absolute;border-radius:50%;border:1.5px solid}
.release b{position:absolute;inset:11px;border-radius:50%;background:radial-gradient(circle at 45% 35%,#f4f4f4,#9c9ea2)}
.cwin{position:absolute;width:30px;height:30px;border-radius:50%;background:#000;box-shadow:inset 0 1px 3px #000,0 0 0 1px #3a3b3e;display:grid;place-items:center;font:500 10px var(--mono);z-index:4}
"""

body = f"""<title>Film Camera UI · Quiet Machines</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=JetBrains+Mono:wght@500&family=Doto:wght@900&display=swap">
<style>{CSS}</style>
<div class="wrap">
  <header class="hero">
    <span class="eyebrow">Working title pending · Round 11 · Static mockups</span>
    <h1>Quiet machines, one loud gesture</h1>
    <i class="rule-h"></i>
    <p class="lede">Ten screens that pair extreme restraint (black and white, tiny engraved type, a lot of empty space) with one bold gesture each: a giant word, a test card, gold segments, a teal grade, a red symbol. Three are borderless. Every screen shows the loaded film's three colors.</p>
    <div class="pals">{pal}</div>
  </header>
  <div class="grid">
{cards}
  </div>
  <footer>Round 11. Earlier rounds are unchanged on their own pages.</footer>
</div>
<script>
(() => {{
const scene = document.createElement('canvas'); scene.width = 600; scene.height = 800;
{paint}
document.documentElement.style.setProperty('--scene', 'url(' + scene.toDataURL('image/jpeg', .85) + ')');
}})();
</script>
"""
(root / 'quiet.html').write_text(body)
head = '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
i = body.index('</style>') + len('</style>')
(root / 'quiet-standalone.html').write_text(head + body[:i] + '\n</head><body>\n' + body[i:] + '</body></html>\n')
print('ok', len(body))
