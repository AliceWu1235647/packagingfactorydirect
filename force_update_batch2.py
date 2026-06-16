import os
import re

# Mapping for Batch 2
image_mapping = {
    "eight-side-seal-pouches.html": "https://sc02.alicdn.com/kf/Ad2b785bffcd24433aa0c393d8d19a16ax.png",
    "pet-food-stand-up-pouches.html": "https://sc02.alicdn.com/kf/A86354ebabb4444379c8cd58ee2a5e9dcY.png",
    "flat-bottom-coffee-bags.html": "https://sc02.alicdn.com/kf/A6447eaa791324d0d9cba5d21f9957a49w.png",
    "frosted-zipper-bags.html": "https://sc02.alicdn.com/kf/A6b99688276684f2ebc25e18fad05f655S.png",
    "custom-paper-bags.html": "https://sc02.alicdn.com/kf/A2cf10cc137604ef79e20db30b22865c8F.png",
    "cannabis-mylar-pouches.html": "https://sc02.alicdn.com/kf/A4faec152ad424b8582db86a95ff8001fY.png",
    "custom-food-packaging-boxes.html": "https://sc02.alicdn.com/kf/Aa8d0330e14124affaa2ea0293511432et.png",
    "custom-stand-up-pouches.html": "https://sc02.alicdn.com/kf/Ac5c3bb361fe641688d671ecf868ed9beR.png",
    "eco-friendly-coffee-pouches.html": "https://sc02.alicdn.com/kf/Abf04052dc1274f5cae1037852d3fe3c70.png",
    "paper-cups-food-containers.html": "https://sc02.alicdn.com/kf/A2466770076964989b327c47a7b422124E.png"
}

def force_replace_images(root_dir):
    updated_count = 0
    for filename, img_url in image_mapping.items():
        file_path = os.path.join(root_dir, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Force replace local paths and placeholders
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
print(f"Total files FORCE updated in Batch 2: {count}")
