# Conceptual Interiors website

Bilingual (EN/ES) static site for Conceptual Interiors: custom window treatments, interior design and furnishings.

## How it's built
- `build.py` holds every page's content (English and Spanish side by side) and writes the finished site to `dist/`.
- `styles.css` holds the brand styles (greige/ivory palette, Cormorant Garamond + Montserrat).
- `site.js` handles the language toggle, mobile menu, portfolio filters and the inquiry form.
- `img/`, `media/` and `brand/` hold photos, videos and logo files.

To change anything: edit `build.py`, `styles.css` or the images, run `python3 build.py`, commit, push. Netlify publishes `dist/` automatically.

## Hosting (Netlify)
- Publish directory: `dist` (no build command).
- The contact form uses Netlify Forms. Under Site settings → Forms → Notifications, add an email notification to clavegiraldo@hotmail.com.

## Still to confirm before launch
- Claudia's bio in her own words (About page, marked TODO in build.py).
- Photo usage rights for the Orlando and Pinecrest projects.
- Domain name, then add a sitemap with the final URL.
