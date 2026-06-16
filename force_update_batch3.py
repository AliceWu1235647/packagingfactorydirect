import os
import re

# Mapping for Batch 3
image_mapping = {
    "bakery-pastry-boxes.html": "https://sc02.alicdn.com/kf/Aff26a23be2d8441f9c224458d042cdceL.png",
    "books-catalogs-manuals.html": "https://sc02.alicdn.com/kf/A87c62bb2834c4ffd93cb2df99a42f8c7O.png",
    "burger-boxes-wraps.html": "https://sc02.alicdn.com/kf/A811d9b1794514069bfa4f03d70c34981U.png",
    "cards-stickers-labels.html": "https://sc02.alicdn.com/kf/Ae517a60cc9014358b551e1c5241bb07ej.png",
    "coffee-paper-cups.html": "https://sc02.alicdn.com/kf/A3bac7971d3e2429781149fe10396fe964.png",
    "custom-folding-carton-boxes.html": "https://sc02.alicdn.com/kf/Afb4e3cd0a8484ea2838eed15f0205d746.png",
    "donut-packaging-sets.html": "https://sc02.alicdn.com/kf/A7f737cfa15b34fca9d809d8a73074730w.png",
    "eco-kraft-mailer-boxes.html": "https://sc02.alicdn.com/kf/Aa9241935a83141abac6b11ff489e090aE.png",
    "food-packaging-boxes.html": "https://sc02.alicdn.com/kf/A878df6de61554bb785c7f98a7922cadbJ.png",
    "fried-chicken-boxes.html": "https://sc02.alicdn.com/kf/A5b7d64e5253540bfbdb2f18d99642d8fI.png"
}

def force_replace_images(root_dir):
    updated_count = 0
    for filename, img_url in image_mapping.items():
        file_path = os.path.join(root_dir, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Pattern to match local image paths in V3 and replace them
            pattern = r'src="/assets/img/products/[^"]*?\.(?:jpg|png|svg)"'
            new_content = re.sub(pattern, f'src="{img_url}"', content)
            
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                updated_count += 1
                print(f"FORCED UPDATE SUCCESS: {filename}")
    return updated_count

products_dir = 'C:/Users/Administrator/.accio/accounts/7072681770/agents/DID-D464A3-75D464A3U1779822-4477-D4AFAE/project/packaging_site/products'
count = force_replace_images(products_dir)
print(f"Total files FORCE updated in Batch 3: {count}")
