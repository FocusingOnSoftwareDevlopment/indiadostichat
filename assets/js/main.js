/**
 * IndiaDostiChat Main JS
 * Version: 9.0
 */

// 1. Initial Theme Application (Fastest execution)
(function() {
    let savedTheme = null;
    try {
        savedTheme = localStorage.getItem("theme");
    } catch (e) {}

    // Check URL parameters for theme override
    const urlParams = new URLSearchParams(window.location.search);
    const themeParam = urlParams.get('theme') || urlParams.get('dark');
    
    let isDark = false;
    if (themeParam === 'dark' || themeParam === '1' || themeParam === 'true') {
        isDark = true;
    } else if (themeParam === 'light' || themeParam === '0' || themeParam === 'false') {
        isDark = false;
    } else {
        const systemPrefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
        isDark = (savedTheme === "dark") || (!savedTheme && systemPrefersDark);
    }
    
    if (isDark) {
        document.documentElement.classList.add("dark-mode");
        if (document.body) {
            document.body.classList.add("dark-mode");
        } else {
            document.addEventListener('DOMContentLoaded', () => {
                document.body.classList.add("dark-mode");
            });
        }
    } else {
        document.documentElement.classList.remove("dark-mode");
        if (document.body) {
            document.body.classList.remove("dark-mode");
        } else {
            document.addEventListener('DOMContentLoaded', () => {
                document.body.classList.remove("dark-mode");
            });
        }
    }
})();

document.addEventListener('DOMContentLoaded', () => {
    const pathLower = window.location.pathname.toLowerCase();
    const isChatPage = pathLower.includes('/chat/') || 
                       pathLower.endsWith('/chat') || 
                       pathLower.endsWith('/chat.html') || 
                       pathLower.endsWith('/chat/index.html');

    // --- 1. Theme Toggle (Dark Mode) ---
    const themeToggle = document.getElementById("theme-toggle");
    const themeIcon = themeToggle ? themeToggle.querySelector(".theme-icon") : null;

    function updateToggleUI(isDark) {
        if (themeIcon) {
            themeIcon.textContent = isDark ? "☀️" : "🌙";
        }
        if (themeToggle) {
            const label = isDark ? "Switch to light mode" : "Switch to dark mode";
            themeToggle.setAttribute("aria-label", label);
            themeToggle.setAttribute("title", label);
        }
    }

    // Update UI on load
    updateToggleUI(document.body.classList.contains("dark-mode"));

    if (themeToggle) {
        themeToggle.onclick = function(e) {
            e.preventDefault();
            const isDark = document.body.classList.toggle("dark-mode");
            document.documentElement.classList.toggle("dark-mode", isDark);
            const newTheme = isDark ? "dark" : "light";
            try {
                localStorage.setItem("theme", newTheme);
            } catch (err) {}
            updateToggleUI(isDark);
        };
    }

    // --- 2. Navigation & Mobile Menu ---
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');

    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.onclick = function() {
            navLinks.classList.toggle('active');
            mobileMenuBtn.classList.toggle('active');
        };
    }

    // Set active link in navigation
    const path = location.pathname.replace(/\/index\.html$/, '/');
    const navItems = document.querySelectorAll('.nav-links a');
    navItems.forEach(item => {
        try {
            const itemPath = new URL(item.href, window.location.origin).pathname.replace(/\/index\.html$/, '/');
            if (itemPath === path) {
                item.style.color = 'var(--primary-color)';
                item.classList.add('active');
            }
        } catch (e) {
            // Ignore
        }
    });

    // --- 3. Visitor Counter & Chat Entry Counter ---
    const visitorCountEls = document.querySelectorAll('#visitor-count');
    const joinCountEls = document.querySelectorAll('#join-count');

    // Function to update join count elements
    function updateJoinUI(count) {
        const formattedCount = Number(count).toLocaleString();
        joinCountEls.forEach(el => el.innerText = formattedCount);
    }

    // Function to handle join chat increment safely
    function incrementJoinChat() {
        let isJoined = false;
        try {
            isJoined = localStorage.getItem(joinKey) === 'true';
        } catch (e) {}

        if (!isJoined) {
            try {
                localStorage.setItem(joinKey, 'true');
            } catch (e) {}
            return fetch('https://api.counterapi.dev/v1/indiadostichat_main/join_chat/up')
                .then(res => res.json())
                .then(data => {
                    if (data && typeof data.count !== 'undefined') {
                        updateJoinUI(data.count);
                    }
                })
                .catch(err => console.warn("Error incrementing join count:", err));
        }
        return Promise.resolve();
    }

    // Delay Counter API initialization by 3 seconds to keep it off the critical path
    let visitKey = '';
    let joinKey = '';
    
    setTimeout(() => {
        // Get today's local date string (YYYY-MM-DD)
        const today = new Date();
        const dateStr = today.getFullYear() + '-' + 
                        String(today.getMonth() + 1).padStart(2, '0') + '-' + 
                        String(today.getDate()).padStart(2, '0');

        // Clean up older local storage keys
        try {
            for (let i = localStorage.length - 1; i >= 0; i--) {
                const key = localStorage.key(i);
                if (key) {
                    if ((key.startsWith('idc_visit_counted_') && key !== 'idc_visit_counted_' + dateStr) ||
                        (key.startsWith('idc_join_counted_') && key !== 'idc_join_counted_' + dateStr)) {
                        localStorage.removeItem(key);
                    }
                }
            }
        } catch (e) {
            console.warn("Storage cleanup failed:", e);
        }

        visitKey = 'idc_visit_counted_' + dateStr;
        joinKey = 'idc_join_counted_' + dateStr;

        // 3a. Community Visits (Visitor Counter) logic
        if (visitorCountEls.length > 0) {
            let isVisited = false;
            try {
                isVisited = localStorage.getItem(visitKey) === 'true';
            } catch (e) {}

            const visitorApiUrl = isVisited 
                ? 'https://api.counterapi.dev/v1/indiadostichat_main/visitors'
                : 'https://api.counterapi.dev/v1/indiadostichat_main/visitors/up';

            fetch(visitorApiUrl)
                .then(res => res.json())
                .then(data => {
                    if (data && typeof data.count !== 'undefined') {
                        const formattedCount = Number(data.count).toLocaleString();
                        visitorCountEls.forEach(el => el.innerText = formattedCount);
                        if (!isVisited) {
                            try {
                                localStorage.setItem(visitKey, 'true');
                            } catch (e) {}
                        }
                    } else {
                        visitorCountEls.forEach(el => el.innerText = '—');
                    }
                })
                .catch(() => {
                    visitorCountEls.forEach(el => el.innerText = '—');
                });
        }

        // 3b. Join Chat Counter logic
        if (joinCountEls.length > 0) {
            fetch('https://api.counterapi.dev/v1/indiadostichat_main/join_chat')
                .then(res => res.json())
                .then(data => {
                    if (data && typeof data.count !== 'undefined') {
                        updateJoinUI(data.count);
                    } else {
                        joinCountEls.forEach(el => el.innerText = '—');
                    }
                })
                .catch(() => {
                    joinCountEls.forEach(el => el.innerText = '—');
                });
        }

        if (isChatPage) {
            incrementJoinChat();
        }

        // Attach click listeners to Join Chat links/buttons on other pages
        document.addEventListener('click', (e) => {
            let targetEl = e.target;
            while (targetEl && targetEl !== document.body) {
                if (targetEl.tagName === 'A' && targetEl.href) {
                    try {
                        const url = new URL(targetEl.href, window.location.origin);
                        const hrefPath = url.pathname.toLowerCase();
                        if (hrefPath.includes('/chat/') || 
                            hrefPath.endsWith('/chat') || 
                            hrefPath.endsWith('/chat.html') || 
                            hrefPath.endsWith('/chat/index.html')) {
                            incrementJoinChat();
                            break;
                        }
                    } catch (err) {}
                }
                targetEl = targetEl.parentElement;
            }
        });
    }, 3000);

    // --- 4. Landing Page Rotating Backgrounds ---
    const landingHeroes = document.querySelectorAll('.landing-hero');
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (!prefersReducedMotion && landingHeroes.length > 0) {
        landingHeroes.forEach(hero => {
            const bgAttr = hero.getAttribute('data-bg-images');
            if (bgAttr) {
                const images = bgAttr.split(',').map(s => s.trim()).filter(s => s.length > 0);
                if (images.length > 1) {
                    let idx = 0;
                    setInterval(() => {
                        idx = (idx + 1) % images.length;
                        hero.style.setProperty('--landing-bg-image', `url('${images[idx]}')`);
                    }, 8000);
                }
            }
        });
    }

    // --- 4b. Homepage Hero Rotating Backgrounds ---
    const heroBgLayers = document.querySelectorAll('.hero-bg-layer');
    const locationLabel = document.querySelector('.hero-location-text');
    
    if (heroBgLayers.length > 0) {
        const heroImages = [
            { name: "mumbai-gateway", label: "Mumbai", loaded: true },
            { name: "delhi-india-gate", label: "Delhi", loaded: false },
            { name: "hyderabad-charminar", label: "Hyderabad", loaded: false },
            { name: "jaipur-hawa-mahal", label: "Jaipur", loaded: false },
            { name: "kerala-backwaters", label: "Kerala", loaded: false },
            { name: "kashmir-mountains", label: "Kashmir", loaded: false },
            { name: "varanasi-ghats", label: "Varanasi", loaded: false },
            { name: "goa-beach", label: "Goa", loaded: false },
            { name: "india-festival-lights", label: "India", loaded: false }
        ];

        const isMobile = window.innerWidth <= 768;
        function getHeroSrc(name) {
            if (isMobile) {
                return `/assets/images/home-hero/mobile/${name}-mobile.webp`;
            }
            return `/assets/images/home-hero/${name}.webp`;
        }

        let currentImgIdx = 0;
        let activeLayerIdx = 0;

        // Lazy load rotating images one by one after window load (lazy queue)
        window.addEventListener('load', () => {
            const loadNextImage = (idx) => {
                if (idx >= heroImages.length) return;
                const img = new Image();
                img.onload = () => {
                    heroImages[idx].loaded = true;
                    setTimeout(() => loadNextImage(idx + 1), 2000);
                };
                img.onerror = () => {
                    setTimeout(() => loadNextImage(idx + 1), 2000);
                };
                img.src = getHeroSrc(heroImages[idx].name);
            };
            
            // Start queue after 4 seconds
            setTimeout(() => loadNextImage(1), 4000);
        });

        if (!prefersReducedMotion && heroBgLayers.length >= 2) {
            setInterval(() => {
                const nextImgIdx = (currentImgIdx + 1) % heroImages.length;
                
                // Do not switch or request image if it hasn't loaded yet
                if (nextImgIdx !== 0 && !heroImages[nextImgIdx].loaded) {
                    return;
                }
                
                const nextLayerIdx = 1 - activeLayerIdx;
                const activeLayer = heroBgLayers[activeLayerIdx];
                const inactiveLayer = heroBgLayers[nextLayerIdx];

                // Set image on the inactive layer
                inactiveLayer.style.backgroundImage = `url('${getHeroSrc(heroImages[nextImgIdx].name)}')`;
                
                // Add active to inactive layer, remove from active
                inactiveLayer.classList.add('active');
                activeLayer.classList.remove('active');

                // Update location label
                if (locationLabel) {
                    locationLabel.style.opacity = '0';
                    setTimeout(() => {
                        locationLabel.textContent = heroImages[nextImgIdx].label;
                        locationLabel.style.opacity = '1';
                    }, 400);
                }

                currentImgIdx = nextImgIdx;
                activeLayerIdx = nextLayerIdx;
            }, 6000);
        }
    }

    // --- 5. Back to Top / Scroll Down Buttons ---
    if (!isChatPage) {
        const backToTopBtn = document.createElement('button');
        backToTopBtn.className = 'back-to-top';
        backToTopBtn.innerHTML = '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" style="width: 24px; height: 24px; display: block; margin: auto;"><line x1="12" y1="19" x2="12" y2="5"></line><polyline points="5 12 12 5 19 12"></polyline></svg>';
        backToTopBtn.setAttribute('aria-label', 'Back to top');
        document.body.appendChild(backToTopBtn);

        let scrollTicking = false;
        let lastScrollY = 0;
        const updateScrollBtn = () => {
            // Read layout property synchronously outside requestAnimationFrame
            lastScrollY = window.scrollY;
            if (!scrollTicking) {
                scrollTicking = true;
                window.requestAnimationFrame(() => {
                    if (lastScrollY > 300) {
                        backToTopBtn.classList.add('visible');
                    } else {
                        backToTopBtn.classList.remove('visible');
                    }
                    scrollTicking = false;
                });
            }
        };

        window.addEventListener('scroll', updateScrollBtn, { passive: true });

        backToTopBtn.onclick = function() {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        };
    } else {
        // Implement Scroll Down Button for chat page
        const scrollDownBtn = document.createElement('button');
        scrollDownBtn.className = 'scroll-down-btn';
        scrollDownBtn.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" style="margin: auto; display: block;"><line x1="12" y1="5" x2="12" y2="19"></line><polyline points="19 12 12 19 5 12"></polyline></svg>';
        scrollDownBtn.setAttribute('aria-label', 'Scroll to bottom');
        document.body.appendChild(scrollDownBtn);

        let chatScrollTicking = false;
        let lastScrollY = 0;
        let lastScrollHeight = 0;
        let lastInnerHeight = 0;
        let lastClientHeight = 0;
        let lastVvScale = 1;
        let lastVvHeight = 0;
        let lastVvOffsetTop = 0;
        const hasVisualViewport = !!window.visualViewport;

        const checkScroll = () => {
            // Read all layout properties synchronously in the event handler task before any DOM writes
            lastScrollY = window.scrollY;
            lastScrollHeight = document.documentElement.scrollHeight;
            lastInnerHeight = window.innerHeight;
            lastClientHeight = document.documentElement.clientHeight;
            if (hasVisualViewport) {
                lastVvScale = window.visualViewport.scale;
                lastVvHeight = window.visualViewport.height;
                lastVvOffsetTop = window.visualViewport.offsetTop;
            }

            if (!chatScrollTicking) {
                chatScrollTicking = true;
                window.requestAnimationFrame(() => {
                    let isScrolledUp = false;
                    const scrollableHeight = lastScrollHeight - lastInnerHeight;
                    if (scrollableHeight > 50 && lastScrollY < scrollableHeight - 50) {
                        isScrolledUp = true;
                    }
                    if (hasVisualViewport) {
                        const maxOffsetTop = lastClientHeight - lastVvHeight;
                        if (lastVvScale > 1.05 && lastVvOffsetTop < maxOffsetTop - 20) {
                            isScrolledUp = true;
                        }
                    }
                    
                    if (isScrolledUp) {
                        scrollDownBtn.classList.add('visible');
                    } else {
                        scrollDownBtn.classList.remove('visible');
                    }
                    chatScrollTicking = false;
                });
            }
        };

        window.addEventListener('scroll', checkScroll, { passive: true });
        window.addEventListener('resize', checkScroll, { passive: true });
        if (hasVisualViewport) {
            window.visualViewport.addEventListener('scroll', checkScroll, { passive: true });
            window.visualViewport.addEventListener('resize', checkScroll, { passive: true });
        }
        
        scrollDownBtn.onclick = function() {
            window.scrollTo({ top: document.documentElement.scrollHeight, behavior: 'smooth' });
        };
        setTimeout(checkScroll, 500);
    }

    // --- 6. Age Gate Logic (for chat.html) ---
    const ageGateModal = document.getElementById("age-gate-modal");
    const ageGateAccept = document.getElementById("age-gate-accept");
    const ageGateExit = document.getElementById("age-gate-exit");

    if (ageGateModal && ageGateAccept && ageGateExit) {
        const isAccepted = localStorage.getItem("idc_age_gate_accepted") === "true";

        if (!isAccepted) {
            ageGateModal.classList.add("active");
            document.body.classList.add("age-gate-open");
            setTimeout(() => ageGateAccept.focus(), 100);
        }

        ageGateAccept.onclick = function() {
            localStorage.setItem("idc_age_gate_accepted", "true");
            localStorage.setItem("idc_safety_accepted", "true");
            ageGateModal.classList.remove("active");
            document.body.classList.remove("age-gate-open");
            const chatFrame = document.getElementById("chat-frame");
            if (chatFrame && chatFrame.getAttribute("data-src")) {
                chatFrame.src = chatFrame.getAttribute("data-src");
            }
        };

        ageGateExit.onclick = function() {
            window.location.href = "/";
        };

        window.addEventListener("keydown", (e) => {
            if (e.key === "Escape" && ageGateModal.classList.contains("active")) {
                if (localStorage.getItem("idc_age_gate_accepted") !== "true") {
                    e.preventDefault();
                }
            }
        });
    }

    // --- 7. Dynamic Safety Alert Popup ---
    const isSafetyAccepted = localStorage.getItem("idc_safety_accepted") === "true";
    const isAgeGateAccepted = localStorage.getItem("idc_age_gate_accepted") === "true";

    if (!isChatPage && !isSafetyAccepted && !isAgeGateAccepted) {
        const safetyOverlay = document.createElement("div");
        safetyOverlay.className = "safety-alert-overlay active";
        safetyOverlay.innerHTML = `
            <div class="safety-alert-card age-gate-card" style="max-width: 520px; text-align: left; padding: 2rem 1.5rem; border-radius: 16px; margin: 10px;">
                <div class="age-gate-icon" style="font-size: 2.5rem; margin-bottom: 0.5rem; text-align: center;">🛡️</div>
                <h2 style="font-size: 1.5rem; font-weight: 700; color: var(--accent-color); margin-bottom: 1rem; text-align: center;">Safety & Age Notice</h2>
                <p style="font-size: 0.95rem; margin-bottom: 1rem; line-height: 1.5;">
                    IndiaDostiChat is intended <strong>only for users aged 18 and above</strong>. By entering, you agree to chat responsibly, protect your privacy, and treat others with respect.
                </p>
                <p style="font-size: 0.9rem; margin-bottom: 1.5rem; line-height: 1.5; color: var(--text-color); opacity: 0.9;">
                    Please read and follow our safety guidelines. You can check all our community guidelines on the <a href="/rules/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Rules Page</a>.
                </p>
                <div class="age-gate-actions" style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;">
                    <button class="btn btn-primary btn-ok" style="background: var(--primary-color); border: none; padding: 10px 30px; border-radius: 999px; color: #0f172a !important; font-weight: 700; cursor: pointer; font-size: 0.95rem; transition: var(--transition);">I am 18+ and I Agree</button>
                    <button class="btn btn-secondary btn-leave" style="background: transparent; border: 1px solid var(--border-color); padding: 10px 30px; border-radius: 999px; color: var(--text-color); font-weight: 700; cursor: pointer; font-size: 0.95rem; transition: var(--transition);">Exit</button>
                </div>
            </div>
        `;
        document.body.appendChild(safetyOverlay);
        document.body.classList.add("age-gate-open");

        const okBtn = safetyOverlay.querySelector(".btn-ok");
        const leaveBtn = safetyOverlay.querySelector(".btn-leave");

        if (okBtn) {
            okBtn.onclick = function() {
                localStorage.setItem("idc_safety_accepted", "true");
                localStorage.setItem("idc_age_gate_accepted", "true");
                safetyOverlay.classList.remove("active");
                document.body.classList.remove("age-gate-open");
                setTimeout(() => safetyOverlay.remove(), 300);
            };
        }

        if (leaveBtn) {
            leaveBtn.onclick = function() {
                window.location.href = "https://www.google.com";
            };
        }
    }
});


// --- 8. UNO Tournament Razorpay Integration ---
document.addEventListener('DOMContentLoaded', () => {
    const RAZORPAY_KEY_ID = "YOUR_RAZORPAY_KEY_ID";
    const GOOGLE_SCRIPT_URL = "YOUR_GOOGLE_APPS_SCRIPT_WEB_APP_URL";

    const form = document.getElementById("uno-form");
    const payButton = document.getElementById("pay-uno-btn");
    const message = document.getElementById("uno-message");

    if (payButton) {
        payButton.addEventListener("click", function () {
            const usernameInput = document.getElementById("uno-username");
            const emailInput = document.getElementById("uno-email");
            const notesInput = document.getElementById("uno-notes");
            
            const username = usernameInput ? usernameInput.value.trim() : "";
            const email = emailInput ? emailInput.value.trim() : "";
            const notes = notesInput ? notesInput.value.trim() : "";

            if (!username) {
                if (message) {
                    message.textContent = "Please enter your IndiaDostiChat username.";
                    message.className = "form-message error";
                }
                return;
            }

            if (message) {
                message.textContent = "Opening Razorpay payment...";
                message.className = "form-message info";
            }

            const options = {
                key: RAZORPAY_KEY_ID,
                amount: 2500,
                currency: "INR",
                name: "IndiaDostiChat",
                description: "DUNO Tournament Entry Fee",
                prefill: {
                    name: username,
                    email: email
                },
                notes: {
                    username: username,
                    tournament: "IndiaDostiChat DUNO Tournament"
                },
                handler: function (response) {
                    const payload = {
                        username: username,
                        email: email,
                        razorpay_payment_id: response.razorpay_payment_id,
                        payment_status: "Paid - Client Reported",
                        amount: "25",
                        tournament: "IndiaDostiChat DUNO Tournament",
                        notes: notes,
                        source: "duno-tournament"
                    };

                    fetch(GOOGLE_SCRIPT_URL, {
                        method: "POST",
                        mode: "no-cors",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify(payload)
                    }).catch(err => console.warn("Form submission error", err));

                    if (message) {
                        message.textContent = "Payment successful. Registration submitted. Payment ID: " + response.razorpay_payment_id + ". Your payment will be manually verified before slot confirmation.";
                        message.className = "form-message success";
                    }

                    if (form) {
                        form.reset();
                    }
                },
                modal: {
                    ondismiss: function () {
                        if (message) {
                            message.textContent = "Payment was not completed.";
                            message.className = "form-message error";
                        }
                    }
                },
                theme: {
                    color: "#16a34a"
                }
            };

            if (typeof Razorpay !== 'undefined') {
                const rzp = new Razorpay(options);
                rzp.open();
            } else {
                if (message) {
                    message.textContent = "Razorpay script not loaded. Please refresh the page.";
                    message.className = "form-message error";
                }
            }
        });
    }

    // --- PWA Installation Click Handler ---
    const installBtn = document.getElementById('install-app-btn');
    if (installBtn) {
        if (window.deferredPrompt) {
            installBtn.style.display = 'inline-flex';
        }
        
        installBtn.addEventListener('click', async (e) => {
            e.preventDefault();
            if (window.deferredPrompt) {
                window.deferredPrompt.prompt();
                const { outcome } = await window.deferredPrompt.userChoice;
                console.log(`User choice: ${outcome}`);
                window.deferredPrompt = null;
                installBtn.style.display = 'none';
            }
        });
    }

    // --- 9. Premium India Stories Loader Transition ---
    function generateChakraSVG() {
        let lines = '';
        for (let i = 0; i < 24; i++) {
            const angle = i * 15;
            lines += `<line x1="60" y1="60" x2="60" y2="12" transform="rotate(${angle} 60 60)" />`;
            const dotAngle = angle + 7.5;
            const rad = (dotAngle * Math.PI) / 180;
            const dotX = 60 + 44 * Math.sin(rad);
            const dotY = 60 - 44 * Math.cos(rad);
            lines += `<circle cx="${dotX}" cy="${dotY}" r="1.5" />`;
        }
        return `
            <svg class="india-stories-loader-chakra-svg" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                <circle cx="60" cy="60" r="54" class="chakra-outer-ring" stroke-width="3" fill="none" />
                <circle cx="60" cy="60" r="48" class="chakra-inner-ring" stroke-width="0.8" fill="none" />
                <circle cx="60" cy="60" r="8" class="chakra-hub" />
                <circle cx="60" cy="60" r="3" fill="#ffffff" />
                <g class="chakra-spokes" stroke-width="1.8" stroke-linecap="round">
                    ${lines}
                </g>
            </svg>
        `;
    }

    // Dynamic Injection of Loader overlay
    const loaderContainer = document.createElement('div');
    loaderContainer.id = 'india-stories-loader';
    loaderContainer.className = 'india-stories-loader';
    loaderContainer.setAttribute('aria-hidden', 'true');
    loaderContainer.innerHTML = `
        <div class="india-stories-loader-card">
            <div class="india-stories-loader-chakra" aria-hidden="true">
                ${generateChakraSVG()}
            </div>
            <h2>Opening India Stories…</h2>
            <p>A journey through India’s culture, history and people</p>
            <div class="india-stories-loader-line" aria-hidden="true"></div>
        </div>
    `;
    document.body.appendChild(loaderContainer);

    // Click interceptor for India Stories links
    document.addEventListener('click', function(event) {
        const link = event.target.closest('a');
        if (!link) return;

        const href = link.getAttribute('href');
        if (!href) return;

        // Determine absolute URL destination
        let destinationUrl;
        try {
            destinationUrl = new URL(link.href, window.location.origin);
        } catch (e) {
            return; // Invalid URL
        }

        // Check if destination is pointing to /india-stories/
        const isIndiaStories = destinationUrl.origin === window.location.origin &&
            (destinationUrl.pathname === '/india-stories/' || 
             destinationUrl.pathname.startsWith('/india-stories/'));

        if (!isIndiaStories) return;

        // Skip if modifier keys are pressed or if link opens in new tab
        if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
        if (link.target === '_blank') return;

        // Prevent immediate navigation
        event.preventDefault();

        // Add class to body
        document.body.classList.add('is-loading-india-stories');

        // Show the loader overlay
        const loader = document.getElementById('india-stories-loader');
        if (loader) {
            loader.setAttribute('aria-hidden', 'false');
            loader.classList.add('active');
        }

        // Motion preferences check
        const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        const delay = reduceMotion ? 100 : 900;

        window.setTimeout(function() {
            window.location.href = link.href;
        }, delay);
    });

    // Dismiss loading animation when page is shown (handles Back button BFCache restores)
    window.addEventListener('pageshow', function(event) {
        document.body.classList.remove('is-loading-india-stories');
        const loader = document.getElementById('india-stories-loader');
        if (loader) {
            loader.setAttribute('aria-hidden', 'true');
            loader.classList.remove('active');
        }
    });
});

// --- PWA Installation Event Listener (runs immediately) ---
window.deferredPrompt = null;
window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    window.deferredPrompt = e;
    const installBtn = document.getElementById('install-app-btn');
    if (installBtn) {
        installBtn.style.display = 'inline-flex';
    }
});

