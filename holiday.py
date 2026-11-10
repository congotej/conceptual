"""Holiday Collection page: items available by special order. No prices on the site — clients request them.
Images live in img/hol-cm-hNN.jpg. Item order fixes each piece's code (CM-H01 … CM-H50); add new items at the end."""

# (id, name EN, name ES, starting price shown on the page)
COLLECTIONS = [
    ("pinecone", "Pinecone Collection", "Colección de piñas", 10),
    ("glass", "Mercury &amp; Antique Glass", "Vidrio mercurio y antiguo", 9),
    ("natural", "Natural &amp; Gilded", "Natural y dorado", 8),
    ("bells", "Bells &amp; Drops", "Cascabeles y colgantes", 12),
    ("greenery", "Greenery &amp; Branches", "Follaje y ramas", 6),
]

# (collection, name EN, name ES, description EN, description ES, size EN, size ES)
ITEMS = [
    ("pinecone", "Burgundy Elongated Pinecone", "Piña alargada borgoña", "Deep wine scales with a metallic edge, hung on natural jute.", "Escamas color vino con borde metálico, colgada en yute natural.", "7.5\" H × 3.5\" dia", "7.5\" alto × 3.5\" diám."),
    ("pinecone", "Burgundy Pinecone", "Piña borgoña", "A fuller burgundy cone with shimmering tips.", "Piña borgoña más llena, con puntas brillantes.", "6.75\" H × 4.75\" dia", "6.75\" alto × 4.75\" diám."),
    ("pinecone", "Burgundy Pinecone Sphere", "Esfera de piña borgoña", "Round burgundy pinecone ornament, layered petals all around.", "Adorno redondo de piña borgoña, con pétalos en capas.", "5.5\" dia", "5.5\" diám."),
    ("pinecone", "Champagne Elongated Pinecone", "Piña alargada champaña", "Slim cone in soft champagne gold.", "Piña delgada en un suave dorado champaña.", "7.5\" H × 3.5\" dia", "7.5\" alto × 3.5\" diám."),
    ("pinecone", "Gold Pinecone", "Piña dorada", "Warm brushed-gold scales on a jute loop.", "Escamas en dorado cepillado, con colgador de yute.", "5.5\" H × 4\" dia", "5.5\" alto × 4\" diám."),
    ("pinecone", "Gold Tall Pinecone", "Piña dorada alta", "Taller gold cone with a natural, slightly rustic finish.", "Piña dorada más alta, con acabado natural y algo rústico.", "6.75\" H × 4.75\" dia", "6.75\" alto × 4.75\" diám."),
    ("pinecone", "Gold Pinecone Sphere", "Esfera de piña dorada", "Round gilded pinecone with glittered edges.", "Piña redonda dorada con bordes escarchados.", "4.25\" dia", "4.25\" diám."),
    ("pinecone", "Gold Pinecone Globe", "Globo de piña dorado", "Full round globe of golden pinecone scales.", "Globo redondo y lleno de escamas doradas.", "5.5\" dia", "5.5\" diám."),
    ("pinecone", "Bronze Pinecone", "Piña bronce", "Dark bronze cone with gold-touched tips.", "Piña en bronce oscuro con puntas doradas.", "5.5\" H × 4\" dia", "5.5\" alto × 4\" diám."),
    ("pinecone", "Bronze Tall Pinecone", "Piña bronce alta", "Elongated bronze cone, rich and earthy.", "Piña alargada en bronce, cálida y terrosa.", "6.75\" H × 4.75\" dia", "6.75\" alto × 4.75\" diám."),
    ("pinecone", "Bronze Pinecone Sphere", "Esfera de piña bronce", "Round bronze pinecone with metallic highlights.", "Piña redonda en bronce con destellos metálicos.", "4.25\" dia", "4.25\" diám."),
    ("pinecone", "Blush Bronze Petal Ball", "Bola de pétalos bronce rosado", "Dense blush-bronze petals for a softer, textured look.", "Pétalos en bronce rosado para un look suave y con textura.", "4.75\" dia", "4.75\" diám."),
    ("pinecone", "Iridescent Pinecone Ball", "Bola de piña iridiscente", "Natural pinecone petals with iridescent glitter, on chunky jute rope.", "Pétalos de piña natural con brillo iridiscente, con cuerda gruesa de yute.", "4.25\" dia", "4.25\" diám."),
    ("pinecone", "Iridescent Pinecone Globe", "Globo de piña iridiscente", "The iridescent pinecone ball in a larger size.", "La bola de piña iridiscente en un tamaño más grande.", "5.5\" dia", "5.5\" diám."),
    ("pinecone", "Iridescent Pinecone Icicle", "Carámbano de piña iridiscente", "Long pinecone-petal icicle with iridescent glitter.", "Carámbano largo de pétalos de piña con brillo iridiscente.", "12\" H", "12\" alto"),
    ("pinecone", "Natural Pod Icicle", "Carámbano de vainas naturales", "Layered natural pod sections forming a hanging icicle.", "Secciones de vainas naturales en capas, formando un carámbano colgante.", "12\" H", "12\" alto"),
    ("glass", "Champagne Rustic Glass Ornament", "Adorno de vidrio rústico champaña", "Matte champagne and brown glass in two shapes, ball and onion.", "Vidrio mate champaña y café en dos formas: bola y cebolla.", "4\" dia", "4\" diám."),
    ("glass", "Gold Thread Glass Ball", "Bola de vidrio con hilo dorado", "Clear glass wrapped in fine gold threadwork.", "Vidrio transparente envuelto en fino hilo dorado.", "4\" dia", "4\" diám."),
    ("glass", "Gold Thread Glass Globe", "Globo de vidrio con hilo dorado", "The gold-thread design in a bolder statement piece.", "El diseño de hilo dorado en una pieza protagonista.", "5\" dia", "5\" diám."),
    ("glass", "Silver Mercury Glass Ball", "Bola de vidrio mercurio plateada", "Classic speckled mercury glass with a silver cap.", "Clásico vidrio mercurio moteado con tapa plateada.", "4\" dia", "4\" diám."),
    ("glass", "Silver Mercury Glass Globe", "Globo de vidrio mercurio plateado", "Speckled silver mercury glass with a generous round profile.", "Vidrio mercurio plateado moteado, de silueta redonda y generosa.", "4.75\" dia", "4.75\" diám."),
    ("glass", "Rustic Green Glass Ball", "Bola de vidrio rústico verde", "Shiny glass in rustic green and white with an aged finish.", "Vidrio brillante en verde rústico y blanco, con acabado envejecido.", "5\" dia", "5\" diám."),
    ("glass", "Rustic Green Glass Globe", "Globo de vidrio rústico verde", "The rustic green and white glass in a larger statement size.", "El vidrio rústico verde y blanco en un tamaño protagonista.", "6\" dia", "6\" diám."),
    ("glass", "Silver &amp; White Glass Ball", "Bola de vidrio plata y blanco", "Silver and white glass with a vintage mercury look.", "Vidrio plata y blanco con look de mercurio vintage.", "4\" dia", "4\" diám."),
    ("glass", "Silver &amp; White Glass Globe", "Globo de vidrio plata y blanco", "The silver and white glass in a larger statement size.", "El vidrio plata y blanco en un tamaño protagonista.", "6\" dia", "6\" diám."),
    ("glass", "Copper Patina Glass Ball", "Bola de vidrio pátina cobre", "Textured antique glass in dusty copper and green.", "Vidrio antiguo texturizado en cobre empolvado y verde.", "5\" dia", "5\" diám."),
    ("glass", "Gold &amp; Green Marbled Glass Ball", "Bola de vidrio marmoleado oro y verde", "Glass with a marble finish in gold and green.", "Vidrio con acabado marmoleado en oro y verde.", "3.75\" dia", "3.75\" diám."),
    ("glass", "White &amp; Gold Marbled Glass Ball", "Bola de vidrio marmoleado blanco y oro", "Glass with a marble finish in white and gold.", "Vidrio con acabado marmoleado en blanco y oro.", "3.75\" dia", "3.75\" diám."),
    ("glass", "Gold &amp; Green Marbled Glass Globe", "Globo de vidrio marmoleado oro y verde", "The gold and green marbled glass in a larger size.", "El vidrio marmoleado oro y verde en un tamaño más grande.", "4.5\" dia", "4.5\" diám."),
    ("glass", "Taupe &amp; Silver Quilted Glass Ball", "Bola de vidrio capitoneada taupe y plata", "Molded quilted pattern in matte antique taupe and silver.", "Relieve capitoneado en taupe antiguo mate y plata.", "150 mm (≈6\") dia", "150 mm (≈6\") diám."),
    ("natural", "Twig Ball", "Bola de ramas", "Hand-wrapped natural twig sphere on jute.", "Esfera de ramitas naturales envuelta a mano, con yute.", "4.75\" dia", "4.75\" diám."),
    ("natural", "Twig Globe", "Globo de ramas", "The natural twig sphere in a fuller, rounder style.", "La esfera de ramitas en un estilo más lleno y redondo.", "6\" dia", "6\" diám."),
    ("natural", "Gilded Bark Sphere", "Esfera de corteza dorada", "Bark-textured ball with gold leaf in every crack.", "Bola con textura de corteza y hoja de oro en cada grieta.", "4.25\" dia", "4.25\" diám."),
    ("natural", "Gilded Songbird on Acorn", "Pajarito dorado sobre bellota", "Antique-gold aluminum bird perched on an acorn. Two styles, sold individually.", "Pajarito de aluminio en dorado antiguo sobre una bellota. Dos estilos, se venden por separado.", "5.25\"", "5.25\""),
    ("natural", "Gilded Stag Head", "Cabeza de venado dorada", "Antique-gold stag head ornament with full antlers.", "Adorno de cabeza de venado en dorado antiguo, con astas completas.", "10\"", "10\""),
    ("bells", "Pine &amp; Red Bell Drop", "Colgante de pino y cascabeles rojos", "Pine sprig with a cascade of red jingle bells.", "Ramita de pino con una cascada de cascabeles rojos.", "21\" L", "21\" largo"),
    ("bells", "Pine &amp; Bronze Bell Drop", "Colgante de pino y cascabeles bronce", "Pine sprig with a cascade of bronze jingle bells.", "Ramita de pino con una cascada de cascabeles bronce.", "21\" L", "21\" largo"),
    ("bells", "Red Bell Branch", "Rama con cascabeles rojos", "Arching branch hung with red bells, great in tall vases.", "Rama arqueada con cascabeles rojos, ideal en jarrones altos.", "43\" L", "43\" largo"),
    ("bells", "Gold Bell Branch", "Rama con cascabeles dorados", "Arching branch hung with gold bells.", "Rama arqueada con cascabeles dorados.", "43\" L", "43\" largo"),
    ("greenery", "Pine &amp; Pinecone Garland", "Guirnalda de pino con piñas", "Full mixed-pine garland with pinecones and tiny pearls.", "Guirnalda frondosa de pinos mixtos con piñas y pequeñas perlas.", "6' L", "6' largo"),
    ("greenery", "Trailing Larch Branch", "Rama colgante de alerce", "Delicate trailing branch with mini cones.", "Rama colgante delicada con mini piñas.", "46\" L", "46\" largo"),
    ("greenery", "Frosted Trailing Pine", "Pino colgante escarchado", "Soft draping pine with a light frost and cones.", "Pino suave y colgante, con un toque escarchado y piñas.", "22\" L", "22\" largo"),
    ("greenery", "Pine &amp; Cone Spray", "Ramo de pino con piñas", "Full pine spray with natural cones.", "Ramo frondoso de pino con piñas naturales.", "19\" L", "19\" largo"),
    ("greenery", "Pine &amp; Cone Pick", "Vara de pino con piñas", "Airy pine pick with small natural pinecones.", "Vara de pino ligera con pequeñas piñas naturales.", "16\" L", "16\" largo"),
    ("greenery", "Balsam Fir &amp; Cone Spray", "Ramo de abeto con piñas", "Classic balsam fir spray with pinecones that fills arrangements beautifully.", "Ramo clásico de abeto con piñas, perfecto para llenar arreglos.", "21\" L", "21\" largo"),
    ("greenery", "Alpine Fir, Berry &amp; Cone Pick", "Vara de abeto, bayas y piña", "Alpine fir with red berries and a pinecone.", "Abeto alpino con bayas rojas y una piña.", "26\" L", "26\" largo"),
    ("greenery", "Pine &amp; Red Berry Spray", "Ramo de pino con bayas rojas", "Dark pine with clusters of red berries.", "Pino oscuro con racimos de bayas rojas.", "31\" L", "31\" largo"),
    ("greenery", "Frosted Pine &amp; Berry Spray", "Ramo de pino escarchado con bayas", "Frosted pine with bright red berry clusters.", "Pino escarchado con racimos de bayas rojas.", "28\" L", "28\" largo"),
    ("greenery", "Red &amp; White Berry Pick", "Vara de bayas rojas y blancas", "Branch pick with red and white berries.", "Vara con bayas rojas y blancas.", "16.5\" L", "16.5\" largo"),
    ("greenery", "Twig &amp; Cone Branch", "Rama con mini piñas", "Bare twig branch with tiny natural cones.", "Rama de ramitas con pequeñas piñas naturales.", "27\" L", "27\" largo"),
    ("natural", "Gilded Stag Candle Holder", "Portavela de venado dorado", "Antique-gold stag head whose antlers cradle a candle.", "Cabeza de venado dorada cuyas astas sostienen una vela.", "13\" H × 8\" L", "13\" alto × 8\" largo"),
    ("bells", "Copper Bell Cluster with Berries", "Racimo de campanas cobre con bayas", "Copper bells on burgundy ribbon, topped with berries and cedar.", "Campanas cobre con cinta borgoña, bayas y cedro.", "21\" L", "21\" largo"),
    ("bells", "Gold Jingle Bell Cluster", "Racimo de cascabeles dorados", "Gold jingle bells on red ribbon with a pine and berry sprig.", "Cascabeles dorados con cinta roja y una ramita de pino con bayas.", "20\" L", "20\" largo"),
    ("greenery", "Trailing Gold Cone Branch", "Rama colgante con piñas doradas", "Cascading branch dotted with gold-dusted mini cones.", "Rama en cascada con mini piñas espolvoreadas en dorado.", "39.5\" L", "39.5\" largo"),
    ("greenery", "Trailing Whitewashed Cone Branch", "Rama colgante con piñas blanqueadas", "Cascading branch with brown, whitewashed mini cones.", "Rama en cascada con mini piñas café blanqueadas.", "39.5\" L", "39.5\" largo"),
    ("pinecone", "Champagne Star Petal Ball", "Bola de pétalos estrella champaña", "Clusters of star-shaped petals in soft champagne bronze.", "Racimos de pétalos en forma de estrella, en bronce champaña suave.", "5.5\" dia", "5.5\" diám."),
    ("pinecone", "Champagne Star Petal Cone", "Cono de pétalos estrella champaña", "The star-petal design in a hanging cone shape.", "El diseño de pétalos estrella en forma de cono colgante.", "6\" H × 3.5\" dia", "6\" alto × 3.5\" diám."),
]


# Retail price in USD for each item, in the same order as ITEMS (from the pricing sheet, 2.2x markup)
PRICES = [19, 28, 27, 20, 21, 29, 17, 28, 19, 28, 16, 18, 10, 16, 17, 14, 10, 16, 22, 9, 10, 18, 19, 11, 18, 14, 9, 9, 13, 15, 12, 16, 8, 31, 8, 12, 12, 25, 25, 70, 18, 16, 17, 6, 7, 15, 14, 21, 10, 10, 74, 26, 23, 17, 17, 24, 13]
assert len(PRICES) == len(ITEMS)


def holiday_body(t):
    hero = [1, 29, 35]
    cards = {}
    for i, ((c, en, es, den, des, sen, ses), price) in enumerate(zip(ITEMS, PRICES), 1):
        code = f"CM-H{i:02d}"
        qen, qes = sen.replace('"', "&quot;"), ses.replace('"', "&quot;")
        cards.setdefault(c, []).append(
            f'<article class="hc-card" data-code="{code}" data-en="{en}" data-es="{es}" data-den="{den}" data-des="{des}" data-sen="{qen}" data-ses="{qes}" data-price="{price}" data-cat="{c}">'
            f'<button type="button" class="hc-ph" aria-label="{en}"><img src="img/hol-cm-h{i:02d}.jpg" alt="{en}" loading="lazy"></button>'
            f'<div class="hc-meta"><div class="hc-code">{code}</div><h3>{t(en, es)}</h3><p class="hc-size">{t(sen, ses)}</p><p class="hc-price">${price}</p>'
            f'<button type="button" class="hc-add" data-code="{code}">{t("+ Select", "+ Elegir")}</button></div></article>')
    chips = (f'<button type="button" data-filter="all" aria-pressed="true">{t("All", "Todo")} <i>{len(ITEMS)}</i></button>'
             + "".join(f'<button type="button" data-filter="{c}" aria-pressed="false">{t(en, es)} <i>{len(cards[c])}</i></button>'
                       for c, en, es, _ in COLLECTIONS))
    sections = "".join(
        f'<div class="hc-col" data-col="{c}"><div class="hc-col-head"><div><h2>{t(en, es)}</h2>'
        f'<p class="hc-from">{t(f"From ${frm}", f"Desde ${frm}")}</p></div>'
        f'<span class="label">{len(cards[c])} {t("pieces", "piezas")}</span></div>'
        f'<div class="hc-grid">{"".join(cards[c])}</div></div>'
        for c, en, es, frm in COLLECTIONS)
    return f'''<section class="intro hc-intro">
  <div class="wrap hc-hero">
    <div class="stack">
      <div class="label">{t("Holiday 2026 · Special order", "Navidad 2026 · Por encargo")}</div>
      <h1>{t("The Holiday Collection", "La Colección Navideña")}</h1>
      <p class="lede">{t(f"{len(ITEMS)} pieces chosen by Claudia for this season: pinecone ornaments, mercury and antique glass, gilded accents and lifelike greenery in warm golds, burgundy and woodland pine.", f"{len(ITEMS)} piezas escogidas por Claudia para esta temporada: piñas decorativas, vidrio mercurio y antiguo, detalles dorados y follaje realista en dorados cálidos, borgoña y verde pino.")}</p>
      <p class="muted">{t("Pieces are ordered for you. Choose what you love, send us your selection, and we'll confirm availability and delivery.", "Las piezas se piden para ti. Elige lo que te guste, envíanos tu selección y te confirmamos disponibilidad y entrega.")}</p>
      <div class="btns"><a class="btn solid" href="#collection">{t("View the collection", "Ver la colección")}</a><button type="button" class="btn line" data-open-sel>{t("My selection", "Mi selección")}</button></div>
    </div>
    <div class="hc-hero-art">{"".join(f'<div><img src="img/hol-cm-h{n:02d}.jpg" alt=""></div>' for n in hero)}</div>
  </div>
</section>
<section class="hc-how">
  <div class="wrap"><ol class="hc-steps">
    <li><b>1</b><span><strong>{t("Browse", "Explora")}</strong>{t("Tap any piece to see it up close.", "Toca cualquier pieza para verla de cerca.")}</span></li>
    <li><b>2</b><span><strong>{t("Select", "Elige")}</strong>{t("Add the pieces you love to your selection.", "Agrega a tu selección las piezas que te gusten.")}</span></li>
    <li><b>3</b><span><strong>{t("Request", "Solicita")}</strong>{t("Send your list and we'll confirm availability.", "Envíanos tu lista y te confirmamos disponibilidad.")}</span></li>
  </ol></div>
</section>
<section id="collection" class="hc-shop">
  <div class="hc-bar"><div class="wrap hc-bar-row"><div class="filters hc-filters">{chips}</div>
    <button type="button" class="btn line hc-sel-btn" data-open-sel>{t("My selection", "Mi selección")} <span class="hc-count">0</span></button></div></div>
  <div class="wrap">{sections}</div>
</section>
<section class="sand">
  <div class="wrap split">
    <div class="stack narrow">
      <div class="label">{t("Seasonal styling", "Decoración de temporada")}</div>
      <h2>{t("Want it installed, too?", "¿También quieres que lo instalemos?")}</h2>
      <p class="lede">{t("We can design and dress your tree, mantel and table with these pieces, ready for the season.", "Podemos diseñar y decorar tu árbol, repisa y mesa con estas piezas, listos para la temporada.")}</p>
      <div class="btns"><a class="btn solid" href="contact.html">{t("Reserve a holiday date", "Reserva tu fecha")}</a><a class="textlink" href="interior-design.html#seasonal">{t("A Conceptual Christmas", "Una Navidad Conceptual")}</a></div>
    </div>
    <div class="media">{'<img src="img/xmas-dress11.jpg" alt="Dressing the tree in gold and bronze ornaments" loading="lazy" style="object-position:50% 55%">'}</div>
  </div>
</section>

<div class="hc-lb" id="hc-lb" hidden><div class="hc-lb-box" role="dialog" aria-modal="true" aria-labelledby="hc-lb-name">
  <button type="button" class="hc-x" data-close-lb aria-label="Close">×</button>
  <div class="hc-lb-ph"><button type="button" class="hc-nav prev" aria-label="Previous">‹</button><img id="hc-lb-img" alt=""><button type="button" class="hc-nav next" aria-label="Next">›</button></div>
  <div class="hc-lb-info stack">
    <div class="hc-code" id="hc-lb-code"></div>
    <h2 id="hc-lb-name"></h2>
    <p class="hc-size" id="hc-lb-size"></p>
    <p class="hc-price hc-lb-price" id="hc-lb-price"></p>
    <p class="muted" id="hc-lb-desc"></p>
    <button type="button" class="btn solid" id="hc-lb-add"></button>
    <p class="hc-note">{t("Prices in USD. Subject to availability: we confirm stock and delivery before you pay.", "Precios en USD. Sujeto a disponibilidad: confirmamos existencias y entrega antes de que pagues.")}</p>
  </div>
</div></div>

<div class="hc-shade" id="hc-shade" hidden></div>
<aside class="hc-drawer" id="hc-drawer" aria-label="My selection" hidden>
  <div class="hc-dr-head"><h2>{t("My selection", "Mi selección")}</h2><button type="button" class="hc-x" data-close-sel aria-label="Close">×</button></div>
  <div class="hc-dr-body" id="hc-dr-body"></div>
  <div class="hc-dr-foot">
    <div class="hc-total"><span>{t("Total", "Total")}</span><b id="hc-total">$0</b></div>
    <p class="hc-avail">{t("Prices in USD. We confirm availability and delivery before you pay.", "Precios en USD. Confirmamos disponibilidad y entrega antes de que pagues.")}</p>
    <input id="hc-name" autocomplete="name" data-ph-en="Your name" data-ph-es="Tu nombre" placeholder="Your name">
    <a class="btn solid" id="hc-wa" href="https://wa.me/17542456323" target="_blank" rel="noopener">{t("Send via WhatsApp", "Enviar por WhatsApp")}</a>
    <button type="button" class="btn line" id="hc-copy">{t("Copy my list", "Copiar mi lista")}</button>
    <p class="hc-toast" id="hc-toast" role="status"></p>
  </div>
</aside>'''
