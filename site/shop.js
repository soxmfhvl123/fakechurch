(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const products = window.PRODUCTS || [];

  // [key, label, code prefix]; null entries start a new group in the filter bar
  const CATS = [
    ["all", "All"],
    null, ["apparel", "Apparel"],
    ["top", "Tops", "T"],
    ["outer", "Outerwear", "O"],
    ["bottom", "Bottoms", "B"],
    ["headwear", "Headwear", "H"],
    null, ["jewelry", "Jewelry"],
    ["ring", "Rings", "R"],
    ["pendant", "Pendants", "P"],
    ["necklace", "Necklaces", "N"],
    ["earring", "Earrings", "E"],
    ["bracelet", "Bracelets", "BR"],
  ];
  const catLabel = Object.fromEntries(CATS.filter(Boolean).map(([k, en, pre]) => [k, { en, pre }]));
  const inCat = (p, k) => k === "all" || p.cat === k || p.group === k;
  const won = n => "₩" + n.toLocaleString("en-US");
  const code = p => `FC-${catLabel[p.cat].pre}${String(products.filter(x => x.cat === p.cat).indexOf(p) + 1).padStart(2, "0")}`;

  /* ---------------- Filters ---------------- */
  const filters = $("#filters"), grid = $("#grid"), count = $("#shopCount");
  filters.innerHTML = CATS.map(c => {
    if (!c) return '<span class="filter-rule" aria-hidden="true"></span>';
    const [k, en, pre] = c;
    const n = products.filter(p => inCat(p, k)).length;
    const cls = k === "all" || !pre ? "group" : "";
    return `<button class="${cls}" data-cat="${k}" aria-pressed="false"><span class="en">${en}</span><sup class="mono">${n}</sup></button>`;
  }).join("");

  function setCat(cat, push = true) {
    if (!catLabel[cat]) cat = "all";
    $$("button", filters).forEach(b => b.setAttribute("aria-pressed", b.dataset.cat === cat));
    const list = products.filter(p => inCat(p, cat));
    grid.innerHTML = list.map((p, i) => `
      <a class="card" href="#${p.id}" data-id="${p.id}" style="--i:${i}">
        <div class="card-img">
          <img src="${p.images[0]}" alt="${p.name}" loading="lazy">
          ${p.images[1] ? `<img class="alt" src="${p.images[1]}" alt="" loading="lazy">` : ""}
        </div>
        <div class="card-meta">
          <p class="mono card-code">${code(p)}</p>
          <h3>${p.name}</h3>
          <p class="mono card-price">${won(p.price)}</p>
        </div>
      </a>`).join("");
    count.textContent = `${list.length} ${list.length === 1 ? "object" : "objects"}`;
    if (push) history.replaceState(null, "", cat === "all" ? "shop.html" : `shop.html?c=${cat}`);
  }
  filters.addEventListener("click", e => {
    const b = e.target.closest("button"); if (b) setCat(b.dataset.cat);
  });

  /* ---------------- Detail sheet ---------------- */
  const JEWELRY_SPECS = [["Material", "925 sterling silver"], ["Finish", "Oxidized, hand-polished"], ["Lead time", "Made to order, approx. 3 weeks"]];
  const sheet = $("#sheet");
  let lastFocus = null;

  function openItem(id) {
    const p = products.find(x => x.id === id); if (!p) return;
    lastFocus = document.activeElement;
    $("#sheetCat").textContent = `${code(p)} · ${catLabel[p.cat].en}`;
    $("#sheetName").textContent = p.name;
    $("#sheetPrice").textContent = won(p.price);
    $("#sheetDesc").textContent = p.desc;
    const img = $("#sheetImg");
    img.src = p.images[0]; img.alt = p.name;
    $("#sheetThumbs").innerHTML = p.images.length > 1
      ? p.images.map((src, i) => `<button aria-pressed="${i === 0}" data-src="${src}"><img src="${src}" alt=""></button>`).join("")
      : "";
    const sizes = p.cat === "ring" ? [5, 6, 7, 8, 9, 10, 11, 12] : p.sizes;
    $("#sheetSize").hidden = !sizes;
    if (sizes) {
      $("#sizeLabel").textContent = p.cat === "ring" ? "Size (US)" : "Size";
      $("#sizes").innerHTML = sizes.map((s, i) => `<button aria-pressed="${i === (p.cat === "ring" ? 3 : 1)}">${s}</button>`).join("");
    }
    const specs = p.specs || JEWELRY_SPECS;
    $("#sheetSpec").innerHTML = specs.map(([k, v]) => `<dt>${k}</dt><dd>${v}</dd>`).join("");
    sheet.hidden = false;
    requestAnimationFrame(() => sheet.classList.add("open"));
    document.body.style.overflow = "hidden";
    $(".sheet-close").focus();
  }
  function closeItem() {
    if (sheet.hidden) return;
    sheet.classList.remove("open");
    document.body.style.overflow = "";
    setTimeout(() => { sheet.hidden = true; }, 500);
    if (location.hash) history.replaceState(null, "", location.pathname + location.search);
    lastFocus?.focus?.();
  }

  grid.addEventListener("click", e => {
    const card = e.target.closest(".card"); if (!card) return;
    e.preventDefault();
    history.replaceState(null, "", "#" + card.dataset.id);
    openItem(card.dataset.id);
  });
  sheet.addEventListener("click", e => {
    if (e.target.closest("[data-close]")) return closeItem();
    const t = e.target.closest(".sheet-thumbs button");
    if (t) {
      $("#sheetImg").src = t.dataset.src;
      $$(".sheet-thumbs button").forEach(b => b.setAttribute("aria-pressed", b === t));
    }
    const s = e.target.closest(".sizes button");
    if (s) $$(".sizes button").forEach(b => b.setAttribute("aria-pressed", b === s));
  });

  /* ---------------- Menu ---------------- */
  const menu = $("#menu"), toggle = $("#menuToggle");
  const setMenu = open => {
    menu.classList.toggle("open", open); menu.setAttribute("aria-hidden", String(!open));
    toggle.setAttribute("aria-expanded", String(open));
  };
  toggle.addEventListener("click", () => setMenu(!menu.classList.contains("open")));
  document.addEventListener("keydown", e => {
    if (e.key !== "Escape") return;
    if (!sheet.hidden) closeItem(); else setMenu(false);
  });

  /* ---------------- Cursor halo ---------------- */
  const halo = $(".cursor-halo");
  document.addEventListener("pointermove", e => {
    halo.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
    halo.classList.toggle("on", !!e.target.closest("a, button"));
  }, { passive: true });
  document.addEventListener("pointerleave", () => halo.classList.remove("on"));

  // links elsewhere on the page (the look credits) point at #product-id
  window.addEventListener("hashchange", () => { if (location.hash.length > 1) openItem(location.hash.slice(1)); });

  /* ---------------- Init ---------------- */
  setCat(new URLSearchParams(location.search).get("c") || "all", false);
  if (location.hash) openItem(location.hash.slice(1));
})();
