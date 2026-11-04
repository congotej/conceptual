(function () {
  var root = document.documentElement;

  // Language (EN / ES)
  function setLang(l) {
    root.setAttribute('data-lang', l);
    root.lang = l;
    document.querySelectorAll('.lang button').forEach(function (b) {
      b.setAttribute('aria-pressed', String(b.dataset.set === l));
    });
    document.querySelectorAll('option[data-en]').forEach(function (o) { o.textContent = o.dataset[l]; });
    document.querySelectorAll('[data-ph-en]').forEach(function (i) { i.placeholder = i.dataset['ph' + (l === 'es' ? 'Es' : 'En')]; });
    try { localStorage.setItem('ci-lang', l); } catch (e) {}
  }
  var saved = null;
  try { saved = localStorage.getItem('ci-lang'); } catch (e) {}
  if (!saved) saved = (navigator.language || 'en').toLowerCase().indexOf('es') === 0 ? 'es' : 'en';
  setLang(saved);
  document.querySelectorAll('.lang button').forEach(function (b) {
    b.addEventListener('click', function () { setLang(b.dataset.set); });
  });

  // Mobile: hide the sticky consultation bar while the hero's own buttons are on screen, and on the contact page
  var bar = document.querySelector('.mobile-cta'), heroBtns = document.querySelector('.hero .btns');
  if (bar && document.getElementById('inquiry')) bar.classList.add('away');
  else if (bar && heroBtns) {
    var sync = function () { bar.classList.toggle('away', heroBtns.getBoundingClientRect().bottom > 0); };
    sync();
    window.addEventListener('scroll', sync, { passive: true });
    window.addEventListener('resize', sync);
  }

  // Mobile menu
  var mb = document.getElementById('menu-btn'), nav = document.getElementById('site-nav');
  if (mb && nav) mb.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    mb.setAttribute('aria-expanded', String(open));
  });

  // Respect reduced motion for autoplaying video
  try {
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) {
      document.querySelectorAll('video[autoplay]').forEach(function (v) { v.removeAttribute('autoplay'); v.pause(); v.controls = true; });
    }
  } catch (e) {}

  // Portfolio filters
  var filters = document.querySelectorAll('.filters button');
  filters.forEach(function (b) {
    b.addEventListener('click', function () {
      var f = b.dataset.filter;
      filters.forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
      document.querySelectorAll('.filterable figure').forEach(function (fig) {
        fig.hidden = !(f === 'all' || fig.dataset.cat === f);
      });
    });
  });

  // Inquiry form
  var form = document.getElementById('inquiry'), status = document.getElementById('form-status');
  if (form && status) {
    var msg = function (en, es) {
      status.hidden = false;
      status.textContent = root.getAttribute('data-lang') === 'es' ? es : en;
    };
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = form.querySelector('#f-name'), email = form.querySelector('#f-email'),
          loc = form.querySelector('#f-location'), consent = form.querySelector('#f-consent');
      if (!name.value.trim() || !email.validity.valid || !email.value.trim() || !loc.value.trim()) {
        msg('Please add your name, a valid email and the project location.', 'Por favor agrega tu nombre, un correo válido y la ubicación del proyecto.');
        return;
      }
      if (!consent.checked) {
        msg('Please check the consent box so we can contact you.', 'Por favor marca la casilla de consentimiento para poder contactarte.');
        return;
      }
      var preview = /claude|anthropic|usercontent/.test(location.hostname) || location.protocol === 'file:';
      if (preview) {
        msg('Preview only: this form will send inquiries once the site is live.', 'Vista previa: este formulario enviará solicitudes cuando el sitio esté publicado.');
        return;
      }
      var fd = new FormData(form);
      var data = new URLSearchParams(fd).toString();
      // 1) Keep a copy in the Netlify dashboard (Forms → inquiry). Failure here does not block sending.
      fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: data }).catch(function () {});
      // 2) Email the inquiry straight to Claudia through FormSubmit.
      var services = fd.getAll('service').join(', ');
      var payload = {
        _subject: 'New inquiry from the website: ' + (fd.get('name') || ''),
        _template: 'table',
        _captcha: 'false',
        _replyto: fd.get('email') || '',
        Name: fd.get('name') || '',
        Email: fd.get('email') || '',
        Phone: fd.get('phone') || '',
        'Project location': fd.get('location') || '',
        Services: services,
        Timeline: fd.get('timeline') || '',
        Budget: fd.get('budget') || 'Prefer not to say',
        'Preferred contact': fd.get('contact_method') || '',
        Message: fd.get('message') || '',
        Language: root.getAttribute('data-lang') === 'es' ? 'Español' : 'English'
      };
      if (fd.get('company')) return; // honeypot filled: likely spam, drop silently
      fetch('https://formsubmit.co/ajax/clavegiraldo@hotmail.com', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify(payload)
      })
        .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (!res.ok || String(res.j && res.j.success) !== 'true') throw new Error('send failed');
          form.reset();
          msg('Thank you. Your inquiry was sent and we will be in touch soon.', 'Gracias. Tu solicitud fue enviada y te contactaremos pronto.');
        })
        .catch(function () {
          msg('The inquiry did not send. Please try again, or message us on Instagram @conceptualusa.', 'La solicitud no se envió. Inténtalo de nuevo o escríbenos por Instagram @conceptualusa.');
        });
    });
  }
})();
