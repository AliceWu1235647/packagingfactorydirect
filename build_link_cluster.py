import os

def link_blog_to_products(root_dir):
    blog_dir = os.path.join(root_dir, 'blog')
    cases_dir = os.path.join(root_dir, 'cases')
    
    # Internal linking blocks
    links_html = """
<div class="internal-linking">
  <h4>Related Custom Packaging Solutions</h4>
  <div class="links-grid">
    <a href="/products/pharmaceutical-serialization.html">&rarr; GS1 Pharmaceutical Boxes</a>
    <a href="/products/collapsible-magnetic-boxes.html">&rarr; Custom Magnetic Gift Boxes</a>
    <a href="/products/pet-food-packaging-bags.html">&rarr; High Barrier Pouches</a>
    <a href="/solutions/">&rarr; View All Industry Solutions</a>
  </div>
</div>
"""
    
    updated = 0
    # Process Blog and Cases
    for folder in [blog_dir, cases_dir]:
        if not os.path.exists(folder): continue
        for filename in os.listdir(folder):
            if filename.endswith('.html') and filename != 'index.html':
                file_path = os.path.join(folder, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if 'internal-linking' not in content:
                    insertion_point = content.find('</div></section></main>')
                    if insertion_point != -1:
                        new_content = content[:insertion_point] + links_html + content[insertion_point:]
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        updated += 1
    return updated

root_dir = 'C:/Users/Administrator/.accio/accounts/7072681770/agents/DID-D464A3-75D464A3U1779822-4477-D4AFAE/project/packaging_site'
count = link_blog_to_products(root_dir)
print(f"Created internal link clusters in {count} content pages.")
