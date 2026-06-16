import os

# Mapping of product files to their new realistic image URLs
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
    "luxury-magnetic-gift-boxes.html": "https://sc02.alicdn.com/kf/A27de7768569e45a5a2ce89d4af2d21c5d.png"
}

def update_product_images(root_dir):
    updated_count = 0
    for filename, img_url in image_mapping.items():
        file_path = os.path.join(root_dir, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Pattern to match the main product image (usually the first img or one with a placeholder)
            # In V3, it often looks like <img src="/assets/img/products/..."
            new_content = content.replace('/assets/img/products/placeholder.svg', img_url)
            
            # Backup: replace any .svg in the main product section if placeholder is different
            if new_content == content:
                 # Search for any SVG in the products folder path
                 import re
                 new_content = re.sub(r'src="/assets/img/products/.*?.svg"', f'src="{img_url}"', content)

            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                updated_count += 1
                print(f"Successfully updated: {filename}")
    return updated_count

products_dir = 'C:/Users/Administrator/.accio/accounts/7072681770/agents/DID-D464A3-75D464A3U1779822-4477-D4AFAE/project/packaging_site/products'
count = update_product_images(products_dir)
print(f"Total files updated in Batch 1: {count}")
