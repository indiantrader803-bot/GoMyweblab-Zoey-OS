with open(r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Replace body CSS to guarantee full viewport fit
old_body_rule = """    body {
      background-color: var(--bg);
      background-image: 
        radial-gradient(circle at 10% 15%, rgba(219, 234, 254, 0.85), transparent 40%),
        radial-gradient(circle at 90% 15%, rgba(243, 232, 255, 0.85), transparent 40%),
        radial-gradient(circle at 50% 90%, rgba(220, 252, 231, 0.7), transparent 50%);
      color: var(--text-dark);
      font-family: var(--font-sans);
      min-height: 100vh;
      max-height: 100vh;
      padding: 14px 24px 14px;
      position: relative;
      overflow-x: hidden;
      overflow-y: auto;
      scrollbar-width: thin;
    }"""

new_body_rule = """    html, body {
      height: 100vh;
      max-height: 100vh;
      overflow: hidden;
      margin: 0;
      padding: 0;
    }
    body {
      background-color: var(--bg);
      background-image: 
        radial-gradient(circle at 10% 15%, rgba(219, 234, 254, 0.85), transparent 40%),
        radial-gradient(circle at 90% 15%, rgba(243, 232, 255, 0.85), transparent 40%),
        radial-gradient(circle at 50% 90%, rgba(220, 252, 231, 0.7), transparent 50%);
      color: var(--text-dark);
      font-family: var(--font-sans);
      padding: 12px 20px 10px;
      display: flex;
      flex-direction: column;
      box-sizing: border-box;
    }"""

if old_body_rule in text:
    text = text.replace(old_body_rule, new_body_rule)
    print("Replaced body rule!")
else:
    print("Old body rule not matched exactly, replacing via regex")
    import re
    text = re.sub(r'body\s*\{[^}]+\}', new_body_rule, text, count=1)

# Ensure layout flex-1 and fits
text = text.replace('class="dashboard-layout"', 'class="dashboard-layout" style="flex:1; display:grid; grid-template-columns: 210px 1fr; gap:12px; overflow:hidden;"')
text = text.replace('class="teams-main-grid"', 'class="teams-main-grid" style="display:grid; grid-template-columns: repeat(2, 1fr); gap:10px; overflow-y:auto; padding-right:4px; max-height: calc(100vh - 170px); scrollbar-width:thin;"')

with open(r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated index.html container constraints!")
