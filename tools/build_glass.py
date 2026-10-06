"""Builds glass.html (artifact source) and glass-standalone.html: six simple screens on a golden-ratio layout,
four of them pairing liquid glass with analog instruments."""
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / 'concepts.html').read_text()
paint = src[src.index('(function paint(g){'):src.index("})(scene.getContext('2d'));") + len("})(scene.getContext('2d'));")]

BOLT = '<svg viewBox="0 0 24 24"><path d="M13 3 6 13.5h5L10 21l7-10.5h-5z"/></svg>'
FLIP = '<svg viewBox="0 0 24 24"><path d="M5 9a7 7 0 0 1 12.5-2.5M19 15a7 7 0 0 1-12.5 2.5"/><path d="M17.5 3v3.5H14M6.5 21v-3.5H10"/></svg>'
SB = '<div class="island"></div><div class="sb"><span>9:41</span><i class="bat"></i></div>'
PHI = '<div class="phi"><i class="h1"></i><i class="h2"></i><i class="v1"></i><i class="v2"></i></div>'
def phone(cls, inner): return f'<div class="phone"><div class="screen {cls}">{SB}{inner}{PHI}</div></div>'
def vf(extra='', cls=''): return f'<div class="vf {cls}"><div class="scene"></div>{extra}</div>'
TOP = '<div class="top"><span>A</span><span>AURUM 200</span><span>12/36</span></div>'
LENS = '<div class="lens"><span>26</span><span class="on">35</span><span>50</span></div>'
def deck(center='<span class="shutter"></span>'):
    return f'<div class="deck"><span class="roll"></span>{center}<span class="ico flash">{BOLT}</span></div>'

ticks = ''.join(f'<i style="--a:{(v/3)*38}deg" class="{"maj" if v%3==0 else ""}"></i>' for v in range(-9, 10))

G = []
G.append(('Level', 'The exposure meter is a spirit level. A glass bubble floats in a liquid vial, and its position is the exposure: centered between the two marks means correct. Tilt the phone and the same bubble shows the horizon, so one vial does two jobs.',
  'Glass + analog: the bubble is liquid glass, refracting the dark vial behind it.',
  phone('lv', TOP + vf('<i class="cross"></i>') + '''
  <div class="row r1"><span class="ro">1/250</span><div class="vial"><i class="mark l"></i><i class="mark r"></i><span class="m">−</span><span class="p">+</span><i class="bubble glass"></i></div><span class="ro">ISO 200</span></div>
  ''' + LENS + deck())))

G.append(('Drop', 'A single drop of liquid glass sits on the bottom edge of the frame and magnifies it. The analog meter is etched inside the drop. It stays clear when the exposure is right and only shows the needle when you touch it or drift more than a third of a stop.',
  'The answer to "can glass hide the meter": the needle lives inside the drop and fades in only when needed.',
  phone('dr', TOP + vf('<i class="cross"></i>') + f'''
  <div class="drop glass"><div class="mag"></div><div class="arc">{ticks}<b class="ndl"></b></div></div>
  <div class="row r1 wide"><span class="ro">1/250</span><span class="ro">ISO 200</span></div>
  ''' + LENS + deck())))

def scale(vals, on):
    return ''.join(f'<span class="{"on" if i==on else ""}">{v}</span>' for i, v in enumerate(vals))
G.append(('Cyclops', 'Settings are etched on thin glass rulers, and a small glass bubble magnifies the current value, like the date window on a watch. Slide a ruler under its bubble to change it. On the EV ruler the bubble moves instead, so the bubble is the needle.',
  'Three rulers, one idea: small type everywhere, and the glass makes the one number that matters big.',
  phone('cy', TOP + vf('<i class="cross"></i>') + f'''
  <div class="rulers">
    <div class="ruler"><small>S</small><div class="track">{scale(['1/30','1/60','1/125','1/250','1/500','1/1000','1/2000'],3)}<i class="cyc glass" style="--x:50%"><b>1/250</b></i></div></div>
    <div class="ruler"><small>ISO</small><div class="track">{scale(['50','100','200','400','800','1600','3200'],2)}<i class="cyc glass" style="--x:50%"><b>200</b></i></div></div>
    <div class="ruler"><small>EV</small><div class="track ev">{scale(['−3','−2','−1','0','+1','+2','+3'],3)}<i class="cyc glass" style="--x:58%"><b>+0.3</b></i></div></div>
  </div>''' + deck())))

G.append(('Frosted Window', 'The controls are a frosted glass slab resting over the bottom edge of the frame. A classic needle meter sits behind the glass, softened into a glow, and a clear slit is cut through the frost where the needle crosses.',
  'The meter is hidden in plain sight: you only see the part of it that matters.',
  phone('fw', TOP + vf() + f'''
  <div class="dial"><div class="arc">{ticks}<b class="ndl"></b></div></div>
  <div class="slab"></div><div class="slit"></div>
  <div class="fw-read"><span>1/250</span><span>ƒ1.8</span><span>ISO 200</span></div>
  ''' + LENS + deck())))

G.append(('Construction', 'This takes the blueprint idea and keeps only the part that works: the drawing is the composition guide. The frame is a golden rectangle, the guide is a golden spiral instead of thirds, and the settings sit in a small specification table.',
  'From Cyanotype, but practical: no callouts on the image, just exact lines and a datasheet.',
  phone('cn', '<div class="top"><span>FIG. 12</span><span>1 : φ</span><span>AURUM 200</span></div>' + vf('''<svg class="spiral" viewBox="0 0 1000 1618" preserveAspectRatio="none">
      <path d="M0 1000H1000M382 1000V1618M0 1236H382M236 1000V1236M236 1146H382M292 1146V1236" />
      <path class="sp" d="M0 0A1000 1000 0 0 1 1000 1000A618 618 0 0 1 382 1618A382 382 0 0 1 0 1236A236 236 0 0 1 236 1000A146 146 0 0 1 382 1146A90 90 0 0 1 292 1236"/></svg>''', 'gold') + '''
  <div class="dimv"><span>φ</span></div>
  <table class="spec"><tr><td>SHUTTER</td><td>1/250</td><td>ISO</td><td>200</td></tr><tr><td>EV</td><td>+0.0</td><td>LENS</td><td>35 MM</td></tr>
    <tr><td colspan="4"><div class="hair"><i></i><b></b></div></td></tr></table>
  ''' + deck('<span class="shutter cn-sh"><i></i></span>'))))

G.append(('Command Line', 'The terminal, refined. Settings are the arguments of one command, and you tap an argument to change it. The meter is one line of characters. The shutter is a Return key: you run the command to take the picture.',
  'The cleverest-looking of the six with the least design, and very cheap to build.',
  phone('cl', '<div class="top"><span>~/roll-01</span><span>aurum200</span><span>12/36</span></div>' + vf('<i class="cross"></i>') + '''
  <pre class="cmd"><span class="pr">$</span> expose <i>-s</i> <b>1/250</b> <i>-iso</i> <b>200</b>
         <i>-ev</i> <b>+0.0</b> <i>-mm</i> <b>35</b> <i>-f</i> <b>auto</b><span class="cur"></span>
  <span class="dim">meter</span>  [·· ··· ·<b>|</b>· ··· ··]</pre>
  <div class="deck"><span class="roll"></span><span class="ret"><b>⏎</b><small>return</small></span><span class="ico flash">''' + FLIP + '</span></div>')))

cards = '\n'.join(f'''<figure class="card"><div class="ph">{html}</div><figcaption><span class="no">{i:02d}</span><h3>{n}</h3><p>{d}</p><p class="key">{k}</p></figcaption></figure>'''
                  for i, (n, d, k, html) in enumerate(G, 1))

CSS = r"""
/* Layout: φ everywhere. Inner screen 286×626 splits at 387 (626/φ); frame 218×327 (2:3) with 34px sides; spacing 5·8·13·21·34·55·89. Single dark look by design. */
:root{--bg:#09090a;--ink:#ececee;--dim:#76787e;--line:#232427;
  --f-sans:'Geist','Helvetica Neue',system-ui,sans-serif;--f-mono:'Geist Mono',ui-monospace,Menlo,monospace;
  color-scheme:dark}
*{box-sizing:border-box}
html,body{background:var(--bg);color:var(--ink)}
body{font-family:var(--f-sans);font-size:15px;line-height:1.55;padding-inline:clamp(16px,4vw,55px);padding-block:0 89px}
.wrap{max-width:1180px;margin:0 auto}
.hero{display:grid;grid-template-columns:minmax(0,1.618fr) minmax(0,1fr);gap:21px 55px;align-items:end;padding-block:89px 34px;border-bottom:1px solid var(--line);margin-bottom:55px}
.eyebrow{grid-column:1/-1;font:500 11px var(--f-mono);letter-spacing:.16em;text-transform:uppercase;color:var(--dim)}
h1{margin:0;font-weight:500;font-size:clamp(34px,5.5vw,55px);line-height:1;letter-spacing:-.035em;text-wrap:balance}
.lede{margin:0;color:#a9abb1;max-width:52ch}
.tog{grid-column:1/-1;justify-self:start;display:inline-flex;align-items:center;gap:8px;background:none;border:1px solid #34363a;color:var(--ink);border-radius:999px;padding:8px 13px;font:500 12px var(--f-mono);cursor:pointer}
.tog:focus-visible{outline:2px solid #fff;outline-offset:2px}
.tog i{width:8px;height:8px;border-radius:50%;border:1px solid currentColor}
.show-phi .tog i{background:#e7c26a;border-color:#e7c26a}
@media (max-width:760px){.hero{grid-template-columns:1fr}}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:89px 34px}
.card{margin:0;display:grid;gap:21px;justify-items:center;align-content:start}
.card figcaption{max-width:300px;display:grid;gap:5px}
.no{font:500 11px var(--f-mono);color:var(--dim)}
.card h3{margin:0;font-weight:500;font-size:21px;letter-spacing:-.02em}
.card p{margin:0;font-size:14px;color:#a9abb1}
.card p.key{margin-top:8px;padding-top:8px;border-top:1px solid var(--line);color:#dcdde0;font-size:13.5px}
footer{margin-top:89px;padding-top:21px;border-top:1px solid var(--line);color:var(--dim);font-size:13.5px;max-width:68ch}

/* ---- phone, everything absolutely placed on the φ grid ---- */
.phone{width:300px;height:640px;border-radius:50px;padding:7px;background:linear-gradient(140deg,#3a3b3f,#151618 40%,#2a2b2e 70%,#111);box-shadow:0 0 0 1px #000,0 34px 55px -21px rgba(0,0,0,.8)}
.screen{position:relative;width:286px;height:626px;border-radius:43px;overflow:hidden;background:#000;color:#ececee;font-family:var(--f-mono)}
.island{position:absolute;top:10px;left:50%;width:84px;height:24px;border-radius:14px;background:#000;transform:translateX(-50%);z-index:9}
.sb{position:absolute;left:0;right:0;top:0;height:42px;display:flex;align-items:center;justify-content:space-between;padding:6px 26px 0;font:600 12px var(--f-sans)}
.bat{display:inline-block;width:22px;height:10px;border:1px solid currentColor;border-radius:3px;position:relative}
.bat::before{content:'';position:absolute;inset:1.5px 6px 1.5px 1.5px;background:currentColor;border-radius:1px}
.top{position:absolute;left:34px;right:34px;top:40px;height:13px;display:flex;justify-content:space-between;align-items:center;font-size:8.5px;letter-spacing:.08em;color:#9a9ca2}
.vf{position:absolute;left:34px;top:55px;width:218px;height:327px;overflow:hidden;background:#111}
.vf.gold{left:42px;width:202px}
.scene{position:absolute;inset:0;background:var(--scene) center/cover;filter:sepia(.2) saturate(1.1) contrast(1.05) hue-rotate(-6deg)}
.cross{position:absolute;left:50%;top:50%;width:13px;height:13px;transform:translate(-50%,-50%)}
.cross::before,.cross::after{content:'';position:absolute;background:rgba(255,255,255,.85)}
.cross::before{left:50%;top:0;bottom:0;width:1px}.cross::after{top:50%;left:0;right:0;height:1px}
.row{position:absolute;left:34px;right:34px;display:flex;align-items:center;justify-content:space-between}
.r1{top:400px;height:21px}
.ro{font-size:9.5px;color:#cfd0d4}
.lens{position:absolute;left:0;right:0;top:443px;display:flex;justify-content:center;gap:13px;font-size:11px}
.lens span{color:#5f6167;padding:0 2px 3px;border-bottom:1px solid transparent}
.lens span.on{color:#fff;border-bottom-color:#fff}
.deck{position:absolute;left:34px;right:34px;top:494px;height:89px;display:flex;align-items:center;justify-content:space-between}
.shutter{width:68px;height:68px;border-radius:50%;box-shadow:inset 0 0 0 1.5px #ececee;position:relative}
.shutter::after{content:'';position:absolute;inset:6.5px;border-radius:50%;background:#ececee}
.roll{width:34px;height:34px;border-radius:8px;background:var(--scene) center/cover;box-shadow:0 0 0 1px #4a4c50}
.ico{display:grid;place-items:center;width:34px;height:34px;color:#cfd0d4}
.ico svg{width:17px;height:17px;stroke:currentColor;fill:none;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}

/* liquid glass */
.glass{background:rgba(255,255,255,.05);-webkit-backdrop-filter:blur(1.5px) saturate(1.8) brightness(1.12);backdrop-filter:blur(1.5px) saturate(1.8) brightness(1.12);
  box-shadow:inset 0 1px 1px rgba(255,255,255,.75),inset 0 -1px 1px rgba(255,255,255,.3),inset 3px 0 8px rgba(255,255,255,.14),inset -3px 0 8px rgba(255,255,255,.1),inset 0 -6px 10px rgba(255,255,255,.06),0 5px 13px rgba(0,0,0,.45)}
.glass::before{content:'';position:absolute;left:12%;right:30%;top:7%;height:28%;border-radius:50%;background:linear-gradient(180deg,rgba(255,255,255,.55),rgba(255,255,255,0));filter:blur(.5px);pointer-events:none}

/* φ overlay */
.phi{position:absolute;inset:0;pointer-events:none;opacity:0;transition:opacity .3s;z-index:20}
.show-phi .phi{opacity:1}
.phi i{position:absolute;background:rgba(231,194,106,.75)}
.phi .h1{left:0;right:0;top:387px;height:1px}
.phi .h2{left:0;right:0;top:239px;height:1px;opacity:.45}
.phi .v1{top:0;bottom:0;left:109px;width:1px;opacity:.45}
.phi .v2{top:0;bottom:0;left:177px;width:1px;opacity:.45}

/* ===== 01 Level ===== */
.vial{position:relative;width:144px;height:21px;border-radius:11px;background:linear-gradient(180deg,#1b1a12,#0b0a06);box-shadow:inset 0 0 0 1px #3a3830,inset 0 3px 5px rgba(0,0,0,.8)}
.vial::after{content:'';position:absolute;left:8px;right:8px;top:3px;height:5px;border-radius:3px;background:linear-gradient(180deg,rgba(255,255,255,.18),transparent)}
.mark{position:absolute;top:3px;bottom:3px;width:1px;background:rgba(236,236,238,.7)}
.mark.l{left:calc(50% - 18px)}.mark.r{left:calc(50% + 18px)}
.vial .m,.vial .p{position:absolute;top:50%;transform:translateY(-50%);font-size:9px;color:#7d7a6a}
.vial .m{left:8px}.vial .p{right:8px}
.bubble{position:absolute;top:2px;left:calc(50% - 15px + 6px);width:30px;height:17px;border-radius:9px;overflow:hidden;background:rgba(255,255,255,.16)}

/* ===== 02 Drop ===== */
.drop{position:absolute;left:99px;top:316px;width:89px;height:89px;border-radius:50%;overflow:hidden;z-index:3}
.drop .mag{position:absolute;inset:0;border-radius:50%;background:var(--scene) no-repeat;background-size:343px 458px;background-position:-127px -383px;filter:sepia(.2) saturate(1.2) contrast(1.05) hue-rotate(-6deg) brightness(1.1)}
.arc{position:absolute;left:50%;top:50%}
.arc i{position:absolute;left:-.5px;top:-34px;width:1px;height:5px;background:rgba(255,255,255,.75);transform-origin:50% 34px;transform:rotate(var(--a))}
.arc i.maj{height:8px;background:#fff}
.arc .ndl{position:absolute;left:-.5px;top:-31px;width:1px;height:31px;background:#fff;transform-origin:50% 31px;transform:rotate(8deg);box-shadow:0 0 4px rgba(255,255,255,.8)}
.drop .arc{top:58%}
.r1.wide{top:400px}

/* ===== 03 Cyclops ===== */
.rulers{position:absolute;left:21px;right:21px;top:395px;display:grid;gap:8px}
.ruler{display:grid;grid-template-columns:21px 1fr;align-items:center;gap:5px}
.ruler small{font-size:7.5px;color:#5f6167;letter-spacing:.08em}
.track{position:relative;height:21px;display:flex;justify-content:space-between;align-items:center;padding:0 5px;border-radius:5px;background:linear-gradient(180deg,rgba(255,255,255,.06),rgba(255,255,255,.02));box-shadow:inset 0 0 0 1px rgba(255,255,255,.08)}
.track span{font-size:7px;color:#55575d}
.track span.on{color:transparent}
.cyc{position:absolute;top:-4px;left:var(--x);transform:translateX(-50%);width:47px;height:29px;border-radius:15px;display:grid;place-items:center;font-style:normal}
.cyc b{font-size:12.5px;font-weight:500;color:#fff}
.cy .deck{top:510px}

/* ===== 04 Frosted window ===== */
.dial{position:absolute;left:0;right:0;top:362px;height:110px}
.dial .arc{top:100px}
.dial .arc i{top:-89px;height:13px;transform-origin:50% 89px;background:rgba(255,215,140,.95);box-shadow:0 0 6px rgba(255,190,90,.8)}
.dial .arc i.maj{height:21px}
.dial .ndl{top:-95px;height:95px;transform-origin:50% 95px;width:2px;background:#fff;box-shadow:0 0 8px rgba(255,255,255,.9);transform:rotate(-6deg)}
.slab{position:absolute;left:13px;right:13px;top:369px;bottom:13px;border-radius:34px;z-index:2;
  background:rgba(40,41,44,.35);-webkit-backdrop-filter:blur(13px) saturate(1.4);backdrop-filter:blur(13px) saturate(1.4);
  box-shadow:inset 0 1px 1px rgba(255,255,255,.4),inset 0 0 0 1px rgba(255,255,255,.08);
  -webkit-mask:linear-gradient(#000 0 0) top/100% 21px no-repeat,linear-gradient(#000 0 0) bottom/100% calc(100% - 42px) no-repeat;mask:linear-gradient(#000 0 0) top/100% 21px no-repeat,linear-gradient(#000 0 0) bottom/100% calc(100% - 42px) no-repeat}
.slit{position:absolute;left:13px;right:13px;top:390px;height:21px;z-index:2;box-shadow:inset 0 1px 0 rgba(255,255,255,.35),inset 0 -1px 0 rgba(255,255,255,.2)}
.fw-read{position:absolute;left:34px;right:34px;top:425px;display:flex;justify-content:space-between;font-size:9.5px;z-index:3}
.fw .lens{top:455px;z-index:3}
.fw .deck{z-index:3;top:497px}
.fw .shutter{box-shadow:inset 0 0 0 1.5px #ececee,0 0 0 8px rgba(255,255,255,.04)}

/* ===== 05 Construction ===== */
.cn .vf{box-shadow:0 0 0 1px rgba(255,255,255,.5)}
.spiral{position:absolute;inset:0;width:100%;height:100%}
.spiral path{fill:none;stroke:rgba(255,255,255,.4);stroke-width:2;vector-effect:non-scaling-stroke}
.spiral path{stroke-width:.75}
.spiral .sp{stroke:rgba(255,255,255,.85);stroke-width:1}
.dimv{position:absolute;left:21px;top:55px;width:1px;height:327px;background:rgba(255,255,255,.4)}
.dimv::before,.dimv::after{content:'';position:absolute;left:-3px;width:7px;height:1px;background:rgba(255,255,255,.6)}
.dimv::before{top:0}.dimv::after{bottom:0}
.dimv span{position:absolute;left:-5px;top:50%;transform:translateY(-50%);background:#000;padding:3px 0;font-size:10px;color:#cfd0d4}
.spec{position:absolute;left:34px;right:34px;top:400px;width:218px;border-collapse:collapse;font-size:8.5px}
.spec td{border:1px solid #2c2e31;padding:5px 6px;color:#6f7177;letter-spacing:.06em}
.spec td:nth-child(even){color:#ececee;font-size:10px}
.hair{position:relative;height:8px}
.hair i{position:absolute;left:0;right:0;top:4px;height:1px;background:repeating-linear-gradient(90deg,#6f7177 0 1px,transparent 1px 10%)}
.hair b{position:absolute;left:52%;top:0;width:1px;height:8px;background:#fff}
.cn .deck{top:500px}
.cn-sh{box-shadow:inset 0 0 0 1px #ececee}
.cn-sh::after{background:none;box-shadow:inset 0 0 0 1px rgba(255,255,255,.5)}
.cn-sh i{position:absolute;inset:-8px;background:linear-gradient(#fff,#fff) center/1px 100% no-repeat,linear-gradient(#fff,#fff) center/100% 1px no-repeat;opacity:.35}

/* ===== 06 Command line ===== */
.cl .top{color:#7d7f85}
.cmd{position:absolute;left:21px;right:13px;top:396px;margin:0;font:400 9.5px/1.75 var(--f-mono);color:#9a9ca2;white-space:pre}
.cmd i{font-style:normal;color:#5f6167}
.cmd b{font-weight:500;color:#fff;text-decoration:underline dotted rgba(255,255,255,.4);text-underline-offset:3px}
.cmd .pr{color:#e7c26a}
.cmd .dim{color:#5f6167}
.cur{display:inline-block;width:6px;height:12px;background:#e7c26a;vertical-align:-2px;margin-left:3px}
.cl .deck{top:497px}
.ret{width:89px;height:55px;border-radius:13px;display:grid;place-items:center;align-content:center;gap:2px;background:linear-gradient(180deg,#232427,#151618);box-shadow:inset 0 1px 0 rgba(255,255,255,.12),0 0 0 1px #34363a,0 5px 0 #0b0b0c}
.ret b{font-size:21px;font-weight:400;line-height:1}
.ret small{font-size:8px;color:#76787e;letter-spacing:.1em}
"""

body = f"""<title>Film Camera UI · Glass and Needle</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap">
<style>{CSS}</style>
<div class="wrap">
  <header class="hero">
    <span class="eyebrow">Working title pending · Round 6 · Static mockups</span>
    <h1>Glass and needle</h1>
    <p class="lede">Six simple screens, each built around one clever idea. Four pair liquid glass with an analog instrument, including two that hide the meter until it matters. Every screen shares one golden-ratio layout: the frame ends at 1/φ of the screen height, and all spacing comes from 5, 8, 13, 21, 34, 55 and 89.</p>
    <button class="tog" id="phi-toggle" type="button" aria-pressed="false"><i></i>Show φ guides</button>
  </header>
  <div class="grid">
{cards}
  </div>
  <footer>Round 6. The glass here is drawn with CSS: blur, saturation, an edge highlight and a magnified copy of the image under the drop. In the app, iOS 26 Liquid Glass (or a Metal shader on older iOS and on Android) would add true refraction at the edges.</footer>
</div>
<script>
(() => {{
const scene = document.createElement('canvas'); scene.width = 600; scene.height = 800;
{paint}
document.documentElement.style.setProperty('--scene', 'url(' + scene.toDataURL('image/jpeg', .85) + ')');
const b = document.getElementById('phi-toggle');
b.addEventListener('click', () => {{ const on = document.body.classList.toggle('show-phi'); b.setAttribute('aria-pressed', on); b.lastChild.textContent = on ? 'Hide φ guides' : 'Show φ guides'; }});
}})();
</script>
"""
(root / 'glass.html').write_text(body)
head = '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
i = body.index('</style>') + len('</style>')
(root / 'glass-standalone.html').write_text(head + body[:i] + '\n</head><body>\n' + body[i:] + '</body></html>\n')
print('ok', len(body))
