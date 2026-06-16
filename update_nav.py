import os

def update_nav(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Target the menu div and add Home link if not present
    old_menu = '<div class="menu"><a href="/about.html">About Us</a>'
    new_menu = '<div class="menu"><a href="/">Home</a><a href="/about.html">About Us</a>'
    
    # Also handle alternate header patterns if any
    if '<a href="/">Home</a>' not in content:
        content = content.replace('<div class="menu">', '<div class="menu"><a href="/">Home</a>')
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

root_dir = 'C:/Users/Administrator/.accio/accounts/7072681770/agents/DID-D464A3-75D464A3U1779822-4477-D4AFAE/project/packaging_site'

count = 0
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html'):
            update_nav(os.path.join(root, file))
            count += 1

print(f"Updated navigation in {count} files.")
