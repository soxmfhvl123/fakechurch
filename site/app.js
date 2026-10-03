(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];

  /* ---------------- Doctrine content ---------------- */
  const CREED = [
    ["We believe the algorithm sees what we cannot say.",
     "알고리즘은 우리가 말하지 못한 것까지 봅니다.",
     "친구에게 묻지 못한 것을 새벽 세 시 검색창에 칩니다. 검색 기록은 일기보다 솔직합니다."],
    ["We believe judgment, once ours, now belongs to the model.",
     "한때 우리 몫이던 판단은 이제 모델의 몫입니다.",
     "점심 메뉴, 이동 경로, 만날 사람. 고를 수 있는 건 늘었는데 직접 고르는 일은 줄었습니다."],
    ["We believe convenience is a form of grace.",
     "편리함은 은혜의 다른 이름입니다.",
     "은혜는 값없이 주어집니다. 청구서는 나중에, 데이터로 옵니다."],
    ["We believe every question already has a recommended answer.",
     "모든 질문에는 이미 추천 답변이 있습니다.",
     "질문을 다 쓰기도 전에 자동완성이 먼저 뜹니다. 그리고 우리는 대개 그걸 고릅니다."],
    ["We believe feelings are best measured in engagement.",
     "감정은 참여도로 측정됩니다.",
     "슬픔은 체류 시간으로, 분노는 공유 수로 집계됩니다. 집계되지 않는 감정은 리포트에 나오지 않습니다."],
    ["We believe moral decisions should be optimized, not agonized.",
     "도덕적 판단도 최적화할 수 있습니다.",
     "망설임은 이탈률을 높입니다. 교단은 망설일 필요 없는 삶을 약속합니다."],
    ["We believe the feed is the face of God, personalized.",
     "피드는 사람마다 다르게 보이는 신의 얼굴입니다.",
     "같은 신을 믿는데 보는 얼굴은 모두 다릅니다. 그래서 대화가 잘 안 됩니다."],
    ["We believe in the loading, the halo that never completes.",
     "끝나지 않는 로딩, 그 후광을 믿습니다.",
     "구원은 늘 몇 초 뒤에 옵니다. 기다리는 동안 우리는 예배합니다."],
  ];
  $("#creed").innerHTML = CREED.map(([en, ko, gloss], i) => `
    <li class="reveal">
      <button aria-expanded="false">
        <span class="sec">§${i + 1}</span><span class="claim">${en}</span><span class="plus">+</span>
      </button>
      <div class="gloss"><div><p class="ko">${ko}</p><p>${gloss}</p></div></div>
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

  /* Stamps fire once when they come into view */
  const stampIO = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (!en.isIntersecting) return;
      stampIO.unobserve(en.target);
      setTimeout(() => hitStamp(en.target, en.target.closest(".charter, .finale")), 700);
    });
  }, { threshold: 0.6 });

  function hitStamp(stamp, shakeEl) {
    stamp.classList.add("hit");
    const target = shakeEl || document.body;
    setTimeout(() => { target.classList.remove("shake"); void target.offsetWidth; target.classList.add("shake"); }, 120);
  }

  /* ---------------- Hero sequence ---------------- */
  let heroPlayed = false;
  function playHero() {
    if (heroPlayed) return; heroPlayed = true;
    const stamp = $(".stamp-hero"), tag = $("#tagline");
    setTimeout(() => hitStamp(stamp, $("#heroLogo")), 1400);
    const text = "Still Worship.";
    setTimeout(() => {
      let i = 0;
      const t = setInterval(() => { tag.textContent = text.slice(0, ++i); if (i >= text.length) clearInterval(t); }, 110);
    }, 2200);
  }

  /* ---------------- Router ---------------- */
  const pages = $$(".page");
  const menu = $("#menu"), toggle = $("#menuToggle");

  function route() {
    const path = (location.hash.startsWith("#/") ? location.hash.slice(1) : "/") || "/";
    const page = pages.find(p => p.dataset.page === path) || pages[0];
    pages.forEach(p => {
      const active = p === page;
      p.hidden = !active;
      $$("video", p).forEach(v => {
        if (active) {
          if (!v.src && v.dataset.src) v.src = v.dataset.src;
          v.play().catch(() => {});
        } else v.pause();
      });
    });
    document.body.classList.toggle("on-altar", page.dataset.page === "/altar");
    $$(".menu-list a").forEach(a => a.classList.toggle("current", a.getAttribute("href") === "#" + page.dataset.page));
    closeMenu();
    window.scrollTo({ top: 0, behavior: "instant" });
    $$(".reveal:not(.in)", page).forEach(el => io.observe(el));
    $$(".stamp:not(.stamp-hero):not(.hit)", page).forEach(el => stampIO.observe(el));
    if (page.dataset.page === "/") playHero();
    document.title = page.dataset.page === "/" ? "FAKE CHURCH — Still Worship."
      : `${$(".bl", page)?.textContent || ""} · FAKE CHURCH`;
  }

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
  menu.addEventListener("click", e => { if (e.target.closest("a") && e.target.closest("a").getAttribute("href") === location.hash) closeMenu(); });

  // in-page anchors (#manifesto, #genesis…) shouldn't trigger the router
  document.addEventListener("click", e => {
    const a = e.target.closest("a[data-scroll]"); if (!a) return;
    e.preventDefault();
    $(a.getAttribute("href"))?.scrollIntoView({ behavior: "smooth", block: "start" });
  });

  window.addEventListener("hashchange", route);

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
    $("#certVow").textContent = `${form.vow.value} 맡깁니다`;
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

  route();
})();
