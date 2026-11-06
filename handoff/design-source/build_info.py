# Advent Games: Brands A-Z, Brand collection, About + Contact, Help & FAQ design drafts (per wireframes v1).
from common import *
import build_home
from build_pages import crumbs, banner, collection_body, applied, avail_group, price_group, fgroup, flist, chk, recently_viewed, RECENT, RPG, PAGE_JS, BRAND_STORY, G

def sec(name, kind, note, body, cls="sec", sid=""):
    i = f' id="{sid}"' if sid else ""
    return f'<section class="{cls}"{i}>{tag(name, kind, note)}\n{body}</section>\n'

def flag(txt):
    return f'<div class="flag">{I("chat",16)}<span><b>For Jake:</b> {txt}</span></div>'

# ================================================================ BRANDS A-Z
BRANDS = {
 "#": ["1-More-Time Games", "25th Century Games"],
 "A": ["Abacusspiele", "Academy Games", "Aetherworks", "Alderac (AEG)", "Allplay", "Archona Games", "Arcane Wonders", "Ares Games", "Asmodee", "Awaken Realms"],
 "B": ["Bezier Games", "Blue Orange", "Board &amp; Dice", "Bitewing Games", "Bombyx"],
 "C": ["Capstone Games", "Catan Studio", "Chaosium", "CMON", "Compass Games", "Cephalofair", "Czech Games Edition"],
 "D": ["Days of Wonder", "Deep Water Games", "Devir", "Dire Wolf"],
 "E": ["Edge Studio", "Eerie Idol Games", "Eagle-Gryphon Games", "Eggertspiele"],
 "F": ["Fantasy Flight Games", "Feuerland", "Floodgate Games", "Folded Space", "Free League", "Funforge"],
 "G": ["Gamegenic", "Gamewright", "Garphill Games", "GMT Games", "Greater Than Games", "Grey Fox Games"],
 "H": ["Hans im Glück", "Horrible Guild", "Hurrican"],
 "I": ["IELLO", "Indie Boards &amp; Cards", "Inside Up Games"],
 "J": ["Japanime Games"],
 "K": ["Kosmos", "KTBG"],
 "L": ["Leder Games", "Libellud", "Lookout Spiele", "Lucky Duck Games"],
 "M": ["Magpie Games", "Matagot", "Mayday Games", "Mindclash", "Modiphius"],
 "N": ["Next Move Games", "North Star Games"],
 "O": ["Osprey Games"],
 "P": ["Paizo", "Pandasaurus", "Pegasus Spiele", "Plan B Games", "Portal Games"],
 "Q": ["Queen Games"],
 "R": ["Ravensburger", "Red Raven Games", "Renegade Game Studios", "Repos Production", "Rio Grande Games", "Roxley"],
 "S": ["Space Cowboys", "Splotter", "Steamforged Games", "Stonemaier Games", "Strohmann Games"],
 "T": ["Thames &amp; Kosmos", "Thunderworks Games", "Tasty Minstrel"],
 "U": ["Ultra Pro", "Unexpected Games"],
 "V": ["Victory Point Games"],
 "W": ["Wizards of the Coast", "WizKids"],
 "Y": ["Yochai Gal"],
 "Z": ["Z-Man Games", "Zoch Verlag"],
}
LETTERS = ["#"] + [chr(c) for c in range(65, 91)]

def page_brands():
    jump = "".join((f'<a href="#az-{"num" if L == "#" else L}">{L}</a>' if L in BRANDS else f'<span aria-disabled="true">{L}</span>') for L in LETTERS)
    lists = "".join(f'<div class="az-group" id="az-{"num" if L == "#" else L}"><h2 class="az-letter">{L}</h2><ul>' + "".join(f'<li><a href="brand.html">{n}</a></li>' for n in ns) + '</ul></div>' for L, ns in BRANDS.items())
    logos = "".join(f'<a class="logo-tile logo-tile--img" href="brand.html" title="{p}"><img src="img/pub/{f}" alt="{p}"></a>' for p, f in build_home.PUBS)
    main = (crumbs(("Home", "index.html"), ("Brands", None))
        + sec("Rich text", "native", "page.brands template · title + one-line intro", '<div class="inner page-title"><h1>Brands A-Z</h1><p>Over 800 publishers, from Abacusspiele to Zoch Verlag. Pick a brand to see everything we stock from them.</p></div>', cls="sec sec--tight")
        + sec("Logo list", "native", "featured publishers, hand-picked by Dean · same section as the home page", f'<div class="inner">{sec_head("Featured publishers")}<div class="logos">{logos}</div></div>', cls="sec sec--tight")
        + sec("Jump to letter", "tweak", "letter anchors · Custom Liquid that reads the same brands menu, so letters with no brands grey out automatically · sticks under the header on scroll",
              f'<div class="inner"><nav class="az-bar" aria-label="Jump to letter">{jump}</nav></div>', cls="az-sticky")
        + sec("Link list", "native", "one list per letter · each name links to a vendor smart collection (rule: vendor = X) · the import script creates these collections and the menu, so Dean doesn't maintain 800 links by hand",
              f'<div class="inner"><div class="az-grid">{lists}</div><p class="az-foot">Can\'t see a publisher? <a href="about.html#contact">Ask us</a>, we can usually order it in.</p></div>', cls="sec")
    )
    render("brands.html", "Brands A-Z · Advent Games", "Brands A-Z", "page.brands.json", main, extra_js=AZ_JS)

AZ_JS = r'''
(function(){var bar=document.querySelector('.az-bar'); if(!bar) return;
  var links=bar.querySelectorAll('a'), groups=document.querySelectorAll('.az-group');
  function spy(){var y=window.scrollY+220, cur=null; groups.forEach(function(g){if(g.offsetTop<=y) cur=g.id;}); links.forEach(function(a){a.classList.toggle('on',a.getAttribute('href')==='#'+cur);});}
  window.addEventListener('scroll',spy,{passive:true}); spy();
})();'''

# ================================================================ BRAND (vendor collection)
def page_brand():
    fl = [p for p in RPG if p["vendor"] == "Free League"]
    groups = [avail_group(checked=(), counts=("52", "6", "6")), price_group("0", "200"),
              fgroup("RPG system", flist("Search systems...", [("ALIEN", "24"), ("Blade Runner", "12"), ("Dragonbane", "9"), ("Forbidden Lands", "8"), ("Mutant: Year Zero", "6"), ("Vaesen", "5")])),
              fgroup("Category", "".join(chk(n, c) for n, c in [("Core rulebook", "8"), ("Starter set", "5"), ("Adventure", "21"), ("Sourcebook", "17"), ("GM screen", "6"), ("Dice &amp; accessories", "7")]))]
    feat = [card(p["img"], p["title"], p["vendor"], p["price"], p["state"], p.get("badge", ""), line=p["line"], link="product-rpg.html") for p in fl]
    main = (crumbs(("Home", "index.html"), ("Brands", "brands.html"), ("Free League", None))
        + banner("Free League", "64", "Swedish publisher behind the ALIEN, Blade Runner and Dragonbane roleplaying games, known for gorgeous books and the Year Zero Engine.", note="collection.json (vendor collection) · Enterprise banner, title + count + vendor description · no image")
        + f'<section class="sec sec--tight">{tag("Featured collection", "native", "optional · best sellers from this brand · Dean can switch it off per brand")}<div class="inner">{sec_head("Best sellers from Free League", link="#", link_label="View all")}{carousel(feat, cols=5)}</div></section>'
        + f'<section class="coll-sec">{tag("Collection products", "native", "same collection template · Publisher filter hidden automatically (Search &amp; Discovery hides single-value filters) · no filters applied, so Applied filters does not show")}'
        + collection_body(fl, None, groups, "64", 0) + '</section>'
        + recently_viewed(RECENT))
    render("brand.html", "Free League · Advent Games", "Brand collection", "collection.json (vendor) · every brand uses the standard collection template", main, extra_js=PAGE_JS)

# ================================================================ ABOUT + CONTACT
VALUES = [("chat", "Owner-operated", "Questions answered promptly by Dean, not a call centre."),
          ("box", "Huge range", "11,000+ games, preorders and the hard-to-find titles."),
          ("truck", "Fast, careful delivery", "Tracked AusPost eParcel, boxed and padded."),
          ("shield", "Fair prices", "Flat-rate shipping, free on orders over $300.")]

def page_about():
    vals = "".join(f'<div class="val"><span class="val-ic">{I(ic,26)}</span><h3 class="h4">{t}</h3><p>{d}</p></div>' for ic, t, d in VALUES)
    main = (crumbs(("Home", "index.html"), ("About us", None))
        + sec("Image banner", "native", "page.about · tagline from Dean (replaces 'Where Play Comes Alive') · photo to come from Dean", f'''<div class="inner"><div class="about-hero"><img src="img/hero-bg.jpg" alt="">
  <div class="about-hero__c"><span class="eyebrow">About Advent Games</span><h1 class="display">Your friendly, local, online board game store</h1><p class="body-lg">Owner-operated in Sydney, shipping Australia-wide.</p></div></div></div>''', cls="sec sec--tight")
        + sec("Image with text", "native", "our story · copy from the current About Us and Why Buy From Us pages (Dean refines)", f'''<div class="inner"><div class="mwt">
  <div class="mwt-media"><div class="photo"><img src="img/story.jpg" alt=""></div></div>
  <div class="mwt-copy"><span class="eyebrow">Our story</span><h2 class="h2">Integrity, great service and a huge range</h2>
  <p class="body-lg">We're an Australian online board game store based in Sydney. We keep prices fair by running a lean operation and passing the savings on, and we go out of our way to find the hard-to-find games.</p>
  <p class="body-lg">You're not just a customer: we see you as a friend who shares our passion for the hobby.</p>
  <p class="bgg-line"><img src="img/powered-by-bgg.png" alt="BoardGameGeek" class="bgg-mini"> Find Dean on BoardGameGeek: <a href="#">Caldris</a></p></div></div></div>''')
        + sec("Image with text", "native", "meet Dean · text left, photo right · draft copy from what we know (current About, Why Buy From Us and Pick Up pages), Dean to check and add when he started", f'''<div class="inner"><div class="mwt dean">
  <div class="mwt-copy"><span class="eyebrow">Meet Dean</span><h2 class="h2">The person behind the parcels</h2>
  <p class="body-lg">Advent Games is run by Dean, a Sydney board gamer who wanted Australian players to get great games at fair prices, without the hunt. You'll find him on BoardGameGeek as Caldris, and on Tuesday nights at the Northside Gamers Group in Chatswood, which is where our free pickups happen.</p>
  <p class="body-lg">What began as a small online shop has grown into a range of more than 11,000 games, from family favourites to heavy euros, wargames and roleplaying books. We still go out of our way to track down the hard-to-find titles, and we open preorders early so you don't miss the big releases.</p>
  <p class="body-lg">We're still small and owner-operated. When you get in touch, Dean replies himself: not a call centre, and not an AI.</p></div>
  <div class="mwt-media"><div class="photo dean-photo"><img src="img/dean.jpg" alt="Dean from Advent Games at a games convention"></div></div>
</div>{flag("draft copy written from the facts we have, no invented history. Dean to check it and add when Advent started (footer says 2013, not confirmed). Photo is a stand-in (Dean with a designer at a convention); Dean likely has a better portrait.")}</div>''', cls="sec sec--tint")
        + sec("Multicolumn", "native", "why buy from us · icons + short lines, current Why Buy From Us page condensed", f'<div class="inner">{sec_head("Why buy from Advent")}<div class="vals">{vals}</div></div>')
        + sec("Image with text", "native", "community + pickup · details from the current Pick Up page", f'''<div class="inner"><div class="pickup">
  <div class="pickup-copy"><span class="eyebrow">Free pickup</span><h2 class="h2">Pick up in Chatswood</h2><p class="body-lg">Skip the shipping. Collect your order free on Tuesday nights at the Northside Gamers Group in Chatswood, a friendly weekly games night. We'll confirm your pickup by email.</p>
  <a class="ag-btn ag-btn--primary" href="help.html#pickup">Pickup details</a></div>
  <div class="pickup-card"><div class="pickup-row">{I("calendar",22)}<div><strong>Tuesday nights</strong><span>Orders placed Monday or Tuesday are ready the following week</span></div></div>
  <div class="pickup-row">{I("map",22)}<div><strong>Northside Gamers Group</strong><span>Chatswood, NSW</span></div></div>
  <div class="pickup-row">{I("mail",22)}<div><strong>Confirmed by email</strong><span>Choose Local pickup at checkout</span></div></div></div>
  </div>{flag("venue and time differ between the current pages (Chatswood RSL, 446 Victoria Ave, 6-9pm vs The Chatswood Club, 11 Help St, 6:30-9pm). Confirm with Dean before we add the address. A games night photo would replace the details card if Dean has one.")}</div>''', cls="sec sec--sky")
        + sec("Contact form", "native", "Shopify contact form + details column (multicolumn) · special orders welcome", f'''<div class="inner"><div class="contact">
  <form class="contact-form" onsubmit="return false"><h2 class="h2">Get in touch</h2><p class="sub">Questions, special orders or something you can't find. Dean usually replies within a business day.</p>
    <div class="cf-row"><label>Name<input class="ag-input" type="text" autocomplete="name"></label><label>Email<input class="ag-input" type="email" autocomplete="email"></label></div>
    <label><span>Order number <span class="opt">(optional)</span></span><input class="ag-input" type="text" placeholder="#10482"></label>
    <label>Message<textarea class="ag-input" rows="5" placeholder="Special orders welcome: tell us what you're looking for."></textarea></label>
    <button class="ag-btn ag-btn--orange">Send message</button></form>
  <aside class="contact-card"><h3 class="h4">Advent Games</h3>
    <ul><li>{I("map",18)}<span>Online store, Sydney NSW</span></li><li>{I("mail",18)}<a href="#">dean@adventgames.com.au</a></li><li>{I("chat",18)}<a href="#">0411 017 162</a></li><li>{I("shield",18)}<span>ABN 76 649 386 212</span></li></ul>
    <div class="contact-note"><strong>Can't find a game?</strong><p>We source games from around the world. Ask us.</p></div>
    <a class="contact-faq" href="help.html">Check our Help &amp; FAQ first {I("right",14)}</a></aside>
</div></div>''', sid="contact")
    )
    render("about.html", "About us · Advent Games", "About + Contact", "page.about.json", main)

# ================================================================ HELP & FAQ
HELP = [
 ("Shipping", "shipping", "truck", [
   ("How much is shipping?", "<p>$10 to Sydney Metro, Gosford and Wollongong. $15 to the rest of Australia. <b>Free on orders over $300.</b></p>"),
   ("When will I receive my order?", "<p>In-stock games are dispatched in 1-3 business days. Games we order in from our supplier ship in 2-7 business days. Delivery time after that depends on AusPost.</p>"),
   ("Can I track my parcel?", "<p>Yes. Every order goes by Australia Post eParcel with tracking. You'll get the tracking link by email when it ships.</p>"),
   ("Do you ship overseas?", "<p>We ship within Australia only. For overseas orders, email us for a quote.</p>"),
   ("What if I'm not home?", "<p>AusPost will leave a card and hold the parcel at your local post office, or you can deliver to a Parcel Locker. Uncollected parcels returned to us incur a $13.43 return fee plus reshipping.</p>")]),
 ("Pickup", "pickup", "map", [
   ("Can I pick up my order?", "<p>Yes, free. Choose Local pickup at checkout and collect on Tuesday night at the Northside Gamers Group in Chatswood.</p>"),
   ("When will my pickup be ready?", "<p>Orders placed on a Monday or Tuesday are ready the following Tuesday. We confirm by email.</p>")]),
 ("Preorders &amp; special orders", "preorders", "calendar", [
   ("When is my preorder due?", "<p>Each preorder shows its expected month. Dates come from the publisher and can move; we update the product page if they do.</p>"),
   ("When am I charged?", "<p>At purchase, usually at a discounted preorder price.</p>"),
   ("Will my in-stock items wait for my preorder?", "<p>Yes. In-stock items in the same order are held and shipped together when the preorder arrives. If you'd like them sooner, place them as a separate order.</p>"),
   ("Can I cancel a preorder?", "<p>Yes, any time until the stock ships from our supplier. Email us and we'll refund you.</p>"),
   ("Can you order a game you don't stock?", "<p>Often, yes. We source games from around the world. <a href=\"about.html#contact\">Tell us what you're after.</a></p>")]),
 ("Orders", "orders", "box", [
   ("Do I need an account to buy?", "<p>No. You can check out as a guest. An account lets you see past orders and reorder quickly.</p>"),
   ("How do I check my order status?", "<p>Use the link in your order confirmation email, or sign in to your account and open Orders.</p>"),
   ("Can I add items to an order that hasn't shipped?", "<p>Yes. Place a new order, choose the Order additions shipping option and note the order number to combine with. If the combined total passes $300, we refund the shipping.</p>")]),
 ("Returns &amp; damages", "returns", "shield", [
   ("My parcel arrived damaged", "<p>Note the damage when you receive it and email us with photos. We'll replace the item, or give you a credit or refund.</p>"),
   ("Can I return an unopened game?", "<p>Yes, for change of mind: let us know in writing within 7 days. The game must be unopened and in its original packaging. Preorders, special orders, sleeves and accessories are excluded. We offer an exchange or store credit.</p>"),
   ("How do I start a return?", "<p>Email us for a Return Product Number (RPN) before sending anything back.</p>")]),
 ("Payments", "payments", "lock", [
   ("What payment methods do you accept?", "<p>Visa, Mastercard, PayPal, Apple Pay and Google Pay. All prices are in AUD.</p>"),
   ("How does bank transfer work?", "<p>Choose bank transfer at checkout and use your order number as the reference. We ship once payment arrives. Unpaid orders are cancelled after 3 business days.</p>")]),
 ("Our games", "games", "dice", [
   ("How is a game's Complexity rating determined?", "<p>Complexity ratings on product pages come from BoardGameGeek, the hobby's main source of discussion and knowledge. Games are rated out of 5: 1 is very light and easy to learn, 5 is highly complex. Ratings are submitted by players, so they're subjective and change over time, but they're a good guide to how heavy a game will feel.</p>"),
   ("Which edition is this game?", "<p>English retail editions unless tagged otherwise. German editions, Kickstarter editions (KS) and Deluxe editions (DELUXE) are marked in the title.</p>"),
   ("Why are board games expensive in Australia?", "<p><span class=\"ph-inline\">Dean to write</span></p>")]),
]

def page_help():
    pills = "".join(f'<a href="#{a}">{I(ic,16)}{t}</a>' for t, a, ic, _ in HELP)
    groups = "".join(f'''<div class="help-group" id="{a}"><h2 class="h3">{I(ic,22)}{t}</h2><div class="acc">''' + "".join(f'<details{" open" if i == 0 else ""}><summary>{q} {I("chev",18)}</summary><div class="ab">{ans}</div></details>' for i, (q, ans) in enumerate(qs)) + '</div></div>' for t, a, ic, qs in HELP)
    main = (crumbs(("Home", "index.html"), ("Help &amp; FAQ", None))
        + sec("Rich text", "native", "page.help · title + intro", '<div class="inner page-title"><h1>Help &amp; FAQ</h1><p>Shipping, pickup, preorders, returns and payments. Can\'t find your answer? <a href="about.html#contact">Contact Dean</a>.</p></div>', cls="sec sec--tight")
        + sec("Quick links", "tweak", "jump to anchors · rich text buttons, stick under the header on scroll", f'<div class="inner"><nav class="help-pills" aria-label="Help topics">{pills}</nav></div>', cls="help-sticky")
        + sec("FAQ", "native", "one Enterprise FAQ section per topic · answers live in one shared FAQ so product page accordions and the cart use the same copy · current site's FAQ, Shipping, Pick Up, Pre-Orders, Returns and Payment pages regrouped",
              f'<div class="inner help-wrap">{groups}{flag("full policies (Shipping, Returns, Pre-orders &amp; special orders, Payments, Privacy, Terms) stay as Shopify policy pages, linked from the footer. Open questions for Dean: pickup venue and time, supplier dispatch window (2-7 or 3-5 days), and whether bank transfer stays. Payment methods assume Shopify Payments + PayPal.")}</div>')
        + sec("Image banner", "native", "contact CTA", f'''<div class="inner"><div class="help-cta"><div><h2 class="h2">Still stuck?</h2><p class="body-lg">Dean answers every message himself, usually within a business day.</p></div>
  <div class="help-cta__btns"><a class="ag-btn ag-btn--orange" href="about.html#contact">Contact Dean</a><a class="ag-btn ag-btn--secondary" href="#">dean@adventgames.com.au</a></div></div></div>''')
    )
    render("help.html", "Help & FAQ · Advent Games", "Help & FAQ", "page.help.json", main, extra_js=HELP_JS)

HELP_JS = r'''
(function(){var bar=document.querySelector('.help-pills'); if(!bar) return;
  var links=bar.querySelectorAll('a'), groups=document.querySelectorAll('.help-group');
  function spy(){var y=window.scrollY+240, cur=null; groups.forEach(function(g){if(g.offsetTop<=y) cur=g.id;}); links.forEach(function(a){a.classList.toggle('on',a.getAttribute('href')==='#'+cur);});}
  window.addEventListener('scroll',spy,{passive:true}); spy();
})();'''

if __name__ == "__main__":
    page_brands(); page_brand(); page_about(); page_help()
