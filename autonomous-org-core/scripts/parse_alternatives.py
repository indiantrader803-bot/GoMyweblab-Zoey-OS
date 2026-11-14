import re
import json

readme_path = r'c:\Users\karth\OneDrive\Desktop\GoMyweblab\open-source-alternatives\README.md'
out_path = r'c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-core\data\open_source_alternatives.json'

with open(readme_path, encoding='utf-8') as f:
    content = f.read()

categories = []
current_cat = None

for line in content.splitlines():
    line = line.strip()
    if line.startswith('### '):
        cat_title = line[4:].strip()
        current_cat = {'category': cat_title, 'tools': []}
        categories.append(current_cat)
    elif line.startswith('[') and current_cat is not None and '|' in line:
        parts = line.split('|')
        if len(parts) >= 2:
            m_name = re.search(r'\[(.*?)\]\((.*?)\)', parts[0])
            m_site = re.search(r'\[(.*?)\]\((.*?)\)', parts[1])
            if m_name:
                name = m_name.group(1)
                github = m_name.group(2)
                site = m_site.group(2) if m_site else ''
                current_cat['tools'].append({
                    'name': name,
                    'github': github,
                    'website': site
                })

total_tools = sum(len(c['tools']) for c in categories)
print(f"Extracted {len(categories)} categories and {total_tools} open source alternatives!")

with open(out_path, 'w', encoding='utf-8') as out:
    json.dump(categories, out, indent=2)
