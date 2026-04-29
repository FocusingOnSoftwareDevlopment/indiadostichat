
(function () {
  const cfg = window.SITE_CONFIG || {};
  const captchaBox = document.getElementById("captchaBox");
  const chatBox = document.getElementById("chatBox");
  const kiwiFrame = document.getElementById("kiwiFrame");
  const fallbackCaptcha = document.getElementById("fallbackCaptcha");
  const fallbackLabel = document.getElementById("fallbackLabel");
  const fallbackInput = document.getElementById("fallbackInput");
  const fallbackVerify = document.getElementById("fallbackVerify");
  const captchaError = document.getElementById("captchaError");
  const turnstileContainer = document.getElementById("turnstileContainer");

  function showChat() {
    if (kiwiFrame && !kiwiFrame.src) {
      kiwiFrame.src = cfg.kiwiEmbedUrl || "https://kiwiirc.hybridirc.com/#IndiaDostiChat";
    }
    captchaBox.classList.add("hidden");
    chatBox.classList.remove("hidden");
  }

  function setupFallback() {
    if (!fallbackCaptcha) return;
    fallbackCaptcha.classList.remove("hidden");
    const question = cfg.fallbackQuestion || "Type CHAT to enter";
    const answer = (cfg.fallbackAnswer || "CHAT").toLowerCase().trim();
    fallbackLabel.textContent = question;

    fallbackVerify.addEventListener("click", () => {
      const value = (fallbackInput.value || "").toLowerCase().trim();
      if (value === answer) {
        showChat();
      } else {
        captchaError.textContent = "Wrong answer. Please try again.";
      }
    });

    fallbackInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter") fallbackVerify.click();
    });
  }

  if (cfg.captchaEnabled && cfg.turnstileSiteKey && cfg.turnstileSiteKey.indexOf("PASTE_") === -1) {
    fallbackCaptcha.classList.add("hidden");

    const waitForTurnstile = setInterval(() => {
      if (window.turnstile) {
        clearInterval(waitForTurnstile);
        window.turnstile.render(turnstileContainer, {
          sitekey: cfg.turnstileSiteKey,
          callback: function () {
            showChat();
          }
        });
      }
    }, 300);
  } else {
    setupFallback();
  }
})();
