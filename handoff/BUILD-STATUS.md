# Advent build: status

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
- Reviews: placeholder until the Google Reviews app is chosen. No "Reviews" eyebrow, sub or "Leave us a review" link, and the stars sit below the quote.
- Product cards: many demo products have no images or BGG data, so their stats rows are short or hidden.

## Flags for Jake
- Wishlist: Jake parked the header icon and wishlist page for now (7 November 2026).
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

---

# Other pages: first draft (7 November 2026)

Every page below is on the dev theme. Checked on the demo products at desktop width and about 375px, with no Liquid errors, no missing translations and no sideways scroll on 22 URLs. The demo data is thin, so many data-driven blocks could not be seen with real content.

## Pages built
- **Collections:** `collection.json` (standard, also vendor pages), `.preorders` (with How it works steps), `.just-arrived`, `.rpg` (Shop by system, New to roleplaying), `.accessories`. SEO copy block from new collection metafields, hidden when empty.
- **Product:** one `product.json` for all product types. Blocks show or hide from the data: BGG line, RRP, availability card, stats strip (board game, RPG or accessory), tags, expansion note, tabs, videos, staff note + FAQ, related rows.
- **Search:** results plus the no-results tips and buttons.
- **About + contact, Help & FAQ, Brands A-Z:** `page.about`, `page.help`, `page.brands`.
- **Blog and article:** `blog.json`, `article.json`.
- **Home:** carousels now 4 across, as Jake asked.

## Not built
- Wishlist page and header icon (parked by Jake).
- "Games in this article" row (optional in the design).
- "Best sellers from [brand]" row on brand pages: vendor pages have no per-brand collection to read yet.

## Custom sections where the design said native
Each is editable with settings and blocks. For Jake to check:
- `advent-help`: Enterprise's FAQ has no topic anchors for the sticky pills.
- `advent-brands-az`: groups a menu by letter (the design notes tweak on the bar, native on the lists).
- `advent-contact`: form and details card side by side, plus an order number field.
- `advent-pickup`: the details card rows.
- `advent-product-details`: Enterprise's Product details sits in the left column; the design has it full width.
The design already marks `advent-product-videos` and `advent-note-faq` as custom. `advent-product-row` replaces Featured collection so rows can follow the product's data.

## Differences from the design
- **Per page:** 48, not 200 with a picker. Enterprise caps the setting at 50; the picker needs alternate collection views (Shopify's own limit is 250).
- **Filters are checkboxes:** Players, Play time and Complexity don't have the design's range sliders or chips yet.
- **Availability filter** is native In stock / Out of stock. Preorder and Coming soon options need a filter on `advent.availability_state`.
- **Applied filters** use Enterprise's styling, and the filter button says Filter rather than Hide filters.
- **Product gallery** was only seen with one image per product, so thumbnails on the left are unchecked.
- **Article:** no "By Dean · 4 minute read" line as designed; share and previous/next are Enterprise's.
- **Reviews, wishlist hearts on the product page:** not in this draft.

## Store data changed (all on the dev store)
- **Search & Discovery filters added:** Players, Play time, Complexity, Youngest player, Game type, Product type, Publisher, Category, Mechanic, RPG system, RPG category, Sleeve size. Not added yet: Setting, Made for.
- **Pages created and published:** About us, Help & FAQ, Brands A-Z.
- **Sample articles created and published:** 7, using the design's titles and copy, in the News blog (renamed "News & reviews"). Delete before launch or replace with Dean's.
- **Menu created:** `brands`, 93 publishers from the design, linking to vendor pages.
- **Collections created and published:** ALIEN, Blade Runner, Arkham Horror RPG, Call of Cthulhu, Avatar Legends, Animal Adventures. Empty manual placeholders for the Shop by system tiles.
- **Collections updated:** template assignments on Preorders, New to Preorder, Coming Soon, Just Arrived, Roleplaying, Accessories; descriptions on Board Games, Preorders, Roleplaying, Accessories from the design.
- **Metafield definitions added:** collection `advent.seo_heading`, `advent.seo_text`. Board Games has sample copy.
- **Files:** 16 design images uploaded.

## Needs real data before it can be checked
- RPG and accessory fields (`rpg.*`, `advent.sleeve_size`, `pack_quantity`, `finish`, `related_game_names`): stats strip, card lines, RPG and sleeve filters and rows.
- `bgg.weight`, `rating`, `rank`, `designers`, `year_published`, `families`, `expands`: Complexity filter, BGG line, expansion note, series row.
- `advent.staff_note`, `advent.notice`, complementary products, video media, extra product images.
- Row collections by handle: series name, `sleeves-` + size.

## For Dean
- Two FAQ answers are switched off until written: "Do you price match?" and "Why are board games expensive in Australia?"
- Pickup venue and time differ between his current pages. The draft says Northside Gamers Group, Chatswood, with no address.
- When Advent started: home says "since 2012", the design notes mention 2013.
- About page copy is a draft, and the Dean photo is a stand-in.
- Bank transfer: the trust strip and Help mention it. Is it staying?
- Supplier dispatch window: 2-7 business days as designed.


# BugHerd backlog: Dean's feedback on the mockup (9 November 2026)

Five Backlog tasks in BugHerd project 546364, all left on the Cloudflare mockup. Checked against the Shopify build and actioned where they apply. Nothing was posted or changed in BugHerd.

- **#99 Menu fade and bigger dropdowns.** Done. The page no longer dims behind desktop dropdowns and mega menus (the mobile menu drawer keeps its dim). Just Arrived and Sale now have mega menu blocks like Preorders and Accessories: links on the left, three image promos on the right. The promo labels reuse Dean's own menu labels (New board games, New RPGs, Back in stock; Weekly sale, Clearance, Dings & dents) with stock product images, and all link to the collection because the menu sub-links are still `#`. Dean can swap any promo for "20% off RRP" style banners in the theme editor (Header > Just Arrived / Sale block > Promo 1 to 3).
- **#100 Price slider knob clipped on the left.** Done. The same clipping happened in the Shopify build. The slider track is now inset so both knobs, and their hover scale, sit inside the filter column.
- **#101 Filter column cut off on the left, focus ring clipped.** Done. Filter panels now have a few pixels of room on each side, and the desktop filter column no longer hides overflow, so focus rings show in full.
- **#102 Filters should scroll with the page.** Already native in Enterprise. The filter column scrolls with the page, pins when its bottom is reached, and scrolls back up when the shopper scrolls up (checked with all filters expanded). Not done: keeping "Applied filters" frozen at the top. That would be custom work, so ask Dean if he still wants it after trying the build.
- **#98 Facebook reviews mixed with Google reviews.** Not a theme change. It depends on the reviews app. Pick an app that pulls both Google and Facebook reviews into one feed, then drop its block into the Reviews section. Needs Jake's call on the app.
