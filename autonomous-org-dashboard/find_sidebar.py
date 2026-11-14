with open(r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\admin.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if "sidebar" in l.lower() or "views" in l.lower() or "menu-item" in l.lower() or "nav-item" in l.lower():
        print(f"Line {i}: {l.strip()[:80]}")
