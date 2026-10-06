"""Builds devices.html (artifact source) and devices-standalone.html: six static gadget layouts.
Red only as hairlines or small text; each film shows its color signature."""
import pathlib, math
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / 'concepts.html').read_text()
paint = src[src.index('(function paint(g){'):src.index("})(scene.getContext('2d'));") + len("})(scene.getContext('2d'));")]

FILMS = [
 ('AURUM 200','AU',['#d9a441','#b8432f','#2e3b4e']), ('VERANO 400','VE',['#e58b6b','#f3d3a8','#4f7a6a']),
 ('LUMEN 100','LU',['#2f5fd0','#e8eef9','#d23b2a']), ('NOCTA 800T','NO',['#1e6f7a','#c9473a','#0e1b2c']),
 ('KINO 250D','KI',['#c0362c','#e7d9bf','#3d4a3a']), ('ARGENT 400','AR',['#e9e9e9','#8a8a8a','#1a1a1a']),
 ('GRAFIT 3200','GR',['#4a4a4a','#c8c8c8','#d02a1f']), ('PASTEL 160','PA',['#9fd3bd','#f2c6d3','#f4e9b8']),
 ('INSTA 600','IN',['#efe6d2','#6fb3c9','#e2735a']), ('MERIDIAN XP','XP',['#7b4fa0','#3fbf9b','#f0c43a']),
]
C = {n: c for n, _, c in FILMS}
FILT = {'AURUM 200':'sepia(.25) saturate(1.25) contrast(1.05) hue-rotate(-8deg) brightness(1.03)',
 'NOCTA 800T':'hue-rotate(-20deg) saturate(1.1) contrast(1.06) brightness(.96)',
 'KINO 250D':'saturate(.85) contrast(1.1) sepia(.08) hue-rotate(6deg)',
 'LUMEN 100':'saturate(1.6) contrast(1.22) hue-rotate(-4deg) brightness(.97)',
 'MERIDIAN XP':'saturate(1.5) hue-rotate(25deg) contrast(1.25) sepia(.1)',
 'VERANO 400':'sepia(.12) saturate(.9) contrast(.94) brightness(1.06)',
 'ARGENT 400':'grayscale(1) contrast(1.15)'}
SB = '<div class="island"></div><div class="sb"><span>9:41</span><i class="bat"></i></div>'
def bars(film, cls='bars'): return f'<span class="{cls}">' + ''.join(f'<i style="background:{c}"></i>' for c in C[film]) + '</span>'
def vf(film, x, y, w, h, extra=''): return f'<div class="vf" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><div class="scene" style="filter:{FILT[film]}"></div><i class="cross"></i>{extra}</div>'
def roll(x, y, w=40, h=52, label='12/36'): return f'<span class="roll" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><span>{label}</span></span>'
def shutter(cx, cy, d=72): return f'<span class="shutter" style="left:{cx-d/2}px;top:{cy-d/2}px;width:{d}px;height:{d}px"></span>'
def at(x, y, html, cls=''): return f'<div class="at {cls}" style="left:{x}px;top:{y}px">{html}</div>'
def phone(cls, inner): return f'<div class="phone"><div class="screen {cls}">{SB}{inner}</div></div>'
def ticks(n=19, w=120, red=10):
    out = ''
    for i in range(n):
        x = i * w / (n - 1)
        maj = i % 3 == 0
        out += f'<i style="left:{x:.1f}px;height:{7 if maj else 4}px"></i>'
    return f'<span class="tks" style="width:{w}px">{out}<b style="left:{red*w/(n-1):.1f}px"></b></span>'

D = []
# 01 Rail
D.append(('Rail', 'One hairline runs across the device under the frame like a ruler. Shutter speed, ISO and exposure are printed along it, and the meter needle is a red hairline that crosses it. Below sit the shutter, the camera roll and a column of small text keys.',
 phone('rail', at(21,44,'<span class="lbl">AURUM 200</span>' + bars('AURUM 200')) + at(232,44,'<span class="lbl dim">12/36</span>')
   + vf('AURUM 200',21,62,244,325)
   + '<div class="railline"></div>' + at(21,404,'<span class="v">1/250</span><small>S</small>') + at(216,404,'<small>ISO</small><span class="v">200</span>')
   + at(83,421, ticks(19,120,10)) + at(130,438,'<span class="redt">+0.3 EV</span>')
   + at(98,462,'<span class="lens"><span>26</span><span class="on">35</span><span>50</span></span>')
   + roll(30,516) + shutter(143,542)
   + at(208,508,'<div class="keys"><span>FILM ▸</span><span>FLASH · A</span><span>FLIP</span></div>'))))

# 02 Cartridge
D.append(('Cartridge', 'The film is a cartridge in a slot above the frame. Its label carries the name, the speed and the color band, and the FILM key beside the slot ejects it and loads the next one. Settings sit in a two-column block, and the shutter is on the right under your thumb.',
 phone('cart', at(16,46,f'''<div class="slot"><div class="label"><span class="band">{''.join(f'<i style="background:{c}"></i>' for c in C['NOCTA 800T'])}</span><b>NOCTA 800T</b><small>36 EXP · TUNGSTEN</small></div></div>''')
   + at(232,52,'<span class="eject">FILM<br>▸</span>')
   + vf('NOCTA 800T',21,96,244,318)
   + at(21,428,'<div class="spec"><span><small>S</small>1/250</span><span><small>ƒ</small>1.8</span><span><small>ISO</small>800</span><span><small>EV</small>+0.0</span></div>')
   + at(164,432,'<div class="minimeter"><i></i><b></b></div><small class="mm">METER</small>')
   + at(98,476,'<span class="lens"><span>26</span><span class="on">35</span><span>50</span></span>')
   + roll(26,528) + at(86,532,'<div class="pair"><span>FLASH<br>A</span><span>FLIP</span></div>') + shutter(226,556))))

# 03 Side bar
D.append(('Side Bar', 'The frame sits to the left and an instrument column runs down its right side: the film\'s color band, then shutter, ISO, EV and lens stacked like gauges, with a vertical meter whose needle is a red line. The area below the frame is nearly empty.',
 phone('side', at(14,44,'<span class="lbl">LUMEN 100</span>') + at(198,44,'<span class="lbl dim">12/36</span>')
   + vf('LUMEN 100',14,62,222,296)
   + at(246,62,f'''<div class="col">{bars('LUMEN 100','vband')}<span><small>S</small>1/250</span><span><small>ISO</small>100</span><span><small>EV</small>+0.0</span><span><small>MM</small>35</span>
       <span class="vmeter"><i></i><b></b></span></div>''')
   + at(14,374,'<span class="hint">AE ·  CENTRE  ·  3:4</span>')
   + at(98,404,'<span class="lens"><span>26</span><span class="on">35</span><span>50</span></span>')
   + roll(30,500,44,58) + shutter(143,529,76)
   + at(212,494,'<div class="keys"><span>FILM ▸</span><span>FLASH · A</span><span>FLIP</span></div>'))))

# 04 Ticker
D.append(('Ticker', 'A single dot-matrix strip under the frame scrolls the settings like the display on an old pager. A row of dots beneath it is the meter, with zero marked by a short red underline. The rest is one key for film and the shutter.',
 phone('tick', at(16,44,'<span class="lbl">KINO 250D</span>' + bars('KINO 250D')) + at(232,44,'<span class="lbl dim">12/36</span>')
   + vf('KINO 250D',16,62,254,339)
   + at(16,412,'<div class="ticker"><span>1/250 · ISO 200 · EV +0.3 · ƒ1.8 · 35MM · FLASH A</span></div>')
   + at(16,446,'<div class="dots">' + ''.join(f'<i class="{"on" if i==12 else ""}"></i>' for i in range(21)) + '<b></b></div>')
   + at(98,466,'<span class="lens dm"><span>26</span><span class="on">35</span><span>50</span></span>')
   + shutter(56,548) + at(108,532,'<span class="pill">FILM ▸</span><span class="mini">FLASH A · FLIP</span>') + roll(224,520,46,58))))

# 05 Panels
D.append(('Panels', 'A light grey device divided into engraved modules, each with a tiny red number: 01 optics, 02 exposure, 03 film, 04 release. The structure is the decoration, the way it is on lab equipment and old synthesizers.',
 phone('pan', '<div class="seam" style="top:418px"></div><div class="seam" style="top:476px"></div><div class="seam" style="top:520px"></div>'
   + at(16,44,'<span class="mod">01</span><span class="lbl">OPTICS</span>') + at(206,44,'<span class="lbl">ƒ1.8 · 3:4</span>')
   + f'<div class="well" style="left:12px;top:60px;width:262px;height:350px"></div>' + vf('ARGENT 400',18,66,250,338)
   + at(16,426,'<span class="mod">02</span><span class="lbl">EXPOSURE</span>')
   + at(16,446,'<div class="spec row"><span><small>S</small>1/250</span><span><small>ISO</small>400</span><span><small>EV</small>+0.0</span></div>') + at(190,446, ticks(13,80,7))
   + at(16,484,'<span class="mod">03</span><span class="lbl">FILM</span>') + at(80,484,'<b class="film">ARGENT 400</b>' + bars('ARGENT 400')) + at(222,480,'<span class="key">NEXT ▸</span>')
   + at(16,528,'<span class="mod">04</span><span class="lbl">RELEASE</span>')
   + roll(20,548,40,52) + at(78,560,'<div class="pair"><span>FLASH<br>A</span><span>FLIP</span></div>')
   + at(160,546,'<span class="lens v"><span>26</span><span class="on">35</span><span>50</span></span>') + shutter(236,574,62))))

# 06 Index ring
ring = ''
for i, (n, code, cols) in enumerate(FILMS):
    a = (i - 1) * 36
    on = ' on' if code == 'VE' else ''
    ring += f'<span class="code{on}" style="--a:{a}deg">{code}</span>'
arc = ''.join(f'<i style="--a:{-14 + j*10}deg;background:{c}"></i>' for j, c in enumerate(C['VERANO 400']))
D.append(('Index Ring', 'Film is chosen on a printed ring around the shutter, like the index ring on an old lens. The ten stock codes sit around it, and the current one is at the top with its colors as a short arc. Turn the ring to change film, and press the middle to shoot.',
 phone('ring', at(16,44,'<span class="lbl">VERANO 400</span>') + at(232,44,'<span class="lbl dim">12/36</span>')
   + vf('VERANO 400',16,62,254,312)
   + at(16,384,'<span class="v sm">1/250</span><small> S</small>') + at(83,388, ticks(19,120,11)) + at(220,384,'<small>ISO </small><span class="v sm">400</span>')
   + at(110,408,'<span class="lens"><span>26</span><span class="on">35</span><span>50</span></span>')
   + f'<div class="dial" style="left:53px;top:438px"><span class="ringline"></span><span class="arc">{arc}</span>{ring}</div>'
   + shutter(143,528,68) + roll(18,560,36,46) + at(200,560,'<div class="keys sm"><span>FLASH · A</span><span>FLIP</span></div>'))))

cards = '\n'.join(f'''<figure class="card"><div class="ph">{html}</div><figcaption><span class="no">{i:02d}</span><h3>{n}</h3><p>{d}</p></figcaption></figure>'''
                  for i, (n, d, html) in enumerate(D, 1))
palette = '\n'.join(f'''<div class="pf"><span class="sw">{''.join(f'<i style="background:{c}"></i>' for c in cols)}</span><b>{name}</b><small>{code}</small></div>''' for name, code, cols in FILMS)

CSS = r"""
/* Layout: dark gallery of six static devices. Each phone is absolutely laid out so every layout can differ; shared parts are the film line, black-margined frame, hairline meter, lens row, shutter, keys and roll. Single dark look by design. */
:root{--bg:#070708;--ink:#e9eaec;--dim:#7a7c82;--line:#1f2023;--red:#e2231a;
  --sans:'Archivo',system-ui,-apple-system,'Segoe UI',sans-serif;--mono:'JetBrains Mono',ui-monospace,Menlo,monospace;--dot:'Doto','JetBrains Mono',monospace;
  --noise:url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 .5 0 0 0 0 .5 0 0 0 0 .5 0 0 0 .5 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  color-scheme:dark}
*{box-sizing:border-box}
html,body{background:var(--bg);color:var(--ink)}
body{font-family:var(--sans);font-size:15px;line-height:1.55;padding-inline:clamp(16px,4vw,56px);padding-block:0 80px}
.wrap{max-width:1180px;margin:0 auto}
.hero{padding-block:72px 32px;display:grid;gap:16px;border-bottom:1px solid var(--line)}
.eyebrow{font:500 11px var(--mono);letter-spacing:.16em;text-transform:uppercase;color:var(--dim)}
h1{margin:0;font-weight:600;font-size:clamp(30px,5vw,54px);line-height:1.02;letter-spacing:-.03em;text-wrap:balance}
h1 span{display:inline-block;width:.9em;height:2px;background:var(--red);vertical-align:.25em;margin-left:.2em}
.lede{margin:0;color:#a8aab0;max-width:66ch}
.palette{padding-block:32px;border-bottom:1px solid var(--line);margin-bottom:56px;display:grid;gap:14px}
.palette h2{margin:0;font:500 11px var(--mono);letter-spacing:.16em;text-transform:uppercase;color:var(--dim)}
.pl{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:12px 20px}
.pf{display:flex;align-items:center;gap:10px;font:500 11px var(--mono);letter-spacing:.06em}
.pf small{color:var(--dim)}
.sw{display:flex;width:42px;height:12px;border-radius:2px;overflow:hidden;box-shadow:0 0 0 1px #2a2b2e;flex:none}
.sw i{flex:1}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:72px 32px}
.card{margin:0;display:grid;gap:18px;justify-items:center;align-content:start}
.card figcaption{max-width:300px;display:grid;gap:5px}
.no{font:500 11px var(--mono);color:var(--red)}
.card h3{margin:0;font-weight:600;font-size:19px;letter-spacing:-.01em}
.card p{margin:0;font-size:14px;color:#a8aab0}
footer{margin-top:72px;padding-top:18px;border-top:1px solid var(--line);color:var(--dim);font-size:13.5px;max-width:70ch}

/* ---- phone ---- */
.phone{width:300px;height:640px;border-radius:50px;padding:7px;background:linear-gradient(140deg,#3a3b3f,#151618 40%,#2a2b2e 70%,#111);box-shadow:0 0 0 1px #000,0 30px 55px -20px rgba(0,0,0,.85)}
.screen{position:relative;width:286px;height:626px;border-radius:43px;overflow:hidden;background:#000;color:#e9eaec;font-family:var(--mono);
  --ink:#dcdde0;--dim:#64666c}
.island{position:absolute;top:10px;left:50%;width:84px;height:24px;border-radius:14px;background:#000;transform:translateX(-50%);z-index:9}
.sb{position:absolute;left:0;right:0;top:0;height:42px;display:flex;align-items:center;justify-content:space-between;padding:6px 26px 0;font:600 12px system-ui,sans-serif}
.bat{display:inline-block;width:22px;height:10px;border:1px solid currentColor;border-radius:3px;position:relative}
.bat::before{content:'';position:absolute;inset:1.5px 6px 1.5px 1.5px;background:currentColor;border-radius:1px}
.at{position:absolute;display:flex;align-items:center;gap:6px;white-space:nowrap}
.lbl{font:500 9.5px var(--mono);letter-spacing:.08em;color:var(--ink)}
.lbl.dim{color:var(--dim)}
.bars{display:inline-flex;gap:1.5px}
.bars i{width:9px;height:3px}
.vf{position:absolute;overflow:hidden;background:#111}
.scene{position:absolute;inset:0;background:var(--scene) center/cover}
.cross{position:absolute;left:50%;top:50%;width:16px;height:16px;transform:translate(-50%,-50%)}
.cross::before,.cross::after{content:'';position:absolute;background:rgba(255,255,255,.8)}
.cross::before{left:50%;top:0;bottom:0;width:1px}.cross::after{top:50%;left:0;right:0;height:1px}
.v{font:500 11px var(--mono);color:var(--ink)}
.v.sm{font-size:10px}
.at small,small{font:500 7.5px var(--mono);color:var(--dim);letter-spacing:.1em}
.redt{font:500 8px var(--mono);color:var(--red);letter-spacing:.08em;transform:translateX(-50%)}
.tks{position:relative;display:block;height:9px}
.tks i{position:absolute;top:0;width:1px;background:#77797f}
.tks b{position:absolute;top:-6px;width:1px;height:17px;background:var(--red)}
.lens{display:flex;gap:4px}
.lens span{font:400 11px var(--mono);color:var(--dim);padding:4px 9px;border-bottom:1px solid transparent}
.lens span.on{color:var(--ink);border-bottom-color:var(--ink)}
.shutter{position:absolute;border-radius:50%;box-shadow:inset 0 0 0 1.5px var(--ink)}
.shutter::after{content:'';position:absolute;inset:6px;border-radius:50%;background:var(--ink)}
.roll{position:absolute;border-radius:3px;overflow:hidden;border:1px solid #55575c;background:var(--scene) center/cover}
.roll>span{position:absolute;left:0;right:0;bottom:0;font:500 7px var(--mono);text-align:center;padding:6px 0 2px;background:linear-gradient(transparent,rgba(0,0,0,.85));color:#e9eaec}
.keys{display:grid;gap:6px}
.keys span{font:500 8.5px var(--mono);letter-spacing:.08em;color:var(--ink);padding:6px 9px;border:1px solid #34363a;border-radius:3px;text-align:center}
.keys.sm span{padding:4px 7px;font-size:8px}
.pair{display:flex;gap:6px}
.pair span{font:500 8px/1.3 var(--mono);letter-spacing:.08em;color:var(--ink);width:40px;height:40px;border-radius:50%;border:1px solid #3a3c40;display:grid;place-items:center;text-align:center}

/* 01 Rail */
.railline{position:absolute;left:21px;right:21px;top:424px;height:1px;background:#3a3b3e}
.rail .at small{order:2}
/* 02 Cartridge */
.cart{background:radial-gradient(ellipse at 50% 0%,#1d1e21,#0b0b0c 70%)}
.slot{width:206px;height:42px;border-radius:6px;padding:5px;background:#050506;box-shadow:inset 0 2px 4px #000,0 1px 0 rgba(255,255,255,.08)}
.label{height:100%;display:grid;grid-template-columns:auto 1fr;grid-template-rows:auto auto;column-gap:8px;align-items:center;padding:0 8px 0 0;border-radius:3px;background:linear-gradient(180deg,#26272a,#1b1c1e);box-shadow:inset 0 1px 0 rgba(255,255,255,.08)}
.band{grid-row:1/3;display:flex;flex-direction:column;width:6px;height:100%;border-radius:3px 0 0 3px;overflow:hidden}
.band i{flex:1}
.label b{font:600 10px var(--mono);letter-spacing:.08em}
.label small{font-size:6.5px}
.eject{display:grid;place-items:center;width:36px;height:36px;border:1px solid #3a3c40;border-radius:6px;font:500 7.5px/1.3 var(--mono);letter-spacing:.1em;text-align:center}
.spec{display:grid;grid-template-columns:repeat(2,auto);gap:4px 18px;font:500 10.5px var(--mono)}
.spec span{display:flex;gap:5px;align-items:baseline}
.spec.row{display:flex;gap:14px}
.minimeter{position:relative;width:96px;height:1px;background:#3a3b3e}
.minimeter i{position:absolute;left:0;right:0;top:-3px;height:7px;background:repeating-linear-gradient(90deg,#55575c 0 1px,transparent 1px 16%)}
.minimeter b{position:absolute;left:52%;top:-7px;width:1px;height:15px;background:var(--red)}
.mm{position:absolute;left:0;top:10px}
/* 03 Side bar */
.col{display:flex;flex-direction:column;align-items:flex-start;gap:10px;height:296px}
.col span{display:grid;gap:1px;font:500 10px var(--mono)}
.vband{display:flex!important;flex-direction:column;gap:0!important;width:26px}
.vband i{height:4px}
.vmeter{position:relative;margin-top:auto;width:12px;height:84px;border-left:1px solid #3a3b3e;background:repeating-linear-gradient(180deg,#55575c 0 1px,transparent 1px 14px) left/6px 100% no-repeat}
.vmeter b{position:absolute;left:-1px;top:46%;width:14px;height:1px;background:var(--red)}
.hint{font:500 7.5px var(--mono);letter-spacing:.14em;color:var(--dim)}
/* 04 Ticker */
.ticker{width:254px;height:24px;overflow:hidden;display:flex;align-items:center;padding-left:6px;background:#0a0a0b;border:1px solid #1d1e20;border-radius:3px;-webkit-mask:linear-gradient(90deg,#000 80%,transparent);mask:linear-gradient(90deg,#000 80%,transparent)}
.ticker span{font:800 12px var(--dot);color:#f2f2f2;letter-spacing:.06em;text-shadow:0 0 4px rgba(255,255,255,.4)}
.dots{position:relative;display:flex;gap:7px;width:254px;justify-content:center}
.dots i{width:3px;height:3px;border-radius:50%;background:#2c2d30}
.dots i.on{background:#fff;box-shadow:0 0 4px #fff}
.dots b{position:absolute;left:calc(50% - 5px);top:7px;width:10px;height:1px;background:var(--red)}
.lens.dm span{font:800 13px var(--dot)}
.pill{font:500 9px var(--mono);letter-spacing:.1em;padding:8px 14px;border:1px solid #3a3c40;border-radius:16px}
.tick .at:has(.pill){flex-direction:column;align-items:flex-start;gap:8px}
.mini{font:500 7.5px var(--mono);letter-spacing:.12em;color:var(--dim);padding-left:4px}
/* 05 Panels */
.pan{background:var(--noise),linear-gradient(180deg,#d5d6d6,#c3c4c5);background-size:120px,100%;color:#1f2022;--ink:#1f2022;--dim:#66686c}
.pan .sb{color:#1f2022}
.seam{position:absolute;left:0;right:0;height:2px;background:linear-gradient(180deg,rgba(0,0,0,.28) 0 1px,rgba(255,255,255,.7) 1px 2px)}
.mod{font:600 8px var(--mono);color:var(--red);letter-spacing:.1em}
.pan .lbl{color:#3a3b3e}
.well{position:absolute;border-radius:8px;background:#0b0b0c;box-shadow:inset 0 2px 4px #000,0 1px 0 rgba(255,255,255,.7)}
.pan .vf{border-radius:3px}
.pan .tks i{background:#55575c}
.film{font:600 10.5px var(--mono);letter-spacing:.08em}
.key{font:500 8px var(--mono);letter-spacing:.1em;padding:7px 10px;border-radius:4px;background:linear-gradient(180deg,#e2e3e3,#c9caca);box-shadow:0 1px 0 #fff inset,0 2px 0 #8e9093}
.pan .pair span{border-color:#8e9093;background:linear-gradient(180deg,#e2e3e3,#c9caca);box-shadow:0 2px 0 #8e9093}
.pan .roll{border:2px solid #1f2022}
.lens.v{flex-direction:column;gap:0}
.lens.v span{padding:2px 6px;border-bottom:0;border-left:1px solid transparent}
.lens.v span.on{border-left-color:var(--ink)}
.pan .shutter{box-shadow:0 0 0 3px #b4b5b6,0 3px 0 #8e9093;background:radial-gradient(circle at 45% 35%,#3a3b3e,#141516 70%)}
.pan .shutter::after{display:none}
/* 06 Index ring */
.dial{position:absolute;width:180px;height:180px}
.ringline{position:absolute;inset:22px;border-radius:50%;border:1px solid #2c2d30;background:repeating-conic-gradient(#4a4c50 0 .6deg,transparent .6deg 6deg);-webkit-mask:radial-gradient(circle,transparent 62px,#000 62.5px 67px,transparent 67.5px);mask:radial-gradient(circle,transparent 62px,#000 62.5px 67px,transparent 67.5px)}
.code{position:absolute;left:50%;top:50%;font:500 8px var(--mono);color:#55575c;letter-spacing:.08em;transform:translate(-50%,-50%) rotate(var(--a)) translateY(-82px) rotate(calc(var(--a) * -1))}
.code.on{color:#fff}
.arc{position:absolute;left:50%;top:50%}
.arc i{position:absolute;left:-1px;top:-71px;width:3px;height:8px;transform-origin:50% 71px;transform:rotate(var(--a))}
.ring .tks{top:4px}
.ring .shutter{z-index:2}
.ring .dial::after{content:'';position:absolute;left:50%;top:6px;width:1px;height:10px;background:var(--red)}
"""

body = f"""<title>Film Camera UI · Devices</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&family=Doto:wght@700;800&display=swap">
<style>{CSS}</style>
<div class="wrap">
  <header class="hero">
    <span class="eyebrow">Working title pending · Round 9 · Static mockups</span>
    <h1>Six devices<span></span></h1>
    <p class="lede">New layouts, not tied to E. Each one is a simple object with small details. Red appears only as a hairline or a few letters: the meter needle, a module number, a reading. Every film shows its color signature, and a FILM key cycles stocks while the name stays above the frame.</p>
  </header>
  <section class="palette" aria-labelledby="pal-h">
    <h2 id="pal-h">Film color signatures</h2>
    <div class="pl">{palette}</div>
  </section>
  <div class="grid">
{cards}
  </div>
  <footer>Round 9. Earlier rounds are unchanged on their own pages.</footer>
</div>
<script>
(() => {{
const scene = document.createElement('canvas'); scene.width = 600; scene.height = 800;
{paint}
document.documentElement.style.setProperty('--scene', 'url(' + scene.toDataURL('image/jpeg', .85) + ')');
}})();
</script>
"""
(root / 'devices.html').write_text(body)
head = '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
i = body.index('</style>') + len('</style>')
(root / 'devices-standalone.html').write_text(head + body[:i] + '\n</head><body>\n' + body[i:] + '</body></html>\n')
print('ok', len(body))
