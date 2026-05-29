/**
 * Hidden India Section Interactive JS
 * Vanilla JavaScript - No external libraries
 */

// Early Theme Check to avoid flash of dark background in light mode
(function() {
  console.log("India Stories: Scoped early theme check script running...");
  let savedTheme = null;
  try {
    savedTheme = localStorage.getItem("indiaStoriesTheme");
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
  initSideArt();
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
 * 6. Scoped Hanging Bulb + Pull String Theme Toggle (with premium SVG and micro-animations)
 */
function initThemeToggle() {
  console.log("India Stories: Creating and appending premium fixed lightbulb image toggle...");

  // Create bulb toggle button
  const bulbToggle = document.createElement('button');
  bulbToggle.id = 'hidden-india-bulb-toggle';
  bulbToggle.className = 'is-bulb-toggle';
  bulbToggle.setAttribute('aria-label', 'Toggle India Stories light mode');
  
  const isCurrentlyLight = document.documentElement.classList.contains('light-mode');
  bulbToggle.setAttribute('title', isCurrentlyLight ? 'Pull for dark' : 'Pull for light');
  
  // Hanging switch image & HTML structure
  bulbToggle.innerHTML = `
    <span class="is-bulb-wrap">
      <img src="/india-stories/images/bulb-toggle.png" alt="" class="is-bulb-img" aria-hidden="true">
      <span class="is-bulb-glow" aria-hidden="true"></span>
    </span>
    <span class="is-pull-string" aria-hidden="true"></span>
    <span class="is-pull-knob" aria-hidden="true"></span>
  `;

  // Append directly to the body for clean fixed overlay positioning
  document.body.appendChild(bulbToggle);

  bulbToggle.addEventListener('click', (e) => {
    e.preventDefault();
    
    // Trigger physics spring animations
    bulbToggle.classList.add('is-pulled');
    setTimeout(() => {
      bulbToggle.classList.remove('is-pulled');
    }, 400); // pull move snap duration

    const isLightNow = document.body.classList.toggle('light-mode');
    document.documentElement.classList.toggle('light-mode', isLightNow);
    
    bulbToggle.setAttribute('title', isLightNow ? 'Pull for dark' : 'Pull for light');
    
    try {
      localStorage.setItem('indiaStoriesTheme', isLightNow ? 'light' : 'dark');
    } catch (err) {}
  });
}

/**
 * 7. Inject Traditional Indian Print Side Art Panels (Warli & Mandala)
 */
function initSideArt() {
  console.log("India Stories: Injecting vertical side art panels...");
  
  // Clean existing ones if any
  document.querySelectorAll('.india-stories-side-art-left, .india-stories-side-art-right').forEach(el => el.remove());
  
  const leftArt = document.createElement('div');
  leftArt.className = 'india-stories-side-art-left';
  leftArt.setAttribute('aria-hidden', 'true');
  
  const rightArt = document.createElement('div');
  rightArt.className = 'india-stories-side-art-right';
  rightArt.setAttribute('aria-hidden', 'true');
  
  // Custom Warli tribal dance & circular mandala pattern SVG
  const sideSvgMarkup = `
    <svg viewBox="0 0 100 800" class="india-stories-side-art-svg" xmlns="http://www.w3.org/2000/svg">
      <!-- Axis cord line -->
      <line x1="50" y1="0" x2="50" y2="800" stroke="currentColor" stroke-width="0.8" stroke-dasharray="4,6" />
      
      <!-- Top Mandala (y = 100) -->
      <g>
        <circle cx="50" cy="100" r="22" fill="none" stroke="currentColor" stroke-width="1.2" />
        <circle cx="50" cy="100" r="15" fill="none" stroke="currentColor" stroke-width="0.8" stroke-dasharray="2,2" />
        <circle cx="50" cy="100" r="8" fill="none" stroke="currentColor" stroke-width="1.2" />
        <circle cx="50" cy="100" r="2" fill="currentColor" />
        <path d="M 50 72 L 50 128 M 22 100 L 78 100 M 30 80 L 70 120 M 30 120 L 70 80" stroke="currentColor" stroke-width="0.8" />
      </g>
      
      <!-- Upper Warli Dancing Pair (y = 250) -->
      <g>
        <!-- Figure 1 (Left) -->
        <circle cx="38" cy="245" r="4" fill="currentColor" />
        <polygon points="34,251 42,251 38,259" fill="currentColor" />
        <polygon points="34,267 42,267 38,259" fill="currentColor" />
        <path d="M 38 255 L 28 250 M 38 255 L 48 261" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
        <path d="M 38 267 L 33 282 M 38 267 L 43 282" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
        
        <!-- Hand connection -->
        <path d="M 48 261 Q 50 263 52 261" stroke="currentColor" stroke-width="1.5" fill="none" />
        
        <!-- Figure 2 (Right) -->
        <circle cx="62" cy="245" r="4" fill="currentColor" />
        <polygon points="58,251 66,251 62,259" fill="currentColor" />
        <polygon points="58,267 66,267 62,259" fill="currentColor" />
        <path d="M 62 255 L 52 261 M 62 255 L 72 250" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
        <path d="M 62 267 L 57 282 M 62 267 L 67 282" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
      </g>
      
      <!-- Middle Mandala (y = 400) -->
      <g>
        <circle cx="50" cy="400" r="22" fill="none" stroke="currentColor" stroke-width="1.2" />
        <circle cx="50" cy="400" r="15" fill="none" stroke="currentColor" stroke-width="0.8" stroke-dasharray="2,2" />
        <circle cx="50" cy="400" r="8" fill="none" stroke="currentColor" stroke-width="1.2" />
        <circle cx="50" cy="400" r="2" fill="currentColor" />
        <path d="M 50 372 L 50 428 M 22 400 L 78 400 M 30 380 L 70 420 M 30 420 L 70 380" stroke="currentColor" stroke-width="0.8" />
      </g>
      
      <!-- Lower Warli Dancing Pair (y = 550) -->
      <g>
        <!-- Figure 3 (Left) -->
        <circle cx="38" cy="545" r="4" fill="currentColor" />
        <polygon points="34,551 42,551 38,559" fill="currentColor" />
        <polygon points="34,567 42,567 38,559" fill="currentColor" />
        <path d="M 38 555 L 28 550 M 38 555 L 48 561" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
        <path d="M 38 567 L 33 582 M 38 567 L 43 582" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
        
        <!-- Hand connection -->
        <path d="M 48 561 Q 50 563 52 561" stroke="currentColor" stroke-width="1.5" fill="none" />
        
        <!-- Figure 4 (Right) -->
        <circle cx="62" cy="545" r="4" fill="currentColor" />
        <polygon points="58,551 66,551 62,559" fill="currentColor" />
        <polygon points="58,567 66,567 62,559" fill="currentColor" />
        <path d="M 62 555 L 52 561 M 62 555 L 72 550" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
        <path d="M 62 567 L 57 582 M 62 567 L 67 582" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
      </g>
      
      <!-- Bottom Mandala (y = 700) -->
      <g>
        <circle cx="50" cy="700" r="22" fill="none" stroke="currentColor" stroke-width="1.2" />
        <circle cx="50" cy="700" r="15" fill="none" stroke="currentColor" stroke-width="0.8" stroke-dasharray="2,2" />
        <circle cx="50" cy="700" r="8" fill="none" stroke="currentColor" stroke-width="1.2" />
        <circle cx="50" cy="700" r="2" fill="currentColor" />
        <path d="M 50 672 L 50 728 M 22 700 L 78 700 M 30 680 L 70 720 M 30 720 L 70 680" stroke="currentColor" stroke-width="0.8" />
      </g>
    </svg>
  `;
  
  leftArt.innerHTML = sideSvgMarkup;
  rightArt.innerHTML = sideSvgMarkup;
  
  // Append to the body
  document.body.appendChild(leftArt);
  document.body.appendChild(rightArt);
}
