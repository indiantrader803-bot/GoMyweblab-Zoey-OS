with open(r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\admin.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
views = re.findall(r'id=["\']view-([^"\']+)["\']', text)
print("Views in admin.html:", set(views))

# Check sidebar menu buttons
buttons = re.findall(r'switchView\(["\']([^"\']+)["\']\)', text)
print("Sidebar switchView targets:", set(buttons))
