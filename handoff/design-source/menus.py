"""Header menus: desktop mega menus, mobile drawer, predictive search. Content follows the approved wireframe (meganav.html);
layouts follow Enterprise's three mega menu block types (Column, Sidebar, plus standard dropdown)."""
import html
from common import I, tag

C = "collection.html"; P = "collection-preorders.html"; R = "collection-rpg.html"; A = "collection-accessories.html"

def lk(t, u=C):
    return f'<a href="{u}">{t}</a>'

# ---------------------------------------------------------------- data
PRE_COLS = [("Preorders", [("New to preorder", P), ("Coming soon", P), ("All preorders", P), ("Kickstarter", P)]),
            ("By type", [("Board games", P), ("Expansions", P), ("RPGs", P), ("Accessories", P)])]
PRE_BANNERS = [("Due this month", "Big releases landing soon", "age-of-innovation", "sky"),
               ("Kickstarter pledges", "Late pledges and retail editions", "aberration", "sun"),
               ("How preorders work", "Pay today, ships on release", "okc-wild-kingdom", "orange")]
ARRIVED = ["New board games", "New expansions", "New RPGs", "New accessories", "Back in stock", "Everything new"]
SALE = ["Weekly sale", "Clearance", "Dings &amp; dents", "All sale"]
BOARD = [
    ("Game type", "mind", [("Strategy", "mind", ""), ("Family", "family", ""), ("Party", "balloon", ""), ("Thematic", "book", ""),
                           ("Wargames", "tank", ""), ("Abstract", "hex", ""), ("Children's", "blocks", ""), ("Card games", "cards", "")]),
    ("Player count", "p1", [("Solo", "p1", ""), ("Two-player", "p2", ""), ("3-4 players", "p4", ""), ("Big groups (6+)", "p6", "")]),
    ("Rankings &amp; awards", "trophy", [("Best sellers", "star", ""), ("BGG Top 100", "trophy", "Top 100"), ("Gateway games", "meeple", ""), ("Spiel des Jahres", "award", "Award"),
                           ("Kinderspiel des Jahres", "award", "Award"), ("Deutscher Spiele Preis", "award", "Award"), ("International Gamers Award", "award", "Award"), ("Meeple's Choice", "award", "Award")]),
    ("LCGs &amp; miniatures", "mini", [("All Living Card Games", "cards", ""), ("Arkham Horror LCG", "cards", ""), ("Marvel Champions LCG", "cards", ""), ("The Lord of the Rings LCG", "cards", ""),
                           ("All miniatures games", "mini", ""), ("Star Wars: Legion", "mini", ""), ("Star Wars: X-Wing", "mini", ""), ("Marvel: Crisis Protocol", "mini", "")]),
    ("Collections", "deck", [("Euro heavyweights", "mind", ""), ("Openers: light &amp; fun", "balloon", ""), ("Hard to find", "crown", ""), ("Kickstarter", "box", "")]),
    ("Expansions", "puzzle", [("All expansions", "puzzle", ""), ("New expansions", "puzzle", "New"), ("Expansions on preorder", "calendar", "")]),
]
TONES = ["blue", "sun", "orange", "sky", "green", "muted"]
RPG_COLS = [("Fantasy", ["Dungeons &amp; Dragons", "Pathfinder", "Daggerheart", "The One Ring", "Warhammer Fantasy"]),
            ("Sci-fi", ["Starfinder", "Alien RPG", "Cyberpunk RED", "Star Wars RPG", "Dune"]),
            ("Horror &amp; modern", ["Call of Cthulhu", "Vampire: The Masquerade", "Delta Green"]),
            ("Browse all", ["All roleplaying games", "Starter sets", "Core rulebooks", "Solo RPGs", "RPG preorders"]),
            ("RPG accessories", ["Dice", "Miniatures", "Maps &amp; tiles", "GM screens"])]
ACC_COLS = [("Protect", ["Sleeves", "Inserts &amp; organisers"]), ("Upgrade", ["Tokens &amp; scenery", "Coins", "Component upgrades"]), ("Play", ["Dice", "Play mats"])]
ACC_BANNERS = [("Card sleeves", "Every standard size in stock", "clank-sleeves-dragon", "sky"),
               ("Organisers", "Tidy boxes, faster setup", "compile-aux-3", "sun"),
               ("Dice", "Sets for every system", "dragon-d6-dice", "orange")]

KIND = {"preorders": "column", "arrived": "dropdown", "board": "sidebar", "rpg": "column", "acc": "column", "sale": "dropdown"}
NAV_KEYS = ["preorders", "arrived", "board", "rpg", "acc", "sale"]

# ---------------------------------------------------------------- desktop
def _col(h, links, u):
    items = "".join(f'<li>{lk(t, u)}</li>' for t in links)
    return f'<div class="mm-col"><h4>{h}</h4><ul>{items}</ul><a class="mm-all" href="{u}">Shop all {I("right",12)}</a></div>'

def _banner(t, s, img, tone, u):
    return f'<a class="mm-ban mm-ban--{tone}" href="{u}"><div><strong>{t}</strong><span>{s}</span><em>Shop now {I("right",12)}</em></div><img src="img/{img}.jpg" alt="" loading="lazy"></a>'

def _tile(t, ic, badge, u=C, i=0):
    b = f'<span class="mm-badge">{badge}</span>' if badge else ""
    return f'<a class="mm-tile mm-tile--icon" href="{u}"><span class="mm-tile__img type--{TONES[i % len(TONES)]}">{I(ic,80,"mm-tile__ic")}{b}</span><span class="mm-tile__t">{t}</span></a>'

def _tiles(ts):
    return "".join(_tile(n, ic, bd, C, i) for i, (n, ic, bd) in enumerate(ts))

def _thumb(ic, i):
    return f'<span class="mm-thumb type--{TONES[i % len(TONES)]}">{I(ic,20)}</span>'

def mega_panels():
    pre = (f'<div class="mega mega--col" data-mega="preorders">{tag("Mega menu: Column", "native", "Preorders · 2 link columns (no images) + 3 promo banners set in the block, swapped monthly")}<div class="inner mm-wrap">'
           f'<div class="mm-cols" style="--n:2">{"".join(_col(h, [t for t, _ in ls], P) for h, ls in PRE_COLS)}</div>'
           f'<div class="mm-bans">{"".join(_banner(*b, P) for b in PRE_BANNERS)}</div></div></div>')
    side = "".join(f'<button type="button" class="mm-side__item{" on" if i == 0 else ""}" data-tab="{i}">{_thumb(th, i)}<span>{g}</span>{I("right",14)}</button>' for i, (g, th, _) in enumerate(BOARD))
    panes = "".join(f'<div class="mm-pane" data-pane="{i}"{"" if i == 0 else " hidden"}><div class="mm-pane__h"><h4>{g}</h4><a class="mm-all" href="{C}">Shop all {g.lower()} {I("right",12)}</a></div><div class="mm-tiles">{_tiles(ts)}</div></div>' for i, (g, _, ts) in enumerate(BOARD))
    board = (f'<div class="mega mega--side" data-mega="board">{tag("Mega menu: Sidebar", "native", "Board Games · left list = 2nd-level menu items with thumbnail; hover swaps the image tiles · tiles use the same pastel icon style as the home page game types (icons + colours set in the block, no photos to source)")}<div class="inner mm-wrap">'
             f'<div class="mm-side">{side}<a class="mm-side__all" href="{C}">All board games {I("right",14)}</a></div><div class="mm-panes">{panes}</div></div></div>')
    rpg = (f'<div class="mega mega--col" data-mega="rpg">{tag("Mega menu: Column", "native", "Roleplaying · systems grouped by genre (from the rpg_system metaobject), Browse all, RPG accessories · no images")}<div class="inner mm-wrap">'
           f'<div class="mm-cols" style="--n:5">{"".join(_col(h, ls, A if h == "RPG accessories" else R) for h, ls in RPG_COLS)}</div></div></div>')
    acc = (f'<div class="mega mega--col" data-mega="acc">{tag("Mega menu: Column", "native", "Accessories · grouped by job (protect, upgrade, play) + 3 promo banners")}<div class="inner mm-wrap">'
           f'<div class="mm-cols" style="--n:3">{"".join(_col(h, ls, A) for h, ls in ACC_COLS)}</div>'
           f'<div class="mm-bans">{"".join(_banner(*b, A) for b in ACC_BANNERS)}</div></div></div>')
    arrived = (f'<div class="mega mega--drop" data-mega="arrived">{tag("Dropdown", "native", "standard dropdown, no mega menu block · no images (Dean)")}'
               f'<ul>{"".join(f"<li>{lk(t, P)}</li>" for t in ARRIVED)}</ul></div>')
    sale = (f'<div class="mega mega--drop" data-mega="sale">{tag("Dropdown", "native", "standard dropdown · kept small on purpose")}'
            f'<ul>{"".join(f"<li>{lk(t)}</li>" for t in SALE)}</ul></div>')
    return pre + arrived + board + rpg + acc + sale

# ---------------------------------------------------------------- mobile drawer
def _acc(title, body, open_=False, thumb=""):
    th = thumb
    return f'<details class="mob-acc"{" open" if open_ else ""}><summary>{th}<span>{title}</span>{I("chev",16)}</summary><div class="mob-acc__b">{body}</div></details>'

def _links(ls, u):
    return '<ul class="mob-links">' + "".join(f'<li>{lk(t, u)}</li>' for t in ls) + f'</ul><a class="mob-all" href="{u}">Shop all {I("right",12)}</a>'

def _mob_bans(bs, u):
    return '<div class="mob-bans">' + "".join(_banner(*b, u) for b in bs) + '</div>'

NAV_LABEL = {"preorders": ("Preorders", P), "arrived": ("Just Arrived", P), "board": ("Board Games", C), "rpg": ("Roleplaying", R), "acc": ("Accessories", A), "sale": ("Sale", C)}

def _sub(key):
    lab, u = NAV_LABEL[key]
    if key == "preorders":
        body = "".join(_acc(h, _links([t for t, _ in ls], P), i == 0) for i, (h, ls) in enumerate(PRE_COLS)) + _mob_bans(PRE_BANNERS, P)
    elif key == "board":
        body = "".join(_acc(g, '<div class="mob-tiles">' + _tiles(ts) + f'</div><a class="mob-all" href="{C}">Shop all {I("right",12)}</a>', i == 0, _thumb(th, i)) for i, (g, th, ts) in enumerate(BOARD))
    elif key == "rpg":
        body = "".join(_acc(h, _links(ls, A if h == "RPG accessories" else R), i == 0) for i, (h, ls) in enumerate(RPG_COLS))
    elif key == "acc":
        body = "".join(_acc(h, _links(ls, A), i == 0) for i, (h, ls) in enumerate(ACC_COLS)) + _mob_bans(ACC_BANNERS, A)
    else:
        ls = ARRIVED if key == "arrived" else SALE
        body = '<ul class="mob-links mob-links--flat">' + "".join(f'<li>{lk(t, u)}</li>' for t in ls) + '</ul>'
    return (f'<div class="mob-panel mob-panel--sub" data-sub="{key}" aria-hidden="true">'
            f'<button type="button" class="mob-back js-mob-back">{I("left",18)} Back</button>'
            f'<div class="mob-sub-h"><h3 class="h4">{lab}</h3><a href="{u}">Go to {lab} {I("right",12)}</a></div>{body}</div>')

def mobile_drawer():
    top = "".join(f'<li><button type="button" class="mob-item js-mob-go" data-go="{k}"><span>{NAV_LABEL[k][0]}</span>{I("right",18)}</button></li>' for k in NAV_KEYS)
    return f'''<div class="mob-scrim js-mob-close" hidden></div>
<aside class="mob" id="mobile-menu" aria-hidden="true" aria-label="Menu">
  <div class="mob-head">{tag("Mobile menu drawer", "native", "Enterprise mobile drawer · built from the same mega menu blocks as desktop · no custom work")}
    <button type="button" class="mob-x js-mob-close" aria-label="Close menu">{I("x",24)}</button>
    <a href="index.html" class="mob-logo"><img src="img/advent-logo-h.png" alt="Advent Games"></a>
    <div class="mob-head-r"><a href="#" aria-label="Account">{I("user",24)}</a><a href="#" class="js-mob-cart" aria-label="Cart">{I("cart",24)}</a></div>
  </div>
  <div class="mob-stage">
    <div class="mob-panel mob-panel--main">
      <ul class="mob-list">{top}</ul>
      <ul class="mob-extra"><li><a href="wishlist.html">{I("heart",18)} Wishlist</a></li><li><a href="#">{I("user",18)} Account</a></li><li><a href="help.html">{I("chat",18)} Help &amp; FAQ</a></li><li><a href="help.html#orders">{I("truck",18)} Track my order</a></li><li><a href="help.html#shipping">{I("map",18)} Shipping &amp; pickup</a></li><li><a href="brands.html">{I("book",18)} Brands A-Z</a></li><li><a href="about.html">{I("book",18)} About</a></li></ul>
    </div>
    {"".join(_sub(k) for k in NAV_KEYS)}
  </div>
</aside>'''

# ---------------------------------------------------------------- predictive search
SEARCH_PRODUCTS = [
    ("old-kings-crown", "The Old King's Crown", "Eerie Idol Games", "134.95", "in"),
    ("okc-wild-kingdom", "The Old King's Crown: Wild Kingdom", "Eerie Idol Games", "64.95", "pre"),
    ("okc-sleeves", "The Old King's Crown: Card Sleeve Pack", "Eerie Idol Games", "19.95", "in"),
    ("wingspan-pocket", "Wingspan: Pocket Edition", "Stonemaier Games", "49.95", "in"),
    ("harmonies-pulse", "Harmonies", "Libellud", "59.95", "in"),
    ("harmonies-crescendo", "Harmonies: Crescendo", "Libellud", "39.95", "pre"),
    ("power-grid", "Power Grid Recharged", "Rio Grande Games", "69.95", "sup"),
    ("carcassonne", "Carcassonne", "Z-Man Games", "54.95", "in"),
    ("alien-core", "ALIEN: The Roleplaying Game Core Rulebook", "Free League", "84.95", "in"),
    ("alien-starter", "ALIEN RPG Starter Set", "Free League", "64.95", "in"),
    ("euphoria", "Euphoria: Essential Edition", "Stonemaier Games", "59.95", "soon"),
    ("king-of-tokyo", "King of Tokyo", "IELLO", "49.95", "in"),
    ("camel-up", "Camel Up", "Eggertspiele", "54.95", "in"),
    ("pandemic", "Pandemic", "Z-Man Games", "59.95", "in"),
    ("sushi-go-party", "Sushi Go Party!", "Gamewright", "34.95", "in"),
]

def search_panel():
    return f'''<div class="ps" id="predictive" hidden>{tag("Predictive search", "native", "Enterprise predictive search · Products / Collections / Articles tabs + Suggestions · View all results goes to the search page")}
  <div class="inner ps-wrap">
    <div class="ps-main">
      <div class="ps-tabs" role="tablist"><button type="button" class="on" data-pt="p">Products</button><button type="button" data-pt="c">Collections</button><button type="button" data-pt="a">Articles</button></div>
      <div class="ps-res js-ps-res" data-ptab="p"></div>
      <div class="ps-res" data-ptab="c" hidden><ul class="ps-plain"><li><a href="{C}">Board Games</a></li><li><a href="{C}">Strategy games</a></li><li><a href="{P}">Preorders</a></li><li><a href="{A}">Card sleeves</a></li></ul></div>
      <div class="ps-res" data-ptab="a" hidden><ul class="ps-plain"><li><a href="#">Worker placement: where to start</a></li><li><a href="#">Our top 10 gateway games</a></li><li><a href="#">How preorders work at Advent</a></li></ul></div>
      <a href="search.html" class="ps-all js-ps-all">View all results {I("right",14)}</a>
    </div>
    <div class="ps-side"><strong>Suggestions</strong><ul class="js-ps-sugg"></ul><strong class="ps-pop-h">Popular right now</strong><ul class="ps-pop"><li><a href="#">wingspan</a></li><li><a href="#">harmonies</a></li><li><a href="#">d&amp;d starter set</a></li><li><a href="#">card sleeves</a></li></ul></div>
  </div>
</div>'''

def menus_html():
    return mobile_drawer() + "\n"

PRODUCTS_JS = "[" + ",".join("{img:%r,t:%r,v:%r,p:%r,s:%r}" % (a, html.unescape(b), c, d, e) for a, b, c, d, e in SEARCH_PRODUCTS) + "]"

MENU_JS = r"""
(function(){
  // ---- desktop mega menus: hover/focus a top-level item to open its panel
  var row=document.querySelector('.nav-row'); if(!row) return;
  var items=row.querySelectorAll('.nav li[data-key]'), panels=row.querySelectorAll('.mega'), t=null, cur=null;
  function show(k,li){
    clearTimeout(t); if(cur===k) return; cur=k;
    panels.forEach(function(p){p.classList.toggle('on',p.dataset.mega===k);});
    items.forEach(function(x){x.classList.toggle('on',x.dataset.key===k); var a=x.querySelector('a'); if(a) a.setAttribute('aria-expanded',String(x.dataset.key===k));});
    var p=row.querySelector('.mega--drop[data-mega="'+k+'"]');
    if(p&&li){var r=li.getBoundingClientRect(), rr=row.getBoundingClientRect(); p.style.left=(r.left-rr.left)+'px';}
    document.body.classList.toggle('mega-open',!!k&&!(p));
  }
  function hide(){t=setTimeout(function(){cur=null;panels.forEach(function(p){p.classList.remove('on');});items.forEach(function(x){x.classList.remove('on');});document.body.classList.remove('mega-open');},140);}
  items.forEach(function(li){li.addEventListener('mouseenter',function(){show(li.dataset.key,li);}); li.addEventListener('focusin',function(){show(li.dataset.key,li);});});
  row.querySelectorAll('.nav-aux').forEach(function(x){x.addEventListener('mouseenter',hide);});
  row.addEventListener('mouseleave',hide); row.addEventListener('mouseenter',function(){clearTimeout(t);});
  document.addEventListener('keydown',function(e){if(e.key==='Escape') hide();});
  row.querySelectorAll('.mm-side__item').forEach(function(b){
    function go(){var side=b.closest('.mega'); side.querySelectorAll('.mm-side__item').forEach(function(x){x.classList.toggle('on',x===b);}); side.querySelectorAll('.mm-pane').forEach(function(p){p.hidden=p.dataset.pane!==b.dataset.tab;});}
    b.addEventListener('mouseenter',go); b.addEventListener('click',go); b.addEventListener('focus',go);
  });
  window.addEventListener('scroll',function(){if(cur) hide();},{passive:true});
})();
(function(){
  // ---- mobile drawer
  var m=document.getElementById('mobile-menu'); if(!m) return;
  var scrim=document.querySelector('.mob-scrim'), burger=document.querySelector('.burger');
  function open(){scrim.hidden=false; requestAnimationFrame(function(){document.body.classList.add('mob-open');}); m.setAttribute('aria-hidden','false'); setTimeout(function(){m.querySelector('.mob-x').focus();},250);}
  function close(){document.body.classList.remove('mob-open'); m.setAttribute('aria-hidden','true'); setTimeout(function(){scrim.hidden=true; back();},260); if(burger) burger.focus();}
  function go(k){m.querySelectorAll('.mob-panel--sub').forEach(function(p){var on=p.dataset.sub===k; p.classList.toggle('on',on); p.setAttribute('aria-hidden',String(!on)); if(on) p.scrollTop=0;}); m.classList.add('is-sub');}
  function back(){m.classList.remove('is-sub'); m.querySelectorAll('.mob-panel--sub').forEach(function(p){p.classList.remove('on');p.setAttribute('aria-hidden','true');});}
  if(burger) burger.addEventListener('click',open);
  m.querySelectorAll('.js-mob-go').forEach(function(b){b.addEventListener('click',function(){go(b.dataset.go);});});
  m.querySelectorAll('.js-mob-back').forEach(function(b){b.addEventListener('click',back);});
  document.querySelectorAll('.js-mob-close').forEach(function(b){b.addEventListener('click',close);});
  var mc=m.querySelector('.js-mob-cart'); if(mc) mc.addEventListener('click',function(e){e.preventDefault(); close(); var c=document.querySelector('.hdr-icons .cart'); if(c) setTimeout(function(){c.click();},280);});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&document.body.classList.contains('mob-open')) close();});
  document.querySelectorAll('[data-open-menu]').forEach(function(b){b.addEventListener('click',open);});
})();
(function(){
  // ---- predictive search
  var ps=document.getElementById('predictive'), form=document.querySelector('.hdr .search'); if(!ps||!form) return;
  var input=form.querySelector('.search-in'), res=ps.querySelector('.js-ps-res'), sugg=ps.querySelector('.js-ps-sugg');
  var DATA=__PRODUCTS__;
  var AV={in:['in','In stock'],sup:['supplier','At supplier'],pre:['preorder','Preorder'],soon:['coming','Coming soon']};
  function esc(s){var e=document.createElement('span');e.textContent=s;return e.innerHTML;}
  function mark(s,q){var i=s.toLowerCase().indexOf(q.toLowerCase()); if(i<0||!q) return esc(s); return esc(s.slice(0,i))+'<b class="ps-hl">'+esc(s.slice(i,i+q.length))+'</b>'+esc(s.slice(i+q.length));}
  function run(){
    var q=input.value.trim();
    if(q.length<2){ps.hidden=true; document.body.classList.remove('ps-open'); return;}
    var hits=DATA.filter(function(d){return (d.t+' '+d.v).toLowerCase().indexOf(q.toLowerCase())>-1;}).slice(0,5);
    res.innerHTML=hits.length?hits.map(function(d){var a=AV[d.s]||AV.in; var link=/rpg|ALIEN/i.test(d.t)?'product-rpg.html':(/sleeve/i.test(d.t)?'product-accessory.html':(/Wild Kingdom/.test(d.t)?'product-expansion.html':'product.html'));
        return '<a class="ps-row" href="'+link+'"><img src="img/'+d.img+'.jpg" alt=""><span class="ps-row__t"><strong>'+mark(d.t,q)+'</strong><span class="ps-row__v">'+esc(d.v)+'</span><span class="ag-avail ag-avail--'+a[0]+'">'+a[1]+'</span></span><span class="ps-row__p">$'+d.p+'</span></a>';}).join('')
      :'<p class="ps-none">No products match <strong>'+esc(q)+'</strong>. Try a game, publisher or designer.</p>';
    var words={};DATA.forEach(function(d){d.t.toLowerCase().split(/[:,!]/).forEach(function(w){w=w.trim(); if(w.indexOf(q.toLowerCase())>-1) words[w]=1;});});
    sugg.innerHTML=Object.keys(words).slice(0,4).map(function(w){return '<li><a href="#">'+mark(w,q)+'</a></li>';}).join('')||'<li class="ps-muted">No suggestions</li>';
    ps.querySelector('.js-ps-all').innerHTML='View all results for &ldquo;'+esc(q)+'&rdquo; ';
    ps.hidden=false; document.body.classList.add('ps-open');
  }
  input.addEventListener('input',run); input.addEventListener('focus',run);
  form.addEventListener('submit',function(e){e.preventDefault(); location.href='search.html';});
  document.addEventListener('click',function(e){if(!ps.hidden&&!ps.contains(e.target)&&!form.contains(e.target)&&!e.target.closest('[data-try-search]')){ps.hidden=true;document.body.classList.remove('ps-open');}});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!ps.hidden){ps.hidden=true;document.body.classList.remove('ps-open');input.blur();}});
  ps.querySelectorAll('.ps-tabs button').forEach(function(b){b.addEventListener('click',function(){ps.querySelectorAll('.ps-tabs button').forEach(function(x){x.classList.toggle('on',x===b);}); ps.querySelectorAll('[data-ptab]').forEach(function(p){p.hidden=p.dataset.ptab!==b.dataset.pt;});});});
  ps.querySelectorAll('.ps-pop a').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault(); input.value=a.textContent; run(); input.focus();});});
  document.querySelectorAll('[data-try-search]').forEach(function(b){b.addEventListener('click',function(){window.scrollTo(0,0); input.value='old king'; run(); input.focus();});});
})();
""".replace("__PRODUCTS__", PRODUCTS_JS)
