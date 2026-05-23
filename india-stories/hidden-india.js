/**
 * Hidden India Section Interactive JS
 * Vanilla JavaScript - No external libraries
 */

document.addEventListener('DOMContentLoaded', () => {
  // Check for reduced motion preferences
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  initTaglineRotator(prefersReducedMotion);
  initMapInteractivity();
  initRevealOnScroll(prefersReducedMotion);
  initFaqAccordion();
  initSmoothScroll();
});

/**
 * 1. Rotating Hero Taglines
 */
function initTaglineRotator(prefersReducedMotion) {
  const taglineEl = document.querySelector('.hidden-india-tagline');
  if (!taglineEl) return;

  const taglines = [
    "India is not just a country. It is a conversation.",
    "A billion stories. One shared heartbeat.",
    "From ancient roots to digital friendships.",
    "Many languages. One feeling.",
    "Where culture becomes connection.",
    "Where strangers become dost.",
    "Every city has a story. Every story needs someone to listen.",
    "India lives in its people, memories, festivals, food, and friendships.",
    "From Mumbai streets to Delhi nights, India keeps talking.",
    "IndiaDostiChat — where India meets online."
  ];

  // Pick 3-5 taglines to rotate in this session
  // We will shuffle and take 4 taglines to keep it clean and subtle
  const shuffled = taglines.sort(() => 0.5 - Math.random());
  const selectedTaglines = shuffled.slice(0, 4);

  let currentIndex = 0;

  // Set initial tagline
  taglineEl.textContent = selectedTaglines[currentIndex];
  taglineEl.classList.add('active');

  if (prefersReducedMotion) return; // Do not rotate if reduced motion is requested

  setInterval(() => {
    // Fade out
    taglineEl.classList.remove('active');

    setTimeout(() => {
      // Switch text
      currentIndex = (currentIndex + 1) % selectedTaglines.length;
      taglineEl.textContent = selectedTaglines[currentIndex];
      // Fade in
      taglineEl.classList.add('active');
    }, 800); // Match CSS transition duration
  }, 6000); // Stay visible for 6 seconds
}

/**
 * 2. Animated Map City Hover Labels
 */
function initMapInteractivity() {
  const mapContainer = document.querySelector('.hidden-india-map-container');
  const cityGroups = document.querySelectorAll('.hidden-india-city-group');
  if (!mapContainer || cityGroups.length === 0) return;

  // Create tooltip element dynamically
  const tooltip = document.createElement('div');
  tooltip.className = 'hidden-india-map-tooltip';
  mapContainer.appendChild(tooltip);

  cityGroups.forEach(group => {
    const cityName = group.getAttribute('data-city');
    const stateName = group.getAttribute('data-state');

    const showTooltip = (circle) => {
      if (!circle) return;
      const cx = parseFloat(circle.getAttribute('cx'));
      const cy = parseFloat(circle.getAttribute('cy'));
      const xPercent = (cx / 612) * 100;
      const yPercent = (cy / 696) * 100;

      tooltip.textContent = `${cityName}, ${stateName}`;
      tooltip.style.left = `${xPercent}%`;
      tooltip.style.top = `${yPercent}%`;
      tooltip.classList.add('active');
    };

    group.addEventListener('mouseenter', () => {
      const circle = group.querySelector('.hidden-india-city-dot');
      showTooltip(circle);
    });

    group.addEventListener('mouseleave', () => {
      tooltip.classList.remove('active');
    });

    // Touch/tap trigger for mobile compatibility
    group.addEventListener('click', (e) => {
      e.stopPropagation();
      const circle = group.querySelector('.hidden-india-city-dot');
      const isActive = tooltip.classList.contains('active') && tooltip.textContent === `${cityName}, ${stateName}`;
      
      if (isActive) {
        tooltip.classList.remove('active');
      } else {
        showTooltip(circle);
      }
    });
  });

  // Tap anywhere else to dismiss tooltip on mobile
  document.addEventListener('click', () => {
    tooltip.classList.remove('active');
  });
}

/**
 * 3. Reveal-on-scroll animation using IntersectionObserver
 */
function initRevealOnScroll(prefersReducedMotion) {
  if (prefersReducedMotion) return;

  const revealElements = document.querySelectorAll('.reveal-element');
  if (revealElements.length === 0) return;

  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        // Unobserve after showing
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  revealElements.forEach(el => observer.observe(el));
}

/**
 * 4. FAQ Accordion Collapse/Expand
 */
function initFaqAccordion() {
  const faqQuestions = document.querySelectorAll('.hidden-india-faq-question');
  
  faqQuestions.forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.parentElement;
      const answer = item.querySelector('.hidden-india-faq-answer');
      const isActive = item.classList.contains('active');

      // Close all other items first (optional, but premium feel)
      document.querySelectorAll('.hidden-india-faq-item').forEach(otherItem => {
        if (otherItem !== item) {
          otherItem.classList.remove('active');
          otherItem.querySelector('.hidden-india-faq-answer').style.maxHeight = null;
        }
      });

      if (isActive) {
        item.classList.remove('active');
        answer.style.maxHeight = null;
      } else {
        item.classList.add('active');
        // Set max-height to its scrollHeight to transition smoothly
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });
}

/**
 * 5. Smooth Scroll for Table of Contents
 */
function initSmoothScroll() {
  const tocLinks = document.querySelectorAll('.hidden-india-toc-link, .hidden-india-nav-link');
  
  tocLinks.forEach(link => {
    const targetId = link.getAttribute('href');
    if (!targetId || !targetId.startsWith('#')) return;

    link.addEventListener('click', (e) => {
      e.preventDefault();
      const targetEl = document.querySelector(targetId);
      if (targetEl) {
        targetEl.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
}
