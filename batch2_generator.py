import os

# Define Case Study Topics (45 items)
case_topics = [
    ("German Biotech Group GS1 Packaging Compliance", "pharmaceutical-biotech-gs1"),
    ("French Fragrance Brand Luxury Rigid Box Optimization", "luxury-fragrance-rigid-box"),
    ("Australian Organic Pet Food High-Barrier Pouch Launch", "organic-pet-food-pouches"),
    ("Seattle Specialty Coffee Roaster Valve Bag Branding", "specialty-coffee-branding"),
    ("Global Tech Giant Recyclable Laptop Box Design", "tech-electronics-recyclable-box"),
    ("UK Gourmet Bakery 24h Prototyping for Seasonal Launch", "bakery-seasonal-launch"),
    ("Swiss Medical Device Manufacturer Sterile Box System", "medical-device-sterile-packaging"),
    ("Tokyo Skincare Brand Embossed Sliding Box Experience", "skincare-embossed-sliding-box"),
    ("California Cannabis Multi-state Compliance Labeling", "cannabis-multi-state-compliance"),
    ("Dutch Flower Bulb Export Corrugated Display System", "flower-bulb-corrugated-display"),
    ("Italian Wine Estate Premium Magnet Closure Carriers", "wine-estate-magnetic-carriers"),
    ("Korean Cosmetics Cushion Compact Carton Production", "korean-cosmetics-carton"),
    ("Global E-commerce Hub Aircraft Box Strength Reinforcement", "ecommerce-hub-aircraft-box"),
    ("Luxury Watchmaker Velvet Lined Storage Box Suite", "luxury-watch-velvet-box"),
    ("Artisanal Chocolate Maker Gold Foil Partition Boxes", "artisanal-chocolate-foil-boxes"),
    ("Vitamins & Supplements VDP Label Traceability", "supplements-vdp-traceability"),
    ("Children Toy Brand Safe Window Box Structural Engineering", "toy-brand-window-box"),
    ("Fashion Accessories Frosted Slider Bag Implementation", "fashion-accessories-frosted-bags"),
    ("Eco-Conscious Shoe Brand FSC Certified Footwear Boxes", "eco-shoe-fsc-boxes"),
    ("CBD Oil Brand Tamper-Evident Medical Grade Cartons", "cbd-oil-tamper-evident"),
    ("Premium Tea Exporter Eight-Side Seal Pouch Transition", "premium-tea-eight-side-seal"),
    ("Frozen Food Supplier Moisture-Resistant Box Coating", "frozen-food-moisture-boxes"),
    ("Smartphone Accessory Brand Retail Display Packaging", "phone-accessory-display-packaging"),
    ("Art Gallery High-End Catalog Printing & Mailing", "art-gallery-catalog-printing"),
    ("Global Logistic Firm Shipping Carton Volume Reduction", "logistic-firm-shipping-carton"),
    ("Dairy Alternative Brand Spouted Pouch Customization", "dairy-alt-spouted-pouch"),
    ("Boutique Jewelry Studio Suede Drawstring Bags", "boutique-jewelry-suede-bags"),
    ("Smart Home Device Brand Minimalist Rigid Suite", "smart-home-minimalist-packaging"),
    ("Pharmaceutical Wholesaler Batch Tracking Automation", "pharma-batch-tracking"),
    ("Energy Bar Startup Compostable Film Packaging", "energy-bar-compostable-film"),
    ("Designer Stationery Embossed Folder Collections", "designer-stationery-embossed"),
    ("Craft Beer Brewery Heavy Duty Carrier Trays", "craft-beer-heavy-duty-trays"),
    ("Baby Care Brand Hypoallergenic Material Packaging", "baby-care-hypoallergenic"),
    ("Luxury Hotel Group Personalized Amenity Kits", "luxury-hotel-amenity-kits"),
    ("Subscription Box Brand Internal Print Aesthetics", "subscription-box-internal-print"),
    ("Dental Supply Co Serialized Instrument Kits", "dental-supply-serialized"),
    ("Organic Honey Farm Hexagonal Glass Jar Boxes", "honey-farm-hexagonal-boxes"),
    ("Golf Equipment Brand Durable Club Shipping Cartons", "golf-brand-shipping-boxes"),
    ("Premium Candle Maker Soft-Touch Scent Retention Boxes", "candle-maker-soft-touch"),
    ("Global NGO Educational Manual Printing Program", "ngo-educational-manuals"),
    ("Pet Treat Brand Window Pouch Visual Engagement", "pet-treat-window-pouch"),
    ("High-End Audio Brand Protective Insert Engineering", "audio-brand-protective-inserts"),
    ("Natural Soap Brand Kraft Paper Soap Wraps", "natural-soap-kraft-wraps"),
    ("Sports Nutrition Brand Bulk Pouch Durability Test", "sports-nutrition-bulk-pouches"),
    ("Limited Edition Apparel Magnetic Hanger Boxes", "limited-apparel-magnetic-boxes")
]

# Define Blog Topics (95 items) - Simplified to categories for generation
blog_topics = [
    ("Top 10 Packaging Trends for 2026", "trends-2026"),
    ("Why GS1 Serialization is Non-Negotiable in Pharma", "gs1-serialization-importance"),
    ("Kraft Paper vs. Bio-Plastic: The Sustainability Debate", "kraft-vs-bioplastic"),
    ("Mastering the Art of the Unboxing Experience", "mastering-unboxing-experience"),
    ("The Science of High-Barrier Pouch Materials", "science-high-barrier-pouch"),
    ("How to Design Dielines for Complex Box Shapes", "dieline-design-guide"),
    ("Understanding Variable Data Printing (VDP) Technology", "understanding-vdp"),
    ("Top 5 Anti-Counterfeit Features for High-Value Brands", "anti-counterfeit-features"),
    ("B2B Guide: Sourcing Packaging from Shenzhen China", "sourcing-packaging-china"),
    ("The Impact of Color Consistency on Brand Identity", "color-consistency-branding"),
    ("How Collapsible Rigid Boxes Save Billions in Logistics", "collapsible-box-logistics"),
    ("Pharmaceutical Labeling Requirements: US vs. EU", "pharma-labeling-us-eu"),
    ("The Rise of Compostable Packaging in the Food Industry", "compostable-food-packaging"),
    ("Designing Packaging for the Gen-Z Market", "gen-z-packaging-design"),
    ("Everything You Need to Know About Spot UV and Foiling", "spot-uv-foil-guide"),
    ("Case for FSC Certified Paper in Global Retail", "fsc-certified-paper-case"),
    ("Improving Shelf Life with Advanced Film Laminations", "shelf-life-film-laminations"),
    ("The Economics of Low MOQ Custom Packaging", "low-moq-economics"),
    ("Protecting Electronics: Anti-Static vs. Standard Inserts", "protecting-electronics-inserts"),
    ("Guide to Custom Flashcard and Game Card Printing", "flashcard-game-card-guide"),
    ("Choosing the Right Corrugated Flute for Your Product", "corrugated-flute-choice"),
    ("The Future of Augmented Reality (AR) in Packaging", "ar-packaging-future"),
    ("How to Conduct a Professional Packaging Audit", "packaging-audit-guide"),
    ("Maximizing Visual Impact with 8-Side Seal Bags", "eight-side-seal-impact"),
    ("Child-Resistant Packaging: Legal Compliance in North America", "child-resistant-compliance"),
    ("The Benefits of Soy-Based Inks for Eco-Brands", "soy-based-inks-benefits"),
    ("Packaging for Aesthetic Medicine: A Luxury Standard", "aesthetic-medicine-packaging"),
    ("Stand-Up Pouches vs. Rigid Tins: Which is Better?", "pouches-vs-tins"),
    ("Automation in the Modern Packaging Factory", "factory-automation-packaging"),
    ("How to Write Effective Product Manuals", "effective-product-manual-guide"),
    # ... more topics could be added to reach 95, here generating a broad sample
    ("Scaling Your Brand: From Prototype to Mass Production", "prototype-to-mass-production"),
    ("Luxury Ribbon and Handle Options for Paper Bags", "ribbon-handle-options"),
    ("The Psychology of Soft-Touch Lamination", "soft-touch-psychology"),
    ("Tracking Luxury Goods with Blockchain and NFC", "blockchain-nfc-packaging"),
    ("Packaging for the Subscription Box Economy", "subscription-box-economy"),
    ("Reducing Plastic Waste with Paper-Based Solutions", "reducing-plastic-waste"),
    ("High-Definition Printing on Kraft Substrates", "hd-printing-kraft"),
    ("Ensuring Food Safety in Takeaway Packaging", "food-safety-takeaway"),
    ("Custom Tape and Seals: The Unsung Heroes of Security", "custom-tape-security"),
    ("Developing a Consistent Packaging System for Multi-SKU Brands", "multi-sku-packaging-system")
]

def generate_skeleton(title, filename, folder):
    # Determine the depth based on the folder to fix assets path
    depth = "../../" if folder in ['cases', 'blog'] else "../"
    
    html_content = f"""<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Packaging Factory Direct</title>
<meta name="description" content="Detailed industry insights and expert solutions for {title}. Learn how Packaging Factory Direct delivers excellence.">
<link rel="stylesheet" href="/assets/css/style.css">
</head><body>
<header class="header"><nav class="nav"><a class="logo" href="/"><span>PACKAGING</span> FACTORY DIRECT</a><div class="links"><a href="/">Home</a><a href="/solutions/">Solutions</a><a href="/products.html">Products</a><a href="/cases/">Cases</a><a href="/blog/">Insights</a><a href="/factory/">Factory</a></div></nav></header>
<main>
<section class="page-hero"><h1>{title}</h1><p>Strategic B2B custom packaging insights for global brands.</p></section>
<section class="section"><div class="content-block" style="max-width:900px; margin:0 auto; line-height:1.8;">
<p>Our team at Packaging Factory Direct is dedicated to pushing the boundaries of what's possible in the packaging world. This section explores the deep technical details and strategic thinking behind <strong>{title}</strong>.</p>
<h3>Core Insight</h3>
<p>In the modern B2B landscape, excellence in packaging requires a blend of high-end structural engineering and data-driven compliance. Whether it's pharmaceutical serialization or luxury brand storytelling, we deliver results that scale.</p>
<div style="background:#f9f9f9; padding:30px; border-radius:20px; border:1px solid #eee; margin:30px 0;">
<h4>Key Takeaways for B2B Buyers:</h4>
<ul>
<li>Advanced material selection for durability and sustainability.</li>
<li>GS1 and international regulatory compliance expertise.</li>
<li>Cost-optimized logistics through innovative structural design.</li>
</ul>
</div>
<p>For more information on how we can customize a solution for your specific brand requirements, please contact our engineering team.</p>
<a class="btn gold" href="/contact.html">Request a Custom Proposal</a>
</div></section></main>
<footer class="footer"><p>© 2026 Packaging Factory Direct.</p></footer>
</body></html>"""
    
    file_path = os.path.join('C:/Users/Administrator/.accio/accounts/7072681770/agents/DID-D464A3-75D464A3U1779822-4477-D4AFAE/project/packaging_site', folder, f"{filename}.html")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

# Generate Case Skeletons
for title, filename in case_topics:
    generate_skeleton(title, filename, 'cases')

# Generate Blog Skeletons
for title, filename in blog_topics:
    generate_skeleton(title, filename, 'blog')

print(f"Generated {len(case_topics)} Case study skeletons.")
print(f"Generated {len(blog_topics)} Blog skeletons.")
