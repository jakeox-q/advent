import json, re, os
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "out"); os.makedirs(OUT, exist_ok=True)

# ---------------- settings_data.json: start from the Enterprise preset, override with the Advent design system
sd = json.loads(re.sub(r'^/\*.*?\*/\s*', '', open(os.path.join(ROOT, "settings_data_src.json")).read(), flags=re.S))
cur = dict(sd["presets"]["Enterprise"])
cur.update({
  # colours (design system tokens)
  "bg_color": "#ffffff", "heading_color": "#16213a", "text_color": "#16213a", "link_color": "#2f4a85", "star_color": "#f4d44d",
  "button_bg_color": "#2f4a85", "button_text_color": "#ffffff", "button_alt_bg_color": "#ffffff", "button_alt_text_color": "#2f4a85",
  # scheme 1 = surface-subtle band
  "color_scheme_1_bg": "#f6f8fa", "color_scheme_1_bg_grad": "", "color_scheme_1_heading": "#16213a", "color_scheme_1_text": "#16213a", "color_scheme_1_btn_bg": "#2f4a85", "color_scheme_1_btn_text": "#ffffff",
  # scheme 2 = sky-tint (announcement, newsletter, soft promo)
  "color_scheme_2_bg": "#e2f2f6", "color_scheme_2_bg_grad": "", "color_scheme_2_heading": "#16213a", "color_scheme_2_text": "#16213a", "color_scheme_2_btn_bg": "#2f4a85", "color_scheme_2_btn_text": "#ffffff",
  # scheme 3 = orange-tint (one seasonal campaign band)
  "color_scheme_3_bg": "#fdeee3", "color_scheme_3_bg_grad": "", "color_scheme_3_heading": "#16213a", "color_scheme_3_text": "#16213a", "color_scheme_3_btn_bg": "#2f4a85", "color_scheme_3_btn_text": "#ffffff",
  "panel_bg_color": "#f6f8fa", "panel_heading_color": "#16213a", "panel_text_color": "#16213a", "drawer_bg_color": "#ffffff", "drawer_text_color": "#16213a",
  "error_bg_color": "#fdeee3", "error_text_color": "#b42318", "success_bg_color": "#e3f2e9", "success_text_color": "#1e6a3e", "info_bg_color": "#e8eef8", "info_text_color": "#2f4a85",
  "blend_product_images": True, "blend_collection_images": True, "blend_bg_color": "#f6f8fa",
  # type
  "heading_font": "nunito_n8", "heading_uppercase": False, "subheading_uppercase": True, "button_text_uppercase": False, "heading_scale_start": "4", "heading_type_scale": "1.3",
  "body_font": "dm_sans_n4", "body_font_size": 16, "navigation_font": "dm_sans_n7",
  # design
  "max_page_width": 1600, "section_gap": "64", "input_button_border_width": "1", "input_button_border_radius": 10,
  "slider_show_arrows": "always", "slider_button_style": "btn--secondary", "slider_items_per_nav": "slide",
  "drawer_border_radius": 16, "overlay_border_radius": 10, "disclosure_toggle": "arrow",
  "show_breadcrumbs_product": True, "show_breadcrumbs_collection": True, "show_breadcrumbs_collection_list": False, "show_breadcrumbs_article": True, "show_breadcrumbs_blog": False,
  "pagination_style": "traditional", "pagination_infinite": False,
  # collection cards
  "coll_card_image_ratio": "1.77", "coll_card_image_fit": "contain", "coll_text_align": "text-start", "coll_show_link": True, "coll_label_color": "#2f4a85", "coll_bg_color": "#f6f8fa", "coll_border_color": "#e3e7ec",
  # product cards
  "prod_card_image_ratio": "1", "prod_card_image_fit": "contain", "card_hover_action": "second_image",
  "card_show_vendor": True, "card_show_subtitle": False, "card_show_rating": True, "card_show_inventory": True, "card_price_bottom": False,
  "enable_quick_add": True, "card_atc_mobile": "text_button_bottom", "card_atc_desktop": "text_button_bottom", "quick_add_sticky_buttons": False,
  "show_dividers": False, "card_contain": True, "card_bg_color": "#ffffff", "card_text_color": "#16213a", "card_border_color": "#e3e7ec",
  "card_highlight_bg_color": "#ffffff", "card_highlight_text_color": "#16213a", "card_highlight_border_color": "#2f4a85",
  # compare off (not in the wireframes)
  "enable_compare": False, "compare_toggle": "none",
  # inventory
  "inventory_threshold_low": 3, "inventory_threshold_very_low": 1, "inventory_show_notice": "always", "hide_no_stock_backordered": False, "inventory_show_count": "never",
  "in_stock_text_color": "#1e6a3e", "low_stock_text_color": "#1e6a3e", "very_low_stock_text_color": "#1e6a3e", "no_stock_text_color": "#b42318", "no_stock_backordered_text_color": "#2f4a85",
  # labels (badges)
  "product_label_card_position": "top-0 start",
  "show_sale_label": True, "sale_label_bg_color": "#fdeee3", "sale_label_text_color": "#9a4210", "sale_label_icon": "none", "sale_label_type": "standard",
  "show_sold_out_label": True, "sold_out_label_bg_color": "#eef0f3", "sold_out_label_text_color": "#4c5870", "sold_out_label_icon": "none",
  "show_new_label": True, "new_label_bg_color": "#fcf3cc", "new_label_text_color": "#6a5200", "new_label_icon": "none", "show_new_label_tag": True, "new_label_tag": "Just arrived", "show_new_label_days": False,
  "preorder_label_bg_color": "#e8eef8", "preorder_label_text_color": "#2f4a85", "preorder_label_icon": "none",
  "show_custom_label": True, "custom_label_bg_color": "#e2f2f6", "custom_label_text_color": "#1b5b70", "custom_label_icon": "none",
  # search
  "show_search_types": True, "enable_predictive_search": True, "predictive_search_limit": 6, "predictive_search_show_vendor": True, "predictive_search_show_price": True, "predictive_search_include_skus": False,
  "search_input_placeholder_1": "Search 11,000+ games, publishers, designers...", "search_input_placeholder_2": "Search for a game...", "search_input_placeholder_3": "Search for a publisher...",
  "search_input_font": "body", "prompts_mobile": False, "enable_speech_search": False, "speech_icon_color": "#2f4a85",
  # cart
  "cart_icon": "cart", "cart_type": "drawer", "after_add_to_cart": "drawer", "cart_empty_shop_link": "/collections/board-games",
  "show_recommendations": True, "recommendations_heading": "You may also like", "recommendations_to_show": 4, "cart_shaking": False,
  "show_free_shipping_notice": True, "free_shipping_minimum": "300", "free_shipping_color_scheme": "2",
  # motion off (Dean dislikes fades)
  "animations_enabled": "disabled", "animation_speed": "fast",
  "image_quality": "1", "show_blur_messages": False, "vibrate_on_atc": False,
})
settings_data = {"current": cur, "presets": sd["presets"]}
open(os.path.join(OUT, "settings_data.json"), "w").write(json.dumps(settings_data, indent=2))

# ---------------- header-group.json
header_group = {
  "type": "header", "name": "Header Group",
  "sections": {
    "announcement": {"type": "announcement",
      "blocks": {"msg": {"type": "announcement", "settings": {"text": "<p><strong>Flat rate shipping</strong> $10 Sydney Metro, Gosford &amp; Wollongong · $15 rest of Australia · <strong>Free over $300</strong></p>"}}},
      "block_order": ["msg"],
      "settings": {"link1": "/pages/help", "link1_label": "Help & FAQ", "link2": "/account", "link2_label": "Track my order", "enable_country_selector": False, "enable_language_selector": False,
                   "bg_color": "#e2f2f6", "text_color": "#16213a", "text_type_scale": "small", "read_time": 8}},
    "header": {"type": "header",
      "blocks": {
        "preorders": {"type": "columns", "settings": {"title": "Preorders", "collection_images": "none", "show_underline": True, "promo_position": "bottom", "promo_min_height": 120,
                      "promo1_content": "<p><strong>Due this month</strong></p>", "promo1_link_url": "/collections/preorders", "promo2_content": "<p><strong>Kickstarter pledges</strong></p>", "promo2_link_url": "/collections/preorders", "promo3_content": "<p><strong>How preorders work</strong></p>", "promo3_link_url": "/pages/help",
                      "promo_text_color": "#16213a", "promo_tint_color": "#e2f2f6", "promo_tint_opacity": 80}},
        "board": {"type": "sidebar", "settings": {"title": "Board Games", "collection_images": "large", "collection_use_product_image": True, "collection_circle_image": False, "show_underline": True, "show_collection_images": True, "sidebar_link_use_product_image": True, "show_product_images": True, "aspect_ratio": "1"}},
        "rpg": {"type": "columns", "settings": {"title": "Roleplaying", "collection_images": "none", "show_underline": True, "promo_position": "bottom"}},
        "acc": {"type": "columns", "settings": {"title": "Accessories", "collection_images": "none", "show_underline": True, "promo_position": "bottom", "promo_min_height": 120,
                "promo1_content": "<p><strong>Find the right sleeve</strong></p>", "promo1_link_url": "/collections/accessories", "promo_text_color": "#16213a", "promo_tint_color": "#e2f2f6", "promo_tint_opacity": 80}},
      },
      "block_order": ["preorders", "board", "rpg", "acc"],
      "settings": {"enable_sticky": True, "mobile_menu_position": "burger-left", "logo_type_scale": "2", "logo": "shopify://shop_images/advent-logo.png", "logo_width": 110, "logo_h1": True, "logo_center": False,
                   "enable_search": True, "minimise_search_mobile": False, "minimise_search_desktop": False, "menu": "main-menu", "menu_center": False, "link_toggle": "mobile", "repeat_links": True, "menu_featured_link": "Sale",
                   "cta_show": False, "bg_color": "#ffffff", "text_color": "#16213a", "accent_color": "#2f4a85"}},
    "trust": {"type": "icons-with-text",
      "blocks": {
        "t1": {"type": "item", "settings": {"icon": "truck", "heading": "Free shipping over $300", "text": "<p>$10 Sydney Metro · $15 Australia-wide</p>", "link": "/pages/help"}},
        "t2": {"type": "item", "settings": {"icon": "map_pin", "heading": "Australia-wide via AusPost", "text": "<p>Tracked, boxed and padded</p>", "link": "/pages/help"}},
        "t3": {"type": "item", "settings": {"icon": "chat_bubble", "heading": "Friendly, local service", "text": "<p>You'll hear back from Dean</p>", "link": "/pages/about"}},
        "t4": {"type": "item", "settings": {"icon": "lock", "heading": "Secure checkout", "text": "<p>Card, PayPal or bank transfer</p>", "link": "/pages/help"}},
      },
      "block_order": ["t1", "t2", "t3", "t4"],
      "settings": {"heading": "", "heading_align": "text-start", "icon_size": 24, "title_type_scale": "small", "text_type_scale": "small", "icon_position": "beside", "mobile_stack": False, "section_height": "xsmall", "color_scheme": "none", "full_width": True, "dividers": "border-bottom", "prevent_animation": True}},
  },
  "order": ["announcement", "header", "trust"],
}
open(os.path.join(OUT, "header-group.json"), "w").write(json.dumps(header_group, indent=2))

# ---------------- footer-group.json
footer_group = {
  "type": "footer", "name": "Footer Group",
  "sections": {
    "footer": {"type": "footer",
      "blocks": {
        "text": {"type": "text", "settings": {"image": "shopify://shop_images/advent-logo.png", "image_width": 110, "heading": "", "text": "<p>Your friendly, local, online board game store. Sydney based, shipping Australia-wide.</p><p>dean@adventgames.com.au · 0411 017 162<br>Free pickup Tuesday nights, Chatswood</p>", "show_social": False, "text_align": "text-start"}},
        "shop": {"type": "link_list", "settings": {"heading": "Shop", "menu": "footer-shop"}},
        "help": {"type": "link_list", "settings": {"heading": "Help", "menu": "footer-help"}},
        "advent": {"type": "link_list", "settings": {"heading": "Advent Games", "menu": "footer-advent"}},
      },
      "block_order": ["text", "shop", "help", "advent"],
      "settings": {"show_back_to_top": False, "show_payment_icons": True, "show_powered_by": True, "enable_country_selector": False, "enable_language_selector": False, "bg_color": "#f6f8fa", "text_color": "#16213a"}},
  },
  "order": ["footer"],
}
open(os.path.join(OUT, "footer-group.json"), "w").write(json.dumps(footer_group, indent=2))

# ---------------- templates/index.json
def fc(key, title, coll, scheme="none", view_all=True, products=8):
    return (key, {"type": "featured-collection", "settings": {"title": title, "heading_align": "text-start", "show_view_all": view_all, "collection": coll, "layout": "carousel", "card_size_mobile": "small", "card_size": "small", "products_to_show": products, "show_highlight_products": False, "show_promo_info": False, "image_ratio": "1", "promo_title": "", "content": "", "link_url": "", "button_label": "", "color_scheme": scheme, "button_style": "btn btn--secondary"}})

def mwt(key, layout, sub, heading, text, btn_label, btn_link, scheme="none", image=""):
    return (key, {"type": "media-with-text",
      "blocks": {"sub": {"type": "subheading", "settings": {"text": sub}}, "h": {"type": "heading", "settings": {"heading": heading, "heading_size": "h2", "heading_h1": False}}, "t": {"type": "text", "settings": {"text": text, "enlarge_text": True}}, "b": {"type": "button", "settings": {"button_label": btn_label, "button_link": btn_link, "button_style": "btn btn--primary"}}},
      "block_order": ["sub", "h", "t", "b"],
      "settings": {"image": image, "layout": layout, "image_fit": "contain", "media_width": 50, "media_scale": 100, "text_align": "text-start", "color_scheme": scheme}})

sections = [
  ("hero", {"type": "promo-grid",
    "blocks": {
      "big": {"type": "media", "settings": {"link_url": "/blogs/news", "columns": 2, "rows": 2, "line1_text": "New site, same Dean", "line1_text_type_scale": "text-h6", "line2_text": "Welcome to the new look Advent Games!", "line2_text_type_scale": "text-h1", "line3_text": "Same friendly service, a much easier way to find your next game.", "line3_text_type_scale": "text-h6", "overlay_position": "justify-start items-center", "text_alignment": "text-start", "promo_circle": False, "background_color": "#e2f2f6", "text_color": "#16213a", "subheading": "", "link_text": "Read the blog post", "text_type_scale": "h6", "tint_color": "#000000", "tint_opacity": 0}},
      "arrived": {"type": "media", "settings": {"link_url": "/collections/just-arrived", "columns": 1, "rows": 1, "line1_text": "This week", "line1_text_type_scale": "text-h6", "line2_text": "Just arrived", "line2_text_type_scale": "text-h3", "line3_text": "", "line3_text_type_scale": "text-h6", "overlay_position": "justify-start items-end", "text_alignment": "text-start", "promo_circle": False, "background_color": "#f4d44d", "text_color": "#16213a", "subheading": "", "link_text": "See what's new", "text_type_scale": "h6", "tint_color": "#000000", "tint_opacity": 0}},
      "preorders": {"type": "media", "settings": {"link_url": "/collections/preorders", "columns": 1, "rows": 1, "line1_text": "Reserve now", "line1_text_type_scale": "text-h6", "line2_text": "Preorders open", "line2_text_type_scale": "text-h3", "line3_text": "", "line3_text_type_scale": "text-h6", "overlay_position": "justify-start items-end", "text_alignment": "text-start", "promo_circle": False, "background_color": "#f6f8fa", "text_color": "#16213a", "subheading": "", "link_text": "The big December releases", "text_type_scale": "h6", "tint_color": "#000000", "tint_opacity": 0}},
    },
    "block_order": ["big", "arrived", "preorders"],
    "settings": {"title": "", "heading_align": "text-start", "button_label": "", "button_link": "", "gallery_cols_max": 3, "mobile_carousel": False, "gallery_cols_min": "1", "fixed_height_desktop": 210, "fixed_height_mobile": 220, "text_overlay_font": "heading", "color_scheme": "default"}}),
  fc("just_arrived", "Just arrived", "just-arrived"),
  fc("new_preorder", "New to preorder", "new-to-preorder", scheme="1"),
  ("types", {"type": "collection-list",
    "blocks": {h: {"type": "collection", "settings": {"collection": h, "image": ""}} for h in ["strategy", "family", "party", "thematic", "wargames", "solo-games", "two-player", "kids"]},
    "block_order": ["strategy", "family", "party", "thematic", "wargames", "solo-games", "two-player", "kids"],
    "settings": {"title": "Find your next game", "heading_align": "text-start", "button_label": "", "button_link": "", "layout": "grid", "card_size": "medium", "use_product_image": True, "circle_image": False, "show_border": True, "color_scheme": "none", "full_width": True}}),
  fc("best_sellers", "Best sellers", "best-sellers"),
  ("staff", {"type": "product-list", "settings": {"title": "Staff recommendations", "heading_align": "text-start", "view_all_url": "/collections/staff-picks", "product_list": ["the-great-harbor", "three-days-of-gettysburg-deluxe-edition", "d-d-castle-ravenloft-board-game", "d-d-legend-of-drizzt-board-game"], "layout": "grid", "card_size_mobile": "small", "card_size": "medium", "show_highlight_products": False, "show_promo_info": False, "image_ratio": "1", "promo_title": "", "content": "", "link_url": "", "button_label": "", "color_scheme": "1", "button_style": "btn btn--secondary"}}),
  mwt("beginners", "left", "Start here", "New to board games?", "<p>Every journey begins with a single step, and these collections will set you on the Board Game path. These games provide a strong base for learning essential board game mechanics, and are great fun for nearly all ages!</p>", "Gateway games", "/collections/gateway-games"),
  mwt("giftcards", "right", "Gift cards", "Can't pick for them? Let them pick.", "<p>Advent Games gift cards are emailed straight away and work on every game, expansion and preorder on the site.</p>", "Buy a gift card", "/products/gift-card"),
  ("campaign", {"type": "image-banner",
    "blocks": {"sub": {"type": "subheading", "settings": {"text": "Campaign slot"}}, "h": {"type": "heading", "settings": {"heading": "Boxing Day sale starts 26 December", "heading_size": "h2", "heading_h1": False}}, "t": {"type": "text", "settings": {"text": "<p>Selected games, while stocks last. One campaign at a time, swapped each season.</p>", "enlarge_text": True}}, "b": {"type": "button", "settings": {"button_1_label": "Set a reminder", "button_1_link": "/collections/sale", "button_1_style": "btn btn--primary", "button_2_label": "", "button_2_link": "", "button_2_style": "btn btn--primary"}}},
    "block_order": ["sub", "h", "t", "b"],
    "settings": {"url": "", "height_mode": "fixed", "fixed_height_desktop": 400, "fixed_height_mobile": 320, "overlay_position": "justify-start items-center", "overlay_text_align": "text-start", "mob_center_text": False, "mobile_stacked": False, "color_scheme": "3", "full_width": False, "transparent_content_color": "#16213a", "tint_color": "#000000", "tint_opacity": 0, "prevent_animation": True}}),
  ("publishers", {"type": "logo-list",
    "blocks": {f"p{i}": {"type": "logo", "settings": {"url": "/pages/brands", "logo_width": 120, "text": p}} for i, p in enumerate(["GMT Games", "Stonemaier Games", "Lookout Spiele", "Czech Games Edition", "Days of Wonder", "Capstone Games", "Pegasus Spiele", "Rio Grande Games"])},
    "block_order": [f"p{i}" for i in range(8)],
    "settings": {"title": "Shop by publisher", "heading_align": "text-start", "button_label": "All brands A-Z", "button_link": "/pages/brands", "layout": "grid", "spacing": 40, "logo_grid_align": "justify-start", "color_scheme": "none", "full_width": True}}),
  mwt("story", "left", "About Advent Games", "Your friendly, local, online board game store", "<p>Owner-operated in Sydney, with a huge range, fair prices and the hard-to-find games other stores don't carry. Ask about a game, a preorder or an order you've already placed and you'll hear back from Dean, not an AI response.</p>", "Our story", "/pages/about", scheme="1"),
  ("reviews", {"type": "testimonials",
    "blocks": {f"r{i}": {"type": "testimonial", "settings": {"testimonial": f"<p>{q}</p>", "author": "Example reviewer", "author_info": "Google review (example, replaced by the Google Reviews app block)", "show_star_rating": True, "star_rating": 5}} for i, q in enumerate([
      "Ordered Monday night, arrived Wednesday. Dean emailed to check I knew the expansion needed the base game. That's service.",
      "Best range of wargames in Australia and the preorder pricing beats everyone else I've found.",
      "Picked up at Chatswood on Tuesday night and got a game recommendation thrown in. Will be back."])},
    "block_order": ["r0", "r1", "r2"],
    "settings": {"heading": "What our customers say", "show_quotes": True, "testimonial_size": "h5", "text_position": "justify-center", "text_align": "text-center justify-center", "nav_style": "arrows", "transition": "fade", "autoplay": False, "slider_pause": False, "autoplay_speed": 5, "color_scheme": "default", "full_width": True}}),
  ("newsletter", {"type": "newsletter",
    "blocks": {"h": {"type": "heading", "settings": {"heading": "New releases and preorders, first.", "heading_size": "h3"}}, "t": {"type": "text", "settings": {"text": "<p>New arrivals, preorders and the odd special, straight to your inbox. No spam, unsubscribe any time.</p>", "enlarge_text": False}}, "f": {"type": "form", "settings": {}}},
    "block_order": ["h", "t", "f"],
    "settings": {"overlay_position": "justify-center", "text_align": "text-center", "image": "", "color_scheme": "2", "full_width": True, "transparent_content_color": "#16213a", "tint_color": "#000000", "tint_opacity": 0}}),
]
index = {"sections": {k: v for k, v in sections}, "order": [k for k, _ in sections]}
open(os.path.join(OUT, "index.json"), "w").write(json.dumps(index, indent=2))
print("ok", [os.path.getsize(os.path.join(OUT, f)) for f in os.listdir(OUT)])
