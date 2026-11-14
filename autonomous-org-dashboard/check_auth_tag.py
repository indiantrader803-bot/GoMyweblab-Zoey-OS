with open(r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = re.findall(r'<div[^>]*id=["\']authModal["\'][^>]*>', text)
print("authModal tags found:", matches)
