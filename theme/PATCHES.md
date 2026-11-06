# Edits to Enterprise's own files

The repo is public, so Enterprise's files are not committed. These are the only changes made to them on the `Advent build (dev)` theme. Re-apply them after a theme update.

1. `layout/theme.liquid`: after `{{ content_for_header }}` add
   `{{ 'advent.css' | asset_url | stylesheet_tag }}`
2. `snippets/product-card.liquid`: just before the closing `</div>` of `.card__info-container` (after the quick add block) add
   `{%- render 'advent-staff-note', product: product -%}`
   The markup lives in our own `snippets/advent-staff-note.liquid`. It is hidden by `advent.css` everywhere except the Staff recommendations section.
3. `locales/en.default.json`: add `"advent": { "staff_note_byline": "Dean, Advent Games" }` (editable in Edit theme content).
4. `snippets/product-card.liquid` (two more hooks):
   - after the `product-label` render in `.card__media`: `{%- render 'advent-card-badges', product: product -%}`
   - after the top `price` render: `{%- render 'advent-card-stats', product: product -%}`
   Enterprise's own card labels are off (Theme settings > Product labels > position: none) so badges don't double up.
5. `sections/featured-collection.liquid`, `sections/product-list.liquid`, `sections/collection-list.liquid`: a text setting `advent_subheading` ("Subheading") after `title` in the schema, rendered after the section `</h2>` as `<p class="advent-section-sub">`.
6. `sections/announcement.liquid`: settings `link3` and `link3_label` after `link2_label`, rendered after link 2 (spacer classes adjusted so the last link has `no-spacer`).
7. `locales/en.default.json`: `advent.badges.*` and `advent.stats.*` wording for the card badges and stats row.
8. `locales/en.default.json`: `advent.wishlist.add` / `advent.wishlist.remove` labels for the card heart. The heart itself is ours (`snippets/advent-wishlist-heart.liquid`, `assets/advent-wishlist.js`), rendered from `snippets/advent-card-badges.liquid`. It saves to the shopper's browser until a wishlist app is chosen; remove its render line to take it out.
