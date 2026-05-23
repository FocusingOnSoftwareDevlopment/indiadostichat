/**
 * Hidden India Section Interactive JS
 * Vanilla JavaScript - No external libraries
 */

document.addEventListener('DOMContentLoaded', () => {
  // Check for reduced motion preferences
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  initDropdownMenu();
  initTaglineRotator(prefersReducedMotion);
  initMapInteractivity();
  initRevealOnScroll(prefersReducedMotion);
  initFaqAccordion();
  initSmoothScroll();
});

/**
 * 0. Dropdown Menu Toggle
 */
function initDropdownMenu() {
  const dropdown = document.querySelector('.hidden-india-dropdown');
  const btn = document.querySelector('.hidden-india-dropdown-btn');
  if (!dropdown || !btn) return;

  btn.addEventListener('click', (e) => {
    e.stopPropagation();
    const isActive = dropdown.classList.contains('active');
    if (isActive) {
      dropdown.classList.remove('active');
      btn.setAttribute('aria-expanded', 'false');
    } else {
      dropdown.classList.add('active');
      btn.setAttribute('aria-expanded', 'true');
    }
  });

  // Close when clicking anywhere else
  document.addEventListener('click', () => {
    dropdown.classList.remove('active');
    btn.setAttribute('aria-expanded', 'false');
  });

  // Close when pressing Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      dropdown.classList.remove('active');
      btn.setAttribute('aria-expanded', 'false');
    }
  });
}

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
 * 2. Animated Map City Hover Labels (With Relative Percentages & Closest-City Tap targeting)
 */
function initMapInteractivity() {
  const mapContainer = document.querySelector('.hidden-india-map-container');
  const svg = document.querySelector('#hidden-india-svg-map');
  const cityGroups = document.querySelectorAll('.hidden-india-city-group');
  if (!mapContainer || !svg || cityGroups.length === 0) return;

  // Create tooltip element dynamically
  const tooltip = document.createElement('div');
  tooltip.className = 'hidden-india-map-tooltip';
  mapContainer.appendChild(tooltip);

  // Read cities data from DOM attributes
  const cities = Array.from(cityGroups).map(group => {
    return {
      el: group,
      name: group.getAttribute('data-city'),
      state: group.getAttribute('data-state'),
      x: parseFloat(group.getAttribute('data-x')),
      y: parseFloat(group.getAttribute('data-y'))
    };
  });

  const showCityTooltip = (city) => {
    tooltip.textContent = `${city.name}, ${city.state}`;
    tooltip.style.left = `${(city.x / 612) * 100}%`;
    tooltip.style.top = `${(city.y / 696) * 100}%`;
    tooltip.classList.add('active');
  };

  const hideTooltip = () => {
    tooltip.classList.remove('active');
  };

  // 1. Desktop Hover: use mouseenter/mouseleave for precision
  cities.forEach(city => {
    city.el.addEventListener('mouseenter', () => {
      showCityTooltip(city);
    });
    city.el.addEventListener('mouseleave', () => {
      hideTooltip();
    });
  });

  // 2. Click/Touch targeting for both mobile and desktop clicking:
  // We listen on the SVG element itself.
  svg.addEventListener('click', (e) => {
    e.stopPropagation();
    
    const rect = svg.getBoundingClientRect();
    const clickX = e.clientX - rect.left;
    const clickY = e.clientY - rect.top;
    
    // Convert screen click coordinates to viewBox units (0-612, 0-696)
    const viewX = (clickX / rect.width) * 612;
    const viewY = (clickY / rect.height) * 696;
    
    let closestCity = null;
    let minDistance = Infinity;
    
    cities.forEach(city => {
      const dist = Math.sqrt((viewX - city.x) ** 2 + (viewY - city.y) ** 2);
      if (dist < minDistance) {
        minDistance = dist;
        closestCity = city;
      }
    });
    
    // If click is within 45 viewBox units (approx. 20-30px on screen), show tooltip
    if (minDistance < 45) {
      const isActive = tooltip.classList.contains('active') && 
                       tooltip.textContent === `${closestCity.name}, ${closestCity.state}`;
      if (isActive) {
        hideTooltip();
      } else {
        showCityTooltip(closestCity);
      }
    } else {
      hideTooltip();
    }
  });

  // Tap/click anywhere else to dismiss tooltip
  document.addEventListener('click', () => {
    hideTooltip();
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
