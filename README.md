# Advent Games wireframes

Clickable greyscale wireframes for the Advent Games Shopify build (Enterprise theme).

- `build.py` generates every page into `site/`. Edit it, then run `python3 build.py`.
- `site/` is what Cloudflare serves (static assets via `wrangler.jsonc`). Commit the rebuilt pages.
- `icons/` holds the Phosphor (MIT) SVGs inlined at build time.
- The site is set to noindex (meta tag, `_headers`, `robots.txt`).
