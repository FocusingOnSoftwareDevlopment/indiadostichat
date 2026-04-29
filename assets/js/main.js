
(function () {
  const cfg = window.SITE_CONFIG || {};

  document.querySelectorAll("[data-site-name]").forEach(el => {
    el.textContent = cfg.siteName || "IndiaDostiChat";
  });

  document.querySelectorAll("[data-tagline]").forEach(el => {
    el.textContent = cfg.tagline || "India’s friendly IRC chat community";
  });

  document.querySelectorAll("[data-logo]").forEach(img => {
    img.src = cfg.logoPath || "assets/logo/logo.png";
  });

  const year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();

  const menuBtn = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".nav");
  if (menuBtn && nav) {
    menuBtn.addEventListener("click", () => nav.classList.toggle("open"));
  }
})();
