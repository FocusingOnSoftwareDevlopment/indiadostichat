/*
  IndiaDostiChat Website Configuration
  Change only this file when needed.
*/
window.SITE_CONFIG = {
  siteName: "IndiaDostiChat",
  tagline: "India’s friendly IRC chat community",
  channelName: "IndiaDostiChat",

  // KiwiIRC opens inside your website using this embedded iframe URL.
  kiwiEmbedUrl: "https://kiwiirc.hybridirc.com/#IndiaDostiChat",

  // Logo path. Put your logo inside assets/logo/ and keep this filename.
  logoPath: "assets/logo/logo.png",

  // Captcha options:
  // For GitHub Pages, Google reCAPTCHA usually needs backend verification.
  // Cloudflare Turnstile is easier for static sites.
  // 1) Create free Turnstile site key from Cloudflare
  // 2) Replace this value
  // 3) Set captchaEnabled: true
  captchaEnabled: false,
  turnstileSiteKey: "PASTE_YOUR_CLOUDFLARE_TURNSTILE_SITE_KEY_HERE",

  // Simple fallback gate when captchaEnabled is false.
  fallbackQuestion: "Type CHAT to enter",
  fallbackAnswer: "CHAT"
};
