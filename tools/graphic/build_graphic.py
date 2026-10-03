"""Generate site/graphic.html: FAKE CHURCH brand graphics as outlined, self-contained SVGs."""
import json, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = sys.argv[1]
O = json.load(open(os.path.join(HERE, 'outlines.json')))

INK, BLACK, RED, C1, C2, PAPER = '#f2efe6', '#0a0a0a', '#c41e1e', '#d8d8d8', '#7c7c7c', '#efede8'

def chrome(gid):
    return (f'<linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="{C1}"/><stop offset=".5" stop-color="{C2}"/><stop offset="1" stop-color="{C1}"/>'
            f'</linearGradient>')

def svg(vb, body, defs='', label=''):
    d = f'<defs>{defs}</defs>' if defs else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}">'
            f'{d}{body}</svg>')

# ---------- halo: 8 annular segments, 34deg arc / 11deg gap, one segment centred at 12 o'clock
def halo_paths(cx=0, cy=0, ro=43, ri=37, arc=34, step=45, ring=True):
    out = []
    for i in range(8):
        a0 = math.radians(-90 - arc / 2 + i * step)
        a1 = a0 + math.radians(arc)
        p = lambda r, a: f'{cx + r * math.cos(a):.3f} {cy + r * math.sin(a):.3f}'
        out.append(f'M{p(ro, a0)}A{ro} {ro} 0 0 1 {p(ro, a1)}L{p(ri, a1)}A{ri} {ri} 0 0 0 {p(ri, a0)}Z')
    d = ''.join(out)
    inner = ''
    if ring:  # hairline inner ring as a filled annulus (outline, no stroke)
        r1, r2 = 30.3, 29.7
        inner = (f'M{cx + r1} {cy}A{r1} {r1} 0 1 0 {cx - r1} {cy}A{r1} {r1} 0 1 0 {cx + r1} {cy}Z'
                 f'M{cx + r2} {cy}A{r2} {r2} 0 1 1 {cx - r2} {cy}A{r2} {r2} 0 1 1 {cx + r2} {cy}Z')
    return d, inner

def halo_svg(fill, gid=None, ring=True, label='Halo symbol'):
    d, inner = halo_paths(ring=ring)
    defs = chrome(gid) if gid else ''
    f = f'url(#{gid})' if gid else fill
    body = f'<path fill="{f}" d="{d}"/>'
    if inner:
        body += f'<path fill="{f}" fill-rule="evenodd" opacity=".6" d="{inner}"/>'
    return svg('-50 -50 100 100', body, defs, label)

# ---------- stamp: lettering + double rule frame, in stamp-em units (F)
F = 500                       # stamp em in logo units
KNOCK = 22                    # knockout gap around the stamp ink, logo units

class Stamp:
    """Frame geometry follows the lettering it carries."""
    def __init__(self, key, scale, px=.22, py=.14):
        self.key, self.S = key, scale
        self.fx, self.fy, fw, fh = O[key]['box']
        self.TW, self.TH = fw * scale, fh * scale
        self.PX, self.PY = px * F, py * F
        self.BW, self.GAP, self.IL, self.R = .09 * F, .03 * F, .03 * F, .1 * F
        self.SW = self.TW + 2 * self.PX + 2 * self.BW
        self.SH = self.TH + 2 * self.PY + 2 * self.BW

    def group(self, color, mask=None, knock=0):
        """Drawn with its top-left at 0,0 (unrotated). knock>0 widens every shape (for masks)."""
        S, BW = self.S, self.BW
        tx = BW + self.PX - self.fx * S
        ty = BW + self.PY - self.fy * S
        m = f' mask="url(#{mask})"' if mask else ''
        o = BW / 2
        i = BW + self.GAP + self.IL / 2
        ts = (f'stroke="{color}" stroke-width="{2 * knock / S:.0f}" stroke-linejoin="round"' if knock else 'stroke="none"')
        return (f'<g fill="none" stroke="{color}"{m}>'
                f'<rect x="{o:.1f}" y="{o:.1f}" width="{self.SW - 2 * o:.1f}" height="{self.SH - 2 * o:.1f}" rx="{self.R - o:.1f}" stroke-width="{BW + 2 * knock:.1f}"/>'
                f'<rect x="{i:.1f}" y="{i:.1f}" width="{self.SW - 2 * i:.1f}" height="{self.SH - 2 * i:.1f}" rx="{max(self.R - i, 4):.1f}" stroke-width="{self.IL + 2 * knock:.1f}"/>'
                f'<path fill="{color}" {ts} transform="translate({tx:.1f} {ty:.1f}) scale({S:.5f})" d="{O[self.key]["d"]}"/>'
                f'</g>')

    def ink_mask(self, mid):
        """Rubber-stamp ink loss as an SVG mask (vector-compatible, resolution independent)."""
        W, H = self.SW + 100, self.SH + 100
        return (f'<filter id="{mid}f" x="0" y="0" width="1" height="1">'
                f'<feTurbulence type="fractalNoise" baseFrequency=".15" numOctaves="3" seed="4"/>'
                f'<feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 -2.4 2.15"/></filter>'
                f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="-50" y="-50" width="{W:.0f}" height="{H:.0f}">'
                f'<rect x="-50" y="-50" width="{W:.0f}" height="{H:.0f}" filter="url(#{mid}f)"/></mask>')

STENCIL = Stamp('fake', F / 2048)
GOTHIC = Stamp('fakeBl', 0.48, px=.18, py=.06)
SW, SH = STENCIL.SW, STENCIL.SH

def stamp_svg(color, inked=False, uid='s', label='FAKE stamp', st=STENCIL):
    defs = st.ink_mask(uid + 'm') if inked else ''
    pad = 40
    body = st.group(color, uid + 'm' if inked else None)
    return svg(f'{-pad} {-pad} {st.SW + 2 * pad:.0f} {st.SH + 2 * pad:.0f}', body, defs, label)

# ---------- primary lockup: CHURCH + rotated stamp
cx0, cy0, cw, ch = O['church']['box']
STAMP_C = (1850, -420)         # stamp centre in CHURCH outline units

def lockup_svg(word_fill, stamp_color, uid, inked=True, label='FAKE CHURCH primary logo', st=STENCIL):
    defs, wf = '', word_fill
    if word_fill == 'chrome':
        defs += chrome(uid + 'g'); wf = f'url(#{uid}g)'
    if inked:
        defs += st.ink_mask(uid + 'm')
    sx, sy = STAMP_C[0] - st.SW / 2, STAMP_C[1] - st.SH / 2
    place = f'rotate(-8 {STAMP_C[0]} {STAMP_C[1]}) translate({sx:.1f} {sy:.1f})'
    # knockout: CHURCH is cut back around the stamp's ink so the stamp reads cleanly
    defs += (f'<mask id="{uid}k" maskUnits="userSpaceOnUse" x="{cx0 - 400:.0f}" y="{cy0 - 400:.0f}" width="{cw + 800:.0f}" height="{ch + 800:.0f}">'
             f'<rect x="{cx0 - 400:.0f}" y="{cy0 - 400:.0f}" width="{cw + 800:.0f}" height="{ch + 800:.0f}" fill="#fff"/>'
             f'<g transform="{place}">{st.group("#000", None, knock=KNOCK)}</g></mask>')
    body = (f'<path fill="{wf}" mask="url(#{uid}k)" d="{O["church"]["d"]}"/>'
            f'<g transform="{place}">{st.group(stamp_color, uid + "m" if inked else None)}</g>')
    m = 160
    return svg(f'{cx0 - m:.0f} {cy0 - m:.0f} {cw + 2 * m:.0f} {ch + 2 * m:.0f}', body, defs, label)

# ---------- blackletter FAKE (outlined)
def word_svg(key, fill, uid, label, m=120):
    defs, f = '', fill
    if fill == 'chrome':
        defs = chrome(uid + 'g'); f = f'url(#{uid}g)'
    x, y, w, h = O[key]['box']
    return svg(f'{x - m:.0f} {y - m:.0f} {w + 2 * m:.0f} {h + 2 * m:.0f}', f'<path fill="{f}" d="{O[key]["d"]}"/>', defs, label)

# ---------- horizontal wordmark: halo + Fake Church
wx, wy, ww, wh = O['fakeChurch']['box']
def wordmark_svg(fill, uid, label='FAKE CHURCH wordmark'):
    defs, f = '', fill
    if fill == 'chrome':
        defs = chrome(uid + 'g'); f = f'url(#{uid}g)'
    hs = 9.5                         # halo 100u -> 950 units
    d, inner = halo_paths()
    gap = 380
    hx = wx - gap - 50 * hs          # halo centre x
    hy = -560                        # optical centre of the cap height
    body = (f'<g transform="translate({hx:.0f} {hy}) scale({hs})"><path fill="{f}" d="{d}"/>'
            f'<path fill="{f}" fill-rule="evenodd" opacity=".6" d="{inner}"/></g>'
            f'<path fill="{f}" d="{O["fakeChurch"]["d"]}"/>')
    left = hx - 50 * hs
    m = 140
    return svg(f'{left - m:.0f} {wy - m:.0f} {wx + ww - left + 2 * m:.0f} {wh + 2 * m:.0f}', body, defs, label)

# ---------- tagline
tx_, ty_, tw_, th_ = O['stillWorship']['box']
def tagline_svg(fill, uid, label='Still Worship. tagline'):
    defs, f = '', fill
    if fill == 'chrome':
        defs = chrome(uid + 'g'); f = f'url(#{uid}g)'
    m = 120
    return svg(f'{tx_ - m:.0f} {ty_ - m:.0f} {tw_ + 2 * m:.0f} {th_ + 2 * m:.0f}', f'<path fill="{f}" d="{O["stillWorship"]["d"]}"/>', defs, label)

# ---------- line icons (stroke = currentColor so they recolour anywhere)
ICONS = [
 ('Doctrine', '<path d="M32 6v52M14 22h36"/><circle cx="32" cy="22" r="20" stroke-dasharray="6 4"/>'),
 ('Scripture', '<path d="M32 14C24 9 14 9 6 12v40c8-3 18-3 26 2 8-5 18-5 26-2V12c-8-3-18-3-26 2zM32 14v40"/><path d="M12 22h12M12 30h12M40 22h12M40 30h12"/>'),
 ('Altar', '<rect x="18" y="20" width="28" height="34"/><path d="M24 28h16M24 34h16M24 40h16M12 54h40"/><circle cx="32" cy="10" r="6" stroke-dasharray="3 2"/>'),
 ('Baptism', '<path d="M14 30h36l-4 12H18z"/><path d="M26 42v10h12V42M20 52h24"/><circle cx="32" cy="16" r="9" stroke-dasharray="5 3"/>'),
 ('Communion', '<path d="M18 8h28c0 16-6 24-14 24S18 24 18 8z"/><path d="M32 32v18M22 56h20"/><path d="M24 14h6v6h6M36 14h4"/>'),
 ('Confession', '<path d="M16 56V16a16 16 0 0132 0v40z"/><circle cx="32" cy="30" r="7"/><path d="M27 30h10M27 27h10M27 33h10"/>'),
 ('Tithe', '<circle cx="24" cy="32" r="14"/><rect x="30" y="20" width="26" height="24" rx="3"/><path d="M30 28h26M36 38h8"/>'),
 ('Sabbath', '<rect x="12" y="16" width="40" height="28" rx="2"/><path d="M24 52h16M32 44v8"/><path d="M38 22a9 9 0 100 16 11 11 0 010-16z"/>'),
]
def icon_svg(name, body):
    return svg('0 0 64 64', f'<g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">{body}</g>', '', f'{name} icon')

# ---------- assemble cards
def card(fid, title, spec, art, bg='dark', wide=False, note=''):
    cls = 'g-card' + (' wide' if wide else '')
    n = f'<p class="g-note">{note}</p>' if note else ''
    return (f'<figure class="{cls}" id="{fid}"><div class="g-stage {bg}">{art}</div>'
            f'<figcaption><div><h3>{title}</h3><p class="mono">{spec}</p>{n}</div>'
            f'<div class="g-actions"><button class="mono" data-dl="{fid}">SVG ↓</button>'
            f'<button class="mono" data-png="{fid}">PNG ↓</button></div></figcaption></figure>')

sys.path.insert(0, HERE)
import emblems as EM
import ornaments as OR

def ornament_svg(fn, label):
    body, vb = fn(G)
    return svg(vb, body, '', label)

def ornament_sheet(bg, ink, label):
    """Sheet No. 1: the ornaments laid out like a cast sheet."""
    W, H = 1200, 1500
    cols, cw, ch = 4, 270, 330
    out = [f'<rect width="{W}" height="{H}" fill="{bg}"/>', f'<g color="{ink}">']
    for i, (k, _, _, fn) in enumerate(OR.ORNAMENTS):
        body, vb = fn(G)
        x, y, w, h = map(float, vb.split())
        sc = min(230 / w, 260 / h)
        cx = (W - cols * cw) / 2 + (i % cols) * cw + cw / 2
        cy = 90 + (i // cols) * ch + ch / 2
        out.append(f'<g transform="translate({cx:.1f} {cy:.1f}) scale({sc:.3f}) translate({-(x + w / 2):.1f} {-(y + h / 2):.1f})">{body}</g>')
    out.append('</g>')
    return svg(f'0 0 {W} {H}', ''.join(out).replace(OR.BG, bg), '', label)
G = O['glyphs']

def emblem_svg(fn, label):
    body, vb = fn(G)
    return svg(vb, body, '', label)

def plate(bg, ink, label):
    """Plate No. 1: the emblem set engraved on one sheet."""
    W, H = 1200, 1600
    out = [f'<rect width="{W}" height="{H}" fill="{bg}"/>',
           f'<g color="{ink}" style="--g-bg:{bg}">']
    fr = lambda m: f'M{m} {m}H{W - m}V{H - m}H{m}Z'
    out.append(EM.line(fr(48), 2.4) + EM.line(fr(60), 1.2))
    for x, y in ((60, 60), (W - 60, 60), (60, H - 60), (W - 60, H - 60)):
        out.append(f'<g transform="translate({x} {y})">{EM.lozenge_diamond(14)}</g>')
    body, vb = EM.crest(G)
    out.append(f'<g transform="translate(600 360) scale(2.2)">{body}</g>')
    picks = ['seeing-eye', 'sacred-heart', 'cursor', 'church-key', 'chalice', 'thorn-crown', 'rose-window', 'dagger', 'compass-star']
    table = {k: f for k, _, _, f in EM.EMBLEMS}
    cell = 300
    for i, k in enumerate(picks):
        cx = 300 + (i % 3) * cell
        cy = 820 + (i // 3) * 250
        body, vb = table[k](G)
        x, y, w, h = map(float, vb.split())
        sc = min(190 / w, 200 / h)
        out.append(f'<g transform="translate({cx} {cy}) scale({sc:.3f}) translate({-(x + w / 2):.1f} {-(y + h / 2):.1f})">{body}</g>')
    out.append(f'<g transform="translate(600 1500)">{EM.dotted_tagline(G, ["plate", "no", "one"], .028, 0, 0)}</g>')
    out.append('</g>')
    return svg(f'0 0 {W} {H}', ''.join(out).replace(EM.BG, bg), '', label)

sections = []
sections.append(('01', 'Primary Logo', 'Blackletter CHURCH struck with the FAKE customs stamp at −8°. All lettering is outlined; no fonts required.', ''.join([
    card('logo-primary', 'Primary', 'Chrome on black · inked stamp', lockup_svg('chrome', RED, 'lp'), 'dark', True),
    card('logo-ink', 'Mono, reversed', 'Bone white on black', lockup_svg(INK, RED, 'li'), 'dark'),
    card('logo-black', 'Mono, positive', 'Black on paper', lockup_svg(BLACK, RED, 'lb'), 'light'),
    card('logo-gothic', 'Gothic stamp', 'Blackletter Fake in the stamp frame', lockup_svg('chrome', RED, 'lg', st=GOTHIC), 'dark'),
    card('logo-gothic-black', 'Gothic stamp, positive', 'Black on paper', lockup_svg(BLACK, RED, 'lgb', st=GOTHIC), 'light'),
    card('logo-clean', 'Clean stamp', 'Without ink texture, for small sizes', lockup_svg('chrome', RED, 'lc', inked=False), 'dark'),
    card('logo-oneink', 'One colour', 'Single ink for engraving, foil, embossing', lockup_svg(BLACK, BLACK, 'lo', inked=False), 'light'),
])))
sections.append(('02', 'FAKE in Blackletter', 'The seizure word, set in the same blackletter as CHURCH. For engraving, merchandise and places where the stamp would be too loud.', ''.join([
    card('fake-bl-chrome', 'FAKE', 'Blackletter capitals · chrome', word_svg('FAKEBl', 'chrome', 'fbc', 'FAKE in blackletter'), 'dark', True),
    card('fake-bl-title', 'Fake', 'Blackletter title case · bone', word_svg('fakeBl', INK, 'fbt', 'Fake in blackletter'), 'dark'),
    card('fake-bl-red', 'FAKE, stamp red', 'Restricted use', word_svg('FAKEBl', RED, 'fbr', 'FAKE in blackletter, red'), 'dark'),
    card('fake-bl-black', 'FAKE, positive', 'Black on paper', word_svg('FAKEBl', BLACK, 'fbb', 'FAKE in blackletter, black'), 'light'),
    card('stamp-gothic', 'Gothic stamp', 'Blackletter Fake · inked', stamp_svg(RED, True, 'sg', 'Gothic FAKE stamp', GOTHIC), 'paper'),
])))
sections.append(('03', 'Wordmark', 'Halo and blackletter name, set as one horizontal line. Used in the site header.', ''.join([
    card('wordmark-chrome', 'Horizontal', 'Chrome on black', wordmark_svg('chrome', 'wc'), 'dark', True),
    card('wordmark-ink', 'Reversed', 'Bone white on black', wordmark_svg(INK, 'wi'), 'dark'),
    card('wordmark-black', 'Positive', 'Black on paper', wordmark_svg(BLACK, 'wb'), 'light'),
])))
sections.append(('04', 'Halo', 'The halo, reread as a loading spinner. Eight segments, 34° of arc and 11° of gap each, one segment centred at twelve o’clock. It never finishes loading.', ''.join([
    card('halo-chrome', 'Halo', 'Chrome · 8 × 34° / 11°', halo_svg(None, 'hc'), 'dark'),
    card('halo-ink', 'Halo, reversed', 'Bone white', halo_svg(INK), 'dark'),
    card('halo-black', 'Halo, positive', 'Black', halo_svg(BLACK), 'light'),
    card('halo-red', 'Halo, stamp red', 'Restricted use', halo_svg(RED, ring=False), 'dark'),
])))
sections.append(('05', 'Stamp', 'A customs seizure stamp. Red appears only at the moment of the stamp: hero, charter, and the end of the page.', ''.join([
    card('stamp-inked', 'FAKE, inked', 'Stamp red · ink-loss mask', stamp_svg(RED, True, 'si'), 'paper'),
    card('stamp-clean', 'FAKE, clean', 'Stamp red · solid', stamp_svg(RED, False, 'sc'), 'paper'),
    card('stamp-dark', 'FAKE on black', 'Stamp red · inked', stamp_svg(RED, True, 'sd'), 'dark'),
])))
or_cards = ''.join(card('or-' + key, name, spec, ornament_svg(fn, name), 'dark') for key, name, spec, fn in OR.ORNAMENTS)
sections.append(('06', 'Ornaments', 'Cast silver pieces. Solid metal with an engraved line just inside every edge; parts are soldered back to front, medallions cover the joints, capitals are cast or cut into bands.',
    '<div class="tone" role="group" aria-label="Ornament colour"><button class="mono" data-tone="bone" aria-pressed="true">Silver on black</button><button class="mono" data-tone="black" aria-pressed="false">Black on paper</button><button class="mono" data-tone="red" aria-pressed="false">Red on black</button></div><div class="sym-grid orn">' + or_cards + '</div>'))
em_cards = ''.join(card('em-' + key, name, spec, emblem_svg(fn, name), 'dark' + (' wide-em' if key == 'crest' else ''), key == 'crest')
                   for key, name, spec, fn in EM.EMBLEMS)
sections.append(('07', 'Emblems', 'Engravings of silver objects. One line weight, faceted lozenge spikes, double bands, ball finials; front shapes cover what lies behind. Blackletter is the only solid.',
    '<div class="tone" role="group" aria-label="Emblem colour"><button class="mono" data-tone="bone" aria-pressed="true">Bone on black</button><button class="mono" data-tone="black" aria-pressed="false">Black on paper</button><button class="mono" data-tone="red" aria-pressed="false">Red on black</button></div><div class="sym-grid">' + em_cards + '</div>'))
sections.append(('08', 'Sheets', 'The sets composed for print: poster, packaging insert, sticker sheet.', ''.join([
    card('sheet-black', 'Sheet No. 1', 'Ornaments · silver on black · 1200 × 1500', ornament_sheet('#0a0a0a', '#f2efe6', 'Sheet No. 1'), 'dark sheet'),
    card('sheet-paper', 'Sheet No. 1, paper', 'Ornaments · black on paper · 1200 × 1500', ornament_sheet('#ebe4d2', '#0a0a0a', 'Sheet No. 1, paper'), 'paper sheet'),
    card('plate-black', 'Plate No. 1', 'Bone on black · 1200 × 1600', plate('#0a0a0a', '#f2efe6', 'Plate No. 1'), 'dark poster'),
    card('plate-paper', 'Plate No. 1, paper', 'Black on paper · 1200 × 1600', plate('#ebe4d2', '#0a0a0a', 'Plate No. 1, paper'), 'paper poster'),
])))
sections.append(('09', 'Tagline', 'Still Worship.', ''.join([
    card('tagline-chrome', 'Tagline', 'Chrome on black', tagline_svg('chrome', 'tc'), 'dark', True),
    card('tagline-black', 'Tagline, positive', 'Black on paper', tagline_svg(BLACK, 'tb'), 'light'),
])))
sections.append(('10', 'Icons', 'Engraved line icons on a 64 grid, 1.4 stroke. Stroke uses currentColor, so they take the colour of their context.', '<div class="icon-grid">' + ''.join(
    card('icon-' + n.lower(), n, '64 × 64 · stroke 1.4', icon_svg(n, b), 'dark') for n, b in ICONS) + '</div>'))

COLORS = [('Deep Black', '--bg-deep', BLACK, 'Background'), ('Bone', '--ink', INK, 'Text'),
          ('Chrome Light', '--chrome-1', C1, 'Highlight'), ('Chrome Shadow', '--chrome-2', C2, 'Shadow'),
          ('Stamp Red', '--stamp-red', RED, 'The stamp only'), ('Gallery White', 'altar', PAPER, 'The Altar')]

body = []
for no, title, desc, inner in sections:
    grid = inner if inner.startswith('<div') else f'<div class="g-grid">{inner}</div>'
    body.append(f'<section class="g-sec" id="s{no}"><header class="g-head"><p class="mono kicker">{no}</p><h2>{title}</h2><p>{desc}</p></header>{grid}</section>')

sw = ''.join(f'<li><span class="sw" style="background:{hx}"></span><b>{n}</b><span class="mono">{hx.upper()}</span><span class="mono dim">{v}</span><em>{use}</em></li>' for n, v, hx, use in COLORS)
body.append(f'''<section class="g-sec" id="s11"><header class="g-head"><p class="mono kicker">11</p><h2>Colour</h2><p>Withholding colour is what makes the authority. Chrome is always a 135° gradient, light to shadow to light.</p></header>
<ul class="swatches">{sw}<li class="grad"><span class="sw" style="background:linear-gradient(135deg,{C1},{C2} 50%,{C1})"></span><b>Chrome Gradient</b><span class="mono">135° · {C1.upper()} → {C2.upper()} → {C1.upper()}</span></li></ul></section>''')
body.append('''<section class="g-sec" id="s12"><header class="g-head"><p class="mono kicker">12</p><h2>Typography</h2><p>Blackletter for names and titles; one Garamond for everything that is read. Blackletter is never used for running text.</p></header>
<div class="type-grid">
<div class="type-row"><p class="t-spec bl">Fake Church</p><div><b>Brotheric</b><span class="mono">Display · logo, chapter titles</span></div></div>
<div class="type-row"><p class="t-spec stampf">FAKE</p><div><b>Black Ops One</b><span class="mono">Stamp only</span></div></div>
<div class="type-row"><p class="t-spec serif">Thou shalt not turn off notifications.</p><div><b>EB Garamond</b><span class="mono">Body, scripture, creed, documents</span></div></div>
<div class="type-row"><p class="t-spec mono">REGION: AUTO · 404</p><div><b>EB Garamond, spaced capitals</b><span class="mono">Labels, numbers, data</span></div></div>
</div></section>''')

nav = ''.join(f'<a href="#s{no}">{t}</a>' for no, t, *_ in sections) + '<a href="#s11">Colour</a><a href="#s12">Typography</a>'

html = open(os.path.join(HERE, 'graphic_template.html'), encoding='utf-8').read()
html = html.replace('{{NAV}}', nav).replace('{{BODY}}', '\n'.join(body))
open(os.path.join(SITE, 'graphic.html'), 'w', encoding='utf-8').write(html)
print('ok', len(html) // 1024, 'KB')
