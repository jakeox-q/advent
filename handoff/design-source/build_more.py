# Advent Games: Search results, Blog, Article, Wishlist design drafts (per wireframes v1, which follow the Enterprise demo).
import re
from common import *
from build_pages import crumbs, collection_body, applied, avail_group, price_group, fgroup, flist, chk, recently_viewed, RECENT, RPG, BOARD, PAGE_JS

def sec(name, kind, note, body, cls="sec", sid=""):
    i = f' id="{sid}"' if sid else ""
    return f'<section class="{cls}"{i}>{tag(name, kind, note)}\n{body}</section>\n'

def flag(txt):
    return f'<div class="flag">{I("chat",16)}<span><b>For Jake:</b> {txt}</span></div>'

def by(slug):
    return next(p for p in BOARD + RPG if p["img"] == slug)

def gcard(p, **kw):
    keys = ("img", "title", "vendor", "price", "state", "badge", "rrp", "meta", "eta", "exp", "line", "page", "link")
    d = {k: v for k, v in p.items() if k in keys}; d.update(kw)
    return card(**d)

# ---------------------------------------------------------------- blog data
POSTS = [
    ("story", "Store news", "Our new website is live", "2 Nov 2026", "A faster store, better filters and preorders you can actually find. Here's what's changed and what's coming next."),
    ("courage", "Reviews", "Five great two-player games under $50", "21 Oct 2026", "Small boxes, big decisions. Our favourite head-to-head games for couples, flatmates and lunchtime rematches."),
    ("okc-wild-kingdom", "New releases", "The big preorders landing before Christmas", "10 Oct 2026", "From The Old King's Crown expansion to Euphoria's new edition, here's what's due and when to lock it in."),
    ("carcassonne", "Reviews", "Five gateway games for your next family games night", "28 Sep 2026", "Easy to teach, quick to play and fun at any age. Start here if you're new to modern board games."),
    ("gettysburg", "New releases", "GMT's latest P500 list, explained", "14 Sep 2026", "What P500 means, how it works with preorders at Advent, and the titles we're most excited about."),
    ("akropolis-pantheon", "Store news", "Pickup is changing for the holidays", "1 Sep 2026", "Tuesday night pickups take a short break over Christmas. Here are the dates to plan around."),
]
FEATURED = ("okc-1", "New releases", "Essen 2026: the games we're most excited to stock", "3 Nov 2026", "Every October the hobby descends on Essen, Germany, for the world's biggest board game fair. These are the new releases we'll be bringing to Australia, and when you can expect them.")

def post_card(img, tg, t, d, ex, h="h3"):
    return (f'<a class="post-card" href="article.html"><span class="post-card__img"><img src="img/{img}.jpg" alt="" loading="lazy"></span>'
            f'<span class="post-tag">{tg}</span><{h} class="post-card__t">{t}</{h}><span class="post-date">{d}</span></a>')

SHARE = f'<div class="share"><span>Share</span><a href="#" aria-label="Share on Facebook">Facebook</a><a href="#" aria-label="Share on X">X</a><a href="#" aria-label="Share on Pinterest">Pinterest</a><a href="#" aria-label="Copy link">{I("mail",14)} Email</a></div>'

# ================================================================ SEARCH
def page_search():
    alien = [p for p in RPG if p["title"].startswith("ALIEN")]
    groups = [avail_group(checked=(), counts=("5", "1", "0")), price_group("0", "100"),
              fgroup("Product type", "".join(chk(n, c) for n, c in [("RPG book", "3"), ("RPG accessory", "2"), ("Board game", "1")])),
              fgroup("Publisher", "".join(chk(n, c) for n, c in [("Free League", "5"), ("Gale Force Nine", "1")]))]
    body = collection_body(alien, None, groups, "6", 0, per_page=False)
    body = re.sub(r'<select aria-label="Sort by">.*?</select>', '<select aria-label="Sort by"><option selected>Relevance</option><option>Price, low to high</option><option>Price, high to low</option></select>', body, count=1, flags=re.S)
    body = body.replace('6 products</span>', '6 products · 1 article</span>', 1)
    body = re.sub(r'<nav class="paging".*?</nav>', '', body, count=1, flags=re.S)
    art = ('<a class="ag-card search-art" href="article.html"><span class="search-art__img"><img src="img/alien-starter.jpg" alt="" loading="lazy"><span class="ag-badge ag-badge--new">Article</span></span>'
           '<span class="search-art__b"><span class="post-tag">Reviews</span><strong>ALIEN Evolved: which box should you start with?</strong><span class="post-date">12 Oct 2026</span><span class="search-art__more">Read article ' + I("right", 14) + '</span></span></a>')
    i = body.index('<div class="plist">')
    j = body.rindex('</div>', 0, i)
    body = body[:j] + art + body[j:]
    main = (crumbs(("Home", "index.html"), ("Search", None))
        + sec("Search template", "native", "Enterprise search page · heading + search field, then the same toolbar and Search &amp; Discovery sidebar as collections · sort is Relevance / Price only (Shopify limit) · matching blog articles show inline as cards after the products",
              f'''<div class="inner search-head"><h1>Search</h1>
  <form class="search-big" onsubmit="return false"><label class="sr" for="sq">Search</label><input id="sq" class="ag-input" type="search" value="alien"><button class="ag-btn ag-btn--primary" type="submit">{I("search",18)} Search</button></form>
  <p class="search-sum">Showing <b>7 results</b> for <b>&ldquo;alien&rdquo;</b></p></div>''', cls="sec sec--tight")
        + f'<section class="coll-sec">{tag("Search results", "native", "same product card and filters as collections · no Products / Articles tabs on this page (they live in the predictive search dropdown)")}' + body + '</section>'
        + sec("Search: no results", "native", "what shows when nothing matches · Enterprise empty state + our tips and a link to special orders", f'''<div class="inner"><div class="search-empty">{I("search",36)}<h2 class="h3">No results for &ldquo;nusfjordd&rdquo;</h2>
  <p>Check the spelling or try fewer words. Searching by publisher or designer works too.</p>
  <div class="search-empty__btns"><a class="ag-btn ag-btn--primary" href="collection.html">Browse board games</a><a class="ag-btn ag-btn--secondary" href="about.html#contact">Ask Dean to order it in</a></div></div></div>''', cls="sec sec--tint")
        + recently_viewed(RECENT))
    render("search.html", "Search: alien · Advent Games", "Search results", "search.json · Enterprise search template", main, extra_js=PAGE_JS)

# ================================================================ BLOG
def page_blog():
    tags = "".join(f'<a href="#"{" class=\"on\"" if i == 0 else ""}>{t}</a>' for i, t in enumerate(["All", "New releases", "Reviews", "Store news"]))
    fi, ftg, ft, fd, fex = FEATURED
    main = (crumbs(("Home", "index.html"), ("News &amp; reviews", None))
        + sec("Blog posts (main blog)", "native", "Enterprise main blog, no changes · centred title + description, share links, tag links (All + each article tag), latest post as a wide featured card, then 3-column grid · Dean just tags posts and the links appear",
              f'''<div class="inner"><div class="blog-head"><h1>News &amp; reviews</h1><p>New releases, honest reviews and store news from Dean. What's landing, what we're playing and what's worth your table time.</p>{SHARE}
  <nav class="blog-tags" aria-label="Filter by topic">{tags}</nav></div>
  <a class="post-feat" href="article.html"><span class="post-feat__img"><img src="img/{fi}.jpg" alt=""></span><span class="post-feat__b"><span class="post-tag">{ftg}</span><h2 class="h2">{ft}</h2><p>{fex}</p><span class="post-date">{fd}</span><span class="post-more">Read more {I("right",14)}</span></span></a>
  <div class="post-grid">{"".join(post_card(*p) for p in POSTS)}</div>
  <nav class="paging" aria-label="Pages"><ol><li><a href="#" aria-label="Previous page">{I("left",16)}</a></li><li><span class="cur" aria-current="page">1</span></li><li><a href="#">2</a></li><li><a href="#">3</a></li><li><a href="#" aria-label="Next page">{I("right",16)}</a></li></ol></nav></div>''')
        + sec("Media with text", "native", "optional · as on the Enterprise demo blog page", f'''<div class="inner"><div class="mwt blog-help">
  <div class="mwt-media"><div class="photo"><img src="img/beginners.jpg" alt=""></div></div>
  <div class="mwt-copy"><span class="eyebrow">Need a hand?</span><h2 class="h2">Not sure what to play next?</h2><p class="body-lg">Tell Dean who you play with and what you enjoy, and he'll point you to a few games that fit. No call centre, no bots, just a fellow gamer.</p><a class="ag-btn ag-btn--orange" href="about.html#contact">Ask Dean</a></div></div></div>''', cls="sec sec--tint")
    )
    render("blog.html", "News & reviews · Advent Games", "Blog", "blog.json · Enterprise main blog", main)

# ================================================================ ARTICLE
GAMES = [("carcassonne", "Carcassonne", "The tile-laying classic. Draw a tile, add it to the map, place a meeple to claim a road, city or field. Turns take seconds, the rules take five minutes, and the countryside you build together looks great on the table."),
         ("sushi-go-party", "Sushi Go Party!", "Pick a card, pass the rest, build the best plate of sushi. It plays up to eight, so it's perfect when cousins come over, and the menu changes every game so it stays fresh."),
         ("camel-up", "Camel Up", "A chaotic camel race where camels stack and ride each other to the finish. Place your bets, shake the pyramid and watch it all go wrong. Loud, silly and great with kids."),
         ("king-of-tokyo", "King of Tokyo", "Giant monsters fighting over Tokyo with Yahtzee-style dice. Smash, heal or buy power cards. Quick, punchy and a gateway to bigger dice games."),
         ("pandemic", "Pandemic", "Work together to stop four diseases spreading across the world. Everyone wins or loses as a team, which makes it the perfect first co-op for families who don't love losing to each other.")]

def page_article():
    body = "".join(f'<h2 class="h3">{i+1}. {n}</h2><p>{d} <a href="product.html">Shop {n}</a></p>' + (f'<figure class="art-fig"><img src="img/{s}.jpg" alt="{n} box art"><figcaption>{n}</figcaption></figure>' if i in (0, 2) else "") for i, (s, n, d) in enumerate(GAMES))
    shop = [gcard(by(s)) for s, _, _ in GAMES]
    main = (crumbs(("Home", "index.html"), ("News &amp; reviews", "blog.html"), ("Reviews", None))
        + sec("Article (main article)", "native", "Enterprise main article, no changes · tag, centred title and date, full-width hero, narrow reading column, share + prev/next + read time at the end · products linked inline from the body text",
              f'''<article><div class="inner"><header class="art-head"><span class="post-tag">Reviews</span><h1>Five gateway games for your next family games night</h1><p class="art-meta">By Dean · 28 Sep 2026 · 4 minute read</p></header>
  <div class="art-hero"><img src="img/beginners.jpg" alt=""></div>
  <div class="art-body"><p class="art-lede">New to modern board games, or teaching someone who is? These five are easy to learn, quick to set up and fun across ages. Every one of them has earned a permanent spot on our own shelf.</p>{body}
  <p>Want a recommendation for your group? <a href="about.html#contact">Ask Dean</a> and tell us who you play with.</p>
  <footer class="art-foot">{SHARE}<nav class="art-nav"><a href="#">{I("left",14)} Previous</a><a href="#">Next {I("right",14)}</a></nav></footer></div></div></article>''')
        + sec("Featured collection", "tweak", "optional · 'Games in this article' · the theme's product carousel fed by an article.featured_games metafield (products picked per post) + a few lines of Liquid · hides when empty · cut if the budget is tight, inline links do the same job for free",
              f'<div class="inner">{sec_head("Games in this article")}{carousel(shop, cols=5)}</div>', cls="sec sec--tint")
        + sec("Featured blog", "native", "Enterprise featured blog section · related articles", f'<div class="inner">{sec_head("Related articles", link="blog.html")}<div class="post-grid">{"".join(post_card(*p) for p in POSTS[:3])}</div></div>')
        + sec("Image banner", "native", "as on the Enterprise demo article · links to Help", f'''<div class="inner"><div class="help-cta"><div><h2 class="h2">Questions about an order?</h2><p class="body-lg">Shipping, pickup, preorders and returns, all in one place.</p></div><div class="help-cta__btns"><a class="ag-btn ag-btn--orange" href="help.html">Help &amp; FAQ</a></div></div>
  {flag("blog comments are native but off in this draft. Recommend leaving them off at launch (moderation load) unless Dean wants them.")}</div>''')
    )
    render("article.html", "Five gateway games · Advent Games", "Blog post", "article.json · Enterprise main article", main)

# ================================================================ WISHLIST
def page_wishlist():
    items = [gcard(by("okc-wild-kingdom")) if False else card("okc-wild-kingdom", "The Old King's Crown: Wild Kingdom", "Eerie Idol Games", "64.95", "pre", "Preorder", exp=True, meta=("1-4", "60-120 min", "12+", "3.2")),
             gcard(by("euphoria")), gcard(by("power-grid")),
             card("gettysburg", "Three Days of Gettysburg: Deluxe Edition", "GMT Games", "169.95", "out", meta=("1-2", "2 hrs+", "14+", "3.7")),
             gcard(by("harmonies-crescendo"))]
    items = [c.replace('class="ag-card__fav"', 'class="ag-card__fav is-on"', 1) for c in items]
    main = (crumbs(("Home", "index.html"), ("Wishlist", None))
        + sec("App block: Wishlist", "custom", "OPTIONAL APP · not in build scope · Enterprise has no native wishlist · kept simple: hearts on cards + product page, saved list, share link (standard in wishlist apps) · app not chosen yet · monthly app cost to Dean",
              f'''<div class="inner"><div class="wl-head"><div><h1>Your wishlist</h1><p>Saved games and their current availability. Share your list with family before birthdays and Christmas.</p></div>
  <div class="wl-actions"><button class="ag-btn ag-btn--secondary" type="button">{I("mail",16)} Share wishlist</button><button class="ag-btn ag-btn--orange js-wl-addall" type="button">{I("cart",16)} Add in-stock items to cart</button>{tag("Add all button", "custom", "small custom JS if the chosen app doesn't include it: adds every in-stock item on the list to the cart in one go via Shopify's cart API, then opens the cart drawer")}</div></div>
  <div class="pgrid wl-grid">{"".join(items)}</div>
  {flag("optional, from Dean's design doc (desirable but secondary). App not chosen yet, so this shows only the basics most wishlist apps share. App subscription is client cost, setup time to quote.")}</div>''')
        + recently_viewed(RECENT))
    render("wishlist.html", "Wishlist · Advent Games", "Wishlist (optional app)", "page.wishlist.json · app block", main, extra_js=WL_JS)

WL_JS = r'''
(function(){var b=document.querySelector('.js-wl-addall'); if(!b) return;
  b.addEventListener('click',function(){
    var btns=[].slice.call(document.querySelectorAll('.wl-grid .ag-card')).filter(function(c){return c.querySelector('.ag-avail--in');}).map(function(c){return c.querySelector('.ag-card__action button');});
    btns.forEach(function(x){x.click();});
    var n=document.querySelector('.js-cd-added-name'); if(n) n.textContent=btns.length+(btns.length===1?' in-stock item':' in-stock items')+' from your wishlist';
  });
})();'''

if __name__ == "__main__":
    page_search(); page_blog(); page_article(); page_wishlist()
