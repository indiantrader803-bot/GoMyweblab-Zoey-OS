import re

source = r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\orbit_v28_raw.html"
target = r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\admin.html"

with open(source, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update identity to Arnab
text = text.replace("Karthik · Director", "Arnab · Director")
text = text.replace("Karthik", "Arnab")
text = text.replace("karthik", "arnab")
text = text.replace("director@gomyweblab.com", "arnab@gomyweblab.ai")
text = text.replace("admin123", "arnab123")
text = text.replace("gomyweblab@upi", "8240438062@superyes")

# 2. Strict Auth Lock check
auth_check = """
  <script>
    function checkAdminAuth() {
      const user = localStorage.getItem('gomyweblab_user');
      const token = localStorage.getItem('gomyweblab_token');
      const authModal = document.getElementById('authModal');
      if (!user || !token) {
        if (authModal) {
          authModal.style.display = 'flex';
          document.body.style.overflow = 'hidden';
        }
      } else {
        if (authModal) {
          authModal.style.display = 'none';
          document.body.style.overflow = 'auto';
        }
      }
    }
    window.addEventListener('DOMContentLoaded', () => {
      checkAdminAuth();
    });
    function logoutAdmin() {
      localStorage.removeItem('gomyweblab_user');
      localStorage.removeItem('gomyweblab_token');
      location.reload();
    }
  </script>
"""

# 3. Top portal switcher bar
top_bar = """
<div style="position:fixed; top:12px; right:20px; z-index:99999; display:flex; gap:8px; background:rgba(15,23,42,0.92); backdrop-filter:blur(10px); padding:6px 14px; border-radius:14px; border:1px solid rgba(255,255,255,0.18); box-shadow:0 6px 20px rgba(0,0,0,0.25); align-items:center;">
  <a href="/" style="color:#38bdf8; text-decoration:none; font-size:12px; font-weight:700; padding:4px 10px; border-radius:8px; background:rgba(56,189,248,0.15);">🏠 Homepage (Grok Teams)</a>
  <span style="color:#64748b;">|</span>
  <span style="color:#ffffff; font-size:12px; font-weight:800; padding:4px 10px; border-radius:8px; background:#10b981;">📊 Admin Deck (Orbit V28)</span>
  <span style="color:#64748b;">|</span>
  <span style="color:#a7f3d0; font-size:11px; font-family:monospace; font-weight:700;">UPI: 8240438062@superyes</span>
  <span style="color:#64748b;">|</span>
  <button onclick="logoutAdmin()" style="background:#ef4444; color:#fff; border:none; padding:4px 10px; font-size:11px; font-weight:700; border-radius:6px; cursor:pointer;">Sign Out</button>
</div>
"""

if "</head>" in text:
    text = text.replace("</head>", auth_check + "\n</head>")
if "</body>" in text:
    text = text.replace("</body>", top_bar + "\n</body>")

with open(target, "w", encoding="utf-8") as f:
    f.write(text)

print("admin.html (Orbit Dashboard V28) configured and locked successfully!")
