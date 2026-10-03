"""FAKE CHURCH emblem set: monoline engravings of silver objects.

Grammar (shared by every piece):
  * one line weight (LW) everywhere, round joins
  * spikes are faceted lozenges: outline, centre ridge, girdle line
  * bands are double lines; ends close with a straight cap
  * tips end in ball finials
  * front shapes are filled with the ground colour so they occlude what is behind
  * blackletter is the only filled element, set on arcs or on a dotted baseline
Ink is currentColor; the ground is var(--g-bg) with a black fallback.
"""
import math

INK = 'currentColor'
BG = 'var(--g-bg, #0a0a0a)'
LW = 2.2


def P(x, y):
    return f'{x:.2f} {y:.2f}'


def polar(r, deg, cx=0, cy=0):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def line(d, w=LW, extra=''):
    return f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'


def shape(d, w=LW, fill=BG, extra=''):
    return f'<path d="{d}" fill="{fill}" stroke="{INK}" stroke-width="{w}" stroke-linejoin="round" {extra}/>'


def solid(d, extra=''):
    return f'<path d="{d}" fill="{INK}" {extra}/>'


def circle_d(r, cx=0, cy=0):
    return f'M{P(cx + r, cy)}A{r} {r} 0 1 0 {P(cx - r, cy)}A{r} {r} 0 1 0 {P(cx + r, cy)}Z'


def ball(x, y, r=4.2):
    return shape(circle_d(r, x, y))


# ------------------------------------------------------------- primitives
def lozenge(B, T, w, f=0.22, finial=4.2, girdle=True):
    """Faceted spike from base B to tip T, widest (half-width w) at fraction f."""
    bx, by = B
    tx, ty = T
    dx, dy = tx - bx, ty - by
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    mx, my = bx + dx * f, by + dy * f
    Lp = (mx + nx * w, my + ny * w)
    Rp = (mx - nx * w, my - ny * w)
    out = shape(f'M{P(bx, by)}L{P(*Lp)}L{P(tx, ty)}L{P(*Rp)}Z')
    out += line(f'M{P(bx, by)}L{P(tx, ty)}', LW * .55)
    if girdle:
        out += line(f'M{P(*Lp)}L{P(*Rp)}', LW * .55)
    if finial:
        out += ball(tx + ux * finial, ty + uy * finial, finial)
    return out


def band_segment(ro, ri, a0, a1, cx=0, cy=0):
    q = lambda r, a: P(*polar(r, a, cx, cy))
    large = 1 if (a1 - a0) > 180 else 0
    return shape(f'M{q(ro, a0)}A{ro} {ro} 0 {large} 1 {q(ro, a1)}L{q(ri, a1)}A{ri} {ri} 0 {large} 0 {q(ri, a0)}Z')


def halo_band(ro, ri, n=8, arc=34, offset=0, cx=0, cy=0, studs=False):
    step = 360 / n
    out = ''
    for i in range(n):
        a0 = -90 - arc / 2 + i * step + offset
        out += band_segment(ro, ri, a0, a0 + arc, cx, cy)
        if studs:
            out += ball(*polar((ro + ri) / 2, a0 + arc + (step - arc) / 2, cx, cy), 1.8)
    return out


def double_ring(ro, ri, cx=0, cy=0):
    return shape(circle_d(ro, cx, cy)) + shape(circle_d(ri, cx, cy))


def strand(d, width):
    """A centreline drawn as a double-line band (ink stroke, then ground stroke)."""
    return (f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{width + 2 * LW}" stroke-linecap="butt" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{BG}" stroke-width="{width}" stroke-linecap="butt" stroke-linejoin="round"/>')


def tick_cross(x, y, s=7, w=LW * .8):
    """Small engraved cross, used as sparkle."""
    return line(f'M{P(x, y - s)}L{P(x, y + s)}M{P(x - s * .62, y - s * .25)}L{P(x + s * .62, y - s * .25)}', w)


def sparkle(x, y, s=6):
    return line(f'M{P(x, y - s)}L{P(x, y + s)}M{P(x - s, y)}L{P(x + s, y)}', LW * .6) + \
        line(f'M{P(x - s * .4, y - s * .4)}L{P(x + s * .4, y + s * .4)}M{P(x + s * .4, y - s * .4)}L{P(x - s * .4, y + s * .4)}', LW * .45)


def lozenge_diamond(r, cx=0, cy=0, inner=.55):
    q = lambda rr: f'M{P(cx, cy - rr)}L{P(cx + rr, cy)}L{P(cx, cy + rr)}L{P(cx - rr, cy)}Z'
    return (shape(q(r)) + shape(q(r * inner)) +
            line(f'M{P(cx, cy - r)}L{P(cx, cy - r * inner)}M{P(cx + r, cy)}L{P(cx + r * inner, cy)}'
                 f'M{P(cx, cy + r)}L{P(cx, cy + r * inner)}M{P(cx - r, cy)}L{P(cx - r * inner, cy)}', LW * .55))


# ------------------------------------------------------------- text
def text_width(G, s, k):
    return sum(G[c]['adv'] * k if c in G else 300 * k for c in s)


def text_line(G, s, k, cx, baseline):
    """Blackletter on a straight baseline, centred on cx."""
    x = cx - text_width(G, s, k) / 2
    out = ''
    for c in s:
        if c in G:
            out += f'<g transform="translate({x:.2f} {baseline:.2f}) scale({k:.5f})">{solid(G[c]["d"])}</g>'
        x += (G[c]['adv'] if c in G else 300) * k
    return out


def text_arc(G, s, k, R, cx=0, cy=0, centre=-90, outward=True):
    """Blackletter set on a circle. outward=True: letters stand on the top arc."""
    total = text_width(G, s, k)
    pos = -total / 2
    out = ''
    for c in s:
        adv = (G[c]['adv'] if c in G else 300) * k
        mid = pos + adv / 2
        if outward:
            ang = centre + math.degrees(mid / R)
            x, y = polar(R, ang, cx, cy)
            rotd = ang + 90
        else:  # reads left-to-right along the bottom arc
            ang = centre - math.degrees(mid / R)
            x, y = polar(R, ang, cx, cy)
            rotd = ang - 90
        if c in G:
            out += (f'<g transform="translate({x:.2f} {y:.2f}) rotate({rotd:.2f}) translate({-adv / 2:.2f} 0) scale({k:.5f})">'
                    f'{solid(G[c]["d"])}</g>')
        pos += adv
    return out


def dotted_tagline(G, words, k, cx, baseline, gap=9):
    widths = [text_width(G, w, k) for w in words]
    total = sum(widths) + gap * 2 * (len(words) - 1)
    x = cx - total / 2
    out = ''
    for i, w in enumerate(words):
        out += text_line(G, w, k, x + widths[i] / 2, baseline)
        x += widths[i]
        if i < len(words) - 1:
            out += f'<circle cx="{x + gap:.2f}" cy="{baseline - 1000 * k * .28:.2f}" r="{1000 * k * .07:.2f}" fill="{INK}"/>'
            x += gap * 2
    return out


# ------------------------------------------------------------- emblems
def faceted_cross(cx=0, cy=0, s=1.0, halo=False):
    p = lambda x, y: (cx + x * s, cy + y * s)
    out = ''
    if halo:
        out += halo_band(54 * s, 44 * s, offset=22.5, cx=cx, cy=cy)
    out += lozenge(p(0, -12), p(0, -80), 11 * s, .2, 4.4 * s)
    out += lozenge(p(0, 12), p(0, 96), 11 * s, .16, 4.4 * s)
    out += lozenge(p(-12, 0), p(-66, 0), 10 * s, .22, 4.2 * s)
    out += lozenge(p(12, 0), p(66, 0), 10 * s, .22, 4.2 * s)
    out += lozenge_diamond(17 * s, cx, cy)
    return out


def crest(G):
    """Primary emblem: arched name, halo band, faceted cross, dotted tagline."""
    out = text_arc(G, 'fake church', .046, 100, 0, 20)
    out += halo_band(60, 49, offset=22.5, studs=True, cy=20)
    out += lozenge((0, 8), (0, -54), 11, .2, 4.4)
    out += lozenge((0, 32), (0, 104), 11, .16, 4.4)
    out += lozenge((-12, 20), (-78, 20), 10, .22, 4.2)
    out += lozenge((12, 20), (78, 20), 10, .22, 4.2)
    out += lozenge_diamond(17, 0, 20)
    for a in (-135, -45, 45, 135):
        out += sparkle(*polar(76, a, 0, 20), 5)
    out += dotted_tagline(G, ['still', 'worship'], .03, 0, 150)
    return out, '-132 -150 264 320'


def cross_emblem(G):
    return faceted_cross(), '-110 -100 220 220'


def halo_emblem(G):
    out = halo_band(80, 66, studs=True) + halo_band(56, 50, n=16, arc=14)
    for a in range(0, 360, 90):
        out += lozenge(polar(14, a - 90), polar(40, a - 90), 6, .25, 2.6)
    for a in range(45, 360, 90):
        out += lozenge(polar(12, a - 90), polar(30, a - 90), 4.5, .25, 0)
    out += shape(circle_d(9)) + shape(circle_d(4))
    return out, '-100 -100 200 200'


def seeing_eye(G):
    tri = shape('M0 -82L88 70H-88Z') + line('M0 -68L75 62H-75Z', LW * .7)
    eye = shape('M-52 22Q0 -18 52 22Q0 62 -52 22Z') + line('M-40 22Q0 -6 40 22Q0 50 -40 22Z', LW * .6)
    iris = double_ring(17, 12, 0, 22) + halo_band(9, 5.5, n=8, arc=30, cy=22)
    lashes = ''.join(line(f'M{P(x, 4 + abs(x) * .22)}L{P(x * 1.12, -6 + abs(x) * .26)}', LW * .7) for x in (-30, -15, 0, 15, 30))
    crosses = tick_cross(-62, -20, 8) + tick_cross(62, -20, 8) + tick_cross(0, -100, 9) + tick_cross(-98, 72, 7) + tick_cross(98, 72, 7)
    return tri + eye + lashes + iris + crosses, '-112 -116 224 200'


def sacred_heart(G):
    heart = 'M0 96C-62 54-76 12-50 -10C-30 -26-8 -18 0 -2C8 -18 30 -26 50 -10C76 12 62 54 0 96Z'
    inner = 'M0 82C-50 48-62 14-42 -4C-27 -16-9 -10 0 4C9 -10 27 -16 42 -4C62 14 50 48 0 82Z'
    flame = lambda dx, sc, rot: (f'<g transform="translate({dx} -6) rotate({rot}) scale({sc})">'
                                 + shape('M0 0C-14 -10-16 -26-6 -40C-4 -30 2 -30 0 -46C12 -36 16 -18 8 0Z')
                                 + line('M0 -4C-6 -12-6 -22-2 -30', LW * .55 / sc) + '</g>')
    flames = flame(-16, .8, -24) + flame(16, .8, 24) + flame(0, 1.05, 0)
    cross = lozenge((0, -50), (0, -92), 5, .3, 3) + line('M-11 -76H11', LW)
    out = flames + cross + shape(heart) + line(inner, LW * .6)
    out += strand('M-74 40C-46 24-18 56 8 36S50 24 76 30', 7)
    for x in (-50, -24, 2, 30, 54):
        out += line(f'M{P(x, 34 + 8 * math.sin(x / 15))}l4 -10', LW * .7)
    return out, '-100 -104 200 210'


def church_key(G):
    out = ''
    for c in [(0, -82), (14, -68), (0, -54), (-14, -68)]:
        out += double_ring(13, 8.5, *c)
    out += lozenge_diamond(7, 0, -68, .45)
    out += shape('M-6 -40H6V82H-6Z') + line('M0 -40V82', LW * .5)
    out += shape('M-12 -42H12V-34H-12Z') + shape('M-10 -26H10V-20H-10Z')
    out += shape('M6 46H34V55H25V62H34V71H25V78H34V86H6Z')
    out += lozenge((0, 82), (0, 98), 6, .2, 0, girdle=False)
    return out, '-60 -100 120 210'


def chalice(G):
    out = halo_band(18, 13, cy=-82) + shape(circle_d(4.5, 0, -82))
    out += shape('M-52 -44H52V-35H-52Z')
    out += shape('M-48 -35H48C48 6 26 24 0 26C-26 24 -48 6 -48 -35Z') + line('M-38 -26H38C36 4 18 16 0 18', LW * .55)
    out += shape('M-5 26H5V58H-5Z')
    out += lozenge_diamond(12, 0, 42, .5)
    out += shape('M-46 92C-36 76-14 70-7 58H7C14 70 36 76 46 92Z') + shape('M-50 92H50V99H-50Z')
    out += line('M-30 88C-22 80-10 74-4 66', LW * .5)
    return out, '-80 -110 160 220'


def thorn_crown(G):
    pts = lambda ph: 'M' + 'L'.join(P((62 + 7 * math.sin(7 * t + ph)) * math.cos(t), (62 + 7 * math.sin(7 * t + ph)) * math.sin(t))
                                    for t in [k / 240 * 2 * math.pi for k in range(241)]) + 'Z'
    out = strand(pts(0), 6) + strand(pts(math.pi), 6)
    for k in range(14):
        a = k * 360 / 14 + 6
        out_ = k % 2 == 0
        r0, r1 = (66, 88) if out_ else (58, 38)
        b1, b2 = polar(r0, a - 4), polar(r0, a + 4)
        tip = polar(r1, a + (5 if out_ else -5))
        out += shape(f'M{P(*b1)}Q{P(*polar((r0 + r1) / 2, a - 1))} {P(*tip)}Q{P(*polar((r0 + r1) / 2, a + 3))} {P(*b2)}Z', LW * .8)
    return out, '-100 -100 200 200'


def rose_window(G):
    out = double_ring(90, 82) + shape(circle_d(70))
    for k in range(8):
        a = -90 + k * 45
        out += double_ring(20, 15, *polar(46, a))
        out += line(f'M{P(*polar(24, a + 22.5))}L{P(*polar(70, a + 22.5))}', LW * .8)
        out += ball(*polar(76, a + 22.5), 2.4)
    for k in range(4):
        out += shape(circle_d(9.5, *polar(9.5, -90 + k * 90)))
    out += lozenge_diamond(6)
    return out, '-100 -100 200 200'


def cursor_gem(G):
    o = [(-34, -86), (-34, 56), (-6, 30), (16, 80), (38, 70), (17, 22), (54, 22)]
    i = [(-26, -66), (-26, 36), (-4, 16), (16, 62), (25, 58), (5, 12), (34, 12)]
    out = shape('M' + 'L'.join(P(*p) for p in o) + 'Z')
    out += line('M' + 'L'.join(P(*p) for p in i) + 'Z', LW * .6)
    out += line(''.join(f'M{P(*a)}L{P(*b)}' for a, b in zip(o, i)), LW * .45)
    out += lozenge((-14, -38), (-14, -58), 3.6, .25, 2, girdle=False) + lozenge((-14, -20), (-14, 10), 3.6, .2, 2, girdle=False)
    out += lozenge((-20, -30), (-30, -30), 3, .25, 1.8, girdle=False) + lozenge((-8, -30), (2, -30), 3, .25, 1.8, girdle=False)
    out += sparkle(52, -54, 7) + sparkle(-56, 78, 5)
    return out, '-80 -100 160 200'


def dagger(G):
    out = lozenge((0, 14), (0, 98), 9, .12, 0)
    out += shape('M-46 6C-34 4-22 2-10 2H10C22 2 34 4 46 6C40 14 22 16 10 14H-10C-22 16-40 14-46 6Z')
    out += ball(-50, 4, 3.6) + ball(50, 4, 3.6)
    out += shape('M-5 2V-50H5V2Z') + line('M-5 -14H5M-5 -26H5M-5 -38H5', LW * .55)
    out += lozenge_diamond(11, 0, -60, .5) + ball(0, -76, 4)
    return out, '-70 -100 140 210'


def compass_star(G):
    out = ''
    for k in range(8):
        a = -90 + k * 45
        L = 92 if k % 2 == 0 else 58
        w = 13 if k % 2 == 0 else 9
        out += lozenge((0, 0), polar(L, a), w, .3, 3.6 if k % 2 == 0 else 0)
    out += shape(circle_d(12)) + shape(circle_d(6.5))
    return out, '-104 -104 208 208'


def fake_seal(G):
    out = double_ring(94, 89) + double_ring(52, 48)
    out += text_arc(G, 'fake', .03, 57, 0, 0, -90, True)
    out += text_arc(G, 'church', .03, 85, 0, 0, 90, False)
    for a in (180, 0):
        out += lozenge_diamond(5, *polar(71, a))
    out += halo_band(40, 33, offset=22.5)
    out += lozenge((0, -6), (0, -30), 5, .2, 2.4) + lozenge((0, 6), (0, 34), 5, .16, 2.4)
    out += lozenge((-6, 0), (-26, 0), 4.5, .22, 2.4) + lozenge((6, 0), (26, 0), 4.5, .22, 2.4)
    out += lozenge_diamond(7)
    return out, '-100 -100 200 200'


def monogram(G):
    out = double_ring(86, 80) + halo_band(74, 68, n=24, arc=10)
    k = .068
    for ch, dx in (('F', -17), ('C', 19)):
        w = G[ch]['adv'] * k
        out += f'<g transform="translate({dx - w / 2:.2f} 30) scale({k})">{solid(G[ch]["d"])}</g>'
    out += tick_cross(0, -54, 6)
    return out, '-100 -100 200 200'


EMBLEMS = [
    ('crest', 'Crest', 'Primary emblem · arched name, halo, cross, dotted tagline', crest),
    ('fake-seal', 'Seizure Seal', 'Round seal · fake / church on the ring', fake_seal),
    ('monogram', 'FC Monogram', 'Signet monogram inside the studded halo', monogram),
    ('faceted-cross', 'Faceted Cross', 'Four lozenge arms, ball finials, double diamond', cross_emblem),
    ('halo', 'Halo', 'Segmented double band with studs', halo_emblem),
    ('compass-star', 'Star of Recommendation', 'Eight faceted rays', compass_star),
    ('seeing-eye', 'All-Seeing', 'Engraved eye, loading iris, struck crosses', seeing_eye),
    ('sacred-heart', 'Sacred Heart', 'Flames, cross and a thorned band', sacred_heart),
    ('cursor', 'Cursor, cut as a gem', 'Pointer drawn with crown and pavilion facets', cursor_gem),
    ('rose-window', 'Rose Window', 'Double tracery, eight lights', rose_window),
    ('thorn-crown', 'Crown of Thorns', 'Two braided strands', thorn_crown),
    ('church-key', 'Church Key', 'Quatrefoil bow, faceted bit', church_key),
    ('chalice', 'Chalice of the Host', 'The host is the loading halo', chalice),
    ('dagger', 'Dagger', 'Lozenge blade, ball quillons', dagger),
]
