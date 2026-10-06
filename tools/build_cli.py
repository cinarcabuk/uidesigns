"""Builds cli.html (artifact source) and cli-standalone.html: ten command-line camera layouts with X100-style button clusters."""
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / 'concepts.html').read_text()
paint = src[src.index('(function paint(g){'):src.index("})(scene.getContext('2d'));") + len("})(scene.getContext('2d'));")]

SB = '<div class="island"></div><div class="sb"><span>9:41</span><i class="bat"></i></div>'
def top(film='aurum200'):
    return f'<div class="top"><span>{film}</span><span>A · ƒ1.8</span><span>12/36</span></div>'
VF = '<div class="vf"><div class="scene"></div><i class="cross"></i><i class="cr tl"></i><i class="cr tr"></i><i class="cr bl"></i><i class="cr br"></i></div>'
CUR = '<span class="cur"></span>'
METER = 'meter  [·· ··· ·<b>|</b>· ··· ··]'
EXP_FLAGS = f'''<pre class="exp">expose <i>-s</i> <b>1/250</b> <i>-iso</i> <b>200</b>
       <i>-ev</i> <b>+0.0</b> <i>-mm</i> <b>35</b> <i>-f</i> <b>auto</b>{CUR}
<span class="d">{METER}</span></pre>'''
EXP_KV = f'''<pre class="exp">s=<b>1/250</b>  iso=<b>200</b>  ev=<b>+0.0</b>
mm=<b>35</b>   flash=<b>auto</b>  mode=<b>A</b>{CUR}
<span class="d">{METER}</span></pre>'''
EXP_COL = f'''<pre class="exp"><span class="d">shutter  iso   ev     mm  flash</span>
<b>1/250</b>    <b>200</b>   <b>+0.0</b>   <b>35</b>  <b>auto</b>{CUR}
<span class="d">{METER}</span></pre>'''

def k(label, val='', cls=''):
    v = f'<small>{val}</small>' if val else ''
    return f'<span class="k {cls}"><b>{label}</b>{v}</span>'
SHUT = '<span class="sh"></span>'
JOY = '<span class="joy"><i>▲</i><i>▶</i><i>▼</i><i>◀</i><b></b></span>'
def phone(cls, exp, deck, film='aurum200'):
    return f'<div class="phone"><div class="screen {cls}">{SB}{top(film)}{VF}{exp}<div class="deck">{deck}</div><i class="grit"></i></div></div>'

L = []
# 01 Rear Panel
L.append(('Rear Panel', 'The closest translation of the X100VI back. Keys run down the left like the camera\'s DISP/Q column, the focus joystick sits in the middle, and the shutter sits where your right thumb lands, with playback and flash under it.',
 phone('l1', EXP_FLAGS, f'''
  <div class="col">{k('FILM ▸','aurum')}{k('Q')}{k('DISP')}</div>
  <div class="mid">{JOY}{k('AE-L')}</div>
  <div class="right">{SHUT}<div class="pair">{k('▶')}{k('FLASH','auto')}</div></div>''')))

# 02 Top Plate
L.append(('Top Plate', 'The X100\'s top dials, turned into text strips. Shutter speed and exposure compensation scroll sideways under a bracket. One row below holds the film, flash, flip, shutter and playback keys.',
 phone('l2', EXP_KV, f'''
  <div class="strip"><small>S</small><span>1/60  1/125 <b>[1/250]</b> 1/500  1/1000</span></div>
  <div class="strip"><small>EV</small><span>−1.0  −0.3  <b>[+0.0]</b>  +0.3  +1.0</span></div>
  <div class="row">{k('FILM ▸')}{k('FLASH','auto')}{SHUT}{k('⟲','flip')}{k('▶')}</div>''')))

# 03 Key Grid
L.append(('Key Grid', 'Eight labelled keys in a tidy two-by-four grid, each showing its current value, with a tall shutter key on the right. Nothing is hidden and every key does exactly one thing.',
 phone('l3', EXP_COL, f'''
  <div class="grid8">{k('FILM','aurum')}{k('FLASH','auto')}{k('TIMER','off')}{k('DISP','grid')}{k('Q')}{k('AE-L','off')}{k('FLIP')}{k('PLAY','12')}</div>
  <span class="tall"><b>●</b><small>EXPOSE</small></span>''')))

# 04 Joystick
L.append(('Joystick', 'The focus lever is the hero. A large joystick moves the focus point, and four keys sit on its diagonals like a game controller: FILM, Q, PLAY and AE-L. The shutter is on its own to the right.',
 phone('l4', EXP_FLAGS, f'''
  <div class="pad">{k('FILM ▸','','d tl')}{k('Q','','d tr')}{k('▶','','d bl')}{k('AE-L','','d br')}<span class="joy big"><i>▲</i><i>▶</i><i>▼</i><i>◀</i><b></b></span></div>
  <div class="right">{SHUT}<div class="pair">{k('FLASH','auto')}{k('⟲')}</div></div>''')))

# 05 Thumb Rest
REST = '//// //// ////\n' * 7
L.append(('Thumb Rest', 'A right-handed layout. The left side is a textured thumb rest made of slashes, as on a real camera grip, so your left thumb has somewhere to sit. All controls are within reach of the right thumb.',
 phone('l5', EXP_KV, f'''
  <pre class="rest">{REST}</pre>
  <div class="rcl">{SHUT}<div class="g">{k('FILM ▸')}{k('Q')}{k('AE-L')}{k('▶')}{k('FLASH','auto')}{k('DISP')}</div></div>''')))

# 06 ASCII Hardware
ascii = """┌──────┐ ┌──────┐  ╭───────╮
│ FILM │ │FLASH │  │       │
│  >>  │ │ auto │  │   ●   │
└──────┘ └──────┘  │       │
┌──────┐ ┌──────┐  ╰───────╯
│  Q   │ │ PLAY │  [ SHOOT ]
└──────┘ └──────┘"""
L.append(('ASCII Hardware', 'The buttons are drawn entirely with box-drawing characters, so the hardware is made of the same text as everything else. It is the grittiest of the ten and pure command line.',
 phone('l6', EXP_FLAGS, f'<pre class="ascii">{ascii}</pre>')))

# 07 Function Row
L.append(('Function Row', 'A keyboard\'s function row. Six F-keys carry the camera functions, with their labels printed above, and a wide space bar is the shutter. It reads instantly to anyone who has used a keyboard.',
 phone('l7', EXP_COL, f'''
  <div class="flabels"><span>FILM</span><span>FLASH</span><span>TIMER</span><span>DISP</span><span>AE-L</span><span>PLAY</span></div>
  <div class="frow">{''.join(k(f'F{i}') for i in range(1,7))}</div>
  <span class="space"><b>EXPOSE</b><small>space</small></span>''')))

# 08 Dial + OK
L.append(('Command Dial', 'The X100\'s rear command dial, drawn as a ring of ticks with OK in the middle. Turn it to change whichever setting is selected and press OK to confirm. FILM, Q and DISP sit to the left, and the shutter and PLAY to the right.',
 phone('l8', EXP_KV, f'''
  <div class="col">{k('FILM ▸')}{k('Q')}{k('DISP')}</div>
  <span class="dial"><i></i><b>OK</b><small class="n">S</small><small class="e">ISO</small><small class="s">MM</small><small class="w">EV</small></span>
  <div class="right">{SHUT}{k('▶','12')}</div>''')))

# 09 Soft Keys
L.append(('Soft Keys', 'The last line of the exposure block labels four blank keys underneath it, like the soft keys on an old phone or a camera LCD. The labels can change by context, so four keys can do many jobs.',
 phone('l9', f'''<pre class="exp">expose <i>-s</i> <b>1/250</b> <i>-iso</i> <b>200</b> <i>-ev</i> <b>+0.0</b>{CUR}
<span class="d">{METER}</span>
<span class="soft">FILM▸    FLASH:A   TIMER:-   ROLL</span></pre>''', f'''
  <div class="blanks"><i></i><i></i><i></i><i></i></div>
  <div class="row3">{k('⟲','flip')}{SHUT}{k('AE-L')}</div>''')))

# 10 Split
L.append(('Split', 'The deck is split in two. On the left are the top-plate readouts as bracketed values, and on the right is the rear panel. The film button sits right under the shutter and shows which roll comes next.',
 phone('l10', EXP_COL, f'''
  <div class="tp"><small>// top</small><span>S   <b>[1/250]</b></span><span>ISO <b>[200]</b></span><span>EV  <b>[+0.0]</b></span><span>MM  <b>[35]</b></span></div>
  <div class="rp"><small>// rear</small>{SHUT}<span class="k film"><b>FILM ▸</b><small>next: verano400</small></span><div class="pair">{k('Q')}{k('▶')}{k('FLASH','a')}</div></div>''')))

cards = '\n'.join(f'''<figure class="card"><div class="ph">{html}</div><figcaption><span class="no">{i:02d}</span><h3>{n}</h3><p>{d}</p></figcaption></figure>'''
                  for i, (n, d, html) in enumerate(L, 1))

CSS = r"""
/* Layout: dark contact sheet. Phones share one shell: film line above a larger 2:3 frame, the exposure block, then a 132px deck that changes per layout. */
:root{--bg:#08080a;--ink:#e6e7e9;--dim:#74767c;--line:#222326;--amber:#e7c26a;
  --mono:'JetBrains Mono',ui-monospace,Menlo,monospace;
  --noise:url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='140' height='140'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 .5 0 0 0 0 .5 0 0 0 0 .5 0 0 0 1.4 -.25'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  color-scheme:dark}
*{box-sizing:border-box}
html,body{background:var(--bg);color:var(--ink)}
body{font-family:var(--mono);font-size:14px;line-height:1.6;padding-inline:clamp(16px,4vw,56px);padding-block:0 80px}
.wrap{max-width:1240px;margin:0 auto}
.hero{padding-block:72px 32px;border-bottom:1px dashed #2c2d30;margin-bottom:52px;display:grid;gap:16px}
.eyebrow{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--dim)}
h1{margin:0;font-weight:500;font-size:clamp(28px,4.6vw,48px);line-height:1.05;letter-spacing:-.03em}
h1 span{display:inline-block;width:.5em;height:.9em;background:var(--amber);vertical-align:-.08em;margin-left:.12em}
.lede{margin:0;color:#a6a8ae;max-width:68ch}
.rules{display:flex;flex-wrap:wrap;gap:8px}
.rules span{font-size:11.5px;color:#cfd0d4;border:1px solid #2c2d30;padding:4px 10px;border-radius:3px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:64px 32px}
.card{margin:0;display:grid;gap:18px;justify-items:center;align-content:start}
.card figcaption{max-width:300px;display:grid;gap:4px}
.no{font-size:11px;color:var(--dim)}
.card h3{margin:0;font-weight:500;font-size:17px}
.card p{margin:0;font-size:13px;color:#a6a8ae;font-family:system-ui,-apple-system,'Segoe UI',sans-serif;line-height:1.55}
footer{margin-top:72px;padding-top:18px;border-top:1px dashed #2c2d30;color:var(--dim);font-size:12.5px;max-width:72ch}

/* ---- phone shell ---- */
.phone{width:300px;height:640px;border-radius:50px;padding:7px;background:linear-gradient(140deg,#38393d,#141517 40%,#28292c 70%,#101011);box-shadow:0 0 0 1px #000,0 30px 50px -20px rgba(0,0,0,.8)}
.screen{position:relative;width:286px;height:626px;border-radius:43px;overflow:hidden;background:#050506;color:#dcdde0;font-family:var(--mono);text-shadow:0 0 3px rgba(255,255,255,.12)}
.grit{position:absolute;inset:0;pointer-events:none;background:var(--noise),repeating-linear-gradient(0deg,rgba(255,255,255,.025) 0 1px,transparent 1px 3px);background-size:140px,100%;mix-blend-mode:overlay;opacity:.55;z-index:10}
.island{position:absolute;top:10px;left:50%;width:84px;height:24px;border-radius:14px;background:#000;transform:translateX(-50%);z-index:11}
.sb{position:absolute;left:0;right:0;top:0;height:42px;display:flex;align-items:center;justify-content:space-between;padding:6px 26px 0;font:600 12px system-ui,sans-serif;text-shadow:none}
.bat{display:inline-block;width:22px;height:10px;border:1px solid currentColor;border-radius:3px;position:relative}
.bat::before{content:'';position:absolute;inset:1.5px 6px 1.5px 1.5px;background:currentColor;border-radius:1px}
.top{position:absolute;left:22px;right:22px;top:40px;display:flex;justify-content:space-between;font-size:9.5px;color:#9a9ca2}
.top span:first-child{color:#fff}
.vf{position:absolute;left:22px;top:56px;width:242px;height:363px;overflow:hidden;background:#111}
.scene{position:absolute;inset:0;background:var(--scene) center/cover;filter:sepia(.22) saturate(1.05) contrast(1.08) hue-rotate(-6deg)}
.cross{position:absolute;left:50%;top:50%;width:13px;height:13px;transform:translate(-50%,-50%)}
.cross::before,.cross::after{content:'';position:absolute;background:rgba(255,255,255,.85)}
.cross::before{left:50%;top:0;bottom:0;width:1px}.cross::after{top:50%;left:0;right:0;height:1px}
.cr{position:absolute;width:9px;height:9px;border:0 solid rgba(255,255,255,.7)}
.cr.tl{left:7px;top:7px;border-left-width:1px;border-top-width:1px}.cr.tr{right:7px;top:7px;border-right-width:1px;border-top-width:1px}
.cr.bl{left:7px;bottom:7px;border-left-width:1px;border-bottom-width:1px}.cr.br{right:7px;bottom:7px;border-right-width:1px;border-bottom-width:1px}
.exp{position:absolute;left:22px;right:10px;top:426px;margin:0;font:400 9.5px/1.7 var(--mono);color:#9a9ca2;white-space:pre}
.exp i{font-style:normal;color:#5f6167}
.exp b{font-weight:500;color:#fff;text-decoration:underline dotted rgba(255,255,255,.35);text-underline-offset:3px}
.exp .d{color:#5f6167}
.exp .d b{text-decoration:none;color:var(--amber)}
.cur{display:inline-block;width:6px;height:11px;background:var(--amber);vertical-align:-2px;margin-left:3px}
.deck{position:absolute;left:16px;right:16px;top:484px;height:126px}

/* shared parts */
.k{display:grid;place-items:center;align-content:center;gap:1px;min-height:28px;padding:3px 8px;border:1px solid #34363a;border-radius:3px;background:#0d0e10;box-shadow:0 2px 0 #000,inset 0 1px 0 rgba(255,255,255,.05);color:#e6e7e9;white-space:nowrap}
.k b{font:500 8.5px var(--mono);letter-spacing:.08em}
.k small{font:400 7px var(--mono);color:var(--amber);letter-spacing:.04em}
.sh{display:block;width:62px;height:62px;border-radius:50%;box-shadow:inset 0 0 0 1.5px #e6e7e9;position:relative;flex:none}
.sh::after{content:'';position:absolute;inset:6px;border-radius:50%;background:#e6e7e9}
.joy{position:relative;display:block;width:46px;height:46px;border-radius:50%;border:1px solid #34363a;background:radial-gradient(circle,#16171a 0 40%,#0b0b0d 41%)}
.joy b{position:absolute;left:50%;top:50%;width:16px;height:16px;margin:-8px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#5a5c61,#1a1b1d);box-shadow:0 0 0 1px #000}
.joy i{position:absolute;font-style:normal;font-size:6px;color:#74767c;line-height:1}
.joy i:nth-child(1){left:50%;top:3px;transform:translateX(-50%)}.joy i:nth-child(2){right:3px;top:50%;transform:translateY(-50%)}
.joy i:nth-child(3){left:50%;bottom:3px;transform:translateX(-50%)}.joy i:nth-child(4){left:3px;top:50%;transform:translateY(-50%)}
.pair{display:flex;gap:6px}
.right{position:absolute;right:0;top:0;bottom:0;display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:2px 0 4px}
.col{position:absolute;left:0;top:0;bottom:0;width:70px;display:flex;flex-direction:column;justify-content:space-between;padding:2px 0 4px}

/* 01 */
.l1 .mid{position:absolute;left:92px;top:2px;bottom:4px;display:flex;flex-direction:column;align-items:center;justify-content:space-between}
/* 02 */
.strip{display:grid;grid-template-columns:20px 1fr;align-items:center;height:20px;font-size:8.5px;color:#5f6167;white-space:pre;border-bottom:1px dashed #222326}
.strip small{font-size:7.5px}
.strip b{color:#fff;font-weight:500}
.l2 .row{position:absolute;left:0;right:0;bottom:2px;display:flex;justify-content:space-between;align-items:center}
/* 03 */
.grid8{position:absolute;left:0;right:76px;top:4px;display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:54px;gap:6px}
.grid8 .k{padding:3px 2px}
.tall{position:absolute;right:0;top:4px;width:68px;height:114px;border-radius:6px;display:grid;place-items:center;align-content:center;gap:4px;background:#e6e7e9;color:#050506;box-shadow:0 3px 0 #6f7277;text-shadow:none}
.tall b{font-size:22px;line-height:1}.tall small{font:600 7.5px var(--mono);letter-spacing:.14em}
/* 04 */
.pad{position:absolute;left:4px;top:0;width:150px;height:122px}
.joy.big{position:absolute;left:50%;top:50%;width:62px;height:62px;margin:-31px}
.joy.big b{width:22px;height:22px;margin:-11px}
.k.d{position:absolute;min-height:24px;padding:2px 6px}
.k.tl{left:0;top:0}.k.tr{right:0;top:0}.k.bl{left:0;bottom:0}.k.br{right:0;bottom:0}
/* 05 */
.rest{position:absolute;left:0;top:0;margin:0;font-size:9px;line-height:1.55;color:#2a2b2e;letter-spacing:.06em}
.rcl{position:absolute;right:0;top:0;bottom:0;width:150px;display:grid;justify-items:end;align-content:space-between}
.rcl .g{display:grid;grid-template-columns:repeat(3,1fr);gap:5px;width:150px}
.rcl .k{min-height:24px;padding:2px 4px}
/* 06 */
.ascii{position:absolute;left:0;top:0;margin:0;font:400 11px/1.16 var(--mono);color:#cfd0d4;white-space:pre;letter-spacing:0;top:4px}
/* 07 */
.flabels{display:grid;grid-template-columns:repeat(6,1fr);gap:4px;font-size:6.5px;letter-spacing:.06em;color:#74767c;text-align:center}
.frow{display:grid;grid-template-columns:repeat(6,1fr);gap:4px;margin-top:3px}
.frow .k{padding:3px 0;min-height:30px}
.space{position:absolute;left:0;right:0;bottom:4px;height:48px;border-radius:5px;display:grid;place-items:center;align-content:center;gap:1px;background:#e6e7e9;color:#050506;box-shadow:0 3px 0 #6f7277;text-shadow:none}
.space b{font:600 11px var(--mono);letter-spacing:.24em}.space small{font:500 7px var(--mono);color:#55575c}
/* 08 */
.dial{position:absolute;left:50%;top:50%;width:104px;height:104px;margin:-52px 0 0 -58px;border-radius:50%;border:1px solid #34363a;background:repeating-conic-gradient(#5f6167 0 1deg,transparent 1deg 7.5deg)}
.dial i{position:absolute;inset:13px;border-radius:50%;background:#050506;border:1px solid #34363a}
.dial b{position:absolute;left:50%;top:50%;width:40px;height:40px;margin:-20px;border-radius:50%;display:grid;place-items:center;font:600 9.5px var(--mono);background:#16171a;border:1px solid #4a4c50}
.dial small{position:absolute;font-size:6.5px;color:#9a9ca2}
.dial .n{left:50%;top:16px;transform:translateX(-50%);color:var(--amber)}.dial .s{left:50%;bottom:16px;transform:translateX(-50%)}
.dial .e{right:15px;top:50%;transform:translateY(-50%)}.dial .w{left:15px;top:50%;transform:translateY(-50%)}
/* 09 */
.soft{color:#e6e7e9}
.l9 .exp{top:430px}
.blanks{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-top:2px}
.blanks i{height:16px;border-radius:3px;border:1px solid #34363a;background:#0d0e10;box-shadow:0 2px 0 #000}
.row3{position:absolute;left:18px;right:18px;bottom:2px;display:flex;justify-content:space-between;align-items:center}
/* 10 */
.tp{position:absolute;left:0;top:0;bottom:0;width:112px;display:grid;align-content:space-between;font-size:9px;color:#74767c;white-space:pre;border-right:1px dashed #2c2d30;padding:2px 0 6px}
.tp small,.rp small{font-size:7.5px;color:#4a4c50}
.tp b{color:#fff;font-weight:500}
.rp{position:absolute;left:124px;right:0;top:0;bottom:0;display:grid;justify-items:center;align-content:space-between;padding-bottom:2px}
.rp small{justify-self:start}
.rp .sh{width:52px;height:52px}
.k.film{min-height:24px;width:100%}
.l10 .pair .k{min-height:22px;padding:2px 8px}
"""

body = f"""<title>Command Line Camera</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap">
<style>{CSS}</style>
<div class="wrap">
  <header class="hero">
    <span class="eyebrow">Working title pending · Round 7 · Static mockups</span>
    <h1>Command line camera<span></span></h1>
    <p class="lede">Ten button layouts for the command-line direction. The look stays gritty and monospace. The button arrangements borrow from the back of a Fujifilm X100VI: FILM, Q, AE-L, DISP and PLAY keys, a focus joystick and a command dial. They also bring back flash, flip and the camera roll from earlier rounds.</p>
    <div class="rules"><span>larger 2:3 frame</span><span>no $ prompt</span><span>film name above the frame</span><span>FILM ▸ key cycles stocks</span><span>exposure block kept</span><span>three block styles: flags · key=value · columns</span></div>
  </header>
  <div class="grid">
{cards}
  </div>
  <footer>Round 7. Every underlined value in an exposure block can be tapped to change it, and the FILM ▸ key moves to the next stock and updates the line above the frame. The earlier pages are unchanged.</footer>
</div>
<script>
(() => {{
const scene = document.createElement('canvas'); scene.width = 600; scene.height = 800;
{paint}
document.documentElement.style.setProperty('--scene', 'url(' + scene.toDataURL('image/jpeg', .85) + ')');
}})();
</script>
"""
(root / 'cli.html').write_text(body)
head = '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
i = body.index('</style>') + len('</style>')
(root / 'cli-standalone.html').write_text(head + body[:i] + '\n</head><body>\n' + body[i:] + '</body></html>\n')
print('ok', len(body))
