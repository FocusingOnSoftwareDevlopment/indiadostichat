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
            const icon = mobileMenuBtn.querySelector('i');
            if (icon) {
                if (navLinks.classList.contains('active')) {
                    icon.classList.remove('fa-bars');
                    icon.classList.add('fa-times');
                } else {
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            }
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

    const visitKey = 'idc_visit_counted_' + dateStr;
    const joinKey = 'idc_join_counted_' + dateStr;

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
                    visitorCountEls.forEach(el => el.innerText = 'Unavailable');
                }
            })
            .catch(() => {
                visitorCountEls.forEach(el => el.innerText = 'Unavailable');
            });
    }

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
                .catch(err => console.error("Error incrementing join count:", err));
        }
        return Promise.resolve();
    }

    // 3b. Join Chat Counter logic
    if (joinCountEls.length > 0) {
        // Fetch current join count (always show it)
        fetch('https://api.counterapi.dev/v1/indiadostichat_main/join_chat')
            .then(res => res.json())
            .then(data => {
                if (data && typeof data.count !== 'undefined') {
                    updateJoinUI(data.count);
                } else {
                    joinCountEls.forEach(el => el.innerText = 'Unavailable');
                }
            })
            .catch(() => {
                joinCountEls.forEach(el => el.innerText = 'Unavailable');
            });
    }

    // Check if the user is on the chat page directly
    const pathLower = window.location.pathname.toLowerCase();
    const isDirectChatPage = pathLower.includes('/chat/') || 
                             pathLower.endsWith('/chat') || 
                             pathLower.endsWith('/chat.html') || 
                             pathLower.endsWith('/chat/index.html');

    if (isDirectChatPage) {
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
            { src: "assets/images/home-hero/mumbai-gateway.webp", label: "Mumbai" },
            { src: "assets/images/home-hero/delhi-india-gate.webp", label: "Delhi" },
            { src: "assets/images/home-hero/hyderabad-charminar.webp", label: "Hyderabad" },
            { src: "assets/images/home-hero/jaipur-hawa-mahal.webp", label: "Jaipur" },
            { src: "assets/images/home-hero/kerala-backwaters.webp", label: "Kerala" },
            { src: "assets/images/home-hero/kashmir-mountains.webp", label: "Kashmir" },
            { src: "assets/images/home-hero/varanasi-ghats.webp", label: "Varanasi" },
            { src: "assets/images/home-hero/goa-beach.webp", label: "Goa" },
            { src: "assets/images/home-hero/india-festival-lights.webp", label: "India" }
        ];

        let currentImgIdx = 0;
        let activeLayerIdx = 0;

        // Preload other images after the page loads
        window.addEventListener('load', () => {
            for (let i = 1; i < heroImages.length; i++) {
                const img = new Image();
                img.src = heroImages[i].src;
            }
        });

        if (!prefersReducedMotion && heroBgLayers.length >= 2) {
            setInterval(() => {
                const nextImgIdx = (currentImgIdx + 1) % heroImages.length;
                const nextLayerIdx = 1 - activeLayerIdx;
                
                const activeLayer = heroBgLayers[activeLayerIdx];
                const inactiveLayer = heroBgLayers[nextLayerIdx];

                // Set image on the inactive layer
                inactiveLayer.style.backgroundImage = `url('${heroImages[nextImgIdx].src}')`;
                
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

    // --- 5. Back to Top Button ---
    const backToTopBtn = document.createElement('button');
    backToTopBtn.className = 'back-to-top';
    backToTopBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    backToTopBtn.setAttribute('aria-label', 'Back to top');
    document.body.appendChild(backToTopBtn);

    window.onscroll = function() {
        if (window.scrollY > 300) {
            backToTopBtn.classList.add('visible');
        } else {
            backToTopBtn.classList.remove('visible');
        }
    };

    backToTopBtn.onclick = function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };

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
    const isChatPage = window.location.pathname.includes("/chat/");
    const isSafetyAccepted = localStorage.getItem("idc_safety_accepted") === "true";
    const isAgeGateAccepted = localStorage.getItem("idc_age_gate_accepted") === "true";

    if (!isChatPage && !isSafetyAccepted && !isAgeGateAccepted) {
        const safetyOverlay = document.createElement("div");
        safetyOverlay.className = "safety-alert-overlay active";
        safetyOverlay.innerHTML = `
            <div class="safety-alert-card age-gate-card" style="max-width: 680px; text-align: left; padding: 2.5rem; border-radius: 16px;">
                <div class="age-gate-icon" style="font-size: 3rem; margin-bottom: 1rem; text-align: center;">🛡️</div>
                <h2 style="font-size: 1.8rem; font-weight: 700; color: var(--accent-color); margin-bottom: 1.5rem; text-align: center;">Safety & Age Notice</h2>
                <p style="font-size: 1rem; margin-bottom: 1rem; line-height: 1.6;">
                    IndiaDostiChat is intended only for users aged 18 and above. If you are under 18, you must leave this site immediately.
                </p>
                <p style="font-size: 0.95rem; margin-bottom: 1rem; font-weight: 500;">Before entering, please understand and agree to the following safety guidelines:</p>
                <ul style="font-size: 0.88rem; margin-bottom: 24px; padding-left: 20px; line-height: 1.6; color: var(--text-color); opacity: 0.9;">
                    <li style="margin-bottom: 8px;"><strong>Protect Your Privacy:</strong> Do not share phone numbers, home address, passwords, OTP, financial details, private photos, or sensitive information.</li>
                    <li style="margin-bottom: 8px;"><strong>Stay Safe:</strong> Do not trust strangers with money, personal details, or private content.</li>
                    <li style="margin-bottom: 8px;"><strong>Prohibited Content:</strong> Do not post or request adult, sexual, abusive, hateful, threatening, illegal, or harmful content.</li>
                    <li style="margin-bottom: 8px;"><strong>Respect Others:</strong> Do not harass, bully, spam, impersonate, scam, or disturb other users.</li>
                    <li style="margin-bottom: 8px;"><strong>User Responsibility:</strong> IndiaDostiChat does not verify user identity. Conversations are user-generated, and users are responsible for their own actions.</li>
                </ul>
                <p style="font-size: 0.95rem; margin-bottom: 1.5rem; line-height: 1.6;">
                    By clicking <strong>"I am 18+ and I Agree,"</strong> you confirm that you are at least 18 years old and agree to follow the IndiaDostiChat rules.
                </p>
                <div class="age-gate-actions" style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;">
                    <button class="btn btn-primary btn-ok" style="background: var(--primary-color); border: none; padding: 12px 40px; border-radius: 999px; color: white; font-weight: 700; cursor: pointer; font-size: 1rem; transition: var(--transition);">I am 18+ and I Agree</button>
                    <button class="btn btn-secondary btn-leave" style="background: transparent; border: 1px solid var(--border-color); padding: 12px 40px; border-radius: 999px; color: var(--text-color); font-weight: 700; cursor: pointer; font-size: 1rem; transition: var(--transition);">Exit</button>
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
                    }).catch(err => console.error("Form submission error", err));

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

