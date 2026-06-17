import os

def fix_broken_links(root_dir):
    # Mapping of identified broken links to their correct existing files
    correction_map = {
        '/products/pharmaceutical-serialization-packaging.html': '/products/pharmaceutical-serialization.html',
        '/products/collapsible-magnetic-gift-boxes.html': '/products/collapsible-magnetic-boxes.html',
        '/products/custom-bakery-pastry-boxes.html': '/products/bakery-pastry-boxes.html'
    }
    
    updated_files = 0
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                for broken, correct in correction_map.items():
                    new_content = new_content.replace(f'href="{broken}"', f'href="{correct}"')
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    updated_files += 1
                    print(f"Fixed links in: {file}")
    
    return updated_files

root_dir = 'C:/Users/Administrator/.accio/accounts/7072681770/agents/DID-D464A3-75D464A3U1779822-4477-D4AFAE/project/packaging_site'
count = fix_broken_links(root_dir)
print(f"Total files repaired: {count}")
