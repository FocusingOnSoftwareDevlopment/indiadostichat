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
