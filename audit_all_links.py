import os
import re

def get_all_html_files(root_dir):
    html_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files

def audit_links(root_dir):
    all_files = get_all_html_files(root_dir)
    broken_links = []
    
    # Files that physically exist
    existing_paths = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            full_path = os.path.join(root, file).replace('\\', '/')
            rel_path = '/' + os.path.relpath(full_path, root_dir).replace('\\', '/')
            existing_paths.append(rel_path)
            # Add directory style too
            if file == 'index.html':
                existing_paths.append(rel_path.replace('index.html', ''))

    for file_path in all_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all local hrefs
        links = re.findall(r'href="(/[^"]*?)"', content)
        for link in links:
            # Strip anchors and queries
            clean_link = link.split('#')[0].split('?')[0]
            if clean_link == '/': continue
            
            # Check existence
            if clean_link not in existing_paths and clean_link + '.html' not in existing_paths and not any(clean_link.endswith(ext) for ext in ['.com', '.net', '.org']):
                broken_links.append((os.path.relpath(file_path, root_dir), link))
                
    return broken_links

root_dir = 'C:/Users/Administrator/.accio/accounts/7072681770/agents/DID-D464A3-75D464A3U1779822-4477-D4AFAE/project/packaging_site'
results = audit_links(root_dir)

if results:
    print(f"Found {len(results)} potentially broken links:")
    for file, link in results:
        print(f"File: {file} -> Link: {link}")
else:
    print("No broken internal links found.")
