# Edits to Enterprise's own files

The repo is public, so Enterprise's files are not committed. These are the only changes made to them on the `Advent build (dev)` theme. Re-apply them after a theme update.

1. `layout/theme.liquid`: after `{{ content_for_header }}` add
   `{{ 'advent.css' | asset_url | stylesheet_tag }}`
2. `snippets/product-card.liquid`: just before the closing `</div>` of `.card__info-container` (after the quick add block) add
   `{%- render 'advent-staff-note', product: product -%}`
   The markup lives in our own `snippets/advent-staff-note.liquid`. It is hidden by `advent.css` everywhere except the Staff recommendations section.
3. `locales/en.default.json`: add `"advent": { "staff_note_byline": "Dean, Advent Games" }` (editable in Edit theme content).
