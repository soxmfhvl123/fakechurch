/* Split logo: blackletter over grotesque, the seam travelling down to swap them.
   Used by the loading screen and the home hero. The study page (LOGO-animation.html)
   carries its own copy with the other modes.

   SplitLogo.mount(canvas, {
     src: "assets/img/wordmark.webp",   blackletter artwork (transparent PNG/WebP)
     timeline: "loop" | "intro",         loop forever, or play the intro once
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
  const LOOP = [
    { from: BA, to: BA, d: 1.5 },               // blackletter over grotesque
    { from: BA, to: AB, d: .8, move: true },
    { from: AB, to: AB, d: 1.5 },               // grotesque over blackletter
    { from: AB, to: BA, d: .8, move: true },
  ];
  const INTRO = [
    { from: BA, to: BA, d: 1.1 },
    { from: BA, to: { top: "B", bot: "B", s: .5 }, d: .9, move: true },
    { from: { top: "B", bot: "B", s: .5 }, to: { top: "B", bot: "B", s: .5 }, d: .7 },
  ];

  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
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
    const segs = opts.timeline === "intro" ? INTRO : LOOP;
    const total = segs.reduce((s, x) => s + x.d, 0);
    let W = 0, H = 0, box = null, logo = null, raf = 0, start = 0, done = false;

    function layout() {
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      const r = canvas.getBoundingClientRect();
      W = canvas.width = Math.max(1, Math.round(r.width * dpr));
      H = canvas.height = Math.max(1, Math.round(r.height * dpr));
      const ratio = logo ? logo.naturalHeight / logo.naturalWidth : .3;
      // the mark fills the width, with room for the descending flourishes
      const bw = Math.min(W * .94, H / ratio * .78), bh = bw * ratio;
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
      for (const [word, a, b] of WORDS) {
        const ws = [...word].map(ch => c.measureText(ch).width);
        const len = ws.reduce((x, y) => x + y, 0) + track * (word.length - 1);
        let x = box.x + ((a + b) / 2) * box.w - len / 2;
        [...word].forEach((ch, i) => { c.fillText(ch, x, base); x += ws[i] + track; });
      }
    }
    function drawB() {
      const c = B.getContext("2d");
      c.clearRect(0, 0, W, H);
      if (logo) c.drawImage(logo, box.x, box.y, box.w, box.h);
    }

    // 1-bit blocks across a horizontal band, for the travelling seam
    function pixelate(src, block, y0, y1) {
      const sx = box.x - box.h * .2, sw = box.w + box.h * .4, sh = y1 - y0;
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

    function frame(now) {
      if (!start) start = now;
      let t = (now - start) / 1000;
      if (opts.timeline === "intro" && t >= total) {
        render(segs[segs.length - 1], segs[segs.length - 1].d);
        if (!done) { done = true; opts.onDone && opts.onDone(); }
        return;
      }
      t %= total;
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
