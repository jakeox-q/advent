# Advent Games home page design draft.
import os
from common import *

# ------------------------------------------------------------------ data (sample products from the current catalogue; BGG figures illustrative)
JUST = [
    card("wingspan-pocket", "Wingspan Pocket", "Stonemaier Games", "32.95", "in", "Just arrived", meta=("1-2", "20-40 min", "10+", "1.8"), year="2026", rating="7.6"),
    card("old-kings-crown", "The Old King's Crown", "Eerie Idol Games", "134.95", "in", "Just arrived", meta=("1-4", "60-120 min", "12+", "3.2"), link="product.html", year="2025", rating="8.1"),
    card("abroad", "Abroad", "Allplay", "109.95", "in", "Just arrived", meta=("1-4", "90-120 min", "14+", "3.4"), year="2026", rating="7.9"),
    card("akropolis-pantheon", "Akropolis: Pantheon", "Gigamic", "22.95", "in", "Just arrived", exp=True, meta=("2-4", "30 min", "8+", "1.8"), year="2025", rating="7.6"),
    card("harmonies-crescendo", "Harmonies: Crescendo", "Libellud", "26.95", "in", "Back in stock", exp=True, meta=("1-4", "30-45 min", "10+", "2.0"), year="2025", rating="7.8"),
    card("compile-aux-3", "Compile: Aux 3", "Greater Than Games", "9.95", "in", "Just arrived", exp=True, meta=("2", "20-30 min", "14+", "2.1"), year="2026"),
]
PRE = [
    card("8-dragons", "8 Dragons", "Capstone Games", "110.95", "pre", "Preorder", meta=("1-4", "60-90 min", "14+", "3.0"), year="2026"),
    card("1848", "1848: The Springtime of Nations", "Phalanx", "118.95", "pre", "Preorder", rrp="140", meta=("2-4", "120-180 min", "14+", "3.6"), year="2026"),
    card("aberration", "Aberration", "Deepwater Games", "127.95", "pre", "Preorder", meta=("1-4", "90-150 min", "14+", "3.3"), year="2026"),
    card("arribada", "Arribada", "Devir Games", "59.95", "pre", "Preorder", meta=("2-4", "45-60 min", "10+", "2.2"), year="2026"),
    card("accuse", "Accuse!", "Hub Games", "34.95", "pre", "Preorder", meta=("3-6", "30 min", "10+", "1.6"), year="2026"),
]
COMING = [
    card("age-of-innovation", "Age of Innovation: Future &amp; Past", "Capstone Games", "74.95", "soon", "Coming soon", exp=True, eta="Nov 2026", meta=("1-5", "40-150 min", "14+", "3.9"), year="2026"),
    card("forest-shuffle-dartmoor", "Forest Shuffle: Dartmoor - Exmoor", "Lookout Spiele", "29.95", "soon", "Coming soon", exp=True, eta="Nov 2026", meta=("2-5", "40-60 min", "10+", "2.0"), year="2026"),
    card("euphoria", "Euphoria (Essential Edition)", "Stonemaier Games", "69.95", "soon", "Coming soon", eta="Nov 2026", meta=("2-6", "60 min", "13+", "2.2"), year="2026"),
    card("dorfromantik-south-seas", "Dorfromantik: The South Seas", "Pegasus Spiele", "44.95", "soon", "Coming soon", exp=True, eta="Dec 2026", meta=("1-6", "30-60 min", "8+", "1.6"), year="2026"),
    card("courage", "Courage: An Everdell Journeys Expansion", "Starling Games", "84.95", "soon", "Coming soon", rrp="100", eta="Feb 2027", exp=True, meta=("1-4", "40-80 min", "10+", "2.4"), year="2027"),
    card("gettysburg", "Three Days of Gettysburg: Deluxe Edition", "GMT Games", "169.95", "soon", "Coming soon", eta="Mar 2027", meta=("1-2", "2 hrs+", "14+", "3.7"), year="2024", rating="8.2"),
]
BEST = [
    card("carcassonne", "Carcassonne", "Hans im Glück", "58.95", "in", meta=("2-5", "30-45 min", "7+", "1.9"), year="2000", rating="7.4"),
    card("camel-up", "Camel Up (Second Edition)", "Pretzel Games", "76.95", "in", meta=("3-8", "30-45 min", "8+", "1.5"), year="2018", rating="7.5"),
    card("pandemic", "Pandemic", "Z-Man Games", "59.95", "sup", meta=("2-4", "45 min", "8+", "2.4"), year="2008", rating="7.5"),
    card("king-of-tokyo", "King of Tokyo (Second Edition)", "IELLO", "59.95", "in", "Sale", rrp="70.00", meta=("2-6", "30 min", "8+", "1.5"), year="2016", rating="7.1"),
    card("sushi-go-party", "Sushi Go Party!", "Gamewright", "49.95", "in", meta=("2-8", "20 min", "8+", "1.3"), year="2016", rating="7.3"),
    card("power-grid", "Power Grid (Recharged)", "Rio Grande Games", "84.95", "in", meta=("2-6", "120 min", "12+", "3.3"), year="2019", rating="7.8"),
]
PICKS = [
    card("great-harbor", "The Great Harbor", "Archona Games", "84.95", "in", meta=("1-4", "60-90 min", "12+", "2.7"), year="2025", rating="7.7",
         note="Tight little port-builder with a clever tide track. Out of the box and on the table in ten minutes. <mark>[Dean to write]</mark>"),
    card("gettysburg", "Three Days of Gettysburg: Deluxe Edition", "GMT Games", "169.95", "in", meta=("1-2", "2 hrs+", "14+", "3.7"), year="2024", rating="8.2",
         note="The one we keep going back to on Tuesday nights. Big map, no fiddly chits. <mark>[Dean to write]</mark>"),
    card("ravenloft", "D&amp;D: Castle Ravenloft", "Wizards of the Coast", "99.95", "sup", meta=("1-5", "60 min", "12+", "2.4"), year="2010", rating="6.8",
         note="Best co-op dungeon crawl for a table that has never played one. <mark>[Dean to write]</mark>"),
    card("drizzt", "D&amp;D: The Legend of Drizzt", "Wizards of the Coast", "99.95", "in", meta=("1-5", "60 min", "12+", "2.4"), year="2011", rating="7.0",
         note="Plays solo as well as it does with five. Pairs with Ravenloft if you want a campaign. <mark>[Dean to write]</mark>"),
]
TYPES = [("Strategy", "blue", "Euros, engine builders, heavy thinkers", "mind"), ("Family", "sun", "Easy to learn, fun for everyone", "family"), ("Party", "orange", "Big groups, big laughs", "balloon"), ("Thematic", "sky", "Story first, dice second", "book"),
         ("Wargames", "muted", "Hex and counter to block wars", "tank"), ("Solo games", "orange", "Plays well with one", "dice"), ("Two-player", "sky", "Head to head", "duel"), ("Kids", "green", "Ages 4 and up", "blocks")]
PUBS = [("GMT Games","gmt.png"), ("Stonemaier Games","stonemaier.png"), ("Lookout Spiele","lookout.png"), ("Czech Games Edition","cge.svg"), ("Days of Wonder","daysofwonder.png"), ("Capstone Games","capstone.png"), ("Pegasus Spiele","pegasus.svg"), ("Rio Grande Games","riogrande.svg")]

MAIN = f'''<!-- ============ HERO ============ -->
<section class="sec hero-sec">{tag("Promo grid", "tweak", "1 large + 2 small static tiles · native image + text panel on the large tile · small tiles: colour fill with box art bleeding off the edge (CSS tweak)")}
<div class="inner hero">
  <a class="tile tile-lg" href="#">
    <img class="tile-bg" src="img/hero-bg.jpg" alt="">
    <img class="tile-bg tile-bg--sale" src="img/sale-bg.jpg" alt="">
    <div class="tile-panel hero-launch">
      <span class="eyebrow">New site, same Dean</span>
      <h1 class="display">Welcome to the new look Advent Games!</h1>
      <p class="body-lg">Same friendly service, a much easier way to find your next game. Filter 11,000+ games by players, play time, complexity, categories, mechanics, designers, and much more!</p>
      <span class="ag-btn ag-btn--primary">Read the blog post</span>
    </div>
    <span class="sale-ribbon" aria-hidden="true">Sale on</span>
    <div class="tile-panel hero-sale">
      <span class="sale-pill">{I("star",14)} Up to 40% off <em>· 26 Dec to 5 Jan</em></span>
      <h1 class="display">Boxing Day sale is on</h1>
      <p class="body-lg">Up to 40% off selected games, expansions and accessories. While stocks last.</p>
      <span class="ag-btn ag-btn--primary">Shop the sale</span>
    </div>
  </a>
  <a class="tile tile-sm tile-sun" href="#">
    <div class="tile-copy"><span class="eyebrow">This week</span><h2 class="h3">Just arrived</h2><span class="tile-link">See what's new {I("right",14)}</span></div>
    <img class="tile-art" src="img/abroad.jpg" alt="" aria-hidden="true">
  </a>
  <a class="tile tile-sm tile-subtle" href="#">
    <div class="tile-copy"><span class="eyebrow">Reserve now</span><h2 class="h3">Preorders open</h2><span class="tile-link">The big December releases {I("right",14)}</span></div>
    <img class="tile-art" src="img/8-dragons.jpg" alt="" aria-hidden="true">
  </a>
</div></section>

<!-- ============ FIND YOUR NEXT GAME ============ -->
<section class="sec">{tag("Collection list", "tweak", "8 smart collections · grid 4 across · no images: coloured text tiles (CSS tweak so Dean never has to pick hero images)")}
<div class="inner">
  {sec_head("Find your next game", "Browse by the way you like to play.")}
  <div class="types">{"".join(f'<a class="type type--{c}" href="#">{I(ic,150,"type-icon")}<span class="type-name">{n}</span><span class="type-sub">{d} {I("right",14)}</span></a>' for n, c, d, ic in TYPES)}</div>
</div></section>

<!-- ============ JUST ARRIVED ============ -->
<section class="sec">{tag("Featured collection", "native", "carousel · collection: Just Arrived · ordered by advent.arrived_at · Dean's #1 browse path")}
<div class="inner">
  {sec_head("Just arrived", "Fresh off the truck and ready to ship from Sydney.", "#")}
  {carousel(JUST)}
</div></section>

<!-- ============ NEW TO PREORDER ============ -->
<section class="sec band">{tag("Featured collection", "native", "carousel · collection: New to Preorder (no due date yet) · surface-subtle band")}
<div class="inner">
  {sec_head("New to preorder", "Charged now, shipped the day they land. Cancel any time before they leave our supplier.", "#", "All preorders")}
  {carousel(PRE)}
</div></section>

<!-- ============ COMING SOON ============ -->
<section class="sec">{tag("Featured collection", "native", "carousel · collection: Coming soon (titles with a supplier due date) · same card, shows Expected month")}
<div class="inner">
  {sec_head("Coming soon", "On the way from our suppliers, with a due date. Preorder now to lock in your copy.", "#", "All coming soon")}
  {carousel(COMING)}
</div></section>

<!-- ============ BEST SELLERS ============ -->
<section class="sec">{tag("Featured collection", "native", "carousel · collection: Best sellers (automated, best-selling sort)")}
<div class="inner">
  {sec_head("Best sellers", "The games our customers keep coming back for.", "#")}
  {carousel(BEST)}
</div></section>

<!-- ============ STAFF RECOMMENDATIONS ============ -->
<section class="sec band band--sun">{tag("Product list", "tweak", "manual Staff picks · colour scheme: sun tint · card tweak shows advent.staff_note inside each card · note hides when empty")}
<div class="inner">
  {sec_head("Staff recommendations", "What have we been playing this week?", "#", "All staff picks")}
  <div class="picks">{"".join(PICKS)}</div>
</div></section>

<!-- ============ NEW TO BOARD GAMES ============ -->
<section class="sec">{tag("Media with text", "native", "image left, text right · buttons go to Gateway, Family and Two-player smart collections")}
<div class="inner mwt">
  <div class="mwt-media photo"><img src="img/beginners.jpg" alt="Hands moving pieces on a board game"></div>
  <div class="mwt-copy">
    <span class="eyebrow">Start here</span>
    <h2 class="h2">New to board games?</h2>
    <p class="body-lg">Every journey begins with a single step, and these collections will set you on the Board Game path. These games provide a strong base for learning essential board game mechanics, and are great fun for nearly all ages!</p>
    <div class="btn-row"><a class="ag-btn ag-btn--primary" href="#">Gateway games</a><a class="ag-btn ag-btn--secondary" href="#">Family games</a><a class="ag-btn ag-btn--secondary" href="#">Two-player</a></div>
  </div>
</div></section>

<!-- ============ GIFT CARDS ============ -->
<section class="sec">{tag("Media with text", "native", "text left, image right · links to the native Shopify gift card product")}
<div class="inner mwt mwt-rev">
  <div class="mwt-copy">
    <span class="eyebrow">Gift cards</span>
    <h2 class="h2">Can't pick for them? Let them pick.</h2>
    <p class="body-lg">Advent Games gift cards are digital, land in their inbox straight away, and work on every game, expansion and preorder on the site. <mark>[Dean to confirm copy]</mark></p>
    <div class="btn-row"><a class="ag-btn ag-btn--primary" href="#">Buy a gift card</a></div>
  </div>
  <div class="mwt-media photo"><img src="img/giftcard-email.jpg" alt="Advent Games digital gift card arriving by email on a phone"></div>
</div></section>

<!-- ============ SEASONAL CAMPAIGN ============ -->
<section class="sec">{tag("Image banner", "tweak", "one seasonal campaign slot · same treatment as the sale hero: uploaded background image, text panel, offer pill, corner ribbon (ribbon = CSS tweak) · optional Countdown timer section")}
<div class="inner">
  <div class="campaign">
    <img class="campaign-bg" src="img/sale-bg.jpg" alt="">
    <span class="sale-ribbon" aria-hidden="true">Sale on</span>
    <div class="campaign-panel">
      <span class="sale-pill">{I("star",14)} Up to 40% off <em>· 26 Dec to 5 Jan</em></span>
      <h2 class="h1">Boxing Day sale starts 26 December</h2>
      <p class="body-lg">Up to 40% off selected games, expansions and accessories. While stocks last.</p>
      <div class="btn-row"><a class="ag-btn ag-btn--primary" href="#">Set a reminder</a><a class="ag-btn ag-btn--secondary" href="#">See last year's picks</a></div>
    </div>
  </div>
</div></section>

<!-- ============ SHOP BY PUBLISHER ============ -->
<section class="sec">{tag("Logo list", "native", "8 publisher logos linking to vendor collections · logos from publisher sites · full colour (greyscale option available)")}
<div class="inner">
  {sec_head("Shop by publisher", "", "#", "All brands A-Z")}
  <div class="logos">{"".join((f'<a class="logo-tile logo-tile--img" href="#" title="{p}"><img src="img/pub/{f}" alt="{p}"></a>' if f else f'<a class="logo-tile" href="#"><span>{p}</span></a>') for p,f in PUBS)}</div>
</div></section>

<!-- ============ BRAND STORY ============ -->
<section class="sec band band--story">{tag("Media with text", "tweak", "image left, text right · colour scheme: brand-blue tint · floating game-piece icons added via section background (CSS/SVG, decorative)")}
<div class="story-float" aria-hidden="true">
  {I("dice",120,"sf sf-1")}{I("meeple",96,"sf sf-2")}{I("crown",84,"sf sf-3")}{I("d20",110,"sf sf-4")}{I("puzzle",90,"sf sf-5")}{I("meeple",64,"sf sf-6")}{I("dice",72,"sf sf-7")}
</div>
<div class="inner mwt">
  <div class="mwt-media photo"><img src="img/story.jpg" alt="Torvi the staffy watching a game of Lost Cities on the deck"></div>
  <div class="mwt-copy">
    <span class="eyebrow">About Advent Games</span>
    <h2 class="h2">Your friendly, local, online board game store</h2>
    <p class="body-lg">Owner-operated in Sydney since 2012, with a huge range, fair prices and the hard-to-find games other stores don't carry. Ask about a game, a preorder or an order you've already placed and you'll hear back from Dean, not an AI response.</p>
    <div class="btn-row"><a class="ag-btn ag-btn--primary" href="#">Our story</a><a class="ag-btn ag-btn--secondary" href="#">Pickup &amp; shipping</a></div>
  </div>
</div></section>

<!-- ============ GOOGLE REVIEWS ============ -->
<section class="sec">{tag("Apps · Google Reviews", "custom", "app block (in scope) · 3 latest reviews · Leave a review link to the Google review form")}
<div class="inner">
  {sec_head("What our customers say", "Live from Google. Example reviews shown.", "#", "Leave us a review", eyebrow="Reviews")}
  <div class="reviews-wrap"><div class="reviews">
    <blockquote class="review"><div class="stars">{star()*5}</div><p>"Ordered Monday night, arrived Wednesday. Dean emailed to check I knew the expansion needed the base game. That's service."</p><footer>Example reviewer · Google</footer></blockquote>
    <blockquote class="review"><div class="stars">{star()*5}</div><p>"Best range of wargames in Australia and the preorder pricing beats everyone else I've found."</p><footer>Example reviewer · Google</footer></blockquote>
    <blockquote class="review"><div class="stars">{star()*5}</div><p>"Picked up at Chatswood on Tuesday night and got a game recommendation thrown in. Will be back."</p><footer>Example reviewer · Google</footer></blockquote>
  </div><div class="car-nav rev-nav"><button class="car-btn" aria-label="Previous">{I("left",18)}</button><button class="car-btn" aria-label="Next">{I("right",18)}</button></div></div>
</div></section>'''

HERO_TOGGLE = '''<div class="wf-toggle" role="group" aria-label="Hero variant"><span class="wf-lbl">Hero:</span><button type="button" data-hero="launch" aria-pressed="true">Launch</button><button type="button" data-hero="sale" aria-pressed="false">Boxing Day sale</button></div>'''

if __name__ == "__main__":
    render("index.html", "Advent Games Home", "Home design v2", "Enterprise theme · desktop draft · 1590px page width", MAIN, HERO_TOGGLE)
