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

// ---- Simulated secure checkout + PDF delivery (test) ----
function openCheckout(pdfFile, btnEl) {
  var btn = btnEl || document.querySelector('.buy-btn');
  if (!btn) return;
  btn.disabled = true;
  btn.textContent = 'Opening secure checkout\u2026';
  var overlay = document.getElementById('checkout-overlay');
  if (!overlay) { window.location.hash = '#'; return; }
  overlay.style.display = 'flex';
  var price = overlay.querySelector('.checkout-price');
  if (price) price.textContent = 'Emergency Checklist \u2014 $4.99 (test)';
  var payBtn = overlay.querySelector('.checkout-pay');
  if (payBtn) { payBtn.dataset.pdf = pdfFile; payBtn.disabled = false; payBtn.textContent = 'Pay $4.99'; }
  var msg = overlay.querySelector('.checkout-msg');
  if (msg) msg.textContent = 'Verifying payment gateway\u2026';
}

function payCheckout(pdfFile) {
  var overlay = document.getElementById('checkout-overlay');
  if (!overlay) return;
  var payBtn = overlay.querySelector('.checkout-pay');
  var msg = overlay.querySelector('.checkout-msg');
  if (payBtn) { payBtn.disabled = true; payBtn.textContent = 'Processing secure payment\u2026'; }
  if (msg) { msg.textContent = 'Processing secure payment\u2026'; msg.className = 'checkout-msg processing'; }
  setTimeout(function() {
    if (msg) { msg.textContent = 'Payment received \u2705 \u2014 delivering your checklist now.'; msg.className = 'checkout-msg success'; }
    var a = document.createElement('a');
    a.href = pdfFile;
    a.download = pdfFile;
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(function() { var ov = document.getElementById('checkout-overlay'); if (ov) ov.style.display = 'none'; }, 2600);
  }, 1400);
}

// ---- Email capture form (newsletter signup) ----
document.addEventListener('DOMContentLoaded', function() {
  var form = document.getElementById('email-capture-form');
  if (!form) return;
  form.addEventListener('submit', function(e) {
    e.preventDefault();
    var btn = form.querySelector('button[type="submit"]');
    var status = document.getElementById('ec-status');
    if (!status) return;
    btn.disabled = true;
    btn.textContent = 'Sending\u2026';
    status.textContent = 'Sending\u2026';
    var data = new FormData(form);
    fetch(form.action, {
      method: 'POST',
      body: data,
      headers: { 'Accept': 'application/json' }
    }).then(function() {
      status.textContent = 'Thanks for subscribing! Your free guide is on its way.';
      status.className = 'ec-status success';
      form.reset();
      btn.disabled = false;
      btn.textContent = 'Subscribe & Get Your Guide';
      setTimeout(function() { if (status) status.textContent = ''; }, 6000);
    }).catch(function() {
      status.textContent = 'Something went wrong. Please try again.';
      status.className = 'ec-status error';
      btn.disabled = false;
      btn.textContent = 'Subscribe & Get Your Guide';
    });
  });
});
