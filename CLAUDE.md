# Advent Games repo

This repo holds the Advent Games wireframes and design (served from Cloudflare at https://advent.qagency.workers.dev) and the handoff for the Shopify build.

**If you've been asked to build the Shopify theme, or weren't given a specific task: read `handoff/README.md` first and follow it.** It explains the job (starting with the home page), the store, the tools, the rules and how to report back. You don't need further instructions to begin.

Repo layout:
- `handoff/`: build brief, design tokens, home page spec, earlier theme draft JSON, and the design's source files.
- `site/design/`: the finished design pages and images (deployed). Don't change these as part of the build.
- `site/` and `build.py`: the older greyscale wireframes (deployed). Don't change these.
- Pushing to `main` deploys `site/` to Cloudflare. Do build work on a branch.

House rules: Australian English, no em dashes, native Enterprise sections first, never publish or edit the live theme, never add products, never comment in BugHerd or contact the client.
