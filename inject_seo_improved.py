import os
import re

# Comprehensive Schema.org JSON-LD for B2B Packaging Factory
schema_template = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Packaging Factory Direct",
  "image": "https://packagingfactorydirect.com/assets/img/hero-main.png",
  "@id": "https://packagingfactorydirect.com",
  "url": "https://packagingfactorydirect.com",
  "telephone": "+86-18165730353",
  "email": "linda@colorprintingpackage.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Custom Packaging Industrial Park",
    "addressLocality": "Shenzhen",
    "addressRegion": "Guangdong",
    "postalCode": "518000",
    "addressCountry": "CN"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 22.5431,
    "longitude": 114.0579
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday"
    ],
    "opens": "09:00",
    "closes": "18:00"
  },
  "description": "Leading B2B custom packaging manufacturer specializing in pharmaceutical serialization, luxury gift boxes, food-grade containers, and flexible packaging solutions.",
  "sameAs": [
    "https://www.linkedin.com/company/packagingfactorydirect"
  ],
  "knowsAbout": [
    "Custom Packaging Design",
    "Pharmaceutical Serialization GS1",
    "B2B Wholesale Packaging",
    "Sustainable Printing Solutions",
    "VDP Variable Data Printing"
  ]
}
</script>"""

def inject_seo(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Inject JSON-LD if not exists
    if 'application/ld+json' not in content:
        content = content.replace('</head>', f'{schema_template}\n</head>')
    
    # 2. Add OG Tags for AI/Social sharing
    og_tags = """
<meta property="og:title" content="Packaging Factory Direct | Custom B2B Packaging Manufacturer">
<meta property="og:description" content="Factory-direct custom packaging for pharma, food, and luxury brands. Low MOQ, GS1 compliant, and global shipping.">
<meta property="og:url" content="https://packagingfactorydirect.com/">
<meta property="og:type" content="website">
<meta property="og:image" content="https://packagingfactorydirect.com/assets/img/hero-main.png">
"""
    if 'og:title' not in content:
        content = content.replace('</head>', f'{og_tags}\n</head>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

root_dir = 'C:/Users/Administrator/.accio/accounts/7072681770/agents/DID-D464A3-75D464A3U1779822-4477-D4AFAE/project/packaging_site'

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html'):
            inject_seo(os.path.join(root, file))

print("SEO & AI optimization injected into all HTML files.")
