// Hamburger menu functionality
document.addEventListener('DOMContentLoaded', function() {
    const nav = document.querySelector('nav');
    
    // Create hamburger button if it doesn't exist
    if (!document.querySelector('.hamburger')) {
        // Create the hamburger button
        const hamburger = document.createElement('button');
        hamburger.className = 'hamburger';
        hamburger.setAttribute('aria-label', 'Menu');
        
        // Create three spans for the hamburger icon
        for (let i = 0; i < 3; i++) {
            const span = document.createElement('span');
            hamburger.appendChild(span);
        }
        
        // Insert hamburger at the beginning of nav
        nav.insertBefore(hamburger, nav.firstChild);
        
        // Ensure the button is the last element
        const navButton = document.querySelector('.navbar-button');
        if (navButton && navButton.parentNode === nav) {
            nav.appendChild(navButton);
        }
    }
    
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('nav ul');
    
    hamburger.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        navMenu.classList.toggle('active');
        hamburger.classList.toggle('active');
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        if (!nav.contains(event.target) && navMenu.classList.contains('active')) {
            navMenu.classList.remove('active');
            hamburger.classList.remove('active');
        }
    });
    
    // Close menu when clicking on a nav link
    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navMenu.classList.remove('active');
            hamburger.classList.remove('active');
        });
    });
    
    // Improved image fallback for roaster cards
    const placeholderPath = '/static/img/coffee-placeholder.jpg';
    
    // Pre-load the placeholder image to ensure it's in the browser cache
    const preloadPlaceholder = new Image();
    preloadPlaceholder.src = placeholderPath;
    
    // Apply fallback to all roaster images
    const roasterImages = document.querySelectorAll('.roaster-image img');
    roasterImages.forEach(img => {
        // Hide image initially until we know it loads correctly
        img.style.opacity = '0';
        img.style.transition = 'opacity 0.3s ease';
        
        // Function to apply the placeholder
        const applyPlaceholder = () => {
            img.src = placeholderPath;
            img.classList.add('fallback-image');
            img.style.opacity = '1';
        };
        
        // Function when image loads successfully
        const imageLoaded = () => {
            img.style.opacity = '1';
        };
        
        // Set up event handlers
        img.addEventListener('error', applyPlaceholder);
        img.addEventListener('load', imageLoaded);
        
        // Check images that might have already failed before JS loaded
        if (img.complete) {
            if (img.naturalWidth === 0 || img.naturalHeight === 0) {
                applyPlaceholder();
            } else {
                imageLoaded();
            }
        }
    });
});

// Console log when page is loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('Coffee Roasters Directory loaded');
});
    