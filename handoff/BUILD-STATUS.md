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
Checked against the design at 1440px and 390px with Playwright (home page, Board Games and Preorders mega menus, cart drawer). Side-by-side screenshots: `handoff/qa/`.

Remaining differences from Enterprise's native layout:
- Section subs under headings are missing (no setting, see flags).
- Product cards: no badges, wishlist heart or players/time/complexity row yet (these come from metafields and are product page work). Many demo products have no images.
- Carousels show Enterprise's progress line instead of round arrow buttons.
- Search button is an icon inside the field rather than a blue button.
- Newsletter submit is an arrow button rather than "Sign up".
- Hero text panel sits at the bottom of the large tile rather than vertically centred.

## Flags for Jake
- Featured collection, Product list and Collection list have no subtitle setting, so the one-line section subs are missing.
- Announcement bar has two link slots, so "Brands A-Z" is missing there (it is in the footer).
- Media with text allows one button: extra buttons are links in the text block styled as secondary buttons.
- Newsletter section is not allowed in the footer group: it sits at the end of the home template, so other templates need it added.
- Mobile logo and BGG logo are CSS images (Enterprise has one logo setting, footer allows four blocks).
- Testimonials placeholder is a one-at-a-time slider, not three cards. Google Reviews app not installed.
- Page width is 1590px (Enterprise steps by 30 from 1200).

## Missing in the store (Dean or Jake)
- Gift card product (`/products/gift-card`), staff notes on the 4 staff picks, vendor collections for publisher logos, `/pages/help`, `/pages/about`, `/pages/brands`, `/blogs/news` content, and most sub-collections in the mega menus (linked to `#`).
