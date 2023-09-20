
// Select all images with the lazy class
const images = document.querySelectorAll('.lazy');

// Create a new Intersection Observer
const observer = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      // Replace the src attribute with the data-src attribute
      entry.target.src = entry.target.dataset.src;
      // Stop observing the image
      observer.unobserve(entry.target);
    }
  });
});

// Start observing each image
images.forEach(image => {
  observer.observe(image);
});
