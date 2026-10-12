/* Split logo: blackletter and grotesque cut together. The intro runs one seam down to
   the full mark; the loop gives every letter its own cut, turning over at random moments.
   Used by the loading screen and the home hero. The study page (LOGO-animation.html)
   carries its own copy with the other modes.

   SplitLogo.mount(canvas, {
     src: "assets/img/wordmark.webp",   blackletter artwork (transparent PNG/WebP)
     timeline: "loop" | "intro",         loop forever, or play the intro once
     fit: .94,                            share of the canvas width the mark may take
     onDone: () => {},                   intro only: called when it has finished
   })
*/
(function () {
  const STEP = 12;                                  // the moving seam runs at 12 fps
  const INK = "#f2efe6";
  // where the blackletter lowercase body sits in the mark, measured from the artwork
  const BODY_TOP = .374, BODY_BASE = .781, SEAM = (BODY_TOP + BODY_BASE) / 2;
  const WORDS = [["FAKE", .03, .372], ["CHURCH", .458, .985]];   // "Fake" and "Church" spans
  const TRACK = -.14;                               // grotesque tracking, in em

  // A state is `top` above the cut and `bot` below it; s = where the cut sits
  // (0 = above the mark, all `bot`; .5 = the middle of the lowercase; 1 = below, all `top`).
  // A move wipes downward from one state to the next, so the two faces are always cut together.
  const BA = { top: "B", bot: "A", s: .5 }, AB = { top: "A", bot: "B", s: .5 };
  const INTRO = [
    { from: BA, to: BA, d: 1.1 },
    { from: BA, to: { top: "B", bot: "B", s: .5 }, d: .9, move: true },
    { from: { top: "B", bot: "B", s: .5 }, to: { top: "B", bot: "B", s: .5 }, d: .7 },
  ];

  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const hash = n => { const x = Math.sin(n * 127.1 + 311.7) * 43758.5453; return x - Math.floor(x); };

  // Loop (hero): every letter has its own cut. Each starts blackletter-over-grotesque or the
  // reverse, and turns over two or four times at its own moments: [start, duration, dir],
  // dir 1 = the cut runs down, -1 = up. An even number of turns closes the 12 s loop.
  const RANDOM = (() => {
    const L = 12, plans = [];
    for (let i = 0; i < 10; i++) {
      const n = hash(i * 7.3 + 1) > .4 ? 4 : 2, slot = L / n, ev = [];
      for (let k = 0; k < n; k++) {
        const d = .4 + hash(i * 3.1 + k * 5.7) * .4;
        ev.push([k * slot + .3 + hash(i * 11.9 + k * 2.3) * (slot - d - .6), d, hash(i * 4.4 + k * 9.1) > .5 ? 1 : -1]);
      }
      plans.push({ init: hash(i * 2.9 + 3.3) > .5, ev });
    }
    return { L, plans };
  })();
  const easeInOut = t => t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
  const images = {};
  const loadImage = src => images[src] || (images[src] = new Promise(res => {
    const im = new Image();
    im.onload = () => res(im); im.onerror = () => res(null);
    im.src = src;
  }));
  const fontReady = () => (document.fonts ? document.fonts.load('800 100px "Inter Tight"').catch(() => {}) : Promise.resolve());

  function mount(canvas, opts = {}) {
    const ctx = canvas.getContext("2d");
    const mk = () => document.createElement("canvas");
    const A = mk(), B = mk(), comp = mk(), small = mk();
    const intro = opts.timeline === "intro";
    const segs = INTRO;
    const total = intro ? segs.reduce((s, x) => s + x.d, 0) : RANDOM.L;
    let W = 0, H = 0, box = null, logo = null, raf = 0, start = 0, done = false, COLS = [];

    function layout() {
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      const r = canvas.getBoundingClientRect();
      W = canvas.width = Math.max(1, Math.round(r.width * dpr));
      H = canvas.height = Math.max(1, Math.round(r.height * dpr));
      const ratio = logo ? logo.naturalHeight / logo.naturalWidth : .3;
      // the mark fills the width, with room for the descending flourishes
      const bw = Math.min(W * (opts.fit || .94), H / ratio * .78), bh = bw * ratio;
      box = { x: (W - bw) / 2, y: (H - bh) / 2, w: bw, h: bh };
      for (const o of [A, B, comp]) { o.width = W; o.height = H; }
      drawA(); drawB();
    }

    function drawA() {
      const c = A.getContext("2d");
      c.clearRect(0, 0, W, H);
      const font = sz => `800 ${sz}px "Inter Tight", "Helvetica Neue", Arial, sans-serif`;
      c.font = font(100);
      const capRatio = (c.measureText("H").actualBoundingBoxAscent || 72.7) / 100;
      const size = (BODY_BASE - BODY_TOP) * box.h / capRatio;
      c.font = font(size);
      c.fillStyle = INK;
      const track = TRACK * size, base = box.y + BODY_BASE * box.h;
      const centres = [];
      for (const [word, a, b] of WORDS) {
        const ws = [...word].map(ch => c.measureText(ch).width);
        const len = ws.reduce((x, y) => x + y, 0) + track * (word.length - 1);
        let x = box.x + ((a + b) / 2) * box.w - len / 2;
        [...word].forEach((ch, i) => { c.fillText(ch, x, base); centres.push(x + ws[i] / 2); x += ws[i] + track; });
      }
      // one column per letter, split halfway between neighbours, the outer ones running to the edges
      COLS = centres.map((x, i) => [
        i ? Math.round((centres[i - 1] + x) / 2) : 0,
        i < centres.length - 1 ? Math.round((x + centres[i + 1]) / 2) : W,
      ]);
    }
    function drawB() {
      const c = B.getContext("2d");
      c.clearRect(0, 0, W, H);
      if (logo) c.drawImage(logo, box.x, box.y, box.w, box.h);
    }

    // 1-bit blocks across a horizontal band, for the travelling seam
    function pixelate(src, block, y0, y1, x0 = box.x - box.h * .2, x1 = box.x + box.w + box.h * .2) {
      const sx = x0, sw = x1 - x0, sh = y1 - y0;
      const cw = Math.max(1, Math.round(sw / block)), ch = Math.max(1, Math.round(sh / block));
      small.width = cw; small.height = ch;
      const c = small.getContext("2d");
      c.clearRect(0, 0, cw, ch);
      c.drawImage(src, sx, y0, sw, sh, 0, 0, cw, ch);
      try {
        const d = c.getImageData(0, 0, cw, ch), p = d.data;
        for (let i = 0; i < p.length; i += 4) { p[i] = 242; p[i + 1] = 239; p[i + 2] = 230; p[i + 3] = p[i + 3] > 92 ? 255 : 0; }
        c.putImageData(d, 0, 0);
      } catch (e) { /* file://: keep the soft blocks */ }
      ctx.imageSmoothingEnabled = false;
      ctx.drawImage(small, 0, 0, cw, ch, sx, y0, sw, sh);
      ctx.imageSmoothingEnabled = true;
    }

    function render(f, local) {
      const step = Math.floor(local * STEP);
      const top = box.y - box.h * .06, cut = box.y + SEAM * box.h, bot = box.y + box.h * 1.06;
      const seamAt = v => Math.round(v <= .5 ? top + (cut - top) * (v / .5) : cut + (bot - cut) * ((v - .5) / .5));
      const q = f.move ? easeInOut(clamp(step / (f.d * STEP), 0, 1)) : 1;
      const w = f.move ? Math.round(top + (bot - top) * q) : H;   // rows above w show `to`
      const kick = f.move ? Math.sin(Math.PI * q) : 0;
      const dx = Math.round(kick * box.w * .012);
      const S = { A, B };
      const c = comp.getContext("2d");
      const rows = (src, y0, y1, ox) => { if (y1 > y0) c.drawImage(src, 0, y0, W, y1 - y0, ox, y0, W, y1 - y0); };
      const state = (st, y0, y1, ox) => {
        const ys = seamAt(st.s);
        rows(S[st.top], y0, Math.min(y1, ys), ox);
        rows(S[st.bot], Math.max(y0, ys), y1, ox);
      };
      c.clearRect(0, 0, W, H);
      state(f.to, 0, w, -dx);
      state(f.from, w, H, dx);
      ctx.clearRect(0, 0, W, H);
      ctx.drawImage(comp, 0, 0);
      if (f.move) {
        const band = box.h * .16;
        ctx.clearRect(0, w - band / 2, W, band);
        pixelate(comp, box.h * (.03 + .05 * kick), w - band / 2, w + band / 2);
      }
    }

    // the random loop: a cut per letter
    function letterState(p, t) {
      let top = p.init;
      for (const [s0, d, dir] of p.ev) {
        if (t < s0) break;
        if (t < s0 + d) return { from: top, to: !top, local: t - s0, d, dir };
        top = !top;
      }
      return { from: top, to: top };
    }
    function renderLetters(t) {
      const top = box.y - box.h * .06, cut = Math.round(box.y + SEAM * box.h), bot = box.y + box.h * 1.06;
      const c = comp.getContext("2d");
      const slice = (src, x0, x1, y0, y1, ox) => {
        if (x1 > x0 && y1 > y0) c.drawImage(src, x0, y0, x1 - x0, y1 - y0, x0 + ox, y0, x1 - x0, y1 - y0);
      };
      c.clearRect(0, 0, W, H);
      const bands = [];
      COLS.forEach(([x0, x1], i) => {
        const st = letterState(RANDOM.plans[i], t);
        let w = H, up = st.to, lo = st.to, kick = 0;
        if (st.d) {
          const q = easeInOut(clamp(Math.floor(st.local * STEP) / (st.d * STEP), 0, 1));
          kick = Math.sin(Math.PI * q);
          if (st.dir > 0) { w = Math.round(top + (bot - top) * q); up = st.to; lo = st.from; }
          else { w = Math.round(bot - (bot - top) * q); up = st.from; lo = st.to; }
          bands.push([x0, x1, w, kick]);
        }
        const dx = Math.round(kick * box.w * .006);
        const rows = (bTop, y0, y1, ox) => {
          slice(bTop ? B : A, x0, x1, y0, Math.min(y1, cut), ox);
          slice(bTop ? A : B, x0, x1, Math.max(y0, cut), y1, ox);
        };
        rows(up, 0, w, -dx);
        rows(lo, w, H, dx);
      });
      ctx.clearRect(0, 0, W, H);
      ctx.drawImage(comp, 0, 0);
      const band = box.h * .14;
      for (const [x0, x1, w, kick] of bands) {
        ctx.clearRect(x0, w - band / 2, x1 - x0, band);
        pixelate(comp, box.h * (.025 + .04 * kick), w - band / 2, w + band / 2, x0, x1);
      }
    }

    function frame(now) {
      if (!start) start = now;
      let t = (now - start) / 1000;
      if (opts.timeline === "intro" && t >= total) {
        render(segs[segs.length - 1], segs[segs.length - 1].d);
        if (!done) { done = true; opts.onDone && opts.onDone(); }
        return;
      }
      t %= total;
      if (!intro) { renderLetters(t); raf = requestAnimationFrame(frame); return; }
      let acc = 0, seg = segs[0], local = 0;
      for (const f of segs) { if (t < acc + f.d) { seg = f; local = t - acc; break; } acc += f.d; }
      render(seg, local);
      raf = requestAnimationFrame(frame);
    }

    const ready = Promise.all([loadImage(opts.src || "assets/img/wordmark.webp"), fontReady()]).then(([im]) => {
      logo = im;
      if (!logo) { opts.onDone && opts.onDone(); return false; }
      layout();
      raf = requestAnimationFrame(frame);
      return true;
    });
    // re-measure whenever the canvas changes size (including when it first becomes visible)
    const ro = new ResizeObserver(() => { if (logo) layout(); });
    ro.observe(canvas);

    return {
      ready,
      stop() { cancelAnimationFrame(raf); ro.disconnect(); },
    };
  }

  window.SplitLogo = { mount };
})();
