# Generates the Advent Games Enterprise wireframe set.
import os
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "site")

# ---------------------------------------------------------------- helpers
def mf(k, kind=""):
    cls = "mf" + (" " + kind if kind else "")
    return f'<span class="{cls}">{k}</span>'

def tag(name, kind=""):
    cls = "vol" + (" " + kind if kind else "")
    return f'<span class="{cls}">{name}</span>'

def sec(tagname, body, note="", kind="", extra_tags="", style="", sid="", internal=False):
    n = f' <span class="lbl">{note}</span>' if note else ""
    i = f' id="{sid}"' if sid else ""
    return f'''
  <div class="sec{' internal' if internal else ''}"{i}{(' style="'+style+'"') if style else ''}>
    <div class="sec-head">{tag(tagname, kind)}{extra_tags}{n}</div>
    {body}
  </div>'''

NAV = [
    ("Preorders", "meganav.html#preorders", "preorders"),
    ("Just Arrived", "meganav.html#arrived", "arrived"),
    ("Board Games", "meganav.html#board", "board"),
    ("Roleplaying", "meganav.html#rpg", "rpg"),
    ("Accessories", "meganav.html#acc", "acc"),
    ("Sale", "meganav.html#sale", "sale"),
    ("Brands", "brands.html", "brands"),
]

PAGES = [  # for the wireframe index strip
    ("Home", "index.html"), ("Navigation + drawers", "meganav.html"), ("Board Games", "collection.html"), ("Preorders", "collection-preorders.html"),
    ("RPG", "collection-rpg.html"), ("Accessories", "collection-accessories.html"), ("Brands", "brands.html"),
    ("Brand", "brand.html"), ("Search", "search.html"), ("Product", "product.html"),
    ("Product: expansion example", "product-preorder.html"), ("Product: RPG example", "product-rpg.html"), ("Product: accessory example", "product-accessory.html"),
    ("Cart", "cart.html"), ("Account", "account.html"), ("Wishlist", "wishlist.html"),
    ("About + Contact", "about.html"), ("Help", "help.html"), ("Blog", "blog.html"), ("Blog post", "article.html"),
    ("DATA MAP", "data-map.html"),
]

CURRENT_FILE = [""]
STATES = [None]
def head(title, template, current=""):
    nav = "".join(
        f'<a href="{h}"{" style=\"font-weight:700;text-decoration:underline;\"" if k == current else ""}>{l}{" ▾" if k not in ("brands","sale") else ""}</a>'
        for l, h, k in NAV)
    cur = CURRENT_FILE[0]
    opts = "".join(f'<option value="{h}"{" selected" if h == cur else ""}>{l}</option>' for l, h in PAGES)
    mfk = mf("namespace.key"); mfn = mf("proposed field", "new")
    stsw = ""
    if STATES[0]:
        d, opts_ = STATES[0]
        stsw = '<div class="wf-toggle wf-state" role="group" aria-label="Availability state" data-default="' + d + '"><span style="padding:4px 8px;color:#aaa;font-size:11px;">Availability:</span>' + "".join(f'<button type="button" data-st="{k}" aria-pressed="{str(k==d).lower()}">{l}</button>' for k, l in opts_) + '</div>'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="robots" content="noindex, nofollow">
<script type="text/javascript" src="https://www.bugherd.com/sidebarv2.js?apikey=urqa1bezzmybdhdmbsptcg" async="true"></script>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} wireframe</title>
<link rel="stylesheet" href="wireframe.css">
<link rel="stylesheet" href="advent.css">
</head>
<body>
<script>try{{if(location.hash==="#clean"||localStorage.getItem("advent-wf-mode")==="clean")document.body.classList.add("clean");}}catch(e){{}}</script>
<div class="page">
  <div class="wfbar">
    <div class="wf-left"><strong>Advent Games × Enterprise</strong>
      <select class="wf-pages" aria-label="Wireframe page" onchange="location.href=this.value">{opts}</select></div>
    <div class="wf-right">
      <div class="legend"><span class="vol">Enterprise section</span><span class="vol tweak">native + tweak</span><span class="vol custom">custom / app</span>{mfk}{mfn}</div>
      {stsw}
      <div class="wf-toggle" role="group" aria-label="View mode"><button type="button" data-mode="notes" aria-pressed="true">Annotated</button><button type="button" data-mode="clean" aria-pressed="false">Clean</button></div>
    </div>
  </div>

  <!-- ============ HEADER GROUP (same on every page) ============ -->
  <div class="sec tg" style="padding:0;">
    <div style="padding:10px 40px 0;"><div class="sec-head" style="margin-bottom:6px;">{tag("Announcement bar")} <span class="lbl">site message left · utility links right</span></div></div>
    <div class="row small" style="justify-content:space-between;background:#f2f2f2;padding:7px 40px;font-size:12px;">
      <span>Flat rate shipping $10 Sydney Metro, Gosford &amp; Wollongong · $15 rest of Australia · Free over $300</span>
      <span class="row" style="gap:16px;"><a href="help.html">Help &amp; FAQ</a><a href="account.html">Track my order</a><a href="brands.html">Brands A-Z</a></span>
    </div>
    <div style="padding:14px 40px 0;"><div class="sec-head" style="margin-bottom:8px;">{tag("Header")} <span class="lbl">sticky · search with category dropdown · mega menu</span></div></div>
    <div class="row hd-main" style="align-items:center;justify-content:space-between;padding:4px 40px 12px;gap:24px;">
      <a href="meganav.html#mobile-menu" class="burger" aria-label="Menu">☰</a><a href="index.html" class="hd-logo"><div class="img" style="width:150px;height:44px;">Logo</div></a>
      <a href="search.html" class="hd-search" style="flex:1;display:flex;"><div class="field" style="width:120px;border-right:none;border-radius:4px 0 0 4px;">All ▾</div><div class="field" style="flex:1;border-radius:0 4px 4px 0;">Search 11,000+ games, publishers, designers...</div></a>
      <div class="row small hd-icons" style="gap:16px;align-items:center;"><a href="account.html">Account</a><a href="wishlist.html">♡ Wishlist</a><a href="cart.html"><strong>Cart (2)</strong></a></div>
    </div>
    <div class="row small nav" style="gap:22px;padding:10px 40px;border-top:1px solid var(--line);justify-content:space-between;">
      <div class="row" style="gap:22px;flex-wrap:wrap;">{nav}</div>
      <div class="row" style="gap:16px;color:#777;"><a href="help.html">Shipping &amp; pickup</a><a href="about.html">About</a></div>
    </div>
    <div style="padding:10px 40px 0;border-top:1px solid var(--line);"><div class="sec-head" style="margin-bottom:6px;">{tag("Icons with text")} <span class="lbl">header group trust strip · editable</span></div></div>
    <div class="grid g4 small center" style="padding:6px 40px 14px;color:#555;">
      <span>▢ Free shipping over $300</span><span>▢ Australia-wide via AusPost</span><span>▢ Friendly, local service</span><span>▢ Secure checkout + PayPal</span>
    </div>
  </div>
'''

TOGGLE_JS = "<script>\ndocument.addEventListener('click',function(e){var t=e.target.closest('.wf-tabs [data-tab]');if(!t)return;var sec=t.closest('.sec');sec.querySelectorAll('.wf-tabs [data-tab]').forEach(function(x){x.classList.toggle('on',x===t);});sec.querySelectorAll('.tabpanel').forEach(function(p){p.hidden=p.dataset.panel!==t.dataset.tab;});});\n(function(){\n  var g=document.querySelector('.wf-state'); if(!g) return;\n  var b=document.body, btns=g.querySelectorAll('button[data-st]');\n  function set(k){ b.setAttribute('data-st',k); btns.forEach(function(x){x.setAttribute('aria-pressed',String(x.dataset.st===k));}); }\n  set(g.dataset.default);\n  btns.forEach(function(x){x.addEventListener('click',function(){set(x.dataset.st);});});\n})();\n</script>\n" + "<script>\n(function(){\n  var b=document.body, btns=document.querySelectorAll('.wf-toggle button[data-mode]');\n  function set(mode, save){\n    b.classList.toggle('clean', mode==='clean');\n    btns.forEach(function(x){x.setAttribute('aria-pressed', String(x.dataset.mode===mode));});\n    if(save){try{localStorage.setItem('advent-wf-mode', mode);}catch(e){}}\n  }\n  set(b.classList.contains('clean')?'clean':'notes', false);\n  btns.forEach(function(x){x.addEventListener('click',function(){set(x.dataset.mode,true);});});\n})();\n</script>\n"

FOOTER = f'''
  <!-- ============ FOOTER GROUP (same on every page) ============ -->
  <div class="sec tg" style="background:#2b2b2b;color:#ddd;border:none;">
    <div class="sec-head" style="margin-bottom:14px;">{tag("Newsletter")} <span class="lbl" style="color:#aaa;">Mailchimp list</span></div>
    <div class="row" style="justify-content:space-between;align-items:center;">
      <div><h3 style="color:#fff;">New releases and preorders, first.</h3><p class="small" style="color:#aaa;margin-top:4px;">New arrivals, preorders and offers straight to your inbox.</p></div>
      <div class="row" style="gap:8px;"><div class="field" style="width:260px;background:#3a3a3a;border-color:#555;">Email address</div><span class="btn solid" style="background:#555;border-color:#555;">Sign up</span></div>
    </div>
  </div>
  <div class="sec tg" style="background:#2b2b2b;color:#ddd;border:none;padding-top:10px;">
    <div class="sec-head" style="margin-bottom:14px;">{tag("Footer")}</div>
    <div class="row" style="justify-content:space-between;">
      <div style="flex:1.4;"><div class="img" style="width:150px;height:40px;background:#3a3a3a;border-color:#555;color:#888;">Logo</div><p class="small" style="margin-top:12px;color:#aaa;max-width:280px;">Your friendly, local, online board game store. Sydney based, shipping Australia-wide.</p>
        <div class="row" style="gap:8px;margin-top:12px;"><div class="img" style="width:28px;height:28px;background:#3a3a3a;border-color:#555;"> </div><div class="img" style="width:28px;height:28px;background:#3a3a3a;border-color:#555;"> </div><div class="img" style="width:28px;height:28px;background:#3a3a3a;border-color:#555;"> </div></div></div>
      <div style="flex:1;"><p class="small" style="color:#888;letter-spacing:.1em;">SHOP</p><p class="small" style="line-height:2;color:#ccc;"><a href="collection-preorders.html">Preorders</a><br><a href="collection-preorders.html#just-arrived">Just Arrived</a><br><a href="collection.html">Board Games</a><br><a href="collection-rpg.html">Roleplaying</a><br><a href="collection-accessories.html">Accessories</a><br><a href="brands.html">Brands A-Z</a></p></div>
      <div style="flex:1;"><p class="small" style="color:#888;letter-spacing:.1em;">HELP</p><p class="small" style="line-height:2;color:#ccc;"><a href="help.html">Shipping &amp; pickup</a><br><a href="help.html">Preorder policy</a><br><a href="help.html">Returns</a><br><a href="help.html">FAQ</a><br><a href="account.html">Track my order</a></p></div>
      <div style="flex:1;"><p class="small" style="color:#888;letter-spacing:.1em;">ADVENT GAMES</p><p class="small" style="line-height:2;color:#ccc;"><a href="about.html">About us</a><br><a href="about.html#contact">Contact</a><br><a href="blog.html">News &amp; reviews</a><br><a href="wishlist.html">Wishlist</a></p></div>
    </div>
    <div class="row" style="justify-content:space-between;margin-top:20px;align-items:center;"><p class="small" style="color:#777;font-size:11px;">© 2026 Advent Games · Privacy Policy · Terms &amp; Conditions · Shipping &amp; Returns</p>
      <div class="row" style="gap:6px;"><span class="pill">Visa</span><span class="pill">MC</span><span class="pill">PayPal</span><span class="pill">Bank transfer</span>
        <span class="bgg-badge" title="Required by BoardGameGeek's API terms">Powered by BGG</span></div></div>
  </div>
</div>
</body>
</html>
'''

def write(fn, title, template, current, body, states=None, hosted=False):
    if hosted: body = '<style>.sec.tg{display:none;}</style><div class="sec" style="padding:12px 40px;background:#fbf6f0;"><p class="small"><strong>Shopify-hosted page.</strong> The store header and footer don\'t appear here: customers land on Shopify\'s customer accounts (on the shop\'s account subdomain) with the store logo, colours and fonts, and a link back to the shop.</p></div>' + body
    CURRENT_FILE[0] = fn
    STATES[0] = states
    with open(os.path.join(OUT, fn), "w") as f:
        f.write(head(title, template, current) + body + FOOTER.replace("</body>", TOGGLE_JS + "</body>"))

# product card ---------------------------------------------------------


# Phosphor Icons (MIT), Regular weight, inlined as SVG
import os as _os, re as _re
_ICD = _os.path.join(ROOT, "icons")
ICONS = {f[:-4]: open(_os.path.join(_ICD, f)).read() for f in _os.listdir(_ICD) if f.endswith(".svg")}
def ico(name, size=15):
    svg = ICONS[name]
    return svg.replace('<svg ', f'<svg width="{size}" height="{size}" aria-hidden="true" style="vertical-align:-0.18em;flex-shrink:0;" ', 1)

STAT_ICON = {"Players": "users-three", "Play time": "clock", "Age": "person", "Complexity": "brain", "Weight": "brain", "System": "book-open", "Kind": "books", "Category": "books",
             "Publisher": "buildings", "Sleeve size": "ruler", "Pack": "stack", "Finish": "sparkle"}

def meta_icons(meta):
    parts = [x.strip() for x in meta.split("·")]
    out = []; hit = False
    for x in parts:
        if x.startswith("Complexity:"):
            out.append(ico("brain", 13) + " " + x.replace("Complexity:", "").strip() + '<span class="muted">/5</span>'); hit = True
        elif _re.match(r"^\d+(-\d+)?$", x):
            out.append(ico("users-three", 13) + " " + x); hit = True
        elif "min" in x or "hr" in x:
            out.append(ico("clock", 13) + " " + x.replace(" min", "m").replace(" hrs+", "h+").replace("Under 30m", "&lt;30m")); hit = True
        elif _re.match(r"^\d+\+$", x):
            out.append(ico("person", 13) + " " + x); hit = True
        else:
            out.append(x)
    if not hit: return meta
    return '<span class="mi">' + "".join(f"<span>{o}</span>" for o in out) + "</span>"

# Illustrative BGG data for card badges (placeholder figures, not live BGG values)
BGG = {
 "Wingspan": (2019, 8.0, 32, 0), "Sky Team": (2023, 7.9, 60, 0), "Ark Nova": (2021, 8.5, 2, 0),
 "Nusfjord": (2017, 7.6, 387, 0), "Cascadia": (2021, 7.9, 55, 0), "Three Days of Gettysburg: Deluxe": (2024, 8.2, 0, 0),
 "Spirit Island: Nature Incarnate": (2023, 9.0, 0, 1), "Nusfjord: Expansion Pack #1": (2019, 7.8, 0, 1),
 "Heat: Pedal to the Metal": (2022, 8.0, 30, 0), "Baltic Empires": (2021, 8.1, 0, 0), "Wyrmspan": (2024, 7.9, 140, 0),
 "Viticulture Essential": (2015, 8.0, 25, 0), "Thunderbolt: Deluxe Edition": (2025, 8.0, 0, 0), "The Crew: Mission Deep Sea": (2021, 8.1, 70, 0),
 "The Crew": (2019, 7.8, 110, 0), "Scythe": (2016, 8.1, 20, 0), "Nusfjord: Big Box": (2026, 0, 0, 1), "Jaipur": (2009, 7.4, 290, 0),
 "Heat: Tunnel Vision": (2027, 0, 0, 1), "Hallertau": (2020, 7.7, 400, 0), "Fields of Arle": (2014, 8.0, 160, 0),
 "Expeditions": (2023, 8.0, 230, 0), "Exp. #6: Generals": (2019, 8.3, 0, 1), "Exp. #5: Generals, Marshals, Tacticians": (2015, 8.2, 0, 1),
 "Earthborne Rangers: Legends": (2027, 0, 0, 1), "Dune: Imperium: Bloodlines": (2026, 0, 0, 1), "Container: More Containers": (2019, 7.6, 0, 1),
 "Commands &amp; Colors: Napoleonics Exp. #7": (2026, 0, 0, 1), "Commands & Colors: Napoleonics Exp. #7": (2026, 0, 0, 1),
 "Caverna": (2013, 8.0, 50, 0), "Cascadia: Landmarks": (2024, 8.2, 0, 1), "C&amp;C Napoleonics": (2010, 8.0, 260, 0),
 "C&amp;C Medieval": (2019, 7.9, 0, 0), "C&amp;C Ancients": (2006, 7.7, 600, 0), "Arcs: Leaders & Lore Pack": (2026, 0, 0, 1),
 "Agricola": (2007, 7.9, 45, 0), "A Feast for Odin": (2016, 8.1, 38, 0),
}

def bgg_line(title, rating_on=True):
    d = BGG.get(title)
    if not d: return ""
    year, rating, rank, exp = d
    parts = [f'<span>{year}</span>']
    if rating and rating_on: parts.append(f'<span class="rb">{ico("star", 11)} {rating} BGG</span>')
    if exp: parts.append(f'<span class="xb">{ico("puzzle-piece", 11)} Expansion</span>')
    return '<div class="bggl">' + "".join(parts) + '</div>'

def card(title, vendor, price, state="in", badge="", was="", meta="1-4 · 60-120 min · 14+ · Complexity: 2.9", eta="", qa=True, link="product.html"):
    states = {
        "in": ('<i></i>In stock', "Add to cart"),
        "pre": (f'<i class="hollow"></i>Preorder · due {eta or "Nov 2026"}', "Preorder"),
        "soon": (f'<i class="hollow"></i>Coming soon · {eta or "early 2027"}', "Notify me"),
        "sup": ('<i class="half"></i>At supplier · ships 2-7 days', "Add to cart"),
        "out": ('<i class="hollow"></i>Out of stock', "Notify me"),
    }
    av, btn = states[state]
    b = f'<span class="badge{" out" if badge in ("Out of stock",) else ""}">{badge}</span>' if badge else ""
    w = f'<s>${was}</s>' if was else ""
    q = f'<div class="qa">{btn}</div>' if qa else ""
    m = f'<div class="meta">{meta_icons(meta)}</div>' if meta else ""
    return f'''<a class="pc" href="{link}"><div class="img">Box art</div>{b}<span class="heart">♡</span>
      <div class="vendor">{vendor}</div><div class="title">{title}</div>{bgg_line(title)}<div class="price">${price}{w}</div>
      {m}<div class="avail inv">{av}</div>{q}</a>'''

def carousel(cards, cols=4):
    return (f'<div class="carousel" style="--cols:{cols};">{"".join(cards)}</div>'
            '<div class="row small" style="justify-content:flex-end;gap:10px;margin-top:8px;"><span class="car-arrow">‹</span><span class="car-arrow">›</span></div>')

ROW_JUST = [card("Nusfjord: Expansion Pack #1", "Lookout Spiele", "44.95", meta="1-5 · 20-100 min · 12+ · Complexity: 2.9", badge="Just arrived"),
            card("Three Days of Gettysburg: Deluxe", "GMT", "169.95", meta="1-2 · 2 hrs+ · 14+ · Complexity: 3.7"),
            card("Thunderbolt: Deluxe Edition", "GMT", "169.95", meta="1-2 · 2 hrs+ · 14+ · Complexity: 3.7"),
            card("Container: More Containers", "Pegasus Spiele", "39.95", meta="3-5 · 60-120 min · 12+ · Complexity: 2.9"),
            card("Cascadia: Landmarks", "Flatout Games", "49.95", meta="1-5 · 30-60 min · 10+ · Complexity: 2.1", badge="Back in stock")]
ROW_PRE = [card("Commands & Colors: Napoleonics Exp. #7", "GMT", "144.95", "pre", "Preorder", eta="Nov 2026", meta="2 · 60-120 min · 12+ · Complexity: 2.9", link="product-preorder.html"),
           card("Baltic Empires", "Compass Games", "129.95", "pre", "Preorder", eta="Dec 2026", meta="1-4 · 2 hrs+ · 14+ · Complexity: 3.7", link="product-preorder.html"),
           card("Arcs: Leaders & Lore Pack", "Leder Games", "54.95", "pre", "Preorder", eta="Jan 2027", meta="2-4 · 60-120 min · 14+ · Complexity: 2.9", link="product-preorder.html"),
           card("Spirit Island: Nature Incarnate", "Greater Than Games", "89.95", "pre", "Preorder", eta="Feb 2027", meta="1-4 · 60-120 min · 13+ · Complexity: 3.7", link="product-preorder.html"),
           card("Heat: Tunnel Vision", "Days of Wonder", "64.95", "soon", "Coming soon", eta="Mar 2027", meta="1-6 · 30-60 min · 10+ · Complexity: 2.1", link="product-preorder.html")]

# ---- Enterprise collection UI (matched to the live Enterprise demo) ----
ENT_FILTER_ICO = '<svg width="18" height="18" viewBox="0 0 20 20" fill="none" stroke-width="1.25" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" d="M1 6h18M1 14h18"/><circle cx="7" cy="6" r="3" fill="#fff"/><circle cx="13" cy="14" r="3" fill="#fff"/></svg>'
ENT_LIST_ICO = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" aria-hidden="true"><g stroke="currentColor" stroke-width="1.5"><path d="M7.4 6.8h13.1M7.4 12h13.1M7.4 17.2h13.1"/></g><g fill="currentColor"><circle cx="4.1" cy="6.8" r="1.1"/><circle cx="4.1" cy="12" r="1.1"/><circle cx="4.1" cy="17.2" r="1.1"/></g></svg>'
ENT_GRID_ICO = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="4" y="4" width="6.5" height="6.5"/><rect x="13.5" y="4" width="6.5" height="6.5"/><rect x="4" y="13.5" width="6.5" height="6.5"/><rect x="13.5" y="13.5" width="6.5" height="6.5"/></svg>'
ENT_CHEV = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M5 15.5 12.5 8 20 15.5"/></svg>'
ENT_X = '<span class="ent-x">✕</span>'

def ent_banner(crumbs, title, count, desc, note="Enterprise collection banner: title, product count, description. No image."):
    return sec("Collection banner", f'''<p class="small muted">{crumbs}</p>
    <div class="center" style="max-width:720px;margin:18px auto 0;"><h1>{title}</h1><p class="small" style="color:#888;font-weight:600;margin-top:2px;">({count} products)</p><p style="margin-top:12px;">{desc}</p></div>''', note=note)

def ent_toolbar(sort="BGG rank"):
    return f'''<div class="ent-tb">
      <div class="ent-tb-l"><span class="ent-fbtn"><span class="d">Filter</span><span class="m">Filter &amp; Sort</span>{ENT_FILTER_ICO}</span>
        <span class="ent-sort"><span class="small">Sort by</span><span class="ent-input">{sort} <span style="margin-left:auto;">▾</span></span></span></div>
      <div class="ent-tb-r"><span class="ent-lay">{ENT_LIST_ICO}</span><span class="ent-lay on">{ENT_GRID_ICO}</span></div>
    </div>'''

def ent_applied(chips):
    n = len(chips)
    return f'''<div class="fgroup ent-applied"><h3>{n} Applied Filter{"s" if n != 1 else ""} {ENT_CHEV}</h3>
      <div style="margin-top:8px;display:flex;flex-direction:column;gap:8px;">{"".join(f'<span class="ent-chip">{ENT_X}{c}</span>' for c in chips)}</div>
      <p class="small" style="margin-top:10px;text-decoration:underline;">Clear all</p></div>'''

def ent_inputs(lo, hi, prefix=""):
    p = f'<span class="muted">{prefix}</span>' if prefix else ""
    return f'<div class="row ent-pr" style="gap:6px;align-items:center;margin-top:8px;"><span class="ent-input">{p}{lo}</span><span class="muted">–</span><span class="ent-input">{p}{hi}</span></div>'

def ent_slider(n_stops, a, b, labels=None):
    l = a / (n_stops - 1) * 100; r = b / (n_stops - 1) * 100
    ticks = "".join(f'<span class="ent-tick" style="left:{i/(n_stops-1)*100}%;"></span>' for i in range(n_stops)) if labels else ""
    lab = '<div class="row" style="gap:2px;font-size:10px;color:#777;margin-top:6px;">' + "".join(f'<span style="flex:1;text-align:{"left" if i==0 else "right" if i==len(labels)-1 else "center"};">{x}</span>' for i, x in enumerate(labels)) + '</div>' if labels else ""
    return f'''<div class="ent-track">{ticks}<span class="ent-thumb" style="left:{l}%;"></span><span class="ent-thumb" style="left:{r}%;"></span></div>{lab}'''

def price_range():
    return ent_inputs("0", "450", "$") + ent_slider(2, 0, 1)

def minmax(lo, hi, unit=""):
    return ent_inputs(lo, hi) + ent_slider(6, 1, 3, ["1", "2", "3", "4", "5", "6+"])

def stepped(stops, a, b, lo=None, hi=None):
    return ent_inputs(lo or stops[a], hi or stops[b]) + ent_slider(len(stops), a, b, stops)

def filters(groups, applied=None):
    out = []
    if applied: out.append(ent_applied(applied))
    for name, src, opts, note in groups:
        if isinstance(opts, str):
            o = opts; active = False
        elif not opts:
            o = price_range(); active = False
        elif str(opts[0]).startswith("Search"):
            active = False
            items = "".join(f'<div class="chk"><b></b>{x}</div>' for x in opts[1:])
            o = (f'<div style="margin-top:8px;"><span class="ent-input" style="width:100%;color:#888;">⌕ {opts[0]}</span></div>'
                 f'<div class="ent-scroll">{items}</div>')
        else:
            active = any(str(x).startswith("✓") for x in opts)
            vis = opts[:5]
            o = "".join((f'<div class="chk on"><b>✓</b>{x[1:].strip()}</div>' if str(x).startswith("✓") else f'<div class="chk"><b></b>{x}</div>') for x in vis)
            if len(opts) > 5 or any("more" in str(x) for x in opts): o += '<p class="small" style="margin-top:6px;text-decoration:underline;">Show more</p>'
        if active: o += '<p class="small muted" style="margin-top:6px;text-decoration:underline;">Clear</p>'
        n = f'<div class="note" style="margin-top:4px;">{note}</div>' if note else ""
        out.append(f'<div class="fgroup"><h3>{name} {ENT_CHEV}</h3><div style="margin-top:4px;">{src}</div>{o}{n}</div>')
    return "".join(out)

def ent_products(sidebar_groups, applied, cards_html, sort="BGG rank", cols=3, count="2,379", extra_anno=""):
    return f'''{ent_toolbar(sort)}
    <div class="row ent-body" style="gap:28px;margin-top:14px;align-items:flex-start;">
      <div class="ent-side" style="width:240px;flex-shrink:0;">{filters(sidebar_groups, applied)}</div>
      <div style="flex:1;min-width:0;"><div class="grid g{cols} ent-grid">{cards_html}</div>
        <p class="center" style="margin-top:20px;"><span class="btn">Load more</span></p><p class="center muted" style="margin-top:6px;font-size:11px;">Showing 24 of {count}</p></div>
    </div>
    <div class="anno"><strong>Matches Enterprise's collection UI:</strong> "Filter" button toggles the sidebar; "Sort by" dropdown; list / grid view icons; applied filters as the first sidebar group with ⓧ chips and "Clear all"; each group collapsible with counts, "Show more" and "Clear". On mobile the button reads "Filter &amp; Sort" and opens Enterprise's drawer with sort, filters and a "Show N results" button. Price uses Enterprise's own price range (inputs + slider); players, play time, complexity and rating reuse that same slider look over the band values. {extra_anno}</div>'''

BOARD_FILTERS = [
    ("Availability", mf("advent.availability_state"), ["In stock (2,242)", "Preorder (137)", "Out of stock (1,120)"], "Three options only (Dean): In stock includes games we order in from the supplier; Preorder covers preorders with or without a date. Replaces the native in/out of stock filter."),
    ("Price", mf("variant price"), [], "Native range: min / max inputs"),
    ("Product type", mf("product_type"), ["Board Game", "Expansion", "Card Game"], ""),
    ("Game type", mf("bgg.type"), ["Strategy", "Family", "Party", "Thematic", "Wargames", "+ 3 more"], ""),
    ("Players", mf("bgg.supports_players") + ' <span class="vol tweak">min/max tweak</span>', minmax("2", "4"), "Min/Max like Meeplewatch. Min and max can be the same (1 and 1 shows solo-only games). Script ticks every count in between on the native list filter."),
    ("Play time", mf("bgg.playtime_band") + ' <span class="vol tweak">stepped slider</span>', stepped(["&lt;30m", "30-60", "1-2h", "2h+"], 1, 2, "30 min", "2 hrs"), "Min and max boxes each hold a single time. Slider snaps to the bands and ticks them. No app."),
    ("Youngest player", mf("bgg.age_band") + ' <span class="vol tweak">single select</span>', '<div style="margin-top:8px;"><span class="ent-input" style="width:100%;">8 years <span style="margin-left:auto;">▾</span></span></div>', "Ticks every band suitable for that age (6+, 8+). Dean asked for no multi-checkboxes here."),
    ("Complexity", mf("bgg.weight_band") + ' <span class="vol tweak">stepped slider</span>', stepped(["1", "2", "3", "4", "5"], 1, 3, "2.0", "3.9"), "BGG complexity score out of 5. Slider snaps to whole numbers and ticks the bands 1.0-1.9, 2.0-2.9, 3.0-3.9, 4.0-5.0."),
    ("Publisher", mf("vendor") + ' <span class="vol tweak">search box tweak</span>', ["Search publishers...", "Abacusspiele (12)", "Allplay (9)", "Asmodee (186)", "Capstone Games (14)", "Compass Games (22)", "Feuerland (11)", "GMT (214)", "Lookout Spiele (28)", "Stonemaier Games (31)", "Zoch Verlag (8)"], "800+ publishers: search box with a scrollable list (like Meeplewatch). Theme tweak."),
    ("Category / theme", mf("bgg.categories") + " " + mf("game_category", ""), ["Search categories...", "Adventure (412)", "Card Game (390)", "Economic (288)", "Fantasy (604)", "Historical (351)", "Horror (97)", "Science Fiction (318)", "Wargame (402)"], "Search box with a scrollable list. Metaobject reference."),
    ("Mechanic", mf("bgg.mechanics"), ["Search mechanics...", "Area Majority (244)", "Cooperative Game (301)", "Deck Building (176)", "Dice Rolling (520)", "Drafting (231)", "Hand Management (610)", "Tile Placement (198)", "Worker Placement (142)"], "Search box with a scrollable list. Metaobject reference."),
    ("Designer", mf("bgg.designers"), ["Search designers...", "Bruno Faidutti (14)", "Martin Wallace (22)", "Reiner Knizia (61)", "Stefan Feld (19)", "Uwe Rosenberg (27)", "Vital Lacerda (9)", "Vlaada Chvátil (12)"], "Search box with a scrollable list. Metaobject reference."),
    ("Artist", mf("bgg.artists"), ["Search artists...", "Beth Sobel (18)", "Ian O'Toole (24)", "Kwanchai Moriya (21)", "Lukas Siegmon (11)", "Vincent Dutrait (33)"], "Search box with a scrollable list. Metaobject reference."),
    ("Series / family", mf("bgg.families"), ["Search...", "Commands & Colors"], ""),
    ("Base game or expansion", mf("bgg.is_expansion"), ["Base game", "Expansion"], ""),
    ("Offers", mf("tags"), ["On sale", "Clearance", "Dings & dents", "Kickstarter"], "State tags only"),
    ("BGG rating", mf("bgg.rating_band", "new") + ' <span class="vol tweak">min select</span>', '<div style="margin-top:8px;"><span class="ent-input" style="width:100%;">7.5 and up <span style="margin-left:auto;">▾</span></span></div>', "Needs a rating band field (8+, 7.5+, 7+, 6.5+, 6+)."),
    ("BGG rank", mf("bgg.rank_band", "new"), ["Top 100", "Top 500", "Top 1000"], "Optional. Rank sort covers most of this."),
]
AVAIL_ON = ("Availability", BOARD_FILTERS[0][1], ["✓ In stock (2,242)", "Preorder (137)", "Out of stock (1,120)"], BOARD_FILTERS[0][3])
# Board Games sidebar order (all filters live in Enterprise's sidebar, applied filters group on top)
# BGG rating and BGG rank filters removed (Dean): new games have no rating or rank yet
SIDEBAR = [AVAIL_ON] + [BOARD_FILTERS[i] for i in (1, 4, 5, 6, 7, 3, 2, 8, 9, 10, 11, 12, 13, 14, 15)]

CN = ' <span class="lbl" style="border-color:#9a5b2b;color:#9a5b2b;">content needed</span>'
L1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante venenatis dapibus."
L2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris."

# ================================================================ HOME
home = sec("Gallery (promo tiles)", f'''
    <div class="grid" style="grid-template-columns:2fr 1fr;gap:12px;">
      <div class="img" style="height:340px;flex-direction:column;align-items:flex-start;justify-content:flex-end;padding:24px;text-transform:none;letter-spacing:0;color:#333;font-size:14px;">
        <span class="pill">Launch</span><h1 style="margin-top:8px;">Welcome to the new look Advent Games!</h1>
        <p class="muted" style="margin-top:6px;">Same friendly service, a much easier way to find your next game.</p>
        <a href="article.html" class="btn solid" style="margin-top:12px;">Read the blog post</a></div>
      <div class="grid" style="gap:12px;">
        <div class="img" style="height:164px;flex-direction:column;align-items:flex-start;justify-content:flex-end;padding:16px;text-transform:none;letter-spacing:0;color:#333;"><h3>Just arrived this week</h3><span class="small" style="text-decoration:underline;">See what's new</span></div>
        <div class="img" style="height:164px;flex-direction:column;align-items:flex-start;justify-content:flex-end;padding:16px;text-transform:none;letter-spacing:0;color:#333;"><h3>Preorders open</h3><span class="small" style="text-decoration:underline;">Reserve the big December releases</span></div>
      </div></div>
    <div class="anno">Static tiles, no auto-rotate. Dean flagged constant moving banners on Gameology as a dislike, and it fits the moodboard's "modular card-grid hero" direction. Dean edits image, heading, link per tile. Slideshow remains available if he wants one rotating hero for big campaigns.</div>''',
    note="hero · 1 large + 2 small tiles")

home += sec("Featured collection", f'''
    <div class="row" style="justify-content:space-between;align-items:end;margin-bottom:14px;"><div><h2>Just arrived</h2><p class="muted small">Fresh off the truck and ready to ship today.</p></div><a href="collection-preorders.html#just-arrived" class="small" style="text-decoration:underline;">View all</a></div>
    {carousel(ROW_JUST)}
    <div class="anno">Collection: <strong>Just Arrived</strong> (tag {mf("new-arrival")}, set by the 30-day job on {mf("advent.arrived_at")}). Carousel: side-scrolls with arrows on desktop, swipe on mobile (Enterprise featured collection, carousel layout). Order needs to follow arrival date, see Data Map gap #8.</div>''',
    note="carousel · Dean's #1 browse path", sid="just-arrived-row")

home += sec("Featured collection", f'''
    <div class="row" style="justify-content:space-between;align-items:end;margin-bottom:14px;"><div><h2>New to preorder</h2><p class="muted small">Reserve before they sell through.</p></div><a href="collection-preorders.html" class="small" style="text-decoration:underline;">All preorders</a></div>
    {carousel(ROW_PRE)}''', note="carousel · collection: New to Preorder")

home += sec("Collection list", f'''
    <h2>Find your next game</h2><p class="muted small" style="margin-top:4px;">Browse by the way you like to play.</p>
    <div class="grid g4" style="margin-top:16px;">
      {"".join(f'<a href="collection.html"><div class="img" style="height:120px;">Collection image</div><p class="small" style="margin-top:6px;font-weight:600;">{x}</p></a>' for x in ["Strategy","Family","Party","Thematic","Wargames","Solo games","Two-player","Kids"])}
    </div>
    <div class="anno">Each tile is a real smart collection with products behind it (bgg.type / supports_players rules), so none render empty. Collection images give the "banner and collection background images tie the collections together" Dean asked for.</div>''',
    note="shop by game type · 8 tiles")

home += sec("Featured collection", f'''
    <div class="row" style="justify-content:space-between;align-items:end;margin-bottom:14px;"><h2>Best sellers</h2><a href="collection.html" class="small" style="text-decoration:underline;">View all</a></div>
    {carousel([card("Cascadia", "Flatout Games", "54.95", meta="1-4 · 30-60 min · 10+ · Complexity: 2.1"), card("Wingspan", "Stonemaier Games", "79.95", meta="1-5 · 60-120 min · 10+ · Complexity: 2.9"), card("Ark Nova", "Feuerland", "99.95", "sup", meta="1-4 · 2 hrs+ · 14+ · Complexity: 3.7"), card("Sky Team", "Le Scorpion Masqué", "39.95", meta="2 · Under 30 min · 12+ · Complexity: 2.1"), card("The Crew: Mission Deep Sea", "KOSMOS", "24.95", meta="2-5 · Under 30 min · 10+ · Complexity: 2.1")])}''',
    note="carousel · repeatable for any collection (Solo, Gateway, Staff picks)")

PICKS = [("Sky Team","Le Scorpion Masqué","39.95","2 · Under 30 min · 12+ · Complexity: 2.1","Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
         ("Cascadia","Flatout Games","54.95","1-4 · 30-60 min · 10+ · Complexity: 2.1","Integer posuere erat a ante venenatis dapibus posuere."),
         ("Ark Nova","Feuerland","99.95","1-4 · 2 hrs+ · 14+ · Complexity: 3.7","Donec ullamcorper nulla non metus auctor fringilla."),
         ("Nusfjord","Lookout Spiele","79.95","1-5 · 20-100 min · 12+ · Complexity: 2.9","Cras mattis consectetur purus sit amet fermentum.")]
picks_html = "".join('<div>' + card(t, v, p, meta=m) + '<p class="small" style="margin-top:8px;border-left:2px solid #999;padding-left:8px;font-style:italic;">"' + q + '"</p></div>' for t, v, p, m, q in PICKS)
home += sec("Featured collection",
    '<div class="row" style="justify-content:space-between;align-items:end;margin-bottom:14px;"><div><h2>Staff recommendations</h2><p class="muted small">What have we been playing this week?</p></div><a href="collection.html" class="small" style="text-decoration:underline;">All staff picks</a></div>'
    + '<div class="grid g4">' + picks_html + '</div>'
    + '<div class="anno">Leans on Dean\'s personal knowledge, the point of difference he named (range plus his personal service). Manual "Staff picks" collection, with a one-line note per game from ' + mf("advent.staff_note","new") + ' that also shows on the product page. Note hides when empty.</div>',
    note="staff picks", extra_tags=CN)
home += sec("Image with text",
    '<div class="row" style="gap:32px;align-items:center;"><div style="flex:1;"><div class="img" style="height:220px;">Photo: family playing</div></div>'
    + '<div style="flex:1;"><h2>New to board games? Start here</h2><p class="muted" style="margin-top:8px;">Every journey begins with a single step, and these collections will set you on the Board Game path. These games provide a strong base for learning essential board game mechanics, and are great fun for nearly all ages!</p>'
    + '<div class="row" style="gap:8px;margin-top:14px;flex-wrap:wrap;"><a href="collection.html" class="btn">Gateway games</a><a href="collection.html" class="btn">Family games</a><a href="collection.html" class="btn">Two-player</a></div></div></div>'
    + '<div class="anno">For the family buyer and gift buyer personas in Dean\'s design doc, who need simple guidance on age, play time and complexity. Buttons go to existing smart collections.</div>',
    note="beginner pathway", extra_tags=CN)
home += sec("Image with text",
    '<div class="row" style="gap:32px;align-items:center;"><div style="flex:1;"><h2>Gift cards</h2><p class="muted" style="margin-top:8px;">' + L1 + '</p><p style="margin-top:12px;"><span class="btn solid">Buy a gift card</span></p></div><div style="flex:1;"><div class="img" style="height:160px;">Gift card image</div></div></div>'
    + '<div class="anno">The current site has a Gift Vouchers category that Dean says never worked. Shopify gift cards are native, so this can launch working, and it is worth surfacing before Christmas.</div>',
    note="native gift cards", extra_tags=CN)

home += sec("Image banner", '''
    <div class="img" style="height:220px;flex-direction:column;text-transform:none;letter-spacing:0;color:#333;"><span class="pill">Campaign slot</span><h2 style="margin-top:8px;">Boxing Day sale starts 26 December</h2><p class="muted small" style="margin-top:4px;">Selected games, while stocks last.</p><span class="btn solid" style="margin-top:12px;">Set a reminder</span></div>
    <div class="anno">One campaign banner Dean swaps per season (Christmas gifts, Boxing Day, Essen releases). Pairs with Enterprise's Countdown timer section if he wants a timer. Keeps sale messaging in one place instead of everywhere.</div>''', note="seasonal campaign")

home += sec("Gallery", f'''
    <div class="row" style="justify-content:space-between;align-items:end;margin-bottom:14px;"><h2>Shop by publisher</h2><a href="brands.html" class="small" style="text-decoration:underline;">All brands A-Z</a></div>
    <div class="grid g6">{"".join('<a href="brand.html"><div class="img" style="height:70px;">Logo</div></a>' for _ in range(6))}</div>''', note="logo tiles link to brand collections")

home += sec("Image with text", '''
    <div class="row" style="gap:32px;align-items:center;"><div style="flex:1;"><div class="img" style="height:240px;">Photo: Dean / packing table / games shelf</div></div>
    <div style="flex:1;"><h2>Your friendly, local, online board game store</h2><p class="muted" style="margin-top:10px;">Owner-operated in Sydney, with a huge range, fair prices and the hard-to-find games other stores don't carry. Ask about a game, a preorder or an order you've already placed and you'll hear back from Dean, not an AI response.</p>
    <p style="margin-top:14px;"><a href="about.html" class="btn">Our story</a> <a href="help.html" class="btn ghost">Pickup &amp; shipping</a></p></div></div>''', note="brand story · USP")

home += sec("App block: Google Reviews", '''
    <h2 class="center">What our customers say</h2>
    <div class="grid g3" style="margin-top:16px;">''' + "".join('<div class="card small"><p>★★★★★</p><p style="margin-top:6px;">"Example review text pulled live from Google Reviews."</p><p class="muted" style="margin-top:8px;">Reviewer name · Google</p></div>' for _ in range(3)) + '</div>',
    kind="custom", note="Google Reviews integration (in scope)")

home += sec("BGG Hotness", '<div class="img" style="height:90px;flex-direction:column;">Trending on BoardGameGeek<span class="note">future roadmap, out of scope for launch. Slot reserved below reviews.</span></div>', kind="future", note="future", internal=True)

write("index.html", "Home", "index.json", "", home)

# ================================================================ COLLECTION (Board Games master)
def card_anatomy():
    return f'''
    <div class="row" style="gap:28px;align-items:flex-start;">
      <div style="width:220px;">{card("Nusfjord: Expansion Pack #1", "Lookout Spiele", "44.95", meta="1-5 · 20-100 min · 12+ · Complexity: 2.9", badge="Just arrived")}</div>
      <div style="flex:1;" class="small">
        <table class="tbl"><tr><th>Card element</th><th>Source</th><th>Notes</th></tr>
        <tr><td>Box art (square)</td><td>{mf("featured image")}</td><td>Fixed 1:1 ratio, contain not crop. Hover shows 2nd image (theme setting).</td></tr>
        <tr><td>Badge (one only)</td><td>{mf("advent.availability_state")} {mf("tags")}</td><td>Priority: Preorder &gt; Coming soon &gt; Sale &gt; Just arrived &gt; Back in stock &gt; Dings &amp; dents. Native badges + Liquid tweak.</td></tr>
        <tr><td>Wishlist heart</td><td>app</td><td><strong>Optional app, not in build scope.</strong> Shows only if Dean adds a wishlist app (monthly cost to him, plus setup time).</td></tr>
        <tr><td>Publisher</td><td>{mf("vendor")}</td><td>Native "show vendor"</td></tr>
        <tr><td>Year · BGG rating chip</td><td>{mf("bgg.year_published")} {mf("bgg.rating")}</td><td>One chip like Meeplewatch: "☆ 7.7 BGG". Hidden when blank (unreleased games). Rank is not shown on cards, it drives the default sort.</td></tr>
        <tr><td>Expansion badge</td><td>{mf("bgg.is_expansion")}</td><td>Inline badge, separate from the status badge, so a preorder expansion shows both.</td></tr>
        <tr><td>Title + price</td><td>{mf("title")} {mf("price")}</td><td>Strike-through only on genuine sales, see gap #3 (RRP)</td></tr>
        <tr><td>Availability line</td><td>{mf("advent.availability_state")} {mf("advent.eta")} {mf("advent.supplier_lead_time","new")}</td><td>Reuses Enterprise's card stock line (<code>product-inventory__status</code>: top rule, small text, normal / low-stock colour). We swap its text for our availability state ("In stock", "At supplier · ships 2-7 days", "Preorder · due Nov 2026") and keep the theme's low-stock level for "Only 2 left". Labels in Data Map state matrix.</td></tr>
        <tr><td>Play stats row (icons)</td><td>{mf("bgg.min_players")} {mf("bgg.max_players")} {mf("bgg.playtime_band")} {mf("bgg.min_age")} {mf("bgg.weight")}</td><td>Hidden if no BGG data (accessories). Complexity shown as BGG's decimal score out of 5 (e.g. 2.9/5). Labelled \"Complexity\" rather than BGG's \"Weight\" so non-hobbyists understand it (Dean).</td></tr>
        <tr><td>Quick add</td><td>native quick buy</td><td>Label switches: Add to cart / Preorder / Notify me. Single-variant games add straight to the drawer.</td></tr>
        </table></div></div>'''

coll = ent_banner('<a href="index.html">Home</a> / Board Games', "Board Games", "2,379", "Over 9,000 board games from family classics to 4-hour heavy euros. Use the filters to narrow by player count, play time and complexity, or jump into a type below.")


grid_cards = [card("Nusfjord", "Lookout Spiele", "79.95", meta="1-5 · 20-100 min · 12+ · Complexity: 2.9"),
              card("Three Days of Gettysburg: Deluxe", "GMT", "169.95", meta="1-2 · 2 hrs+ · 14+ · Complexity: 3.7"),
              card("Wingspan", "Stonemaier Games", "79.95", "sup", meta="1-5 · 60-120 min · 10+ · Complexity: 2.9"),
              '<div class="img" style="aspect-ratio:1/1.55;flex-direction:column;text-transform:none;letter-spacing:0;color:#333;padding:12px;text-align:center;"><span class="vol">Promo tile</span><h3 style="margin-top:8px;">New to preorder this month</h3><span class="small" style="text-decoration:underline;">Reserve now</span></div>',
              card("Ark Nova", "Feuerland", "99.95", meta="1-4 · 2 hrs+ · 14+ · Complexity: 3.7"),
              card("Baltic Empires", "Compass Games", "129.95", "pre", "Preorder", eta="Dec 2026", meta="1-4 · 2 hrs+ · 14+ · Complexity: 3.7", link="product-preorder.html"),
              card("Sky Team", "Le Scorpion Masqué", "39.95", meta="2 · Under 30 min · 12+ · Complexity: 2.1", badge="Sale", was="44.95"),
              card("Cascadia", "Flatout Games", "54.95", meta="1-4 · 30-60 min · 10+ · Complexity: 2.1"),
              card("Heat: Pedal to the Metal", "Days of Wonder", "84.95", "out", "Out of stock", meta="1-6 · 30-60 min · 10+ · Complexity: 2.1")]

coll += sec("Collection products", ent_products(SIDEBAR, ["Players: 2-4", "Complexity: 2.0-3.9", "In stock"], "".join(grid_cards), sort="BGG rank", cols=3, count="2,379",
    extra_anno='<br><br><strong>Sort by options:</strong> BGG rank (default), Best selling, Alphabetically A-Z / Z-A, Price low to high / high to low, Date new to old. "BGG rank" is Shopify\'s Featured (manual) order renamed in the theme, set nightly by Ben\'s script in rank order with unranked games last. Only one custom order per collection, so BGG rating can\'t also be a sort. <strong>Range filters:</strong> the slider look and min/max inputs are Enterprise\'s own price range UI, reused over the native band filters (no app). Free-value ranges (e.g. complexity 2.3 to 3.1) would need a filter app. <strong>Compare:</strong> switched off in theme settings (Dean: not needed). <strong>Default:</strong> "In stock" applied on arrival, matching the design doc\'s "hide out of stock while browsing". <strong>Paging:</strong> "Load more" keeps the footer reachable and URLs keep filter state.'),
    note="Enterprise toolbar · sidebar filters (Search & Discovery) · grid with promo tile")


def lvrow(title, vendor, price, avail, stats, btn="Add to cart", link="product.html"):
    return f"""<div class="lv"><div class="img" style="width:48px;height:48px;"> </div>
      <div><a href="{link}"><strong>{title}</strong></a><div class="muted" style="font-size:11px;">{vendor}</div>{bgg_line(title, rating_on=False)}</div>
      <div class="muted">{meta_icons(stats)}</div><div class="avail">{avail}</div><strong>${price}</strong><div class="qa" style="margin:0;">{btn}</div></div>"""

LIST_VIEW = sec("Collection products (list view)", '<div class="lv h"><span></span><span>Game</span><span>Players · time · complexity</span><span>Availability</span><span>Price</span><span></span></div>' + "".join([
    lvrow("Ark Nova", "Feuerland", "99.95", '<i></i>In stock', "1-4 · 2 hrs+ · Complexity: 3.7"),
    lvrow("Nusfjord: Expansion Pack #1", "Lookout Spiele", "44.95", '<i></i>In stock', "1-5 · 20-100 min · Complexity: 2.9"),
    lvrow("Wingspan", "Stonemaier Games", "79.95", '<i class="half"></i>At supplier · 2-7 days', "1-5 · 60-120 min · Complexity: 2.9"),
    lvrow("Spirit Island: Nature Incarnate", "Greater Than Games", "89.95", '<i class="hollow"></i>Preorder · Feb 2027', "1-4 · 60-120 min · Complexity: 3.7", "Preorder", "product-preorder.html"),
    lvrow("Heat: Pedal to the Metal", "Days of Wonder", "84.95", '<i class="hollow"></i>Out of stock', "1-6 · 30-60 min · Complexity: 2.1", "Notify me"),
    ]) + '<div class="anno">The list view icon in Enterprise\'s toolbar switches the grid to dense rows, like Meeplewatch\'s list view. For hobby gamers scanning a lot of titles, it shows the same data as the card in a scannable line. The column layout is a CSS/Liquid tweak on its list card. View choice is remembered per visitor.</div>',
    note="same data as the card, one line per game", kind="tweak")

coll += LIST_VIEW
coll += sec("Product card anatomy", card_anatomy(), note="applies to every product grid and carousel", kind="tweak", internal=True)

coll += sec("Rich text", '<h3>About our board game range</h3><p class="muted small" style="margin-top:6px;max-width:760px;">' + L2 + ' ' + L1 + '</p><div class="anno">SEO copy below the grid, so it never pushes products down. One short block per main collection (Board Games, Strategy, Family, Party, RPG, Accessories), explaining each type in Dean\'s voice for search visibility.</div>', note="SEO copy below grid", sid="sale", extra_tags=CN)
coll += sec("Featured collection", f'<h2>Recently viewed</h2>{carousel([card("Wingspan","Stonemaier Games","79.95",qa=False,meta=""), card("Ark Nova","Feuerland","99.95",qa=False,meta=""), card("Cascadia","Flatout Games","54.95",qa=False,meta=""), card("Sky Team","Le Scorpion Masqué","39.95",qa=False,meta=""), card("Nusfjord","Lookout Spiele","79.95",qa=False,meta="")])}', note="Enterprise recently viewed")
coll += '<div class="sec internal"><div class="anno"><strong>Same template serves:</strong> Shop All, every Board Games sub-collection, Sale (Clearance / Dings &amp; Dents / Weekly sale sub-collections), Best Sellers, BGG Top 100, Award Winners, LCGs, Miniatures, Kickstarter and the brand collections. Only the banner and filter visibility change.</div></div>'
write("collection.html", "Board Games", "collection.json", "board", coll)

# ================================================================ PREORDERS
pre = ent_banner('<a href="index.html">Home</a> / Preorders', "Preorders", "137", "Reserve upcoming games before they land. We'll email you the moment your copy is allocated.")
pre += sec("Rich text", f'''<div class="grid g3 small">
    <div class="card"><strong>1. Reserve and pay today</strong><p class="muted" style="margin-top:4px;">Preorders are charged at checkout, which locks in your copy and the price.</p></div>
    <div class="card"><strong>2. Ships on release</strong><p class="muted" style="margin-top:4px;">We dispatch within one working day of the game arriving with us.</p></div>
    <div class="card"><strong>3. Mixed orders wait for everything</strong><p class="muted" style="margin-top:4px;">Orders with in-stock items are held until the preorder lands, unless you pay for extra shipping to send them separately.</p></div></div>
    <div class="anno">From Dean's current preorder policy. Same copy appears in the PDP "How preorders work" accordion and the Help page, edited once in a metaobject or page block.</div>''', note="how preorders work · 3 steps")
pre_cards = ROW_PRE + [card("Dune: Imperium: Bloodlines", "Dire Wolf", "54.95", "pre", "Preorder", eta="Nov 2026", link="product-preorder.html"),
                       card("Earthborne Rangers: Legends", "Earthborne Games", "79.95", "pre", "Preorder", eta="Dec 2026", link="product-preorder.html"),
                       card("Pathfinder 2e: Lost Omens Atlas", "Paizo", "79.95", "pre", "Preorder", eta="Jan 2027", meta="RPG · Sourcebook", link="product-preorder.html")]
PRE_FILTERS = [BOARD_FILTERS[0], BOARD_FILTERS[1], ("Product type", mf("product_type"), ["Board Game","Expansion","RPG","Accessory"], ""), ("Expected arrival", mf("advent.eta_month","new"), ["✓ Nov 2026","Dec 2026","Jan 2027","Later"], "ETA is free text today, can't filter cleanly"), BOARD_FILTERS[4], BOARD_FILTERS[8]]
pre += sec("Collection products", ent_products(PRE_FILTERS, ["Expected arrival: Nov 2026"], "".join(pre_cards), sort="Date, new to old", cols=4, count="137",
    extra_anno='<br><br><strong>Sort:</strong> Date, new to old (newest preorders first). <strong>Mixed-catalogue filters</strong> (Dean\'s open question): Preorders and Just Arrived hold board games and RPGs together. Shopify only shows filter values that exist in the current results, so BGG filters collapse when an RPG-only result set is showing. Shorter set here (availability, price, type, expected arrival, players, publisher); the full set lives on Board Games.'),
    note="Enterprise toolbar · short filter set")
pre += sec("Collection products", f'''<h2>Just Arrived</h2><p class="muted small" style="margin-top:4px;">Same template, collection: Just Arrived. Sub-collections: New Board Games, New Expansions, New RPGs, New Accessories, Back in Stock.</p>
    <div class="grid g5" style="margin-top:14px;">{"".join(ROW_JUST)}</div>
    <div class="anno">Ordering must follow {mf("advent.arrived_at")}, not created date. A restocked old title would otherwise sit at the bottom. Fix: the stock import job reorders this manual collection by arrival date (Data Map gap #8).</div>''', note="template reuse", sid="just-arrived")
write("collection-preorders.html", "Preorders / Just Arrived", "collection.preorders.json", "preorders", pre)

# ================================================================ RPG
rpg_filters = [BOARD_FILTERS[0], BOARD_FILTERS[1],
    ("RPG system", mf("rpg.system") + " " + mf("rpg_system"), ["Search...", "✓ Pathfinder 2e", "D&amp;D 5e", "Call of Cthulhu 7e", "Starfinder"], "metaobject reference"),
    ("Category", mf("rpg.product_kind"), ["Core Rulebook", "Starter Set", "Adventure", "Campaign", "Sourcebook", "Solo RPG", "RPG Accessory"], ""),
    ("Publisher", mf("vendor"), ["Paizo", "Chaosium", "Free League"], ""),
    ("Genre", mf("bgg.categories"), ["Fantasy", "Horror", "Science Fiction"], "re-use BGG categories"),
    ("Setting", mf("rpg.setting", "new"), ["Golarion", "Forgotten Realms"], "optional, Dean listed Settings separately"),
    ("Designer", mf("bgg.designers"), ["Search..."], "")]
rpg = ent_banner('<a href="index.html">Home</a> / Roleplaying Games', "Roleplaying Games", "1,164", "Core rulebooks, starter sets, adventures and accessories for every table.", note="collection.rpg template · Enterprise banner, no image")
rpg += sec("Collection list", '<h3>Shop by system</h3><div class="grid g6" style="margin-top:12px;">' + "".join(f'<a href="collection-rpg.html"><div class="img" style="height:80px;">System logo</div><p class="small" style="margin-top:4px;">{x}</p></a>' for x in ["Pathfinder 2e","D&amp;D 5e","Call of Cthulhu","Starfinder","Alien RPG","Daggerheart"]) + '</div><div class="anno">One smart collection per major system (rule: rpg.system = X), created by the import script. Keeps tiles real and editable.</div>', note="system tiles")
rpg += sec("Image with text", '<div class="row" style="gap:32px;align-items:center;"><div style="flex:1;"><h2>New to roleplaying?</h2><p class="muted" style="margin-top:8px;">' + L2 + '</p><p style="margin-top:12px;"><a href="collection-rpg.html" class="btn">Shop starter sets</a></p></div><div style="flex:1;"><div class="img" style="height:180px;">RPG table photo</div></div></div><div class="anno">Starter sets are the easiest RPG sale. A short beginner block pointing at the Starter Sets kind.</div>', note="beginner pathway", extra_tags=CN)
RPG_CARDS = "".join(card(t, v, p, meta=m) for t,v,p,m in [("Pathfinder Player Core","Paizo","89.95","RPG · Core Rulebook · Pathfinder 2e"),("Call of Cthulhu Starter Set","Chaosium","44.95","RPG · Starter Set · Call of Cthulhu 7e"),("Alien RPG: Building Better Worlds","Free League","69.95","RPG · Sourcebook · Alien RPG"),("Pathfinder Beginner Box","Paizo","59.95","RPG · Starter Set · Pathfinder 2e"),("Ironsworn: Starforged","Tomkin Press","79.95","RPG · Solo RPG"),("Dice Set: Polyhedral 7","Chessex","14.95","RPG Accessory")])
rpg += sec("Collection products", ent_products(rpg_filters, ["System: Pathfinder 2e"], RPG_CARDS, sort="Best selling", count="1,164",
    extra_anno=f'<br><br>RPG cards swap the play-stats row for <strong>category · system</strong> from {mf("rpg.product_kind")} {mf("rpg.system")}. Same card snippet, conditional on product type = RPG.'), note="Enterprise toolbar · RPG filter set")
write("collection-rpg.html", "Roleplaying", "collection.rpg.json", "rpg", rpg)

# ================================================================ ACCESSORIES
acc_filters = [BOARD_FILTERS[0], BOARD_FILTERS[1],
    ("Accessory type", mf("product_type"), ["✓ Sleeves", "Dice", "Playmat", "Insert / Organiser", "Tokens / Scenery"], ""),
    ("Sleeve size", mf("advent.sleeve_size"), ["63.5 x 88 (standard)", "57.5 x 89 (euro)", "41 x 63 (mini)", "70 x 120 (tarot)"], "needs consistent formatting at import"),
    ("Made for", mf("advent.related_game_names", "new"), ["Search games...", "Wingspan", "Ark Nova"], "product references can't be filters, so a text mirror is needed"),
    ("Brand", mf("vendor"), ["Gamegenic", "Mayday", "Folded Space", "Chessex"], "")]
accp = ent_banner('<a href="index.html">Home</a> / Accessories &amp; Sleeves', "Accessories &amp; Sleeves", "1,412", "Protect, organise and upgrade the games you love.", note="collection.accessories template · Enterprise banner, no image")
ACC_CARDS = "".join(card(t, v, p, meta=m, link="product-accessory.html") for t,v,p,m in [("Matte Sleeves 63.5 x 88 (100)","Gamegenic","9.95","63.5 x 88 · 100 sleeves"),("Wingspan Organiser","Folded Space","39.95","Made for Wingspan"),("Euro Sleeves 59 x 92 (80)","Mayday","6.95","59 x 92 · 80 sleeves"),("Neoprene Playmat 60 x 35","Gamegenic","34.95","Playmat"),("Metal Coins Set","Stonemaier Games","44.95","Made for Scythe"),("Prime Sleeves 41 x 63 (50)","Gamegenic","6.95","41 x 63 · 50 sleeves")])
accp += sec("Collection products", ent_products(acc_filters, ["Accessory type: Sleeves"], ACC_CARDS, sort="Best selling", count="1,412",
    extra_anno=f'<br><br>Accessory cards show <strong>size · pack count</strong> or <strong>Made for X</strong> instead of play stats. Needs {mf("advent.pack_quantity","new")} for sleeve counts.'), note="Enterprise toolbar · accessory filter set")
write("collection-accessories.html", "Accessories", "collection.accessories.json", "acc", accp)

# ================================================================ BRANDS A-Z
brands = sec("Rich text", '<p class="small muted"><a href="index.html">Home</a> / Brands</p><h1 style="margin-top:8px;">Brands A-Z</h1><p class="muted" style="margin-top:6px;">Over 800 publishers, from Abacusspiele to Zoch Verlag.</p>', note="page.brands template")
brands += sec("Gallery", '<h3>Featured publishers</h3><div class="grid g6" style="margin-top:12px;">' + "".join('<a href="brand.html"><div class="img" style="height:70px;">Logo</div></a>' for _ in range(6)) + '</div>', note="logos, hand-picked")
brands += sec("Quick links", ''.join(f'<span class="pill" style="margin:0 4px 6px 0;">{x}</span>' for x in "# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()), note="'Jump to' letter anchors")
brands += sec("Link list", '<div class="grid g4 small">' + "".join(f'<div><strong>{L}</strong><p style="line-height:1.9;margin-top:4px;">' + "<br>".join(f'<a href="brand.html">{n}</a>' for n in ns) + '</p></div>' for L, ns in [("A",["Aetherworks","Alderac (AEG)","Asmodee","Awaken Realms"]),("C",["Chaosium","Compass Games","Czech Games Edition","CMON"]),("G",["Gamegenic","GMT","Greater Than Games","Garphill Games"]),("L",["Leder Games","Lookout Spiele","Lucky Duck Games"])]) + '</div><div class="anno">Each name links to a vendor smart collection (rule: vendor = X). The import script creates these and the menu that feeds this Link list, so Dean doesn\'t maintain 100+ links by hand.</div>', note="one list per letter")
write("brands.html", "Brands A-Z", "page.brands.json", "brands", brands)

# ================================================================ BRAND
brand = ent_banner('<a href="index.html">Home</a> / <a href="brands.html">Brands</a> / Stonemaier Games', "Stonemaier Games", "31", "Publisher of Wingspan, Scythe and Viticulture.", note="Enterprise banner · vendor collection description")
brand += sec("Featured collection", f'<h3>Best sellers from Stonemaier</h3><div style="margin-top:12px;">{carousel([card("Wingspan","Stonemaier Games","79.95"), card("Scythe","Stonemaier Games","119.95","sup"), card("Viticulture Essential","Stonemaier Games","89.95"), card("Wyrmspan","Stonemaier Games","89.95"), card("Expeditions","Stonemaier Games","129.95","pre","Preorder")])}</div>', note="optional")
brand += sec("Collection products", ent_products([BOARD_FILTERS[0],BOARD_FILTERS[1],BOARD_FILTERS[2],BOARD_FILTERS[4],BOARD_FILTERS[7]], None, "".join(card(t,"Stonemaier Games",p) for t,p in [("Wingspan","79.95"),("Wingspan: Asia","59.95"),("Scythe","119.95"),("Tapestry","119.95"),("Charterstone","99.95"),("Pendulum","89.95")]), count="31",
    extra_anno='<br><br>Same collection template with the Publisher filter hidden (Search &amp; Discovery hides single-value filters automatically). No filters applied here, so the Applied Filters group doesn\'t render.'), note="standard grid")
write("brand.html", "Brand collection", "collection.json (vendor)", "brands", brand)

def ent_predictive(q, rest, prods, sugg):
    rows = "".join(f'<div class="row" style="gap:14px;align-items:flex-start;margin-top:14px;"><div class="img" style="width:56px;height:56px;flex-shrink:0;"> </div><div><strong>{t}</strong><p style="margin-top:4px;">{p}</p><p class="muted small">{v}</p></div></div>' for t, p, v in prods)
    sg = "".join(f'<p style="margin-top:12px;">{a}<strong>{q}{b}</strong></p>' if a == "" else f'<p style="margin-top:12px;">{a}<strong>{q}</strong>{b}</p>' for a, b in sugg)
    return f'''<div style="border:1px solid #999;border-radius:10px;overflow:hidden;max-width:860px;">
      <div class="row" style="gap:0;padding:10px;border-bottom:1px solid var(--line);"><div class="field" style="width:170px;border-radius:999px 0 0 999px;">All <span style="float:right;">⌄</span></div><div class="field" style="flex:1;border-radius:0 999px 999px 0;color:#222;border-color:#333;">{q}{rest}<span style="float:right;color:#666;">✕ &nbsp;|&nbsp; 🎙</span></div></div>
      <div class="row" style="gap:0;align-items:stretch;"><div style="flex:1.8;padding:16px 20px;"><div class="row small" style="gap:22px;"><strong style="border-bottom:2px solid #222;padding-bottom:3px;">Products</strong><span class="muted">Collections</span><span class="muted">Articles</span></div>{rows}</div>
      <div class="small" style="flex:1;padding:16px 20px;border-left:1px solid var(--line);background:#fafafa;"><strong>Suggestions</strong>{sg}</div></div></div>'''

# ================================================================ SEARCH
search = sec("Predictive search", ent_predictive("nusf", "|", [("Nusfjord", "$79.95", "Lookout Spiele"), ("Nusfjord: Expansion Pack #1", "$44.95", "Lookout Spiele"), ("Nusfjord: Big Box", "$119.95", "Lookout Spiele")], [("", "jord"), ("", "jord expansion"), ("", "jord big box")])
    + '<div class="anno">Enterprise\'s own predictive search, unchanged: category dropdown on the left of the bar (scopes to a collection, set in the header settings), clear and voice buttons, tabs for Products / Collections / Articles, product rows with image, title, price and vendor, and a Suggestions column. Matches the "limited drop down results, then a full results page" Dean described. What we set up, not build: the dropdown\'s collections (All / Board Games / Roleplaying / Accessories) and Search &amp; Discovery synonyms for abbreviations ("D&amp;D" = "Dungeons &amp; Dragons", "TI4", "LCG"), plus which metafields are searchable so designer and mechanic names return results. Not promised: availability or BGG data in the dropdown rows (would be a template tweak; the results page cards carry it).</div>', note="Enterprise predictive search · native")
ART_CARD = '<div class="card small" style="aspect-ratio:auto;"><div class="img" style="height:120px;">Article image</div><p style="margin-top:8px;"><strong>Worker placement: where to start</strong></p><p class="muted">Dean | 3 March 2026</p></div>'
search += sec("Search results", '''<h1 class="center">Search</h1><div class="row" style="max-width:560px;margin:12px auto 18px;gap:0;"><div class="field" style="flex:1;color:#222;">worker placement</div><span class="btn solid" style="border-radius:0 4px 4px 0;">Search</span></div>''' + ent_products([BOARD_FILTERS[0], BOARD_FILTERS[1], BOARD_FILTERS[4], BOARD_FILTERS[5], BOARD_FILTERS[7], BOARD_FILTERS[2]], None, "".join(grid_cards[:3]+grid_cards[4:7]) + ART_CARD, sort="Relevance", count="148",
    extra_anno='<br><br><strong>Matches Enterprise\'s search page:</strong> "Search" heading with the search field, then the same toolbar and sidebar as collections. Sort is Relevance / Price low to high / Price high to low only (Shopify limits search sorting). No Products / Articles tabs on this page: matching blog articles appear inline as cards after the products. Filters are the same Search &amp; Discovery filters as collections.'), note="Enterprise search template · native")
write("search.html", "Search", "search.json", "", search)

def highlights(items):
    return '<div class="grid g4" style="margin-top:6px;">' + "".join(f'<div class="stat"><span class="small muted">{k}</span><b>{v}</b>{m}</div>' for k, v, m in items) + '</div>'

def details_tab(rows):
    return '<div class="kv">' + "".join(f'<div class="muted">{k}</div><div>{v}</div>' for k, v in rows) + '</div>'

# ================================================================ PRODUCT TEMPLATES (v2: data-rich top fold)
ALL_STATES = [("in", "In stock"), ("sup", "At supplier"), ("pre", "Preorder"), ("soon", "Coming soon"), ("out", "Out of stock")]

def st(keys, html, tag="span"):
    return f'<{tag} class="st {" ".join("st-"+k for k in keys.split())}">{html}</{tag}>'

def avail_card(eta="November 2026", release="14 Nov 2026", notice=True):
    nt = f'<div style="margin-top:8px;border-top:1px dashed var(--line);padding-top:8px;">⚠ Publisher update: this wave has slipped two weeks. {mf("advent.notice","new")}</div>' if notice else ""
    return f"""<div class="card small" style="margin-top:12px;padding:14px;">
      {st("in", '<div class="avail" style="font-size:13px;"><i></i><strong>In stock</strong> · dispatched in 1-3 business days</div><div class="muted" style="margin-top:4px;">Ready to ship from Sydney.</div>', "div")}
      {st("sup", '<div class="avail" style="font-size:13px;"><i class="half"></i><strong>Available from supplier</strong> · ships in 2-7 business days ' + mf("advent.supplier_lead_time","new") + '</div><div class="muted" style="margin-top:4px;">We order it in as soon as you check out.</div>', "div")}
      {st("pre", f'<div class="avail" style="font-size:13px;"><i class="hollow"></i><strong>Preorder</strong> · expected {eta} {mf("advent.eta")}</div><div class="muted" style="margin-top:4px;">Publisher release {release} {mf("advent.release_date")}. Charged now, shipped within one working day of release. Cancel any time before it leaves our supplier.</div>{nt}', "div")}
      {st("soon", f'<div class="avail" style="font-size:13px;"><i class="hollow"></i><strong>Coming soon</strong> · {eta}</div><div class="muted" style="margin-top:4px;">Preorders aren\'t open yet. Get an email the moment they are.</div>', "div")}
      {st("out", '<div class="avail" style="font-size:13px;"><i class="hollow"></i><strong>Out of stock</strong></div><div class="muted" style="margin-top:4px;">We\'ll email you as soon as it\'s back.</div>', "div")}
      <div class="note" style="margin-top:6px;">Custom Liquid block driven by {mf("advent.availability_state")}. Use the Availability switch in the top bar to see each state.</div></div>"""

def cta_row():
    return f"""<div class="row" style="gap:8px;margin-top:12px;align-items:stretch;">
      {st("in sup pre", '<div class="field" style="width:90px;">− 1 +</div>', "div")}
      {st("soon out", '<div class="field" style="flex:1;">Email address</div>', "div")}
      <span class="btn solid" style="flex:1;text-align:center;">{st("in sup", "Add to cart")}{st("pre", "Preorder now")}{st("soon out", ico("bell-ringing",15) + " Notify me")}</span><span class="btn">♡</span></div>
      {st("soon out", '<p class="note" style="margin-top:4px;">Back-in-stock / notify app block (same app as wishlist if possible).</p>', "div")}"""

def meta_line(year, rating, ratings, rank, designer):
    return f"""<div class="bggl" style="font-size:12.5px;margin-top:6px;gap:10px;"><span>{ico("calendar-blank",13)} {year}</span><span class="rb">{ico("star",12)} {rating} BGG</span><span class="muted">{ratings} ratings</span><span class="muted">{ico("trophy",13)} Rank #{rank}</span><span>{ico("pen-nib",13)} <a style="text-decoration:underline;">{designer}</a></span></div>
      <div style="margin-top:4px;">{mf("bgg.year_published")} {mf("bgg.rating")} {mf("bgg.num_ratings","new")} {mf("bgg.rank")} {mf("bgg.designers")}</div>"""

def stat_strip(items):
    return '<div class="grid stat-strip" style="grid-template-columns:repeat(' + str(len(items)) + ',minmax(0,1fr));gap:0;margin-top:14px;border:1px solid var(--line);border-radius:6px;">' + "".join(
        f'<div style="padding:10px 6px;text-align:center;{"border-left:1px solid var(--line);" if i else ""}"><div style="color:#333;">{ico(STAT_ICON.get(k, "star"), 22)}</div><div class="muted" style="font-size:10.5px;margin-top:2px;">{k}</div><strong style="font-size:13px;">{v}</strong><div>{m}</div></div>'
        for i, (k, v, m) in enumerate(items)) + '</div>'

DELIVERY = """<div class="small" style="margin-top:12px;line-height:1.8;">
      <div>""" + ico("truck",16) + """ <strong>$10</strong> Sydney Metro, Gosford &amp; Wollongong · <strong>$15</strong> rest of Australia · <strong>Free over $300</strong></div>
      <div>""" + ico("storefront",16) + """ Free pickup in Chatswood, Tuesday nights</div>
      <div class="st st-pre st-sup" style="color:#555;">""" + ico("package",16) + """ Mixed orders are held and shipped together unless you ask us to split</div></div>"""

def _acc_open(title, body):
    return f'<div class="acc-open small"><div class="row" style="justify-content:space-between;font-weight:600;"><span>{title}</span><span>–</span></div><div class="acc-body">{body}</div></div>'
POLICY_ACC = (
  _acc_open("Delivery &amp; pickup",
    "<p>We ship Australia-wide with Australia Post eParcel, tracked. Games are boxed and padded; small items may go in a satchel.</p>"
    "<ul><li><strong>$10</strong> Sydney Metro, Gosford and Wollongong</li><li><strong>$15</strong> rest of Australia</li><li><strong>Free</strong> on orders over $300</li></ul>"
    "<p>In-stock games are dispatched in 1-3 business days. Games we order in from our supplier ship in 2-7 business days.</p>"
    "<p><strong>Free pickup:</strong> Tuesday nights at Northside Gamers Group, Chatswood. Orders placed on a Monday or Tuesday are ready the following Tuesday.</p>"
    "<p>We currently ship within Australia only. For overseas delivery, email us for a quote.</p>"
    '<p class="note">Confirm with Dean: pickup venue and time (Chatswood RSL 6-9pm vs The Chatswood Club 6:30-9pm).</p>')
  + _acc_open("Returns &amp; damaged games",
    "<p><strong>Change of mind:</strong> let us know in writing within 7 days of delivery. The game must be unopened and in its original packaging. We offer an exchange or store credit. Preorders, special orders, sleeves and accessories can't be returned for change of mind.</p>"
    "<p><strong>Arrived damaged?</strong> Please note any damage when you receive the parcel, then email us for a Return Product Number (RPN). We'll replace the item, or give you a credit or refund for it.</p>"
    '<p><a href="help.html" style="text-decoration:underline;">Full returns policy</a></p>'
    '<p class="note">Copy rewritten from the current site&#39;s Returns page. Check the 7-day window and exclusions still apply, and that the wording sits right with Australian Consumer Law (Dean or his adviser to confirm).</p>')
)

def comp_block(items):
    if not items: return ""
    t, p, btn, more = items[0]
    dots = "".join(f'<span style="width:6px;height:6px;border-radius:50%;background:{"#333" if i==0 else "#ccc"};display:inline-block;"></span>' for i in range(len(items)))
    return (f'<div style="margin-top:16px;"><div class="row" style="justify-content:space-between;align-items:center;"><strong>You might also need...</strong><span class="muted">‹ &nbsp; ›</span></div>'
            f'<div class="row" style="gap:14px;align-items:center;margin-top:8px;padding:12px;background:#f2f2f2;border-radius:6px;"><div class="img" style="width:72px;height:72px;flex-shrink:0;"> </div>'
            f'<div style="flex:1;"><strong class="small">{t}</strong><p class="small" style="margin-top:2px;font-weight:600;">${p}</p><span class="btn" style="margin-top:6px;display:inline-block;padding:4px 14px;font-size:12px;border-radius:999px;">{btn}</span></div></div>'
            f'<div class="row" style="gap:5px;justify-content:center;margin-top:8px;">{dots}</div>'
            f'<p class="small muted" style="margin-top:4px;">{more}</p>'
            f'<div class="anno" style="margin-top:6px;"><strong>Enterprise\'s built-in complementary products block</strong> (the "You might also need..." slider on the demo product page), one product at a time with arrows. Fed by Shopify\'s native {mf("shopify--discovery--product_recommendation.complementary_products")} list. Ben\'s script fills it per product: expansions for base games (from {mf("bgg.expands")} on each expansion), then sleeves and accessories (from {mf("advent.related_game")}). Hides itself when the list is empty, so games without extras show nothing.</div></div>')



def comp_row(title, cards):
    return sec("Expansions &amp; accessories (full width)", f'<h2>{title}</h2><div class="grid g4" style="margin-top:12px;">{"".join(cards)}</div>'
        + f'<div class="anno">Moved out of the buy box into a full-width row of cards, below the description (Dean). Pulls from the expansions and accessories already linked to each game in Dean\'s product file: Ben\'s import writes them into Shopify\'s complementary products list ({mf("shopify--discovery--product_recommendation.complementary_products")}), and this section shows them as normal product cards. Hides when the list is empty. Enterprise\'s complementary block is a one-at-a-time slider, so a page-wide grid is a small theme tweak (a product grid section reading that list).</div>',
        note="full-width grid · hides when empty", kind="tweak")

def pdp2(title, vendor, price, crumbs, crumb_link, badges, meta, summary, strip, extra="", rrp="", gallery="Box art (zoom)", videos=True, eta="November 2026", comp=None, comp_off=None):
    vid = '<div class="img" style="height:60px;">▶ How to play</div>' if videos else '<div class="img" style="height:60px;"> </div>'
    r = f'<p class="small muted" style="margin-top:2px;">{rrp} {mf("advent.rrp","new")} · Card, PayPal or bank transfer</p>' if rrp else '<p class="small muted" style="margin-top:2px;">Card, PayPal or bank transfer</p>'
    watch = f'<p class="small" style="margin-top:10px;"><a href="#videos" style="text-decoration:underline;">{ico("play-circle",15)} Watch how to play</a> · <a href="#details" style="text-decoration:underline;">Full game details ↓</a></p>' if videos else '<p class="small" style="margin-top:10px;"><a href="#details" style="text-decoration:underline;">Full details ↓</a></p>'
    return sec("Product page (main product)", f'''
    <p class="small muted"><a href="index.html">Home</a> / <a href="{crumb_link}">{crumbs}</a> / {title}</p>
    <div class="row pdp-top" style="gap:36px;margin-top:12px;align-items:flex-start;">
      <div class="pdp-gal" style="flex:1.05;min-width:0;"><div class="img pdp-main" style="height:440px;">{gallery}</div>
        <div class="grid g5 pdp-thumbs" style="margin-top:8px;">{"".join('<div class="img" style="height:60px;"> </div>' for _ in range(4))}{vid}</div>
        <p class="note" style="margin-top:6px;">Gallery: box front, back, components, then YouTube videos added as product media (native "Add from URL"). Box art contained, never cropped. On phones it becomes a swipe gallery.</p></div>
      <div class="pdp-buy" style="flex:1;min-width:0;">
        <div class="o-head"><div class="row" style="gap:6px;flex-wrap:wrap;">{badges}</div>
        <p class="small" style="margin-top:6px;"><a href="brand.html" style="text-decoration:underline;">{vendor}</a> {mf("vendor")}</p>
        <h1 style="font-size:28px;margin-top:2px;line-height:1.15;">{title}</h1>
        {meta}</div>
        <div class="o-strip">{strip}</div>
        <div class="o-sum"><p class="muted small" style="margin-top:12px;">{summary} {mf("custom.game_summary")}</p>
        {extra}</div>
        <div class="o-price"><p style="margin-top:14px;font-size:24px;font-weight:700;">${price}</p>{r}</div>
        <div class="o-avail">{avail_card(eta=eta)}</div>
        <div class="o-cta">{cta_row()}</div>
        {comp_block(comp)}
        <div class="o-rest">{DELIVERY}
        {watch}
        {POLICY_ACC}
      </div></div></div>
    <div class="anno">Top fold carries everything a buyer needs to decide: BGG line (Meeplewatch), at-a-glance stats strip (Gameology's icon box, with our data), real dispatch promise per state, delivery costs from the current site, and a jump to videos (More Than Meeples). Description moves below the fold instead of being the wall of text competitors lead with. Built from Enterprise main-product blocks plus three Custom Liquid blocks (BGG line, stats strip, availability) fed by metafields. <strong>Mobile:</strong> narrow the window to see the phone order: title and BGG line first, then gallery, price, availability and button inside the first screen, then the stats strip. Same blocks, reordered with CSS.</div>''',
    note="buy box · sticky add to cart on scroll", extra_tags=" " + tag("BGG line + stats strip + availability = Custom Liquid blocks", "tweak"))

def mobile_fold(title, price, cta="Add to cart"):
    return sec("Product page (mobile order)", f'''<div class="row" style="gap:32px;align-items:flex-start;">
      <div style="width:300px;border:2px solid #555;border-radius:18px;padding:14px;flex-shrink:0;">
        <p class="small muted">Lookout Spiele</p><h3 style="font-size:18px;">{title}</h3>
        <div class="bggl" style="margin-top:4px;"><span>2017</span><span class="rb">{ico("star",11)} 7.6 BGG</span><span class="muted">Rank #387</span></div>
        <div class="img" style="height:230px;margin-top:8px;">Gallery (swipe)</div>
        <p style="margin-top:8px;font-size:20px;font-weight:700;">${price}</p>
        <div class="avail" style="font-size:12px;"><i></i>In stock · dispatched in 1-3 business days</div>
        <span class="btn solid" style="display:block;text-align:center;margin-top:8px;">{cta}</span>
        <div class="grid g4 center" style="gap:0;margin-top:10px;border:1px solid var(--line);border-radius:6px;font-size:10.5px;"><div style="padding:6px 2px;">{ico("users-three",16)}<br>1-5</div><div style="padding:6px 2px;border-left:1px solid var(--line);">{ico("clock",16)}<br>20-100m</div><div style="padding:6px 2px;border-left:1px solid var(--line);">{ico("person",16)}<br>12+</div><div style="padding:6px 2px;border-left:1px solid var(--line);">{ico("brain",16)}<br>2.9/5</div></div>
      </div>
      <div style="flex:1;min-width:0;"><div class="anno" style="margin-top:0;">On phones the title and BGG line sit above the gallery so the game is identified before the scroll, then price, availability and the button land inside the first screen. Stats strip follows straight after. Same blocks as desktop, reordered with CSS only. Sticky add to cart bar appears once the main button scrolls away (Enterprise setting).</div></div></div>''', note="first screen on a phone")

DESC_P = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante venenatis dapibus posuere velit aliquet. Cras mattis consectetur purus sit amet fermentum.",
          "Donec ullamcorper nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod semper. Maecenas sed diam eget risus varius blandit sit amet non magna."]
BOX_DEFAULT = ["1 game board", "5 player boards", "75 building cards", "60 wooden workers", "Fish, wood and gold tokens", "Rulebook"]

def details_section(rows, tabs=("Description", "Game details", "Reviews (12)"), on=0, bgg=True, box=None):
    box = box or BOX_DEFAULT
    def panel(name):
        n = name.lower()
        if n.startswith("description"):
            return (f'<div style="max-width:760px;"><p>{DESC_P[0]}</p><p style="margin-top:10px;">{DESC_P[1]}</p>'
                    f'<p class="small" style="margin-top:10px;text-decoration:underline;">Show more</p><p style="margin-top:8px;">{mf("body_html")}</p></div>'
                    '<div class="anno">Native product description, first two paragraphs then "Show more" (Meeplewatch), so long publisher blurbs stop pushing everything down. Component lists move out of here into their own tab.</div>')
        if "details" in n:
            return (details_tab(rows) + '<div class="anno">Spec rows from metafields (Custom Liquid). Pills link to pre-filtered collections (every designer, category, mechanic is clickable). Rows hide when empty.</div>')
        if "box" in n:
            return (f'<ul style="margin:0;padding-left:18px;line-height:1.9;">' + "".join(f"<li>{x}</li>" for x in box) + f'</ul><p style="margin-top:8px;">{mf("advent.components","new")} <span class="note">example contents</span></p>'
                    '<div class="anno">The component list Dean already writes into his descriptions, as a simple list in its own tab. Two ways to fill it: Ben\'s import splits it out of the description into a new multi-line field (advent.components), or Dean keeps it in the description under a "What\'s in the box" heading and the tab is dropped. Tab hides when empty (accessories, most RPG books).</div>')
        if n.startswith("review"):
            return ('<p class="small">★★★★★ 4.8 from 12 reviews</p>' + "".join(f'<div class="card small" style="margin-top:8px;"><strong>★★★★★ Reviewer name</strong><p class="muted" style="margin-top:4px;">{DESC_P[0][:90]}...</p></div>' for _ in range(2))
                    + '<div class="anno">Product reviews app block (app TBC: Shopify Product Reviews, Judge.me or similar). Not product data, so nothing for Ben here. Google Reviews (in scope) are store reviews and sit on the home page, not here.</div>')
        return ""
    t = "".join(f'<span data-tab="{i}"{" class=\"on\"" if i == on else ""}>{x}</span>' for i, x in enumerate(tabs))
    p = "".join(f'<div class="tabpanel" data-panel="{i}"{"" if i == on else " hidden"}>{panel(x)}</div>' for i, x in enumerate(tabs))
    attrib = f'<p class="small muted" style="margin-top:12px;">Game data from <span style="text-decoration:underline;">BoardGameGeek</span> {mf("bgg.id")}</p>' if bgg else ""
    return sec("Product details", f'''<div class="tabs wf-tabs">{t}</div><div style="margin-top:14px;">{p}</div>{attrib}
    <div class="note" style="margin-top:8px;">Click the tabs to see each one (Enterprise product details tabs).</div>''',
    note="tabs below the fold · click to switch", sid="details", extra_tags=" " + tag("spec rows via Custom Liquid", "tweak"))

def videos_section(name):
    return sec("Custom section: Product videos", f'''<h2>Watch before you buy</h2>
    <div class="grid g3" style="margin-top:12px;">{"".join(f'<div><div class="img" style="height:150px;">▶ YouTube</div><p class="small" style="margin-top:6px;"><strong>{t}</strong> <span class="muted">· {c}</span></p></div>' for t, c in [("How to play", "Watch It Played"), ("Review", "Shut Up &amp; Sit Down"), ("Playthrough", "Rahdo Runs Through")])}</div>
    <div class="anno">Dean wanted videos back but found them slow to add. Here he just pastes YouTube links into the product's media in Shopify admin and types the label (How to play / Review / Playthrough) as the alt text. This small custom section lists any videos the product has, labelled, and hides itself when there are none. No metafields, no app. Sits straight under the buy box, above the spec tabs, so the \"Watch how to play\" link only jumps a short way. Pattern taken from More Than Meeples (but higher up the page than theirs). The channel name shows under each video, replacing the current site's separate Video Reviews Credits page.</div>''',
    kind="custom", note="appears only when the product has videos", sid="videos")

def comp_table():
    rows = [
     ("Meeplewatch", "BGG line under the title: year, rating, rank, ratings count, players, time, weight. Description collapsed with Show more. Designer / category / mechanic chips. Expansions tab with a count. 'Powered by BGG' credit.", "Directory layout: no buy box. Data is a dense grey line, easy to skim past."),
     ("Advent (current)", "Real delivery prices ($10 / $15 / free over $300). Notify me when out of stock. Component lists in descriptions.", "Players/time/age as a small table buried inside the description. Three sidebars squeeze the product."),
     ("Gameology", "Icon box for time / publisher / age beside the price. Delivery, click &amp; collect and in-store availability as clear rows. Instalments shown. 'Buy it with' fills the space under the gallery.", "Price-match and loyalty boxes crowd the buy box. Heavy RRP-saving messaging (not our tone)."),
     ("More Than Meeples", "Labelled videos: How to play, Review, Playthrough. Specs table (SKU, barcode, weight, dimensions). Clear 'In stock' line.", "Long description sits above everything else, videos far down the page."),
     ("Board Game Master", "One-line '1-5 Players | 60-120 Min | Ages 12+' right under the buy button.", "Everything else is a text dump."),
     ("Gamerholic / Games Empire", "Stock count shown ('Stock available: 20'). Instalments next to price.", "No game data at all above the fold."),
    ]
    return sec("Competitor learnings", '<div class="tblwrap"><table class="tbl"><tr><th>Site</th><th>Taken</th><th>Avoided</th></tr>' + "".join(f'<tr><td><strong>{a}</strong></td><td>{b}</td><td>{c}</td></tr>' for a, b, c in rows) + '</table></div>', note="Nusfjord compared across 7 sites", internal=True)

nus_rows = [
    ("Designer", f'<a style="text-decoration:underline;">Uwe Rosenberg</a> {mf("bgg.designers")}'),
    ("Artist", f'<a style="text-decoration:underline;">Lukas Siegmon</a> {mf("bgg.artists")}'),
    ("Publisher", f'<a href="brand.html" style="text-decoration:underline;">Lookout Spiele</a> {mf("vendor")}'),
    ("Game type", f'<span class="pill">Strategy</span> {mf("bgg.type")}'),
    ("Categories", f'<span class="pill">Economic</span> <span class="pill">Nautical</span> {mf("bgg.categories")}'),
    ("Mechanics", f'<span class="pill">Worker Placement</span> <span class="pill">Open Drafting</span> <span class="pill">Turn Order: Claim Action</span> {mf("bgg.mechanics")}'),
    ("Series", f'<a style="text-decoration:underline;">Nusfjord</a> {mf("bgg.families")}'),
    ("Players", f'1-5 {mf("bgg.min_players")} {mf("bgg.max_players")}'),
    ("Play time", f'20-100 min {mf("bgg.min_playtime")} {mf("bgg.max_playtime")}'),
    ("Age", f'12+ {mf("bgg.min_age")}'),
    ("Complexity", f'2.88 / 5 {mf("bgg.weight")}'),
    ("Year published", f'2017 {mf("bgg.year_published")}'),
    ("BoardGameGeek", f'☆ 7.6 from 7,551 ratings · Rank #387 · <a style="text-decoration:underline;">View on BGG ↗</a> {mf("bgg.rating")} {mf("bgg.rank")}'),
    ("Awards", f'[BGG honours list, e.g. award name and year] {mf("bgg.honors","new")} <span class="note">row hides when empty</span>'),
    ("Barcode", f'4260402312200 {mf("variant barcode")}'),
]
GAME_STRIP = stat_strip([("Players", "1-5", mf("bgg.supports_players")), ("Play time", "20-100 min", mf("bgg.min_playtime")), ("Age", "12+", mf("bgg.min_age")), ("Complexity", "2.88 / 5", mf("bgg.weight"))]) + \
    '<div class="small" style="margin-top:10px;line-height:2;"><span class="muted">Categories:</span> <a class="pill">Economic</a> <a class="pill">Nautical</a> &nbsp; <span class="muted">Mechanics:</span> <a class="pill">Worker Placement</a> <a class="pill">Open Drafting</a> ' + mf("bgg.categories") + ' ' + mf("bgg.mechanics") + '</div><p class="small" style="margin-top:4px;"><a href="help.html#games" style="text-decoration:underline;">What does complexity mean?</a></p>'

# ---- product.html: board game
prod = pdp2("Nusfjord", "Lookout Spiele", "107.95", "Board Games", "collection.html",
    badges=st("pre", '<span class="pill" style="background:#333;color:#fff;">Preorder</span>') + st("soon", '<span class="pill" style="background:#333;color:#fff;">Coming soon</span>') + st("in", '<span class="pill">Just arrived</span>'),
    meta=meta_line(2017, 7.6, "7,551", 387, "Uwe Rosenberg"),
    summary="Grow a Norwegian fishing village: build your fleet, clear the forest and keep the village elders happy. Worker placement from the designer of Agricola.",
    strip=GAME_STRIP, rrp="RRP $120.00 · you save $12.05",
    comp_off=[("Nusfjord: Expansion Pack #1", "44.95", "Add to cart", ""), ("Nusfjord: Big Box", "119.95", "Preorder", ""), ("Matte Sleeves 63.5 x 88 (100)", "9.95", "Add to cart", ""), ("Nusfjord Organiser", "34.95", "Add to cart", "")])
prod += videos_section("Nusfjord")
prod += details_section(nus_rows)
prod += comp_row("Expansions &amp; accessories for Nusfjord", [card("Nusfjord: Expansion Pack #1","Lookout Spiele","44.95",meta=""), card("Nusfjord: Big Box","Lookout Spiele","119.95","pre","Preorder",meta=""), card("Matte Sleeves 63.5 x 88 (100)","Gamegenic","9.95",meta="",link="product-accessory.html"), card("Nusfjord Organiser","Folded Space","34.95",meta="",link="product-accessory.html")])
prod += sec("Rich text", '<div class="row" style="gap:20px;align-items:flex-start;"><div class="img" style="width:64px;height:64px;border-radius:50%;flex-shrink:0;">Dean</div><div><h3>Why we like it</h3><p class="muted" style="margin-top:6px;font-style:italic;">"' + L1 + ' Sed posuere consectetur est at lobortis."</p><p class="small" style="margin-top:6px;">Dean, Advent Games</p></div></div><div class="anno">Optional one or two lines from ' + mf("advent.staff_note","new") + '. Only shows when filled, so Dean can add notes to a handful of favourites rather than 11,000 products. The same note feeds the "Staff recommendations" row on the home page.</div>', note="staff note · hides when empty", kind="tweak", extra_tags=CN)
prod += sec("Product recommendations", f'<h2>You might also like</h2><div style="margin-top:12px;">{carousel([card("Agricola","Lookout Spiele","99.95"), card("Caverna","Lookout Spiele","129.95","sup"), card("Hallertau","Lookout Spiele","99.95"), card("Fields of Arle","Lookout Spiele","119.95","out"), card("A Feast for Odin","Lookout Spiele","139.95")])}</div><div class="note" style="margin-top:6px;">Shopify related products, overridable per product via {mf("shopify--discovery--product_recommendation.related_products")}.</div>', note="related products")
prod += sec("FAQ", '<h3>Questions about buying from Advent</h3>' + "".join(f'<div class="acc small"><span>{q}</span><span>+</span></div>' for q in ["When will my order be dispatched?", "Is this the English edition?", "Do you offer pickup?", "What if the game arrives damaged?"]), note="cc-faq · shared content")
prod += sec("Featured collection", '<h3>Recently viewed</h3><p class="note">Enterprise recently viewed products</p>', note="recently viewed")
prod += comp_table()
write("product.html", "Product: board game", "product.json", "board", prod, states=("in", ALL_STATES))

# ---- product-preorder.html: expansion on preorder
cc_rows = [("Requires", f'<a href="product.html" style="text-decoration:underline;">Commands &amp; Colors: Napoleonics (base game)</a> {mf("bgg.expands")}'),
           ("Designer", f'<a style="text-decoration:underline;">Richard Borg</a> {mf("bgg.designers")}'), ("Publisher", f'<a href="brand.html" style="text-decoration:underline;">GMT</a> {mf("vendor")}'),
           ("Categories", f'<span class="pill">Historical</span> <span class="pill">Napoleonic</span> {mf("bgg.categories")}'),
           ("Mechanics", f'<span class="pill">Dice Rolling</span> <span class="pill">Hand Management</span> {mf("bgg.mechanics")}'),
           ("Series", f'<a style="text-decoration:underline;">Commands &amp; Colors</a> {mf("bgg.families")}'),
           ("Release date", f'14 Nov 2026 {mf("advent.release_date")}')]
ppre = pdp2("Commands &amp; Colors: Napoleonics Expansion #7: The Grand Battles", "GMT", "144.95", "Preorders", "collection-preorders.html",
    badges=st("pre", '<span class="pill" style="background:#333;color:#fff;">Preorder</span>') + st("soon", '<span class="pill" style="background:#333;color:#fff;">Coming soon</span>') + '<span class="xb" style="background:#e2e2e2;border-radius:3px;padding:2px 8px;font-size:11px;font-weight:600;">Expansion</span> ' + mf("bgg.is_expansion"),
    meta=f'<div class="bggl" style="font-size:12.5px;margin-top:6px;gap:8px;"><span>2026</span><span class="muted">Not yet rated on BGG</span><span>by <a style="text-decoration:underline;">Richard Borg</a></span></div><div style="margin-top:4px;" class="note">Rating and rank chips hide until BGG has data.</div>',
    summary="Two-board grand battles for up to eight players, using the Napoleonics system.",
    strip=stat_strip([("Players", "2-8", ""), ("Play time", "2 hrs+", ""), ("Age", "14+", ""), ("Complexity", "2.6 / 5", "")]),
    extra=f'<div class="card small" style="margin-top:12px;background:#f4f4f4;"><strong>Expansion:</strong> needs <a href="product.html" style="text-decoration:underline;">Commands &amp; Colors: Napoleonics</a> to play. {mf("bgg.is_expansion")} {mf("bgg.expands")}</div>',
    videos=False, eta="November 2026", rrp="RRP $170.00 · you save $25.05",
    comp_off=None)
ppre += details_section(cc_rows, tabs=("Description", "Game details", "Reviews"), box=["2 double-sided battle maps", "Army unit blocks and labels", "Command and tactician cards", "Scenario booklet", "Rules supplement"])
ppre += comp_row("Goes with this expansion", [card("Commands &amp; Colors: Napoleonics","GMT","129.95",meta=""), card("Exp. #5: Generals, Marshals, Tacticians","GMT","79.95",meta=""), card("Exp. #6: Generals","GMT","74.95","out","Out of stock",meta="")])
ppre += sec("Featured collection", f'<h2>More from the Commands &amp; Colors series</h2><div style="margin-top:12px;">{carousel([card("C&amp;C Napoleonics","GMT","129.95"), card("C&amp;C Ancients","GMT","119.95","sup"), card("C&amp;C Medieval","GMT","119.95"), card("Exp. #6: Generals","GMT","74.95","out"), card("Exp. #5: Generals, Marshals, Tacticians","GMT","79.95")])}</div><div class="note" style="margin-top:6px;">Series row: smart collection on {mf("bgg.families")}.</div>', note="optional", kind="tweak")
ppre += sec("State matrix", '''<div class="tblwrap"><table class="tbl"><tr><th>advent.availability_state</th><th>Badge</th><th>Availability line</th><th>Button</th><th>Purchasable?</th><th>Inventory policy</th></tr>
    <tr><td>in_stock</td><td>none (or Just arrived)</td><td>In stock · dispatched in 1-3 business days</td><td>Add to cart</td><td>Yes</td><td>Deny when 0</td></tr>
    <tr><td>at_supplier</td><td>none</td><td>Available from supplier · ships in 2-7 business days</td><td>Add to cart</td><td>Yes</td><td>Continue selling</td></tr>
    <tr><td>preorder</td><td>Preorder</td><td>Preorder · expected {eta}</td><td>Preorder now</td><td>Yes</td><td>Continue selling</td></tr>
    <tr><td>coming_soon</td><td>Coming soon</td><td>Coming soon · {eta}. Preorders open soon.</td><td>Notify me</td><td>No</td><td>Deny</td></tr>
    <tr><td>out_of_stock</td><td>Out of stock</td><td>Out of stock · we'll email you when it's back</td><td>Notify me</td><td>No</td><td>Deny</td></tr>
    <tr><td>discontinued</td><td>none</td><td>No longer available</td><td>hidden</td><td>No</td><td>Deny · hide from collections</td></tr></table></div>
    <div class="anno">Same rules drive the card availability line, PDP block, cart line labels and the Availability filter. Check what triggers Enterprise's own pre-order label (tag, inventory policy or metafield) against this.</div>''', note="for Ben + middleware", kind="tweak", internal=True)
write("product-preorder.html", "Product: expansion example", "product.json (same template, expansion blocks shown)", "preorders", ppre, states=("pre", ALL_STATES))

# ---- product-rpg.html
rpg_rows = [("System", f'<a href="collection-rpg.html" style="text-decoration:underline;">Pathfinder 2e</a> {mf("rpg.system")}'),
            ("Category", f'<a href="collection-rpg.html" style="text-decoration:underline;">Core Rulebook</a> {mf("rpg.product_kind")}'),
            ("Publisher", f'<a href="brand.html" style="text-decoration:underline;">Paizo</a> {mf("vendor")}'),
            ("Designers", f'<a style="text-decoration:underline;">Logan Bonner</a>, <a style="text-decoration:underline;">Mark Seifter</a> {mf("bgg.designers")}'),
            ("Genre", f'<span class="pill">Fantasy</span> {mf("bgg.categories")}'),
            ("Year published", f'2023 {mf("bgg.year_published")}'),
            ("Barcode", f'9781640785540 {mf("variant barcode")}')]
prpg = pdp2("Pathfinder Player Core", "Paizo", "89.95", "Roleplaying", "collection-rpg.html",
    badges=f'<span class="pill">Core Rulebook</span> {mf("rpg.product_kind")}',
    meta=f'<div class="bggl" style="font-size:12.5px;margin-top:6px;gap:8px;"><span>2023</span><span><a href="collection-rpg.html" style="text-decoration:underline;">Pathfinder 2e</a></span><span class="muted">Remastered</span></div><div style="margin-top:4px;">{mf("bgg.year_published")} {mf("rpg.system")}</div>',
    summary="Everything players need to build characters and play Pathfinder: ancestries, classes, spells and the core rules.",
    strip=stat_strip([("System", "Pathfinder 2e", mf("rpg.system")), ("Category", "Core Rulebook", mf("rpg.product_kind")), ("Publisher", "Paizo", mf("vendor"))]),
    videos=False, rrp="RRP $99.95 · you save $10.00")
prpg += details_section(rpg_rows, tabs=("Description", "Book details", "Reviews"), bgg=False)
prpg += sec("Featured collection", f'<h2>More for Pathfinder 2e</h2><div style="margin-top:12px;">{carousel([card("Pathfinder GM Core","Paizo","89.95",meta="RPG · Core Rulebook"), card("Pathfinder Beginner Box","Paizo","59.95",meta="RPG · Starter Set"), card("Pathfinder 2e: Lost Omens Atlas","Paizo","79.95","pre","Preorder",meta="RPG · Sourcebook",link="product-preorder.html"), card("Pathfinder Flip-Mat","Paizo","24.95",meta="RPG Accessory")], 5)}</div><div class="anno">Smart collection per system ({mf("rpg.system")}). The system metaobject image doubles as the collection logo.</div>', note="same-system row", kind="tweak")
write("product-rpg.html", "Product: RPG example", "product.json (same template, RPG blocks shown)", "rpg", prpg, states=("in", ALL_STATES))

# ---- product-accessory.html
pacc = pdp2("Matte Sleeves 63.5 x 88 (100)", "Gamegenic", "9.95", "Accessories", "collection-accessories.html",
    badges=f'<span class="pill">Sleeves</span> {mf("product_type")}',
    meta=f'<div class="small" style="margin-top:6px;">Made for: <a href="product.html" style="text-decoration:underline;">Nusfjord</a> {mf("advent.related_game","fix")}</div><div class="note" style="margin-top:4px;">Game-specific accessories (organisers, upgrades) link back to their game. The "Fits" list for generic sleeves stays hidden until sleeve sizes are filled in for games.</div>',
    summary="Standard American-size sleeves with a matte finish for shuffle-heavy games.",
    strip=stat_strip([("Sleeve size", "63.5 x 88", mf("advent.sleeve_size")), ("Pack", "100", mf("advent.pack_quantity","new")), ("Finish", "Matte", "")]),
    videos=False, gallery="Product photo")
pacc += details_section([], tabs=("Description", "Reviews"), bgg=False)
pacc += sec("Featured collection", f'<h2>Other sleeves in this size</h2><div style="margin-top:12px;">{carousel([card("Prime Sleeves 63.5 x 88 (50)","Gamegenic","6.95",meta=""), card("Premium Sleeves 63.5 x 88 (100)","Mayday","8.95",meta=""), card("Clear Sleeves 63.5 x 88 (100)","Ultra Pro","5.95",meta="")])}</div><div class="note" style="margin-top:6px;">Accessories filtered by {mf("advent.sleeve_size")}.</div>', note="same-size alternatives")
write("product-accessory.html", "Product: accessory example", "product.json (same template, game blocks hidden)", "acc", pacc, states=("in", ALL_STATES))


def drawer_line(vendor, title, price, avail):
    return (f'<div class="row" style="gap:14px;align-items:flex-start;padding:14px 0;border-bottom:1px solid var(--line);"><div class="img" style="width:76px;height:76px;flex-shrink:0;"> </div>'
            f'<div style="flex:1;"><p class="small muted">{vendor}</p><strong class="small">{title}</strong><p class="small" style="margin-top:2px;font-weight:600;">${price}</p>'
            f'<div class="avail" style="font-size:11px;margin-top:2px;">{avail}</div>'
            f'<div class="row" style="gap:10px;align-items:center;margin-top:8px;"><span style="border:1px solid #999;border-radius:999px;padding:3px 12px;font-size:12px;">−&nbsp;&nbsp; 1 &nbsp;&nbsp;+</span><span class="muted small" style="text-decoration:underline;">Remove</span></div></div>'
            f'<strong class="small">${price}</strong></div>')

def cart_drawer_sec(sid="cart-drawer"):
    body = ('<div style="max-width:420px;margin-left:auto;border:2px solid #555;border-radius:6px;overflow:hidden;background:#fff;">'
        '<div class="row" style="justify-content:space-between;align-items:center;padding:16px 18px;border-bottom:1px solid var(--line);"><h3>Your cart</h3><span class="small"><u>View cart</u> &nbsp;&nbsp; ✕</span></div>'
        '<div style="padding:14px 18px;border-bottom:1px solid var(--line);"><div class="row small" style="justify-content:space-between;"><u>Add order note</u><u>Estimate shipping</u></div>'
        '<span class="btn solid" style="display:block;text-align:center;margin-top:10px;border-radius:999px;">Checkout - $224.90 AUD</span> <span class="vol tweak">button goes to checkout</span></div>'
        '<div style="padding:12px 18px;background:#f2f2f2;text-align:center;"><p class="small" style="font-weight:600;">You\'re $75.10 away from free shipping</p><div style="height:6px;background:#ddd;border-radius:3px;margin-top:8px;"><div style="width:75%;height:6px;background:#333;border-radius:3px;"></div></div></div>'
        '<div style="padding:0 18px;">'
        + drawer_line("Lookout Spiele", "Nusfjord", "79.95", '<i></i>In stock')
        + drawer_line("GMT", "C&amp;C Napoleonics Exp. #7", "144.95", '<i class="hollow"></i>Preorder · due Nov 2026')
        + '</div>'
        '<div style="padding:14px 18px;"><div class="row" style="justify-content:space-between;align-items:center;"><strong>You may also like...</strong><span class="muted">‹ &nbsp; ›</span></div>'
        '<div class="row" style="gap:12px;align-items:center;margin-top:8px;padding:10px;background:#f2f2f2;border-radius:6px;"><div class="img" style="width:64px;height:64px;flex-shrink:0;"> </div><div><strong class="small">Matte Sleeves 63.5 x 88 (100)</strong><p class="small" style="font-weight:600;">$9.95</p><span class="btn" style="margin-top:4px;display:inline-block;padding:3px 12px;font-size:12px;border-radius:999px;">Add to cart</span></div></div></div>'
        '<div style="padding:0 18px 18px;"><div class="img" style="height:120px;flex-direction:column;align-items:flex-start;justify-content:center;padding:16px;text-transform:none;letter-spacing:0;color:#333;"><h3>New to preorder</h3><span class="btn" style="margin-top:8px;border-radius:999px;">Reserve now</span></div></div>'
        '</div>'
        '<div class="anno"><strong>Enterprise cart drawer, as on the demo:</strong> "View cart" link and close at the top, order note and shipping estimate links, a full-width main button, the free shipping progress bar (set to $300 in theme settings), line items with quantity and remove, a "You may also like..." slider (Shopify product recommendations; check in the theme editor whether it uses related or complementary products), and a promo image banner at the bottom that Dean can swap. <strong>Tweaks:</strong> (1) the main button reads "Checkout - $total" and goes straight to checkout instead of the theme\'s default "View cart - $total", since the drawer already shows everything the cart page does and the "View cart" link stays at the top for anyone who wants it. Small Liquid/JS change to the drawer snippet (button label and link to /checkout), to check for a theme setting first. (2) our availability line under each item (same snippet as the cards) so preorders are clear before checkout.</div>')
    return sec("Cart drawer", body, note="opens on add to cart · Enterprise cart drawer", sid=sid, kind="tweak")


# ================================================================ CART
def line(t, p, av, q=1):
    return f'<div class="row" style="gap:14px;align-items:center;border-bottom:1px solid var(--line);padding:12px 0;"><div class="img" style="width:70px;height:70px;"> </div><div style="flex:1;"><strong class="small">{t}</strong><div class="avail">{av}</div></div><div class="field" style="width:80px;">− {q} +</div><strong style="width:80px;text-align:right;">${p}</strong></div>'
def ymal_card(t, p):
    return f'<div class="row" style="gap:12px;align-items:center;padding:10px;background:#f2f2f2;border-radius:6px;flex:1;"><div class="img" style="width:72px;height:72px;flex-shrink:0;"> </div><div><strong class="small">{t}</strong><p class="small" style="font-weight:600;">${p}</p><span class="btn" style="margin-top:4px;display:inline-block;padding:3px 12px;font-size:12px;border-radius:999px;">Add to cart</span></div></div>'
cart = sec("Cart (main cart)", f'''<div class="row" style="gap:48px;align-items:flex-start;">
      <div style="flex:1.6;min-width:0;"><h1>Your cart</h1>
        <div style="padding:16px 20px;background:#f2f2f2;margin-top:16px;"><p class="small" style="font-weight:600;">You're $65.15 away from free shipping</p><div style="height:6px;background:#ddd;border-radius:3px;margin-top:10px;"><div style="width:78%;height:6px;background:#333;border-radius:3px;"></div></div></div>
        {drawer_line("Lookout Spiele", "Nusfjord", "79.95", '<i></i>In stock')}
        {drawer_line("GMT", "C&amp;C Napoleonics Exp. #7", "144.95", '<i class="hollow"></i>Preorder · due Nov 2026')}
        {drawer_line("Gamegenic", "Matte Sleeves 63.5 x 88 (100)", "9.95", '<i class="half"></i>At supplier · ships 2-7 days')}
        <div class="row" style="justify-content:space-between;align-items:center;margin-top:22px;"><h3>You may also like...</h3><span class="muted">‹ &nbsp; ›</span></div>
        <div class="row" style="gap:14px;margin-top:10px;">{ymal_card("Nusfjord Organiser", "34.95")}{ymal_card("The Crew: Mission Deep Sea", "24.95")}</div>
      </div>
      <div style="flex:1;min-width:0;margin-top:48px;"><div style="border:1px solid var(--line);padding:22px;">
        <h2>Order summary</h2>
        <div class="row small" style="justify-content:space-between;padding:14px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);margin-top:14px;"><span>Add order note</span><span>⌄</span></div>
        <p class="small" style="margin-top:14px;">Tax included, shipping calculated at checkout.</p>
        <div class="row" style="justify-content:space-between;margin-top:12px;"><strong>Subtotal:</strong><strong>$234.85 AUD</strong></div>
        <span class="btn solid" style="display:block;text-align:center;margin-top:14px;border-radius:999px;">Checkout</span>
        <p class="center small" style="margin-top:12px;text-decoration:underline;">Continue shopping</p></div>
        <div class="anno">Checkout is Shopify-hosted: shipping vs local pickup is chosen there (native). <strong>Bookable pickup dates/windows</strong> from the design doc fall under "complex delivery logic", excluded from scope.</div></div>
    </div>
    <div class="anno"><strong>Enterprise cart page, as on the demo:</strong> free shipping progress bar ($300 in theme settings), line items with publisher, quantity and remove, "You may also like..." slider under the items, and an Order summary box on the right with order note, tax line, subtotal, Checkout and Continue shopping. Only tweak: our availability line under each item (same snippet as the cards and drawer).</div>''', note="Enterprise main cart", kind="tweak")
cart += cart_drawer_sec("drawer")
write("cart.html", "Cart", "cart.json", "", cart)

# ================================================================ ACCOUNT
ACC_LINE = lambda t, q, p, ext: f'<div class="row" style="gap:12px;align-items:flex-start;padding:10px 0;border-bottom:1px solid var(--line);"><div class="img" style="width:56px;height:56px;flex-shrink:0;"> </div><div style="flex:1;"><strong>{t}</strong><p class="small muted">Qty {q}</p><div class="ext-slot small">{ext}</div></div><strong>${p}</strong></div>'
acct = sec("Customer accounts: Order status (Shopify-hosted)", f'''<div style="max-width:680px;margin:0 auto;border:1px solid var(--line);border-radius:10px;padding:18px;">
    <div class="row" style="justify-content:space-between;align-items:center;border-bottom:1px solid var(--line);padding-bottom:12px;"><div class="img" style="width:110px;height:34px;">Logo</div><span class="small">Shop · Orders · Profile</span></div>
    <p class="small muted" style="margin-top:14px;">&lt; Orders</p><h2>Order #10482</h2><p class="small muted">Confirmed 2 Oct 2026</p>
    <div class="ext-slot small" style="margin-top:10px;padding:10px;"><strong>Part of this order is a preorder.</strong> In-stock items are held and shipped together when the preorder lands, unless you've paid for split shipping. <span class="vol tweak">order-status.block.render</span></div>
    <div class="card small" style="margin-top:12px;"><strong>Confirmed</strong> · 2 Oct<p class="muted" style="margin-top:4px;">Native fulfilment timeline. Shows tracking once AusPost fulfils.</p></div>
    <div class="row" style="gap:8px;margin-top:12px;"><span class="btn">Buy again</span><span class="btn ghost">Request return</span><span class="btn ghost">Add items to this order <span class="vol tweak">order action</span></span></div>
    <h3 style="margin-top:18px;">Order summary</h3>
    {ACC_LINE("Nusfjord", 1, "107.95", '<span class="pill">In stock · waiting for the rest of your order</span> <span class="vol tweak">line-item render-after</span>')}
    {ACC_LINE("C&amp;C Napoleonics Exp. #7", 1, "144.95", '<span class="pill">Preorder · expected November 2026</span>')}
    {ACC_LINE("Matte Sleeves 63.5 x 88", 2, "19.90", '<span class="pill">Arriving from supplier · due in 2-7 business days</span>')}
    <p class="small" style="margin-top:12px;text-align:right;">Subtotal, shipping, total (native)</p>
    <h3 style="margin-top:14px;">Order details</h3><p class="small muted">Contact · Shipping address · Payment · Billing address (native)</p></div>
    <div class="anno"><strong>What this page really is:</strong> Shopify's own customer accounts page, not a theme template. Since Feb 2026 new stores can only use the current (hosted) customer accounts; the old theme-based account pages are deprecated. So Enterprise has no say in this layout. What we control: <strong>branding</strong> (logo, colours, fonts, corner style) in the Checkout &amp; accounts editor, and <strong>small add-ons in fixed slots</strong> from a custom app (customer account UI extensions). Everything not marked with a dashed box is Shopify's native page and looks the same on every store.<br><br><strong>The dashed boxes are the only custom parts</strong>, and each needs the custom app:<br>1. <strong>Status text under each item</strong> (target: line item render-after). Reads a per-item status the middleware writes to the order (order or line metafields). This is the closest Shopify gets to the design doc's "item-level status". It sits under each line, not as a status column in a table.<br>2. <strong>Preorder notice banner</strong> (order status block). Optional, plain text.<br>3. <strong>"Add items to this order"</strong> (order action menu item). The simple version opens instructions for the current workaround: choose the $0 "Order addition" shipping rate at checkout and note the order number. Actually merging into a paid order would need order editing through the app backend, a bigger build: treat as out of scope unless quoted.<br><br><strong>Scope check:</strong> none of this is theme work. It is a small custom app, deployed through the Shopify CLI, plus the middleware writing the statuses. Confirm whether it sits under the middleware line in the quote; if not, launch with the native page and the shipping-rate workaround only, and nothing is promised that can't be delivered.</div>''', kind="custom", note="native page · 3 extension slots marked")
acct += sec("Customer accounts: Order list + Profile (Shopify-hosted)", '<div class="grid g3 small"><div class="card"><strong>Orders</strong><p class="muted">Native list with status, Buy again, returns</p></div><div class="card"><strong>Profile</strong><p class="muted">Native: name, addresses, marketing consent</p></div><div class="card"><strong>Wishlist</strong><p class="muted">Optional app, not in scope. Lives on the storefront if added. Linked from the header, not inside the account.</p></div></div><div class="anno">Branding only, no layout changes. Sign-in is a one-time email code (no passwords), so migrated customers simply sign in with their email; there is nothing to activate or import. Enterprise\'s header "Account" link goes straight here.</div>', note="native pages")
write("account.html", "Account (Shopify-hosted)", "customer accounts (not a theme template)", "", acct, hosted=True)

# ================================================================ WISHLIST
wl = sec("App block: Wishlist", f'<h1>Your wishlist</h1><p class="muted small" style="margin-top:4px;">Saved games and their current availability. Share your list with family before birthdays and Christmas.</p><div class="grid g4" style="margin-top:16px;">{"".join([card("Ark Nova","Feuerland","99.95"), card("Spirit Island: Nature Incarnate","Greater Than Games","89.95","pre","Preorder",eta="Feb 2027",link="product-preorder.html"), card("Heat: Pedal to the Metal","Days of Wonder","84.95","out","Out of stock"), card("Wingspan Organiser","Folded Space","39.95",link="product-accessory.html")])}</div><div class="anno"><strong>Optional, not in the build scope.</strong> Enterprise has no native wishlist. From Dean\'s design doc, which calls it desirable but secondary. If he wants it: a wishlist app (e.g. Swym / Wishlist Plus), monthly app cost to Dean plus setup time to quote. What it gives: hearts on cards and PDP, guest wishlist that merges on login, share link, and back-in-stock / price-drop emails. One app can cover wishlist + back-in-stock alerts. App subscription is client cost.</div>', kind="custom", extra_tags=" " + tag("OPTIONAL APP", "custom"), note="optional app · not in scope · page.wishlist")
write("wishlist.html", "Wishlist", "page.wishlist.json", "", wl)

# ================================================================ ABOUT + CONTACT
ab = sec("Image banner", '<div class="img" style="height:220px;flex-direction:column;text-transform:none;letter-spacing:0;color:#333;"><h1>Your friendly, local, online board game store</h1><p class="muted" style="margin-top:6px;">Owner-operated in Sydney, shipping Australia-wide.</p></div>', note="page.about · tagline from Dean (replaces 'Where Play Comes Alive')")
ab += sec("Image with text", '<div class="row" style="gap:32px;align-items:center;"><div style="flex:1;"><div class="img" style="height:220px;">Photo: Dean / the shelves</div></div><div style="flex:1;"><h2>Integrity, great service and a huge range</h2><p class="muted" style="margin-top:8px;">We are an Australian online board game store based in Sydney. We keep our prices fair by running a lean operation and passing the savings on, and we go out of our way to find the hard-to-find games. You are not just a customer: we see you as a friend who shares our passion for the hobby.</p><p class="small" style="margin-top:10px;">Find Dean on BoardGameGeek: <u>Caldris</u></p></div></div><div class="anno">Copy drawn from the current About Us and Why Buy From Us pages (copywriting is client-supplied, so Dean refines). Founding year not stated on the current site (footer copyright says 2013), so it is left out until Dean confirms.</div>', note="our story")
ab += sec("Rich text", '<div style="max-width:720px;margin:0 auto;" class="center"><h2>How it started</h2><p class="muted" style="margin-top:10px;">' + L2 + '</p><p class="muted" style="margin-top:10px;">' + L1 + '</p></div><div class="anno">The current About page has values but no story: when Advent started, why, and how it has grown. A short history builds the trust the brief asks for. Dean to supply.</div>', note="our story", extra_tags=CN)
ab += sec("Multicolumn", '<div class="grid g4 small center">' + "".join(f'<div><div class="img" style="height:50px;width:50px;margin:0 auto;"> </div><strong style="display:block;margin-top:8px;">{t}</strong><p class="muted">{d}</p></div>' for t, d in [("Owner-operated","Questions answered promptly by Dean, not a call centre"),("Huge range","11,000+ games, preorders and hard-to-find titles"),("Fast, careful delivery","Tracked AusPost eParcel, boxed and padded"),("Fair prices","Flat-rate shipping, free over $300")]) + '</div><div class="anno">Value props are the current "Why Buy From Us" page condensed.</div>', note="why buy from us")
ab += sec("Image with text", '<div class="row" style="gap:32px;align-items:center;"><div style="flex:1;"><h2>Pick up in Chatswood</h2><p class="muted" style="margin-top:8px;">Skip the shipping. Collect your order free on Tuesday nights at the Northside Gamers Group in Chatswood, a friendly weekly games night. We\'ll confirm your pickup by email.</p><p style="margin-top:12px;"><a href="help.html#pickup" class="btn">Pickup details</a></p></div><div style="flex:1;"><div class="img" style="height:180px;">Games night photo</div></div></div><div class="anno">From the current Pick Up page. Venue differs between pages (Chatswood RSL, 446 Victoria Ave, 6-9pm vs The Chatswood Club, 11 Help St, 6:30-9pm): confirm with Dean. PlayCon pickups seen in order data can be added as an event pickup location.</div>', note="community + pickup")
ab += sec("Contact form", '<div class="row" style="gap:32px;align-items:flex-start;"><div style="flex:1.3;"><h2>Get in touch</h2><div class="grid g2" style="margin-top:12px;"><div class="field">Name</div><div class="field">Email</div></div><div class="field" style="margin-top:10px;">Order number (optional)</div><div class="field" style="margin-top:10px;height:90px;">Message (special orders welcome: tell us what you are looking for)</div><span class="btn solid" style="margin-top:10px;">Send message</span></div><div style="flex:1;" class="card small"><strong>Advent Games</strong><p class="muted" style="margin-top:6px;">Online store, Sydney NSW<br>dean@adventgames.com.au<br>0411 017 162<br>ABN 76 649 386 212</p><p style="margin-top:10px;">Can\'t find a game? We source games from around the world. Ask us.</p><p style="margin-top:10px;"><a href="help.html" style="text-decoration:underline;">Check our FAQ first</a></p></div></div><div class="anno">Contact details as published on the current FAQ &amp; Contact page. Special orders mention comes from "Can I order items not in the store?".</div>', note="native form + details column", sid="contact")
write("about.html", "About + Contact", "page.about.json", "", ab)

# ================================================================ HELP
hp = sec("Rich text", '<h1>Help &amp; FAQ</h1><p class="muted" style="margin-top:6px;">Shipping, pickup, preorders, returns and payments.</p>', note="page.help")
hp += sec("Quick links", ''.join(f'<span class="pill" style="margin-right:6px;">{x}</span>' for x in ["Shipping","Pickup","Preorders &amp; special orders","Orders","Returns &amp; damages","Payments","Our games"]), note="jump to anchors")
HELP = [
 ("Shipping", "shipping", ["How much is shipping? ($10 Sydney Metro, Gosford, Wollongong · $15 rest of Australia · free over $300)", "When will I receive my order? (dispatched in 1-3 business days, 2-7 if ordered from a supplier)", "Can I track my parcel?", "Do you ship overseas? (Australia only, email for a quote)", "What if I'm not home? (parcel lockers, uncollected parcels)"]),
 ("Pickup", "pickup", ["Can I pick up my order? (free, Tuesday nights, Northside Gamers Group, Chatswood)", "When will my pickup be ready?"]),
 ("Preorders &amp; special orders", "preorders", ["When is my preorder due?", "When am I charged? (at purchase)", "Will my in-stock items wait for my preorder?", "Can I cancel a preorder?", "Can you order a game you don't stock?"]),
 ("Orders", "orders", ["Do I need an account to buy?", "How do I check my order status?", "Can I add items to an order that hasn't shipped?"]),
 ("Returns &amp; damages", "returns", ["My parcel arrived damaged", "Can I return an unopened game? (7 days, exclusions apply)", "How do I start a return? (Return Product Number)"]),
 ("Payments", "payments", ["What payment methods do you accept?", "How does bank transfer work?"]),
 ("Our games", "games", [("How is a game's Complexity rating determined?", "Complexity ratings on product pages are taken from data on Board Game Geek, the hobby's main repository of discussion and knowledge. Games are given a rating out of 5, with 1 being extremely light, easy-to-learn and for nearly all ages, and 5 being highly complex, with possibly obtuse rules. These ratings are user submitted, so they are very subjective and change over time as more people vote, but are an excellent indicator of how complex you're likely to find a game to be."), "Which edition is this game? (English retail unless tagged German, KS or Deluxe)", "Why are board games expensive in Australia?"]),
]
for t, a, qs in HELP:
    hp += sec("FAQ", f'<h2>{t}</h2>' + "".join((f'<div class="acc-open small"><div class="row" style="justify-content:space-between;font-weight:600;"><span>{q[0]}</span><span>–</span></div><div class="acc-body"><p>{q[1]}</p></div></div>' if isinstance(q, tuple) else f'<div class="acc small"><span>{q}</span><span>+</span></div>') for q in qs), note=t, sid=a)
hp += sec("Image banner", '<div class="img" style="height:120px;flex-direction:column;text-transform:none;letter-spacing:0;color:#333;"><h3>Still stuck?</h3><a href="about.html#contact" class="btn" style="margin-top:8px;">Contact Dean</a></div>', note="contact CTA")
hp += '<div class="sec internal"><div class="anno">Questions are the current FAQ &amp; Contact, Shipping, Pick Up, Pre-Orders, Returns and Payment Options pages regrouped (bracketed text = the gist of today\'s answer). Answers live in one shared FAQ so the product page accordions and the cart pull the same copy. Full policies (Shipping, Returns, Pre-orders &amp; special orders, Payments, Privacy, Terms) stay as default policy pages. The old "Video review credits" page can go: credits sit under each video instead.</div></div>'
write("help.html", "Help & FAQ", "page.help.json", "", hp)

# ================================================================ BLOG
POSTS = [('Reviews', 'Five great two-player games under $50', '21 Sep 2026'), ('Store news', 'Our new website is live', '2 Sep 2026'), ('New releases', 'The big preorders landing before Christmas', '28 Aug 2026'), ('Reviews', 'Gateway games for a family games night', '14 Aug 2026'), ('New releases', "GMT's autumn P500 list, explained", '1 Aug 2026'), ('Store news', 'Pickup is changing for the holidays', '20 Jul 2026')]
def post_card(tg, t, d):
    return f'<a href="article.html"><div class="img" style="height:170px;">Image</div><p class="small" style="margin-top:8px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;font-size:10.5px;">{tg}</p><h3 style="margin-top:2px;">{t}</h3><p class="small muted" style="margin-top:4px;">{d}</p></a>'
bl = sec("Blog posts (main blog)", '<h1 class="center">News &amp; reviews</h1><p class="center muted" style="max-width:640px;margin:8px auto 0;">' + L1 + '</p>'
    + '<div class="row small center" style="gap:16px;justify-content:center;margin-top:14px;"><span>Share:</span><span class="muted">X · Facebook · Pinterest</span></div>'
    + '<div class="row small" style="gap:18px;justify-content:center;margin-top:12px;"><strong style="text-decoration:underline;">All</strong><span>New releases</span><span>Reviews</span><span>Store news</span></div>'
    + '<a href="article.html" class="row" style="gap:0;margin-top:22px;border:1px solid var(--line);border-radius:8px;overflow:hidden;align-items:stretch;"><div class="img" style="flex:1;height:300px;border:none;">Featured image</div><div style="flex:1;padding:32px;display:flex;flex-direction:column;justify-content:center;"><p class="small" style="font-weight:600;letter-spacing:.06em;text-transform:uppercase;font-size:10.5px;">New releases</p><h2 style="margin-top:4px;">Essen 2026: the games we\'re most excited to stock</h2><p class="muted small" style="margin-top:8px;">' + L1 + '</p><p class="small muted" style="margin-top:10px;">3 Oct 2026</p></div></a>'
    + '<div class="grid g3" style="margin-top:22px;gap:22px;">' + "".join(post_card(*p) for p in POSTS) + '</div><p class="center small" style="margin-top:20px;">‹ 1 <strong>2</strong> 3 ›</p>'
    + '<div class="anno"><strong>Enterprise main blog, as is.</strong> Centred title and blog description, share links, tag links (All plus each article tag), latest post as a wide featured card (image beside text), then a 3-column grid of cards: image, tag, title, date. Pagination below. Nothing custom: Dean just tags posts (New releases / Reviews / Store news) and the tag links appear. Mobile stacks to one column.</div>', note="blog.json · Enterprise main blog, no changes")
bl += sec("Media with text", '<div class="row" style="gap:32px;align-items:center;"><div style="flex:1;"><div class="img" style="height:180px;">Image</div></div><div style="flex:1;"><h2>Need a hand choosing?</h2><p class="muted" style="margin-top:8px;">' + L1 + '</p><p style="margin-top:12px;"><a href="help.html" class="btn">Ask Dean</a></p></div></div>', note="optional · same as Enterprise demo blog page")
write("blog.html", "Blog", "blog.json", "", bl)

art = sec("Article (main article)", f'''<div class="center" style="max-width:820px;margin:0 auto;"><p class="small" style="font-weight:600;letter-spacing:.06em;text-transform:uppercase;font-size:10.5px;">Reviews</p><h1 style="margin-top:6px;">Five great two-player games under $50</h1><p class="small muted" style="margin-top:8px;">21 Sep 2026</p></div>
    <div class="img" style="height:380px;margin-top:20px;">Hero image (full width)</div>
    <div style="max-width:620px;margin:24px auto 0;">
      <p>{L2}</p><h3 style="margin-top:18px;">1. Sky Team</h3><p class="muted" style="margin-top:6px;">{L1} <a href="product.html" style="text-decoration:underline;">Shop Sky Team</a></p>
      <div class="img" style="height:200px;margin-top:14px;">Inline image</div>
      <h3 style="margin-top:18px;">2. Jaipur</h3><p class="muted" style="margin-top:6px;">{L1} <a href="product.html" style="text-decoration:underline;">Shop Jaipur</a></p>
      <div class="row small" style="justify-content:space-between;margin-top:26px;padding-top:12px;border-top:1px solid var(--line);"><span>Share: X · Facebook · Pinterest</span><span>‹ Previous &nbsp; · &nbsp; 4 minute read &nbsp; · &nbsp; Next ›</span></div></div>
    <div class="anno"><strong>Enterprise main article, as is.</strong> Tag, centred title and date, full-width hero image, then a narrow reading column. Share links, previous / next and an automatic read time at the end. Products are linked inline from the body text, which needs nothing built. The author line is a theme setting (shown or hidden).</div>''', note="article.json · Enterprise main article, no changes")
art += sec("Featured collection", f'<h2>Games in this article</h2><div style="margin-top:12px;">{carousel([card("Sky Team","Le Scorpion Masqué","39.95",meta=""), card("Jaipur","Space Cowboys","29.95",meta=""), card("Patchwork","Lookout Spiele","34.95",meta=""), card("Lost Cities","KOSMOS","29.95",meta="")], 4)}</div><div class="anno"><strong>Optional, cut if the budget is tight.</strong> Enterprise has no "products in this article" block, so this is the theme\'s product carousel fed by {mf("article.featured_games","new")} (list of products picked per post) with a few lines of Liquid. Hides when empty. Without it, inline links in the body do the same job for free.</div>', note="optional · shoppable post", kind="tweak")
art += sec("Article comments", '<h3>Leave a comment</h3><p class="small muted" style="margin-top:4px;">Please note: comments must be approved before they are published.</p><div class="grid g2" style="margin-top:10px;gap:10px;"><div class="field">Name</div><div class="field">Email</div></div><div class="field" style="margin-top:10px;height:70px;">Comment</div><p style="margin-top:10px;"><span class="btn solid">Post comment</span></p><div class="anno">Native, only shows if comments are turned on for the blog in Shopify admin. Recommend off at launch (moderation load) unless Dean wants them.</div>', note="native · optional")
art += sec("Featured blog", '<div class="row" style="justify-content:space-between;align-items:end;"><h2>Related articles</h2><a href="blog.html" class="small" style="text-decoration:underline;">View all</a></div><div class="grid g3" style="margin-top:14px;gap:22px;">' + "".join(post_card(*p) for p in POSTS[:3]) + '</div>', note="Enterprise featured blog section")
art += sec("Image banner", '<div class="img" style="height:180px;flex-direction:column;text-transform:none;letter-spacing:0;color:#333;"><h2>Questions about an order?</h2><span class="btn" style="margin-top:10px;">Help &amp; FAQ</span></div>', note="as on the Enterprise demo article")
write("article.html", "Blog post", "article.json", "", art)


# ================================================================ MEGANAV
def navbar(key):
    return '<div class="row small" style="gap:22px;border-bottom:1px solid var(--line);padding-bottom:10px;margin-bottom:12px;">' + "".join(f'<a href="meganav.html#{k}"' + (' style="font-weight:700;text-decoration:underline;"' if k == key else ' style="color:#999;"') + f'>{l}{" ▾" if k not in ("brands",) else ""}</a>' for l, h, k in NAV) + '</div>'

MEGA_NOTE = {"column": "Enterprise Column mega menu", "button": "Enterprise Button mega menu", "sidebar": "Enterprise Sidebar mega menu", "dropdown": "Enterprise standard dropdown"}
def mega_wrap(key, label, kind, inner, why):
    return sec("Header: mega menu", navbar(key) + f'<div class="mega">{inner}</div><div class="anno"><strong>{MEGA_NOTE[kind]}.</strong> {why}</div>',
               note=f"{label} · {MEGA_NOTE[kind]}", sid=key, extra_tags=" " + tag(f"mega menu block: {kind}"))

def mega_column(key, label, cols, banners, why, images=True):
    im = '<div class="img" style="height:70px;margin-bottom:8px;">Image</div>' if images else ''
    c = "".join(f'<div class="small">{im}<p><strong>{h}</strong></p><p style="line-height:1.9;margin-top:4px;">' + "<br>".join(f'<a href="{u}">{t}</a>' for t, u in items) + f'</p><p style="margin-top:6px;"><a href="{items[0][1]}" style="text-decoration:underline;">Shop all &gt;</a></p></div>' for h, items in cols)
    bn = ('<div class="grid g3" style="gap:12px;margin-top:18px;">' + "".join(f'<div class="img" style="height:90px;flex-direction:column;align-items:flex-start;justify-content:flex-end;padding:12px;text-transform:none;letter-spacing:0;color:#333;"><strong>{t}</strong><span class="small muted">{s}</span></div>' for t, s in banners) + '</div>') if banners else ""
    return mega_wrap(key, label, "column", f'<div class="grid" style="grid-template-columns:repeat({len(cols)},minmax(0,1fr));gap:24px;">{c}</div>{bn}', why)

def mega_button(key, label, cards, why):
    c = "".join(f'<a href="{u}"><p class="small" style="font-weight:700;margin-bottom:6px;">{t} &gt;</p><div class="img" style="height:130px;">{img}</div></a>' for t, u, img in cards)
    return mega_wrap(key, label, "button", f'<div class="grid" style="grid-template-columns:repeat({len(cards)},minmax(0,1fr));gap:14px;">{c}</div>', why)

def mega_sidebar(key, label, groups, active, why):
    side = "".join(f'<div data-tab="{i}" class="row small{" on" if i == active else ""}" style="gap:10px;align-items:center;padding:8px 10px;border-radius:6px;"><div class="img" style="width:32px;height:32px;"> </div><span style="flex:1;">{g}</span><span>›</span></div>' for i, (g, _) in enumerate(groups))
    def tiles(ts): return "".join(f'<a href="{u}" style="position:relative;"><div class="img" style="height:110px;">Image</div>' + (f'<span class="badge" style="top:6px;left:6px;">{b}</span>' if b else "") + f'<p class="small" style="margin-top:6px;font-weight:600;">{n}</p></a>' for n, u, b in ts)
    panels = "".join(f'<div class="tabpanel" data-panel="{i}"{"" if i == active else " hidden"}><div class="grid g4" style="gap:14px;">{tiles(ts)}</div><p class="small" style="margin-top:14px;"><a href="collection.html" style="text-decoration:underline;">Shop all &gt;</a></p></div>' for i, (g, ts) in enumerate(groups))
    return mega_wrap(key, label, "sidebar", f'<div class="row" style="gap:24px;align-items:flex-start;"><div class="wf-tabs mega-side" style="width:240px;flex-shrink:0;border-right:1px solid var(--line);padding-right:16px;">{side}</div><div style="flex:1;min-width:0;">{panels}</div></div><p class="note" style="margin-top:8px;">Click the groups on the left to switch (hover on the live site).</p>', why)

C = "collection.html"; P = "collection-preorders.html"; R = "collection-rpg.html"; A = "collection-accessories.html"
mn_body = sec("Rich text", '<h1>Navigation + drawers</h1><p class="muted" style="margin-top:6px;max-width:680px;">Every top-level menu item shown open, plus the search, cart and mobile drawers. Each panel uses one of Enterprise\'s three built-in mega menu layouts (Column, Button, Sidebar), picked to suit the size of that menu. Hover opens a panel, clicking the top-level label goes to its parent collection.</p>'
    + '<div class="tblwrap" style="margin-top:12px;"><table class="tbl small"><tr><th>Menu item</th><th>Enterprise layout</th><th>Why</th></tr>'
    + "".join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in [
        ("Preorders", "Column + promo banners", "Two short link groups plus room for timely promos (due this month, Kickstarter)."),
        ("Just Arrived", "Standard dropdown", "Six plain links. No images, as Dean asked."),
        ("Board Games", "Sidebar", "The big catalogue: several groups with 8+ links each. Sidebar shows one group at a time instead of a wall of links."),
        ("Roleplaying", "Column", "RPG customers shop by system first. Systems grouped by genre, plus an all-RPGs link, beginner shortcuts and accessories, so the menu covers the whole category."),
        ("Accessories", "Column + promo banners", "Three small groups by job (protect, upgrade, play) plus sleeve finder and organiser promos."),
        ("Sale", "Standard dropdown", "Four links. Kept small on purpose."),
        ("Brands", "Plain link", "100+ brands go to the A-Z page.")]) + '</table></div>'
    + '<div class="anno">All three layouts are Enterprise header blocks: add a mega menu block, pick its layout and the top-level menu item it attaches to. Links come from the Shopify navigation menu; images, badges and promo banners are set in the block. Any menu item without a mega menu block falls back to Enterprise\'s standard dropdown.</div>', note="index of panels", internal=True)

mn_body += mega_column("preorders", "Preorders",
    [("Preorders", [("New to preorder", P), ("Coming soon", P), ("All preorders", P), ("Kickstarter", P)]), ("By type", [("Board games", P), ("Expansions", P), ("RPGs", P), ("Accessories", P)])],
    [("Due this month", "Big releases landing soon"), ("Kickstarter pledges", "Late pledges and retail editions"), ("How preorders work", "Pay today, ships on release")],
    "Dean's #2 browse path after Just Arrived. Column headings without images, link list and \"Shop all\", then a row of three promo banners (Enterprise's column layout supports these). Banners swapped monthly.", images=False)
mn_body += mega_wrap("arrived", "Just Arrived", "dropdown", '<div style="width:240px;" class="small"><p style="line-height:2;">' + "<br>".join(f'<a href="{P}#just-arrived">{x}</a>' for x in ["New board games", "New expansions", "New RPGs", "New accessories", "Back in stock", "Everything new"]) + '</p></div>',
    "A simple list, no images (Dean: hard to picture New expansions as an image). Enterprise standard dropdown, so no mega menu block needed. Each link is a tag-based smart collection fed by the arrival job.")
mn_body += mega_sidebar("board", "Board Games", [
    ("Game type", [(x, C, "") for x in ["Strategy", "Family", "Party", "Thematic", "Wargames", "Abstract", "Children's", "Card games"]]),
    ("Player count", [("Solo", C, ""), ("Two-player", C, ""), ("3-4 players", C, ""), ("Big groups (6+)", C, "")]),
    ("Rankings &amp; awards", [("Best sellers", C, ""), ("BGG Top 100", C, "Top 100"), ("Gateway games", C, ""), ("Spiel des Jahres", C, "Award"), ("Kinderspiel des Jahres", C, "Award"), ("Deutscher Spiele Preis", C, "Award"), ("International Gamers Award", C, "Award"), ("Meeple's Choice", C, "Award")]),
    ("LCGs &amp; miniatures", [("All Living Card Games", C, ""), ("Arkham Horror LCG", C, ""), ("Marvel Champions LCG", C, ""), ("The Lord of the Rings LCG", C, ""), ("All miniatures games", C, ""), ("Star Wars: Legion", C, ""), ("Star Wars: X-Wing", C, ""), ("Marvel: Crisis Protocol", C, "")]),
    ("Collections", [("Euro heavyweights", C, ""), ("Openers: light &amp; fun", C, ""), ("Hard to find", C, ""), ("Kickstarter", C, "")]),
    ("Expansions", [("All expansions", C, ""), ("New expansions", P + "#just-arrived", "New"), ("Expansions on preorder", P, "")]),
  ], 0,
    "Left list = second-level menu items with a thumbnail and chevron; hovering one swaps the image tiles on the right to its children. Types map to bgg.type, players to bgg.supports_players, awards to one Award winners collection filtered by award (tags set by Ben's script from the old category IDs), LCG and miniatures lines to bgg.families, the rest to smart rules (rank, weight) or tags, so every tile has real products behind it. Tile badges are set per tile in the block. Tile lists are placeholders: Dean to confirm which lines and awards to feature.")
mn_body += mega_column("rpg", "Roleplaying",
    [("Fantasy", [("Dungeons &amp; Dragons", R), ("Pathfinder", R), ("Daggerheart", R), ("The One Ring", R), ("Warhammer Fantasy", R)]),
     ("Sci-fi", [("Starfinder", R), ("Alien RPG", R), ("Cyberpunk RED", R), ("Star Wars RPG", R), ("Dune", R)]),
     ("Horror &amp; modern", [("Call of Cthulhu", R), ("Vampire: The Masquerade", R), ("Delta Green", R)]),
     ("Browse all", [("All roleplaying games", R), ("Starter sets", R), ("Core rulebooks", R), ("Solo RPGs", R), ("RPG preorders", P)]),
     ("RPG accessories", [("Dice", A), ("Miniatures", A), ("Maps &amp; tiles", A), ("GM screens", A)])],
    None,
    "Follows how Australian RPG retailers organise the category (Good Games, Gameology, Games Empire all lead with game system, Good Games groups systems by genre). Systems are the main way in, with \"All roleplaying games\" first in the Browse column so nothing in the range is hidden, beginner shortcuts across every system, and RPG accessories. \"Shop all\" under each column goes to the full Roleplaying collection with that genre or kind filtered. System names here are placeholders: the real list comes from Dean's range (rpg.system values, ordered by sales), and genre comes from the rpg_system metaobject so a new system lands in the right column.", images=False)
mn_body += mega_column("acc", "Accessories",
    [("Protect", [("Sleeves", A), ("Inserts &amp; organisers", A)]), ("Upgrade", [("Tokens &amp; scenery", A), ("Coins", A), ("Component upgrades", A)]), ("Play", [("Dice", A), ("Play mats", A)])],
    [("Card sleeves", "Every standard size in stock"), ("Organisers", "Tidy boxes, faster setup"), ("Dice", "Sets for every system")],
    "Grouped by job rather than a flat list of types. Coins and component upgrades need a product type before they can exist as collections (Dean's doc marks them with ?).")
mn_body += mega_wrap("sale", "Sale", "dropdown", '<div style="width:220px;" class="small"><p style="line-height:2;"><a href="collection.html">Weekly sale</a><br><a href="collection.html">Clearance</a><br><a href="collection.html">Dings &amp; dents</a><br><a href="collection.html">All sale</a></p></div>',
    "No mega menu block, so Enterprise shows its standard dropdown. Small on purpose: sale lives here and in one campaign banner, not spread across the site (brief: built to convert, not a discount store).")
mn_body += sec("Header", '<div class="row small" style="gap:22px;">' + "".join(f'<span{" style=\"font-weight:700;text-decoration:underline;\"" if k=="brands" else " style=\"color:#999;\""}>{l}{" ▾" if k!="brands" else ""}</span>' for l,h,k in NAV) + '</div><div class="anno">Brands is a plain link to the A-Z page (100+ brands is too many for a panel). Featured publisher logos live on the home page.</div>', note="Brands: direct link, no panel", sid="brands")

mn_body += sec("Predictive search", ent_predictive("wingsp", "|", [("Wingspan", "$79.95", "Stonemaier Games"), ("Wingspan: Asia", "$59.95", "Stonemaier Games"), ("Wingspan Organiser", "$39.95", "Folded Space")], [("", "an"), ("", "an asia"), ("", "an organiser")]) + '<div class="anno">Enterprise\'s native predictive search panel, opens under the header bar. Same layout as on the Search page wireframe. "View all results" at the bottom goes to the full results page with filters.</div>', note="Enterprise predictive search · native", sid="search-drawer")

mn_body += cart_drawer_sec()

mn_body += sec("Header: mobile menu", """<div style="max-width:340px;border:2px solid #555;padding:16px;">
    <div class="row" style="justify-content:space-between;"><strong>Menu</strong><span>✕</span></div>
    <div class="field" style="margin-top:10px;">Search games...</div>""" + "".join(f'<div class="acc small"><span>{l}</span><span>{">" if k!="brands" else ""}</span></div>' for l,h,k in NAV) + """
    <p class="small" style="margin-top:12px;line-height:1.9;">Account<br>Wishlist<br>Help &amp; FAQ<br>Track my order</p></div>
    <div class="anno">Drill-down drawer: each item opens its panel's links as a second level. Promo tiles are dropped on mobile.</div>""", note="mobile drawer", sid="mobile-menu")
write("meganav.html", "Navigation + drawers", "header group + drawers", "", mn_body)

# ================================================================ DATA MAP
Y = "●"
def frow(field, typ, card_, pdp_, filt, coll_, note):
    return f'<tr><td>{field}</td><td class="small">{typ}</td><td class="center">{card_}</td><td class="center">{pdp_}</td><td class="center">{filt}</td><td class="center">{coll_}</td><td class="small">{note}</td></tr>'

FIELDS = [
 ("Core Shopify", [
  (mf("title"), "native", Y, Y, "", "", "Strip '(PREORDER)' etc. already done"),
  (mf("vendor"), "native text", Y, Y, Y, Y, "Publisher filter + brand smart collections. Must match Brands sheet exactly"),
  (mf("product_type"), "native, closed list", "", "", Y, Y, "Drives top-level collections + Product type / Accessory type filter"),
  (mf("tags"), "native, state only", "badge", "badge", "Offers", Y, "sale, clearance, dings-dents, kickstarter, new-arrival, back-in-stock, gift-ideas"),
  (mf("price / compare at"), "native", Y, Y, "Price", "", "Compare at only on genuine sales, see gap 3"),
  (mf("media"), "native", Y, Y, "", "", "YouTube videos as product media, no field needed"),
 ]),
 ("advent.* (operational)", [
  (mf("advent.availability_state"), "single_line_text", Y, Y, Y, Y, "The master state. Add choice validation (gap 7)"),
  (mf("advent.eta"), "single_line_text", Y, Y, "", "", "Customer-facing 'November 2026'. Free text can't filter or sort"),
  (mf("advent.release_date"), "date", "", Y, "", "", "PDP preorder block. Could drive 'Coming soon' ordering via script"),
  (mf("advent.arrived_at"), "date", "", "", "", Y, "Drives Just Arrived membership + order (gap 8)"),
  (mf("advent.sleeve_size"), "single_line_text", Y, Y, Y, "", "Accessories. Normalise format ('63.5 x 88')"),
  (mf("advent.related_game"), "product_reference", Y, Y, "✕", "", "Change to list + text mirror (gap 2)"),
  (mf("advent.supplier_*"), "single_line_text ×4", "", "", "", "", "Admin only. Never rendered"),
  (mf("advent.ashop_category_ids"), "list.single_line_text", "", "", "", "", "Migration traceability only"),
 ]),
 ("bgg.* (game data)", [
  (mf("bgg.id"), "number_integer", "", Y, "", "", "Builds the 'View on BGG' attribution link"),
  (mf("bgg.type"), "list.single_line_text", "", Y, Y, Y, "Game type filter + Strategy/Family/Party... collections"),
  (mf("bgg.categories"), "list.metaobject_reference", "", Y, Y, "", "Pills link to filtered collection URL"),
  (mf("bgg.mechanics"), "list.metaobject_reference", "", Y, Y, "", "As above. Searchable filter list (tweak)"),
  (mf("bgg.designers"), "list.metaobject_reference", "", Y, Y, "", "As above"),
  (mf("bgg.artists"), "list.metaobject_reference", "", Y, Y, "", "As above"),
  (mf("bgg.families"), "list.single_line_text", "", Y, Y, "opt.", "Series row on PDP (optional)"),
  (mf("bgg.min_players / max_players"), "number_integer", Y, Y, "", "", "Card + PDP display '1-5'"),
  (mf("bgg.supports_players"), "list.single_line_text (derived)", "", "", Y, Y, "Players filter + Solo / Two-player collections"),
  (mf("bgg.min_playtime / max_playtime"), "number_integer", "", Y, "", "", "PDP display. Card uses the band (shorter)"),
  (mf("bgg.playtime_band"), "single_line_text (derived)", Y, "", Y, "", "Card + filter"),
  (mf("bgg.min_age"), "number_integer", Y, Y, "", "", "Display '12+'"),
  (mf("bgg.age_band"), "single_line_text (derived)", "", "", Y, "", "Filter"),
  (mf("bgg.weight"), "number_decimal", Y, Y, "", Y, "BGG's own score out of 5 (averageweight), pulled by Ben's import, no manual entry. Shown as '2.88 / 5' on the PDP. Gateway / Heavyweights collection rules"),
  (mf("bgg.weight_band"), "single_line_text (derived)", "", Y, Y, "", "Set by the import script from bgg.weight: 1.0-1.9, 2.0-2.9, 3.0-3.9, 4.0-5.0. Filter only, never shown as a word. Shopify can't filter a decimal as a range, so the slider ticks these bands"),
  (mf("bgg.rank / rating"), "number", "rating", Y, "via band", Y, "Rating chip on cards, both on PDP, BGG Top 100 rule. Rank drives the scripted 'BGG rank' sort (gap 9)"),
  (mf("bgg.year_published"), "number_integer", Y, Y, "skip", "", "Card badge row + PDP. No filter at launch"),
  (mf("bgg.is_expansion"), "boolean", "badge", Y, "toolbar", Y, "Expansion badge on cards, Games / Expansions / All switch, PDP notice"),
  (mf("bgg.expands"), "product_reference", "", Y, "", "", "'Requires base game' link on expansions"),
 ]),
 ("rpg.* and custom.*", [
  (mf("rpg.system"), "metaobject_reference", Y, Y, Y, Y, "RPG card line, filter, system collections"),
  (mf("rpg.product_kind"), "single_line_text", Y, Y, Y, Y, "Card line, filter"),
  (mf("custom.game_summary"), "single_line_text", "opt.", Y, "", "", "On the store but NOT in the import sheet (gap 6)"),
 ]),
 ("Native Shopify discovery fields", [
  (mf("…product_recommendation.complementary_products"), "list.product_reference", "", Y, "", "", "'You might also need...' slider in the buy box (expansions + sleeves/accessories), filled by script (gap 1)"),
  (mf("…product_recommendation.related_products"), "list.product_reference", "", Y, "", "", "Optional manual override of 'You might also like'"),
 ]),
]

ftable = '<div class="tblwrap"><table class="tbl"><tr><th>Field</th><th>Type</th><th>Card</th><th>PDP</th><th>Filter</th><th>Collection rule</th><th>Notes</th></tr>'
for grp, rows in FIELDS:
    ftable += f'<tr><th colspan="7" style="background:#e6e6e6;">{grp}</th></tr>' + "".join(frow(*r) for r in rows)
ftable += '</table></div>'

GAPS = [
 ("Must", "Expansions + accessories in 'You might also need...'", mf("shopify--discovery--product_recommendation.complementary_products") + " (native, script-filled)", "Enterprise's complementary products slider in the buy box replaces separate Expansions and Sleeves sections. Ben's script writes each base game's expansions (reverse of {}) and fitting accessories (from advent.related_game) into the native complementary products list. No bgg.expansions field needed.".format(mf("bgg.expands"))),
 ("Must", "Accessories that fit many games", mf("advent.related_game","fix") + " → list.product_reference<br>" + mf("advent.related_game_names","new") + " list.single_line_text", "Sleeves and organisers fit more than one game. Product references aren't a supported storefront filter type, so 'Made for' filtering needs a plain-text mirror. Script also pushes accessories into the game's native complementary_products."),
 ("Must", "RRP vs genuine sale price", mf("advent.rrp","new") + " number_decimal", "Ben already flagged it. Mapping RRP to compare-at puts a strike-through on nearly every product, which is the 'discount store' look we want to avoid. Recommend: RRP as a quiet line on the PDP only, compare-at reserved for real sales. Needs Dean's call."),
 ("Must", "At-supplier lead time", mf("advent.supplier_lead_time","new") + " single_line_text", "For 'ships in 2-7 business days'. Could be a single theme setting instead if lead time is the same for every supplier. Ask Dean."),
 ("Should", "Product-level operational notice", mf("advent.notice","new") + " single_line_text", "'Publisher delay: now expected Feb'. Shown in the PDP availability block and on the cart line. Matches the design doc's front-end messaging requirement without an app."),
 ("Should", "Game summary not in import", mf("custom.game_summary"), "Defined on the store, missing from the import sheet. Add the column (first sentence of description or BGG blurb) or delete the definition. Used as the PDP standfirst."),
 ("Should", "Clean availability filter", mf("advent.availability_state","fix") + " add choice validation", "Lock values to the 6 states so the filter never shows typos. Customer-facing labels mapped in the theme (state matrix on the preorder PDP). Hide the native in/out-of-stock filter, it treats preorders as 'in stock'."),
 ("Should", "Just Arrived / New to Preorder ordering", "script, no new field", "Collections can't sort by a metafield. The stock import job should reorder the manual Just Arrived collection by {} (and New to Preorder by created date). This is the exact issue Dean noted in his collection doc.".format(mf("advent.arrived_at"))),
 ("Should", "Sort by BGG rank (no app)", "script, no new field", "Shopify can't sort by a metafield, but every collection has a manual 'Featured' order. Ben's script sets that order by {} nightly (unranked last) via the collection reorder API, and the theme labels it 'BGG rank'. Filters keep the order. Limits: one custom order per collection, so rating and release date can't also be sorts; search results stay relevance-sorted; Shop All needs a real 'All games' collection; new products sit at the end until the next run.".format(mf("bgg.rank"))),
 ("Should", "Range-style filters (no app)", mf("bgg.rating_band","new") + " " + mf("bgg.rank_band","new") + " optional", "Search &amp; Discovery only returns lists (price is the only range). Theme tweak puts Meeplewatch-style Min/Max on players and stepped sliders on play time and complexity, ticking the band values behind the scenes. Ben's bands make this work. Add rating and rank bands if Dean wants those as filters. Free-value ranges need a filter app."),
 ("Info", "Long filter lists", "theme tweak", "Publisher, Designer, Artist, Mechanic will have hundreds of values. Enterprise has no in-filter search, so add a small type-ahead + max-height scroll (CSS/JS). Check the value cap Shopify returns per filter on the full 11k catalogue."),
 ("Optional", "Staff notes", mf("advent.staff_note","new") + " multi_line_text", "One or two lines from Dean on favourite games. Feeds the 'Staff recommendations' row on the home page and 'Why we like it' on the product page. Hides when empty."),
 ("Optional", "BGG ratings count", mf("bgg.num_ratings","new") + " number_integer", "'7,551 ratings' next to the rating on the product page (Meeplewatch). Gives the rating weight. From the same BGG pull (usersrated)."),
 ("Optional", "What's in the box", mf("advent.components","new") + " multi_line_text", "Component lists already sit in Dean's descriptions. Split into a field for its own product tab, or keep in the description under a heading."),
 ("Info", "Icon set", "theme snippet, no field", "Enterprise ships its own small set of filled icons (truck, return, map pin, chat; the same names as Dawn's icon picker), with nothing for players, play time, age or complexity. Use Phosphor Icons (MIT): users-three, clock, person, brain, star, calendar, trophy, pen-nib, puzzle-piece, play-circle, bell. Add them to the theme as one icon snippet (Fill or Regular weight to match Enterprise), no CDN. Keep Enterprise's own icons in its native sections."),
 ("Info", "Product videos", "no field (product media)", "Dean adds YouTube links as product media and types the label (How to play / Review / Playthrough) as alt text. A small custom section lists them below the fold and the top fold links to them."),
 ("Should", "Expected arrival filter", mf("advent.eta_month","new") + " date or single_line_text", "Powers the Expected arrival filter on Preorders. advent.eta is free text today ('2-7 business days' in the demo row), so it can't be filtered."),
 ("Should", "RPG genre for the menu", "rpg_system metaobject: new genre field", "Fantasy / Sci-fi / Horror &amp; modern columns in the Roleplaying mega menu. Set once per system."),
 ("Optional", "RPG setting", mf("rpg.setting","new") + " single_line_text or metaobject", "Dean lists Settings and Systems separately. Genre can reuse bgg.categories."),
 ("Optional", "Pack quantity", mf("advent.pack_quantity","new") + " number_integer", "Sleeve / dice / token counts on cards and PDP. Could stay in the title instead."),
 ("Optional", "Sleeves needed by a game", mf("advent.card_sleeves","new") + " list.single_line_text", "e.g. '63.5 x 88 ×170'. Powers 'Sleeves for this game' automatically. Nice to have, data-heavy."),
 ("Optional", "Shoppable blog posts", mf("article.featured_games","new") + " list.product_reference (article)", "'Games in this article' block."),
 ("Scope", "Item-level order status in account", "middleware + customer account UI extension", "Hosted customer accounts can't be themed. Needs an extension reading line statuses written by the middleware. Confirm it sits inside the $5,850 middleware line."),
 ("Scope", "Bookable pickup dates", "n/a", "Native local pickup is fine. Date/capacity booking is 'complex delivery logic', excluded."),
]
gtable = '<div class="tblwrap"><table class="tbl"><tr><th>#</th><th>Priority</th><th>What the wireframes need</th><th>Field / change</th><th>Why</th></tr>' + "".join(f'<tr><td>{i}</td><td><strong>{p}</strong></td><td>{w}</td><td class="small">{f}</td><td class="small">{y}</td></tr>' for i, (p, w, f, y) in enumerate(GAPS, 1)) + '</table></div>'

MOBJ = '''<div class="tblwrap"><table class="tbl"><tr><th>Metaobject</th><th>Fields on store</th><th>Used for</th><th>Recommendation</th></tr>
<tr><td>designer</td><td>name, bgg_id, description, image</td><td>Filter, PDP pills</td><td rowspan="4">Set <em>name</em> as display name (filter labels use it). Links go to filtered collection URLs, so no web pages needed at launch. Enabling metaobject web pages later gives designer bio pages for SEO.</td></tr>
<tr><td>artist</td><td>name, bgg_id, description, image</td><td>Filter, PDP pills</td></tr>
<tr><td>mechanic</td><td>name, bgg_id, description, image</td><td>Filter, PDP pills</td></tr>
<tr><td>game_category</td><td>name, bgg_id, description, image</td><td>Filter, PDP pills</td></tr>
<tr><td>rpg_system</td><td>name, publisher, bgg_id, description, image</td><td>Filter, RPG card line, system tiles</td><td>Image field doubles as the system tile logo. One smart collection per major system.</td></tr>
<tr><td><em>brand (not needed)</em></td><td></td><td>Brand pages</td><td>Use vendor smart collections (image = logo) created by script, rather than a Brand metaobject. Keeps vendor as the single source.</td></tr></table></div>'''

FILTER_ORDER = '<p class="small"><strong>Toolbar (Enterprise):</strong> Filter toggle · Sort by · list / grid view. <strong>Sort:</strong> BGG rank (Featured, renamed, default), Best selling, A-Z, Z-A, Price low/high, Date new/old. <strong>Sidebar order</strong> (applied filters group first):</p><ol class="small" style="line-height:1.9;margin:10px 0 0;padding-left:18px;">' + "".join(f"<li>{n} {s}</li>" for n, s, _, _ in SIDEBAR) + '</ol><p class="note" style="margin-top:6px;">18 filters in Search &amp; Discovery, inside the 25-filter limit. RPG and Accessories collections show their own subsets (system, product kind, sleeve size, made for).</p>'

TEMPLATES = '<div class="tblwrap"><table class="tbl"><tr><th>Template</th><th>Wireframe</th><th>Serves</th></tr>' + "".join(f'<tr><td>{t}</td><td><a href="{h}" style="text-decoration:underline;">{h}</a></td><td class="small">{s}</td></tr>' for t, h, s in [
 ("index", "index.html", "Home"), ("header group", "meganav.html", "Mega menu panels, search dropdown, cart drawer, mobile menu"), ("collection (default)", "collection.html", "Shop All, Board Games + sub-collections, Sale, Best Sellers, BGG Top 100"),
 ("collection.preorders", "collection-preorders.html", "Preorders, New to Preorder, Coming Soon, Just Arrived, Back in Stock"),
 ("collection.rpg", "collection-rpg.html", "Roleplaying + systems"), ("collection.accessories", "collection-accessories.html", "Accessories & Sleeves + types"),
 ("collection (vendor)", "brand.html", "100+ brand collections"), ("page.brands", "brands.html", "Brands A-Z"), ("search", "search.html", "Predictive + results"),
 ("product (one template for everything)", "product.html", "Board games, card games, expansions, RPGs and accessories. Conditional blocks: expansion note + base game link when bgg.is_expansion is true (see product-preorder.html); RPG strip when rpg.system is set (product-rpg.html); game details, BGG line and stats hidden when bgg.id is empty (product-accessory.html)"),
 ("cart", "cart.html", "Cart page + drawer"), ("customer accounts", "account.html", "Hosted, extension for item status"),
 ("page.wishlist", "wishlist.html", "Wishlist app page"), ("page.about", "about.html", "About + Contact"), ("page.help / page", "help.html", "Help & FAQ + legal pages"),
 ("blog", "blog.html", "News & reviews list"), ("article", "article.html", "Blog post")]) + '</table></div><p class="note" style="margin-top:6px;">15 templates plus checkout (hosted). Fits "up to 15 pages + Checkout".</p>'

dm = sec("Read me", f'''<h1>Data map: what the wireframes need from the data</h1>
    <p class="muted" style="margin-top:8px;max-width:820px;">For Jake and Ben. Every metafield in the import sheet (and on the dev store) mapped to where it displays, plus the gaps the layouts exposed. Built against the Enterprise theme by Clean Canvas, section names checked against its live demo.</p>
    <div class="grid g3" style="margin-top:16px;">
      <div class="card small"><strong>Theme: Enterprise ✓</strong><p class="muted" style="margin-top:4px;">Built for big catalogues: scoped search bar, sidebar filters with counts, mega menu with promos, promo tiles in grid, quick buy, pre-order, back-in-stock, stock counter, Product details section with stat highlights + spec tabs. Approx $420 USD (client cost). Fallback: Horizon (free, currently live on the store), weaker on big-catalogue browsing.</p></div>
      <div class="card small"><strong>Biggest data asks</strong><p class="muted" style="margin-top:4px;">1. Reverse expansion list on base games. 2. related_game as a list + filterable text mirror. 3. RRP decision. 4. Supplier lead time. 5. Product notice field.</p></div>
      <div class="card small"><strong>What's already right</strong><p class="muted" style="margin-top:4px;">Derived bands for filtering, metaobjects for designers / mechanics / categories, state tags kept separate from merchandising, closed product type list. These map cleanly onto native filters.</p></div>
    </div>''', note="start here")
dm += sec("1. Field usage", ftable + '<p class="note" style="margin-top:6px;">● = displayed / used. ✕ = can\'t be used as-is.</p>', note="every field in Ben's sheet")
dm += sec("2. Gaps and changes from the wireframes", gtable, note="for Ben's next import sheet version")
dm += sec("3. Metaobjects", MOBJ, note="5 on the dev store")
dm += sec("4. Filter set (Board Games)", FILTER_ORDER, note="Search & Discovery, in this order")
dm += sec("5. Templates", TEMPLATES, note="scope check")
dm += sec("6. Questions for Dean", '<ol class="small" style="line-height:1.9;margin:0;padding-left:18px;">' + "".join(f"<li>{q}</li>" for q in [
 "RRP: show strike-through 'was RRP' on everything, or a quiet RRP line on the product page with strike-through only for real sales?",
 "Preorders: charge at checkout or at release? Mixed orders held and shipped together by default?",
 "Is supplier lead time roughly the same for every supplier (one setting) or does it vary (per product)?",
 "Home hero: happy with fixed promo tiles instead of a rotating slideshow?",
 "Which 6-8 game-type tiles and which product carousels on the home page (Just Arrived, New to Preorder, Best Sellers, plus?)",
 "Range filters snap to bands (e.g. weight 2.0-2.9) rather than free values. OK, or worth a filter app?",
 "BGG rank as the default sort on collections, ahead of Newest? Rating and rank as filters too?",
 "Wishlist + back-in-stock app preference (one app can do both).",
 "Pickup: which Chatswood venue and time is current? (Pick Up page says Chatswood RSL 6-9pm, Shipping page says The Chatswood Club 6:30-9pm.) Is PlayCon a regular pickup point?",
 "Preorder ETAs: policy says dates appear 6-8 weeks before arrival, FAQ says 2-3 months. Which?",
 "Payments: keep bank transfer? Add Afterpay / Zip or Shop Pay instalments (not offered today)?",
 "'At supplier' is shown as In Stock on the current site. Happy to show it as its own state with a 2-7 day promise?",
 "When was Advent founded? (2013 is the footer copyright year.)",
 ]) + '</ol>', note="for the next design review")
CONTENT_NEEDED = [
 ("Staff recommendations", "home", "6-12 favourite games with a one-line note each (advent.staff_note)"),
 ("Why we like it", "product page", "optional staff notes on favourite products, same field"),
 ("New to board games? Start here", "home", "2-3 sentences for beginners and gift buyers, plus a photo"),
 ("Gift cards", "home", "short pitch and denominations; gift cards are native Shopify"),
 ("New to roleplaying?", "RPG collection", "2-3 sentences and the starter sets to feature"),
 ("How it started", "about", "the Advent story: when, why, how it has grown"),
 ("Collection intro / SEO copy", "main collections", "one short paragraph per main collection"),
 ("Help answers", "help", "confirm the regrouped FAQ answers and the open questions above"),
 ("Photography", "site-wide", "Dean, the shelves, games nights, a family playing, RPG table (no new imagery in scope, so supply or use stock)"),
]
dm += sec("7. Content needed from Dean", '<p class="small muted">Sections added because they help shoppers but have no content yet. They show lorem ipsum in the wireframes and are marked "content needed".</p><ol class="small" style="line-height:1.9;margin:10px 0 0;padding-left:18px;">' + "".join("<li><strong>" + a + "</strong> (" + b + "): " + c + "</li>" for a, b, c in CONTENT_NEEDED) + '</ol>', note="for the next client check-in")
write("data-map.html", "Data Map", "not a site page", "", dm)

print("built")
