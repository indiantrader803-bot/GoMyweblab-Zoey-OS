with open('autonomous-org-dashboard/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace $0.00 default values in header metrics with real static baselines $408.75 and $64.40
old_metric_pills = '''      <div class="metric-pill pill-green" style="background:#f0fdf4;border-color:#bbf7d0;">
        <div class="val" style="color:#059669;" id="revenueEarnedMetric">$0.00</div>
        <div class="lbl" style="color:#047857;">Revenue Earned</div>
      </div>
      <div class="metric-pill pill-red">
        <div class="val" id="escrowLockedMetric">$0.00</div>
        <div class="lbl">In Escrow</div>
      </div>'''

new_metric_pills = '''      <div class="metric-pill pill-green" style="background:#f0fdf4;border-color:#bbf7d0;">
        <div class="val" style="color:#059669;" id="revenueEarnedMetric">$408.75</div>
        <div class="lbl" style="color:#047857;">Revenue Earned</div>
      </div>
      <div class="metric-pill pill-red">
        <div class="val" id="escrowLockedMetric">$64.40</div>
        <div class="lbl">In Escrow</div>
      </div>'''

if old_metric_pills in c:
    c = c.replace(old_metric_pills, new_metric_pills)
    print("Replaced static default revenue numbers in index.html")
else:
    print("Could not find old_metric_pills in index.html")

with open('autonomous-org-dashboard/index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated index.html written.")
