document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');

    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            const icon = mobileMenuBtn.querySelector('i');
            if (navLinks.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }

    // Chat Gate Logic (for chat.html)
    const chatGate = document.getElementById('chatGate');
    const chatWrapper = document.getElementById('chatWrapper');
    const enterChatBtn = document.getElementById('enterChatBtn');

    if (chatGate && enterChatBtn) {
        enterChatBtn.addEventListener('click', () => {
            // In a real implementation with Turnstile, we would wait for the token
            // Since this is static, we simulate a small loading delay, then show chat
            
            // To implement Turnstile properly:
            // 1. Add Turnstile widget to HTML
            // 2. Listen for 'cf-turnstile-response' event or callback
            // 3. Hide gate, show wrapper
            
            enterChatBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Verifying...';
            enterChatBtn.disabled = true;

            setTimeout(() => {
                chatGate.style.display = 'none';
                chatWrapper.style.display = 'block';
                
                // Hide header/footer if desired for fullscreen immersion
                const header = document.querySelector('header');
                if (header) header.style.display = 'none';
                
                // Remove padding from main
                const main = document.querySelector('main');
                if (main) {
                    main.style.marginTop = '0';
                    main.style.height = '100vh';
                }
                
                // Update container height
                const container = document.querySelector('.chat-container');
                if (container) {
                    container.style.height = '100vh';
                }
            }, 1000);
        });
    }

    // Set active link in navigation
    const currentLocation = location.pathname.split('/').pop();
    const navItems = document.querySelectorAll('.nav-links a');
    
    navItems.forEach(item => {
        const href = item.getAttribute('href');
        if (href === currentLocation || (currentLocation === '' && href === 'index.html')) {
            item.style.color = 'var(--primary-color)';
        }
    });
});

// Turnstile callback (if used)
function onTurnstileSuccess(token) {
    const enterChatBtn = document.getElementById('enterChatBtn');
    if (enterChatBtn) {
        enterChatBtn.disabled = false;
        enterChatBtn.textContent = 'Join Room #IndiaDostiChat';
    }
}

// Visitor Counter Logic
document.addEventListener('DOMContentLoaded', () => {
    const visitorCountEls = document.querySelectorAll('#visitor-count');
    if (visitorCountEls.length > 0) {
        fetch('https://api.counterapi.dev/v1/indiadostichat/visitors/up')
            .then(response => response.json())
            .then(data => {
                visitorCountEls.forEach(el => {
                    el.innerText = data.count;
                });
            })
            .catch(error => {
                console.error('Error fetching visitor count:', error);
                visitorCountEls.forEach(el => {
                    el.innerText = 'Unavailable';
                });
            });
    }

    // Theme Toggle Logic
    const themeToggle = document.getElementById("theme-toggle");
    const themeIcon = themeToggle ? themeToggle.querySelector(".theme-icon") : null;

    function applyTheme(theme) {
        const isDark = theme === "dark";
        document.body.classList.toggle("dark-mode", isDark);
        if (themeIcon) {
            themeIcon.textContent = isDark ? "☀️" : "🌙";
        }
        if (themeToggle) {
            themeToggle.setAttribute("aria-label", isDark ? "Switch to light mode" : "Switch to dark mode");
            themeToggle.setAttribute("title", isDark ? "Switch to light mode" : "Switch to dark mode");
        }
    }

    let savedTheme = null;
    try {
        savedTheme = localStorage.getItem("theme");
    } catch (e) {
        console.warn("localStorage not available", e);
    }
    const systemPrefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
    const initialTheme = savedTheme || (systemPrefersDark ? "dark" : "light");

    applyTheme(initialTheme);

    if (themeToggle) {
        themeToggle.addEventListener("click", function (e) {
            e.preventDefault();
            const isDark = document.body.classList.contains("dark-mode");
            const newTheme = isDark ? "light" : "dark";
            try {
                localStorage.setItem("theme", newTheme);
            } catch (err) {}
            applyTheme(newTheme);
        });
    }

    // Copy Invite Message logic (Removed per request)

    // Rotating Background Logic for Landing Pages
    const landingHeroes = document.querySelectorAll('.landing-hero');
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (!prefersReducedMotion && landingHeroes.length > 0) {
        landingHeroes.forEach(hero => {
            const bgAttr = hero.getAttribute('data-bg-images');
            if (bgAttr) {
                const images = bgAttr.split(',').map(src => src.trim()).filter(src => src.length > 0);
                if (images.length > 1) {
                    let currentIndex = 0;
                    
                    // Preload all images
                    images.forEach(src => {
                        const img = new Image();
                        img.src = src;
                    });

                    // Set initial image
                    hero.style.setProperty('--landing-bg-image', `url('${images[currentIndex]}')`);

                    // Rotate every 8 seconds
                    setInterval(() => {
                        currentIndex = (currentIndex + 1) % images.length;
                        hero.style.setProperty('--landing-bg-image', `url('${images[currentIndex]}')`);
                    }, 8000);
                } else if (images.length === 1) {
                    hero.style.setProperty('--landing-bg-image', `url('${images[0]}')`);
                }
            }
        });
    }
});
