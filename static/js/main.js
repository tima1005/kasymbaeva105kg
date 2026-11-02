document.addEventListener("DOMContentLoaded", function () {

    // =================================
    // MOBILE MENU
    // =================================

    const menuToggle = document.getElementById("menuToggle");
    const mainNav = document.getElementById("mainNav");

    if (menuToggle && mainNav) {
        menuToggle.addEventListener("click", function () {
            mainNav.classList.toggle("active");

            menuToggle.setAttribute(
                "aria-expanded",
                mainNav.classList.contains("active")
            );
        });

        mainNav.querySelectorAll("a").forEach(link => {
            link.addEventListener("click", function () {
                mainNav.classList.remove("active");
                menuToggle.setAttribute("aria-expanded", "false");
            });
        });
    }


    // =================================
    // ACTIVE NAVIGATION
    // =================================

    const currentPath = window.location.pathname;

    document.querySelectorAll(".modern-nav a").forEach(link => {
        const linkPath = new URL(link.href).pathname;

        if (linkPath === currentPath) {
            link.classList.add("active-link");
        }
    });


    // =================================
    // PAGE LOAD ANIMATION
    // =================================

    document.body.classList.add("page-loaded");


    // =================================
    // SCROLL REVEAL ANIMATION
    // =================================

    const animatedElements = document.querySelectorAll(`
        .section-heading,
        .stats-heading,
        .stat-card,
        .about-visual,
        .about-content,
        .info-card,
        .teacher-card,
        .gallery-item,
        .section-more,
        .gallery-banner,
        .contact-cta-inner,
        .about-intro-grid,
        .mission-card,
        .value-card,
        .education-item,
        .about-final,
        .contacts-heading,
        .contact-card,
        .contacts-map,
        .news-card,
        .event-card,
        .achievement-card
    `);

    if ("IntersectionObserver" in window) {
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("is-visible");
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12 });

        animatedElements.forEach((element, index) => {
            element.classList.add("scroll-reveal");

            if (
                element.classList.contains("stat-card") ||
                element.classList.contains("info-card")
            ) {
                element.style.transitionDelay =
                    `${(index % 4) * 100}ms`;
            }

            observer.observe(element);
        });
    } else {
        animatedElements.forEach(element => {
            element.classList.add("is-visible");
        });
    }


    // =================================
    // BUTTON RIPPLE EFFECT
    // =================================

    document.querySelectorAll(".hero-main-btn").forEach(button => {
        button.addEventListener("click", function () {
            button.classList.add("button-clicked");

            setTimeout(() => {
                button.classList.remove("button-clicked");
            }, 300);
        });
    });


    // =================================
    // HEADER SCROLL EFFECT
    // =================================

    const header = document.querySelector(".modern-header");

    if (header) {
        window.addEventListener("scroll", function () {
            header.classList.toggle(
                "header-scrolled",
                window.scrollY > 40
            );
        }, { passive: true });
    }


    // =================================
    // GALLERY LIGHTBOX
    // =================================

    const galleryLightbox =
        document.getElementById("galleryLightbox");

    const lightboxImage =
        document.getElementById("lightboxImage");

    const lightboxClose =
        document.getElementById("lightboxClose");

    const galleryImages =
        Array.from(document.querySelectorAll(".gallery-open"));

    if (
        galleryLightbox &&
        lightboxImage &&
        lightboxClose &&
        galleryImages.length > 0
    ) {

        let currentImageIndex = 0;

        // Навигация баскычтарын түзүү
        const previousButton = document.createElement("button");
        previousButton.className = "lightbox-prev";
        previousButton.innerHTML = "&#10094;";
        previousButton.setAttribute("aria-label", "Мурунку сүрөт");

        const nextButton = document.createElement("button");
        nextButton.className = "lightbox-next";
        nextButton.innerHTML = "&#10095;";
        nextButton.setAttribute("aria-label", "Кийинки сүрөт");

        galleryLightbox.appendChild(previousButton);
        galleryLightbox.appendChild(nextButton);


        // Сүрөттү көрсөтүү
        function showImage(index) {
            currentImageIndex =
                (index + galleryImages.length) % galleryImages.length;

            const selectedImage = galleryImages[currentImageIndex];

            lightboxImage.src = selectedImage.src;
            lightboxImage.alt = selectedImage.alt;

            galleryLightbox.classList.add("active");
            document.body.classList.add("lightbox-open");
        }


        // Галереядагы сүрөттү басуу
        galleryImages.forEach((image, index) => {
            image.style.cursor = "pointer";

            image.addEventListener("click", function () {
                showImage(index);
            });
        });


        // Кийинки сүрөт
        nextButton.addEventListener("click", function (event) {
            event.stopPropagation();
            showImage(currentImageIndex + 1);
        });


        // Мурунку сүрөт
        previousButton.addEventListener("click", function (event) {
            event.stopPropagation();
            showImage(currentImageIndex - 1);
        });


        // Жабуу
        function closeLightbox() {
            galleryLightbox.classList.remove("active");
            document.body.classList.remove("lightbox-open");
            lightboxImage.src = "";
        }

        lightboxClose.addEventListener("click", closeLightbox);

        galleryLightbox.addEventListener("click", function (event) {
            if (event.target === galleryLightbox) {
                closeLightbox();
            }
        });


        // Клавиатура менен башкаруу
        document.addEventListener("keydown", function (event) {

            if (!galleryLightbox.classList.contains("active")) return;

            if (event.key === "Escape") {
                closeLightbox();
            }

            if (event.key === "ArrowRight") {
                showImage(currentImageIndex + 1);
            }

            if (event.key === "ArrowLeft") {
                showImage(currentImageIndex - 1);
            }
        });
    }


    // =================================
    // ANIMATED STATISTICS COUNTER
    // =================================

    const statNumbers = document.querySelectorAll(".stat-number");

    const animateCounter = (element) => {
        const target = Number(element.textContent.trim());

        if (!Number.isFinite(target) || target <= 0) return;

        const duration = 1800;
        const startTime = performance.now();

        const updateCounter = (currentTime) => {
            const progress = Math.min(
                (currentTime - startTime) / duration,
                1
            );

            const easedProgress = 1 - Math.pow(1 - progress, 4);

            const currentNumber = Math.floor(
                target * easedProgress
            );

            element.textContent =
                currentNumber.toLocaleString("ru-RU");

            if (progress < 1) {
                requestAnimationFrame(updateCounter);
            } else {
                element.textContent =
                    target.toLocaleString("ru-RU");
            }
        };

        requestAnimationFrame(updateCounter);
    };

    if ("IntersectionObserver" in window) {
        const statsObserver = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounter(entry.target);
                    statsObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.7 });

        statNumbers.forEach(number => {
            statsObserver.observe(number);
        });
    }

});


// =================================
// WEBSITE PRELOADER
// =================================

const preloader = document.getElementById("sitePreloader");

if (preloader) {

    const hidePreloader = () => {
        preloader.classList.add("hide");
    };

    if (document.readyState === "complete") {
        setTimeout(hidePreloader, 400);
    } else {
        window.addEventListener("load", () => {
            setTimeout(hidePreloader, 400);
        });
    }

    setTimeout(hidePreloader, 4000);
}