import os
import re

# Mapping for Batch 4
image_mapping = {
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

def force_replace_images(root_dir):
    updated_count = 0
    for filename, img_url in image_mapping.items():
        file_path = os.path.join(root_dir, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
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
print(f"Total files FORCE updated in Batch 4: {count}")
