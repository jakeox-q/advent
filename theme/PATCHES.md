# Edits to Enterprise's own files

The repo is public, so Enterprise's files are not committed. These are the only changes made to them on the `Advent build (dev)` theme. Re-apply them after a theme update.

1. `layout/theme.liquid`: after `{{ content_for_header }}` add
   `{{ 'advent.css' | asset_url | stylesheet_tag }}`
2. `snippets/product-card.liquid`: just before the closing `</div>` of `.card__info-container` (after the quick add block) add the staff note:
   ```liquid
   {%- if product.metafields.advent.staff_note != blank -%}
     <div class="advent-staff-note">
       <p class="advent-staff-note__text">{{ product.metafields.advent.staff_note | escape | newline_to_br }}</p>
       <p class="advent-staff-note__by">{{ 'advent.staff_note_byline' | t }}</p>
     </div>
   {%- endif -%}
   ```
   It is hidden by `advent.css` everywhere except the Staff recommendations section.
3. `locales/en.default.json`: add `"advent": { "staff_note_byline": "Dean, Advent Games" }` (editable in Edit theme content).
