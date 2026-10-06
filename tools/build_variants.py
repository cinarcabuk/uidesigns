"""Builds variants.html (artifact source) and variants-standalone.html: ten static E alternatives."""
import re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / 'concepts.html').read_text()
paint = src[src.index('(function paint(g){'):src.index("})(scene.getContext('2d'));") + len("})(scene.getContext('2d'));")]

BOLT = '<svg viewBox="0 0 24 24"><path d="M13 3 6 13.5h5L10 21l7-10.5h-5z"/></svg>'
BOLTA = BOLT + '<span class="bdg">A</span>'
FLIP = '<svg viewBox="0 0 24 24"><path d="M5 9a7 7 0 0 1 12.5-2.5M19 15a7 7 0 0 1-12.5 2.5"/><path d="M17.5 3v3.5H14M6.5 21v-3.5H10"/></svg>'
TIMER = '<svg viewBox="0 0 24 24"><circle cx="12" cy="13" r="7.5"/><path d="M12 9v4l2.5 2M10 3h4"/></svg>'

def meter(kind, needle=0.18):
    if kind == 'line':
        return f'<div class="m-line" style="--n:{needle}"><i class="m-ticks"></i><i class="m-ndl"></i><span>−3</span><span>0</span><span>+3</span></div>'
    if kind == 'led':
        return '<div class="m-led"><i>◀</i><b></b><i class="on">▶</i></div>'
    if kind == 'gauge':
        return f'<div class="m-gauge" style="--n:{needle}"><i></i></div>'
    if kind == 'vert':
        return f'<div class="m-vert" style="--n:{needle}"><i class="m-ticks"></i><i class="m-ndl"></i></div>'
    return ''

def top(film='AURUM 200', fc='#c9a24a', flags=''):
    return f'''<div class="row top"><span class="ro"><b>A</b><small>MODE</small></span><span class="ro"><small>ƒ</small>1.8</span>
      <span class="ro film"><i class="dot" style="--fc:{fc}"></i>{film}</span>{flags}<span class="ro"><small>EV</small><b>±0</b></span></div>'''

def bot(m, shutter='1/250', iso='200', auto=True):
    a = ' auto' if auto else ''
    return f'''<div class="row bot"><span class="ro{a}"><b>{shutter}</b><small>S</small></span>{meter(m)}<span class="ro{a}"><small>ISO</small><b>{iso}</b></span></div>'''

LENS = '<div class="lens"><span>26</span><span class="on">35</span><span>50</span><small>MM</small></div>'

def deck(custom=FLIP, flash=BOLTA, roll='36 / 36'):
    return f'''<div class="deck"><span class="shutter"></span><div class="mid"><span class="btn flash">{flash}</span><span class="btn custom">{custom}</span></div>
      <span class="roll"><span>{roll}</span></span></div>'''

def vf(extra=''):
    return f'<div class="vf"><div class="scene"></div><i class="cross"></i>{extra}</div>'

def phone(cls, inner):
    return f'''<div class="phone"><div class="screen {cls}"><div class="island"></div><div class="sb"><span>9:41</span><i class="bat"></i></div>{inner}</div></div>'''

V = []
# 1 Graphite
V.append(('Graphite', 'Dark brushed gunmetal, halfway between the black and the silver. The type is silver and the highlight is cooler and dimmer than on the silver version.',
  phone('graphite', top() + '<div class="mat">' + vf() + '</div>' + bot('line') + LENS + deck())))
# 2 Two-tone
V.append(('Two-Tone', 'A chrome top plate with black leatherette below, like a classic rangefinder body. The mode, film and EV readouts are engraved on the plate.',
  phone('twotone', '<div class="plate"></div>' + top(film='KINO 250D', fc='#b8352c') + '<div class="mat">' + vf() + '</div>' + bot('line') + LENS + deck())))
# 3 Leatherette
V.append(('Leatherette', 'An all-black pebbled body. Thin chrome rings frame each button and the camera roll. The leather texture stays in the margins and never touches the image.',
  phone('leather', top(film='ARGENT 400', fc='#c6c8cc') + '<div class="mat">' + vf('<i class="bw"></i>') + '</div>' + bot('line') + LENS + deck(roll='12 / 36'))))
# 4 LED finder
V.append(('LED Finder', 'Settings sit in one black info line under the image, like the LED readout in an SLR viewfinder. The meter is two arrows and a center dot, with one red arrow lit when you are off.',
  phone('ledf', top(film='NOCTA 800T', fc='#2c7d8c') + vf() + '<div class="infoline"><span>1/250</span><span>ƒ1.8</span>' + meter('led') + '<span>ISO 800</span><span>±0</span></div>' + LENS + deck())))
# 5 Edge print
V.append(('Edge Print', 'The readouts are printed like the edge markings on a film negative, in small mono type with frame numbers and sprocket marks above and below the image.',
  phone('edge', '<div class="edgerow"><i class="spr"></i><span>▸ 12</span><span>AURUM 200</span><span>A · ƒ1.8</span><span>EV ±0</span><i class="spr"></i></div>' + vf() +
        '<div class="edgerow"><i class="spr"></i><span>1/250</span>' + meter('line') + '<span>ISO 200</span><i class="spr"></i></div>' + LENS + deck(roll='12A'))))
# 6 Side rails
V.append(('Side Rails', 'The readouts run vertically down the left and right margins, and a vertical meter sits on the right. The space above and below the image stays almost empty.',
  phone('rails', '<div class="row top"><span class="ro film"><i class="dot" style="--fc:#d9846b"></i>VERANO 400</span></div>'
        '<div class="railwrap"><div class="rail l"><span class="ro"><b>A</b> MODE</span><span class="ro"><small>ƒ</small>1.8</span><span class="ro auto"><b>1/250</b></span></div>'
        + vf() + '<div class="rail r"><span class="ro"><small>EV</small> ±0</span>' + meter('vert') + '<span class="ro auto"><small>ISO</small> 400</span></div></div>' + LENS + deck())))
# 7 Bead-blast
V.append(('Bead-Blast', 'Matte silver with no brushing, like a sandblasted lens barrel. The shutter is black with a silver ring, the reverse of the chrome version.',
  phone('bead', top(film='LUMEN 100', fc='#3f66b8') + '<div class="mat">' + vf() + '</div>' + bot('line', iso='100') + LENS + deck())))
# 8 Black chrome
V.append(('Black Chrome', 'Glossy black with polished edges. The shutter, the ring around the camera roll and the lens underline are chrome, and the highlight on the black glass is sharper.',
  phone('bchrome', top(film='GRAFIT 3200', fc='#45474c') + vf('<i class="bw"></i>') + bot('line', iso='3200') + LENS + deck(roll='08 / 36'))))
# 9 Gauge
V.append(('Gauge', 'Brushed silver with a tiny round needle gauge between shutter speed and ISO, like the meter dial on a vintage rangefinder. The red needle is the only color.',
  phone('gauge', top(film='PASTEL 160', fc='#8fc1a9') + '<div class="mat">' + vf() + '</div>' + bot('gauge') + LENS + deck(custom=TIMER))))
# 10 Compact
V.append(('Compact', 'A silver point-and-shoot. The image sits in a deeply rounded black window, a round counter on the camera roll shows the frames left, and the buttons are chunkier.',
  phone('compact', top(film='INSTA 600', fc='#e9e1cf') + '<div class="mat">' + vf() + '</div>' + bot('line') + LENS +
        '<div class="deck"><span class="shutter"></span><div class="mid"><span class="btn flash">' + BOLTA + '</span><span class="btn custom">' + FLIP + '</span></div><span class="roll"><span class="cnt">36</span></span></div>')))

cards = '\n'.join(f'''<figure class="card"><div class="ph">{html}</div><figcaption><b>{i:02d}</b><div><h3>{name}</h3><p>{desc}</p></div></figcaption></figure>'''
                  for i, (name, desc, html) in enumerate(V, 1))

CSS = r"""
/* Layout: a contact sheet of ten static phones, each with a short caption. Single black look by design. */
:root{--bg:#0a0a0b;--ink:#e9eaec;--silver:#c3c6cb;--muted:#7d8087;--line:#26272a;
  --f-display:'Michroma','Eurostile','Arial Black',sans-serif;--f-body:'Archivo',system-ui,-apple-system,'Segoe UI',sans-serif;--f-mono:'IBM Plex Mono',ui-monospace,Menlo,monospace;
  --brushed:repeating-linear-gradient(0deg,rgba(255,255,255,.09) 0 1px,rgba(0,0,0,.045) 1px 2px,transparent 2px 3px),linear-gradient(180deg,#e1e3e6 0%,#babdc2 38%,#d2d4d8 62%,#a3a6ab 100%);
  --sheen:linear-gradient(104deg,rgba(255,255,255,0) 30%,rgba(255,255,255,.85) 44%,rgba(255,255,255,0) 56%,rgba(20,22,26,.28) 72%,rgba(20,22,26,0) 88%);
  --chrome:radial-gradient(circle at 42% 34%,#fff 0%,#d6d8db 22%,#8d9095 58%,#c9cbcf 82%,#6f7277 100%);
  --noise:url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 .5 0 0 0 0 .5 0 0 0 0 .5 0 0 0 .55 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  color-scheme:dark}
*{box-sizing:border-box}
html,body{background:var(--bg);color:var(--ink)}
body{font-family:var(--f-body);font-size:15px;line-height:1.55;padding-inline:clamp(16px,4vw,48px);padding-block:0 64px;background:radial-gradient(1200px 600px at 70% -10%,#1b1c1f 0%,transparent 60%),var(--bg)}
.wrap{max-width:1240px;margin:0 auto}
.hero{padding-block:56px 32px;display:grid;gap:16px;border-bottom:1px solid var(--line);margin-bottom:40px}
.eyebrow{font:500 11px var(--f-mono);letter-spacing:.18em;text-transform:uppercase;color:#8b8e94}
h1{font-family:var(--f-display);font-weight:400;font-size:clamp(26px,4.2vw,44px);line-height:1.12;margin:0;text-wrap:balance;
  background:linear-gradient(180deg,#f4f5f6 0%,#b7bac0 55%,#e2e4e7 70%,#8d9096 100%);-webkit-background-clip:text;background-clip:text;color:transparent}
.lede{max-width:68ch;color:#b9bcc2;margin:0}
.kept{display:flex;flex-wrap:wrap;gap:8px}
.kept span{font:500 11.5px var(--f-mono);color:var(--silver);border:1px solid var(--line);border-radius:999px;padding:5px 11px;background:#121214}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:48px 32px}
.card{margin:0;display:grid;gap:16px;justify-items:center}
.card figcaption{display:grid;grid-template-columns:auto 1fr;gap:12px;max-width:300px}
@media (min-width:980px){.grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:56px 40px}.card{grid-template-columns:300px minmax(0,1fr);align-items:center;justify-items:start;gap:28px}.card figcaption{max-width:34ch}}
.card figcaption>b{font:400 22px var(--f-display);color:transparent;-webkit-text-stroke:1px #8b8e94;line-height:1.1}
.card h3{margin:0 0 4px;font:400 13px var(--f-display);letter-spacing:.08em;text-transform:uppercase}
.card p{margin:0;font-size:13.5px;color:#a9acb2}
footer{padding-block:40px 0;color:var(--muted);font-size:13px}

/* ---- phone ---- */
.phone{width:300px;height:640px;border-radius:50px;padding:7px;flex:none;
  background:linear-gradient(140deg,#e6e8eb 0%,#7c7f85 22%,#cfd2d6 48%,#5d6065 72%,#b9bcc1 100%);box-shadow:0 0 0 1px #000,0 30px 60px -20px rgba(0,0,0,.8)}
.screen{position:relative;width:100%;height:100%;border-radius:43px;overflow:hidden;background:#000;display:flex;flex-direction:column;color:#e8e9eb;
  --ink:#d6d8db;--dim:#6c6f74;--auto:#8d9096}
.island{position:absolute;top:10px;left:50%;width:84px;height:24px;border-radius:14px;background:#000;transform:translateX(-50%);z-index:5}
.sb{flex:none;height:42px;display:flex;align-items:center;justify-content:space-between;padding:6px 26px 0;font-size:12px;font-weight:600;position:relative;z-index:2}
.bat{display:inline-block;width:22px;height:10px;border:1px solid currentColor;border-radius:3px;position:relative}
.bat::before{content:'';position:absolute;inset:1.5px 6px 1.5px 1.5px;background:currentColor;border-radius:1px}
.screen>*{position:relative;z-index:1}
.screen>.island{position:absolute;z-index:5}
.row{flex:none;display:flex;align-items:center;justify-content:space-between;gap:6px;padding:0 14px}
.top{height:30px}.bot{height:42px}
.ro{font:500 10.5px var(--f-mono);color:var(--ink);display:inline-flex;align-items:baseline;gap:4px;white-space:nowrap;letter-spacing:.03em}
.ro small{font-size:8px;color:var(--dim);letter-spacing:.1em}
.ro.auto b{color:var(--auto)}
.ro.auto::after{content:'A';font-size:7px;color:var(--dim);align-self:flex-start}
.dot{width:8px;height:8px;border-radius:50%;background:var(--fc);display:inline-block;align-self:center}
.vf{flex:none;position:relative;margin:0 16px;aspect-ratio:3/4;overflow:hidden;border-radius:1px;background:#111}
.scene{position:absolute;inset:0;background:var(--scene) center/cover;filter:sepia(.25) saturate(1.2) contrast(1.05) hue-rotate(-8deg)}
.cross{position:absolute;left:50%;top:50%;width:22px;height:22px;transform:translate(-50%,-50%)}
.cross::before,.cross::after{content:'';position:absolute;background:rgba(255,255,255,.9)}
.cross::before{left:50%;top:0;bottom:0;width:1.5px;transform:translateX(-50%)}
.cross::after{top:50%;left:0;right:0;height:1.5px;transform:translateY(-50%)}
.bw{position:absolute;inset:0;backdrop-filter:grayscale(1) contrast(1.2)}
.mat{flex:none;margin:0 12px;padding:5px;border-radius:7px;background:#050506;box-shadow:inset 0 2px 6px rgba(0,0,0,.9),0 1px 0 rgba(255,255,255,.6)}
.mat .vf{margin:0}
.lens{flex:none;height:40px;margin:4px 16px 0;display:flex;justify-content:center;align-items:center;gap:2px}
.lens span{font:400 12px var(--f-mono);color:var(--dim);padding:6px 10px;border-bottom:1px solid transparent}
.lens span.on{color:var(--ink);border-bottom-color:currentColor}
.lens small{font:500 8px var(--f-mono);color:var(--dim);letter-spacing:.12em;margin-left:2px}
.deck{flex:1;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;padding:4px 26px 16px;gap:10px}
.shutter{justify-self:start;width:74px;height:74px;border-radius:50%;box-shadow:inset 0 0 0 1.5px #e8e9eb;position:relative}
.shutter::after{content:'';position:absolute;inset:6px;border-radius:50%;background:#e8e9eb}
.mid{display:grid;justify-items:center;gap:8px}
.btn{position:relative;border-radius:50%;display:grid;place-items:center;border:1px solid #5d6065;color:#e8e9eb}
.btn svg{width:17px;height:17px;stroke:currentColor;fill:none;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
.btn .bdg{position:absolute;right:5px;top:4px;font:600 7px var(--f-mono)}
.flash{width:40px;height:40px}.custom{width:50px;height:50px}
.custom::after{content:'';position:absolute;right:3px;bottom:5px;width:4px;height:4px;border-radius:50%;background:currentColor;opacity:.5}
.roll{justify-self:end;width:62px;height:86px;position:relative;overflow:hidden;border:1px solid #6f7277;border-radius:3px;background:var(--scene) center/cover}
.roll>span{position:absolute;left:0;right:0;bottom:0;font:500 8px var(--f-mono);text-align:center;padding:8px 0 3px;background:linear-gradient(transparent,rgba(0,0,0,.85));color:#e8e9eb}

/* meters */
.m-line{position:relative;width:112px;height:26px}
.m-line .m-ticks{position:absolute;left:6px;right:6px;top:0;height:9px;
  background:repeating-linear-gradient(90deg,var(--tick,#8b8e94) 0 1px,transparent 1px calc((100% - 1px)/18));
  -webkit-mask:linear-gradient(#000 0 0) top/100% 5px no-repeat,repeating-linear-gradient(90deg,#000 0 1px,transparent 1px calc((100% - 1px)/6));mask:linear-gradient(#000 0 0) top/100% 5px no-repeat,repeating-linear-gradient(90deg,#000 0 1px,transparent 1px calc((100% - 1px)/6))}
.m-line .m-ndl{position:absolute;top:-4px;height:16px;width:1px;left:calc(50% + var(--n)*50px);background:var(--needle,#fff)}
.m-line .m-ndl::after{content:'';position:absolute;left:50%;top:-1px;transform:translateX(-50%);border:4px solid transparent;border-top:5px solid var(--needle,#fff);border-bottom:0}
.m-line span{position:absolute;bottom:1px;font:500 8.5px var(--f-mono);color:var(--dim);transform:translateX(-50%)}
.m-line span:nth-of-type(1){left:6px}.m-line span:nth-of-type(2){left:50%}.m-line span:nth-of-type(3){left:calc(100% - 6px)}
.m-led{display:flex;align-items:center;gap:8px;font-size:9px;color:#3a3b3e}
.m-led b{width:6px;height:6px;border-radius:50%;background:#3a3b3e}
.m-led .on{color:#ff4a3a;text-shadow:0 0 6px rgba(255,74,58,.9)}
.m-gauge{width:40px;height:40px;border-radius:50%;padding:2px;background:linear-gradient(145deg,#f4f5f6,#7d8086);box-shadow:0 2px 4px rgba(0,0,0,.4)}
.m-gauge i{display:block;width:100%;height:100%;border-radius:50%;position:relative;background:
  radial-gradient(circle at 50% 70%,#2a2a2a 0 2px,transparent 2.5px),
  conic-gradient(from -60deg at 50% 70%,transparent 0 0),radial-gradient(circle at 50% 30%,#fbfaf6,#dcd9d1);overflow:hidden}
.m-gauge i::before{content:'';position:absolute;left:4px;right:4px;top:6px;height:20px;border-radius:50% 50% 0 0;border-top:1px dashed #333;opacity:.8}
.m-gauge i::after{content:'';position:absolute;left:50%;bottom:30%;width:1px;height:18px;background:#b3261e;transform-origin:bottom;transform:rotate(calc(var(--n)*55deg))}
.m-vert{position:relative;width:16px;height:96px}
.m-vert .m-ticks{position:absolute;top:4px;bottom:4px;left:0;width:9px;background:repeating-linear-gradient(180deg,var(--tick,#8b8e94) 0 1px,transparent 1px calc((100% - 1px)/18));
  -webkit-mask:linear-gradient(#000 0 0) left/5px 100% no-repeat,repeating-linear-gradient(180deg,#000 0 1px,transparent 1px calc((100% - 1px)/6));mask:linear-gradient(#000 0 0) left/5px 100% no-repeat,repeating-linear-gradient(180deg,#000 0 1px,transparent 1px calc((100% - 1px)/6))}
.m-vert .m-ndl{position:absolute;left:-3px;width:16px;height:1px;top:calc(50% - var(--n)*44px);background:#fff}

/* ===== 01 Graphite ===== */
.graphite{background:linear-gradient(100deg,rgba(255,255,255,0) 30%,rgba(255,255,255,.12) 44%,rgba(255,255,255,0) 58%),repeating-linear-gradient(0deg,rgba(255,255,255,.035) 0 1px,rgba(0,0,0,.08) 1px 2px,transparent 2px 3px),linear-gradient(180deg,#3d3f43,#25262a 40%,#323438 66%,#1d1e21);
  --ink:#d9dbde;--dim:#7f8288;--auto:#9a9da2}
.graphite .mat{box-shadow:inset 0 2px 6px rgba(0,0,0,.9),0 1px 0 rgba(255,255,255,.14)}
.graphite .shutter{background:radial-gradient(circle at 42% 34%,#cfd1d4,#7b7e83 60%,#3d3f43);box-shadow:0 0 0 3px #17181a,0 0 0 4px rgba(255,255,255,.25)}
.graphite .shutter::after{display:none}
.graphite .btn{border:0;background:radial-gradient(circle at 45% 32%,#55575c,#1a1b1d 72%);box-shadow:0 0 0 1px rgba(255,255,255,.18),0 3px 6px rgba(0,0,0,.5)}
.graphite .roll{border:2px solid #0b0b0c;border-radius:5px}

/* ===== 02 Two-tone ===== */
.twotone{background:radial-gradient(rgba(255,255,255,.05) 1px,transparent 1.3px) 0 0/4px 4px,radial-gradient(rgba(0,0,0,.6) 1px,transparent 1.3px) 2px 2px/5px 5px,#131313;
  --ink:#d6d8db}
.twotone .plate{position:absolute;left:0;right:0;top:0;height:78px;z-index:0;background:var(--sheen),var(--brushed);box-shadow:0 1px 0 rgba(255,255,255,.5) inset,0 2px 0 #0a0a0a,0 3px 5px rgba(0,0,0,.6)}
.twotone .sb,.twotone .top{--ink:#17181a;--dim:#55585d;color:#17181a}
.twotone .top .ro{text-shadow:0 1px 0 rgba(255,255,255,.55)}
.twotone .mat{margin-top:6px}
.twotone .shutter{background:var(--chrome);box-shadow:0 0 0 3px #0a0a0a,0 0 0 4.5px #8d9095}
.twotone .shutter::after{display:none}
.twotone .btn{border:1.5px solid #9a9da2;background:#0d0d0d}
.twotone .roll{border:1.5px solid #9a9da2}

/* ===== 03 Leatherette ===== */
.leather{background:radial-gradient(circle at 30% 30%,rgba(255,255,255,.06) 0 1.2px,transparent 1.6px) 0 0/5px 5px,radial-gradient(circle at 70% 60%,rgba(0,0,0,.7) 0 1.4px,transparent 1.8px) 1px 2px/6px 6px,#151515}
.leather .mat{background:#000;box-shadow:0 0 0 1px #8d9095,inset 0 2px 6px rgba(0,0,0,.9)}
.leather .btn{border:0;background:#0c0c0c;box-shadow:0 0 0 2px #0c0c0c,0 0 0 3.5px #b9bcc1}
.leather .roll{border:0;box-shadow:0 0 0 2px #0c0c0c,0 0 0 3.5px #b9bcc1;border-radius:4px}
.leather .shutter{box-shadow:inset 0 0 0 1.5px #e8e9eb,0 0 0 3px #0c0c0c,0 0 0 4.5px #b9bcc1}
.leather .lens span.on{color:#fff}

/* ===== 04 LED finder ===== */
.ledf .vf{margin-bottom:0;border-radius:2px 2px 0 0}
.ledf .infoline{flex:none;margin:0 16px;height:30px;background:#050505;border:1px solid #1d1e20;border-top:0;display:flex;align-items:center;justify-content:space-between;padding:0 12px;
  font:500 10px var(--f-mono);color:#e8e9eb;letter-spacing:.06em}
.ledf .infoline span:nth-child(2){color:#8d9096}
.ledf .lens{margin-top:12px}

/* ===== 05 Edge print ===== */
.edge .edgerow{flex:none;height:30px;margin:0 16px;display:flex;align-items:center;justify-content:space-between;gap:6px;font:600 8.5px var(--f-mono);letter-spacing:.14em;color:#c9cbcf}
.edge .edgerow:nth-of-type(1){margin-top:4px}
.edge .spr{width:10px;height:7px;border:1px solid #6c6f74;border-radius:1.5px}
.edge .vf{margin-top:2px;outline:1px solid #2a2b2e;outline-offset:4px}
.edge .m-line{height:22px;--tick:#c9cbcf}
.edge .m-line span{display:none}
.edge .lens{margin-top:10px}
.edge .roll{border-radius:0;border-color:#c9cbcf}

/* ===== 06 Side rails ===== */
.rails .top{justify-content:center}
.rails .railwrap{flex:none;display:grid;grid-template-columns:28px 1fr 28px;align-items:stretch}
.rails .vf{margin:0;width:228px}
.rails .rail{display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:8px 0}
.rails .rail .ro{writing-mode:vertical-rl;transform:rotate(180deg)}
.rails .rail.r .ro{transform:none}
.rails .lens{margin-top:16px}

/* ===== 07 Bead-blast ===== */
.bead{background:var(--noise),linear-gradient(180deg,#d4d6d9,#c2c4c8 50%,#b6b8bc);color:#17181a;--ink:#1b1c1e;--dim:#5b5e63;--auto:#62656a;--tick:#3e4044;--needle:#b3261e}
.bead .ro{text-shadow:0 1px 0 rgba(255,255,255,.4)}
.bead .mat{box-shadow:inset 0 2px 6px rgba(0,0,0,.9),0 1px 0 rgba(255,255,255,.7)}
.bead .shutter{background:#111;box-shadow:0 0 0 3px #c9cbcf,0 0 0 4.5px #1b1c1e,0 5px 10px rgba(0,0,0,.3)}
.bead .shutter::after{inset:8px;background:radial-gradient(circle at 45% 35%,#3a3b3e,#0b0b0c 70%)}
.bead .btn{border:1.5px solid #1b1c1e;color:#1b1c1e;background:rgba(255,255,255,.12)}
.bead .roll{border:3px solid #111;border-radius:4px}

/* ===== 08 Black chrome ===== */
.bchrome{background:linear-gradient(112deg,rgba(255,255,255,0) 36%,rgba(255,255,255,.16) 44%,rgba(255,255,255,0) 47%),linear-gradient(160deg,#26272a,#050505 42%,#151618 64%,#000);--auto:#9a9da2}
.bchrome .vf{box-shadow:0 0 0 1px #3a3b3e,0 0 0 4px #000,0 0 0 5px #6f7277}
.bchrome .shutter{background:var(--chrome);box-shadow:0 0 0 3px #000,0 0 0 4px #9a9da2}
.bchrome .shutter::after{display:none}
.bchrome .btn{border:0;background:radial-gradient(circle at 45% 30%,#3a3b3e,#000 70%);box-shadow:0 0 0 1.5px #b9bcc1}
.bchrome .roll{border:0;box-shadow:0 0 0 1.5px #b9bcc1;border-radius:4px}
.bchrome .lens span.on{color:#fff;border-bottom:1.5px solid transparent;border-image:linear-gradient(90deg,#6f7277,#fff,#6f7277) 1}

/* ===== 09 Gauge ===== */
.gauge{background:var(--sheen),var(--brushed);color:#17181a;--ink:#1b1c1e;--dim:#5b5e63;--auto:#62656a}
.gauge .ro{text-shadow:0 1px 0 rgba(255,255,255,.55)}
.gauge .shutter{background:var(--chrome);box-shadow:0 0 0 3px #17181a,0 0 0 4.5px rgba(255,255,255,.7),0 6px 10px rgba(0,0,0,.35)}
.gauge .shutter::after{display:none}
.gauge .btn{border:0;color:#e3e5e8;background:radial-gradient(circle at 45% 32%,#4a4c50,#141516 70%);box-shadow:0 0 0 1.5px rgba(255,255,255,.6),0 3px 6px rgba(0,0,0,.4)}
.gauge .roll{border:3px solid #0b0b0c;border-radius:5px}

/* ===== 10 Compact ===== */
.compact{background:var(--sheen),var(--brushed);color:#17181a;--ink:#1b1c1e;--dim:#5b5e63;--auto:#62656a;--tick:#3e4044;--needle:#b3261e}
.compact .ro{text-shadow:0 1px 0 rgba(255,255,255,.55)}
.compact .mat{padding:9px;border-radius:26px;margin:2px 14px 0}
.compact .vf{border-radius:17px}
.compact .shutter{width:70px;height:70px;background:var(--chrome);box-shadow:0 0 0 5px #17181a,0 0 0 7px rgba(255,255,255,.7),0 8px 14px rgba(0,0,0,.35)}
.compact .shutter::after{display:none}
.compact .btn{border:0;background:#17181a;color:#e8e9eb;box-shadow:0 3px 0 #000,0 5px 8px rgba(0,0,0,.35)}
.compact .flash{width:42px;height:42px}.compact .custom{width:48px;height:48px}
.compact .roll{overflow:visible;border:3px solid #0b0b0c;border-radius:12px;background-clip:padding-box}
.compact .roll .cnt{position:absolute;left:auto;right:-12px;top:-12px;bottom:auto;width:30px;height:30px;padding:0;border-radius:50%;background:#050506;color:#fff;display:grid;place-items:center;font:500 11px var(--f-mono);
  box-shadow:inset 0 2px 4px #000,0 0 0 2px #c9cbcf}
"""

body = f"""<title>Film Camera UI · E Variants</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,300..800&family=IBM+Plex+Mono:wght@400;500;600&family=Michroma&display=swap">
<style>{CSS}</style>
<div class="wrap">
  <header class="hero">
    <span class="eyebrow">Working title pending · Round 4 · Static mockups</span>
    <h1>Ten more takes on E</h1>
    <p class="lede">These are still screens to compare, not working demos. Every variant keeps what we agreed on. Only the material, the meter style and where the details sit change. The black and silver E from round 3 is unchanged on its own page.</p>
    <div class="kept"><span>Black margin around the image</span><span>Small readouts around the frame</span><span>Compact meter</span><span>Lens selector only</span><span>Shutter · flash + custom · camera roll</span></div>
  </header>
  <div class="grid">
{cards}
  </div>
  <footer>Round 4. Tell me the numbers you like and I will make them interactive and add their editing screens.</footer>
</div>
<script>
(() => {{
const scene = document.createElement('canvas'); scene.width = 600; scene.height = 800;
{paint}
document.documentElement.style.setProperty('--scene', 'url(' + scene.toDataURL('image/jpeg', .85) + ')');
}})();
</script>
"""
(root / 'variants.html').write_text(body)
head = '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
i = body.index('</style>') + len('</style>')
(root / 'variants-standalone.html').write_text(head + body[:i] + '\n</head><body>\n' + body[i:] + '</body></html>\n')
print('ok', len(body))
