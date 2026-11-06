# Build handoff: Advent Games on Shopify (Enterprise theme)

You're building the Advent Games design into a real Shopify theme. **Start with the home page** (plus the global header, footer and cart drawer it needs). Jake Oxley (Head of Web, Q Agency) will review it before any other page is built.

You don't need further instructions from Jake to start. Read the files below, check your access, then work through the steps.

## Read first, in this order

1. `handoff/context/design-phase-context.md`: the project, the client (Dean), scope, data and copy rules. Background only.
2. `handoff/design-tokens.md`: colours, type, spacing, buttons, cards and gradients.
3. `handoff/homepage-spec.md`: **the job.** Section by section: Enterprise section, settings, content, images, and what's native vs tweak vs custom.
4. The live design: https://advent.qagency.workers.dev/design/ (desktop and mobile). Turn on **Annotated** in the top bar to see the build note on each section. Same files are in `site/design/`, with images in `site/design/img/`.
5. `handoff/design-source/`: the generator for the design (`design.css` has every exact value, `build_home.py` the home page markup and copy, `common.py` the header, footer, card and icon SVGs, `menus.py` the mega menus, mobile drawer and search).
6. `handoff/theme-draft/`: an earlier unstyled draft of the home page JSON, header and footer groups and theme settings, using real Enterprise setting names. Use it as a starting point. The spec overrides it.

## The store

- **Dev store:** `advent-games-017wrq2h.myshopify.com`
- **Theme:** Enterprise by Clean Canvas, already on the store.
- **Never edit or publish the live theme.** Duplicate the base Enterprise theme and name it `Advent build (dev)`. Do all work there.
- **Don't add or edit products.** A demo product set exists and Dean's full import comes later. Collections and menus can be created or pointed at what exists. List anything missing in your report.
- Metafield definitions (`bgg.*`, `advent.*`, `rpg.*`) already exist. Don't change them.

## Tools

Check what you have before starting, and tell Jake straight away if something is missing.

- **Theme files: Shopify CLI** (`shopify theme pull / push / dev` against the dev theme). This is the most reliable way to edit theme code. If the CLI can't authenticate in this environment, ask Jake for a **Theme Access password** for the store (set it as `SHOPIFY_CLI_THEME_TOKEN`) or for the CLI login code.
- **Store data: Shopify MCP** (collections, menus, metafields, files). Make sure it's connected to the **Advent** store (it may be pointed at another client's store; use its switch-shop tool).
- **Claude in Chrome:** for anything only the theme editor can do, for checking the preview, and for side-by-side screenshots against the design. Playwright also works for screenshots if the preview is reachable (the dev store may need its storefront password from Jake).
- **Images:** upload design images from `site/design/img/` to Shopify Files (MCP or theme editor) and reference them as `shopify://shop_images/<name>`.

## How to work

1. **Set up:** duplicate the theme, pull it into `theme/` in this repo, and work on a branch `build/home`. Check whether the repo is private first (`gh repo view --json visibility`). If it's public, don't commit Enterprise's own files: commit only our files (`assets/advent.css`, `templates/index.json`, the group JSON, `config/settings_data.json` and any new sections or snippets), and add the rest to `.gitignore`.
2. **Global first:** theme settings, then the header group (announcement, header and mega menus, trust strip), then the footer group (newsletter, footer). Then the cart drawer settings.
3. **Then the home page sections, top to bottom.** One section at a time: build it, push to the dev theme, screenshot it at 1440px and 390px next to the same section of the design, fix what's off, commit (`Home: <section name>`).
4. **CSS rules:** all our CSS goes in one `assets/advent.css` (included once in `layout/theme.liquid`) or in a section's Custom CSS setting. Scope selectors to the section. Don't edit Enterprise's core CSS or JS. Use theme settings before CSS, and CSS before Liquid.
5. **Native first.** If something marked `native` needs code, or something marked `tweak` turns out to need a custom section, stop and flag it to Jake with the reason and a rough effort. Don't quietly build custom work.
6. **Anything custom must be editable** by a non-technical person through section settings and blocks: no hard-coded copy, images or links.
7. **Mobile follows Enterprise's native layout.** Match the design's sizes where settings or light CSS allow, and don't build custom mobile layouts.

## Rules

- Australian English, no em dashes, plain and friendly copy. Use the copy from the spec exactly. Don't invent copy. Mark gaps as `[Dean to write]` in the Shopify field, not on the live page.
- Don't comment in BugHerd, don't email or message the client, and don't publish anything.
- Ask Jake before anything irreversible (deleting themes, files, menus or collections that already existed).
- Keep commits small, one section each.

## Report back to Jake

When the home page is done (or if you're blocked), send:
- the **preview link** for the dev theme
- a short list of the sections: done / done with differences (what and why) / flagged / blocked
- side-by-side screenshots (design vs build) at desktop and mobile for any section that differs
- what's missing in the store (collections, menus, images, apps) and what Dean or Jake needs to supply
- any spec point you think is wrong or impossible natively, with a suggestion

After Jake signs off the home page, the remaining pages follow the same pattern. Their designs are already live at the link above (collections, product pages, brands, about, help, search, blog, article and wishlist). Jake will ask for page specs in the same format.
