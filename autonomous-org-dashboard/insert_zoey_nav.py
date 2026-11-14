with open('autonomous-org-dashboard/admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = '<li class="nav-item active" onclick="switchPageView(\'dashboard\', this)">'
zoey_nav = '''<li class="nav-item" onclick="switchPageView('zoey', this)" style="border:1.5px solid #a855f7;background:linear-gradient(135deg, #f5f3ff 0%, #ede9fe 100%);margin-bottom:6px;">
            <div class="nav-left-content">
              <span style="font-size:16px;">✨</span>
              <span style="font-weight:800;color:#6d28d9;">ZOEY AI (COO)</span>
            </div>
            <span class="nav-badge-pill" style="background:#7c3aed;color:#fff;">ONLINE</span>
          </li>
          '''

html = html.replace(target, zoey_nav + target)
with open('autonomous-org-dashboard/admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Inserted ZOEY AI navigation into admin.html sidebar")
