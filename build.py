#!/usr/bin/env python3
"""Builds the Conceptual Interiors static site into ./dist (deploy) and ./preview (artifact)."""
import os, re, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
PREV = os.path.join(ROOT, "preview")

def t(en, es, tag="span"):
    return f'<{tag} class="en">{en}</{tag}><{tag} class="es">{es}</{tag}>'

NAV = [
    ("index.html", "Home", "Inicio"),
    ("window-treatments.html", "Window Treatments", "Cortinas y persianas"),
    ("interior-design.html", "Interior Design", "Diseño interior"),
    ("portfolio.html", "Portfolio", "Portafolio"),
    ("about.html", "About", "Nosotros"),
    ("contact.html", "Contact", "Contacto"),
]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@300;400&display=swap">')

def header(active):
    links = "\n".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t(en, es)}</a>'
        for h, en, es in NAV[1:])
    return f'''<header class="site-head">
  <div class="wrap head-row">
    <a class="logo" href="index.html" aria-label="Conceptual Interiors, home">
      <img class="mark" src="brand/logo-mark.svg" alt="" width="60" height="33">
      <span class="word"><b>CONCEPTUAL</b><span>INTERIORS</span></span>
    </a>
    <nav class="nav" id="site-nav" aria-label="Main">
{links}
    </nav>
    <div class="head-tools">
      <div class="lang" role="group" aria-label="Language">
        <button type="button" id="lang-en" data-set="en" aria-pressed="true">EN</button>
        <button type="button" id="lang-es" data-set="es" aria-pressed="false">ES</button>
      </div>
      <a class="btn solid head-cta" href="contact.html">{t("Schedule a consultation", "Agenda una consulta")}</a>
      <button class="menu-btn" type="button" id="menu-btn" aria-expanded="false" aria-controls="site-nav">{t("Menu", "Menú")}</button>
    </div>
  </div>
</header>'''

FOOTER = f'''<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a href="index.html" aria-label="Conceptual Interiors, home"><img class="lockup" src="brand/logo-lockup.svg" alt="Conceptual Interiors" width="182" height="140"></a>
        <p class="foot-tag">{t("Thoughtfully designed.<br>Beautifully lived.", "Pensado con detalle.<br>Hecho para vivirse.")}</p>
      </div>
      <div>
        <h4>{t("Window treatments", "Cortinas")}</h4>
        <ul>
          <li><a href="window-treatments.html#drapery">{t("Custom drapery", "Cortinas a la medida")}</a></li>
          <li><a href="window-treatments.html#sheers">{t("Sheer curtains", "Velos")}</a></li>
          <li><a href="window-treatments.html#shades">{t("Shades &amp; blackout", "Persianas y blackout")}</a></li>
          <li><a href="window-treatments.html#motorization">{t("Motorization", "Motorización")}</a></li>
        </ul>
      </div>
      <div>
        <h4>{t("Studio", "Estudio")}</h4>
        <ul>
          <li><a href="interior-design.html">{t("Interior design", "Diseño interior")}</a></li>
          <li><a href="portfolio.html">{t("Portfolio", "Portafolio")}</a></li>
          <li><a href="about.html">{t("About", "Nosotros")}</a></li>
        </ul>
      </div>
      <div>
        <h4>{t("Contact", "Contacto")}</h4>
        <ul>
          <li><a href="contact.html">{t("Schedule a consultation", "Agenda una consulta")}</a></li>
          <li><a href="https://www.instagram.com/conceptualusa/" target="_blank" rel="noopener">Instagram @conceptualusa</a></li>
          <li><a href="https://www.instagram.com/conceptualfurniture/" target="_blank" rel="noopener">{t("Partner studio", "Estudio aliado")} @conceptualfurniture</a></li>
          <li><a href="tel:+17542456323">754-245-6323</a></li>
          <li><a href="https://wa.me/17542456323" target="_blank" rel="noopener">WhatsApp</a></li>
          <li><a href="mailto:clavegiraldo@hotmail.com">clavegiraldo@hotmail.com</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-base">
      <span>© 2026 Conceptual Interiors</span>
      <span>{t("Custom window treatments &amp; interior design", "Cortinas a la medida y diseño interior")}</span>
    </div>
  </div>
</footer>
<div class="mobile-cta"><a class="btn solid" href="contact.html">{t("Schedule a consultation", "Agenda una consulta")}</a></div>'''

SITE = "https://conceptualusa.com/"
SCRIPT = '<script src="site.js"></script>'

SCHEMA = """
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"HomeAndConstructionBusiness","name":"Conceptual Interiors",
"description":"Custom window treatments and interior design: drapery, sheers, blackout, shades, motorization, furnishings and seasonal styling.",
"telephone":"+1-754-245-6323","email":"clavegiraldo@hotmail.com",
"url":"https://conceptualusa.com/","logo":"https://conceptualusa.com/brand/icon-512.png","image":"https://conceptualusa.com/img/inst13-hero.jpg",
"founder":{"@type":"Person","name":"Claudia Vélez"},
"areaServed":["South Florida","Orlando"],"knowsLanguage":["en","es"],
"sameAs":["https://www.instagram.com/conceptualusa/"]}
</script>"""

def page(fname, title, desc, body):
    url = SITE + ("" if fname == "index.html" else fname)
    head = (f'<title>{title}</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'
            f'<meta name="description" content="{desc}">\n'
            f'<link rel="canonical" href="{url}">\n'
            f'<meta property="og:type" content="website"><meta property="og:site_name" content="Conceptual Interiors">'
            f'<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">'
            f'<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}img/inst13-hero.jpg">'
            f'<meta name="twitter:card" content="summary_large_image">\n'
            '<link rel="icon" href="brand/favicon-32.png" sizes="32x32"><link rel="icon" href="brand/logo-full.svg" type="image/svg+xml">'
            '<link rel="apple-touch-icon" href="brand/apple-touch-icon.png">\n'
            f'{FONTS}\n<link rel="stylesheet" href="styles.css">'
            + (SCHEMA if fname == "index.html" else ""))
    content = f'{header(fname)}\n<main id="main">\n{body}\n</main>\n{FOOTER}\n{SCRIPT}'
    full = (f'<!doctype html>\n<html lang="en" data-lang="en">\n<head>\n<meta charset="utf-8">\n'
            f'<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n{head}\n</head>\n'
            f'<body>\n{content}\n</body>\n</html>\n')
    return full, f'{head}\n{content}\n'

def ph(src, alt, pos=None):
    st = f' style="object-position:{pos}"' if pos else ""
    return f'<div class="ph"><img src="img/{src}" alt="{alt}" loading="lazy"{st}></div>'

def cta_band():
    return f'''<section class="cta-band">
  <div class="wrap stack">
    <div class="label">{t("Begin your project", "Empieza tu proyecto")}</div>
    <h2>{t("Every detail, considered from the first visit.", "Cada detalle, pensado desde la primera visita.")}</h2>
    <p>{t("Tell us about your space and we'll arrange a time to visit, measure and bring samples.", "Cuéntanos de tu espacio y coordinamos una visita para medir y llevar muestras.")}</p>
    <div class="btns"><a class="btn solid" href="contact.html">{t("Schedule a consultation", "Agenda una consulta")}</a></div>
  </div>
</section>'''

PROCESS = f'''<ol class="steps">
  <li>{ph("dsc00593.jpg", "Designer sketching window notes in a notebook")}
    <div class="n">{t("Consult", "Consulta")}</div>
    <h3>{t("Walk the space", "Recorremos el espacio")}</h3>
    <p>{t("We look at the light, the views and how you live in each room.", "Vemos la luz, las vistas y cómo vives cada espacio.")}</p></li>
  <li>{ph("measure-window-v2.jpg", "Claudia measuring a sliding glass door with a tape measure", "52% 50%")}
    <div class="n">{t("Measure", "Medición")}</div>
    <h3>{t("Measure precisely", "Medimos con precisión")}</h3>
    <p>{t("Every opening, ceiling height and clearance is recorded before anything is ordered.", "Cada vano, altura y espacio libre se registra antes de pedir cualquier cosa.")}</p></li>
  <li>{ph("dsc00664.jpg", "Designer turning through fabric samples at a table")}
    <div class="n">{t("Select", "Selección")}</div>
    <h3>{t("Choose the fabric", "Elegimos la tela")}</h3>
    <p>{t("See and feel real samples, from airy sheers to full blackout, in your own light.", "Ves y tocas las muestras reales, de velos ligeros a blackout total, con la luz de tu casa.")}</p></li>
  <li>{ph("inst03.jpg", "Designer dressing the folds of a newly installed linen drape", "50% 35%")}
    <div class="n">{t("Install", "Instalación")}</div>
    <h3>{t("Install &amp; finish", "Instalamos y terminamos")}</h3>
    <p>{t("Every panel is hung, dressed and checked before we hand the room back to you.", "Cada panel se instala, se acomoda y se revisa antes de entregarte el espacio.")}</p></li>
</ol>'''

# ---------------- HOME ----------------
home = f'''<section class="hero">
  <div class="hero-grid">
    <div class="hero-copy">
      <div class="label">{t("Thoughtfully designed. Beautifully lived.", "Pensado con detalle. Hecho para vivirse.")}</div>
      <h1>{t("Custom window treatments, thoughtfully designed for your space.", "Cortinas a la medida, pensadas para tu espacio.")}</h1>
      <p class="lede">{t("From fabric selection to installation, every detail is considered.", "Desde la selección de la tela hasta la instalación, cada detalle está pensado.")}</p>
      <div class="label">{t("Over 20 years in South Florida", "Más de 20 años en el Sur de la Florida")}</div>
      <div class="btns">
        <a class="btn solid" href="contact.html">{t("Schedule a consultation", "Agenda una consulta")}</a>
        <a class="btn line" href="portfolio.html">{t("Explore our work", "Ver nuestro trabajo")}</a>
      </div>
    </div>
    <div class="hero-media"><img src="img/inst13-hero.jpg" alt="Double-height window dressed in floor-to-ceiling linen sheers" fetchpriority="high"></div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <div class="stack">
        <div class="label">{t("Services", "Servicios")}</div>
        <h2>{t("Window treatments first. The whole room when you need it.", "Primero las ventanas. Todo el espacio cuando lo necesites.")}</h2>
      </div>
    </div>
    <div class="feature-grid">
      <a class="card lead" href="window-treatments.html">
        {ph("inst14.jpg", "Floor-to-ceiling linen sheers across a double-height window")}
        <div class="label">{t("Our specialty", "Nuestra especialidad")}</div>
        <h3>{t("Custom window treatments", "Cortinas a la medida")}</h3>
        <p>{t("Drapery, sheers, blackout, Roman and roller shades, and motorization, measured and installed by our team.", "Cortinas, velos, blackout, persianas romanas y enrollables, y motorización, medidas e instaladas por nuestro equipo.")}</p>
        <span class="textlink">{t("Window treatments", "Ver cortinas")}</span>
      </a>
      <div class="feature-side">
        <a class="card small" href="interior-design.html">
          {ph("orl-dining.jpg", "Oak dining table with boucle chairs under a globe chandelier, opening onto the living room", "50% 62%")}
          <div class="stack" style="gap:12px">
            <h3>{t("Interior design &amp; furnishings", "Diseño interior y mobiliario")}</h3>
            <p>{t("Design direction, furniture and curated sourcing for a single room or a whole home.", "Dirección de diseño, mobiliario y selección de piezas para un espacio o la casa completa.")}</p>
            <span class="textlink">{t("Design services", "Ver diseño")}</span>
          </div>
        </a>
        <a class="card small" href="interior-design.html#seasonal">
          {ph("xmas-dress11.jpg", "Two designers dressing a Christmas tree in gold ornaments and dried florals", "50% 55%")}
          <div class="stack" style="gap:12px">
            <h3>{t("Seasonal styling", "Decoración de temporada")}</h3>
            <p>{t("Holiday décor designed and installed in your home, from the tree to the table.", "Decoración navideña diseñada e instalada en tu casa, del árbol a la mesa.")}</p>
            <span class="textlink">{t("A Conceptual Christmas", "Una Navidad Conceptual")}</span>
          </div>
        </a>
      </div>
    </div>
  </div>
</section>

<section class="sand">
  <div class="wrap">
    <div class="sec-head">
      <div class="stack">
        <div class="label">{t("Portfolio", "Portafolio")}</div>
        <h2>{t("Recent installations", "Instalaciones recientes")}</h2>
      </div>
      <a class="textlink" href="portfolio.html">{t("Explore our work", "Ver nuestro trabajo")}</a>
    </div>
    <div class="grid3">
      <figure>{ph("inst05.jpg", "Bedroom sheers filtering a view of palms")}<figcaption>{t("Sheers", "Velos")}</figcaption></figure>
      <figure>{ph("inst01.jpg", "Wall of taupe drapery closed for the evening")}<figcaption>{t("Drapery", "Cortinas")}</figcaption></figure>
      <figure>{ph("inst07.jpg", "Textured linen sheer hanging in even ripplefold waves")}<figcaption>{t("Ripplefold", "Ripplefold")}</figcaption></figure>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <figure class="vid wide">
      <video src="media/home-video.mp4" poster="media/home-video-poster.jpg" muted loop playsinline autoplay preload="metadata" aria-label="Remote closing a motorized linen sheer across a double-height window"></video>
    </figure>
    <div class="stack narrow">
      <div class="label">{t("Motorization", "Motorización")}</div>
      <h2>{t("Beautiful views, effortlessly controlled.", "Vistas hermosas, controladas sin esfuerzo.")}</h2>
      <p class="lede">{t("For tall windows and hard-to-reach tracks, quiet motorized systems open and close your drapery from a remote.", "Para ventanas altas y rieles difíciles de alcanzar, sistemas motorizados silenciosos abren y cierran tus cortinas desde un control remoto.")}</p>
      <div><a class="textlink" href="window-treatments.html#motorization">{t("About motorization", "Sobre la motorización")}</a></div>
    </div>
  </div>
</section>

<section class="sand">
  <div class="wrap">
    <div class="sec-head">
      <div class="stack">
        <div class="label">{t("Process", "Proceso")}</div>
        <h2>{t("From fabric selection to installation.", "De la selección de la tela a la instalación.")}</h2>
      </div>
    </div>
    {PROCESS}
  </div>
</section>

{cta_band()}'''

# ---------------- WINDOW TREATMENTS ----------------
def treat(id_, num, title_en, title_es, body_en, body_es, items, pics, one=False):
    lis = "".join(f"<li>{t(a, b)}</li>" for a, b in items)
    picshtml = "".join(pics)
    return f'''<article class="treat" id="{id_}">
  <div class="stack">
    <div class="num">{num}</div>
    <h2 style="font-size:clamp(1.9rem,3.4vw,2.6rem)">{t(title_en, title_es)}</h2>
    <p class="muted">{t(body_en, body_es)}</p>
    <ul>{lis}</ul>
  </div>
  <div class="pics{' one' if one else ''}">{picshtml}</div>
</article>'''

wt = f'''<section class="intro">
  <div class="wrap stack">
    <div class="label">{t("Window treatments", "Cortinas y persianas")}</div>
    <h1>{t("Custom window treatments, thoughtfully designed for your space.", "Cortinas a la medida, pensadas para tu espacio.")}</h1>
    <p class="lede">{t("Each treatment is specified for the window it hangs on: the light it lets in, the privacy it gives, and how it moves.", "Cada cortina se diseña para la ventana donde va: la luz que deja pasar, la privacidad que da y cómo se mueve.")}</p>
  </div>
</section>
<div class="banner"><img src="img/inst08.jpg" alt="Ceiling-mounted ripplefold track and linen sheers seen from below"></div>

<section style="padding-top:clamp(40px,6vw,72px)">
  <div class="wrap">
{treat("drapery", "01", "Custom drapery", "Cortinas a la medida",
       "Full-length drapery sewn to the exact height of your ceiling or track, in linens and textured weaves.",
       "Cortinas de largo completo confeccionadas a la altura exacta de tu techo o riel, en linos y tejidos con textura.",
       [("Ripplefold and pleated headings", "Cabezales ripplefold y plisados"), ("Ceiling and wall-mounted tracks", "Rieles de techo y de pared"), ("Lined or unlined", "Con o sin forro")],
       [ph("inst01.jpg", "Wall of taupe drapery closed for the evening"), ph("inst03.jpg", "Dressing the folds of a newly hung linen drape", "50% 35%")])}
{treat("sheers", "02", "Sheer curtains", "Velos",
       "Soft, filtered daylight and privacy without giving up the view.",
       "Luz suave y filtrada con privacidad, sin perder la vista.",
       [("Linen and linen-look sheers", "Velos de lino y tipo lino"), ("Layered with drapery or on their own", "Combinados con cortinas o solos"), ("Double-height and floor-to-ceiling", "Doble altura y de piso a techo")],
       [ph("inst16.jpg", "Claudia drawing back a floor-to-ceiling linen sheer", "50% 30%"), ph("inst10.jpg", "Looking up a tall linen sheer in afternoon light")])}
{treat("blackout", "03", "Blackout", "Blackout",
       "Room-darkening fabrics and linings for bedrooms, media rooms and anywhere you need full control of the light.",
       "Telas y forros oscurecedores para habitaciones, salas de cine y cualquier espacio donde necesites controlar la luz por completo.",
       [("Blackout drapery and linings", "Cortinas y forros blackout"), ("Blackout shades", "Persianas blackout"), ("Paired with sheers for day and night", "Combinadas con velos para el día y la noche")],
       [ph("inst09.jpg", "Taupe blackout drapery stacked against a ceiling track"), ph("inst06.jpg", "Blackout-lined drapery beside a sliding glass door")])}
{treat("shades", "04", "Roman &amp; roller shades", "Persianas romanas y enrollables",
       "Tailored shades for kitchens, bathrooms and windows where drapery doesn't fit.",
       "Persianas a la medida para cocinas, baños y ventanas donde una cortina no encaja.",
       [("Roman shades in soft fabrics", "Persianas romanas en telas suaves"), ("Roller, solar and blackout shades", "Enrollables, screen y blackout"), ("Inside or outside mount", "Instalación dentro o fuera del marco")],
       ['<div class="ph" style="aspect-ratio:4/5;max-width:440px"><img src="img/tw03.jpg" alt="Linen-texture roller shade in a ceiling pocket above a sliding glass door" loading="lazy"></div>'], one=True)}
{treat("motorization", "05", "Motorization", "Motorización",
       "Beautiful views, effortlessly controlled. Quiet motors open and close tall or hard-to-reach treatments from a remote.",
       "Vistas hermosas, controladas sin esfuerzo. Motores silenciosos abren y cierran cortinas altas o difíciles de alcanzar desde un control remoto.",
       [("Motorized drapery tracks and shades", "Rieles y persianas motorizadas"), ("Remote control with saved positions", "Control remoto con posiciones guardadas"), ("Ideal for double-height windows", "Ideal para ventanas de doble altura")],
       ['<figure class="vid wide" style="margin:0"><video src="media/home-video.mp4" poster="media/home-video-poster.jpg" muted loop playsinline autoplay preload="metadata" aria-label="Remote closing a motorized linen sheer across a double-height window"></video></figure>'], one=True)}
  </div>
</section>
{cta_band()}'''

# ---------------- INTERIOR DESIGN ----------------
idp = f'''<section class="intro">
  <div class="wrap stack">
    <div class="label">{t("Interior design &amp; furnishings", "Diseño interior y mobiliario")}</div>
    <h1>{t("Thoughtful interiors. Beautifully finished.", "Interiores pensados. Bellamente terminados.")}</h1>
    <p class="lede">{t("When a project needs more than the windows, we design the room around them: layout, furniture, finishing pieces and the details that make it feel lived in.", "Cuando un proyecto necesita más que las ventanas, diseñamos el espacio alrededor de ellas: distribución, mobiliario, piezas de acabado y los detalles que lo hacen sentir vivido.")}</p>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="grid3">
      <figure><div class="stack" style="gap:14px">{ph("orl15.jpg", "Open living area with boucle chairs, a round coffee table and oak slat screens")}
        <h3>{t("Design services", "Servicios de diseño")}</h3>
        <p class="muted">{t("Room planning, palette and material direction, from one room to a whole home.", "Planificación de espacios, paleta y dirección de materiales, de un espacio a la casa completa.")}</p></div></figure>
      <figure><div class="stack" style="gap:14px">{ph("dsc00725.jpg", "Claudia measuring a living room floor beside a boucle chair to plan the furniture layout", "45% 50%")}
        <h3>{t("Furnishings", "Mobiliario")}</h3>
        <p class="muted">{t("We measure each room to plan furniture that fits its scale, comfort and the way you use it, sourced through our partner studio, Conceptual Furniture.", "Medimos cada espacio para elegir muebles que encajen en su escala, su comodidad y la forma en que lo usas, a través de nuestro estudio aliado, Conceptual Furniture.")}</p></div></figure>
      <figure><div class="stack" style="gap:14px">{ph("orl25.jpg", "Lit shelving styled with ceramics beside a sculptural armchair")}
        <h3>{t("Styling &amp; curated sourcing", "Ambientación y selección de piezas")}</h3>
        <p class="muted">{t("The finishing layer: accessories, objects and arrangements sourced and placed for you.", "La última capa: accesorios, objetos y arreglos seleccionados y ubicados por nosotros.")}</p></div></figure>
    </div>
  </div>
</section>

<section class="sand" id="orlando">
  <div class="wrap split rev">
    <div class="media wide"><img src="img/orl13.jpg" alt="Living room with curved sofas, sculptural chairs and a wall of windows" loading="lazy"></div>
    <div class="stack narrow">
      <div class="label">{t("Featured project · Orlando", "Proyecto destacado · Orlando")}</div>
      <h2>{t("A warm modern home, furnished end to end.", "Un hogar moderno y cálido, amueblado de principio a fin.")}</h2>
      <p class="lede">{t("Living, dining and kitchen spaces designed by Conceptual and furnished with pieces from Conceptual Furniture: soft curved sofas, oak and natural textures in a quiet neutral palette.", "Sala, comedor y cocina diseñados por Conceptual y amueblados con piezas de Conceptual Furniture: sofás curvos y suaves, roble y texturas naturales en una paleta neutra y serena.")}</p>
      <div class="btns"><a class="textlink" href="portfolio.html#orlando">{t("See the project", "Ver el proyecto")}</a> <a class="textlink" href="https://www.instagram.com/conceptualfurniture/" target="_blank" rel="noopener">@conceptualfurniture</a></div>
    </div>
  </div>
</section>

<section id="renovations" style="padding-block:clamp(48px,7vw,88px) 0">
  <div class="wrap">
    <div class="stack narrow">
      <div class="label">{t("Renovations &amp; remodeling", "Remodelaciones y renovaciones")}</div>
      <p class="lede">{t("For renovations, additions and remodeling, we collaborate with <a href='https://www.lyconstructioninc.com' target='_blank' rel='noopener'>LY Construction, Inc.</a>, bringing interior design and construction together from concept to completion.", "Para remodelaciones, ampliaciones y renovaciones trabajamos junto a <a href='https://www.lyconstructioninc.com' target='_blank' rel='noopener'>LY Construction, Inc.</a>, uniendo el diseño interior y la construcción desde la idea hasta la entrega.")}</p>
    </div>
  </div>
</section>

<section id="furniture" style="padding-block:clamp(48px,7vw,88px)">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:0;align-items:center">
      <div class="stack">
        <div class="label">{t("Partner studio", "Estudio aliado")}</div>
        <h2 style="font-size:clamp(1.8rem,3.2vw,2.5rem)">Conceptual Furniture</h2>
        <p class="muted narrow">{t("Conceptual Furniture is our partner studio, with a concept store in Medellín, Colombia. For furnishing projects we source pieces through them. Sofas, dining, chairs and accent pieces are selected for each home and coordinated by our studio from order to delivery.", "Conceptual Furniture es nuestro estudio aliado, con su concept store en Medellín, Colombia. Para los proyectos de mobiliario seleccionamos piezas a través de ellos. Sofás, comedores, sillas y piezas decorativas se eligen para cada hogar y nuestro estudio coordina todo, del pedido a la entrega.")}</p>
      </div>
      <div class="btns"><a class="btn line" href="https://www.conceptual.com.co" target="_blank" rel="noopener">{t("See the collection", "Ver la colección")}</a><a class="textlink" href="https://www.instagram.com/conceptualfurniture/" target="_blank" rel="noopener">@conceptualfurniture</a></div>
    </div>
  </div>
</section>

<section id="seasonal">
  <div class="wrap split">
    <div class="stack narrow">
      <div class="label">{t("Seasonal styling", "Decoración de temporada")}</div>
      <h2>{t("A Conceptual Christmas.", "Una Navidad Conceptual.")}</h2>
      <p class="lede">{t("We design and install holiday décor in any style you have in mind, from classic to modern: the tree, garlands, the table and the mantel, ready for the season.", "Diseñamos e instalamos la decoración navideña en el estilo que imagines, de clásico a moderno: el árbol, las guirnaldas, la mesa y la repisa, listos para la temporada.")}</p>
      <p class="muted">{t("Booking for the holidays fills early. Reach out to reserve a date.", "La agenda de temporada se llena pronto. Escríbenos para reservar una fecha.")}</p>
      <div class="btns"><a class="btn solid" href="contact.html">{t("Reserve a holiday date", "Reserva tu fecha")}</a></div>
    </div>
    <figure class="vid">
      <video src="media/christmas.mp4" poster="media/christmas-poster.jpg" controls playsinline preload="none" aria-label="Video of a home being decorated for Christmas"></video>
      <figcaption>{t("Play with sound", "Reproducir con sonido")}</figcaption>
    </figure>
  </div>
</section>

<section>
  <div class="wrap grid4">
    <figure>{ph("xmas-dress11.jpg", "Dressing the tree in gold and bronze ornaments", "50% 55%")}</figure>
    <figure>{ph("xmas-41.jpg", "Lighting twisted beeswax candles on a brass candelabra", "40% 50%")}</figure>
    <figure>{ph("xmas-36.jpg", "Bowl of gilded ornaments and pine cones")}</figure>
    <figure>{ph("xmas-dress33.jpg", "Arranging cedar and pine in a carved wooden vessel")}</figure>
  </div>
</section>
{cta_band()}'''

# ---------------- PORTFOLIO ----------------
proj1 = [("inst14.jpg", "Double-height living room in linen sheers", "sheers"),
         ("inst13.jpg", "Designer at the base of a double-height sheer", "sheers"),
         ("inst16.jpg", "Drawing back a floor-to-ceiling linen sheer", "sheers"),
         ("inst05.jpg", "Bedroom sheers filtering a view of palms", "sheers"),
         ("inst01.jpg", "Wall of taupe drapery closed for the evening", "drapery"),
         ("inst07.jpg", "Textured linen sheer in ripplefold waves", "sheers"),
         ("inst09.jpg", "Taupe drapery stacked against a ceiling track", "drapery"),
         ("inst02.jpg", "Sheer drapery rising to a high ceiling track", "sheers"),
         ("inst03.jpg", "Dressing the folds of a newly hung drape", "drapery"),
         ("inst10.jpg", "Tall linen sheer in afternoon light", "sheers"),
         ("inst06.jpg", "Sheer drapery beside a sliding door and palms", "sheers"),
         ("inst11.jpg", "Single sheer panel stacked beside a three-pane window", "sheers"),
         ("inst12.jpg", "Linen sheer hem resting above the floor", "sheers"),
         ("inst15.jpg", "Remote controlling motorized sheers", "motorized"),
         ("inst04.jpg", "Motorization remote in front of a linen sheer", "motorized"),
         ("inst08.jpg", "Ceiling-mounted ripplefold track from below", "motorized")]
figs1 = "\n".join(f'<figure data-cat="{c}">{ph(s, a)}</figure>' for s, a, c in proj1)
proj2 = [("xmas-dress11.jpg", "Dressing the tree in gold and bronze ornaments"), ("xmas-36.jpg", "Bowl of gilded ornaments and pine cones"),
         ("xmas-41.jpg", "Beeswax candles on a brass candelabra"), ("xmas-4.jpg", "Placing a gilded ornament on the tree")]
figs2 = "\n".join(f'<figure data-cat="seasonal">{ph(s, a)}</figure>' for s, a in proj2)

proj3 = [("orl13.jpg", "Living room with curved sofas and a wall of windows"),
         ("orl-r2.jpg", "Curved linen sofas around a round oak coffee table"),
         ("orl14.jpg", "Oak dining table with upholstered chairs under a globe chandelier"),
         ("orl15.jpg", "Boucle chairs and round coffee table beside oak slat screens"),
         ("orl-r1.jpg", "Dining area opening to the garden"),
         ("orl17.jpg", "Channel-tufted sofas facing a lit oak media wall"),
         ("orl19.jpg", "Kitchen island with stone waterfall edge and wood stools"),
         ("orl23.jpg", "Oak media wall with lit display niches"),
         ("orl25.jpg", "Sculptural armchair beside lit shelving"),
         ("orl-r3.jpg", "Living room with curved sofas and floor lamp"),
         ("orl26.jpg", "Covered terrace with outdoor kitchen and dining"),
         ("orl01.jpg", "Long gallery hallway with skylights and gravel planter")]
figs3 = "\n".join(f'<figure>{ph(s, a)}</figure>' for s, a in proj3)

proj4 = [("tw07.jpg", "Double-height wall of glass dressed in floor-to-ceiling sheers", "sheers"),
         ("tw04.jpg", "Sheers seen over a glass stair rail", "sheers"),
         ("tw02.jpg", "Sheer drapery rising behind a floating staircase", "sheers"),
         ("tw03.jpg", "Roller shade in a ceiling pocket above a sliding door", "shades"),
         ("tw06.jpg", "Workroom team hemming sheers on site, seen from above", "install"),
         ("tw01.jpg", "Installers on scaffolding hanging double-height sheers", "install")]
figs4 = "\n".join(f'<figure>{ph(s, a)}</figure>' for s, a, c in proj4)

pf = f'''<section class="intro">
  <div class="wrap stack">
    <div class="label">{t("Portfolio", "Portafolio")}</div>
    <h1>{t("Real spaces, finished.", "Espacios reales, terminados.")}</h1>
    <p class="lede">{t("Recent projects, organized by space and treatment.", "Proyectos recientes, organizados por espacio y tipo de cortina.")}</p>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap project">
    <hr class="rule">
    <div class="sec-head" style="margin-bottom:0">
      <div class="stack">
        <h2>{t("Double-height residence", "Residencia de doble altura")}</h2>
        <p class="muted narrow">{t("Linen sheers for the day and taupe drapery for the night, on ceiling-mounted ripplefold tracks with motorization for the tallest windows.", "Velos de lino para el día y cortinas taupe para la noche, en rieles ripplefold de techo con motorización para las ventanas más altas.")}</p>
      </div>
      <dl class="project-meta">
        <div><dt>{t("Scope", "Alcance")}</dt><dd>{t("Sheers · Drapery · Motorization", "Velos · Cortinas · Motorización")}</dd></div>
      </dl>
    </div>
    <div class="filters" role="group" aria-label="Filter">
      <button type="button" id="f-all" data-filter="all" aria-pressed="true">{t("All", "Todo")}</button>
      <button type="button" id="f-sheers" data-filter="sheers" aria-pressed="false">{t("Sheers", "Velos")}</button>
      <button type="button" id="f-drapery" data-filter="drapery" aria-pressed="false">{t("Drapery", "Cortinas")}</button>
      <button type="button" id="f-motorized" data-filter="motorized" aria-pressed="false">{t("Motorized", "Motorizado")}</button>
    </div>
    <div class="grid3 filterable">
{figs1}
    </div>
    <div class="stack" style="margin-top:clamp(28px,4vw,48px)">
      <div class="label">{t("Installation day", "Día de instalación")}</div>
      <div class="grid3">
        <figure>{ph("install-track.jpg", "Installer on scaffolding mounting the ceiling track above a double-height window", "40% 30%")}<figcaption>{t("01 · Track", "01 · Riel")}</figcaption></figure>
        <figure>{ph("inst17.jpg", "Installer hooking a linen drape onto the ceiling track", "60% 50%")}<figcaption>{t("02 · Hanging", "02 · Instalación")}</figcaption></figure>
        <figure>{ph("inst16.jpg", "Dressing the folds of the finished sheer", "70% 50%")}<figcaption>{t("03 · Dressing", "03 · Acabado")}</figcaption></figure>
      </div>
    </div>
  </div>
</section>


<section id="pinecrest">
  <div class="wrap project">
    <hr class="rule">
    <div class="sec-head" style="margin-bottom:0">
      <div class="stack">
        <h2>{t("Pinecrest residence", "Residencia en Pinecrest")}</h2>
        <p class="muted narrow">{t("Floor-to-ceiling sheers across a two-story wall of glass, hemmed on site so every panel breaks evenly at the floor, with roller shades in the hallways.", "Velos de piso a techo en un muro de vidrio de dos pisos, con dobladillo hecho en sitio para que cada panel caiga parejo al piso, y persianas enrollables en los pasillos.")}</p>
      </div>
      <dl class="project-meta">
        <div><dt>{t("Scope", "Alcance")}</dt><dd>{t("Sheers · Roller shades", "Velos · Persianas enrollables")}</dd></div>
      </dl>
    </div>
    <div class="grid3">
{figs4}
    </div>
  </div>
</section>

<section id="orlando">
  <div class="wrap project">
    <hr class="rule">
    <div class="sec-head" style="margin-bottom:0">
      <div class="stack">
        <h2>{t("Orlando residence", "Residencia en Orlando")}</h2>
        <p class="muted narrow">{t("Interior design and furnishings for a single-story modern home: open living and dining, kitchen and covered terrace, furnished with pieces sourced through our partner studio, Conceptual Furniture.", "Diseño interior y mobiliario para una casa moderna de un piso: sala y comedor abiertos, cocina y terraza, amueblada con piezas seleccionadas a través de nuestro estudio aliado, Conceptual Furniture.")}</p>
      </div>
      <dl class="project-meta">
        <div><dt>{t("Scope", "Alcance")}</dt><dd>{t("Interior design · Furnishings", "Diseño interior · Mobiliario")}</dd></div>
        <div><dt>{t("Furniture", "Mobiliario")}</dt><dd><a href="https://www.instagram.com/conceptualfurniture/" target="_blank" rel="noopener">@conceptualfurniture</a></dd></div>
      </dl>
    </div>
    <div class="grid3">
{figs3}
    </div>
  </div>
</section>
<section class="sand">
  <div class="wrap project">
    <div class="sec-head" style="margin-bottom:0">
      <div class="stack">
        <h2>{t("A Conceptual Christmas", "Una Navidad Conceptual")}</h2>
        <p class="muted narrow">{t("Holiday styling in gold, bronze and natural greenery.", "Decoración navideña en dorado, bronce y follaje natural.")}</p>
      </div>
      <a class="textlink" href="interior-design.html#seasonal">{t("Watch the video", "Ver el video")}</a>
    </div>
    <div class="grid4">
{figs2}
    </div>
  </div>
</section>
{cta_band()}'''

# ---------------- ABOUT ----------------
ab = f'''<section class="intro">
  <div class="wrap stack">
    <div class="label">{t("About", "Nosotros")}</div>
    <h1>{t("Meet Claudia Vélez", "Conoce a Claudia Vélez")}</h1>
    <p class="lede">{t("Founder &amp; Interior Designer", "Fundadora y diseñadora de interiores")}</p>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap split">
    <div class="media">{'<img src="img/dsc00682.jpg" alt="Claudia Vélez reviewing fabric samples" style="object-position:45% 40%">'}</div>
    <div class="stack narrow">
      <p>{t("With over 20 years of experience in South Florida, Claudia Vélez brings a thoughtful, personalized approach to creating beautiful, functional living spaces.", "Con más de 20 años de experiencia en el Sur de la Florida, Claudia Vélez aporta una mirada cuidadosa y personalizada para crear espacios bellos y funcionales.")}</p>
      <p>{t("She specializes in custom window treatments: drapery, sheers, shades, blackout and motorized systems, chosen with a deep understanding of fabric, light and how each room is lived in. Beyond the windows, she designs and furnishes single rooms and entire homes, from space planning and furniture selection to finishes and decorative details.", "Se especializa en cortinas a la medida: cortinas, velos, persianas, blackout y sistemas motorizados, elegidos con un profundo conocimiento de las telas, la luz y la forma en que se vive cada espacio. Más allá de las ventanas, diseña y amuebla espacios individuales y casas completas, desde la distribución y la selección de muebles hasta los acabados y los detalles decorativos.")}</p>
      <p>{t("For renovations, additions and remodeling, Claudia collaborates with <a href='https://www.lyconstructioninc.com' target='_blank' rel='noopener'>LY Construction, Inc.</a>, bringing interior design and construction together from concept to completion.", "Para remodelaciones, ampliaciones y renovaciones, Claudia trabaja junto a <a href='https://www.lyconstructioninc.com' target='_blank' rel='noopener'>LY Construction, Inc.</a>, uniendo el diseño interior y la construcción desde la idea hasta la entrega.")}</p>
      <p class="quote">{t("“Every home should reflect the people who live in it.”", "“Cada hogar debe reflejar a las personas que lo habitan.”")}</p>
    </div>
  </div>
</section>
<section class="sand">
  <div class="wrap">
    <div class="grid3" style="align-items:start">
      <div class="stack"><div class="label">{t("Point of view", "Visión")}</div><h3>{t("Natural and architectural", "Natural y arquitectónico")}</h3><p class="muted">{t("Warm neutrals, real materials and light that changes through the day.", "Neutros cálidos, materiales reales y luz que cambia durante el día.")}</p></div>
      <div class="stack"><div class="label">{t("Craftsmanship", "Oficio")}</div><h3>{t("Made to measure", "Hecho a la medida")}</h3><p class="muted">{t("Every treatment is specified for its window, sewn to size and installed by our team.", "Cada cortina se diseña para su ventana, se confecciona a la medida y la instala nuestro equipo.")}</p></div>
      <div class="stack"><div class="label">{t("Service areas", "Zonas de servicio")}</div><h3>{t("South Florida &amp; Orlando", "Sur de la Florida y Orlando")}</h3><p class="muted">{t("We work in English and Spanish, with furniture sourced through our partner studio, Conceptual Furniture.", "Trabajamos en español e inglés, con mobiliario a través de nuestro estudio aliado, Conceptual Furniture.")}</p></div>
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="sec-head"><div class="stack"><div class="label">{t("Process", "Proceso")}</div><h2>{t("How we work", "Cómo trabajamos")}</h2></div></div>
    {PROCESS}
  </div>
</section>
{cta_band()}'''

# ---------------- CONTACT ----------------
def opt(v, en, es):
    return f'<option value="{v}" data-en="{en}" data-es="{es}">{en}</option>'

ct = f'''<section class="intro">
  <div class="wrap stack">
    <div class="label">{t("Contact", "Contacto")}</div>
    <h1>{t("Schedule a consultation", "Agenda una consulta")}</h1>
    <p class="lede">{t("Tell us a little about your project and we'll be in touch to arrange a visit.", "Cuéntanos un poco de tu proyecto y te contactaremos para coordinar una visita.")}</p>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap contact-grid">
    <aside class="contact-aside">
      <dl>
        <div><dt>{t("Phone", "Teléfono")}</dt><dd><a href="tel:+17542456323">754-245-6323</a></dd></div>
        <div><dt>WhatsApp</dt><dd><a href="https://wa.me/17542456323" target="_blank" rel="noopener">754-245-6323</a></dd></div>
        <div><dt>{t("Email", "Correo")}</dt><dd><a href="mailto:clavegiraldo@hotmail.com" style="word-break:break-all">clavegiraldo@hotmail.com</a></dd></div>
        <div><dt>Instagram</dt><dd><a href="https://www.instagram.com/conceptualusa/" target="_blank" rel="noopener">@conceptualusa</a></dd></div>
        <div><dt>{t("Service area", "Zona de servicio")}</dt><dd>{t("South Florida &amp; Orlando", "Sur de la Florida y Orlando")}</dd></div>
        <div><dt>{t("Languages", "Idiomas")}</dt><dd>English · Español</dd></div>
      </dl>
      <hr class="rule">
      <p class="muted" style="font-size:.92rem">{t("A photo of the room helps. You can send it by WhatsApp after you submit this form.", "Una foto del espacio ayuda. Puedes enviarla por WhatsApp después de enviar el formulario.")}</p>
    </aside>
    <form class="form" id="inquiry" name="inquiry" method="POST" data-netlify="true" netlify-honeypot="company" novalidate>
      <input type="hidden" name="form-name" value="inquiry">
      <p hidden><label>Leave empty <input name="company" id="company"></label></p>
      <div class="field"><label for="f-name">{t("Name", "Nombre")}</label><input id="f-name" name="name" autocomplete="name" required></div>
      <div class="field"><label for="f-email">{t("Email", "Correo")}</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
      <div class="field"><label for="f-phone">{t("Phone", "Teléfono")} <span class="opt">{t("(optional)", "(opcional)")}</span></label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
      <div class="field"><label for="f-location">{t("Project location", "Ubicación del proyecto")}</label><input id="f-location" name="location" placeholder="City / neighborhood" data-ph-en="City / neighborhood" data-ph-es="Ciudad / barrio" required></div>
      <fieldset class="field full">
        <legend>{t("Service", "Servicio")}</legend>
        <div class="choices">
          <label><input type="checkbox" id="s-wt" name="service" value="Window treatments" checked> {t("Window treatments", "Cortinas y persianas")}</label>
          <label><input type="checkbox" id="s-mo" name="service" value="Motorization"> {t("Motorization", "Motorización")}</label>
          <label><input type="checkbox" id="s-id" name="service" value="Interior design"> {t("Interior design", "Diseño interior")}</label>
          <label><input type="checkbox" id="s-fu" name="service" value="Furnishings"> {t("Furnishings", "Mobiliario")}</label>
          <label><input type="checkbox" id="s-se" name="service" value="Seasonal styling"> {t("Seasonal styling", "Decoración de temporada")}</label>
        </div>
      </fieldset>
      <div class="field"><label for="f-timeline">{t("Timeline", "Tiempo estimado")}</label>
        <select id="f-timeline" name="timeline" class="i18n-select">
          {opt("asap", "As soon as possible", "Lo antes posible")}
          {opt("1-3m", "Within 1–3 months", "En 1–3 meses")}
          {opt("3m+", "3+ months", "Más de 3 meses")}
          {opt("exploring", "Just exploring", "Solo explorando")}
        </select></div>
      <div class="field"><label for="f-budget">{t("Budget", "Presupuesto")} <span class="opt">{t("(optional)", "(opcional)")}</span></label>
        <select id="f-budget" name="budget" class="i18n-select">
          {opt("", "Prefer not to say", "Prefiero no decir")}
          {opt("under-5k", "Under $5,000", "Menos de $5,000")}
          {opt("5-15k", "$5,000–$15,000", "$5,000–$15,000")}
          {opt("15-40k", "$15,000–$40,000", "$15,000–$40,000")}
          {opt("40k+", "$40,000+", "Más de $40,000")}
        </select></div>
      <fieldset class="field full">
        <legend>{t("Preferred contact method", "Método de contacto preferido")}</legend>
        <div class="choices">
          <label><input type="radio" id="c-email" name="contact_method" value="Email" checked> {t("Email", "Correo")}</label>
          <label><input type="radio" id="c-phone" name="contact_method" value="Phone"> {t("Phone call", "Llamada")}</label>
          <label><input type="radio" id="c-wa" name="contact_method" value="WhatsApp"> WhatsApp</label>
        </div>
      </fieldset>
      <div class="field full"><label for="f-msg">{t("Tell us about your project", "Cuéntanos de tu proyecto")}</label><textarea id="f-msg" name="message"></textarea></div>
      <label class="consent full"><input type="checkbox" id="f-consent" name="consent" required> <span>{t("I agree to be contacted by Conceptual Interiors about this inquiry.", "Acepto que Conceptual Interiors me contacte sobre esta solicitud.")}</span></label>
      <div class="full btns"><button class="btn solid" type="submit">{t("Send inquiry", "Enviar solicitud")}</button></div>
      <p class="form-status full" id="form-status" role="status" hidden></p>
    </form>
  </div>
</section>'''

PAGES = [
    ("index.html", "Conceptual Interiors", "Custom window treatments, thoughtfully designed for your space. Drapery, sheers, shades and motorization in South Florida.", home),
    ("window-treatments.html", "Window Treatments · Conceptual Interiors", "Custom drapery, sheer curtains, blackout, Roman and roller shades, and motorization.", wt),
    ("interior-design.html", "Interior Design · Conceptual Interiors", "Interior design, furnishings, styling and seasonal holiday décor by Conceptual Interiors.", idp),
    ("portfolio.html", "Portfolio · Conceptual Interiors", "Recent window treatment and interior projects by Conceptual Interiors.", pf),
    ("about.html", "About · Conceptual Interiors", "Claudia Vélez, founder and designer of Conceptual Interiors.", ab),
    ("contact.html", "Contact · Conceptual Interiors", "Schedule a consultation with Conceptual Interiors.", ct),
]

for d in (DIST, PREV):
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d)
for fname, title, desc, body in PAGES:
    full, frag = page(fname, title, desc, body)
    open(os.path.join(DIST, fname), "w").write(full)
    open(os.path.join(PREV, fname), "w").write(frag if fname == "index.html" else full)
for d in (DIST, PREV):
    for f in ("styles.css", "site.js"):
        shutil.copy(os.path.join(ROOT, f), d)
    os.makedirs(os.path.join(d, "brand"))
    for f in ("logo-mark.svg", "logo-lockup.svg", "logo-full.svg", "favicon-32.png", "apple-touch-icon.png", "icon-512.png"):
        shutil.copy(os.path.join(ROOT, "brand", f), os.path.join(d, "brand", f))
    for sub in ("img", "media"):
        used = set()
        for fname, *_ in PAGES:
            used |= set(re.findall(rf'{sub}/([\w.-]+)', open(os.path.join(DIST, fname)).read()))
        os.makedirs(os.path.join(d, sub))
        for u in sorted(used):
            shutil.copy(os.path.join(ROOT, sub, u), os.path.join(d, sub, u))
from datetime import date
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for fname, *_ in PAGES:
    sm += f'  <url><loc>{SITE}{"" if fname == "index.html" else fname}</loc><lastmod>{date.today()}</lastmod></url>\n'
sm += '</urlset>\n'
open(os.path.join(DIST, "sitemap.xml"), "w").write(sm)
open(os.path.join(DIST, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
print("built", [p[0] for p in PAGES])
