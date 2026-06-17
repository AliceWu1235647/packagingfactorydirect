import os
import re

# Technical Specs per core category
specs_data = {
    "pharmaceutical": """
<table class="spec-table">
  <tr><th>Compliance</th><td>GS1, DSCSA, EU FMD, ISO 15378</td></tr>
  <tr><th>Material</th><td>Medical Grade Ivory Board (250-400gsm)</td></tr>
  <tr><th>VDP Capability</th><td>Data Matrix, QR Code, Unique Serial ID</td></tr>
  <tr><th>Printing Precision</th><td>600 DPI Digital / 200 LPI Offset</td></tr>
  <tr><th>Lead Time</th><td>Sample 24h, Mass Production 7-10 Days</td></tr>
</table>
""",
    "rigid-box": """
<table class="spec-table">
  <tr><th>Construction</th><td>1200gsm Solid Greyboard (A-Grade)</td></tr>
  <tr><th>Closure</th><td>High-Strength Concealed Neodymium Magnets</td></tr>
  <tr><th>Folding Logic</th><td>Collapsible 4-Corner 3M Adhesive Style</td></tr>
  <tr><th>Finish Options</th><td>Soft-Touch, Gold Foil, Spot UV, Emboss</td></tr>
  <tr><th>Sustainability</th><td>100% Recyclable FSC Certified Paper</td></tr>
</table>
""",
    "pouch": """
<table class="spec-table">
  <tr><th>Barrier Level</th><td>High-Barrier OTR & WVTR (Foil Lined)</td></tr>
  <tr><th>Material Layers</th><td>PET/AL/PE, PET/NY/PE, MOPP/VMPET/PE</td></tr>
  <tr><th>Safety Standards</th><td>FDA Approved, BPA Free, SGS Certified</td></tr>
  <tr><th>Customization</th><td>One-way Valve, Resealable Zipper, Euro-hole</td></tr>
  <tr><th>Print Method</th><td>HD Rotogravure or Indigo Digital Print</td></tr>
</table>
"""
}

def inject_spec_tables(root_dir):
    products_dir = os.path.join(root_dir, 'products')
    updated = 0
    for filename in os.listdir(products_dir):
        if not filename.endswith('.html'): continue
        
        file_path = os.path.join(products_dir, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Decide which spec table to inject based on filename
        table_html = ""
        if 'pharma' in filename or 'medical' in filename:
            table_html = specs_data['pharmaceutical']
        elif 'magnetic' in filename or 'rigid' in filename or 'gift-box' in filename:
            table_html = specs_data['rigid-box']
        elif 'pouch' in filename or 'bag' in filename:
            table_html = specs_data['pouch']
        
        if table_html and 'spec-table' not in content:
            # Inject before the button or end of main content
            insertion_point = content.find('</ul>')
            if insertion_point != -1:
                insertion_point += 5
                new_content = content[:insertion_point] + "\n<h3>Technical Specifications</h3>\n" + table_html + content[insertion_point:]
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                updated += 1
    return updated

root_dir = 'C:/Users/Administrator/.accio/accounts/7072681770/agents/DID-D464A3-75D464A3U1779822-4477-D4AFAE/project/packaging_site'
count = inject_spec_tables(root_dir)
print(f"Injected spec tables into {count} pages.")
