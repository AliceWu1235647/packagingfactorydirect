import os
import re

image_mapping = {
    "collapsible-magnetic-boxes.html": "https://sc02.alicdn.com/kf/A74d82c380a404a9f9822743e2204a527f.png",
    "luxury-embossed-sets.html": "https://sc02.alicdn.com/kf/A4824c06bf58a4339808814c6f4ea8062F.png",
    "luxury-chocolate-boxes.html": "https://sc02.alicdn.com/kf/Afed1e4c19f96447c9601ad7055cec3deL.png",
    "boutique-pink-paper-bags.html": "https://sc02.alicdn.com/kf/A07e0fd964c69409091ec1df7dcdded06L.png",
    "luxury-velvet-jewelry-pouches.html": "https://sc02.alicdn.com/kf/A2f175f48bed345fb932ddec0af4564f5K.png",
    "luxury-satin-pouches.html": "https://sc02.alicdn.com/kf/A7ffaf6256b0d4eddb734828f6e2a2a87N.png",
    "luxury-printed-paper-bags.html": "https://sc02.alicdn.com/kf/Accabcf952cee4ce7965a8552beafcf98T.png",
    "cosmetic-packaging-boxes.html": "https://sc02.alicdn.com/kf/A08ac5670737d4aa0bc31332fcbfaf7e48.png",
    "printed-mailer-boxes.html": "https://sc02.alicdn.com/kf/Aac34a5e94eca4003a96d6d41a04ebd4c5.png",
    "luxury-magnetic-gift-boxes.html": "https://sc02.alicdn.com/kf/A27de7768569e45a5a2ce89d4af2d21c5d.png",
    "eight-side-seal-pouches.html": "https://sc02.alicdn.com/kf/Ad2b785bffcd24433aa0c393d8d19a16ax.png",
    "pet-food-stand-up-pouches.html": "https://sc02.alicdn.com/kf/A86354ebabb4444379c8cd58ee2a5e9dcY.png",
    "flat-bottom-coffee-bags.html": "https://sc02.alicdn.com/kf/A6447eaa791324d0d9cba5d21f9957a49w.png",
    "frosted-zipper-bags.html": "https://sc02.alicdn.com/kf/A6b99688276684f2ebc25e18fad05f655S.png",
    "custom-paper-bags.html": "https://sc02.alicdn.com/kf/A2cf10cc137604ef79e20db30b22865c8F.png",
    "cannabis-mylar-pouches.html": "https://sc02.alicdn.com/kf/A4faec152ad424b8582db86a95ff8001fY.png",
    "custom-food-packaging-boxes.html": "https://sc02.alicdn.com/kf/Aa8d0330e14124affaa2ea0293511432et.png",
    "custom-stand-up-pouches.html": "https://sc02.alicdn.com/kf/Ac5c3bb361fe641688d671ecf868ed9beR.png",
    "eco-friendly-coffee-pouches.html": "https://sc02.alicdn.com/kf/Abf04052dc1274f5cae1037852d3fe3c70.png",
    "paper-cups-food-containers.html": "https://sc02.alicdn.com/kf/A2466770076964989b327c47a7b422124E.png",
    "bakery-pastry-boxes.html": "https://sc02.alicdn.com/kf/Aff26a23be2d8441f9c224458d042cdceL.png",
    "books-catalogs-manuals.html": "https://sc02.alicdn.com/kf/A87c62bb2834c4ffd93cb2df99a42f8c7O.png",
    "burger-boxes-wraps.html": "https://sc02.alicdn.com/kf/A811d9b1794514069bfa4f03d70c34981U.png",
    "cards-stickers-labels.html": "https://sc02.alicdn.com/kf/Ae517a60cc9014358b551e1c5241bb07ej.png",
    "coffee-paper-cups.html": "https://sc02.alicdn.com/kf/A3bac7971d3e2429781149fe10396fe964.png",
    "custom-folding-carton-boxes.html": "https://sc02.alicdn.com/kf/Afb4e3cd0a8484ea2838eed15f0205d746.png",
    "donut-packaging-sets.html": "https://sc02.alicdn.com/kf/A7f737cfa15b34fca9d809d8a73074730w.png",
    "eco-kraft-mailer-boxes.html": "https://sc02.alicdn.com/kf/Aa9241935a83141abac6b11ff489e090aE.png",
    "food-packaging-boxes.html": "https://sc02.alicdn.com/kf/A878df6de61554bb785c7f98a7922cadbJ.png",
    "fried-chicken-boxes.html": "https://sc02.alicdn.com/kf/A5b7d64e5253540bfbdb2f18d99642d8fI.png",
    "fries-popcorn-boxes.html": "https://sc02.alicdn.com/kf/A372bdc973ba9458e8ea8e46fee0c2865h.png",
    "hot-dog-boxes-trays.html": "https://sc02.alicdn.com/kf/A6494bb8ec68540e298bbe9e9624c57674.png",
    "pet-food-packaging-bags.html": "https://sc02.alicdn.com/kf/Aa9b668acf2aa444e8de5a498db8f114dA.png",
    "pharmaceutical-serialization-boxes.html": "https://sc02.alicdn.com/kf/Af48712b775fb4886b6c8820e92f3d8d02.png",
    "pharmaceutical-serialization.html": "https://sc02.alicdn.com/kf/A917d76bc50a94b18b639c420429a8b816.png",
    "serialized-medical-boxes.html": "https://sc02.alicdn.com/kf/A50b4e03259f94eba857e6b91af63a65bf.png",
    "shipping-mailer-boxes.html": "https://sc02.alicdn.com/kf/Af3c9f4339c4d48888899f18f63eef879y.png",
    "tape-tin-boxes-pet-bottles.html": "https://sc02.alicdn.com/kf/A587421d89d124a3cb80cf5ae7f16e863v.png",
    "foldable-magnetic-gift-boxes.html": "https://sc02.alicdn.com/kf/Adfada113e470423fa2c62e4759d88d05T.png"
}

def update_all(root_dir):
    products_dir = os.path.join(root_dir, 'products')
    
    # 1. Update products.html (The List Page)
    list_page = os.path.join(root_dir, 'products.html')
    if os.path.exists(list_page):
        with open(list_page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for filename, img_url in image_mapping.items():
            # In products.html, the links are like href="/products/xxx.html"
            # And the image is inside the article card.
            # Match the card containing the link to the product
            # Use regex to find the article block containing that specific product link
            pattern = fr'<article class="card">.*?<a href="/products/{filename}".*?<img src="/assets/img/products/.*?".*?</article>'
            # This is hard to do with simple replace. Let's do a targeted replace for each img tag.
            # Search for the img tag immediately followed by the card-body containing the title/link
            # Actually, simpler: search for the image path that corresponds to the product name
            base_name = filename.replace('.html', '')
            local_img_pattern = fr'src="/assets/img/products/{base_name}-1\.jpg"'
            content = re.sub(local_img_pattern, f'src="{img_url}"', content)
        
        with open(list_page, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated products.html")

    # 2. Update all individual detail pages
    for filename, img_url in image_mapping.items():
        file_path = os.path.join(products_dir, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace main image and all gallery placeholders
            # Pattern matches local paths like /assets/img/products/filename-1.jpg
            # OR the cloud URL if it was already updated but we want to be sure
            local_img_regex = r'src="(?:/assets/img/products/[^"]*?\.(?:jpg|png|svg)|https://sc02\.alicdn\.com/kf/[^"]*?)"'
            content = re.sub(local_img_regex, f'src="{img_url}"', content)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Verified & Updated: {filename}")

root_dir = 'C:/Users/Administrator/.accio/accounts/7072681770/agents/DID-D464A3-75D464A3U1779822-4477-D4AFAE/project/packaging_site'
update_all(root_dir)
