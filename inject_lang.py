import os

def add_language_switcher(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple language switcher HTML
    switcher_html = """
    <div class="lang-switcher" style="position:relative; display:inline-block; margin-left:20px;">
        <button class="btn light" style="padding:8px 15px; font-size:13px;">🌐 Language ▼</button>
        <div class="lang-dropdown" style="display:none; position:absolute; background:#fff; border:1px solid #eee; border-radius:10px; box-shadow:0 10px 30px rgba(0,0,0,0.1); width:120px; z-index:100;">
            <a href="/" style="display:block; padding:10px; font-size:13px; border-bottom:1px solid #f9f9f9;">English</a>
            <a href="/fr/" style="display:block; padding:10px; font-size:13px; border-bottom:1px solid #f9f9f9;">Français</a>
            <a href="/de/" style="display:block; padding:10px; font-size:13px; border-bottom:1px solid #f9f9f9;">Deutsch</a>
            <a href="/es/" style="display:block; padding:10px; font-size:13px;">Español</a>
        </div>
        <style>
            .lang-switcher:hover .lang-dropdown { display:block; }
        </style>
    </div>
    """
    
    # Also add hreflang tags for SEO
    hreflang_tags = """
<link rel="alternate" hreflang="x-default" href="https://packagingfactorydirect.com/">
<link rel="alternate" hreflang="en" href="https://packagingfactorydirect.com/">
<link rel="alternate" hreflang="fr" href="https://packagingfactorydirect.com/fr/">
<link rel="alternate" hreflang="de" href="https://packagingfactorydirect.com/de/">
<link rel="alternate" hreflang="es" href="https://packagingfactorydirect.com/es/">
"""
    
    # 1. Inject hreflang in head
    if 'hreflang' not in content:
        content = content.replace('</head>', f'{hreflang_tags}\n</head>')
    
    # 2. Inject switcher in nav links
    if 'lang-switcher' not in content:
        if '<div class="links">' in content:
            content = content.replace('</div><a class="btn gold"', f'{switcher_html}</div><a class="btn gold"')
        elif '<div class="menu">' in content:
            content = content.replace('</div><a class="btn gold"', f'{switcher_html}</div><a class="btn gold"')
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

root_dir = 'C:/Users/Administrator/.accio/accounts/7072681770/agents/DID-D464A3-75D464A3U1779822-4477-D4AFAE/project/packaging_site'
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html'):
            add_language_switcher(os.path.join(root, file))

print("Injected language switcher and hreflang tags into all pages.")
