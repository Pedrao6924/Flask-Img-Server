document.addEventListener("DOMContentLoaded", function () {
    const lazyImages = document.querySelectorAll("img[data-src]");

    const options = {
        root: null, // Use the viewport as the root
        rootMargin: "0px", // No margin around the root
        threshold: 0.1, // Trigger the callback when 10% of the image is visible
    };

    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                const img = entry.target;
                const src = img.getAttribute("data-src");

                // Load the image
                img.setAttribute("src", src);
                img.removeAttribute("data-src");

                // Stop observing the image once it's loaded
                imageObserver.unobserve(img);
            }
        });
    }, options);

    // Observe each lazy-loaded image
    lazyImages.forEach((img) => {
        imageObserver.observe(img);
    });
});
