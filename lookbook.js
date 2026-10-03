(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const products = Object.fromEntries((window.PRODUCTS || []).map(p => [p.id, p]));
  const won = n => "₩" + n.toLocaleString("en-US");
  const pad = n => String(n).padStart(2, "0");

  // one running sequence for the full-screen view: silver details first, then the looks
  const B = window.BLEED || {};
  const frames = [
    ...(B.first ? [{ ...B.first, bleed: "first" }] : []),
    ...(window.SILVER || []).map(s => ({ ...s, key: `silver-${pad(s.no)}`, title: `Silver ${pad(s.no)}`, kicker: "Detail" })),
    ...(window.LOOKS || []).map(l => ({ ...l, key: `look-${pad(l.no)}`, title: `Look ${pad(l.no)}`, kicker: `${l.model} · ${l.light}` })),
    ...(B.last ? [{ ...B.last, bleed: "last" }] : []),
  ];

  // an item is a shop product id or a plain { name, href }
  const item = it => {
    if (typeof it !== "string") return { name: it.name, href: it.href, price: "" };
    const p = products[it];
    return p ? { name: p.name, href: `shop.html#${p.id}`, price: won(p.price) } : null;
  };
  const itemList = f => (f.items || []).map(item).filter(Boolean)
    .map(i => `<li><a href="${i.href}">${i.name}</a><span class="mono">${i.price}</span></li>`).join("");

  /* ---------------- Grid ----------------
     Editorial layouts on 12 columns: [column, aspect ratio, drop from the row top].
     Each set repeats its own pattern. */
  const LAYOUTS = {
    silver: [
      ["1 / span 6", "1 / 1", 0],
      ["8 / span 5", "4 / 5", .5],
      ["2 / span 4", "3 / 4", 0],
      ["7 / span 3", "1 / 1", .35],
      ["10 / span 3", "3 / 4", .8],
      ["1 / span 12", "16 / 7", 0],
      ["3 / span 4", "4 / 5", 0],
      ["8 / span 5", "1 / 1", .45],
    ],
    look: [
      ["1 / span 7", "4 / 5", 0],
      ["9 / span 4", "1 / 1", 1],
      ["2 / span 4", "3 / 4", 0],
      ["7 / span 6", "1 / 1", .55],
      ["1 / span 12", "16 / 7", 0],
      ["3 / span 5", "4 / 5", 0],
      ["9 / span 4", "3 / 4", .8],
    ],
  };
  const card = (f, i, n, set) => {
    const L = LAYOUTS[set];
    const [col, ar, drop] = L[n % L.length];
    return `
    <figure class="lb-card reveal${ar === "16 / 7" ? " wide" : ""}" id="${f.key}"
      style="--col:${col};--ar:${ar};--drop:${drop};--pos:${f.pos || "50% 50%"}">
      <button class="lb-open" data-i="${i}" aria-label="Open ${f.title}">
        <img src="${f.image}" alt="${f.alt}" loading="${i < 2 ? "eager" : "lazy"}">
        <span class="lb-no mono">${f.title}</span>
      </button>
    </figure>`;
  };
  // full-bleed plate: edge to edge, uncropped
  const bleed = f => `
    <figure class="lb-card lb-bleed ${f.bleed} reveal" id="${f.key}" style="--ar:${f.ratio}">
      <button class="lb-open" data-i="${frames.indexOf(f)}" aria-label="Open ${f.title}">
        <img src="${f.image}" alt="${f.alt}" loading="${f.bleed === "first" ? "eager" : "lazy"}"${f.bleed === "first" ? ' fetchpriority="high"' : ""}>
        <span class="lb-no mono">${f.title}</span>
      </button>
    </figure>`;
  const divider = (label, note) => `
    <header class="lb-divider reveal"><p class="mono">${label}</p><p class="mono">${note}</p></header>`;

  const silver = frames.filter(f => f.key.startsWith("silver"));
  const looks = frames.filter(f => f.key.startsWith("look"));
  let html = "";
  const first = frames.find(f => f.bleed === "first"), last = frames.find(f => f.bleed === "last");
  if (first) html += bleed(first);
  if (silver.length) html += divider("Silver", `${pad(silver.length)} details · 925 sterling`)
    + silver.map((f, n) => card(f, frames.indexOf(f), n, "silver")).join("");
  if (looks.length) html += divider("Looks", `${pad(looks.length)} looks · Season 01`)
    + looks.map((f, n) => card(f, frames.indexOf(f), n, "look")).join("");
  if (last) html += bleed(last);
  $("#lookGrid").innerHTML = html;

  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
  }), { threshold: .12 });
  document.querySelectorAll("#lookGrid .reveal").forEach(c => io.observe(c));

  /* ---------------- Full-screen view ---------------- */
  const view = $("#lookView");
  let cur = 0, lastFocus = null;

  function show(i) {
    cur = (i + frames.length) % frames.length;
    const f = frames[cur];
    $("#viewImg").src = f.image; $("#viewImg").alt = f.alt;
    $("#viewKicker").textContent = f.kicker;
    $("#viewTitle").textContent = f.title;
    $("#viewItems").innerHTML = itemList(f);
    $("#viewCount").textContent = `${pad(cur + 1)} / ${pad(frames.length)}`;
    history.replaceState(null, "", `#${f.key}`);
  }
  function open(i) {
    lastFocus = document.activeElement;
    show(i);
    view.hidden = false;
    requestAnimationFrame(() => view.classList.add("open"));
    document.body.style.overflow = "hidden";
    $("#viewClose").focus();
  }
  function close() {
    view.classList.remove("open");
    document.body.style.overflow = "";
    setTimeout(() => { view.hidden = true; }, 400);
    history.replaceState(null, "", location.pathname);
    lastFocus?.focus?.();
  }

  $("#lookGrid").addEventListener("click", e => {
    const b = e.target.closest(".lb-open"); if (b) open(+b.dataset.i);
  });
  $("#viewPrev").addEventListener("click", () => show(cur - 1));
  $("#viewNext").addEventListener("click", () => show(cur + 1));
  $("#viewClose").addEventListener("click", close);
  view.addEventListener("click", e => { if (e.target === view) close(); });

  /* ---------------- Menu, keys, cursor ---------------- */
  const menu = $("#menu"), toggle = $("#menuToggle");
  const setMenu = o => {
    menu.classList.toggle("open", o); menu.setAttribute("aria-hidden", String(!o));
    toggle.setAttribute("aria-expanded", String(o));
  };
  toggle.addEventListener("click", () => setMenu(!menu.classList.contains("open")));
  document.addEventListener("keydown", e => {
    if (!view.hidden) {
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") show(cur - 1);
      if (e.key === "ArrowRight") show(cur + 1);
    } else if (e.key === "Escape") setMenu(false);
  });

  const halo = $(".cursor-halo");
  document.addEventListener("pointermove", e => {
    halo.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
    halo.classList.toggle("on", !!e.target.closest("a, button"));
  }, { passive: true });

  // deep link: lookbook.html#look-02 or #silver-03
  if (location.hash.length > 1) {
    const i = frames.findIndex(f => f.key === location.hash.slice(1));
    if (i >= 0) open(i);
  }
})();
