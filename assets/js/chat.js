(function () {
  const cfg = window.SITE_CONFIG || {};
  const captchaBox = document.getElementById("captchaBox");
  const chatBox = document.getElementById("chatBox");
  const kiwiFrame = document.getElementById("kiwiFrame");

  window.onCaptchaSuccess = function(token) {
    console.log("reCAPTCHA verified");
    if (kiwiFrame && !kiwiFrame.src) {
      kiwiFrame.src = cfg.kiwiEmbedUrl || "https://kiwiirc.hybridirc.com/#indiadostichat";
    }
    
    // Hide captcha, show chat
    captchaBox.style.display = "none";
    chatBox.classList.remove("hidden");
    
    // Add fullscreen class dynamically
    document.body.classList.add("chat-active");
  };
})();
