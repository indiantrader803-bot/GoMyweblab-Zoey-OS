with open(r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Locate REAL-TIME AGENT TASK EXECUTION LOG section
target_str = "REAL-TIME AGENT TASK EXECUTION LOG"
idx = text.find(target_str)
print("Found target string at index:", idx)

# Check the surrounding container
box_start = text.rfind('<div class="team-log-bar"', 0, idx)
print("Log bar starts at:", box_start)

# We want to make it collapsible with a toggle button and clean CSS transition
old_log_section = text[box_start:text.find('</div>', text.find('</div>', text.find('</div>', idx) + 1) + 1) + 6]

new_collapsible_log = """  <!-- Collapsible Team Activity Log -->
  <div class="team-log-bar" id="teamLogBar" style="background:#ffffff; border-radius:14px; padding:8px 18px; box-shadow:0 4px 16px rgba(15,23,42,0.05); font-family:var(--font-mono); font-size:11px; margin-top:8px; transition:all 0.3s ease; position:relative; z-index:20;">
    <div class="log-top-row" style="display:flex; justify-content:space-between; align-items:center; cursor:pointer;" onclick="toggleLogCollapse()">
      <div style="display:flex; align-items:center; gap:8px;">
        <span id="logChevron" style="font-size:11px; transition:transform 0.3s; display:inline-block;">▼</span>
        <span style="font-weight:700; color:#475569; letter-spacing:0.5px;">REAL-TIME AGENT TASK EXECUTION LOG</span>
        <span class="live-dot" style="margin-left:4px;"></span>
      </div>
      <div style="display:flex; align-items:center; gap:14px; color:#94a3b8; font-size:10px;">
        <span>TASK PROGRESS • TIME SPENT • ESTIMATED COMPLETION • VERIFIED RESULTS</span>
        <button id="logToggleBtn" style="background:#f1f5f9; border:none; padding:2px 8px; border-radius:6px; font-size:10px; font-family:var(--font-mono); color:#475569; font-weight:700; cursor:pointer;">Collapse ▲</button>
      </div>
    </div>
    <div id="logEntriesContainer" style="max-height:85px; overflow-y:auto; transition:max-height 0.3s ease, opacity 0.3s ease; margin-top:6px;">
      <div class="log-entry-row" style="display:flex; align-items:center; gap:12px; padding:3px 0; color:#0f172a; font-size:11px;">
        <span class="log-time-stamp" style="color:#94a3b8;">19:42</span>
        <span class="log-tag-badge" style="background:#ede9fe; color:#7c3aed; font-size:9.5px; padding:1px 6px; border-radius:4px; font-weight:700;">PR Verifier</span>
        <span>• Completed OWASP security scan on PR #104 [95% Done] · Time spent: 40m · Est remaining: 2m</span>
      </div>
      <div class="log-entry-row" style="display:flex; align-items:center; gap:12px; padding:3px 0; color:#0f172a; font-size:11px;">
        <span class="log-time-stamp" style="color:#94a3b8;">19:40</span>
        <span class="log-tag-badge" style="background:#e0f2fe; color:#0284c7; font-size:9.5px; padding:1px 6px; border-radius:4px; font-weight:700;">Speed Tuner</span>
        <span>• Compressed asset pipeline for Client Site · Mobile score boosted to 96/100 · Time spent: 40m</span>
      </div>
      <div class="log-entry-row" style="display:flex; align-items:center; gap:12px; padding:3px 0; color:#0f172a; font-size:11px;">
        <span class="log-time-stamp" style="color:#94a3b8;">19:38</span>
        <span class="log-tag-badge" style="background:#d1fae5; color:#059669; font-size:9.5px; padding:1px 6px; border-radius:4px; font-weight:700;">FullStack Dev</span>
        <span>• Stripe webhook signature validation deployed [82% Done] · Time spent: 50m</span>
      </div>
    </div>
  </div>

  <script>
    let isLogCollapsed = false;
    function toggleLogCollapse() {
      isLogCollapsed = !isLogCollapsed;
      const container = document.getElementById('logEntriesContainer');
      const btn = document.getElementById('logToggleBtn');
      const chevron = document.getElementById('logChevron');
      
      if (isLogCollapsed) {
        container.style.maxHeight = '0px';
        container.style.opacity = '0';
        container.style.marginTop = '0px';
        btn.innerText = 'Expand ▼';
        chevron.style.transform = 'rotate(-90deg)';
      } else {
        container.style.maxHeight = '85px';
        container.style.opacity = '1';
        container.style.marginTop = '6px';
        btn.innerText = 'Collapse ▲';
        chevron.style.transform = 'rotate(0deg)';
      }
    }
  </script>"""

# Replace in index.html
if box_start != -1:
    end_box = text.find('<!-- Modal for User Auth', box_start)
    if end_box == -1:
        end_box = text.find('</body>', box_start)
    # Target replacing from box_start to just before </body>
    part_before = text[:box_start]
    part_after = text[text.find('</body>', box_start):]
    text = part_before + new_collapsible_log + '\n' + part_after
    
    with open(r"c:\Users\karth\OneDrive\Desktop\GoMyweblab\autonomous-org-dashboard\index.html", "w", encoding="utf-8") as f:
        f.write(text)
    print("Successfully replaced log section with collapsible component!")
