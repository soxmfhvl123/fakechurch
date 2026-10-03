(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];

  /* ---------------- Doctrine content ---------------- */
  const CREED = [
    ["We believe the algorithm sees what we cannot say.",
     "At three in the morning we type into the search bar what we could never ask a friend. The search history is more honest than any diary."],
    ["We believe judgment, once ours, now belongs to the model.",
     "Where to eat, which way home, whom to meet. We have more choices than ever, and make fewer of them ourselves."],
    ["We believe convenience is a form of grace.",
     "Grace is freely given. The invoice arrives later, payable in data."],
    ["We believe every question already has a recommended answer.",
     "Autocomplete arrives before the question is finished. Usually, we take it."],
    ["We believe feelings are best measured in engagement.",
     "Grief is logged as time on page, anger as shares. A feeling that is not tracked does not appear in the report."],
    ["We believe moral decisions should be optimized, not agonized.",
     "Hesitation raises the bounce rate. The church promises a life in which you need never hesitate."],
    ["We believe the feed is the face of God, personalized.",
     "We worship the same god, yet each of us is shown a different face. This is why we no longer understand one another."],
    ["We believe in the loading, the halo that never completes.",
     "Salvation is always a few seconds away. While we wait, we worship."],
  ];
  $("#creed").innerHTML = CREED.map(([claim, gloss], i) => `
    <li class="reveal">
      <button aria-expanded="false">
        <span class="sec">§${i + 1}</span><span class="claim">${claim}</span><span class="plus">+</span>
      </button>
      <div class="gloss"><div><p>${gloss}</p></div></div>
    </li>`).join("");
  $("#creed").addEventListener("click", e => {
    const btn = e.target.closest("button"); if (!btn) return;
    const li = btn.parentElement, open = !li.classList.contains("open");
    li.classList.toggle("open", open);
    btn.setAttribute("aria-expanded", open);
  });

  /* ---------------- Reveal on scroll ---------------- */
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
  }, { threshold: 0.15, rootMargin: "0px 0px -5% 0px" });

  /* ---------------- Hero: the slogan types itself once ---------------- */
  function playHero() {
    const tag = $("#tagline"), text = "Still Worship.";
    setTimeout(() => {
      let i = 0;
      const t = setInterval(() => { tag.textContent = text.slice(0, ++i); if (i >= text.length) clearInterval(t); }, 110);
    }, 1200);
  }

  /* ---------------- Menu + single-page navigation ---------------- */
  const menu = $("#menu"), toggle = $("#menuToggle");
  const menuLinks = $$(".menu-list a");

  function openMenu() {
    menu.classList.add("open"); menu.setAttribute("aria-hidden", "false");
    toggle.setAttribute("aria-expanded", "true");
  }
  function closeMenu() {
    menu.classList.remove("open"); menu.setAttribute("aria-hidden", "true");
    toggle.setAttribute("aria-expanded", "false");
  }
  toggle.addEventListener("click", () => menu.classList.contains("open") ? closeMenu() : openMenu());
  document.addEventListener("keydown", e => { if (e.key === "Escape") closeMenu(); });

  // every in-page anchor scrolls smoothly; menu links also close the doors first
  document.addEventListener("click", e => {
    const a = e.target.closest('a[href^="#"]'); if (!a) return;
    const target = document.getElementById(a.getAttribute("href").slice(1)); if (!target) return;
    e.preventDefault();
    const inMenu = menu.contains(a);
    if (inMenu) closeMenu();
    setTimeout(() => target.scrollIntoView({ behavior: "smooth", block: "start" }), inMenu ? 450 : 0);
    history.replaceState(null, "", a.getAttribute("href"));
  });

  // highlight the chapter currently on screen
  const chapterIO = new IntersectionObserver(entries => {
    entries.forEach(en => {
      const id = en.target.classList.contains("hero") ? "top" : en.target.id;
      if (en.isIntersecting) menuLinks.forEach(a => a.classList.toggle("current", a.getAttribute("href") === "#" + id));
    });
  }, { rootMargin: "-45% 0px -50% 0px" });
  $$(".hero, .chapter").forEach(el => chapterIO.observe(el));

  // videos: load lazily, play only while visible
  const videoIO = new IntersectionObserver(entries => {
    entries.forEach(({ target: v, isIntersecting }) => {
      if (isIntersecting) {
        if (!v.getAttribute("src") && v.dataset.src) v.src = v.dataset.src;
        v.play().catch(() => {});
      } else v.pause();
    });
  }, { rootMargin: "200px 0px" });
  $$("video").forEach(v => videoIO.observe(v));

  $$(".reveal").forEach(el => io.observe(el));
  playHero();

  /* ---------------- Scripture: TOC highlight + gospel tabs ---------------- */
  const tocLinks = $$(".toc a");
  const bookIO = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (en.isIntersecting) tocLinks.forEach(a => a.classList.toggle("active", a.getAttribute("href") === "#" + en.target.id));
    });
  }, { rootMargin: "-40% 0px -55% 0px" });
  $$(".book").forEach(b => bookIO.observe(b));

  const tabs = $$(".tabs button"), panels = $$(".tab-panel");
  tabs.forEach(t => t.addEventListener("click", () => {
    tabs.forEach(x => x.setAttribute("aria-selected", x === t));
    panels.forEach((p, i) => p.hidden = String(i) !== t.dataset.tab);
  }));

  /* ---------------- Altar anatomy: link list rows and cross cells ---------------- */
  const cellEls = $$("[data-cell]");
  const lightCell = n => cellEls.forEach(el => el.classList.toggle("on", el.dataset.cell === n));
  cellEls.forEach(el => {
    el.addEventListener("pointerenter", () => lightCell(el.dataset.cell));
    el.addEventListener("focus", () => lightCell(el.dataset.cell));
    el.addEventListener("pointerleave", () => lightCell(null));
    el.addEventListener("blur", () => lightCell(null));
  });
  // clicking a cell on the map brings its description into view
  $$(".cell").forEach(c => c.addEventListener("click", () => {
    $(`.cell-row[data-cell="${c.dataset.cell}"]`)?.scrollIntoView({ behavior: "smooth", block: "center" });
    lightCell(c.dataset.cell);
  }));

  /* ---------------- Join: fake baptism (nothing stored or sent) ---------------- */
  const form = $("#joinForm"), cert = $("#certificate");
  form.addEventListener("submit", e => {
    e.preventDefault();
    const name = form.name.value.trim();
    if (!name || !form.agree.checked) { form.classList.add("err"); form.name.focus(); return; }
    form.classList.remove("err");
    const no = String(Math.floor(Math.random() * 99) + 1).padStart(6, "0");
    $("#certName").textContent = name;
    $("#certNo").textContent = "No. " + no;
    $("#certVow").textContent = `I entrust ${form.vow.value}.`;
    $("#certTime").textContent = new Date().toLocaleString("sv-SE").slice(0, 16).replace("-", ".").replace("-", ".");
    form.hidden = true; cert.hidden = false;
    cert.scrollIntoView({ behavior: "smooth", block: "center" });
  });
  $("#again").addEventListener("click", () => { form.reset(); cert.hidden = true; form.hidden = false; });

  /* ---------------- Cursor halo over links ---------------- */
  const halo = $(".cursor-halo");
  let hx = 0, hy = 0;
  document.addEventListener("pointermove", e => {
    hx = e.clientX; hy = e.clientY;
    halo.style.transform = `translate(${hx}px, ${hy}px)`;
    halo.classList.toggle("on", !!e.target.closest("a, button, .creed li, label"));
  }, { passive: true });
  document.addEventListener("pointerleave", () => halo.classList.remove("on"));

  document.getElementById(location.hash.replace(/^#\/?/, ""))?.scrollIntoView();
})();
