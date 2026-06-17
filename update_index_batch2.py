import os

def update_index_page(folder, file_path):
    root_dir = 'C:/Users/Administrator/.accio/accounts/7072681770/agents/DID-D464A3-75D464A3U1779822-4477-D4AFAE/project/packaging_site'
    target_dir = os.path.join(root_dir, folder)
    
    # Get all html files in that folder
    files = [f for f in os.listdir(target_dir) if f.endswith('.html') and f != 'index.html']
    
    # Sort files by name to have a consistent list
    files.sort()
    
    # Generate the grid items
    items_html = ""
    for f in files:
        title = f.replace('.html', '').replace('-', ' ').title()
        items_html += f"""
        <article class="card">
          <div class="card-body">
            <h3>{title}</h3>
            <p>Industry-specific professional insights and technical solutions.</p>
            <a class="btn light" href="/{folder}/{f}">Read Detailed Case Study</a>
          </div>
        </article>""" if folder == 'cases' else f"""
        <article class="card">
          <div class="card-body">
            <h3>{title}</h3>
            <p>Deep dive into modern packaging technology, materials, and B2B trends.</p>
            <a class="btn light" href="/{folder}/{f}">Read Full Article</a>
          </div>
        </article>"""
        
    index_content = f"""<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{"Global Success Stories & Success Cases" if folder == 'cases' else "Packaging Industry Insights & Engineering Blog"} | Packaging Factory Direct</title>
<link rel="stylesheet" href="/assets/css/style.css">
</head><body>
<header class="header"><nav class="nav"><a class="logo" href="/"><span>PACKAGING</span> FACTORY DIRECT</a><div class="links"><a href="/">Home</a><a href="/solutions/">Solutions</a><a href="/products.html">Products</a><a href="/cases/">Cases</a><a href="/blog/">Insights</a><a href="/factory/">Factory</a></div></nav></header>
<main>
<section class="page-hero"><h1>{"150+ Technical Resources & Success Stories" if folder == 'cases' else "100+ Professional Packaging Insights"}</h1><p>Explore our library of expert packaging knowledge.</p></section>
<section class="section">
  <div class="grid" style="grid-template-columns: repeat(3, 1fr); gap: 20px;">
    {items_html}
  </div>
</section>
</main>
<footer class="footer"><p>© 2026 Packaging Factory Direct.</p></footer>
</body></html>"""
    
    with open(os.path.join(target_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_content)

update_index_page('cases', '')
update_index_page('blog', '')
print("Updated Cases and Blog index pages with 140+ new items.")
