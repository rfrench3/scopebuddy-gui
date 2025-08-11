// Image Modal Script
document.addEventListener('DOMContentLoaded', function() {
  // Add click event listeners to all images in image galleries
  const galleryImages = document.querySelectorAll('.image-gallery img');
  const modal = new bootstrap.Modal(document.getElementById('imageModal'));
  const modalImage = document.getElementById('modalImage');
  const modalTitle = document.getElementById('imageModalLabel');
  const prevBtn = document.getElementById('prevImageBtn');
  const nextBtn = document.getElementById('nextImageBtn');
  
  let currentGalleryImages = [];
  let currentImageIndex = 0;
  
  function updateModal(index) {
    if (currentGalleryImages[index]) {
      modalImage.src = currentGalleryImages[index].src;
      modalImage.alt = currentGalleryImages[index].alt;
      modalTitle.textContent = currentGalleryImages[index].alt || 'Image Preview';
      
      // Update button visibility
      prevBtn.style.display = index > 0 ? 'block' : 'none';
      nextBtn.style.display = index < currentGalleryImages.length - 1 ? 'block' : 'none';
    }
  }
  
  function showPrevImage() {
    if (currentImageIndex > 0) {
      currentImageIndex--;
      updateModal(currentImageIndex);
    }
  }
  
  function showNextImage() {
    if (currentImageIndex < currentGalleryImages.length - 1) {
      currentImageIndex++;
      updateModal(currentImageIndex);
    }
  }
  
  // Add event listeners to navigation buttons
  prevBtn.addEventListener('click', showPrevImage);
  nextBtn.addEventListener('click', showNextImage);
  
  // Add keyboard navigation
  document.addEventListener('keydown', function(e) {
    if (modal._isShown) {
      if (e.key === 'ArrowLeft') {
        showPrevImage();
      } else if (e.key === 'ArrowRight') {
        showNextImage();
      }
    }
  });
  
  galleryImages.forEach(function(img) {
    img.style.cursor = 'pointer';
    img.addEventListener('click', function() {
      // Find the parent gallery and get all images in it
      const parentGallery = this.closest('.image-gallery');
      currentGalleryImages = Array.from(parentGallery.querySelectorAll('img'));
      currentImageIndex = currentGalleryImages.indexOf(this);
      
      updateModal(currentImageIndex);
      modal.show();
    });
  });
});

// RTL/LTR Auto-Detection Script
const rtlCss = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.rtl.min.css";
const ltrCss = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css";
const html = document.documentElement;
const bootstrapCss = document.getElementById('bootstrap-css');

// List of RTL language codes
const rtlLangs = [
  'ar', 'he', 'fa', 'ur', 'ps', 'syr', 'dv', 'ku', 'yi'
];

function isRtlLang(lang) {
  return rtlLangs.some(rtl => lang.toLowerCase().startsWith(rtl));
}

function setDirectionByLanguage(lang) {
  if (isRtlLang(lang)) {
    html.setAttribute('dir', 'rtl');
    bootstrapCss.setAttribute('href', rtlCss);
  } else {
    html.setAttribute('dir', 'ltr');
    bootstrapCss.setAttribute('href', ltrCss);
  }
  html.setAttribute('lang', lang);
}

// On page load, auto-detect
setDirectionByLanguage(navigator.language || navigator.userLanguage);

// Detect language changes post-load (e.g., by translation tools)
let lastLang = html.getAttribute('lang') || (navigator.language || navigator.userLanguage);

const observer = new MutationObserver(() => {
  const currentLang = html.getAttribute('lang');
  if (currentLang && currentLang !== lastLang) {
    setDirectionByLanguage(currentLang);
    lastLang = currentLang;
  }
});

observer.observe(html, { attributes: true, attributeFilter: ['lang'] });
