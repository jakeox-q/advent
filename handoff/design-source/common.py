# Shared pieces for the Advent Games design drafts (header, footer, cards, page shell).
import os, html
ROOT = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ icons (1.6px stroke line icons)
def I(name, size=16, cls=""):
    paths = {
        "users": '<circle cx="9" cy="8" r="3.2"/><path d="M3 19c0-3.3 2.7-5.5 6-5.5s6 2.2 6 5.5"/><circle cx="17" cy="9" r="2.4"/><path d="M16 13.6c2.8 0 5 1.9 5 4.9"/>',
        "clock": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
        "person": '<circle cx="12" cy="7" r="3.2"/><path d="M6 20v-3.5C6 13.5 8.7 12 12 12s6 1.5 6 4.5V20"/>',
        "brain": '<path d="M4 16a8 8 0 0 1 16 0"/><path d="M12 16l4-5"/><circle cx="12" cy="16" r="1.4"/>',
        "truck": '<path d="M3 7h10v9H3z"/><path d="M13 10h4l3 3v3h-7"/><circle cx="7" cy="17" r="1.8"/><circle cx="17" cy="17" r="1.8"/>',
        "map": '<path d="M12 21s-6-5.3-6-10a6 6 0 0 1 12 0c0 4.7-6 10-6 10z"/><circle cx="12" cy="11" r="2.2"/>',
        "chat": '<path d="M4 5h16v11H9l-5 4V5z"/>',
        "cards": '<rect x="3.5" y="6" width="10" height="14" rx="1.5" transform="rotate(-10 8.5 13)"/><rect x="10" y="4" width="10" height="14" rx="1.5" transform="rotate(8 15 11)"/>',
        "award": '<circle cx="12" cy="9" r="5.5"/><path d="M8.5 13.5L7 21l5-2.5 5 2.5-1.5-7.5"/><path d="M12 6.5l.9 1.8 2 .3-1.45 1.4.35 2-1.8-.95-1.8.95.35-2L9.1 8.6l2-.3z"/>',
        "hex": '<path d="M12 3l7.5 4.3v8.6L12 20.2l-7.5-4.3V7.3z"/><path d="M12 8.2l3.3 1.9v3.8L12 15.8l-3.3-1.9v-3.8z"/>',
        "trophy": '<path d="M7 4h10v5a5 5 0 0 1-10 0z"/><path d="M7 6H4v1.5A3.5 3.5 0 0 0 7.5 11M17 6h3v1.5a3.5 3.5 0 0 1-3.5 3.5"/><path d="M12 14v3M8.5 20h7l-1-3h-5z"/>',
        "p1": '<circle cx="12.00" cy="6.78" r="3.74"/><path d="M5.40 18.22a6.60 6.60 0 0 1 13.20 0"/>',
        "p2": '<circle cx="7.60" cy="8.73" r="2.46"/><path d="M3.25 16.27a4.35 4.35 0 0 1 8.70 0"/><circle cx="16.40" cy="8.73" r="2.46"/><path d="M12.05 16.27a4.35 4.35 0 0 1 8.70 0"/>',
        "p4": '<circle cx="8.20" cy="5.70" r="1.70"/><path d="M5.20 10.90a3.00 3.00 0 0 1 6.00 0"/><circle cx="15.80" cy="5.70" r="1.70"/><path d="M12.80 10.90a3.00 3.00 0 0 1 6.00 0"/><circle cx="8.20" cy="14.20" r="1.70"/><path d="M5.20 19.40a3.00 3.00 0 0 1 6.00 0"/><circle cx="15.80" cy="14.20" r="1.70"/><path d="M12.80 19.40a3.00 3.00 0 0 1 6.00 0"/>',
        "p6": '<circle cx="5.60" cy="6.17" r="1.39"/><path d="M3.14 10.43a2.46 2.46 0 0 1 4.92 0"/><circle cx="12.00" cy="6.17" r="1.39"/><path d="M9.54 10.43a2.46 2.46 0 0 1 4.92 0"/><circle cx="18.40" cy="6.17" r="1.39"/><path d="M15.94 10.43a2.46 2.46 0 0 1 4.92 0"/><circle cx="5.60" cy="14.47" r="1.39"/><path d="M3.14 18.73a2.46 2.46 0 0 1 4.92 0"/><circle cx="12.00" cy="14.47" r="1.39"/><path d="M9.54 18.73a2.46 2.46 0 0 1 4.92 0"/><circle cx="18.40" cy="14.47" r="1.39"/><path d="M15.94 18.73a2.46 2.46 0 0 1 4.92 0"/>',
        "mini": '<circle cx="12" cy="5.2" r="2.2"/><path d="M9.2 9.2h5.6l-.8 5.3H10z"/><path d="M8 12l1.6-2.4M16 12l-1.6-2.4"/><path d="M10 14.5l-1 3.5h6l-1-3.5"/><ellipse cx="12" cy="19.5" rx="6.5" ry="1.8"/>',
        "deck": '<rect x="4" y="7" width="9" height="13" rx="1.5" transform="rotate(-14 8.5 13.5)"/><rect x="7.5" y="5.5" width="9" height="13" rx="1.5"/><rect x="11" y="7" width="9" height="13" rx="1.5" transform="rotate(14 15.5 13.5)"/>',
        "x": '<path d="M6 6l12 12M18 6L6 18"/>',
        "lock": '<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
        "search": '<circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/>',
        "user": '<circle cx="12" cy="8" r="3.6"/><path d="M4.5 20c0-3.6 3.4-6 7.5-6s7.5 2.4 7.5 6"/>',
        "heart": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
        "cart": '<path d="M3 4h2.5l2 11h10l2-7H6"/><circle cx="9" cy="19" r="1.4"/><circle cx="16.5" cy="19" r="1.4"/>',
        "star": '<path d="M12 3.5l2.6 5.4 5.9.8-4.3 4.1 1 5.8L12 16.8l-5.2 2.8 1-5.8-4.3-4.1 5.9-.8z"/>',
        "chev": '<path d="M6 9l6 6 6-6"/>',
        "left": '<path d="M15 5l-7 7 7 7"/>',
        "right": '<path d="M9 5l7 7-7 7"/>',
        "gift": '<rect x="3" y="9" width="18" height="11" rx="1.5"/><path d="M3 13h18M12 9v11M7.5 9c-2 0-3-1.2-3-2.5S6 4 7.5 4c2 0 4.5 5 4.5 5s2.5-5 4.5-5c1.5 0 3 1.2 3 2.5S18.5 9 16.5 9"/>',
        "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
        "meeple": '<path d="M12 3.5c-1.8 0-3 1.4-3 3.2 0 1 .4 1.9 1 2.5L5 12.5c-.8.5-1 1.3-.6 2l.4.7c.4.6 1.2.8 1.9.4l2.3-1.3-1.4 5.2c-.2.6.3 1.3 1 1.3h6.8c.7 0 1.2-.7 1-1.3l-1.4-5.2 2.3 1.3c.7.4 1.5.2 1.9-.4l.4-.7c.4-.7.2-1.5-.6-2l-5-3.3c.6-.6 1-1.5 1-2.5 0-1.8-1.2-3.2-3-3.2z"/>',
        "book": '<path d="M12 6.5c-1.6-1.4-4-2-7.5-2v13c3.5 0 5.9.6 7.5 2 1.6-1.4 4-2 7.5-2v-13c-3.5 0-5.9.6-7.5 2z"/><path d="M12 6.5v13"/><path d="M7 8.5c1.3 0 2.3.2 3.2.6M7 11.5c1.3 0 2.3.2 3.2.6M13.8 9.1c.9-.4 1.9-.6 3.2-.6M13.8 12.1c.9-.4 1.9-.6 3.2-.6"/>',
        "family": '<path d="M5.5 5c-1.1 0-1.9.9-1.9 2 0 .7.3 1.2.7 1.6L1.8 10.3c-.5.3-.6.8-.3 1.3l.2.4c.3.4.8.5 1.2.3l1.1-.6-.8 3.2c-.1.4.2.8.6.8h3.4c.4 0 .7-.4.6-.8l-.8-3.2 1.1.6c.4.2.9.1 1.2-.3l.2-.4c.3-.5.2-1-.3-1.3L7.7 8.6c.4-.4.7-.9.7-1.6 0-1.1-.8-2-1.9-2z"/><path d="M18.5 5c-1.1 0-1.9.9-1.9 2 0 .7.3 1.2.7 1.6l-2.5 1.7c-.5.3-.6.8-.3 1.3l.2.4c.3.4.8.5 1.2.3l1.1-.6-.8 3.2c-.1.4.2.8.6.8h3.4c.4 0 .7-.4.6-.8l-.8-3.2 1.1.6c.4.2.9.1 1.2-.3l.2-.4c.3-.5.2-1-.3-1.3l-2.5-1.7c.4-.4.7-.9.7-1.6 0-1.1-.8-2-1.9-2z"/><path d="M12 11.5c-.8 0-1.4.6-1.4 1.4 0 .5.2.9.5 1.2l-1.8 1.2c-.4.2-.5.7-.2 1l.1.3c.2.3.6.4.9.2l.8-.4-.6 2.4c-.1.3.2.6.5.6h2.4c.3 0 .5-.3.5-.6l-.6-2.4.8.4c.3.2.7.1.9-.2l.1-.3c.2-.4.1-.8-.2-1l-1.8-1.2c.3-.3.5-.7.5-1.2 0-.8-.6-1.4-1.4-1.4z"/>',
        "mind": '<path d="M9.5 4.5a3 3 0 0 0-3 3 2.8 2.8 0 0 0-2 2.7c0 .9.4 1.6 1 2.1a2.8 2.8 0 0 0 1.2 4.6 3 3 0 0 0 5.3 1.1V5.6a3 3 0 0 0-2.5-1.1z"/><path d="M14.5 4.5a3 3 0 0 1 3 3 2.8 2.8 0 0 1 2 2.7c0 .9-.4 1.6-1 2.1a2.8 2.8 0 0 1-1.2 4.6 3 3 0 0 1-5.3 1.1V5.6a3 3 0 0 1 2.5-1.1z"/><path d="M12 5.6V18"/><path d="M6.5 7.5c.5.8 1.3 1.2 2.2 1.3M17.5 7.5c-.5.8-1.3 1.2-2.2 1.3M5.5 12.3c1 .3 1.8.9 2.3 1.7M18.5 12.3c-1 .3-1.8.9-2.3 1.7"/>',
        "tank": '<path d="M3 15.5a3 3 0 0 1 3-3h12a3 3 0 0 1 0 6H6a3 3 0 0 1-3-3z"/><circle cx="6.5" cy="15.5" r="1"/><circle cx="10" cy="15.5" r="1"/><circle cx="13.5" cy="15.5" r="1"/><circle cx="17" cy="15.5" r="1"/><path d="M7.5 12.5V10a2 2 0 0 1 2-2h5a2 2 0 0 1 2 2v2.5"/><path d="M14 9h7"/><path d="M11.5 8V6.5"/>',
        "d20": '<path d="M12 2.5l8.5 5v9l-8.5 5-8.5-5v-9z"/><path d="M12 2.5l-4.5 11h9z"/><path d="M3.5 7.5l4 6-4 3M20.5 7.5l-4 6 4 3M7.5 13.5l4.5 8 4.5-8"/>',
        "crown": '<path d="M4 17h16l1-10-5 4-4-6-4 6-5-4z"/><path d="M4 17v2.5h16V17"/>',
        "party": '<path d="M5 21l4-12 8 8z"/><path d="M9 9c0-2.5 2-4 4-4"/><path d="M13 5c1.5-1.5 3.5-1 4.5.5"/><path d="M17 11c2 .5 3 2 3 3.5"/><circle cx="18" cy="4.5" r="1"/><circle cx="20.5" cy="9" r="1"/><circle cx="14" cy="2.5" r=".8"/>',
        "shield": '<path d="M12 3l7.5 3v6c0 4.5-3.2 7.8-7.5 9-4.3-1.2-7.5-4.5-7.5-9V6z"/><path d="M8.5 12.5l2.5 2.5 4.5-5"/>',
        "duel": '<path d="M6.5 6.5c-1.2 0-2 .9-2 2.1 0 .7.3 1.3.7 1.7L2.4 12.4c-.5.3-.7.9-.4 1.4l.2.4c.3.5.9.6 1.3.3l1.2-.7-.9 3.4c-.1.5.2.8.6.8h4.2c.4 0 .7-.3.6-.8l-.9-3.4 1.2.7c.4.3 1 .2 1.3-.3l.2-.4c.3-.5.1-1.1-.4-1.4l-2.8-1.9c.4-.4.7-1 .7-1.7 0-1.2-.8-2.1-2-2.1z"/><path d="M17.5 6.5c-1.2 0-2 .9-2 2.1 0 .7.3 1.3.7 1.7l-2.8 1.9c-.5.3-.7.9-.4 1.4l.2.4c.3.5.9.6 1.3.3l1.2-.7-.9 3.4c-.1.5.2.8.6.8h4.2c.4 0 .7-.3.6-.8l-.9-3.4 1.2.7c.4.3 1 .2 1.3-.3l.2-.4c.3-.5.1-1.1-.4-1.4l-2.8-1.9c.4-.4.7-1 .7-1.7 0-1.2-.8-2.1-2-2.1z"/>',
        "swords": '<path d="M4 4l10 10M20 4L10 14M4 20l3-3M20 20l-3-3M6 18l-2 2M18 18l2 2M14 14l3 3M10 14l-3 3"/>',
        "dice": '<rect x="3.5" y="3.5" width="17" height="17" rx="3.5"/><circle cx="8" cy="8" r="1.3"/><circle cx="16" cy="8" r="1.3"/><circle cx="12" cy="12" r="1.3"/><circle cx="8" cy="16" r="1.3"/><circle cx="16" cy="16" r="1.3"/>',
        "blocks": '<rect x="3.5" y="12.5" width="8" height="8" rx="1.2"/><rect x="12.5" y="12.5" width="8" height="8" rx="1.2"/><rect x="8" y="4" width="8" height="8" rx="1.2"/><path d="M6 15.5l1 2.5M8 15.5l-1 2.5"/><circle cx="16.5" cy="16.5" r="1.5"/><path d="M12 6.5l.7 1.4 1.5.2-1.1 1 .3 1.5-1.4-.7-1.4.7.3-1.5-1.1-1 1.5-.2z"/>',
        "balloon": '<path d="M12 3c-3.3 0-5.5 2.6-5.5 5.8 0 3.6 3 6.7 5.5 6.7s5.5-3.1 5.5-6.7C17.5 5.6 15.3 3 12 3z"/><path d="M12 15.5l-1 2h2z"/><path d="M12 17.5c0 2-1.5 2.5-1.5 4"/>',
        "puzzle": '<path d="M9.5 4.5a2 2 0 0 1 4 0V6h3.5a1 1 0 0 1 1 1v3.5h1.5a2 2 0 0 1 0 4H18V18a1 1 0 0 1-1 1h-3.5v-1.5a2 2 0 0 0-4 0V19H6a1 1 0 0 1-1-1v-3.5h1.5a2 2 0 0 0 0-4H5V7a1 1 0 0 1 1-1h3.5V4.5z"/>',
        "box": '<path d="M3 8l9-4 9 4-9 4-9-4z"/><path d="M3 8v8l9 4 9-4V8"/><path d="M12 12v8"/>',
        "calendar": '<rect x="3.5" y="5" width="17" height="15" rx="2"/><path d="M3.5 10h17M8 3v4M16 3v4"/>',
        "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
        "play": '<circle cx="12" cy="12" r="9"/><path d="M10 8.6l5.6 3.4-5.6 3.4z" fill="currentColor"/>',
        "playf": '<path d="M8 5.5l11 6.5-11 6.5z" fill="currentColor" stroke="none"/>',
        "grid": '<rect x="4" y="4" width="7" height="7" rx="1.2"/><rect x="13" y="4" width="7" height="7" rx="1.2"/><rect x="4" y="13" width="7" height="7" rx="1.2"/><rect x="13" y="13" width="7" height="7" rx="1.2"/>',
        "list": '<path d="M9 6h11M9 12h11M9 18h11"/><circle cx="5" cy="6" r="1"/><circle cx="5" cy="12" r="1"/><circle cx="5" cy="18" r="1"/>',
        "filter": '<path d="M4 6h16M7 12h10M10 18h4"/>',
        "bell": '<path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z"/><path d="M10 20a2 2 0 0 0 4 0"/>',
    }
    return (f'<svg class="ic {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[name]}</svg>')

def star():
    return f'<svg class="ic star" width="12" height="12" viewBox="0 0 24 24" aria-hidden="true">{I("star")[I("star").index(">")+1:I("star").rindex("<")]}</svg>'

# ------------------------------------------------------------------ annotation helpers
def tag(name, kind="native", note=""):
    label = {"native": "Enterprise section", "tweak": "native + tweak", "custom": "custom / app"}[kind]
    n = f'<span class="an-note">{note}</span>' if note else ""
    return f'<div class="an"><span class="an-tag an-{kind}" title="{label}">{name}</span>{n}</div>'

# ------------------------------------------------------------------ product card (ProductCard from the design system)
def card(img, title, vendor, price, state="in", badge="", rrp="", meta=None, year="", rating="", eta="", exp=False, link=None, note="", line="", page=None):
    info = line
    if link is None:
        page = page or ("product-expansion.html" if exp else "product.html")
        link = page + ("" if state == "in" else f"?state={state}")
    states = {
        "in": ("in", "In stock", "", "Add to cart", "primary"),
        "sup": ("supplier", "Available from supplier", "Ships in 2-7 business days", "Add to cart", "primary"),
        "pre": ("preorder", "Preorder", "", "Preorder now", "primary"),
        "soon": ("coming", "Coming soon", f"Expected {eta}" if eta else "", "Preorder now", "primary"),
        "out": ("out", "Out of stock", "", "Notify me", "secondary"),
    }
    k, line, sub, btn, bstyle = states[state]
    badges = ""
    bk = {"Just arrived": "new", "Preorder": "preorder", "Coming soon": "coming", "Sale": "sale", "Back in stock": "restock", "Dings & dents": "dings"}
    if badge: badges += f'<span class="ag-badge ag-badge--{bk[badge]}">{badge}</span>'
    if exp: badges += f'<span class="ag-badge ag-badge--expansion">{I("puzzle",12)}Expansion</span>'
    ratingh = f'<span class="ag-rating bgg-{int(float(rating))}">{star()} {rating}</span>' if rating else ""
    stats = ""
    if meta:
        p, t, a, c = meta
        stats = (f'<div class="ag-card__stats">'
                 f'<span title="Players">{I("users",14)}{p}</span><span title="Play time">{I("clock",14)}{t}</span>'
                 f'<span title="Complexity">{I("mind",14)}{c}<em>/5</em></span></div>')
    was = f'<span class="ag-price__was">RRP ${int(float(rrp))}</span>' if rrp else ""
    if info: stats = f'<div class="ag-card__stats ag-card__stats--line">{info}</div>'
    sale = " ag-price--sale" if badge == "Sale" else ""
    sub_h = f'<span class="ag-avail__sub">{sub}</span>' if sub else ""
    noteh = f'<div class="staff-note"><p>{note}</p><span class="staff-who">{I("chat",14)} Dean, Advent Games</span></div>' if note else ""
    return f'''<article class="ag-card">
  <a class="ag-card__media" href="{link}"><img src="img/{img}.jpg" alt="{html.escape(title)} box art" loading="lazy"><div class="ag-card__badges">{badges}</div></a>
  <button class="ag-card__fav" aria-label="Add {html.escape(title)} to wishlist">{I("heart",16)}</button>
  <div class="ag-card__body">
    <div class="ag-card__top"><span class="ag-card__vendor">{vendor}</span></div>
    <h3 class="ag-card__title"><a href="{link}">{title}</a></h3>
    <div class="ag-card__price"><span class="ag-price{sale}">${price}</span>{was}</div>
    {stats}
    <div class="ag-card__stock"><span class="ag-avail ag-avail--{k}">{line}</span>{sub_h}</div>
  </div>
  <div class="ag-card__action"><button class="ag-btn ag-btn--{bstyle} ag-btn--block ag-btn--sm">{btn}</button></div>
  {noteh}
</article>'''

def carousel(cards, cols=5):
    return (f'<div class="carousel"><div class="track" style="--cols:{cols}">{"".join(cards)}</div>'
            f'<div class="car-nav"><button class="car-btn" aria-label="Previous">{I("left",18)}</button><button class="car-btn" aria-label="Next">{I("right",18)}</button></div></div>')

def sec_head(h2, sub="", link="", link_label="View all", eyebrow=""):
    e = f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else ""
    s = f'<p class="sub">{sub}</p>' if sub else ""
    l = f'<a class="view-all" href="{link}">{link_label} {I("right",14)}</a>' if link else ""
    return f'<div class="sec-head"><div>{e}<h2 class="h2">{h2}</h2>{s}</div>{l}</div>'


NAV = [("Preorders", True, "collection-preorders.html"), ("Just Arrived", True, "collection-preorders.html"), ("Board Games", True, "collection.html"), ("Roleplaying", True, "collection-rpg.html"), ("Accessories", True, "collection-accessories.html"), ("Sale", True, "collection.html")]

PAGES = [("index.html", "Home"), ("collection.html", "Collection: Board games"), ("collection-preorders.html", "Collection: Preorders"),
         ("collection-rpg.html", "Collection: Roleplaying"), ("collection-accessories.html", "Collection: Accessories"),
         ("product.html", "Product: Board game"), ("product-expansion.html", "Product: Expansion"), ("product-rpg.html", "Product: RPG"), ("product-accessory.html", "Product: Accessory"),
         ("brands.html", "Brands A-Z"), ("brand.html", "Brand collection"), ("about.html", "About + Contact"), ("help.html", "Help & FAQ"),
         ("search.html", "Search results"), ("blog.html", "Blog"), ("article.html", "Blog post"), ("wishlist.html", "Wishlist (optional app)")]

def _menus():
    import menus
    return menus

def header_html():
    return f'''<!-- ============ HEADER GROUP ============ -->
<div class="announce-wrap">{tag("Announcement bar", "tweak", "site message left · utility links right · brand orange · two text fields: desktop message + short mobile message (extra block setting, swapped by CSS)")}
<div class="ag-announce"><div class="inner"><span class="an-desk"><strong>Flat rate shipping</strong> $10 Sydney Metro, Gosford &amp; Wollongong · $15 rest of Australia · <strong>Free over $300</strong></span><span class="an-mob"><strong>Shipping</strong> $10 Sydney · $15 Australia · <strong>Free $300+</strong></span>
<nav><a href="help.html">Help &amp; FAQ</a><a href="help.html#orders">Track my order</a><a href="brands.html">Brands A-Z</a></nav></div></div></div>

<header class="hdr">
  {tag("Header", "native", "sticky (native Enterprise: logo, search and icons stay; menu row returns on scroll up) · logo = home · search with category dropdown · account, wishlist, cart")}
  <div class="inner hdr-main">
    <button class="burger" aria-label="Menu">{I("menu",22)}</button>
    <a class="logo" href="index.html" aria-label="Advent Games home"><img class="logo-std" src="img/advent-logo.png" alt="Advent Games"><img class="logo-h" src="img/advent-logo-h.png" alt="Advent Games"></a>
    <form class="search" role="search" onsubmit="return false">
      <label class="sr" for="cat">Category</label>
      <select id="cat" class="search-cat"><option>All</option><option>Board games</option><option>Expansions</option><option>Roleplaying</option><option>Accessories</option></select>
      <label class="sr" for="q">Search</label>
      <input id="q" class="search-in" type="search" placeholder="Search 11,000+ games, publishers, designers...">
      <button class="search-btn" aria-label="Search">{I("search",20)}</button>
    </form>
    <div class="hdr-icons">
      <a href="#">{I("user",22)}<span>Account</span></a>
      <a href="wishlist.html">{I("heart",22)}<span>Wishlist</span></a>
      <a href="#" class="cart">{I("cart",22)}<span>Cart</span><b class="count">2</b></a>
    </div>
  </div>
  <div class="nav-row"><nav class="inner nav" aria-label="Main">
    <ul>{"".join(f'<li data-key="{k}"><a href="{h}" aria-haspopup="true" aria-expanded="false">{l}{I("chev",14) if c else ""}</a></li>' for (l, c, h), k in zip(NAV, ["preorders","arrived","board","rpg","acc","sale"]))}</ul>
    <div class="nav-aux"><a href="help.html#shipping">Shipping &amp; pickup</a><a href="about.html">About</a></div>
  </nav>{_menus().mega_panels()}</div>
  {_menus().search_panel()}
</header>

<section class="trust-wrap">{tag("Icons with text", "native", "header group trust strip · 4 items · one-at-a-time slider on mobile")}
<div class="inner trust-wrap-inner"><button class="trust-arrow trust-prev" aria-label="Previous">{I("left",18)}</button><div class="ag-trust">
  <div class="ag-trust__item"><span class="ag-trust__icon">{I("truck",20)}</span><div><strong>Free shipping over $300</strong><span>$10 Sydney Metro · $15 Australia-wide</span></div></div>
  <div class="ag-trust__item"><span class="ag-trust__icon ag-trust__icon--logo"><img src="img/auspost-logo-slot.svg" alt="Australia Post"></span><div><strong>Australia-wide via AusPost</strong><span>Tracked, boxed and padded</span></div></div>
  <div class="ag-trust__item"><span class="ag-trust__icon">{I("chat",20)}</span><div><strong>Friendly, local service</strong><span>You'll hear back from Dean</span></div></div>
  <div class="ag-trust__item"><span class="ag-trust__icon">{I("lock",20)}</span><div><strong>Secure checkout</strong><span>Card, PayPal or bank transfer</span></div></div>
</div><button class="trust-arrow trust-next" aria-label="Next">{I("right",18)}</button></div></section>'''

def footer_html():
    return f'''<!-- ============ FOOTER GROUP ============ -->
<section class="newsletter">{tag("Newsletter", "tweak", "Mailchimp list · orange-to-sun gradient (colour scheme) · floating icons right side via CSS/SVG (decorative)")}
<div class="nl-float" aria-hidden="true">{I("dice",110,"nf nf-1")}{I("meeple",90,"nf nf-2")}{I("d20",100,"nf nf-3")}{I("crown",80,"nf nf-4")}{I("puzzle",96,"nf nf-5")}<span class="nl-dot nd-1"></span><span class="nl-dot nd-2"></span><span class="nl-dot nd-3"></span><span class="nl-dot nd-4"></span></div>
<div class="inner nl">
  <div><h2 class="h2">New releases and preorders, first.</h2><p>New arrivals, preorders and the odd special, straight to your inbox. No spam, unsubscribe any time.</p></div>
  <form class="nl-form" onsubmit="return false"><label class="sr" for="nl-email">Email address</label><input id="nl-email" class="ag-input" type="email" placeholder="Email address"><button class="ag-btn ag-btn--primary">Sign up</button></form>
</div></section>

<footer class="ftr">{tag("Footer", "native", "sky-to-blue gradient footer (colour scheme background gradient setting) · logo + line · 3 link columns · Shopify payment icons · Powered by BGG logo slot bottom right")}
<div class="inner ftr-grid">
  <div class="ftr-brand"><img src="img/advent-logo.png" alt="Advent Games" class="ftr-logo"><p>Your friendly, local, online board game store. Sydney based, shipping Australia-wide.</p>
    <p class="small">dean@adventgames.com.au · 0411 017 162<br>Free pickup Tuesday nights, Chatswood</p></div>
  <details class="ftr-col" open><summary><h3 class="h4">Shop</h3>{I("chev",18)}</summary><ul><li><a href="collection-preorders.html">Preorders</a></li><li><a href="collection-preorders.html">Just Arrived</a></li><li><a href="collection.html">Board Games</a></li><li><a href="collection-rpg.html">Roleplaying</a></li><li><a href="collection-accessories.html">Accessories</a></li><li><a href="collection.html">Sale</a></li><li><a href="brands.html">Brands A-Z</a></li></ul></details>
  <details class="ftr-col" open><summary><h3 class="h4">Help</h3>{I("chev",18)}</summary><ul><li><a href="help.html#shipping">Shipping &amp; pickup</a></li><li><a href="help.html#preorders">How preorders work</a></li><li><a href="help.html#returns">Returns &amp; damages</a></li><li><a href="help.html">FAQ</a></li><li><a href="help.html#orders">Track my order</a></li><li><a href="about.html#contact">Contact</a></li></ul></details>
  <details class="ftr-col" open><summary><h3 class="h4">Advent Games</h3>{I("chev",18)}</summary><ul><li><a href="about.html">About us</a></li><li><a href="help.html#preorders">Special orders</a></li><li><a href="blog.html">News &amp; reviews</a></li><li><a href="wishlist.html">Wishlist</a></li><li><a href="#">Gift cards</a></li></ul></details>
</div>
<div class="inner ftr-bottom">
  <p class="small">© 2026 Advent Games · ABN 76 649 386 212 · <a href="#">Privacy policy</a> · <a href="#">Terms &amp; conditions</a> · <a href="#">Refund policy</a></p>
  <div class="pay"><ul class="payment-icons"><li><svg class="w-12 h-auto pr-2 mt-2 space-y-2" xmlns="http://www.w3.org/2000/svg" role="img" viewBox="0 0 38 24" width="38" height="24" fill="none" aria-labelledby="pi-visa"><title id="pi-visa">Visa</title><rect x=".5" y=".5" width="37" height="23" rx="2.5" stroke="#000" stroke-opacity=".07" fill="none"/><path d="M35 0H3C1.3 0 0 1.3 0 3V21C0 22.7 1.4 24 3 24H35C36.7 24 38 22.7 38 21V3C38 1.3 36.6 0 35 0Z" fill="#142FBD" style="fill:#142FBD;fill:color(display-p3 0.0784 0.1843 0.7412);fill-opacity:1;"/><path d="M35 1C36.1 1 37 1.9 37 3V21C37 22.1 36.1 23 35 23H3C1.9 23 1 22.1 1 21V3C1 1.9 1.9 1 3 1H35Z" fill="#1532CB" style="fill:#1532CB;fill:color(display-p3 0.0824 0.1961 0.7961);fill-opacity:1;"/><path d="M29.5944 10.2167H29.2778C28.8556 11.2722 28.5389 11.8 28.2222 13.3833H30.2278C29.9111 11.8 29.9111 11.0611 29.5944 10.2167V10.2167ZM32.6556 16.4444H30.8611C30.7556 16.4444 30.7556 16.4444 30.65 16.3389L30.4389 15.3889L30.3333 15.1778H27.8C27.6944 15.1778 27.5889 15.1778 27.5889 15.3889L27.2722 16.3389C27.2722 16.4444 27.1667 16.4444 27.1667 16.4444H24.95L25.1611 15.9167L28.2222 8.73889C28.2222 8.21111 28.5389 8 29.0667 8H30.65C30.7556 8 30.8611 8 30.8611 8.21111L32.3389 15.0722C32.4444 15.4944 32.55 15.8111 32.55 16.2333C32.6556 16.3389 32.6556 16.3389 32.6556 16.4444V16.4444ZM18.5111 16.1278L18.9333 14.2278C19.0389 14.2278 19.1444 14.3333 19.1444 14.3333C19.8833 14.65 20.6222 14.8611 21.3611 14.7556C21.5722 14.7556 21.8889 14.65 22.1 14.5444C22.6278 14.3333 22.6278 13.8056 22.2056 13.3833C21.9944 13.1722 21.6778 13.0667 21.3611 12.8556C20.9389 12.6444 20.5167 12.4333 20.2 12.1167C18.9333 11.0611 19.3556 9.58333 20.0944 8.84444C20.7278 8.42222 21.0444 8 21.8889 8C23.1556 8 24.5278 8 25.1611 8.21111H25.2667C25.1611 8.84444 25.0556 9.37222 24.8444 10.0056C24.3167 9.79444 23.7889 9.58333 23.2611 9.58333C22.9444 9.58333 22.6278 9.58333 22.3111 9.68889C22.1 9.68889 21.9944 9.79444 21.8889 9.9C21.6778 10.1111 21.6778 10.4278 21.8889 10.6389L22.4167 11.0611C22.8389 11.2722 23.2611 11.4833 23.5778 11.6944C24.1056 12.0111 24.6333 12.5389 24.7389 13.1722C24.95 14.1222 24.6333 14.9667 23.7889 15.6C23.2611 16.0222 23.05 16.2333 22.3111 16.2333C20.8333 16.2333 19.6722 16.3389 18.7222 16.0222C18.6167 16.2333 18.6167 16.2333 18.5111 16.1278V16.1278ZM14.8167 16.4444C14.9222 15.7056 14.9222 15.7056 15.0278 15.3889C15.5556 13.0667 16.0833 10.6389 16.5056 8.31667C16.6111 8.10556 16.6111 8 16.8222 8H18.7222C18.5111 9.26667 18.3 10.2167 17.9833 11.3778C17.6667 12.9611 17.35 14.5444 16.9278 16.1278C16.9278 16.3389 16.8222 16.3389 16.6111 16.3389L14.8167 16.4444ZM5 8.21111C5 8.10556 5.21111 8 5.31667 8H8.90556C9.43333 8 9.85556 8.31667 9.96111 8.84444L10.9111 13.4889C10.9111 13.5944 10.9111 13.5944 11.0167 13.7C11.0167 13.5944 11.1222 13.5944 11.1222 13.5944L13.3389 8.21111C13.2333 8.10556 13.3389 8 13.4444 8H15.6611C15.6611 8.10556 15.6611 8.10556 15.5556 8.21111L12.2833 15.9167C12.1778 16.1278 12.1778 16.2333 12.0722 16.3389C11.9667 16.4444 11.7556 16.3389 11.5444 16.3389H9.96111C9.85556 16.3389 9.75 16.3389 9.75 16.1278L8.06111 9.58333C7.85 9.37222 7.53333 9.05556 7.11111 8.95C6.47778 8.63333 5.31667 8.42222 5.10556 8.42222L5 8.21111Z" fill="white" style="fill:white;fill-opacity:1;"/></svg></li><li><svg class="w-12 h-auto pr-2 mt-2 space-y-2" xmlns="http://www.w3.org/2000/svg" role="img" viewBox="0 0 38 24" width="38" height="24" fill="none" aria-labelledby="pi-master"><title id="pi-master">Mastercard</title><rect x=".5" y=".5" width="37" height="23" rx="2.5" stroke="#000" stroke-opacity=".07" fill="none"/><path d="M35 0H3C1.3 0 0 1.3 0 3V21C0 22.7 1.4 24 3 24H35C36.7 24 38 22.7 38 21V3C38 1.3 36.6 0 35 0Z" fill="#1C1C1C" style="fill:#1C1C1C;fill:color(display-p3 0.1098 0.1098 0.1098);fill-opacity:1;"/><path d="M35 1C36.1 1 37 1.9 37 3V21C37 22.1 36.1 23 35 23H3C1.9 23 1 22.1 1 21V3C1 1.9 1.9 1 3 1H35Z" fill="#232323" style="fill:#232323;fill:color(display-p3 0.1373 0.1373 0.1373);fill-opacity:1;"/><path d="M14.6364 19.2727C18.8538 19.2727 22.2727 15.8538 22.2727 11.6364C22.2727 7.41892 18.8538 4 14.6364 4C10.4189 4 7 7.41892 7 11.6364C7 15.8538 10.4189 19.2727 14.6364 19.2727Z" fill="#EB001B" style="fill:#EB001B;fill:color(display-p3 0.9216 0.0000 0.1059);fill-opacity:1;"/><path d="M23.3637 19.2727C27.5811 19.2727 31 15.8538 31 11.6364C31 7.41892 27.5811 4 23.3637 4C19.1462 4 15.7273 7.41892 15.7273 11.6364C15.7273 15.8538 19.1462 19.2727 23.3637 19.2727Z" fill="#F79E1B" style="fill:#F79E1B;fill:color(display-p3 0.9686 0.6196 0.1059);fill-opacity:1;"/><path d="M22.2727 11.6362C22.2727 9.01797 20.9637 6.72706 19 5.41797C17.0364 6.83615 15.7273 9.12706 15.7273 11.6362C15.7273 14.1452 17.0364 16.5452 19 17.8543C20.9637 16.5452 22.2727 14.2543 22.2727 11.6362Z" fill="#FF5F00" style="fill:#FF5F00;fill:color(display-p3 1.0000 0.3725 0.0000);fill-opacity:1;"/></svg></li><li><svg class="w-12 h-auto pr-2 mt-2 space-y-2" xmlns="http://www.w3.org/2000/svg" role="img" viewBox="0 0 38 24" width="38" height="24" fill="none" aria-labelledby="pi-american_express"><title id="pi-american_express">American Express</title><rect x=".5" y=".5" width="37" height="23" rx="2.5" stroke="#000" stroke-opacity=".07" fill="none"/><path d="M35 0H3C1.3 0 0 1.3 0 3V21C0 22.7 1.4 24 3 24H35C36.7 24 38 22.7 38 21V3C38 1.3 36.6 0 35 0Z" fill="#0071CE" style="fill:#0071CE;fill:color(display-p3 0.0000 0.4431 0.8078);fill-opacity:1;"/><path d="M3 0.5H35C36.3348 0.5 37.5 1.58692 37.5 3V21C37.5 22.4239 36.4239 23.5 35 23.5H3C1.66524 23.5 0.5 22.4131 0.5 21V3C0.5 1.57614 1.57614 0.5 3 0.5Z" stroke="black" stroke-opacity="0.07" style="stroke:black;stroke-opacity:0.07;"/><path d="M25.8662 6.33203V3H31L31.8662 5.5332L32.7334 3H37V14.2002H36.7998L34.8672 16.2656L36.7998 18.3594H37V21.2666H33.5996L31.9336 19.3994L30.2002 21.2666H19.4668V12.666H16L20.2666 3H24.4004L25.8662 6.33203ZM20.5996 20.2656H27V18.5322H22.666V17.3994H26.8662V15.666H22.666V14.5322H27V12.7988H20.5996V20.2656ZM30.5332 16.5322L27 20.2656H29.5996L31.8662 17.8662L34.0664 20.2656H36.7324L33.1992 16.4658L36.7324 12.7988H34.1328L31.8662 15.1992L29.7324 12.7988H27L30.5332 16.5322ZM17.666 11.7324H19.9326L20.5332 10.1992H23.999L24.666 11.7324H26.999L23.666 4.19922H20.999L17.666 11.7324ZM33.5996 4.19922L31.9326 8.86621L30.1992 4.19922H27V11.666H29.0664V6.39941L31 11.666H32.7998L34.7324 6.39941V11.666H36.7324V4.13281L33.5996 4.19922ZM23.2656 8.46582H21.2656L22.2656 5.99902L23.2656 8.46582Z" fill="white" style="fill:white;fill-opacity:1;"/></svg></li><li><svg class="w-12 h-auto pr-2 mt-2 space-y-2" viewBox="0 0 38 24" xmlns="http://www.w3.org/2000/svg" width="38" height="24" role="img" aria-labelledby="pi-paypal"><title id="pi-paypal">PayPal</title><path opacity=".07" d="M35 0H3C1.3 0 0 1.3 0 3v18c0 1.7 1.4 3 3 3h32c1.7 0 3-1.3 3-3V3c0-1.7-1.4-3-3-3z"/><path fill="#fff" d="M35 1c1.1 0 2 .9 2 2v18c0 1.1-.9 2-2 2H3c-1.1 0-2-.9-2-2V3c0-1.1.9-2 2-2h32"/><path fill="#003087" d="M23.9 8.3c.2-1 0-1.7-.6-2.3-.6-.7-1.7-1-3.1-1h-4.1c-.3 0-.5.2-.6.5L14 15.6c0 .2.1.4.3.4H17l.4-3.4 1.8-2.2 4.7-2.1z"/><path fill="#3086C8" d="M23.9 8.3l-.2.2c-.5 2.8-2.2 3.8-4.6 3.8H18c-.3 0-.5.2-.6.5l-.6 3.9-.2 1c0 .2.1.4.3.4H19c.3 0 .5-.2.5-.4v-.1l.4-2.4v-.1c0-.2.3-.4.5-.4h.3c2.1 0 3.7-.8 4.1-3.2.2-1 .1-1.8-.4-2.4-.1-.5-.3-.7-.5-.8z"/><path fill="#012169" d="M23.3 8.1c-.1-.1-.2-.1-.3-.1-.1 0-.2 0-.3-.1-.3-.1-.7-.1-1.1-.1h-3c-.1 0-.2 0-.2.1-.2.1-.3.2-.3.4l-.7 4.4v.1c0-.3.3-.5.6-.5h1.3c2.5 0 4.1-1 4.6-3.8v-.2c-.1-.1-.3-.2-.5-.2h-.1z"/></svg></li><li><svg class="w-12 h-auto pr-2 mt-2 space-y-2" version="1.1" xmlns="http://www.w3.org/2000/svg" role="img" x="0" y="0" width="38" height="24" viewBox="0 0 165.521 105.965" xml:space="preserve" aria-labelledby="pi-apple_pay"><title id="pi-apple_pay">Apple Pay</title><path fill="#000" d="M150.698 0H14.823c-.566 0-1.133 0-1.698.003-.477.004-.953.009-1.43.022-1.039.028-2.087.09-3.113.274a10.51 10.51 0 0 0-2.958.975 9.932 9.932 0 0 0-4.35 4.35 10.463 10.463 0 0 0-.975 2.96C.113 9.611.052 10.658.024 11.696a70.22 70.22 0 0 0-.022 1.43C0 13.69 0 14.256 0 14.823v76.318c0 .567 0 1.132.002 1.699.003.476.009.953.022 1.43.028 1.036.09 2.084.275 3.11a10.46 10.46 0 0 0 .974 2.96 9.897 9.897 0 0 0 1.83 2.52 9.874 9.874 0 0 0 2.52 1.83c.947.483 1.917.79 2.96.977 1.025.183 2.073.245 3.112.273.477.011.953.017 1.43.02.565.004 1.132.004 1.698.004h135.875c.565 0 1.132 0 1.697-.004.476-.002.952-.009 1.431-.02 1.037-.028 2.085-.09 3.113-.273a10.478 10.478 0 0 0 2.958-.977 9.955 9.955 0 0 0 4.35-4.35c.483-.947.789-1.917.974-2.96.186-1.026.246-2.074.274-3.11.013-.477.02-.954.022-1.43.004-.567.004-1.132.004-1.699V14.824c0-.567 0-1.133-.004-1.699a63.067 63.067 0 0 0-.022-1.429c-.028-1.038-.088-2.085-.274-3.112a10.4 10.4 0 0 0-.974-2.96 9.94 9.94 0 0 0-4.35-4.35A10.52 10.52 0 0 0 156.939.3c-1.028-.185-2.076-.246-3.113-.274a71.417 71.417 0 0 0-1.431-.022C151.83 0 151.263 0 150.698 0z" /><path fill="#FFF" d="M150.698 3.532l1.672.003c.452.003.905.008 1.36.02.793.022 1.719.065 2.583.22.75.135 1.38.34 1.984.648a6.392 6.392 0 0 1 2.804 2.807c.306.6.51 1.226.645 1.983.154.854.197 1.783.218 2.58.013.45.019.9.02 1.36.005.557.005 1.113.005 1.671v76.318c0 .558 0 1.114-.004 1.682-.002.45-.008.9-.02 1.35-.022.796-.065 1.725-.221 2.589a6.855 6.855 0 0 1-.645 1.975 6.397 6.397 0 0 1-2.808 2.807c-.6.306-1.228.511-1.971.645-.881.157-1.847.2-2.574.22-.457.01-.912.017-1.379.019-.555.004-1.113.004-1.669.004H14.801c-.55 0-1.1 0-1.66-.004a74.993 74.993 0 0 1-1.35-.018c-.744-.02-1.71-.064-2.584-.22a6.938 6.938 0 0 1-1.986-.65 6.337 6.337 0 0 1-1.622-1.18 6.355 6.355 0 0 1-1.178-1.623 6.935 6.935 0 0 1-.646-1.985c-.156-.863-.2-1.788-.22-2.578a66.088 66.088 0 0 1-.02-1.355l-.003-1.327V14.474l.002-1.325a66.7 66.7 0 0 1 .02-1.357c.022-.792.065-1.717.222-2.587a6.924 6.924 0 0 1 .646-1.981c.304-.598.7-1.144 1.18-1.623a6.386 6.386 0 0 1 1.624-1.18 6.96 6.96 0 0 1 1.98-.646c.865-.155 1.792-.198 2.586-.22.452-.012.905-.017 1.354-.02l1.677-.003h135.875" /><g><g><path fill="#000" d="M43.508 35.77c1.404-1.755 2.356-4.112 2.105-6.52-2.054.102-4.56 1.355-6.012 3.112-1.303 1.504-2.456 3.959-2.156 6.266 2.306.2 4.61-1.152 6.063-2.858" /><path fill="#000" d="M45.587 39.079c-3.35-.2-6.196 1.9-7.795 1.9-1.6 0-4.049-1.8-6.698-1.751-3.447.05-6.645 2-8.395 5.1-3.598 6.2-.95 15.4 2.55 20.45 1.699 2.5 3.747 5.25 6.445 5.151 2.55-.1 3.549-1.65 6.647-1.65 3.097 0 3.997 1.65 6.696 1.6 2.798-.05 4.548-2.5 6.247-5 1.95-2.85 2.747-5.6 2.797-5.75-.05-.05-5.396-2.101-5.446-8.251-.05-5.15 4.198-7.6 4.398-7.751-2.399-3.548-6.147-3.948-7.447-4.048" /></g><g><path fill="#000" d="M78.973 32.11c7.278 0 12.347 5.017 12.347 12.321 0 7.33-5.173 12.373-12.529 12.373h-8.058V69.62h-5.822V32.11h14.062zm-8.24 19.807h6.68c5.07 0 7.954-2.729 7.954-7.46 0-4.73-2.885-7.434-7.928-7.434h-6.706v14.894z" /><path fill="#000" d="M92.764 61.847c0-4.809 3.665-7.564 10.423-7.98l7.252-.442v-2.08c0-3.04-2.001-4.704-5.562-4.704-2.938 0-5.07 1.507-5.51 3.82h-5.252c.157-4.86 4.731-8.395 10.918-8.395 6.654 0 10.995 3.483 10.995 8.89v18.663h-5.38v-4.497h-.13c-1.534 2.937-4.914 4.782-8.579 4.782-5.406 0-9.175-3.222-9.175-8.057zm17.675-2.417v-2.106l-6.472.416c-3.64.234-5.536 1.585-5.536 3.95 0 2.288 1.975 3.77 5.068 3.77 3.95 0 6.94-2.522 6.94-6.03z" /><path fill="#000" d="M120.975 79.652v-4.496c.364.051 1.247.103 1.715.103 2.573 0 4.029-1.09 4.913-3.899l.52-1.663-9.852-27.293h6.082l6.863 22.146h.13l6.862-22.146h5.927l-10.216 28.67c-2.34 6.577-5.017 8.735-10.683 8.735-.442 0-1.872-.052-2.261-.157z" /></g></g></svg></li><li><svg class="w-12 h-auto pr-2 mt-2 space-y-2" xmlns="http://www.w3.org/2000/svg" role="img" viewBox="0 0 38 24" width="38" height="24" aria-labelledby="pi-google_pay"><title id="pi-google_pay">Google Pay</title><path d="M35 0H3C1.3 0 0 1.3 0 3v18c0 1.7 1.4 3 3 3h32c1.7 0 3-1.3 3-3V3c0-1.7-1.4-3-3-3z" fill="#000" opacity=".07"/><path d="M35 1c1.1 0 2 .9 2 2v18c0 1.1-.9 2-2 2H3c-1.1 0-2-.9-2-2V3c0-1.1.9-2 2-2h32" fill="#FFF"/><path d="M18.093 11.976v3.2h-1.018v-7.9h2.691a2.447 2.447 0 0 1 1.747.692 2.28 2.28 0 0 1 .11 3.224l-.11.116c-.47.447-1.098.69-1.747.674l-1.673-.006zm0-3.732v2.788h1.698c.377.012.741-.135 1.005-.404a1.391 1.391 0 0 0-1.005-2.354l-1.698-.03zm6.484 1.348c.65-.03 1.286.188 1.778.613.445.43.682 1.03.65 1.649v3.334h-.969v-.766h-.049a1.93 1.93 0 0 1-1.673.931 2.17 2.17 0 0 1-1.496-.533 1.667 1.667 0 0 1-.613-1.324 1.606 1.606 0 0 1 .613-1.336 2.746 2.746 0 0 1 1.698-.515c.517-.02 1.03.093 1.49.331v-.208a1.134 1.134 0 0 0-.417-.901 1.416 1.416 0 0 0-.98-.368 1.545 1.545 0 0 0-1.319.717l-.895-.564a2.488 2.488 0 0 1 2.182-1.06zM23.29 13.52a.79.79 0 0 0 .337.662c.223.176.5.269.785.263.429-.001.84-.17 1.146-.472.305-.286.478-.685.478-1.103a2.047 2.047 0 0 0-1.324-.374 1.716 1.716 0 0 0-1.03.294.883.883 0 0 0-.392.73zm9.286-3.75l-3.39 7.79h-1.048l1.281-2.728-2.224-5.062h1.103l1.612 3.885 1.569-3.885h1.097z" fill="#5F6368"/><path d="M13.986 11.284c0-.308-.024-.616-.073-.92h-4.29v1.747h2.451a2.096 2.096 0 0 1-.9 1.373v1.134h1.464a4.433 4.433 0 0 0 1.348-3.334z" fill="#4285F4"/><path d="M9.629 15.721a4.352 4.352 0 0 0 3.01-1.097l-1.466-1.14a2.752 2.752 0 0 1-4.094-1.44H5.577v1.17a4.53 4.53 0 0 0 4.052 2.507z" fill="#34A853"/><path d="M7.079 12.05a2.709 2.709 0 0 1 0-1.735v-1.17H5.577a4.505 4.505 0 0 0 0 4.075l1.502-1.17z" fill="#FBBC04"/><path d="M9.629 8.44a2.452 2.452 0 0 1 1.74.68l1.3-1.293a4.37 4.37 0 0 0-3.065-1.183 4.53 4.53 0 0 0-4.027 2.5l1.502 1.171a2.715 2.715 0 0 1 2.55-1.875z" fill="#EA4335"/></svg></li><li><svg class="w-12 h-auto pr-2 mt-2 space-y-2" xmlns="http://www.w3.org/2000/svg" role="img" viewBox="0 0 38 24" width="38" height="24" aria-labelledby="pi-shopify_pay"><title id="pi-shopify_pay">Shop Pay</title><path opacity=".07" d="M35 0H3C1.3 0 0 1.3 0 3v18c0 1.7 1.4 3 3 3h32c1.7 0 3-1.3 3-3V3c0-1.7-1.4-3-3-3z" fill="#000"/><path d="M35.889 0C37.05 0 38 .982 38 2.182v19.636c0 1.2-.95 2.182-2.111 2.182H2.11C.95 24 0 23.018 0 21.818V2.182C0 .982.95 0 2.111 0H35.89z" fill="#5A31F4"/><path d="M9.35 11.368c-1.017-.223-1.47-.31-1.47-.705 0-.372.306-.558.92-.558.54 0 .934.238 1.225.704a.079.079 0 00.104.03l1.146-.584a.082.082 0 00.032-.114c-.475-.831-1.353-1.286-2.51-1.286-1.52 0-2.464.755-2.464 1.956 0 1.275 1.15 1.597 2.17 1.82 1.02.222 1.474.31 1.474.705 0 .396-.332.582-.993.582-.612 0-1.065-.282-1.34-.83a.08.08 0 00-.107-.035l-1.143.57a.083.083 0 00-.036.111c.454.92 1.384 1.437 2.627 1.437 1.583 0 2.539-.742 2.539-1.98s-1.155-1.598-2.173-1.82v-.003zM15.49 8.855c-.65 0-1.224.232-1.636.646a.04.04 0 01-.069-.03v-2.64a.08.08 0 00-.08-.081H12.27a.08.08 0 00-.08.082v8.194a.08.08 0 00.08.082h1.433a.08.08 0 00.081-.082v-3.594c0-.695.528-1.227 1.239-1.227.71 0 1.226.521 1.226 1.227v3.594a.08.08 0 00.081.082h1.433a.08.08 0 00.081-.082v-3.594c0-1.51-.981-2.577-2.355-2.577zM20.753 8.62c-.778 0-1.507.24-2.03.588a.082.082 0 00-.027.109l.632 1.088a.08.08 0 00.11.03 2.5 2.5 0 011.318-.366c1.25 0 2.17.891 2.17 2.068 0 1.003-.736 1.745-1.669 1.745-.76 0-1.288-.446-1.288-1.077 0-.361.152-.657.548-.866a.08.08 0 00.032-.113l-.596-1.018a.08.08 0 00-.098-.035c-.799.299-1.359 1.018-1.359 1.984 0 1.46 1.152 2.55 2.76 2.55 1.877 0 3.227-1.313 3.227-3.195 0-2.018-1.57-3.492-3.73-3.492zM28.675 8.843c-.724 0-1.373.27-1.845.746-.026.027-.069.007-.069-.029v-.572a.08.08 0 00-.08-.082h-1.397a.08.08 0 00-.08.082v8.182a.08.08 0 00.08.081h1.433a.08.08 0 00.081-.081v-2.683c0-.036.043-.054.069-.03a2.6 2.6 0 001.808.7c1.682 0 2.993-1.373 2.993-3.157s-1.313-3.157-2.993-3.157zm-.271 4.929c-.956 0-1.681-.768-1.681-1.783s.723-1.783 1.681-1.783c.958 0 1.68.755 1.68 1.783 0 1.027-.713 1.783-1.681 1.783h.001z" fill="#fff"/></svg></li></ul><a class="bgg" href="https://boardgamegeek.com" title="Powered by BoardGameGeek"><img src="img/powered-by-bgg.png" alt="Powered by BGG"></a></div>
</div>
</footer>'''

def script_html():
    return f'''<script>
(function(){{
  var b=document.body, btns=document.querySelectorAll('.wf-toggle button[data-mode]');
  function set(mode, save){{
    b.classList.toggle('clean', mode==='clean');
    btns.forEach(function(x){{x.setAttribute('aria-pressed', String(x.dataset.mode===mode));}});
    if(save){{try{{localStorage.setItem('advent-design-mode', mode);}}catch(e){{}}}}
  }}
  function barH(){{var bar=document.querySelector('.wfbar'); document.documentElement.style.setProperty('--wfbar-h', (bar?bar.offsetHeight:0)+'px');}}
  barH(); window.addEventListener('resize', barH);
  var m=DEFAULT_MODE; try{{m=localStorage.getItem('advent-design-mode')||DEFAULT_MODE;}}catch(e){{}}
  set(m,false);
  btns.forEach(function(x){{x.addEventListener('click',function(){{set(x.dataset.mode,true);}});}});
  var hb=document.querySelectorAll('[data-hero]');
  function setHero(v,save){{document.body.classList.toggle('hero-sale',v==='sale'); hb.forEach(function(b){{b.setAttribute('aria-pressed',String(b.dataset.hero===v));}}); if(save){{try{{localStorage.setItem('advent-hero',v);}}catch(e){{}}}}}}
  var hv='launch'; try{{hv=localStorage.getItem('advent-hero')||'launch';}}catch(e){{}}
  setHero(hv,false);
  hb.forEach(function(b){{b.addEventListener('click',function(){{setHero(b.dataset.hero,true);}});}});
  var nb=document.querySelectorAll('[data-nav]');
  function setNav(v,save){{document.body.classList.toggle('nav-blue',v==='blue'); nb.forEach(function(b){{b.setAttribute('aria-pressed',String(b.dataset.nav===v));}}); if(save){{try{{localStorage.setItem('advent-nav-v2',v);}}catch(e){{}}}}}}
  var nv='blue'; try{{nv=localStorage.getItem('advent-nav-v2')||'blue';}}catch(e){{}}
  setNav(nv,false);
  nb.forEach(function(b){{b.addEventListener('click',function(){{setNav(b.dataset.nav,true);}});}});
  var hdr=document.querySelector('.hdr'), navRow=document.querySelector('.nav-row'), firstSec=document.querySelector('main > section');
  function navH(){{document.documentElement.style.setProperty('--nav-h',(navRow?navRow.offsetHeight:0)+'px'); if(hdr) document.documentElement.style.setProperty('--hdr-h',hdr.offsetHeight+'px');}}
  navH(); window.addEventListener('resize',navH);
  // sticky bars below the header follow the shy menu row: under the menu row when it shows, under the main header when it tucks away
  function stickyTop(){{var bar=document.querySelector('.wfbar'), c=hdr&&hdr.classList.contains('is-compact');
    var v=(hdr?(parseFloat(getComputedStyle(hdr).top)||0)+hdr.offsetHeight:0)+(c||!navRow?0:navRow.offsetHeight);
    document.documentElement.style.setProperty('--sticky-top',v+'px');}}
  stickyTop(); window.addEventListener('resize',stickyTop);
  var lastY=window.scrollY;
  window.addEventListener('scroll',function(){{var y=window.scrollY, past=firstSec?y>firstSec.offsetTop+firstSec.offsetHeight-80:y>400;
    if(!past){{hdr.classList.remove('is-compact');}} else if(y>lastY+4){{hdr.classList.add('is-compact');}} else if(y<lastY-4){{hdr.classList.remove('is-compact');}}
    stickyTop();
    lastY=y;}},{{passive:true}});
  // carousels: arrows scroll one card
  function slider(track, prev, next){{
    function step(){{var k=track.firstElementChild; return k?k.getBoundingClientRect().width+parseFloat(getComputedStyle(track).columnGap||getComputedStyle(track).gap||0):300;}}
    prev.addEventListener('click',function(){{track.scrollBy({{left:-step(),behavior:'smooth'}});}});
    next.addEventListener('click',function(){{track.scrollBy({{left:step(),behavior:'smooth'}});}});
  }}
  var tw=document.querySelector('.trust-wrap-inner'); if(tw) slider(tw.querySelector('.ag-trust'), tw.querySelector('.trust-prev'), tw.querySelector('.trust-next'));
  var rw=document.querySelector('.reviews-wrap'); if(rw){{var rb=rw.querySelectorAll('.rev-nav .car-btn'); slider(rw.querySelector('.reviews'), rb[0], rb[1]);}}
  function foot(){{var open=window.innerWidth>900; document.querySelectorAll('.ftr-col').forEach(function(d){{d.open=open;}});}}
  foot(); window.addEventListener('resize', foot);
  document.querySelectorAll('.carousel').forEach(function(c){{
    var t=c.querySelector('.track'), bs=c.querySelectorAll('.car-btn');
    function step(){{var k=t.firstElementChild; return k?k.getBoundingClientRect().width+24:300;}}
    bs[0].addEventListener('click',function(){{t.scrollBy({{left:-step(),behavior:'smooth'}});}});
    bs[1].addEventListener('click',function(){{t.scrollBy({{left:step(),behavior:'smooth'}});}});
  }});
}})();
</script>'''

def wfbar(current, label, sub, toggles=""):
    opts = "".join(f'<option value="{f}"{" selected" if f == current else ""}>{n}</option>' for f, n in PAGES)
    return f'''<div class="wfbar">
  <div class="wf-left"><strong>Advent Games · {label}</strong><span class="wf-sub">{sub}</span></div>
  <div class="wf-right">
    <div class="legend"><span class="an-tag an-native">Enterprise section</span><span class="an-tag an-tweak">native + tweak</span><span class="an-tag an-custom">custom / app</span></div>
    <label class="wf-pages"><span class="sr">Page</span><select onchange="location.href=this.value">{opts}</select></label>
    <div class="wf-toggle" role="group" aria-label="Nav colour"><span class="wf-lbl">Nav:</span><button type="button" data-nav="white" aria-pressed="false">White</button><button type="button" data-nav="blue" aria-pressed="true">Gradient</button></div>
    {toggles}
    <button type="button" class="wf-cart wf-cart--alt" data-try-search>{I("search",14)} Try search</button>
    <button type="button" class="wf-cart" data-open-cart>{I("cart",14)} Open cart drawer</button>
    <div class="wf-toggle" role="group" aria-label="View mode"><button type="button" data-mode="notes" aria-pressed="true">Annotated</button><button type="button" data-mode="clean" aria-pressed="false">Clean</button></div>
  </div>
</div>'''


# ---------------------------------------------------------------- cart drawer (Enterprise cart drawer + tweaks)
def cart_drawer_html():
    return f"""<div class="cd-scrim js-cd-close" hidden></div>
<aside class="cd" id="cart-drawer" role="dialog" aria-modal="true" aria-labelledby="cd-title" aria-hidden="true">
  <div class="cd-head">{tag("Cart drawer", "tweak", "Enterprise cart drawer · opens on add to cart and on the cart icon · 440px on desktop, full width on mobile")}
    <h2 id="cd-title" class="h4">Your cart <span class="cd-count js-cd-count">(2)</span></h2>
    <div class="cd-head-r"><a href="#" class="cd-viewcart js-cd-viewcart">View cart</a><button class="cd-x js-cd-close" type="button" aria-label="Close cart">{I("x",22)}</button></div>
  </div>
  <div class="cd-body">
    <div class="cd-added js-cd-added" hidden>{I("cart",16)}<span>Added to your cart: <strong class="js-cd-added-name"></strong></span></div>
    <div class="cd-ship">
      <p class="js-cd-ship-msg">You're <strong>$100.10</strong> away from free shipping</p>
      <div class="cd-bar"><span class="js-cd-bar" style="width:67%"></span></div>
      {tag("Free shipping bar", "native", "threshold set to $300 in theme settings")}
    </div>
    <div class="cd-lines js-cd-lines"></div>
    <div class="cd-empty js-cd-empty" hidden><p class="h4">Your cart is empty</p><a class="ag-btn ag-btn--primary" href="collection.html">Shop board games</a></div>
    <div class="cd-tools">
      <details class="cd-tool"><summary>{I("chat",16)} Add order note</summary><textarea rows="3" placeholder="Anything we should know? Gift message, pickup timing..."></textarea></details>
      <details class="cd-tool"><summary>{I("truck",16)} Estimate shipping</summary>
        <div class="cd-est"><input inputmode="numeric" maxlength="4" placeholder="Postcode" class="js-cd-pc" value="2750"><button type="button" class="ag-btn ag-btn--secondary ag-btn--sm js-cd-calc">Calculate</button></div>
        <ul class="cd-rates js-cd-rates" hidden></ul>
      </details>
    </div>
    <div class="cd-ymal">{tag("You may also like", "native", "Shopify complementary products (Search &amp; Discovery) · slider")}
      <div class="cd-ymal-h"><strong>You may also like</strong><span class="cd-ymal-nav"><button type="button" class="js-ymal-prev" aria-label="Previous">{I("left",16)}</button><button type="button" class="js-ymal-next" aria-label="Next">{I("right",16)}</button></span></div>
      <div class="cd-ymal-track js-ymal-track">
        <div class="cd-ymal-item" data-img="okc-sleeves" data-title="The Old King's Crown: Card Sleeve Pack" data-vendor="Eerie Idol Games" data-price="19.95" data-state="in"><img src="img/okc-sleeves.jpg" alt=""><div><span class="cd-v">Eerie Idol Games</span><strong>The Old King's Crown: Card Sleeve Pack</strong><span class="cd-p">$19.95</span><button type="button" class="ag-btn ag-btn--secondary ag-btn--sm js-cd-add">Add</button></div></div>
        <div class="cd-ymal-item" data-img="okc-player-marker" data-title="The Old King's Crown: Active Player Marker" data-vendor="Eerie Idol Games" data-price="14.95" data-state="in"><img src="img/okc-player-marker.jpg" alt=""><div><span class="cd-v">Eerie Idol Games</span><strong>The Old King's Crown: Active Player Marker</strong><span class="cd-p">$14.95</span><button type="button" class="ag-btn ag-btn--secondary ag-btn--sm js-cd-add">Add</button></div></div>
        <div class="cd-ymal-item" data-img="okc-art-prints" data-title="The Old King's Crown: Art Print Set" data-vendor="Eerie Idol Games" data-price="29.95" data-state="in"><img src="img/okc-art-prints.jpg" alt=""><div><span class="cd-v">Eerie Idol Games</span><strong>The Old King's Crown: Art Print Set</strong><span class="cd-p">$29.95</span><button type="button" class="ag-btn ag-btn--secondary ag-btn--sm js-cd-add">Add</button></div></div>
      </div>
    </div>
    <a class="cd-promo" href="collection-preorders.html">{tag("Promo banner", "native", "cart drawer image block · Dean swaps it in the theme editor")}<div><span class="eyebrow">Coming soon</span><strong class="h4">New to preorder</strong><span class="cd-promo-link">Reserve yours {I("right",14)}</span></div><img src="img/euphoria-cutout.png" alt=""></a>
  </div>
  <div class="cd-foot">
    <div class="cd-sub"><span>Subtotal</span><strong class="js-cd-sub">$199.90 AUD</strong></div>
    <p class="cd-tax">Tax included. Shipping and pickup chosen at checkout.</p>
    <a href="#" class="ag-btn ag-btn--orange ag-btn--block cd-checkout js-cd-checkout">{I("lock",18)}<span>Checkout · <span class="js-cd-total">$199.90</span></span></a>
    {tag("Checkout button", "tweak", "goes straight to /checkout; theme default is View cart · View cart link kept top right")}
    <div class="cd-toast js-cd-toast" hidden>{I("lock",16)} Next step: Shopify's secure checkout (hosted and styled by Shopify, outside the theme).</div>
  </div>
</aside>"""

CART_JS = r"""
(function(){
  var d=document.getElementById('cart-drawer'); if(!d) return;
  var scrim=document.querySelector('.cd-scrim'), linesEl=d.querySelector('.js-cd-lines');
  var FREE=300;
  var AV={in:['in','In stock'],sup:['supplier','Available from supplier','Ships in 2-7 business days'],pre:['preorder','Preorder','Ships on release'],soon:['coming','Coming soon','Ships on release'],out:['out','Out of stock']};
  var cart=[{img:'old-kings-crown',title:"The Old King's Crown",vendor:'Eerie Idol Games',price:134.95,state:'in',qty:1},
            {img:'okc-wild-kingdom',title:"The Old King's Crown: Wild Kingdom",vendor:'Eerie Idol Games',price:64.95,state:'pre',qty:1}];
  function money(n){return '$'+n.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g,',');}
  function esc(s){var e=document.createElement('span');e.textContent=s;return e.innerHTML;}
  function render(){
    var sub=0,count=0;
    linesEl.innerHTML=cart.map(function(it,i){sub+=it.price*it.qty;count+=it.qty;var a=AV[it.state]||AV.in;
      return '<div class="cd-line"><a class="cd-img" href="#"><img src="img/'+it.img+'.jpg" alt=""></a><div class="cd-info"><span class="cd-v">'+esc(it.vendor)+'</span><a href="#" class="cd-t">'+esc(it.title)+'</a>'
        +'<div class="cd-av"><span class="ag-avail ag-avail--'+a[0]+'">'+a[1]+'</span>'+(a[2]?'<span class="ag-avail__sub">'+a[2]+'</span>':'')+'</div>'
        +'<div class="cd-row"><div class="cd-qty"><button type="button" data-i="'+i+'" data-d="-1" aria-label="Decrease quantity">&minus;</button><span>'+it.qty+'</span><button type="button" data-i="'+i+'" data-d="1" aria-label="Increase quantity">+</button></div><button type="button" class="cd-rm" data-rm="'+i+'">Remove</button></div></div>'
        +'<strong class="cd-lp">'+money(it.price*it.qty)+'</strong></div>';}).join('');
    d.querySelector('.js-cd-empty').hidden=cart.length>0;
    d.querySelector('.cd-foot').hidden=cart.length===0;
    d.querySelector('.cd-ship').hidden=cart.length===0;
    d.querySelector('.js-cd-count').textContent='('+count+')';
    document.querySelectorAll('.hdr-icons .count').forEach(function(c){c.textContent=count;c.hidden=count===0;});
    d.querySelector('.js-cd-sub').textContent=money(sub)+' AUD';
    d.querySelector('.js-cd-total').textContent=money(sub);
    var left=FREE-sub;
    d.querySelector('.js-cd-ship-msg').innerHTML=left>0?"You're <strong>"+money(left)+"</strong> away from free shipping":"<strong>You've unlocked free shipping!</strong>";
    d.querySelector('.js-cd-bar').style.width=Math.min(100,sub/FREE*100)+'%';
    d.classList.toggle('is-free',left<=0);
  }
  var lastFocus=null;
  function open(name){
    lastFocus=document.activeElement;
    var ad=d.querySelector('.js-cd-added'); ad.hidden=!name; if(name) d.querySelector('.js-cd-added-name').textContent=name;
    scrim.hidden=false; requestAnimationFrame(function(){document.body.classList.add('cd-open');}); d.setAttribute('aria-hidden','false');
    setTimeout(function(){d.querySelector('.cd-x').focus();},250);
  }
  function close(){document.body.classList.remove('cd-open'); d.setAttribute('aria-hidden','true'); setTimeout(function(){scrim.hidden=true;},250); d.querySelector('.js-cd-toast').hidden=true; if(lastFocus) lastFocus.focus();}
  function add(it){
    var ex=cart.filter(function(c){return c.title===it.title;})[0];
    if(ex) ex.qty+=it.qty||1; else cart.push({img:it.img,title:it.title,vendor:it.vendor,price:it.price,state:it.state,qty:it.qty||1});
    render(); open(it.title);
  }
  // add-to-cart from product cards
  document.addEventListener('click',function(e){
    var b=e.target.closest('button,a'); if(!b) return;
    if(b.closest('.cd')){return;}
    var txt=(b.textContent||'').trim();
    var card=b.closest('.ag-card');
    if(card && /^(Add to cart|Preorder now)$/.test(txt)){
      e.preventDefault();
      var img=(card.querySelector('.ag-card__media img')||{}).getAttribute? card.querySelector('.ag-card__media img').getAttribute('src').replace(/^img\/|\.jpg$/g,''):'';
      var av=card.querySelector('.ag-avail'), st='in';
      if(av){var m=av.className.match(/ag-avail--(\w+)/); st={in:'in',supplier:'sup',preorder:'pre',coming:'soon',out:'out'}[m&&m[1]]||'in';}
      add({img:img,title:card.querySelector('.ag-card__title').textContent.trim(),vendor:(card.querySelector('.ag-card__vendor')||{}).textContent||'',price:parseFloat(card.querySelector('.ag-price').textContent.replace(/[^\d.]/g,'')),state:st});
      return;
    }
    if(b.classList.contains('js-buybtn')){
      e.preventDefault();
      var h1=document.querySelector('.pdp h1'), pr=document.querySelector('.pricebox .now'), vd=document.querySelector('.buy-vendor'), gi=document.querySelector('.pdp img');
      var q=document.querySelector('.js-buyrow input'); var qty=q?Math.max(1,parseInt(q.value,10)||1):1;
      var ac=document.querySelector('.availcard.on'); var st=ac?ac.dataset.state:'in';
      add({img:gi?gi.getAttribute('src').replace(/^img\/|\.jpg$/g,''):'',title:h1.textContent.trim(),vendor:vd?vd.textContent.trim():'',price:parseFloat(pr.textContent.replace(/[^\d.]/g,'')),state:/pre/.test(txt.toLowerCase())?'pre':st,qty:qty});
      return;
    }
    if(b.matches('.hdr-icons .cart')){e.preventDefault(); open(); return;}
  });
  d.addEventListener('click',function(e){
    var t=e.target.closest('button,a'); if(!t) return;
    if(t.dataset.d){var it=cart[+t.dataset.i]; it.qty=Math.max(0,it.qty+ +t.dataset.d); if(!it.qty) cart.splice(+t.dataset.i,1); render(); return;}
    if(t.dataset.rm){cart.splice(+t.dataset.rm,1); render(); return;}
    if(t.classList.contains('js-cd-add')){var x=t.closest('.cd-ymal-item').dataset; add({img:x.img,title:x.title,vendor:x.vendor,price:parseFloat(x.price),state:x.state}); return;}
    if(t.classList.contains('js-cd-checkout')){e.preventDefault(); d.querySelector('.js-cd-toast').hidden=false; return;}
    if(t.classList.contains('js-cd-viewcart')){e.preventDefault(); return;}
    if(t.classList.contains('js-cd-calc')){var pc=parseInt(d.querySelector('.js-cd-pc').value,10)||0, r=d.querySelector('.js-cd-rates');
      var metro=(pc>=2000&&pc<=2234)||(pc>=2250&&pc<=2263)||(pc>=2500&&pc<=2530)||(pc>=2555&&pc<=2574)||(pc>=2745&&pc<=2786);
      r.innerHTML=(pc<200?'<li>Enter a 4-digit postcode</li>':'<li><span>'+(metro?'Sydney Metro, Gosford &amp; Wollongong':'Flat rate, Australia-wide')+'</span><strong>'+(metro?'$10.00':'$15.00')+'</strong></li><li><span>Free shipping on orders over $300</span><strong>$0.00</strong></li><li><span>Local pickup</span><strong>Free</strong></li>');
      r.hidden=false; return;}
  });
  document.querySelectorAll('.js-cd-close').forEach(function(x){x.addEventListener('click',close);});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&document.body.classList.contains('cd-open')) close();});
  var tr=d.querySelector('.js-ymal-track');
  d.querySelector('.js-ymal-prev').addEventListener('click',function(){tr.scrollBy({left:-tr.clientWidth*0.85,behavior:'smooth'});});
  d.querySelector('.js-ymal-next').addEventListener('click',function(){tr.scrollBy({left:tr.clientWidth*0.85,behavior:'smooth'});});
  render();
  if(/[?&]cart=open/.test(location.search)) open();
  document.querySelectorAll('[data-open-cart]').forEach(function(b){b.addEventListener('click',function(){open();});});
})();
"""

CSS_PATH = os.path.join(ROOT, "design.css")
BUGHERD = '<script type="text/javascript" src="https://www.bugherd.com/sidebarv2.js?apikey=urqa1bezzmybdhdmbsptcg" async="true"></script>\n'

def render(filename, title, label, sub, main, toggles="", extra_js=""):
    """Write one design page. index.html is a fragment for the artifact; other pages are full documents.
    With DEPLOY=<dir> every page is a full document with BugHerd, written to that folder."""
    css = open(CSS_PATH, encoding="utf-8").read()
    deploy = os.environ.get("DEPLOY")
    head = (f'<meta charset="utf-8"><title>{title}</title>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&family=Nunito:wght@700;800&display=swap">\n'
            f'<style>\n{css}\n</style>\n')
    body = (wfbar(filename, label, sub, toggles) + "\n" + header_html() + "\n<main>\n" + main + "\n</main>\n" + footer_html() + "\n" + cart_drawer_html() + "\n" + _menus().menus_html()
            + script_html().replace("DEFAULT_MODE", "'clean'" if deploy else "'notes'") + (f"\n<script>\n{extra_js}\n</script>" if extra_js else "") + f"\n<script>{CART_JS}</script>\n<script>{_menus().MENU_JS}</script>")
    full = filename != "index.html" or deploy
    if full:
        doc = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
               + ('<meta name="robots" content="noindex, nofollow">\n' + BUGHERD if deploy else "") + head + "</head>\n<body>\n" + body + "\n</body>\n</html>\n")
    else:
        doc = head.replace('<link rel="preconnect"', '<meta name="claude:viewport-fit-sides" content="cover">\n<link rel="preconnect"', 1) + "\n" + body
    out = deploy or ROOT
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, filename), "w", encoding="utf-8") as f:
        f.write(doc)
    print("wrote", filename, len(doc))
