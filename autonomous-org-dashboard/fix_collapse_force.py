with open(r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Make the toggleLogCollapse function collapse the whole bar cleanly
replacement_js = """    let isLogCollapsed = false;
    function toggleLogCollapse() {
      isLogCollapsed = !isLogCollapsed;
      const container = document.getElementById('logEntriesContainer');
      const btn = document.getElementById('logToggleBtn');
      const chevron = document.getElementById('logChevron');
      
      if (container) {
        if (isLogCollapsed) {
          container.style.cssText = 'display: none !important;';
          if (btn) btn.innerText = 'Expand ▼';
          if (chevron) chevron.innerText = '▶';
        } else {
          container.style.cssText = 'display: block !important; margin-top: 6px;';
          if (btn) btn.innerText = 'Collapse ▲';
          if (chevron) chevron.innerText = '▼';
        }
      }
    }"""

import re
text = re.sub(r'let isLogCollapsed = false;.*?function toggleLogCollapse\(\) \{.*?\n    \}', replacement_js, text, flags=re.DOTALL)

with open(r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated with force display style!")
