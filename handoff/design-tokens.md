# Advent Games design tokens

The exact source for every value is `handoff/design-source/design.css` (the `:root` block at the top and the component rules below it). This file summarises what matters for the Shopify build. When in doubt, open the live design and inspect it: https://advent.qagency.workers.dev/design/

Map each token to an **Enterprise theme setting first** (Theme settings > Colours, Typography, Layout, Buttons, Product cards). Only use CSS in `assets/advent.css` for what the settings can't do.

## Colour

| Token | Hex | Used for |
|---|---|---|
| surface | #ffffff | Page background (site is white-first) |
| surface-subtle | #f6f8fa | Soft bands, image wells |
| surface-muted | #eef0f3 | Muted tiles |
| border | #e3e7ec | Card and divider lines |
| border-strong | #8a94a6 | Inputs, outline buttons, carousel arrows |
| ink | #16213a | Headings and body text |
| ink-muted | #4c5870 | Secondary text |
| brand-blue | #2f4a85 | Primary buttons, links, active states |
| brand-blue-hover | #24396a | Primary button hover |
| brand-blue-tint | #e8eef8 | Preorder badge, brand story band, info |
| sky | #7fcbe0 | Accent |
| sky-tint | #e2f2f6 | Coming soon badge, hero text panel |
| sky-text | #1b5b70 | Text on sky tints |
| sun | #f4d44d | "Just arrived" hero tile, star rating |
| sun-tint | #fcf3cc | Just arrived badge, staff picks band |
| sun-text | #6a5200 | Text on sun tints |
| orange | #e0782f | Sale pill, ribbon (decorative only, white text fails contrast on it) |
| orange-tint | #fdeee3 | Sale badge |
| sale-text | #9a4210 | Sale text |
| success | #1e6a3e | In stock |
| warning | #a35407 | At supplier |
| danger | #b42318 | Out of stock |
| preorders tile | #a2dded | "Preorders open" hero tile (old site blue) |

### Buttons

| Button | Background | Text | Hover |
|---|---|---|---|
| Primary | #2f4a85 | #ffffff | #24396a |
| Secondary | #ffffff, 1px #2f4a85 border | #2f4a85 | bg #e8eef8 |
| **Add to cart / Preorder (product cards, buy box, cart Checkout)** | **#bd5a15** | **#ffffff** | #a84c10 |

Buttons: min-height 44px (36px small), radius 10px, DM Sans 600 15px, sentence case (no uppercase).

### Header, footer and bands (gradients)

| Area | Value |
|---|---|
| Announcement bar | #f5b06a background, #16213a text, 13px |
| **Header (gradient, the default)** main row | linear-gradient(180deg, #8fd8ef 0%, #4a9fd9 100%) |
| Header menu row | linear-gradient(180deg, #2a7cc0 0%, #2470b0 40%, #1d5e98 100%), white 15px 600 text, active underline #f4d44d |
| Search bar on the gradient | white field, no border, brand-blue search button |
| Trust strip (icons with text) | white, 1px bottom border, icons in 40px #e2f2f6 circles |
| Newsletter | linear-gradient(120deg, #ea8c40 0%, #f0a046 50%, #f4d44d 100%) |
| Footer | linear-gradient(180deg, #4a9fd9 0%, #63b8e4 40%, #8fd8ef 100%), ink text |

Enterprise colour schemes support a background gradient setting. Use it for the header, newsletter and footer where the section allows. Fall back to section Custom CSS.

## Type

- **Headings:** Nunito 800 (Shopify font `nunito_n8`). Display 32-48px clamp, H2 28/34, H3 22/28, H4 18/24. No uppercase.
- **Body:** DM Sans 400 16/24 (`dm_sans_n4`). Large body 18/28. Small 13/18.
- **Eyebrow / subheading:** 12px, 700, uppercase, 0.08em letter-spacing, ink-muted.
- **Navigation:** DM Sans 600-700.

## Layout and shape

- Page width **1600px**, gutters 16px (mobile) and up.
- Section spacing 48px (`--space-7`) top and bottom. Tighter (24px) for title-only sections.
- Spacing scale: 4, 8, 12, 16, 24, 32, 48, 64.
- Radius: 6px small, 10px medium (cards, buttons, inputs), 16px large (hero tiles, banners, images).
- Card shadow on hover only: 0 6px 20px rgba(22,33,58,.08).

## Product card

- White card, 1px #e3e7ec border, 10px radius, equal heights, button pinned to the bottom.
- Square box art, **contained, never cropped**, on #f6f8fa.
- Order: badges (top left), wishlist heart (top right), publisher (12px muted), title (16px 600, 2-line clamp), price (RRP struck through only on genuine sales), stats row (players · play time · complexity /5, 13px with icons), availability line (coloured dot + label, optional sub-line), full-width orange Add to cart.
- **No BGG rating on cards.**
- Badges: 22px tall, 11px uppercase 700, 6px radius. Preorder = blue tint, Coming soon = sky tint, Sale = orange tint, Just arrived = sun tint, Back in stock = success tint, Expansion = white with outline.

## Motion

- Theme animations **off** (Dean dislikes fades).
- Carousels never auto-rotate. Arrows on desktop, swipe on mobile.
- Hover transitions only, 120-250ms.

## Contrast decisions (already checked)

- White on #e0782f fails, which is why buttons use the darker #bd5a15.
- White menu text on the darker gradient row passes (about 4.8:1 at its lightest point).
- Don't state a WCAG level anywhere client-facing.
