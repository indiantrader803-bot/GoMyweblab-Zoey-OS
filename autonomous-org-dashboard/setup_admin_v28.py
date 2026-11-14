import re
import os

source_path = r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\index_orbit_backup.html"
target_path = r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\admin.html"

with open(source_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update identity to Arnab across the board
text = text.replace("director@gomyweblab.com", "arnab@gomyweblab.ai")
text = text.replace("director", "arnab")
text = text.replace("admin123", "arnab123")
text = text.replace("Karthik", "Arnab")
text = text.replace("karthik", "arnab")

# 2. Update UPI settlement to 8240438062@superyes
text = re.sub(r'[\w\.-]+@(?:okaxis|oksbi|paytm|upi|superyes)', '8240438062@superyes', text)

# 3. Add Top Bar Navigation to easily switch between Grok Teams and Admin V28
nav_pill = """
<div style="position:fixed; top:12px; right:20px; z-index:99999; display:flex; gap:8px; background:rgba(15,23,42,0.9); backdrop-filter:blur(8px); padding:6px 12px; border-radius:12px; border:1px solid rgba(255,255,255,0.15); box-shadow:0 4px 16px rgba(0,0,0,0.2);">
  <a href="/" style="color:#38bdf8; text-decoration:none; font-size:12px; font-weight:700; padding:3px 8px; border-radius:6px; background:rgba(56,189,248,0.15);">🏠 Homepage (Grok Teams)</a>
  <span style="color:#64748b; line-height:24px;">|</span>
  <span style="color:#ffffff; font-size:12px; font-weight:700; padding:3px 8px; border-radius:6px; background:#0284c7;">📊 Admin Deck (Orbit V28)</span>
  <span style="color:#64748b; line-height:24px;">|</span>
  <span style="color:#10b981; font-size:11px; font-weight:700; padding:3px 8px;">UPI: 8240438062@superyes</span>
</div>
"""

if "</body>" in text:
    text = text.replace("</body>", nav_pill + "\n</body>")

with open(target_path, "w", encoding="utf-8") as f:
    f.write(text)

print("admin.html created and configured successfully!")
