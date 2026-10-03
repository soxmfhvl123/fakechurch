"""FAKE CHURCH silver ornaments: solid cast pieces with an engraved inline.

Grammar:
  * every part is solid ink with a thin engraved line running just inside its edge
    (ink fill + ink stroke 2A, then a ground stroke 2B on the same edge: rim / groove / body)
  * pieces are assembled back to front, so overlaps read as soldered seams
  * centre medallions cover the joints of crosses
  * blackletter capitals are either cast (ink, with inline) or engraved (ground) into a band
Ink is currentColor; the ground is var(--g-bg) with a black fallback.
"""
import math

INK = 'currentColor'
BG = 'var(--g-bg, #0a0a0a)'
A, B = 4.0, 1.15          # rim half-width, groove half-width


def P(x, y):
    return f'{x:.2f} {y:.2f}'


def polar(r, deg, cx=0, cy=0):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def mirror(start, segs):
    pts = [start]
    for s in segs:
        pts.append(s[-2:])
    d = 'M' + P(*start)
    for s in segs:
        d += s[0] + ' '.join(P(s[i], s[i + 1]) for i in range(1, len(s), 2))
    for i in range(len(segs) - 1, -1, -1):
        s, p0 = segs[i], pts[i]
        if s[0] == 'L':
            d += 'L' + P(-p0[0], p0[1])
        else:
            x1, y1, x2, y2 = s[1:5]
            d += 'C' + P(-x2, y2) + ' ' + P(-x1, y1) + ' ' + P(-p0[0], p0[1])
    return d + 'Z'


def cast(d, a=A, b=B, extra=''):
    """Solid piece with an engraved inline."""
    return (f'<path d="{d}" fill="{INK}" stroke="{INK}" stroke-width="{2 * a:.2f}" stroke-linejoin="round" {extra}/>'
            f'<path d="{d}" fill="none" stroke="{BG}" stroke-width="{2 * b:.2f}" stroke-linejoin="round" {extra}/>')


def groove(d, w=1.6):
    return f'<path d="{d}" fill="none" stroke="{BG}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'


def engrave(d):
    return f'<path d="{d}" fill="{BG}"/>'


def circle_d(r, cx=0, cy=0):
    return f'M{P(cx + r, cy)}A{r} {r} 0 1 0 {P(cx - r, cy)}A{r} {r} 0 1 0 {P(cx + r, cy)}Z'


def g(body, tf):
    return f'<g transform="{tf}">{body}</g>'


# ------------------------------------------------------------- parts
def arm_flory(L=92, w=8):
    s = L / 92
    return mirror((0, 6), [
        ('L', w, 6), ('L', w, -52 * s),
        ('C', w, -58 * s, 14 * s, -60 * s, 22 * s, -58 * s),
        ('C', 31 * s, -56 * s, 35 * s, -65 * s, 30 * s, -73 * s),
        ('C', 27 * s, -79 * s, 19 * s, -79 * s, 17 * s, -72 * s),
        ('C', 15 * s, -67 * s, 11 * s, -68 * s, 9 * s, -72 * s),
        ('C', 11 * s, -80 * s, 7 * s, -88 * s, 0, -L),
    ])


def arm_pattee(L=90, w=7, end=28):
    s = L / 90
    return mirror((0, 6), [('L', w, 6), ('C', w + 1, -30 * s, end * .5, -60 * s, end, -86 * s),
                           ('L', 10 * s, -90 * s), ('L', 0, -80 * s)])


def medallion(r=15):
    return cast(circle_d(r)) + groove(circle_d(r * .45), 1.4) + f'<circle r="{r * .18:.2f}" fill="{BG}"/>'


def cross(arm, lengths, w=8, med=15, **kw):
    out = ''
    for deg, L in zip((0, 90, 180, 270), lengths):
        out += g(cast(arm(L, w, **kw)), f'rotate({deg})')
    for deg, L in zip((0, 90, 180, 270), lengths):   # a groove down every arm
        out += g(groove(f'M0 -{med + 6}L0 -{L * .52:.1f}', 1.3), f'rotate({deg})')
    return out + medallion(med)


def cross_flory(G):
    return cross(arm_flory, (92, 80, 92, 80)), '-108 -108 216 216'


def latin_flory(G):
    body = cross(arm_flory, (74, 62, 104, 62), w=7.5, med=13)
    return g(body, 'translate(0 -14)'), '-90 -104 180 218'


def cross_pattee(G):
    return cross(arm_pattee, (90, 90, 90, 90), w=7, med=0) + medallion(13), '-104 -104 208 208'


def fleur(G):
    side = ('M10 20C26 6 44 -2 56 -16C70 -32 66 -58 48 -62C38 -64 31 -54 38 -46C44 -51 52 -46 50 -38'
            'C46 -24 30 -10 20 6C16 12 14 18 14 24Z')
    tail = 'M8 34C18 46 30 58 48 58C58 58 63 49 56 43C52 49 42 50 33 42C25 36 17 32 10 30Z'
    centre = mirror((0, 30), [('L', 11, 30), ('C', 24, 0, 25, -50, 0, -98)])
    foot = mirror((0, 30), [('L', 9, 30), ('C', 11, 54, 7, 72, 0, 88)])
    band = 'M-40 14H40Q45 22 40 30H-40Q-45 22 -40 14Z'
    out = cast(side) + g(cast(side), 'scale(-1 1)') + cast(tail) + g(cast(tail), 'scale(-1 1)') + cast(foot)
    out += cast(centre) + groove('M0 -80L0 6', 1.3) + cast(band)
    out += ''.join(f'<circle cx="{x}" cy="22" r="2.2" fill="{BG}"/>' for x in (-26, -13, 0, 13, 26))
    return out, '-82 -106 164 206'


def dagger_parts():
    blade = mirror((0, 0), [('L', 11, 0), ('C', 11, 40, 7, 72, 0, 100)])
    grip = 'M-6 -46H6V0H-6Z'
    guard = 'M-40 -8H40V3H-40Z'
    out = cast(blade) + groove('M0 8L0 86', 1.3) + cast(grip)
    out += ''.join(groove(f'M-6 {y}L6 {y - 5}', 1.3) for y in (-6, -16, -26, -36))
    out += cast(guard)
    out += g(cast(arm_pattee(22, 3.2, 8)), 'translate(-40 -2.5) rotate(-90)') + g(cast(arm_pattee(22, 3.2, 8)), 'translate(40 -2.5) rotate(90)')
    out += cast(circle_d(10, 0, -58)) + groove(circle_d(4.5, 0, -58), 1.3)
    out += g(cast(arm_flory(22, 3)), 'translate(0 -66)')
    return out


def dagger(G):
    return dagger_parts(), '-74 -100 148 208'


def glyph_cast(G, ch, k, x, y, a=2.4, b=.75):
    d = G[ch]['d']
    if not b:   # solid cast letter, slightly fattened
        return g(f'<path d="{d}" fill="{INK}" stroke="{INK}" stroke-width="{2 * a / k:.1f}" stroke-linejoin="round"/>', f'translate({x:.2f} {y:.2f}) scale({k:.5f})')
    return g(cast(d, a / k, b / k), f'translate({x:.2f} {y:.2f}) scale({k:.5f})')


def text_engraved_arc(G, s, k, R, cx=0, cy=0, centre=-90, gap=0):
    adv = lambda c: (G[c]['adv'] if c in G else 320) * k + gap
    total = sum(adv(c) for c in s) - gap
    pos = -total / 2
    out = ''
    for c in s:
        a = adv(c) - gap
        ang = centre + math.degrees((pos + a / 2) / R)
        x, y = polar(R, ang, cx, cy)
        if c in G:
            out += g(engrave(G[c]['d']), f'translate({x:.2f} {y:.2f}) rotate({ang + 90:.2f}) translate({-a / 2:.2f} 0) scale({k:.5f})')
        pos += a + gap
    return out


def halo_ring(G):
    ro, ri = 90, 50
    a0, a1 = 122, 418
    q = lambda r, a: P(*polar(r, a))
    band = f'M{q(ro, a0)}A{ro} {ro} 0 1 1 {q(ro, a1)}L{q(ri, a1)}A{ri} {ri} 0 1 0 {q(ri, a0)}Z'
    out = cast(band)
    out += groove(f'M{q(ro - 6, a0 + 3)}A{ro - 6} {ro - 6} 0 1 1 {q(ro - 6, a1 - 3)}', 1.2)
    out += groove(f'M{q(ri + 6, a0 + 3)}A{ri + 6} {ri + 6} 0 1 1 {q(ri + 6, a1 - 3)}', 1.2)
    out += text_engraved_arc(G, 'FAKE CHURCH', .0205, 58, 0, 0, -90, gap=.6)
    for a in (a0 + 6, a1 - 6):
        x, y = polar((ro + ri) / 2, a)
        out += g(cast(circle_d(5)) , f'translate({x:.2f} {y:.2f})')
    out += g(cross(arm_pattee, (26, 26, 26, 26), w=2.6, med=0, end=9) + medallion(5), 'translate(0 2)')
    return out, '-100 -100 200 200'


def banner(G, words='STILL WORSHIP', k=.0185):
    tailL = 'M-88 -8L-118 -16L-104 4L-120 24L-88 20Z'
    band = 'M-96 -24Q0 -36 96 -24L96 18Q0 6 -96 18Z'
    out = cast(tailL) + g(cast(tailL), 'scale(-1 1)') + cast(band)
    out += groove('M-88 -17Q0 -28 88 -17', 1.1) + groove('M-88 11Q0 0 88 11', 1.1)
    out += text_engraved_arc(G, words, k, 900, 0, 908, -90, gap=.8)
    return out, '-128 -46 256 86'


def stacked(G, rows=('FA', 'KE', 'CH', 'UR', 'CH'), k=.05):
    out = ''
    lh = 1000 * k * 1.28
    for i, r in enumerate(rows):
        w = sum(G[c]['adv'] for c in r) * k
        x = -w / 2
        for c in r:
            out += glyph_cast(G, c, k, x, -len(rows) * lh / 2 + (i + .82) * lh, .6, 0)
            x += G[c]['adv'] * k
    return out, f'-60 {-len(rows) * lh / 2 - 10:.0f} 120 {len(rows) * lh + 20:.0f}'


def monogram(G):
    k = .12
    out = glyph_cast(G, 'F', k, -76, 52, 2.2, .7) + glyph_cast(G, 'C', k, -6, 58, 2.2, .7)
    return out, '-100 -100 200 200'


def star(G):
    pts = []
    for i in range(10):
        r = 94 if i % 2 == 0 else 38
        pts.append(polar(r, -90 + i * 36))
    d = 'M' + 'L'.join(P(*p) for p in pts) + 'Z'
    out = cast(d, 4.2, 1.2)
    out += ''.join(groove(f'M{P(*polar(20, -90 + i * 72))}L{P(*polar(78, -90 + i * 72))}', 1.2) for i in range(5))
    out += cast(circle_d(24)) + g(cross(arm_pattee, (17, 17, 17, 17), w=2, med=0, end=6), '') + f'<circle r="3.2" fill="{BG}"/>'
    return out, '-100 -100 200 200'


def sacred_heart(G):
    heart = 'M0 96C-62 56-76 14-50 -8C-30 -24-8 -16 0 0C8 -16 30 -24 50 -8C76 14 62 56 0 96Z'
    inner = 'M0 80C-50 48-62 16-42 -2C-27 -14-9 -8 0 6C9 -8 27 -14 42 -2C62 16 50 48 0 80Z'
    flame = 'M0 0C-14 -10-16 -26-6 -40C-4 -30 2 -30 0 -46C12 -36 16 -18 8 0Z'
    out = g(cast(flame), 'translate(-18 -2) rotate(-24) scale(.8)') + g(cast(flame), 'translate(18 -2) rotate(24) scale(.8)')
    out += g(cast(flame), 'translate(0 -6)')
    out += g(cross(arm_pattee, (20, 16, 6, 16), w=2.6, med=0, end=7), 'translate(0 -66)')
    out += cast(heart) + groove(inner, 1.3)
    out += cast('M-58 36C-30 22-8 50 18 32S48 26 64 30L66 40C46 36 32 42 18 46S-28 34-56 48Z', 3, 1)
    return out, '-90 -104 180 210'


def shield(G):
    sh = 'M-62 -66H62V-8C62 40 32 70 0 92C-32 70-62 40-62 -8Z'
    out = cast(sh) + groove('M-50 -54H50V-8C50 32 26 58 0 78C-26 58-50 32-50 -8Z', 1.3)
    out += g(dagger_parts(), 'translate(0 2) scale(.62)')
    for x in (-34, 34):
        out += g(cast(arm_flory(18, 2.6)) + g(cast(arm_flory(18, 2.6)), 'rotate(180)') +
                 g(cast(arm_flory(14, 2.6)), 'rotate(90)') + g(cast(arm_flory(14, 2.6)), 'rotate(-90)'), f'translate({x} -36)')
    return out, '-80 -86 160 190'


def strip(G):
    out = ''
    for x in (-92, 92):
        out += g(cross(arm_pattee, (15, 15, 15, 15), w=2, med=0, end=6) + f'<circle r="2.2" fill="{BG}"/>', f'translate({x} 0)')
    k = .03
    letters = 'FAKE'
    xs = [-48, -16, 16, 48]
    for c, x in zip(letters, xs):
        out += glyph_cast(G, c, k, x - G[c]['adv'] * k / 2, 10, .5, 0)
    for x in (-32, 0, 32):
        out += cast(circle_d(2.4, x, -1), 1.4, .4)
    return out, '-116 -24 232 46'


def cursor(G):
    o = [(-36, -88), (-36, 58), (-6, 30), (16, 82), (40, 72), (18, 22), (56, 22)]
    i = [(-28, -68), (-28, 38), (-4, 16), (17, 64), (27, 59), (6, 12), (36, 12)]
    out = cast('M' + 'L'.join(P(*p) for p in o) + 'Z', 4.2, 1.2)
    out += groove('M' + 'L'.join(P(*p) for p in i) + 'Z', 1.2)
    out += g(engrave(arm_pattee(22, 2.6, 8)) + g(engrave(arm_pattee(30, 2.6, 8)), 'rotate(180)') +
             g(engrave(arm_pattee(14, 2.4, 7)), 'rotate(90)') + g(engrave(arm_pattee(14, 2.4, 7)), 'rotate(-90)'), 'translate(-14 -22)')
    return out, '-80 -100 160 200'


def church_key(G):
    bow = cross(arm_flory, (34, 34, 34, 34), w=4, med=8)
    out = g(bow, 'translate(0 -66)')
    out += cast('M-6 -30H6V84H-6Z') + groove('M0 -22V76', 1.2)
    out += cast('M-13 -36H13V-26H-13Z')
    out += cast('M6 44H34V54H26V62H34V72H26V80H34V90H6Z')
    return out, '-60 -108 120 210'


def halo_cross(G):
    out = ''
    for i in range(8):
        a0 = -90 - 17 + i * 45 + 22.5
        a1 = a0 + 34
        q = lambda r, a: P(*polar(r, a))
        out += cast(f'M{q(70, a0)}A70 70 0 0 1 {q(70, a1)}L{q(54, a1)}A54 54 0 0 0 {q(54, a0)}Z', 3.4, 1)
    out += cross(arm_pattee, (94, 94, 94, 94), w=6.5, med=0, end=24) + medallion(13)
    return out, '-104 -104 208 208'


ORNAMENTS = [
    ('cross-flory', 'Cross Flory', 'Trefoil ends, groove-cut arms, medallion', cross_flory),
    ('halo-ring', 'Halo Ring', 'Open loading ring, FAKE CHURCH engraved', halo_ring),
    ('fleur', 'Fleur', 'Cast fleur-de-lis on a studded band', fleur),
    ('latin-flory', 'Latin Flory', 'Long-shaft cross flory', latin_flory),
    ('dagger', 'Dagger', 'Pattée quillons, flory pommel', dagger),
    ('stacked', 'FA KE CH UR CH', 'Stacked blackletter, cast', stacked),
    ('banner', 'Still Worship', 'Scroll banner, engraved capitals', banner),
    ('halo-cross', 'Halo Cross', 'Pattée cross on the segmented halo', halo_cross),
    ('monogram', 'FC', 'Cast blackletter monogram', monogram),
    ('shield', 'Shield', 'Dagger and flory crosses', shield),
    ('star', 'Star', 'Five points, pattée heart', star),
    ('sacred-heart', 'Sacred Heart', 'Flames, pattée cross, thorned band', sacred_heart),
    ('cross-pattee', 'Cross Pattée', 'Notched flared arms', cross_pattee),
    ('cursor', 'Cursor', 'Pointer with an engraved cross', cursor),
    ('church-key', 'Church Key', 'Flory bow', church_key),
    ('strip', 'F·A·K·E', 'Pattée-ended strip', strip),
]
