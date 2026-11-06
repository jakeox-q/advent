# Home page build: status

Dev theme: **Advent build (dev)** (`gid://shopify/OnlineStoreTheme/160180043968`), duplicated from the base Enterprise theme. Live theme untouched.
Preview: https://advent-games-017wrq2h.myshopify.com/?preview_theme_id=160180043968 (storefront password needed).

## Pushed to the dev theme
- Theme settings (colours, Nunito/DM Sans, 1590px width, 10px radius, animations off, cards, cart drawer, $300 free shipping)
- Header group: announcement (desktop + mobile message), gradient header, mega menus, trust strip
- Footer group: footer with logo, contact, three menus, payment icons, Powered by BGG
- Home template: all 13 sections in spec order, plus a disabled Boxing Day hero and the newsletter band at the end
- Cart drawer settings; demo popup disabled
- `assets/advent.css`, `snippets/advent-staff-note.liquid`, and the patches in `theme/PATCHES.md`

## Store data changed
- Products: the 50 demo products that were not on the Online Store channel were published to it so the home page sections render (only `the-great-harbor` and `three-days-of-gettysburg-deluxe-edition` were published before). Unpublish from Products > Sales channels if needed.
- Files: design images, publisher logos, mega menu promo images, type icons and 16:9 type tiles (`build-assets/`)
- Collections: tile image + `theme.label` sub on the 8 game-type collections; new `coming-soon` collection (6 existing preorder products, published)
- Menus: `main-menu` rebuilt from the design (no Brands item), new `header-secondary` and `footer-bgg`

## Visual QA
Checked against the design at 1440px and 390px with Playwright (home page, all mega menus and dropdowns, cart drawer). No sideways scroll at either width. Final pass done after the section subs, card badges, stats row and card spacing changes. Side-by-side screenshots: `handoff/qa/`.

The final local QA pass (6 November 2026) fixed the wishlist heart labels, carousel arrows, newsletter form, media with text layout, sale banner text and footer layout. Those fixes were checked in the live preview at 1440px and at about 390px, using an iframe because the browser window could not be narrowed. The screenshots in `handoff/qa/` were taken before this pass.

Remaining differences from the design:
- Header: no Wishlist icon, and no text labels under the Account and Cart icons. Enterprise has no setting for either, so this needs a Liquid edit (see Flags).
- Carousels: 5 across as the spec says. The design shows 4.
- Reviews: placeholder until the Google Reviews app is chosen. No "Reviews" eyebrow, sub or "Leave us a review" link, and the stars sit below the quote.
- Product cards: many demo products have no images or BGG data, so their stats rows are short or hidden.

## Flags for Jake
- Header Wishlist icon: the spec lists it, but it needs a Liquid edit to Enterprise's header and has no page to link to yet. Waiting on Jake's call.
- Carousel count: the spec says 5 across, the design shows 4. Built to the spec.
- Wishlist heart: built as a browser-saved placeholder until a wishlist app is chosen.
- ABN in the footer comes from the design only. Dean to confirm.
- Section subs, the announcement's third link (Brands A-Z), and the card badges and stats row are small Liquid tweaks to Enterprise files (see `theme/PATCHES.md`), all editable in the theme editor or theme content.
- Media with text allows one button: extra buttons are links in the text block styled as secondary buttons.
- Newsletter section is not allowed in the footer group: it sits at the end of the home template, so other templates need it added.
- Mobile logo and BGG logo are CSS images (Enterprise has one logo setting, footer allows four blocks).
- Testimonials placeholder is a one-at-a-time slider, not three cards. Google Reviews app not installed.
- Page width is 1590px (Enterprise steps by 30 from 1200).

## Missing in the store (Dean or Jake)
- Payment icons: the setting is on, but the store has no payment methods enabled, so none show. They appear once payments are set up. Layout checked with stand-in icons.
- Terms of service and refund policies: the footer links to them, but only the privacy policy exists, so those two links 404 for now.
- `advent-en-default.txt` in Content > Files: leftover temporary upload, not used by the theme. Jake to delete.
- Gift card product (`/products/gift-card`), staff notes on the 4 staff picks, vendor collections for publisher logos, `/pages/help`, `/pages/about`, `/pages/brands`, `/blogs/news` content, and most sub-collections in the mega menus (linked to `#`).
