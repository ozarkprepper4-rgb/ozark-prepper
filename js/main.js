// Mobile menu toggle
function toggleMenu() {
  const menu = document.getElementById('mobile-menu');
  menu.classList.toggle('open');
}

// Close mobile menu when clicking a link
document.addEventListener('DOMContentLoaded', function() {
  const links = document.querySelectorAll('.mobile-menu a');
  links.forEach(link => {
    link.addEventListener('click', function() {
      document.getElementById('mobile-menu').classList.remove('open');
    });
  });
});
