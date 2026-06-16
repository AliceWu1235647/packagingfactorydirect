import os
import re

schema_template = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Packaging Factory Direct",
  "image": "https://packagingfactorydirect.com/assets/logo.png",
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
  "description": "Professional B2B manufacturer specializing in custom packaging boxes, gift boxes, foldable magnetic boxes, paper bags, pharmaceutical packaging, and food-grade containers.",
  "knowsAbout": [
    "Custom Packaging Design",
    "Eco-friendly Materials",
    "B2B Wholesale Supply Chain",
    "Sustainable Printing Solutions",
    "Pharmaceutical Serialization Packaging",
    "Luxury Gift Box Manufacturing"
  ]
}
</script>"""

def update_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace existing JSON-LD
    new_content = re.sub(r'<script type="application/ld\+json">.*?</script>', schema_template, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

root_dir = 'C:/Users/Administrator/.accio/accounts/7072681770/agents/DID-D464A3-75D464A3U1779822-4477-D4AFAE/project/packaging_site'

updated_count = 0
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html'):
            if update_file(os.path.join(root, file)):
                updated_count += 1

print(f"Updated {updated_count} files.")
