import os

def fix_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update navigation links to directory style
    original = content
    content = content.replace('href="/blog.html"', 'href="/blog/"')
    content = content.replace('href="/news.html"', 'href="/news/"')
    content = content.replace('href="/blog"', 'href="/blog/"')
    content = content.replace('href="/news"', 'href="/news/"')
    
    # Fix potential double slashes
    content = content.replace('href="/blog//"', 'href="/blog/"')
    content = content.replace('href="/news//"', 'href="/news/"')

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

root_dir = 'C:/Users/Administrator/.accio/accounts/7072681770/agents/DID-D464A3-75D464A3U1779822-4477-D4AFAE/project/packaging_site'
count = 0
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html'):
            if fix_links(os.path.join(root, file)):
                count += 1

print(f"Updated links in {count} files.")
