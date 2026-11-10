"""Holiday Collection page: items available by special order. No prices on the site — clients request them.
Images live in img/hol-cm-hNN.jpg. Item order fixes each piece's code (CM-H01 … CM-H50); add new items at the end."""

COLLECTIONS = [
    ("pinecone", "Pinecone Collection", "Colección de piñas"),
    ("glass", "Mercury &amp; Antique Glass", "Vidrio mercurio y antiguo"),
    ("natural", "Natural &amp; Gilded", "Natural y dorado"),
    ("bells", "Bells &amp; Drops", "Cascabeles y colgantes"),
    ("greenery", "Greenery &amp; Branches", "Follaje y ramas"),
]

# (collection, name EN, name ES, description EN, description ES)
ITEMS = [
    ("pinecone", "Burgundy Elongated Pinecone", "Piña alargada borgoña", "Deep wine scales with a metallic edge, hung on natural jute.", "Escamas color vino con borde metálico, colgada en yute natural."),
    ("pinecone", "Burgundy Pinecone", "Piña borgoña", "A fuller burgundy cone with shimmering tips.", "Piña borgoña más llena, con puntas brillantes."),
    ("pinecone", "Burgundy Pinecone Sphere", "Esfera de piña borgoña", "Round burgundy pinecone ornament, layered petals all around.", "Adorno redondo de piña borgoña, con pétalos en capas."),
    ("pinecone", "Champagne Elongated Pinecone", "Piña alargada champaña", "Slim cone in soft champagne gold.", "Piña delgada en un suave dorado champaña."),
    ("pinecone", "Gold Pinecone", "Piña dorada", "Warm brushed-gold scales on a jute loop.", "Escamas en dorado cepillado, con colgador de yute."),
    ("pinecone", "Gold Tall Pinecone", "Piña dorada alta", "Taller gold cone with a natural, slightly rustic finish.", "Piña dorada más alta, con acabado natural y algo rústico."),
    ("pinecone", "Gold Pinecone Sphere", "Esfera de piña dorada", "Round gilded pinecone with glittered edges.", "Piña redonda dorada con bordes escarchados."),
    ("pinecone", "Gold Pinecone Globe", "Globo de piña dorado", "Full round globe of golden pinecone scales.", "Globo redondo y lleno de escamas doradas."),
    ("pinecone", "Bronze Pinecone", "Piña bronce", "Dark bronze cone with gold-touched tips.", "Piña en bronce oscuro con puntas doradas."),
    ("pinecone", "Bronze Tall Pinecone", "Piña bronce alta", "Elongated bronze cone, rich and earthy.", "Piña alargada en bronce, cálida y terrosa."),
    ("pinecone", "Bronze Pinecone Sphere", "Esfera de piña bronce", "Round bronze pinecone with metallic highlights.", "Piña redonda en bronce con destellos metálicos."),
    ("pinecone", "Blush Bronze Petal Ball", "Bola de pétalos bronce rosado", "Dense blush-bronze petals for a softer, textured look.", "Pétalos en bronce rosado para un look suave y con textura."),
    ("pinecone", "Frosted Pinecone Ball", "Bola de piña escarchada", "Silver-frosted pinecone sphere on chunky jute rope.", "Esfera de piña escarchada en plata, con cuerda gruesa de yute."),
    ("pinecone", "Snow Pinecone Ball", "Bola de piña nevada", "Snow-white pinecone sphere on chunky jute rope.", "Esfera de piña blanca nieve, con cuerda gruesa de yute."),
    ("pinecone", "Frosted Icicle Cone", "Cono carámbano escarchado", "Long, slender frosted cone that reads like an icicle on the tree.", "Cono largo y delgado escarchado, como un carámbano en el árbol."),
    ("pinecone", "Bronze Leaf Cone Drop", "Colgante de hojas bronce", "Layered bronze leaves forming an elegant hanging cone.", "Hojas bronce en capas que forman un cono colgante elegante."),
    ("glass", "Sage &amp; Gold Antique Glass Set", "Set de vidrio antiguo salvia y oro", "Ball and onion shapes in pale sage with aged-gold patina.", "Bola y forma de cebolla en verde salvia con pátina dorada envejecida."),
    ("glass", "Gold Thread Glass Ball", "Bola de vidrio con hilo dorado", "Clear glass wrapped in fine gold threadwork.", "Vidrio transparente envuelto en fino hilo dorado."),
    ("glass", "Gold Thread Glass Globe", "Globo de vidrio con hilo dorado", "The gold-thread design in a bolder statement piece.", "El diseño de hilo dorado en una pieza protagonista."),
    ("glass", "Silver Mercury Glass Ball", "Bola de vidrio mercurio plateada", "Classic speckled mercury glass with a silver cap.", "Clásico vidrio mercurio moteado con tapa plateada."),
    ("glass", "Silver Mercury Glass Globe", "Globo de vidrio mercurio plateado", "Speckled silver mercury glass with a generous round profile.", "Vidrio mercurio plateado moteado, de silueta redonda y generosa."),
    ("glass", "Antique Gold Glass Ball", "Bola de vidrio antiguo dorada", "Smoky gold glass with a hand-aged finish.", "Vidrio dorado ahumado con acabado envejecido a mano."),
    ("glass", "Antique Amber Glass Ball", "Bola de vidrio antiguo ámbar", "Amber and champagne tones with vintage patina.", "Tonos ámbar y champaña con pátina vintage."),
    ("glass", "Antique Silver-Gold Glass Ball", "Bola de vidrio antiguo plata y oro", "Mixed silver and gold mercury effect.", "Efecto mercurio que mezcla plata y oro."),
    ("glass", "Smoked Bronze Glass Ball", "Bola de vidrio bronce ahumado", "Dark smoked bronze with mirrored highlights.", "Bronce ahumado oscuro con reflejos de espejo."),
    ("glass", "Aged Bronze Glass Ball", "Bola de vidrio bronce envejecido", "Deep weathered bronze for a moody, old-world look.", "Bronce profundo envejecido, con un aire clásico y elegante."),
    ("glass", "Gold Mercury Glass Ball", "Bola de vidrio mercurio dorada", "Bright speckled gold mercury glass.", "Vidrio mercurio dorado, brillante y moteado."),
    ("glass", "Champagne Marbled Glass Ball", "Bola de vidrio champaña marmoleada", "Soft champagne glass with a marbled pattern.", "Vidrio champaña suave con efecto marmoleado."),
    ("glass", "Golden Mirror Glass Globe", "Globo de vidrio espejo dorado", "Mirrored-gold globe with an antique cap.", "Globo dorado tipo espejo con tapa antigua."),
    ("glass", "Olive Quilted Glass Ball", "Bola de vidrio capitoneada oliva", "Raised quilted pattern in a muted olive-silver.", "Relieve capitoneado en un verde oliva plateado y sobrio."),
    ("natural", "Twig Ball", "Bola de ramas", "Hand-wrapped natural twig sphere on jute.", "Esfera de ramitas naturales envuelta a mano, con yute."),
    ("natural", "Twig Globe", "Globo de ramas", "The natural twig sphere in a fuller, rounder style.", "La esfera de ramitas en un estilo más lleno y redondo."),
    ("natural", "Gilded Bark Sphere", "Esfera de corteza dorada", "Bark-textured ball with gold leaf in every crack.", "Bola con textura de corteza y hoja de oro en cada grieta."),
    ("natural", "Gilded Songbird Pair", "Pareja de pajaritos dorados", "Two antique-gold birds perched on acorns.", "Dos pajaritos en dorado antiguo posados sobre bellotas."),
    ("natural", "Gilded Stag Head", "Cabeza de venado dorada", "Antique-gold stag head ornament with full antlers.", "Adorno de cabeza de venado en dorado antiguo, con astas completas."),
    ("bells", "Pine &amp; Red Bell Drop", "Colgante de pino y cascabeles rojos", "Pine sprig with a cascade of red jingle bells.", "Ramita de pino con una cascada de cascabeles rojos."),
    ("bells", "Pine &amp; Bronze Bell Drop", "Colgante de pino y cascabeles bronce", "Pine sprig with a cascade of bronze jingle bells.", "Ramita de pino con una cascada de cascabeles bronce."),
    ("bells", "Red Bell Branch", "Rama con cascabeles rojos", "Arching branch hung with red bells, great in tall vases.", "Rama arqueada con cascabeles rojos, ideal en jarrones altos."),
    ("bells", "Gold Bell Branch", "Rama con cascabeles dorados", "Arching branch hung with gold bells.", "Rama arqueada con cascabeles dorados."),
    ("greenery", "Pine &amp; Pinecone Garland", "Guirnalda de pino con piñas", "Full mixed-pine garland with pinecones and tiny pearls.", "Guirnalda frondosa de pinos mixtos con piñas y pequeñas perlas."),
    ("greenery", "Trailing Larch Branch", "Rama colgante de alerce", "Delicate trailing branch with mini cones.", "Rama colgante delicada con mini piñas."),
    ("greenery", "Frosted Trailing Pine", "Pino colgante escarchado", "Soft draping pine with a light frost and cones.", "Pino suave y colgante, con un toque escarchado y piñas."),
    ("greenery", "Pine &amp; Cone Spray", "Ramo de pino con piñas", "Full pine spray with natural cones.", "Ramo frondoso de pino con piñas naturales."),
    ("greenery", "Cedar &amp; Cone Pick", "Vara de cedro con piñas", "Airy cedar pick with small pinecones.", "Vara de cedro ligera con piñas pequeñas."),
    ("greenery", "Woodland Pine Spray", "Ramo de pino del bosque", "Classic pine spray with cones that fills arrangements beautifully.", "Ramo clásico de pino con piñas, perfecto para llenar arreglos."),
    ("greenery", "Pine, Berry &amp; Cone Pick", "Vara de pino, bayas y piña", "Pine with red berries and a single pinecone.", "Pino con bayas rojas y una piña."),
    ("greenery", "Pine &amp; Red Berry Spray", "Ramo de pino con bayas rojas", "Dark pine with clusters of red berries.", "Pino oscuro con racimos de bayas rojas."),
    ("greenery", "Frosted Pine &amp; Berry Spray", "Ramo de pino escarchado con bayas", "Frosted pine with bright red berry clusters.", "Pino escarchado con racimos de bayas rojas."),
    ("greenery", "Frosted Berry Branch", "Rama escarchada con bayas", "White-frosted branch with red and silver berries.", "Rama escarchada en blanco con bayas rojas y plateadas."),
    ("greenery", "Twig &amp; Cone Branch", "Rama con mini piñas", "Bare twig branch with tiny natural cones.", "Rama de ramitas con pequeñas piñas naturales."),
]


def holiday_body(t):
    hero = [1, 29, 35]
    cards = {}
    for i, (c, en, es, den, des) in enumerate(ITEMS, 1):
        code = f"CM-H{i:02d}"
        cards.setdefault(c, []).append(
            f'<article class="hc-card" data-code="{code}" data-en="{en}" data-es="{es}" data-den="{den}" data-des="{des}" data-cat="{c}">'
            f'<button type="button" class="hc-ph" aria-label="{en}"><img src="img/hol-cm-h{i:02d}.jpg" alt="{en}" loading="lazy"></button>'
            f'<div class="hc-meta"><div class="hc-code">{code}</div><h3>{t(en, es)}</h3>'
            f'<button type="button" class="hc-add" data-code="{code}">{t("+ Select", "+ Elegir")}</button></div></article>')
    chips = (f'<button type="button" data-filter="all" aria-pressed="true">{t("All", "Todo")} <i>{len(ITEMS)}</i></button>'
             + "".join(f'<button type="button" data-filter="{c}" aria-pressed="false">{t(en, es)} <i>{len(cards[c])}</i></button>'
                       for c, en, es in COLLECTIONS))
    sections = "".join(
        f'<div class="hc-col" data-col="{c}"><div class="hc-col-head"><h2>{t(en, es)}</h2>'
        f'<span class="label">{len(cards[c])} {t("pieces", "piezas")}</span></div>'
        f'<div class="hc-grid">{"".join(cards[c])}</div></div>'
        for c, en, es in COLLECTIONS)
    return f'''<section class="intro hc-intro">
  <div class="wrap hc-hero">
    <div class="stack">
      <div class="label">{t("Holiday 2026 · Special order", "Navidad 2026 · Por encargo")}</div>
      <h1>{t("The Holiday Collection", "La Colección Navideña")}</h1>
      <p class="lede">{t("Fifty pieces chosen by Claudia for this season: pinecone ornaments, mercury and antique glass, gilded accents and lifelike greenery in warm golds, burgundy and woodland pine.", "Cincuenta piezas escogidas por Claudia para esta temporada: piñas decorativas, vidrio mercurio y antiguo, detalles dorados y follaje realista en dorados cálidos, borgoña y verde pino.")}</p>
      <p class="muted">{t("Pieces are ordered for you. Choose what you love and we'll send pricing and availability.", "Las piezas se piden para ti. Elige lo que te guste y te enviamos precios y disponibilidad.")}</p>
      <div class="btns"><a class="btn solid" href="#collection">{t("View the collection", "Ver la colección")}</a><button type="button" class="btn line" data-open-sel>{t("Request pricing", "Pedir precios")}</button></div>
    </div>
    <div class="hc-hero-art">{"".join(f'<div><img src="img/hol-cm-h{n:02d}.jpg" alt=""></div>' for n in hero)}</div>
  </div>
</section>
<section class="hc-how">
  <div class="wrap"><ol class="hc-steps">
    <li><b>1</b><span><strong>{t("Browse", "Explora")}</strong>{t("Tap any piece to see it up close.", "Toca cualquier pieza para verla de cerca.")}</span></li>
    <li><b>2</b><span><strong>{t("Select", "Elige")}</strong>{t("Add the pieces you love to your selection.", "Agrega a tu selección las piezas que te gusten.")}</span></li>
    <li><b>3</b><span><strong>{t("Request", "Solicita")}</strong>{t("Send your list and we'll reply with pricing.", "Envíanos tu lista y te respondemos con precios.")}</span></li>
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
    <p class="muted" id="hc-lb-desc"></p>
    <button type="button" class="btn solid" id="hc-lb-add"></button>
    <p class="hc-note">{t("Pricing on request. Add pieces to your selection and send us the list.", "Precios a solicitud. Agrega piezas a tu selección y envíanos la lista.")}</p>
  </div>
</div></div>

<div class="hc-shade" id="hc-shade" hidden></div>
<aside class="hc-drawer" id="hc-drawer" aria-label="My selection" hidden>
  <div class="hc-dr-head"><h2>{t("My selection", "Mi selección")}</h2><button type="button" class="hc-x" data-close-sel aria-label="Close">×</button></div>
  <div class="hc-dr-body" id="hc-dr-body"></div>
  <div class="hc-dr-foot">
    <input id="hc-name" autocomplete="name" data-ph-en="Your name" data-ph-es="Tu nombre" placeholder="Your name">
    <a class="btn solid" id="hc-wa" href="https://wa.me/17542456323" target="_blank" rel="noopener">{t("Send via WhatsApp", "Enviar por WhatsApp")}</a>
    <button type="button" class="btn line" id="hc-copy">{t("Copy my list", "Copiar mi lista")}</button>
    <p class="hc-toast" id="hc-toast" role="status"></p>
  </div>
</aside>'''
