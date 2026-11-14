with open(r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Locate Multi-Page View Navigation Bar
start_comment = "<!-- Multi-Page View Navigation Bar -->"
idx_start = text.find(start_comment)

if idx_start != -1:
    idx_end = text.find("</nav>", idx_start) + 6
    text = text[:idx_start] + text[idx_end:]
    print("Found and removed Multi-Page View Navigation Bar!")
else:
    print("Comment not found, searching for <nav")
    import re
    text = re.sub(r'<nav[^>]*>.*?</nav>', '', text, flags=re.DOTALL)

with open(r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Saved updated index.html without multi-page bar!")
