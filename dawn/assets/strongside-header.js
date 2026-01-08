/**
 * STRONGSIDE Header Enhancement
 * Handles transparent-to-solid header transition on scroll
 */

class StrongsideHeader {
	constructor() {
		this.header = document.querySelector('.section-header');
		this.headerWrapper = document.querySelector('.header-wrapper');
		this.scrollThreshold = 50; // Pixels before header becomes solid
		this.isTransparent = true;

		if (this.header) {
			this.init();
		}
	}

	init() {
		// Set initial transparent state
		this.setTransparent();

		// Listen for scroll events with throttling
		let ticking = false;
		window.addEventListener('scroll', () => {
			if (!ticking) {
				window.requestAnimationFrame(() => {
					this.onScroll();
					ticking = false;
				});
				ticking = true;
			}
		}, { passive: true });

		// Check initial state
		this.onScroll();
	}

	onScroll() {
		const scrollY = window.scrollY || window.pageYOffset;

		if (scrollY > this.scrollThreshold && this.isTransparent) {
			this.setSolid();
		} else if (scrollY <= this.scrollThreshold && !this.isTransparent) {
			this.setTransparent();
		}
	}

	setTransparent() {
		this.isTransparent = true;
		this.header.classList.add('strongside-header-transparent');
		this.header.classList.remove('strongside-header-solid');

		if (this.headerWrapper) {
			this.headerWrapper.style.backgroundColor = 'transparent';
			this.headerWrapper.style.backdropFilter = 'none';
			this.headerWrapper.style.webkitBackdropFilter = 'none';
			this.headerWrapper.style.borderBottom = 'none';
		}
	}

	setSolid() {
		this.isTransparent = false;
		this.header.classList.remove('strongside-header-transparent');
		this.header.classList.add('strongside-header-solid');

		if (this.headerWrapper) {
			this.headerWrapper.style.backgroundColor = 'rgba(5, 5, 5, 0.95)';
			this.headerWrapper.style.backdropFilter = 'blur(12px)';
			this.headerWrapper.style.webkitBackdropFilter = 'blur(12px)';
			this.headerWrapper.style.borderBottom = '1px solid rgba(255, 255, 255, 0.1)';
		}
	}
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
	document.addEventListener('DOMContentLoaded', () => new StrongsideHeader());
} else {
	new StrongsideHeader();
}

// Also reinitialize if Shopify editor reloads sections
document.addEventListener('shopify:section:load', () => new StrongsideHeader());
