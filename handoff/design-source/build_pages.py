# Advent Games collection and product page design drafts.
# Same design system, header, footer and product card as the home page (common.py).
import html
from common import *
import build_home
_hm = build_home.MAIN
BRAND_STORY = _hm[_hm.index('<!-- ============ BRAND STORY ============ -->'):_hm.index('<!-- ============ GOOGLE REVIEWS ============ -->')].replace('{tag', '{tag')

# ------------------------------------------------------------------ shared bits
def crumbs(*items):
    out = []
    for i, (label, href) in enumerate(items):
        if href:
            out.append(f'<a href="{href}">{label}</a>')
        else:
            out.append(f'<span aria-current="page">{label}</span>')
    return '<nav class="crumbs inner" aria-label="Breadcrumb">' + '<span aria-hidden="true">/</span>'.join(out) + '</nav>'

def banner(title, count, desc, note="Enterprise collection banner · title, product count and description · no image (Dean)"):
    return f'''<section class="coll-banner-wrap">{tag("Collection banner", "native", note)}
<div class="inner coll-banner"><h1>{title} <small>{count} products</small></h1><p>{desc}</p></div></section>'''

def chk(label, count="", checked=False):
    c = " checked" if checked else ""
    n = f"<em>{count}</em>" if count else ""
    return f'<label class="chk"><input type="checkbox"{c}> {label}{n}</label>'

def fgroup(title, body, open_=True, clear=False):
    o = " open" if open_ else ""
    cl = '<button class="fclear" type="button">Clear</button>' if clear else ""
    return f'<details class="fgroup"{o}><summary>{title}{I("chev",16)}</summary><div class="fbody">{body}{cl}</div></details>'

def flist(placeholder, items, checked=()):
    rows = "".join(chk(n, c, n in checked) for n, c in items)
    return f'<div class="fsearch">{I("search",14)}<input type="search" placeholder="{placeholder}" aria-label="{placeholder}"></div><div class="fscroll">{rows}</div>'

def slider(lo, hi, ticks):
    return (f'<div class="slider"><span class="bar"></span><span class="fill" style="left:{lo}%;right:{100-hi}%"></span>'
            f'<span class="knob" style="left:{lo}%"></span><span class="knob" style="left:{hi}%"></span></div>'
            f'<div class="ticks">{"".join(f"<span>{t}</span>" for t in ticks)}</div>')

def rng(a, b, pre=""):
    p = f'<span class="pre">{pre}</span>' if pre else ""
    return f'<div class="rng"><label>{p}<input value="{a}" aria-label="From"></label><span>to</span><label>{p}<input value="{b}" aria-label="To"></label></div>'

def applied(chips):
    if not chips:
        return ""
    cs = "".join(f'<button class="chip" type="button">{c} <span class="x" aria-hidden="true">×</span></button>' for c in chips)
    return fgroup(f"Applied filters ({len(chips)})", f'<div class="applied">{cs}</div><button class="fclear" type="button">Clear all</button>').replace('<details class="fgroup"', '<details class="fgroup fgroup--applied"', 1)

def filters_panel(groups, n_results):
    return f'''<aside class="filters" aria-label="Filters">
  <div class="fhead"><strong>Filter &amp; sort</strong><button type="button" class="js-drawer-close" aria-label="Close filters">×</button></div>
  {"".join(groups)}
  <div class="fshow"><button class="ag-btn ag-btn--primary ag-btn--block js-drawer-close" type="button">Show {n_results} results</button></div>
</aside>'''

def toolbar(n_results, n_applied, sort_default="Newest", per_page=True):
    sorts = ["Newest", "Best selling", "BGG rank", "Alphabetically, A-Z", "Alphabetically, Z-A", "Price, low to high", "Price, high to low"]
    so = "".join(f'<option{" selected" if s == sort_default else ""}>{s}</option>' for s in sorts)
    pp = ('<label class="tb-pp">Show <select aria-label="Products per page"><option>48</option><option>96</option><option selected>200</option></select></label>' if per_page else "")
    badge = f" <b>{n_applied}</b>" if n_applied else ""
    return f'''<div class="toolbar">
  <div class="tb-l"><button class="tb-filter js-filter" type="button" aria-expanded="true">{I("filter",16)} <span class="js-filter-label">Hide filters</span>{badge}</button><span class="tb-count">{n_results} products</span></div>
  <div class="tb-r">{pp}<label class="tb-sort"><span>Sort by</span><select aria-label="Sort by">{so}</select></label>
    <div class="tb-view" role="group" aria-label="View"><button type="button" class="js-view" data-view="grid" aria-pressed="true" aria-label="Grid view">{I("grid",18)}</button><button type="button" class="js-view" data-view="list" aria-pressed="false" aria-label="List view">{I("list",18)}</button></div>
  </div>
</div>'''

def prow(p):
    """List view row. p = dict(img,title,vendor,price,state,badge,exp,meta,line,rrp,eta,page)"""
    st = {"in": ("in", "In stock", ""), "sup": ("supplier", "At supplier", "Ships in 2-7 days"), "pre": ("preorder", "Preorder", ""),
          "soon": ("coming", "Coming soon", f"Expected {p.get('eta','')}"), "out": ("out", "Out of stock", "")}[p.get("state", "in")]
    btn = {"in": "Add to cart", "sup": "Add to cart", "pre": "Preorder now", "soon": "Preorder now", "out": "Notify me"}[p.get("state", "in")]
    bstyle = "secondary" if p.get("state") == "out" else "orange"
    exp = f'<span class="ag-badge ag-badge--expansion">{I("puzzle",12)}Expansion</span>' if p.get("exp") else ""
    if p.get("meta"):
        a, b, _, c = p["meta"]
        s = f'<span>{I("users",14)}{a}</span><span>{I("clock",14)}{b}</span><span>{I("mind",14)}{c}/5</span>'
    else:
        s = f'<span>{p.get("line","")}</span>'
    sub = f'<span class="v">{st[2]}</span>' if st[2] else ""
    link = p.get("link", "product.html")
    return f'''<div class="prow"><img src="img/{p["img"]}.jpg" alt="" loading="lazy"><div class="t"><a href="{link}">{p["title"]}</a>{exp}<span class="v">{p["vendor"]}</span></div>
<div class="s">{s}</div><div><span class="ag-avail ag-avail--{st[0]}">{st[1]}</span>{sub}</div><div class="p">${p["price"]}</div>
<button class="ag-btn ag-btn--{bstyle} ag-btn--sm ag-btn--block">{btn}</button></div>'''

def collection_body(items, promo, groups, n_results, applied_n, list_note=True, per_page=True, sort_default="Newest"):
    cards = [card(**{k: v for k, v in p.items() if k in ("img", "title", "vendor", "price", "state", "badge", "rrp", "meta", "eta", "exp", "line", "page", "link")}) for p in items]
    if promo:
        cards.insert(3, promo)
    rows = "".join(prow(p) for p in items)
    head = '<div class="plist-head"><span></span><span>Game</span><span>Players · time · complexity</span><span>Availability</span><span>Price</span><span></span></div>'
    return f'''<div class="inner">
{toolbar(n_results, applied_n, sort_default, per_page)}
<div class="coll js-coll">
  {filters_panel(groups, n_results)}
  <div class="coll-main">
    <div class="pgrid">{"".join(cards)}</div>
    <div class="plist">{head}{rows}</div>
    <nav class="paging" aria-label="Pages"><ol><li><span class="cur" aria-current="page">1</span></li><li><a href="#">2</a></li><li><a href="#">3</a></li><li><span class="gap">…</span></li><li><a href="#">12</a></li><li><a href="#" aria-label="Next page">{I("right",16)}</a></li></ol><p>Showing 1-200 of {n_results}</p></nav>
  </div>
  <div class="scrim js-drawer-close"></div>
</div>
</div>'''

PROMO_PRE = f'''<a class="promo-tile" href="collection-preorders.html"><span class="pt-art"><img src="img/euphoria-cutout.png" alt=""></span><span class="pt-copy"><span class="eyebrow">This month</span><span class="h3">New to preorder</span><span class="view-all">Reserve yours {I("right",14)}</span></span></a>'''

def recently_viewed(cards):
    return f'''<section class="sec">{tag("Featured collection", "native", "Enterprise recently viewed products · hides for first-time visitors")}
<div class="inner">{sec_head("Recently viewed")}{carousel(cards)}</div></section>'''

# ------------------------------------------------------------------ catalogue samples
G = lambda **k: k  # readability
BOARD = [
    G(img="old-kings-crown", title="The Old King's Crown", vendor="Eerie Idol Games", price="134.95", state="in", badge="Just arrived", meta=("1-4", "60-120 min", "12+", "3.2")),
    G(img="great-harbor", title="The Great Harbor", vendor="Archona Games", price="84.95", state="in", meta=("1-4", "60-90 min", "12+", "2.7")),
    G(img="abroad", title="Abroad", vendor="Allplay", price="109.95", state="in", badge="Just arrived", meta=("1-4", "90-120 min", "14+", "3.4")),
    G(img="power-grid", title="Power Grid (Recharged)", vendor="Rio Grande Games", price="84.95", state="sup", meta=("2-6", "120 min", "12+", "3.3")),
    G(img="gettysburg", title="Three Days of Gettysburg: Deluxe Edition", vendor="GMT Games", price="169.95", state="in", meta=("1-2", "2 hrs+", "14+", "3.7")),
    G(img="euphoria", title="Euphoria (Essential Edition)", vendor="Stonemaier Games", price="69.95", state="soon", badge="Coming soon", eta="Nov 2026", meta=("2-6", "60 min", "13+", "2.2")),
    G(img="king-of-tokyo", title="King of Tokyo (Second Edition)", vendor="IELLO", price="59.95", state="in", badge="Sale", rrp="70", meta=("2-6", "30 min", "8+", "1.5")),
    G(img="harmonies-crescendo", title="Harmonies: Crescendo", vendor="Libellud", price="26.95", state="in", badge="Back in stock", exp=True, meta=("1-4", "30-45 min", "10+", "2.0")),
    G(img="camel-up", title="Camel Up (Second Edition)", vendor="Pretzel Games", price="76.95", state="in", meta=("3-8", "30-45 min", "8+", "1.5")),
    G(img="pandemic", title="Pandemic", vendor="Z-Man Games", price="59.95", state="sup", meta=("2-4", "45 min", "8+", "2.4")),
    G(img="8-dragons", title="8 Dragons", vendor="Capstone Games", price="110.95", state="pre", badge="Preorder", meta=("1-4", "60-90 min", "14+", "3.0")),
    G(img="carcassonne", title="Carcassonne", vendor="Hans im Glück", price="58.95", state="in", meta=("2-5", "30-45 min", "7+", "1.9")),
    G(img="ravenloft", title="D&amp;D: Castle Ravenloft", vendor="Wizards of the Coast", price="99.95", state="out", meta=("1-5", "60 min", "12+", "2.4")),
    G(img="sushi-go-party", title="Sushi Go Party!", vendor="Gamewright", price="49.95", state="in", meta=("2-8", "20 min", "8+", "1.3")),
    G(img="1848", title="1848: The Springtime of Nations", vendor="Phalanx", price="118.95", state="pre", badge="Preorder", rrp="140", meta=("2-4", "120-180 min", "14+", "3.6")),
]
for p in BOARD:
    if p["img"] == "old-kings-crown":
        p["link"] = "product.html"

PREORDERS = [
    G(img="8-dragons", title="8 Dragons", vendor="Capstone Games", price="110.95", state="pre", badge="Preorder", meta=("1-4", "60-90 min", "14+", "3.0")),
    G(img="age-of-innovation", title="Age of Innovation: Future &amp; Past", vendor="Capstone Games", price="74.95", state="soon", badge="Coming soon", exp=True, eta="Nov 2026", meta=("1-5", "40-150 min", "14+", "3.9")),
    G(img="1848", title="1848: The Springtime of Nations", vendor="Phalanx", price="118.95", state="pre", badge="Preorder", rrp="140", meta=("2-4", "120-180 min", "14+", "3.6")),
    G(img="forest-shuffle-dartmoor", title="Forest Shuffle: Dartmoor - Exmoor", vendor="Lookout Spiele", price="29.95", state="soon", badge="Coming soon", exp=True, eta="Nov 2026", meta=("2-5", "40-60 min", "10+", "2.0")),
    G(img="aberration", title="Aberration", vendor="Deepwater Games", price="127.95", state="pre", badge="Preorder", meta=("1-4", "90-150 min", "14+", "3.3")),
    G(img="euphoria", title="Euphoria (Essential Edition)", vendor="Stonemaier Games", price="69.95", state="soon", badge="Coming soon", eta="Nov 2026", meta=("2-6", "60 min", "13+", "2.2")),
    G(img="arribada", title="Arribada", vendor="Devir Games", price="59.95", state="pre", badge="Preorder", meta=("2-4", "45-60 min", "10+", "2.2")),
    G(img="dorfromantik-south-seas", title="Dorfromantik: The South Seas", vendor="Pegasus Spiele", price="44.95", state="soon", badge="Coming soon", exp=True, eta="Dec 2026", meta=("1-6", "30-60 min", "8+", "1.6")),
    G(img="accuse", title="Accuse!", vendor="Hub Games", price="34.95", state="pre", badge="Preorder", meta=("3-6", "30 min", "10+", "1.6")),
    G(img="harmonies-pulse", title="Harmonies: Pulse", vendor="Libellud", price="29.95", state="soon", badge="Coming soon", exp=True, eta="Nov 2026", meta=("1-4", "30-45 min", "10+", "2.0")),
    G(img="courage", title="Courage: An Everdell Journeys Expansion", vendor="Starling Games", price="84.95", state="soon", badge="Coming soon", rrp="100", exp=True, eta="Feb 2027", meta=("1-4", "40-80 min", "10+", "2.4")),
    G(img="cairn-players-guide", title="Cairn: Player's Guide (Second Edition)", vendor="Yochai Gal", price="54.95", state="pre", badge="Preorder", line="Cairn · Core rulebook", page="product-rpg.html"),
]

RPG = [
    G(img="alien-core", title="ALIEN: The Roleplaying Game (Evolved Edition) Core Rulebook", vendor="Free League", price="84.95", state="in", badge="Just arrived", line="ALIEN · Core rulebook", link="product-rpg.html"),
    G(img="alien-starter", title="ALIEN: The Roleplaying Game (Evolved Edition) Starter Set", vendor="Free League", price="64.95", state="in", badge="Just arrived", line="ALIEN · Starter set", link="product-rpg.html"),
    G(img="blade-runner-core", title="Blade Runner: The Roleplaying Game Core Rulebook", vendor="Free League", price="74.95", state="in", line="Blade Runner · Core rulebook", link="product-rpg.html"),
    G(img="coc-starter", title="Call of Cthulhu Starter Set", vendor="Chaosium", price="39.95", state="sup", line="Call of Cthulhu · Starter set", link="product-rpg.html"),
    G(img="arkham-rpg-core", title="Arkham Horror: The Roleplaying Game Core Rulebook", vendor="Edge Studio", price="79.95", state="in", line="Arkham Horror RPG · Core rulebook", link="product-rpg.html"),
    G(img="avatar-legends-core", title="Avatar Legends: Core Rulebook", vendor="Magpie Games", price="74.95", state="in", line="Avatar Legends · Core rulebook", link="product-rpg.html"),
    G(img="alien-rapture", title="ALIEN: Rapture Protocol - Cinematic Adventure", vendor="Free League", price="54.95", state="pre", badge="Preorder", line="ALIEN · Adventure", link="product-rpg.html"),
    G(img="animal-adventures-starter", title="Animal Adventures: Starter Set", vendor="Steamforged Games", price="69.95", state="in", line="Animal Adventures · Starter set", link="product-rpg.html"),
    G(img="alien-screen", title="ALIEN: The Roleplaying Game (Evolved Edition) MU/TH/UR Screen", vendor="Free League", price="44.95", state="in", line="ALIEN · GM screen", link="product-rpg.html"),
    G(img="cairn-players-guide", title="Cairn: Player's Guide (Second Edition)", vendor="Yochai Gal", price="54.95", state="pre", badge="Preorder", line="Cairn · Core rulebook", link="product-rpg.html"),
    G(img="alien-stress-dice", title="ALIEN: The Roleplaying Game Stress Dice Set", vendor="Free League", price="24.95", state="in", line="ALIEN · Dice", link="product-rpg.html"),
]

ACCESSORIES = [
    G(img="clank-sleeves-dragon", title="Clank!: Card Sleeves - Dragon", vendor="Dire Wolf", price="17.95", state="in", line="63.5 x 88 mm · 100 sleeves · Made for Clank!", link="product-accessory.html"),
    G(img="arcs-playmat", title="Arcs: Playmat", vendor="Leder Games", price="54.95", state="in", line="Playmat · Made for Arcs", link="product-accessory.html"),
    G(img="dragon-d6-dice", title="Dragon D6 Dice Set", vendor="Chessex", price="14.95", state="in", line="Dice · 12 x D6", link="product-accessory.html"),
    G(img="arkham-sleeves-encounter", title="Arkham Horror: Premium Art Sleeves - Encounter", vendor="Fantasy Flight", price="19.95", state="sup", line="63.5 x 88 mm · 60 sleeves · Made for Arkham Horror LCG", link="product-accessory.html"),
    G(img="architects-coins", title="Architects of the West Kingdom: Metal Coins", vendor="Garphill Games", price="39.95", state="in", line="Coins · Made for Architects of the West Kingdom", link="product-accessory.html"),
    G(img="okc-sleeves", title="The Old King's Crown: Card Sleeve Pack", vendor="Eerie Idol Games", price="19.95", state="in", badge="Just arrived", line="63.5 x 88 mm · 110 sleeves · Made for The Old King's Crown", link="product-accessory.html"),
    G(img="cyberpunk-dice-tray", title="Cyberpunk 2077: Dice Tray Set", vendor="CMON", price="49.95", state="pre", badge="Preorder", line="Dice tray · Made for Cyberpunk 2077", link="product-accessory.html"),
    G(img="cozy-cat-sleeves", title="Cozy Cat Cafe: Card Sleeves Pack", vendor="Smirk &amp; Dagger", price="16.95", state="in", line="57 x 89 mm · 100 sleeves · Made for Cozy Cat Cafe", link="product-accessory.html"),
    G(img="dice-throne-sleeves", title="Dice Throne: Card Sleeves", vendor="Roxley", price="24.95", state="pre", badge="Preorder", line="63.5 x 88 mm · 120 sleeves · Made for Dice Throne", link="product-accessory.html"),
    G(img="compile-playmat", title="Compile: Playmat 1", vendor="Greater Than Games", price="34.95", state="out", line="Playmat · Made for Compile", link="product-accessory.html"),
    G(img="clank-sleeves-artifacts", title="Clank!: Card Sleeves - Artifacts", vendor="Dire Wolf", price="17.95", state="in", line="63.5 x 88 mm · 100 sleeves · Made for Clank!", link="product-accessory.html"),
]

RECENT = [card("great-harbor", "The Great Harbor", "Archona Games", "84.95", "in", meta=("1-4", "60-90 min", "12+", "2.7")),
          card("harmonies-crescendo", "Harmonies: Crescendo", "Libellud", "26.95", "in", exp=True, meta=("1-4", "30-45 min", "10+", "2.0")),
          card("camel-up", "Camel Up (Second Edition)", "Pretzel Games", "76.95", "in", meta=("3-8", "30-45 min", "8+", "1.5")),
          card("euphoria", "Euphoria (Essential Edition)", "Stonemaier Games", "69.95", "soon", "Coming soon", eta="Nov 2026", meta=("2-6", "60 min", "13+", "2.2")),
          card("power-grid", "Power Grid (Recharged)", "Rio Grande Games", "84.95", "sup", meta=("2-6", "120 min", "12+", "3.3"))]

# ------------------------------------------------------------------ filter groups
def avail_group(pre_split=False, checked=("In stock",), counts=("2,242", "137", "1,120")):
    rows = [("In stock", counts[0]), ("Preorder", counts[1]), ("Out of stock", counts[2])]
    if pre_split:
        rows = [("Preorder", "64"), ("Coming soon", "73")]
    return fgroup("Availability", "".join(chk(n, c, n in checked) for n, c in rows), clear=True)

def price_group(a="0", b="450"):
    return fgroup("Price", rng(a, b, "$") + slider(0, 100, ["$0", f"${b}"]))

BOARD_GROUPS = [
    applied(["Players: 2-4", "Complexity: 2-3.9", "In stock"]),
    avail_group(),
    price_group(),
    fgroup("Players", rng("2", "4") + '<div class="pchips" role="group" aria-label="Player count">' + "".join(f'<button type="button" aria-pressed="{"true" if n in ("2","3","4") else "false"}">{n}</button>' for n in ["1", "2", "3", "4", "5", "6+"]) + '</div>'),
    fgroup("Play time", slider(25, 75, ["&lt;30m", "30-60", "1-2h", "2h+"])),
    fgroup("Complexity", slider(25, 75, ["1", "2", "3", "4", "5"])),
    fgroup("Youngest player", '<select class="fselect" aria-label="Youngest player"><option>Any age</option><option>6 years</option><option selected>8 years</option><option>10 years</option><option>12 years</option><option>14 years</option></select>'),
    fgroup("Game type", "".join(chk(n, c) for n, c in [("Strategy", "1,204"), ("Family", "866"), ("Party", "212"), ("Thematic", "731"), ("Wargames", "402")]) + '<button class="fmore" type="button">Show more</button>'),
    fgroup("Product type", "".join(chk(n, c) for n, c in [("Board game", "1,684"), ("Expansion", "618"), ("Card game", "77")])),
    fgroup("Publisher", flist("Search publishers...", [("Abacusspiele", "12"), ("Allplay", "9"), ("Asmodee", "186"), ("Capstone Games", "14"), ("Compass Games", "22"), ("Feuerland", "11"), ("GMT Games", "214"), ("Lookout Spiele", "28"), ("Stonemaier Games", "31"), ("Zoch Verlag", "8")]), open_=False),
    fgroup("Category", flist("Search categories...", [("Adventure", "412"), ("Card Game", "390"), ("Economic", "288"), ("Fantasy", "604"), ("Historical", "351"), ("Horror", "97"), ("Science Fiction", "318")]), open_=False),
    fgroup("Mechanic", flist("Search mechanics...", [("Area Majority", "244"), ("Cooperative Game", "301"), ("Deck Building", "176"), ("Dice Rolling", "520"), ("Drafting", "231"), ("Hand Management", "610"), ("Worker Placement", "142")]), open_=False),
    fgroup("Designer", flist("Search designers...", [("Bruno Faidutti", "14"), ("Martin Wallace", "22"), ("Reiner Knizia", "61"), ("Stefan Feld", "19"), ("Uwe Rosenberg", "27"), ("Vital Lacerda", "9")]), open_=False),
    fgroup("Artist", flist("Search artists...", [("Beth Sobel", "18"), ("Ian O'Toole", "24"), ("Kwanchai Moriya", "21"), ("Vincent Dutrait", "33")]), open_=False),
    fgroup("Series", flist("Search series...", [("Carcassonne", "26"), ("Catan", "31"), ("Commands &amp; Colors", "18"), ("Pandemic", "14"), ("Ticket to Ride", "22")]), open_=False),
    fgroup("Offers", "".join(chk(n, c) for n, c in [("On sale", "48"), ("Clearance", "21"), ("Dings &amp; dents", "9"), ("Kickstarter", "16")]), open_=False),
]

# ------------------------------------------------------------------ collection pages
def page_collection():
    flag34 = '<div class="flag">' + I("chat", 16) + '<span><b>For Jake (#34, #35):</b> numbered pages, defaulting to 200 per page with a 48 / 96 / 200 picker (Dean\'s customers liked 200). The picker is a small tweak using alternate collection views; Shopify caps a page at 250. Default sort shown as Newest so new titles aren\'t buried; BGG rank stays in the list. Swap the default per collection if Dean prefers.</span></div>'
    main = (crumbs(("Home", "index.html"), ("Board Games", None))
            + banner("Board Games", "2,379", "Over 9,000 board games, from family classics to four-hour heavy euros. Use the filters to narrow by player count, play time and complexity, or jump into a game type.")
            + f'<section class="coll-sec">{tag("Collection products", "tweak", "Enterprise toolbar (filter toggle · sort · grid/list) · Search &amp; Discovery sidebar filters · promo tile in grid · numbered pages · range filters reuse Enterprise price-range UI over band filters (tweak) · per-page picker = tweak")}'
            + '<div class="inner">' + flag34 + '</div>'
            + collection_body(BOARD, PROMO_PRE, BOARD_GROUPS, "2,379", 3) + '</section>'
            + f'''<section class="sec">{tag("Rich text", "native", "SEO copy block below the grid · per collection, hidden when empty")}
<div class="inner"><div class="seo"><h2 class="h3">Board games in Australia, from Sydney</h2><p>Advent Games stocks over 9,000 board games, from quick family fillers to deep strategy games and hex-and-counter wargames. Every game is shipped from Sydney, boxed and padded, with flat-rate shipping and free delivery over $300.</p><p>Not sure where to start? Filter by player count and play time, or browse our <a href="#">Strategy</a>, <a href="#">Family</a> and <a href="#">Party</a> collections. <mark>[Dean to confirm copy]</mark></p></div></div></section>'''
            + recently_viewed(RECENT))
    render("collection.html", "Board Games · Advent Games", "Collection: Board Games", "collection.json · also used for Shop all, sub-collections, Sale, Best sellers, Award winners and brands", main, extra_js=PAGE_JS)

def page_preorders():
    groups = [applied([]), avail_group(pre_split=True, checked=()), price_group("0", "300"),
              fgroup("Product type", "".join(chk(n, c) for n, c in [("Board game", "71"), ("Expansion", "44"), ("Roleplaying", "14"), ("Accessory", "8")]))]
    steps = f'''<section>{tag("Rich text · 3 columns", "native", "how preorders work · same content as the Help page")}
<div class="inner"><div class="steps">
  <div class="step"><b>1</b><div><h3>Reserve your copy</h3><p>You're charged now, which locks in the price and your copy, even when the print run is small.</p></div></div>
  <div class="step"><b>2</b><div><h3>We track the release</h3><p><strong>Preorder</strong> means no date yet. <strong>Coming soon</strong> means the supplier has given us a date.</p></div></div>
  <div class="step"><b>3</b><div><h3>Shipped the day it lands</h3><p>Sent within one working day of arriving. Cancel any time before it leaves our supplier.</p></div></div>
</div></div></section>'''
    main = (crumbs(("Home", "index.html"), ("Preorders", None))
            + banner("Preorders", "137", "Reserve the big releases before they sell through. Preorders without a date yet, and Coming soon titles with a supplier date. Just Arrived uses this same layout, sorted by arrival date.", note="collection.preorders.json · Enterprise banner, no image · Just Arrived reuses this template")
            + steps
            + f'<section class="coll-sec">{tag("Collection products", "native", "Enterprise toolbar · short filter set: Availability (Preorder / Coming soon), Price, Product type · sorted Newest")}'
            + collection_body(PREORDERS, None, groups, "137", 0) + '</section>'
            + recently_viewed(RECENT))
    render("collection-preorders.html", "Preorders · Advent Games", "Collection: Preorders", "collection.preorders.json · also Just Arrived (sorted by arrival date)", main, extra_js=PAGE_JS)

def page_rpg():
    systems = [("alien-core", "ALIEN", "Free League · Sci-fi horror"), ("blade-runner-core", "Blade Runner", "Free League · Sci-fi noir"), ("arkham-rpg-core", "Arkham Horror RPG", "Edge Studio · Horror"),
               ("coc-starter", "Call of Cthulhu", "Chaosium · Horror"), ("avatar-legends-core", "Avatar Legends", "Magpie Games · Fantasy"), ("animal-adventures-starter", "Animal Adventures", "Steamforged · Family fantasy")]
    tiles = "".join(f'<a class="sys" href="#"><span class="im"><img src="img/{i}.jpg" alt="" loading="lazy"></span><strong>{n}</strong><span>{s}</span></a>' for i, n, s in systems)
    groups = [applied(["In stock"]), avail_group(counts=("388", "41", "96")), price_group("0", "200"),
              fgroup("RPG system", flist("Search systems...", [("ALIEN", "24"), ("Arkham Horror RPG", "11"), ("Avatar Legends", "9"), ("Blade Runner", "8"), ("Cairn", "4"), ("Call of Cthulhu", "38"), ("Dungeons &amp; Dragons", "64"), ("Pathfinder", "57")])),
              fgroup("Category", "".join(chk(n, c) for n, c in [("Core rulebook", "88"), ("Starter set", "31"), ("Adventure", "142"), ("Sourcebook", "96"), ("GM screen", "27"), ("Dice &amp; accessories", "66")])),
              fgroup("Setting", "".join(chk(n, c) for n, c in [("Fantasy", "214"), ("Sci-fi", "118"), ("Horror &amp; modern", "129")]))]
    main = (crumbs(("Home", "index.html"), ("Roleplaying", None))
            + banner("Roleplaying", "461", "Core rulebooks, starter sets, adventures and accessories for the systems we love, from ALIEN to Call of Cthulhu.", note="collection.rpg.json · Enterprise banner, no image")
            + f'''<section>{tag("Collection list", "native", "Shop by system · tiles use the RPG system record image (rpg.system) · 6 across, 3 on tablet")}
<div class="inner">{sec_head("Shop by system", link="#", link_label="All systems")}<div class="systems">{tiles}</div>
<div class="newrpg"><img src="img/alien-starter.jpg" alt=""><div><h2 class="h3">New to roleplaying?</h2><p>Starter sets have everything a first table needs: quick rules, pre-made characters, dice and an adventure to play tonight.</p></div><a class="ag-btn ag-btn--primary" href="#">Shop starter sets</a></div></div></section>'''
            + f'<section class="coll-sec">{tag("Collection products", "native", "Enterprise toolbar · RPG filter set: Availability, Price, RPG system, Category, Setting · cards show System · Category instead of play stats")}'
            + collection_body(RPG, None, groups, "461", 1) + '</section>'
            + recently_viewed(RECENT))
    render("collection-rpg.html", "Roleplaying · Advent Games", "Collection: Roleplaying", "collection.rpg.json", main, extra_js=PAGE_JS)

def page_accessories():
    groups = [applied(["In stock"]), avail_group(counts=("731", "52", "214")), price_group("0", "100"),
              fgroup("Accessory type", "".join(chk(n, c) for n, c in [("Card sleeves", "412"), ("Playmats", "96"), ("Dice &amp; dice trays", "188"), ("Coins &amp; tokens", "74"), ("Inserts &amp; organisers", "61"), ("Component upgrades", "53")])),
              fgroup("Sleeve size", "".join(chk(n, c) for n, c in [("44 x 68 mm (mini)", "31"), ("57 x 89 mm (standard US)", "48"), ("63.5 x 88 mm (standard)", "126"), ("70 x 120 mm (tarot)", "22"), ("80 x 120 mm (large)", "17")])),
              fgroup("Made for", flist("Search games...", [("Arkham Horror LCG", "14"), ("Arcs", "2"), ("Clank!", "6"), ("Dice Throne", "9"), ("The Old King's Crown", "4"), ("Wingspan", "7")]))]
    main = (crumbs(("Home", "index.html"), ("Accessories", None))
            + banner("Accessories", "884", "Sleeves, playmats, dice, coins and organisers to protect and upgrade your games.", note="collection.accessories.json · Enterprise banner, no image · sleeve finder removed")
            + f'<section class="coll-sec">{tag("Collection products", "native", "Enterprise toolbar · accessory filter set: Availability, Price, Accessory type, Sleeve size, Made for · cards show size · pack · Made for instead of play stats")}'
            + collection_body(ACCESSORIES, None, groups, "884", 1) + '</section>'
            + recently_viewed(RECENT))
    render("collection-accessories.html", "Accessories · Advent Games", "Collection: Accessories", "collection.accessories.json", main, extra_js=PAGE_JS)

# ------------------------------------------------------------------ product pages
STATES = {
    "in":   ("in", "In stock", "· dispatched in 1-3 business days", "Ready to ship from Sydney.", "Add to cart"),
    "sup":  ("supplier", "Available from supplier", "· ships in 2-7 business days", "We order it in as soon as you check out.", "Add to cart"),
    "pre":  ("preorder", "Preorder", "", "Charged now, shipped within one working day of release. Cancel any time before it leaves our supplier.", "Preorder now"),
    "soon": ("coming", "Coming soon", "· expected November 2026", "Charged now, shipped within one working day of release. Cancel any time before it leaves our supplier.", "Preorder now"),
    "out":  ("out", "Out of stock", "", "We'll email you as soon as it's back.", "Notify me"),
}

def availcards(default, notice=False):
    out = []
    for k, (cls, line, sub, txt, btn) in STATES.items():
        n = '<div class="notice"><b>Publisher update:</b> this wave has slipped two weeks. <mark>[optional notice]</mark></div>' if notice and k in ("pre", "soon") else ""
        out.append(f'<div class="availcard{" on" if k == default else ""}" data-state="{k}" data-btn="{btn}"><span class="ag-avail ag-avail--{cls}">{line} <span style="font-weight:400;color:var(--ink-muted)">{sub}</span></span><p>{txt}</p>{n}</div>')
    return "".join(out)

STATE_TOGGLE = ('<div class="wf-toggle" role="group" aria-label="Availability"><span class="wf-lbl">State:</span>'
                + "".join(f'<button type="button" data-state="{k}" aria-pressed="false">{v[1].replace("Available from supplier", "At supplier")}</button>' for k, v in STATES.items()) + '</div>')

def gallery(imgs, video_img=None):
    thumbs = "".join(f'<button type="button" class="js-thumb" data-src="img/{i}.jpg" aria-current="{"true" if n == 0 else "false"}" aria-label="Image {n+1}"><img src="img/{i}.jpg" alt=""></button>' for n, i in enumerate(imgs))
    if video_img:
        thumbs += f'<button type="button" class="vid" aria-label="Play How to play video"><img src="img/{video_img}.jpg" alt="">{I("playf",24)}</button>'
    return f'''<div class="gallery"><div class="g-thumbs">{thumbs}</div><div class="g-main"><img class="js-main" src="img/{imgs[0]}.jpg" alt=""><span class="g-zoom" aria-hidden="true">{I("search",18)}</span></div></div>'''

def comp(items):
    rows = "".join(f'<div class="comp-item"><img src="img/{i}.jpg" alt=""><div><b>{t}</b><span>${p}</span></div><button class="ag-btn ag-btn--secondary ag-btn--sm">Add</button></div>' for i, t, p in items)
    return f'''<div class="comp"><div class="comp-head"><strong>You might also need...</strong><div class="comp-nav"><button type="button" class="js-comp-prev" aria-label="Previous">{I("left",14)}</button><button type="button" class="js-comp-next" aria-label="Next">{I("right",14)}</button></div></div><div class="comp-track js-comp">{rows}</div></div>'''

DELIVERY = f'''<div class="delivery">
  <div>{I("truck",18)}<span><b>$10</b> Sydney Metro, Gosford &amp; Wollongong · <b>$15</b> rest of Australia · <b>Free over $300</b></span></div>
  <div>{I("map",18)}<span>Free pickup in Chatswood, Tuesday nights <mark>[Dean to confirm venue]</mark></span></div>
</div>'''

POLICIES = f'''<div class="acc">
  <details><summary>Delivery &amp; pickup {I("chev",18)}</summary><div class="ab"><p>We ship Australia-wide with Australia Post eParcel, tracked. Games are boxed and padded; small items may go in a satchel.</p><p>In-stock games are dispatched in 1-3 business days. Games we order in from our supplier ship in 2-7 business days. Mixed orders are held and shipped together unless you ask us to split.</p></div></details>
  <details><summary>Returns &amp; damaged games {I("chev",18)}</summary><div class="ab"><p><b>Change of mind:</b> let us know in writing within 7 days of delivery. The game must be unopened and in its original packaging.</p><p><b>Arrived damaged?</b> Email us and we'll replace it, or give you a credit or refund. <a href="#">Full returns policy</a></p></div></details>
</div>'''

PAY = '<div class="paylogos">Pay by card, PayPal, Apple Pay or Google Pay</div>'

FAQ_LIST = f'''<div class="faq">{sec_head("Questions about buying from Advent")}<div class="acc">
  <details><summary>When will my order ship? {I("chev",18)}</summary><div class="ab"><p>In-stock games ship in 1-3 business days. Supplier items ship in 2-7 business days. Preorders ship within one working day of release.</p></div></details>
  <details><summary>Can I mix preorders and in-stock games in one order? {I("chev",18)}</summary><div class="ab"><p>Yes. We hold the order and ship it together when everything has arrived, unless you ask us to split it.</p></div></details>
  <details><summary>Do you price match? {I("chev",18)}</summary><div class="ab"><p><mark>[Dean to write]</mark></p></div></details>
  <details><summary>Can I pick up instead? {I("chev",18)}</summary><div class="ab"><p>Free pickup in Chatswood on Tuesday nights. Choose pickup at checkout.</p></div></details>
</div></div>'''

def pdp(cfg):
    badges = "".join(cfg.get("badges", []))
    stats = ""
    if cfg.get("stats"):
        stats = '<div class="statbox">' + "".join(f'<div>{I(ic,20)}<span>{lab}</span><strong>{val}</strong></div>' for ic, lab, val in cfg["stats"]) + '</div>'
    tags = ""
    for lab, items in cfg.get("tags", []):
        tags += f'<div class="tagrow"><b>{lab}:</b>' + "".join(f'<a class="pill" href="collection.html">{x}</a>' for x in items) + '</div>'
    summary = f'<p class="summary">{cfg["summary"]}</p>' if cfg.get("summary") else ""
    exp = cfg.get("expnote", "")
    rrp = cfg.get("rrp")
    rrph = f'<span class="rrp"><s>RRP ${rrp}</s> <span class="save">You save ${cfg["save"]}</span></span>' if rrp else ""
    compo = comp(cfg["comp"]) if cfg.get("comp") else ""
    bggline = cfg.get("bggline", "")
    specs = "".join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in cfg["specs"])
    tab2 = cfg.get("tab2", "Game details")
    videos = cfg.get("videos")
    vid_sec = ""
    if videos:
        vs = "".join(f'<a class="video" href="#"><span class="vthumb"><img src="img/{i}.jpg" alt="" loading="lazy"><span class="play">{I("playf",22)}</span></span><strong>{t}</strong><span>{c}</span></a>' for i, t, c in videos)
        vid_sec = f'''<section class="sec" id="videos">{tag("Custom section · Product videos", "custom", "only when the product has video media · label = video alt text · channel name under each")}
<div class="inner">{sec_head("Watch before you buy")}<div class="videos">{vs}</div></div></section>'''
    why = ""
    if cfg.get("why"):
        why = f'''<div class="why"><span class="who"><img src="img/advent-logo.png" alt=""></span><div><span class="eyebrow">Why we like it</span><blockquote>{cfg["why"]}</blockquote><footer>Dean, Advent Games</footer></div></div>'''
    note_faq = f'''<section class="sec">{tag("Custom section · staff note + FAQ", "custom", "one section, two halves: advent.staff_note on the left (hidden when empty, FAQ then sits on its own) · FAQ blocks on the right, shared content across product pages")}
<div class="inner"><div class="why-faq{"" if why else " why-faq--solo"}">{why}{FAQ_LIST}</div></div></section>'''
    rows = "".join(f'<section class="sec{" band" if n == 0 else ""}">{tag(t1, "native", t2)}<div class="inner">{sec_head(h, sub, "#" if link else "", "View all")}{carousel(cs)}</div></section>' for n, (t1, t2, h, sub, link, cs) in enumerate(cfg.get("rows", [])))
    default = cfg.get("state", "in")
    btn = STATES[default][4]
    notice = cfg.get("notice", True)
    flags = "".join(f'<div class="flag">{I("chat",16)}<span>{f}</span></div>' for f in cfg.get("flags", []))
    main = (crumbs(*cfg["crumbs"])
            + f'''<section class="pdp-sec">{tag("Main product", "tweak", "Enterprise main product · block order: title, BGG line, price and buy button high (mobile scroll), then stats, tags and summary · BGG line, stats strip and availability card = Custom Liquid blocks fed by metafields · complementary products block · policy accordions · use the State switch in the top bar to see each availability")}
<div class="inner pdp">
  {gallery(cfg["gallery"], cfg.get("video_thumb"))}
  <div class="buy">
    <div class="buy-badges">{badges}</div>
    <a class="buy-vendor" href="#">{cfg["vendor"]}</a>
    <h1>{cfg["title"]}</h1>
    {bggline}
    {exp}
    <div class="pricebox"><span class="now">${cfg["price"]}</span>{rrph}{PAY}</div>
    {availcards(default, notice)}
    <div class="buyrow js-buyrow"><div class="qty"><button type="button" aria-label="Decrease quantity">−</button><input value="1" aria-label="Quantity"><button type="button" aria-label="Increase quantity">+</button></div><button class="ag-btn ag-btn--orange js-buybtn">{btn}</button><button class="wish" type="button" aria-label="Add to wishlist">{I("heart",20)}</button></div>
    <div class="notifyrow js-notify"><input class="ag-input" type="email" placeholder="Email address" aria-label="Email address"><button class="ag-btn ag-btn--primary">Notify me</button></div>
    {stats}
    {tags}
    {summary}
    {compo}
    {DELIVERY}
    <div class="jumps">{('<a href="#videos">' + I("play",16) + ' Watch how to play</a>') if videos else ""}<a href="#details">{I("chev",14)} Full {tab2.lower()}</a></div>
    {POLICIES}
    {flags}
  </div>
</div></section>
<section class="sec" id="details">{tag("Product details", "tweak", "tabs · moved above the videos so the description sits under the buy box (#43) · spec rows via Custom Liquid, rows hide when empty · Reviews tab dropped for launch (#42), returns if Dean adds a reviews app")}
<div class="inner">
  <div class="tabs" role="tablist"><button role="tab" aria-selected="true" data-tab="0" class="js-tab">Description</button><button role="tab" aria-selected="false" data-tab="1" class="js-tab">{tab2}</button></div>
  <div class="tabpanel on" data-panel="0"><div class="desc clamped js-desc">{cfg["desc"]}</div><button class="showmore js-more" type="button">Show more</button></div>
  <div class="tabpanel" data-panel="1"><dl class="specs">{specs}</dl></div>
</div></section>
''' + vid_sec + note_faq + rows + BRAND_STORY + recently_viewed(RECENT))
    return main

def badge(k, label):
    if k == "expansion":
        return f'<span class="ag-badge ag-badge--expansion">{I("puzzle",12)}Expansion</span>'
    return f'<span class="ag-badge ag-badge--{k}">{label}</span>'

def rating(r, n, rank):
    return f'<span class="ag-rating bgg-{int(float(r))}">{star()} {r}</span><span>{n} ratings</span><i>·</i><span>Rank #{rank}</span>'

OKC_DESC = '''<p>The old king is dying, and the great houses of the realm are fighting over who takes the crown. Each player leads a house with its own deck, bidding for Kingdom cards and sending their herald into battles across three regions of the board.</p>
<p>Every round you play cards from your hand to win battles and claim the kingdom's prizes, but every card you commit is worn down by attrition, so your hand shrinks as the game goes on. Gather lore to add stronger cards to your deck, read what your rivals are holding back, and time your big plays for the battles that matter.</p>
<p>Designed and illustrated by Pablo Clark, The Old King's Crown plays with 1-4 players, including a solo mode, in 60-120 minutes.</p>
<p><mark>[publisher description from the product import]</mark></p>'''

OKC_SPECS = [("Designer", '<a href="#">Pablo Clark</a>'), ("Artist", '<a href="#">Pablo Clark</a>'), ("Publisher", '<a href="#">Eerie Idol Games</a>'), ("Game type", '<a href="#">Strategy</a>'),
             ("Categories", '<a href="#">Card Game</a> <a href="#">Fantasy</a> <a href="#">Medieval</a>'), ("Mechanics", '<a href="#">Hand Management</a> <a href="#">Card Play Conflict Resolution</a> <a href="#">Variable Player Powers</a>'),
             ("Series", '<a href="#">The Old King\'s Crown</a>'), ("Players", "1-4"), ("Play time", "60-120 min"), ("Age", "12+"), ("Complexity", "3.2 / 5"), ("Year published", "2025"),
             ("BoardGameGeek", f'{rating("8.1","1,284","1,102")} <a href="https://boardgamegeek.com">View on BGG</a> <mark>[BGG figures illustrative]</mark>'), ("Barcode", "<mark>[from import]</mark>")]

ADDONS = [card("okc-wild-kingdom", "The Old King's Crown: Wild Kingdom", "Eerie Idol Games", "64.95", "pre", "Preorder", exp=True, meta=("1-4", "60-120 min", "12+", "3.2")),
          card("okc-sleeves", "The Old King's Crown: Card Sleeve Pack", "Eerie Idol Games", "19.95", "in", line="63.5 x 88 mm · 110 sleeves · Made for The Old King's Crown", page="product-accessory.html"),
          card("okc-player-marker", "The Old King's Crown: Active Player Marker", "Eerie Idol Games", "14.95", "in", line="Component upgrade · Made for The Old King's Crown", page="product-accessory.html"),
          card("okc-art-prints", "The Old King's Crown: Art Print Pack", "Eerie Idol Games", "29.95", "in", line="Art prints · Made for The Old King's Crown", page="product-accessory.html")]

RELATED = [card("great-harbor", "The Great Harbor", "Archona Games", "84.95", "in", meta=("1-4", "60-90 min", "12+", "2.7")),
           card("abroad", "Abroad", "Allplay", "109.95", "in", "Just arrived", meta=("1-4", "90-120 min", "14+", "3.4")),
           card("power-grid", "Power Grid (Recharged)", "Rio Grande Games", "84.95", "sup", meta=("2-6", "120 min", "12+", "3.3")),
           card("aberration", "Aberration", "Deepwater Games", "127.95", "pre", "Preorder", meta=("1-4", "90-150 min", "14+", "3.3")),
           card("1848", "1848: The Springtime of Nations", "Phalanx", "118.95", "pre", "Preorder", rrp="140", meta=("2-4", "120-180 min", "14+", "3.6"))]

def page_product():
    cfg = dict(
        crumbs=[("Home", "index.html"), ("Board Games", "collection.html"), ("The Old King's Crown", None)],
        gallery=["okc-3", "okc-1", "okc-2"], video_thumb="okc-2",
        badges=[badge("new", "Just arrived")], vendor="Eerie Idol Games", title="The Old King's Crown",
        bggline=f'<div class="bggline"><span>2025</span><i>·</i>{rating("8.1", "1,284", "1,102")}<i>·</i><span>Designed by <a href="#">Pablo Clark</a></span> <mark>[BGG figures illustrative]</mark></div>',
        stats=[("users", "Players", "1-4"), ("clock", "Play time", "60-120 min"), ("person", "Age", "12+"), ("mind", "Complexity", "3.2 / 5")],
        tags=[("Categories", ["Card Game", "Fantasy", "Medieval"]), ("Mechanics", ["Hand Management", "Card Play Conflict Resolution", "Variable Player Powers"])],
        summary="Lead a great house in the fight for a dying king's crown. Bid, bluff and battle across three regions with a hand that wears down every round.",
        price="134.95", rrp="150", save="15.05",
        comp=[("okc-wild-kingdom", "The Old King's Crown: Wild Kingdom (expansion)", "64.95"), ("okc-sleeves", "The Old King's Crown: Card Sleeve Pack", "19.95"), ("okc-player-marker", "Active Player Marker", "14.95")],
        desc=OKC_DESC, specs=OKC_SPECS,
        videos=[("okc-2", "How to play", "Watch It Played"), ("okc-1", "Review", "Shut Up &amp; Sit Down"), ("okc-3", "Playthrough", "Rahdo Runs Through")],
        why="A card battler where every card you play costs you something later. Tense, sharp and gorgeous on the table. Our pick for a night with the regulars. <mark>[Dean to write]</mark>",
        rows=[("Featured collection", "Expansions and accessories for this game, full width (#47) · fed by the same complementary products list as the buy box slider · hidden when empty", "Expansions and accessories for this game", "Everything that works with The Old King's Crown.", "", ADDONS),
              ("Product recommendations", "Shopify related products (automatic) · Dean can override per product with Search &amp; Discovery (#48)", "You might also like", "", "", RELATED)],
        flags=["<b>For Jake:</b> \"You might also need...\" stays in the buy box (where people decide), and the full-width row further down is added as well (#47). Dean's BugHerd ask for a full-width row is covered without losing the in-buy-box upsell."],
    )
    render("product.html", "The Old King's Crown · Advent Games", "Product: Board game", "product.json · one template for board games, expansions, RPGs and accessories · blocks show or hide from the data", pdp(cfg), STATE_TOGGLE, PAGE_JS + PDP_JS)

def page_expansion():
    more = [card("okc-sleeves", "The Old King's Crown: Card Sleeve Pack", "Eerie Idol Games", "19.95", "in", line="63.5 x 88 mm · 110 sleeves", page="product-accessory.html"),
            card("okc-player-marker", "The Old King's Crown: Active Player Marker", "Eerie Idol Games", "14.95", "in", line="Component upgrade", page="product-accessory.html"),
            card("okc-art-prints", "The Old King's Crown: Art Print Pack", "Eerie Idol Games", "29.95", "in", line="Art prints", page="product-accessory.html"),
            card("old-kings-crown", "The Old King's Crown", "Eerie Idol Games", "134.95", "in", "Just arrived", meta=("1-4", "60-120 min", "12+", "3.2"), link="product.html")]
    cfg = dict(
        crumbs=[("Home", "index.html"), ("Board Games", "collection.html"), ("Expansions", "collection.html"), ("Wild Kingdom", None)],
        gallery=["okc-wild-kingdom", "okc-1"], state="pre",
        badges=[badge("preorder", "Preorder"), badge("expansion", "")], vendor="Eerie Idol Games", title="The Old King's Crown: Wild Kingdom",
        bggline='<div class="bggline"><span>2026</span><i>·</i><span>Not yet rated on BGG</span><i>·</i><span>Designed by <a href="#">Pablo Clark</a></span></div>',
        stats=[("users", "Players", "1-4"), ("clock", "Play time", "60-120 min"), ("person", "Age", "12+"), ("mind", "Complexity", "3.2 / 5")],
        tags=[("Categories", ["Card Game", "Fantasy", "Medieval"]), ("Mechanics", ["Hand Management", "Variable Player Powers"])],
        summary="New houses, new Kingdom cards and fresh ways to fight for the crown. <mark>[publisher summary]</mark>",
        expnote='<div class="expnote"><img src="img/old-kings-crown.jpg" alt=""><span>Needs <a href="product.html">The Old King\'s Crown</a> to play. <span style="color:var(--ink-muted)">This is an expansion, not a standalone game.</span></span></div>',
        price="64.95", rrp="75", save="10.05",
        comp=[("old-kings-crown", "The Old King's Crown (base game)", "134.95"), ("okc-sleeves", "The Old King's Crown: Card Sleeve Pack", "19.95")],
        desc='<p>Wild Kingdom brings new houses and Kingdom cards to The Old King\'s Crown, with fresh abilities that change how each battle plays out.</p><p><mark>[publisher description from the product import]</mark></p>',
        specs=[("Base game", '<a href="product.html">The Old King\'s Crown</a>'), ("Designer", '<a href="#">Pablo Clark</a>'), ("Publisher", '<a href="#">Eerie Idol Games</a>'), ("Players", "1-4"), ("Play time", "60-120 min"), ("Age", "12+"), ("Complexity", "3.2 / 5"), ("Year published", "2026"), ("BoardGameGeek", 'Not yet rated · <a href="#">View on BGG</a>')],
        rows=[("Featured collection", "More from the series · bgg.families (real series only) · hidden when empty", "More from The Old King's Crown series", "", "#", more),
              ("Product recommendations", "Shopify related products (automatic)", "You might also like", "", "", RELATED)],
        flags=["<b>Expansion variation:</b> Expansion badge, \"Needs [base game]\" note (from bgg.expands), the base game first in the slider, and a \"More from the series\" row. Shown here in the Preorder state; use the State switch for the others."],
    )
    render("product-expansion.html", "Wild Kingdom · Advent Games", "Product: Expansion", "product.json · expansion data (bgg.is_expansion, bgg.expands)", pdp(cfg), STATE_TOGGLE, PAGE_JS + PDP_JS)

def page_rpg_product():
    more = [card(p["img"], p["title"], p["vendor"], p["price"], p["state"], p.get("badge", ""), line=p["line"], link="product-rpg.html") for p in RPG if p["title"].startswith("ALIEN") and "Core" not in p["title"]]
    cfg = dict(
        crumbs=[("Home", "index.html"), ("Roleplaying", "collection-rpg.html"), ("ALIEN", "collection-rpg.html"), ("Core Rulebook", None)],
        gallery=["alien-core", "alien-screen", "alien-starter"],
        badges=[badge("new", "Just arrived")], vendor="Free League", title="ALIEN: The Roleplaying Game (Evolved Edition) Core Rulebook",
        stats=[("book", "System", "ALIEN"), ("box", "Category", "Core rulebook"), ("user", "Publisher", "Free League"), ("calendar", "Year", "2025")],
        tags=[("Genre", ["Sci-fi", "Horror"])],
        summary="The complete rules for survival horror in the ALIEN universe, rebuilt for the Evolved Edition. Hardcover, 352 pages.",
        price="84.95", rrp="95", save="10.05",
        comp=[("alien-screen", "ALIEN: MU/TH/UR Screen", "44.95"), ("alien-stress-dice", "ALIEN: Stress Dice Set", "24.95")],
        desc='<p>In space, no one can hear you scream. The Evolved Edition of the ALIEN roleplaying game refines the Year Zero Engine rules, with faster stress and panic, a new campaign framework and updated colonial marine, corporate and frontier career paths.</p><p>Hardcover, 352 pages, full colour. <mark>[publisher description]</mark></p>',
        specs=[("System", '<a href="collection-rpg.html">ALIEN</a>'), ("Category", '<a href="#">Core rulebook</a>'), ("Publisher", '<a href="#">Free League</a>'), ("Designers", '<a href="#">Tomas Härenstam</a>'), ("Genre", '<a href="#">Sci-fi</a> <a href="#">Horror</a>'), ("Year published", "2025"), ("Barcode", "9789189765123")],
        tab2="Book details",
        rows=[("Featured collection", "More for this system · rpg.system · hidden when empty", "More for ALIEN", "Starter sets, screens, adventures and dice for the same system.", "#", more)],
        flags=["<b>RPG variation:</b> the stats strip shows System · Category · Publisher · Year instead of players and time, the second tab is \"Book details\", and there's a \"More for [system]\" row. No BGG line (RPGs aren't on BGG)."],
    )
    render("product-rpg.html", "ALIEN Core Rulebook · Advent Games", "Product: RPG", "product.json · rpg.system, rpg.product_kind", pdp(cfg), STATE_TOGGLE, PAGE_JS + PDP_JS)

def page_accessory():
    same = [card(p["img"], p["title"], p["vendor"], p["price"], p["state"], p.get("badge", ""), line=p["line"], link="product-accessory.html") for p in ACCESSORIES if "63.5" in p["line"] and "Clank!: Card Sleeves - Dragon" not in p["title"]]
    cfg = dict(
        crumbs=[("Home", "index.html"), ("Accessories", "collection-accessories.html"), ("Card sleeves", "collection-accessories.html"), ("Clank! Sleeves - Dragon", None)],
        gallery=["clank-sleeves-dragon", "clank-sleeves-artifacts"],
        badges=[], vendor="Dire Wolf", title="Clank!: Card Sleeves - Dragon",
        stats=[("box", "Sleeve size", "63.5 x 88 mm"), ("blocks", "Pack", "100 sleeves"), ("shield", "Finish", "Matte"), ("puzzle", "Made for", '<a href="#">Clank!</a>')],
        summary="Official Dragon art sleeves for Clank!, sized for its standard cards. <mark>[size, pack and finish illustrative]</mark>",
        price="17.95",
        desc='<p>Protect your Clank! cards with official Dragon art sleeves. Matte finish, clear front, 100 sleeves per pack.</p><p><mark>[publisher description]</mark></p>',
        specs=[("Sleeve size", "63.5 x 88 mm"), ("Pack", "100 sleeves"), ("Finish", "Matte"), ("Made for", '<a href="#">Clank!</a>'), ("Publisher", '<a href="#">Dire Wolf</a>'), ("Barcode", "0810058800123")],
        tab2="Details",
        rows=[("Featured collection", "Other sleeves in this size · advent.sleeve_size · hidden when empty", "Other sleeves in 63.5 x 88 mm", "", "#", same)],
        flags=["<b>Accessory variation:</b> the strip shows Sleeve size · Pack · Finish · Made for, no BGG line or videos, and an \"Other sleeves in this size\" row. Generic sleeves show only size and pack (no \"Made for\"), so they never claim to fit a game they weren't made for."],
        notice=False,
    )
    render("product-accessory.html", "Clank! Sleeves · Advent Games", "Product: Accessory", "product.json · advent.sleeve_size, pack_qty, finish, made_for", pdp(cfg), STATE_TOGGLE, PAGE_JS + PDP_JS)

# ------------------------------------------------------------------ page scripts (plain strings, not f-strings)
PAGE_JS = r'''
// filters sidebar scrolls with the page: it moves with the page until its bottom is in view, then sticks;
// scrolling back up, it moves back down until its top is in view (Dean, BugHerd #102). Desktop only.
(function(){var f=document.querySelector('.filters'); if(!f) return;
  var mq=window.matchMedia('(min-width: 901px)'), lastY=window.scrollY, top=null;
  function base(){return (parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--sticky-top'))||96)+12;}
  function upd(){ if(!mq.matches){f.style.top='';return;}
    var b=base(), h=f.offsetHeight, vh=window.innerHeight, y=window.scrollY, d=y-lastY; lastY=y;
    if(top===null) top=b;
    if(h+b+16<=vh){top=b;} else {top=Math.min(b,Math.max(vh-h-16,top-d));}
    f.style.top=top+'px'; f.style.setProperty('--applied-top',(b-12)+'px'); }
  window.addEventListener('scroll',upd,{passive:true}); window.addEventListener('resize',upd);
  f.addEventListener('toggle',upd,true); upd();
})();

(function(){
  var coll=document.querySelector('.js-coll');
  if(coll){
    var fb=document.querySelector('.js-filter'), fl=document.querySelector('.js-filter-label');
    var mobile=function(){return window.innerWidth<=900;};
    fb.addEventListener('click',function(){
      if(mobile()){coll.classList.add('drawer-open');return;}
      var off=coll.classList.toggle('filters-off'); fb.setAttribute('aria-expanded',String(!off)); fl.textContent=off?'Show filters':'Hide filters';
    });
    function label(){fl.textContent=mobile()?'Filter & sort':(coll.classList.contains('filters-off')?'Show filters':'Hide filters');}
    label(); window.addEventListener('resize',label);
    document.querySelectorAll('.js-drawer-close').forEach(function(b){b.addEventListener('click',function(){coll.classList.remove('drawer-open');});});
    var vbs=document.querySelectorAll('.js-view');
    function setView(v){coll.classList.toggle('view-list',v==='list'); vbs.forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.view===v));}); try{localStorage.setItem('advent-view',v);}catch(e){}}
    vbs.forEach(function(b){b.addEventListener('click',function(){setView(b.dataset.view);});});
    try{var sv=localStorage.getItem('advent-view'); if(sv) setView(sv);}catch(e){}
    document.querySelectorAll('.pchips button').forEach(function(b){b.addEventListener('click',function(){b.setAttribute('aria-pressed',String(b.getAttribute('aria-pressed')!=='true'));});});
  }

})();
'''

PDP_JS = r'''
(function(){
  var cards=document.querySelectorAll('.availcard'), btn=document.querySelector('.js-buybtn'), row=document.querySelector('.js-buyrow'), notify=document.querySelector('.js-notify'), tb=document.querySelectorAll('.wf-toggle [data-state]');
  function setState(s){
    var c=document.querySelector('.availcard[data-state="'+s+'"]'); if(!c) return;
    cards.forEach(function(x){x.classList.toggle('on',x===c);});
    btn.textContent=c.dataset.btn; var out=s==='out';
    row.style.display=out?'none':''; notify.style.display=out?'grid':'none';
    tb.forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.state===s));});
  }
  var start=(new URLSearchParams(location.search)).get('state') || (document.querySelector('.availcard.on')||{dataset:{state:'in'}}).dataset.state;
  setState(start);
  tb.forEach(function(b){b.addEventListener('click',function(){setState(b.dataset.state);});});
  var main=document.querySelector('.js-main');
  document.querySelectorAll('.js-thumb').forEach(function(t){t.addEventListener('click',function(){main.src=t.dataset.src; document.querySelectorAll('.js-thumb').forEach(function(x){x.setAttribute('aria-current',String(x===t));});});});
  document.querySelectorAll('.js-tab').forEach(function(t){t.addEventListener('click',function(){var i=t.dataset.tab; document.querySelectorAll('.js-tab').forEach(function(x){x.setAttribute('aria-selected',String(x===t));}); document.querySelectorAll('.tabpanel').forEach(function(p){p.classList.toggle('on',p.dataset.panel===i);});});});
  var more=document.querySelector('.js-more'), desc=document.querySelector('.js-desc');
  if(more){ if(desc.scrollHeight<=230){desc.classList.remove('clamped'); more.style.display='none';}
    more.addEventListener('click',function(){var c=desc.classList.toggle('clamped'); more.textContent=c?'Show more':'Show less';});}
  var ct=document.querySelector('.js-comp');
  if(ct){document.querySelector('.js-comp-prev').addEventListener('click',function(){ct.scrollBy({left:-ct.clientWidth,behavior:'smooth'});}); document.querySelector('.js-comp-next').addEventListener('click',function(){ct.scrollBy({left:ct.clientWidth,behavior:'smooth'});});}
  document.querySelectorAll('.qty').forEach(function(q){var i=q.querySelector('input'), b=q.querySelectorAll('button'); b[0].addEventListener('click',function(){i.value=Math.max(1,(+i.value||1)-1);}); b[1].addEventListener('click',function(){i.value=(+i.value||1)+1;});});
})();
'''

if __name__ == "__main__":
    page_collection(); page_preorders(); page_rpg(); page_accessories()
    page_product(); page_expansion(); page_rpg_product(); page_accessory()
