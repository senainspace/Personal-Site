document.addEventListener("DOMContentLoaded", () => {
  // ---------------------------
  // 1) TR/EN toggle
  // ---------------------------
  const translations = {
    tr: {
      nav_home: "Ana Sayfa",
      nav_about: "Hakkımda",
      nav_education: "Eğitim",
      nav_experience: "Deneyim",
      nav_projects: "Projeler",
      nav_competitions: "Yarışmalar",
      nav_clubs: "Kulüpler ve Topluluklar",
      nav_contact: "İletişim",

      education_title: "Eğitim",
      experience_title: "Deneyim",
      proj_title: "Projeler",
      competitions_title: "Yarışmalar",
      communities_title: "Kulüpler ve Topluluklar",
      contact_title: "İletişim",

      home_hello: "Merhaba, Ben",
      home_sub: "Bilgisayar Mühendisliği öğrencisi · Computer Vision · Algorithms · Autonomous Systems",
      home_desc:
        "Bilgisayarlı görü, algoritmalar ve otonom sistemler üzerine odaklanıyorum. Gerçek dünya problemleri için veri odaklı, sağlam ve iteratif çözümler üretmeyi seviyorum.",
      about_title: "Hakkımda",
      about_text:
        "İzmir’de Bilgisayar Mühendisliği öğrencisiyim. Algoritmalar, veri yapıları ve bilgisayarlı görü alanlarında projeler geliştiriyorum. Özellikle gerçek dünya uygulamalarında model geliştirme, veri hazırlama ve sistem tasarımı süreçlerine ilgi duyuyorum.",
      contact_text: "Bana ulaşmak için e-posta gönderebilir veya LinkedIn’den yazabilirsin.",
    },
    en: {
      nav_home: "Home",
      nav_about: "About",
      nav_education: "Education",
      nav_experience: "Experience",
      nav_projects: "Projects",
      nav_competitions: "Competitions",
      nav_clubs: "Clubs & Communities",
      nav_contact: "Contact",

      education_title: "Education",
      experience_title: "Experience",
      proj_title: "Projects",
      competitions_title: "Competitions",
      communities_title: "Clubs & Communities",
      contact_title: "Contact",

      home_hello: "Hi, I’m",
      home_sub: "Computer Engineering student · Computer Vision · Algorithms · Autonomous Systems",
      home_desc:
        "I focus on computer vision, algorithms, and autonomous systems. I enjoy building data-driven, robust, iterative solutions for real-world engineering problems.",
      about_title: "About",
      about_text:
        "I’m a Computer Engineering student in Izmir. I build projects in algorithms, data structures, and computer vision. I’m especially interested in model development, dataset preparation, and system design for real-world applications.",
      contact_text: "Feel free to email me or reach out via LinkedIn.",
    },
  };

  let currentLang = "tr";
  const btn = document.getElementById("langToggle");

  function applyLang(lang) {
    document.querySelectorAll("[data-i18n]").forEach((el) => {
      const key = el.getAttribute("data-i18n");
      if (translations[lang] && translations[lang][key]) {
        el.textContent = translations[lang][key];
      }
    });
    if (btn) btn.textContent = lang === "tr" ? "EN" : "TR";
    currentLang = lang;
  }

  if (btn) {
    btn.addEventListener("click", () => applyLang(currentLang === "tr" ? "en" : "tr"));
  }
  applyLang("tr");

  // ---------------------------
  // 2) Navbar active link (scroll)
  // ---------------------------
  const sections = [
    "home",
    "about",
    "education",
    "experience",
    "projects",
    "competitions",
    "communities",
    "contact",
  ]
    .map((id) => document.getElementById(id))
    .filter(Boolean);

  const navLinks = Array.from(document.querySelectorAll(".nav-links a"));

  function setActiveLink() {
    const scrollY = window.scrollY + 120;
    let currentId = "home";

    for (const sec of sections) {
      if (sec.offsetTop <= scrollY) currentId = sec.id;
    }

    navLinks.forEach((a) => {
      const href = a.getAttribute("href") || "";
      a.classList.toggle("active", href === `#${currentId}`);
    });
  }

  window.addEventListener("scroll", setActiveLink);
  setActiveLink();

  // ---------------------------
  // helpers
  // ---------------------------
  function splitPipe(s) {
    if (!s) return [];
    return s.split("||").map((x) => x.trim()).filter(Boolean);
  }

  // ---------------------------
  // 3) Competition Modal (show)
  // ---------------------------
  (function setupCompetitionModal() {
    const backdrop = document.getElementById("compModal");
    if (!backdrop) return;

    const closeBtn = backdrop.querySelector(".modal-close");

    const titleEl = document.getElementById("compModalTitle");
    const metaEl = document.getElementById("compModalMeta");
    const badgeEl = document.getElementById("compModalBadge");
    const descEl = document.getElementById("compModalDesc");

    const logoEl = document.getElementById("compModalLogo");
    const imgWrap = document.getElementById("compModalImageWrap");
    const imgEl = document.getElementById("compModalImage");

    const hiWrap = document.getElementById("compModalHighlightsWrap");
    const hiEl = document.getElementById("compModalHighlights");

    const memWrap = document.getElementById("compModalMembersWrap");
    const memEl = document.getElementById("compModalMembers");

    const linkEl = document.getElementById("compModalLink");

    function openModalFromCard(card) {
      const t = card.dataset.title || "";
      const organizer = card.dataset.organizer || "";
      const date = card.dataset.date || "";
      const award = card.dataset.award || "";
      const team = card.dataset.team || "";
      const role = card.dataset.role || "";
      const desc = card.dataset.desc || "";
      const highlights = splitPipe(card.dataset.highlights || "");
      const members = splitPipe(card.dataset.members || "");
      const url = card.dataset.url || "";
      const logo = card.dataset.logo || "";
      const img = card.dataset.img || "";

      if (titleEl) titleEl.textContent = t;

      const metaBits = [];
      if (organizer) metaBits.push(organizer);
      if (date) metaBits.push(date);
      if (role) metaBits.push("Role: " + role);
      if (team) metaBits.push("Team: " + team);
      if (metaEl) metaEl.textContent = metaBits.join(" • ");

      if (badgeEl) {
        if (award) {
          badgeEl.style.display = "inline-flex";
          badgeEl.textContent = award;
        } else {
          badgeEl.style.display = "none";
        }
      }

      if (descEl) descEl.textContent = desc;

      if (hiEl) hiEl.innerHTML = "";
      if (hiWrap) {
        if (highlights.length && hiEl) {
          hiWrap.style.display = "block";
          highlights.forEach((h) => {
            const li = document.createElement("li");
            li.textContent = h;
            hiEl.appendChild(li);
          });
        } else {
          hiWrap.style.display = "none";
        }
      }

      if (memEl) memEl.innerHTML = "";
      if (memWrap) {
        if (members.length && memEl) {
          memWrap.style.display = "block";
          members.forEach((m) => {
            const li = document.createElement("li");
            li.textContent = m;
            memEl.appendChild(li);
          });
        } else {
          memWrap.style.display = "none";
        }
      }

      if (logoEl) {
        if (logo) {
          logoEl.src = logo;
          logoEl.style.display = "block";
        } else {
          logoEl.style.display = "none";
        }
      }

      if (imgWrap && imgEl) {
        if (img) {
          imgEl.src = img;
          imgWrap.style.display = "block";
        } else {
          imgWrap.style.display = "none";
        }
      }

      if (linkEl) {
        if (url) {
          linkEl.href = url;
          linkEl.style.display = "inline-block";
        } else {
          linkEl.style.display = "none";
        }
      }

      backdrop.classList.add("show");
      backdrop.setAttribute("aria-hidden", "false");
      document.body.style.overflow = "hidden";
    }

    function closeModal() {
      backdrop.classList.remove("show");
      backdrop.setAttribute("aria-hidden", "true");
      document.body.style.overflow = "";
    }

    document.addEventListener("click", (e) => {
      const card = e.target.closest('[data-modal="competition"]');
      if (card) openModalFromCard(card);

      if (e.target === backdrop) closeModal();
    });

    if (closeBtn) closeBtn.addEventListener("click", closeModal);

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") closeModal();
    });
  })();

  // ===============================
  // Project Modal (safe + minimal)
  // ===============================
  (function setupProjectModal() {
    const backdrop = document.getElementById("projectModal");
    if (!backdrop) return;

    const modalCloseBtn = backdrop.querySelector(".modal-close");

    const pmImage = backdrop.querySelector("#pmImage");
    const pmTitle = backdrop.querySelector("#pmTitle");
    const pmMeta = backdrop.querySelector("#pmMeta");
    const pmBadge = backdrop.querySelector("#pmBadge");
    const pmDesc = backdrop.querySelector("#pmDesc");

    const pmTagsWrap = backdrop.querySelector("#pmTagsWrap");
    const pmTags = backdrop.querySelector("#pmTags");

    const pmGallery = backdrop.querySelector("#pmGallery");
    const pmView = backdrop.querySelector("#pmView");

    function openModal() {
      backdrop.classList.add("show");
      backdrop.setAttribute("aria-hidden", "false");
      document.body.classList.add("modal-open");
    }

    function closeModal() {
      backdrop.classList.remove("show");
      backdrop.setAttribute("aria-hidden", "true");
      document.body.classList.remove("modal-open");
    }

    function setLink(el, url) {
      if (!el) return;
      const u = (url || "").trim();
      if (!u) {
        el.style.display = "none";
        el.setAttribute("href", "#");
        return;
      }
      el.style.display = "inline-flex";
      el.setAttribute("href", u);
    }

    function fillTags(raw) {
      if (!pmTagsWrap || !pmTags) return;

      const text = (raw || "").trim();
      pmTags.innerHTML = "";

      if (!text) {
        pmTagsWrap.style.display = "none";
        return;
      }

      const parts = text.split("||").map((s) => s.trim()).filter(Boolean);
      parts.forEach((t) => {
        const span = document.createElement("span");
        span.className = "tag";
        span.textContent = t;
        pmTags.appendChild(span);
      });

      pmTagsWrap.style.display = parts.length ? "block" : "none";
    }

    function fillGallery(raw) {
      if (!pmGallery) return;

      pmGallery.innerHTML = "";
      const text = (raw || "").trim();

      if (!text) {
        pmGallery.style.display = "none";
        return;
      }

      const urls = text.split("||").map((s) => s.trim()).filter(Boolean);

      urls.forEach((u) => {
        const img = document.createElement("img");
        img.src = u;
        img.alt = "Project image";
        img.loading = "lazy";
        pmGallery.appendChild(img);
      });

      pmGallery.style.display = urls.length ? "flex" : "none";
    }

    function fillFromCard(card) {
      if (!card) return;

      const title = card.dataset.title || "";
      const role = card.dataset.role || "";
      const period = card.dataset.period || "";
      const desc = card.dataset.desc || "";
      const tags = card.dataset.tags || "";
      const github = card.dataset.github || "";
      const demo = card.dataset.demo || "";
      const featured = card.dataset.featured === "1";

      const image = card.dataset.image || "";
      const imagesRaw = card.dataset.images || "";

      if (pmTitle) pmTitle.textContent = title;
      if (pmDesc) pmDesc.textContent = desc;

      const metaParts = [];
      if (role) metaParts.push(role);
      if (period) metaParts.push(period);
      if (pmMeta) pmMeta.textContent = metaParts.join(" • ");

      if (pmBadge) pmBadge.style.display = featured ? "inline-flex" : "none";

      if (pmImage) {
        if (image) {
          pmImage.src = image;
          pmImage.alt = title ? title : "";
          pmImage.style.display = "block";
        } else {
          pmImage.removeAttribute("src");
          pmImage.alt = "";
          pmImage.style.display = "none";
        }
      }

      fillTags(tags);
      fillGallery(imagesRaw);

      const viewUrl = (demo && demo.trim()) ? demo : ((github && github.trim()) ? github : "");
      setLink(pmView, viewUrl);
    }

    // Open on card click (event delegation)
    document.addEventListener("click", function (e) {
      const card = e.target.closest(".project-card");
      if (!card) return;
      fillFromCard(card);
      openModal();
    });

    // Close: X
    if (modalCloseBtn) modalCloseBtn.addEventListener("click", closeModal);

    // Close: click backdrop
    backdrop.addEventListener("click", function (e) {
      if (e.target === backdrop) closeModal();
    });

    // Close: ESC (only when open)
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && backdrop.classList.contains("show")) {
        closeModal();
      }
    });

    // Keyboard open (Enter/Space when focused)
    document.addEventListener("keydown", function (e) {
      const active = document.activeElement;
      if (!active || !active.classList || !active.classList.contains("project-card")) return;

      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        fillFromCard(active);
        openModal();
      }
    });
  })();
});
