/**
 * Hidden India Section Interactive JS
 * Vanilla JavaScript - No external libraries
 */

// Early Theme Check to avoid flash of dark background in light mode
(function() {
  let savedTheme = null;
  try {
    savedTheme = localStorage.getItem("theme");
  } catch (e) {}
  
  const urlParams = new URLSearchParams(window.location.search);
  const themeParam = urlParams.get('theme') || urlParams.get('dark');
  
  let isLight = false;
  if (themeParam === 'light' || themeParam === '0' || themeParam === 'false') {
    isLight = true;
  } else if (themeParam === 'dark' || themeParam === '1' || themeParam === 'true') {
    isLight = false;
  } else {
    isLight = (savedTheme === "light");
  }
  
  if (isLight) {
    document.documentElement.classList.add("light-mode");
  } else {
    document.documentElement.classList.remove("light-mode");
  }
})();

document.addEventListener('DOMContentLoaded', () => {
  // Sync body class with html element
  if (document.documentElement.classList.contains("light-mode")) {
    document.body.classList.add("light-mode");
  }

  // Check for reduced motion preferences
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  initThemeToggle();
  initMenuDrawer();
  initTaglineRotator(prefersReducedMotion);
  initMapInteractivity();
  initRevealOnScroll(prefersReducedMotion);
  initFaqAccordion();
  initSmoothScroll();
});

/**
 * 0. SpaceX-style Right Menu Drawer Toggle
 */
function initMenuDrawer() {
  const toggleBtn = document.querySelector('.hidden-india-menu-toggle');
  const closeBtn = document.querySelector('.hidden-india-drawer-close');
  const drawer = document.getElementById('hidden-india-drawer');
  const backdrop = document.querySelector('.hidden-india-drawer-backdrop');

  if (!toggleBtn || !drawer) return;

  const openDrawer = () => {
    drawer.classList.add('active');
    drawer.setAttribute('aria-hidden', 'false');
    toggleBtn.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden'; // Prevent background scrolling
  };

  const closeDrawer = () => {
    drawer.classList.remove('active');
    drawer.setAttribute('aria-hidden', 'true');
    toggleBtn.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = ''; // Restore scrolling
  };

  toggleBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    openDrawer();
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', closeDrawer);
  }

  if (backdrop) {
    backdrop.addEventListener('click', closeDrawer);
  }

  // Close when pressing Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('active')) {
      closeDrawer();
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
    
    // Temporarily make active but hidden to get actual dimensions
    tooltip.style.visibility = 'hidden';
    tooltip.classList.add('active');
    const tooltipWidth = tooltip.offsetWidth;
    tooltip.classList.remove('active');
    tooltip.style.visibility = '';
    
    const containerWidth = mapContainer.offsetWidth;
    
    // Calculate raw X position in pixels relative to the container
    let leftPx = (city.x / 612) * containerWidth;
    
    // Constrain tooltip horizontally within map container (10px padding from edges)
    const halfWidth = tooltipWidth / 2;
    if (leftPx - halfWidth < 10) {
      leftPx = halfWidth + 10;
    } else if (leftPx + halfWidth > containerWidth - 10) {
      leftPx = containerWidth - halfWidth - 10;
    }
    
    tooltip.style.left = `${leftPx}px`;
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

/**
 * 6. Lightbulb Theme Toggle (Dark/Light mode switch with micro-animation)
 */
function initThemeToggle() {
  const headerRight = document.querySelector('.hidden-india-nav-right');
  if (!headerRight) return;

  // Create bulb toggle button
  const bulbToggle = document.createElement('button');
  bulbToggle.id = 'hidden-india-bulb-toggle';
  bulbToggle.className = 'hidden-india-bulb-toggle';
  bulbToggle.setAttribute('aria-label', 'Toggle dark mode');
  bulbToggle.setAttribute('title', 'Toggle dark mode');
  
  // Custom bulb SVG content
  bulbToggle.innerHTML = `
    <div class="bulb-glow"></div>
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path class="bulb-fill" d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A5 5 0 0 0 8 8c0 1 .3 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5z" />
      <line x1="9" y1="18" x2="15" y2="18" />
      <line x1="10" y1="22" x2="14" y2="22" />
      <line class="bulb-ray" x1="12" y1="2" x2="12" y2="4" />
      <line class="bulb-ray" x1="5" y1="5" x2="6.4" y2="6.4" />
      <line class="bulb-ray" x1="2" y1="12" x2="4" y2="12" />
      <line class="bulb-ray" x1="5" y1="19" x2="6.4" y2="17.6" />
      <line class="bulb-ray" x1="19" y1="5" x2="17.6" y2="6.4" />
      <line class="bulb-ray" x1="22" y1="12" x2="20" y2="12" />
      <line class="bulb-ray" x1="19" y1="19" x2="17.6" y2="17.6" />
    </svg>
  `;

  // Insert bulb toggle as the first element inside nav-right
  headerRight.insertBefore(bulbToggle, headerRight.firstChild);

  bulbToggle.addEventListener('click', (e) => {
    e.preventDefault();
    
    // Add vibration shake class
    bulbToggle.classList.add('clicked');
    setTimeout(() => {
      bulbToggle.classList.remove('clicked');
    }, 450);

    const isLightNow = document.body.classList.toggle('light-mode');
    document.documentElement.classList.toggle('light-mode', isLightNow);
    
    try {
      localStorage.setItem('theme', isLightNow ? 'light' : 'dark');
    } catch (err) {}
  });
}
