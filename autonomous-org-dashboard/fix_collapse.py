with open(r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Replace toggleLogCollapse to ensure target element exists and animates properly
old_fn = """    let isLogCollapsed = false;
    function toggleLogCollapse() {
      isLogCollapsed = !isLogCollapsed;
      const container = document.getElementById('logEntriesContainer');
      const btn = document.getElementById('logToggleBtn');
      const chevron = document.getElementById('logChevron');
      
      if (isLogCollapsed) {
        container.style.maxHeight = '0px';
        container.style.opacity = '0';
        container.style.marginTop = '0px';
        btn.innerText = 'Expand ▼';
        chevron.style.transform = 'rotate(-90deg)';
      } else {
        container.style.maxHeight = '85px';
        container.style.opacity = '1';
        container.style.marginTop = '6px';
        btn.innerText = 'Collapse ▲';
        chevron.style.transform = 'rotate(0deg)';
      }
    }"""

new_fn = """    let isLogCollapsed = false;
    function toggleLogCollapse() {
      isLogCollapsed = !isLogCollapsed;
      const container = document.getElementById('logEntriesContainer');
      const btn = document.getElementById('logToggleBtn');
      const chevron = document.getElementById('logChevron');
      
      if (container) {
        if (isLogCollapsed) {
          container.style.display = 'none';
          if (btn) btn.innerText = 'Expand ▼';
          if (chevron) chevron.innerText = '▶';
        } else {
          container.style.display = 'block';
          if (btn) btn.innerText = 'Collapse ▲';
          if (chevron) chevron.innerText = '▼';
        }
      }
    }"""

if old_fn in text:
    text = text.replace(old_fn, new_fn)
    print("Replaced toggle function with display toggle!")
else:
    print("Could not find exact old_fn, replacing via regex")
    import re
    text = re.sub(r'let isLogCollapsed = false;.*?function toggleLogCollapse\(\) \{.*?\n    \}', new_fn, text, flags=re.DOTALL)

with open(r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Saved updated index.html!")
