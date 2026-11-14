with open(r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\index.html", "r", encoding="utf-8") as f:
    grok_text = f.read()

with open(r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\admin.html", "r", encoding="utf-8") as f:
    orbit_text = f.read()

# 1. Extract modal HTML from index.html
start = grok_text.find("<!-- Modal for User Auth / Mandatory Access Gate -->")
end = grok_text.find("<!-- Top Navigation Header -->")
modal_html = grok_text[start:end]

# 2. Extract modal JS from index.html
js_start = grok_text.find("// Check Session & Enforce Login Access Gate")
js_end = grok_text.find("// Initial load and periodic refresh")
modal_js = grok_text[js_start:js_end]

# 3. Add to admin.html
if "<body>" in orbit_text:
    orbit_text = orbit_text.replace("<body>", "<body>\n" + modal_html)

script_block = f"""
<script>
{modal_js}
window.addEventListener('DOMContentLoaded', () => {{
    checkAuthStatus();
}});
</script>
"""

if "</body>" in orbit_text:
    orbit_text = orbit_text.replace("</body>", script_block + "\n</body>")

with open(r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\admin.html", "w", encoding="utf-8") as f:
    f.write(orbit_text)

print("Successfully injected auth lock modal and validation into admin.html!")
