with open(r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\index.html", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace('id="authModal" style="display: flex;"', 'id="authModal" style="display: none;"')
text = text.replace('id="authModal" style="display:flex;"', 'id="authModal" style="display: none;"')

with open(r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Replaced authModal style!")
