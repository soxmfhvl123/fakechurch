"""Convert brand lettering to SVG outline paths (y-down, baseline at y=ascender)."""
import json, os, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = sys.argv[1]
FONTS = {
    'brotheric': os.path.join(SITE, 'assets/fonts/brotheric-regular.otf'),
    'stamp': os.path.join(HERE, 'blackopsone.ttf'),
}

def kern_table(font):
    """Pair kerning from the legacy 'kern' table, if any (GPOS is ignored)."""
    pairs = {}
    if 'kern' in font:
        for st in font['kern'].kernTables:
            pairs.update(st.kernTable)
    return pairs

def outline(fontkey, text, tracking=0):
    font = TTFont(FONTS[fontkey])
    gs = font.getGlyphSet()
    cmap = font.getBestCmap()
    hmtx = font['hmtx']
    upm = font['head'].unitsPerEm
    kern = kern_table(font)
    missing = [c for c in text if ord(c) not in cmap and c != ' ']
    pen = SVGPathPen(gs)
    x = 0
    prev = None
    names = [cmap.get(ord(c)) for c in text]
    for c, name in zip(text, names):
        if name is None:
            x += upm * 0.25
            prev = None
            continue
        if prev:
            x += kern.get((prev, name), 0)
        gs[name].draw(TransformPen(pen, (1, 0, 0, -1, x, 0)))
        x += hmtx[name][0] + tracking
        prev = name
    d = pen.getCommands()
    # tight bounds
    bp = BoundsPen(gs)
    x = 0; prev = None
    for name in names:
        if name is None:
            x += upm * 0.25; prev = None; continue
        if prev:
            x += kern.get((prev, name), 0)
        gs[name].draw(TransformPen(bp, (1, 0, 0, -1, x, 0)))
        x += hmtx[name][0] + tracking
        prev = name
    xmin, ymin, xmax, ymax = bp.bounds
    return {'d': d, 'box': [round(xmin, 1), round(ymin, 1), round(xmax - xmin, 1), round(ymax - ymin, 1)], 'missing': missing}

out = {
    'church': outline('brotheric', 'Church'),
    'fakeChurch': outline('brotheric', 'Fake Church'),
    'stillWorship': outline('brotheric', 'Still Worship.'),
    'fake': outline('stamp', 'FAKE', tracking=60),
    'fakeBl': outline('brotheric', 'Fake'),
    'FAKEBl': outline('brotheric', 'FAKE'),
}
def glyph_table(fontkey, chars):
    """Per-glyph outlines (origin at the left of the baseline) and advances."""
    font = TTFont(FONTS[fontkey])
    gs, cmap, hmtx = font.getGlyphSet(), font.getBestCmap(), font['hmtx']
    table = {}
    for c in chars:
        name = cmap.get(ord(c))
        if not name:
            continue
        pen = SVGPathPen(gs)
        gs[name].draw(TransformPen(pen, (1, 0, 0, -1, 0, 0)))
        table[c] = {'d': pen.getCommands(), 'adv': hmtx[name][0]}
    return table

out['glyphs'] = glyph_table('brotheric', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

for k, v in out.items():
    if k == 'glyphs':
        print('glyphs', len(v)); continue
    print(k, v['box'], 'missing:', v['missing'], 'len', len(v['d']))
json.dump(out, open(os.path.join(HERE, 'outlines.json'), 'w'), indent=0)
