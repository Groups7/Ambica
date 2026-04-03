import urllib.parse, os

BASE = "https://ambicapearlsandjewellers.com/wp-content/uploads/2024/"

WA20 = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>'
PH20 = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
WA16 = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>'

def wa_url(name):
    msg = "Hi Ambica, I'm interested in " + name + ". Please share details."
    return "https://wa.me/919876543210?text=" + urllib.parse.quote(msg)

def card(name, img, s1, s2, s3):
    wa = wa_url(name)
    lines = [
        '                <div class="product-card">',
        '                    <div class="product-image">',
        '                        <img src="' + img + '" alt="' + name + '">',
        '                        <div class="product-overlay">',
        '                            <a href="' + wa + '" target="_blank" class="btn-icon" title="Ask on WhatsApp">',
        '                                ' + WA20,
        '                            </a>',
        '                            <a href="tel:+919876543210" class="btn-icon btn-white" title="Call">',
        '                                ' + PH20,
        '                            </a>',
        '                        </div>',
        '                    </div>',
        '                    <div class="product-info">',
        '                        <h3>' + name + '</h3>',
        '                        <div class="product-specs">',
        '                            <span class="spec-chip">' + s1 + '</span>',
        '                            <span class="spec-chip">' + s2 + '</span>',
        '                            <span class="spec-chip">' + s3 + '</span>',
        '                        </div>',
        '                        <a href="' + wa + '" target="_blank" class="btn btn-primary btn-sm">',
        '                            ' + WA16,
        '                            Ask on WhatsApp',
        '                        </a>',
        '                    </div>',
        '                </div>',
    ]
    return '\n' + '\n'.join(lines)

categories = {
    "category-malas.html": [
        ("Pearl Emerald 3-Line Mala",       BASE+"10/Pearl-with-emerald-stone-mala-3-L-nailon-and-tre.jpg",  "3 Line","Emerald Stone","Alloy Mix"),
        ("Blue MOP Pearl Single Line Mala", BASE+"11/onex-blue-mop-pearl-mala-1-line-nailon-and-alloy.jpg",  "1 Line","MOP Pearl","Alloy Mix"),
        ("3-Line Blue Onex Pearl Mala",     BASE+"11/3-L-mala-with-onex-blue-mala-pearl-nailon-alloy.jpg",   "3 Line","Blue Onex","Nailon & Alloy"),
        ("Russian Emerald Oval Mala",       BASE+"10/Russian-emerald-mala-oval-nailon-and-tread.jpg",        "Oval Cut","Russian Emerald","Nailon & Thread"),
        ("Sea Blue MOP Pearl Mala",         BASE+"11/sea-blue-onex-with-mop-pearl-mala-nailon-alloy-m.jpg",  "Sea Blue","MOP Pearl","Alloy Mix"),
        ("Green Onyx 2-Line Pearl Mala",    BASE+"10/Oneyx-cut-green-stone-2-L-nailon-and-tread.jpg",        "2 Line","Green Onyx","Nailon & Thread"),
    ],
    "category-earrings.html": [
        ("Pearl Green Stone Earrings",      BASE+"10/Pearls-with-green-semi-stone-earings-mix-alloy.jpg",    "Semi Stone","Alloy Mix","Gold Plated"),
        ("Pearl Drop Earrings",             BASE+"07/DSC06940.jpg",                                          "Drop Style","Pearl","Alloy Mix"),
        ("Pearl Classic Earrings",          BASE+"07/DSC06931.jpg",                                          "Classic Style","Pearl","Silver Plated"),
        ("Pearl Stud Earrings",             BASE+"07/DSC06923.jpg",                                          "Stud Style","Pearl","Gold Plated"),
        ("Pearl Kundan Earrings",           BASE+"07/DSC07539.jpg",                                          "Kundan Work","Pearl","Alloy Mix"),
        ("Pearl Designer Earrings",         BASE+"07/DSC07473.jpg",                                          "Designer","Pearl","Gold Plated"),
    ],
    "category-bangles.html": [
        ("Pearl Green Stone Bangles",       BASE+"10/Pearls-with-green-stone-combi-bangles-alloy-mix.jpg",   "Combo Set","Green Stone","Alloy Mix"),
        ("1GM Gold Bangle Set A",           BASE+"07/1-GM-BAN-A.jpg",                                        "1GM Gold","Set of 4","Gold Plated"),
        ("1GM Gold Bangle Set B",           BASE+"07/1-GM-BAN-B.jpg",                                        "1GM Gold","Set of 4","Gold Plated"),
        ("1GM Gold Bangle Set C",           BASE+"07/1-GM-BAN-C.jpg",                                        "1GM Gold","Set of 4","Gold Plated"),
        ("1GM Pearl Bangle Style A",        BASE+"07/1GM-A1.jpg",                                            "1GM Style","Pearl","Gold Plated"),
        ("1GM Pearl Bangle Style B",        BASE+"07/1GM-B2.jpg",                                            "1GM Style","Pearl","Gold Plated"),
    ],
    "category-sets.html": [
        ("Turquoise Feroza 2-Line Set",     BASE+"11/turquies-feroza-2-line-set-alloy-mix-plated.jpg",       "2 Line","Feroza Stone","Alloy Mix"),
        ("Turquoise Blue Pearl Set",        BASE+"11/turquies-blue-3-L-pearl-set-alloy-mix-gold.jpg",        "3 Line","Blue Pearl","Gold Mix"),
        ("Ruby Antic Pearl Pendant Set",    BASE+"10/button-pearl-with-Ruby-antic-set-oxadise-metal.jpg",    "Pendant Set","Ruby Stone","Oxidised Metal"),
        ("Green Stone Pearl Pendant Set",   BASE+"10/Semi-green-stone-real-pearl-pendent-set-mix-alloy.jpg", "Pendant Set","Green Stone","Alloy Mix"),
        ("Emerald 3-Row Pearl Set",         BASE+"10/Pearls-with-emerald-3-row-set-alloy-mix-gold-pla.jpg",  "3 Row","Emerald","Gold Plated"),
        ("Green CZ 2-Line Pearl Set",       BASE+"10/Green-cz-s-with-2-L-pearl-set-alloy-gold-plated.jpg",  "2 Line","Green CZ","Gold Plated"),
    ],
    "category-mens.html": [
        ("Gents Pearl Style 1",             BASE+"07/DSC07666-1.jpg",  "Gents","Pearl","Alloy Mix"),
        ("Gents Pearl Style 2",             BASE+"07/DSC07664.jpg",    "Gents","Pearl","Gold Plated"),
        ("Gents Pearl Style 3",             BASE+"07/DSC07662.jpg",    "Gents","Pearl","Silver Plated"),
        ("Gents Pearl Style 4",             BASE+"07/DSC07660.jpg",    "Gents","Pearl","Alloy Mix"),
        ("Gents Pearl Style 5",             BASE+"07/DSC07658.jpg",    "Gents","Pearl","Gold Plated"),
        ("Gents Pearl Style 6",             BASE+"07/DSC07889.jpg",    "Gents","Pearl","Alloy Mix"),
    ],
    "category-western.html": [
        ("Aqua Blue Stone Mix Mala",        BASE+"11/aqua-blue-stone-and-cots-mix-nailon-and-tread.jpg",    "Western","Aqua Blue","Nailon & Thread"),
        ("Blue Aqua 5-Line Stone Mala",     BASE+"11/blue-aqua-stone-wall-th-pearl-5-L-nailon-alloy.jpg",   "5 Line","Aqua Blue","Alloy Mix"),
        ("Pink Opal Stone Mala",            BASE+"11/pink-opel-stone-mala-nailon-and-tread-adjustment.jpg", "Pink Opal","Adjustable","Nailon & Thread"),
        ("Rainbow Moon Stone Mala",         BASE+"11/rainbow-moon-stone-cut-mala-nailon-tread.jpg",         "Rainbow Stone","Cut Design","Nailon & Thread"),
        ("White Opal Uncut Mala",           BASE+"11/white-opel-mala-uncut-nailon-tread-adjustmen.jpg",     "White Opal","Uncut","Adjustable"),
        ("Aqua Blue 4-Line Stone Mala",     BASE+"11/aqua-blue-stone-maniya-4-L-nailon-and-tread-adju.jpg", "4 Line","Aqua Blue","Adjustable"),
    ],
}

for fname, products in categories.items():
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    grid_open = '<div class="products-grid">'
    start = content.find(grid_open)
    if start == -1:
        print("ERROR: products-grid not found in", fname)
        continue

    # Find matching closing </div> by counting nesting depth
    pos = start + len(grid_open)
    depth = 1
    while pos < len(content) and depth > 0:
        if content[pos:pos+4] == '<div':
            depth += 1
        elif content[pos:pos+6] == '</div>':
            depth -= 1
            if depth == 0:
                break
        pos += 1
    end = pos + 6  # include </div>

    new_grid = grid_open
    for p in products:
        new_grid += card(*p)
    new_grid += '\n            </div>'

    content = content[:start] + new_grid + content[end:]

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated:", fname)

print("All done!")
