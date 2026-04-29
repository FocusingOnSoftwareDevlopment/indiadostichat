# IndiaDostiChat GitHub Pages Website

## What this package includes

- `index.html` landing page
- `chat.html` with same-site KiwiIRC embed
- `rules.html`
- `about.html`
- `blog.html`
- `contact.html`
- `assets/logo/` folder for logo
- `config.js` for simple future changes
- Bot/security gate before chat opens

## Upload process to GitHub

1. Download and unzip this package.
2. Open the extracted folder.
3. Put your real logo here:

   `assets/logo/logo.png`

   Keep the filename exactly:

   `logo.png`

4. Go to your GitHub repo:

   `FocusingOnSoftwareDevlopment/indiadostichat`

5. Upload all files and folders from this package into the repo root.
6. Replace old files when GitHub asks.
7. Commit changes.
8. Wait 2-5 minutes for GitHub Pages to update.
9. Open:

   `https://www.indiadostichat.com/`

## Important about captcha

GitHub Pages is static hosting. Full Google reCAPTCHA verification usually needs a backend server.

This package uses two options:

### Option A: No setup fallback
Currently enabled by default.

Users must type `CHAT` before the chat opens.

### Option B: Cloudflare Turnstile captcha
For stronger captcha:

1. Create a free Cloudflare Turnstile site key.
2. Open `config.js`.
3. Change:

   `captchaEnabled: false`

   to:

   `captchaEnabled: true`

4. Paste your Turnstile site key here:

   `turnstileSiteKey: "PASTE_YOUR_CLOUDFLARE_TURNSTILE_SITE_KEY_HERE"`

5. Upload only `config.js` again.

## Change channel link later

Open `config.js` and edit:

`kiwiEmbedUrl: "https://kiwiirc.hybridirc.com/#IndiaDostiChat"`

## Logo location

Your logo folder is:

`assets/logo/`

Your main logo file should be:

`assets/logo/logo.png`
