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

  // Holiday Collection: selection list, lightbox, WhatsApp request (no prices on the page)
  var drawer = document.getElementById('hc-drawer');
  if (drawer) {
    var L = function () { return root.getAttribute('data-lang') === 'es' ? 'es' : 'en'; };
    var tx = function (en, es) { return L() === 'es' ? es : en; };
    var dec = function (s) { var e = document.createElement('textarea'); e.innerHTML = s; return e.value; };
    var cards = Array.prototype.slice.call(document.querySelectorAll('.hc-card'));
    var byCode = {}; cards.forEach(function (c) { byCode[c.dataset.code] = c; });
    var nm = function (code) { return dec(byCode[code].dataset[L()]); };
    var sel = {};
    try { sel = JSON.parse(localStorage.getItem('ci-holiday') || '{}') || {}; } catch (e) {}
    Object.keys(sel).forEach(function (k) { if (!byCode[k]) delete sel[k]; });
    var save = function () { try { localStorage.setItem('ci-holiday', JSON.stringify(sel)); } catch (e) {} };
    var shade = document.getElementById('hc-shade'), lb = document.getElementById('hc-lb'), body = document.getElementById('hc-dr-body');
    var nameIn = document.getElementById('hc-name'), wa = document.getElementById('hc-wa'), toast = document.getElementById('hc-toast');
    var cur = null;
    if (bar) bar.classList.add('away');

    var message = function () {
      var n = nameIn.value.trim(), lines = Object.keys(sel).map(function (k) { return '• ' + k + ' — ' + nm(k) + ' × ' + sel[k]; });
      return tx('Hi Conceptual! ' + (n ? 'This is ' + n + '. ' : '') + "I'd like pricing and availability for these pieces from the Holiday Collection:\n\n",
                '¡Hola Conceptual! ' + (n ? 'Soy ' + n + '. ' : '') + 'Me gustaría saber precios y disponibilidad de estas piezas de la Colección Navideña:\n\n')
        + lines.join('\n') + tx('\n\nThank you!', '\n\n¡Gracias!');
    };
    var render = function () {
      var ks = Object.keys(sel);
      document.querySelectorAll('.hc-count').forEach(function (c) { c.textContent = ks.length; });
      document.querySelectorAll('.hc-add').forEach(function (b) {
        var on = !!sel[b.dataset.code]; b.classList.toggle('on', on);
        b.innerHTML = on ? '<span class="en">✓ Selected</span><span class="es">✓ Elegida</span>' : '<span class="en">+ Select</span><span class="es">+ Elegir</span>';
      });
      if (cur) document.getElementById('hc-lb-add').textContent = sel[cur.dataset.code] ? tx('✓ In your selection — remove', '✓ En tu selección — quitar') : tx('Add to selection', 'Agregar a mi selección');
      body.innerHTML = ks.length ? ks.map(function (k) {
        return '<div class="hc-row"><img src="' + byCode[k].querySelector('img').getAttribute('src') + '" alt=""><div><span class="hc-code">' + k + '</span><b>' + nm(k) + '</b></div>' +
          '<div class="hc-qty"><button type="button" data-q="-1" data-k="' + k + '" aria-label="−">−</button><span>' + sel[k] + '</span><button type="button" data-q="1" data-k="' + k + '" aria-label="+">+</button></div>' +
          '<button type="button" class="hc-x" data-rm="' + k + '" aria-label="Remove">×</button></div>';
      }).join('') : '<p class="hc-empty">' + tx('Nothing selected yet. Tap “+ Select” on any piece.', 'Aún no has elegido nada. Toca “+ Elegir” en cualquier pieza.') + '</p>';
      wa.href = 'https://wa.me/17542456323?text=' + encodeURIComponent(message());
    };
    var toggle = function (k) { if (sel[k]) delete sel[k]; else sel[k] = 1; save(); render(); };
    var flash = function (en, es) { toast.textContent = tx(en, es); clearTimeout(flash.t); flash.t = setTimeout(function () { toast.textContent = ''; }, 4000); };
    var lock = function () { document.body.classList.toggle('hc-lock', !drawer.hidden || !lb.hidden); };
    var openSel = function () { drawer.hidden = false; shade.hidden = false; lock(); };
    var closeSel = function () { drawer.hidden = true; shade.hidden = true; lock(); };
    var visible = function () { return cards.filter(function (c) { return !c.closest('.hc-col').hidden; }); };
    var openLb = function (c) {
      cur = c;
      var img = document.getElementById('hc-lb-img'); img.src = c.querySelector('img').getAttribute('src'); img.alt = nm(c.dataset.code);
      document.getElementById('hc-lb-code').textContent = c.dataset.code;
      document.getElementById('hc-lb-name').textContent = nm(c.dataset.code);
      document.getElementById('hc-lb-desc').textContent = dec(c.dataset[L() === 'es' ? 'des' : 'den']);
      lb.hidden = false; lock(); render();
    };
    var closeLb = function () { lb.hidden = true; cur = null; lock(); };
    var step = function (d) { var v = visible(), i = v.indexOf(cur); openLb(v[(i + d + v.length) % v.length]); };

    document.querySelector('.hc-shop').addEventListener('click', function (e) {
      var ph = e.target.closest('.hc-ph'); if (ph) return openLb(ph.closest('.hc-card'));
      var a = e.target.closest('.hc-add'); if (a) return toggle(a.dataset.code);
      var f = e.target.closest('.hc-filters button');
      if (f) document.querySelectorAll('.hc-col').forEach(function (col) { col.hidden = !(f.dataset.filter === 'all' || col.dataset.col === f.dataset.filter); });
    });
    document.querySelectorAll('[data-open-sel]').forEach(function (b) { b.addEventListener('click', openSel); });
    document.querySelector('[data-close-sel]').addEventListener('click', closeSel);
    shade.addEventListener('click', closeSel);
    document.querySelector('[data-close-lb]').addEventListener('click', closeLb);
    lb.addEventListener('click', function (e) { if (e.target === lb) closeLb(); });
    lb.querySelector('.prev').addEventListener('click', function () { step(-1); });
    lb.querySelector('.next').addEventListener('click', function () { step(1); });
    document.getElementById('hc-lb-add').addEventListener('click', function () { toggle(cur.dataset.code); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { if (!lb.hidden) closeLb(); else if (!drawer.hidden) closeSel(); }
      if (!lb.hidden && e.key === 'ArrowRight') step(1);
      if (!lb.hidden && e.key === 'ArrowLeft') step(-1);
    });
    body.addEventListener('click', function (e) {
      var q = e.target.closest('[data-q]'); if (q) { sel[q.dataset.k] = Math.max(1, sel[q.dataset.k] + Number(q.dataset.q)); save(); render(); }
      var r = e.target.closest('[data-rm]'); if (r) { delete sel[r.dataset.rm]; save(); render(); }
    });
    nameIn.addEventListener('input', render);
    wa.addEventListener('click', function (e) { if (!Object.keys(sel).length) { e.preventDefault(); flash('Add at least one piece first.', 'Agrega al menos una pieza primero.'); } });
    document.getElementById('hc-copy').addEventListener('click', function () {
      if (!Object.keys(sel).length) return flash('Add at least one piece first.', 'Agrega al menos una pieza primero.');
      navigator.clipboard.writeText(message()).then(function () {
        flash('Copied. Paste it in a message to @conceptualusa or 754-245-6323.', 'Copiado. Pégalo en un mensaje a @conceptualusa o al 754-245-6323.');
      }, function () { flash('Could not copy. Please take a screenshot of your list.', 'No se pudo copiar. Toma una captura de tu lista.'); });
    });
    document.querySelectorAll('.lang button').forEach(function (b) { b.addEventListener('click', function () { if (cur) openLb(cur); else render(); }); });
    render();
  }

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
