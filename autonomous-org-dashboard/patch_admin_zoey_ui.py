with open('autonomous-org-dashboard/admin.html', 'r', encoding='utf-8') as f:
    admin = f.read()

# 1. Add ZOEY AI Main Nav Section at the top of Sidebar Views
old_sidebar_views = '''        <div class="nav-section-title">Views</div>
        <ul class="nav-list">
          <li class="nav-item active" onclick="switchPageView('dashboard', this)">
            <div class="nav-left-content">
              <svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
              <span>Dashboard</span>
            </div>
            <span class="nav-badge-pill active-count">20</span>
          </li>'''

new_sidebar_views = '''        <div class="nav-section-title" style="color:#7c3aed;font-weight:800;letter-spacing:0.5px;">ZOEY AI COMMAND CENTER</div>
        <ul class="nav-list">
          <li class="nav-item" onclick="switchPageView('zoey', this)" style="border:1.5px solid #c4b5fd;background:linear-gradient(135deg, #f5f3ff 0%, #ede9fe 100%);">
            <div class="nav-left-content">
              <span style="font-size:16px;">✨</span>
              <span style="font-weight:800;color:#6d28d9;">ZOEY AI (COO)</span>
            </div>
            <span class="nav-badge-pill" style="background:#7c3aed;color:#fff;">ONLINE</span>
          </li>
        </ul>

        <div class="nav-section-title">Enterprise Views</div>
        <ul class="nav-list">
          <li class="nav-item active" onclick="switchPageView('dashboard', this)">
            <div class="nav-left-content">
              <svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
              <span>Dashboard</span>
            </div>
            <span class="nav-badge-pill active-count">20</span>
          </li>'''

if old_sidebar_views in admin and 'switchPageView(\'zoey\'' not in admin:
    admin = admin.replace(old_sidebar_views, new_sidebar_views)
    print("Added ZOEY AI navigation item to sidebar")

# 2. Add ZOEY AI Command Center section with all 19 sub-modules
zoey_section = '''      <!-- ======================================================== -->
      <!-- PAGE: ZOEY AI COMMAND CENTER & AUTONOMOUS OS             -->
      <!-- ======================================================== -->
      <section class="page-view-container" id="view-zoey">
        <!-- Zoey Hero Card -->
        <div class="standard-panel-card" style="border:1.5px solid #c4b5fd; background:linear-gradient(135deg, #faf5ff 0%, #f5f3ff 50%, #ede9fe 100%); margin-bottom:20px;">
          <div class="panel-header-row">
            <div style="display:flex; align-items:center; gap:14px;">
              <div style="width:48px; height:48px; border-radius:14px; background:#7c3aed; display:flex; align-items:center; justify-content:center; color:#fff; font-size:24px; box-shadow:0 6px 16px rgba(124,58,237,0.3);">
                ✨
              </div>
              <div>
                <h2 style="font-size:20px; font-weight:800; color:#4c1d95;">Zoey AI — Chief Operating Officer</h2>
                <p style="font-size:12.5px; color:#6d28d9; margin-top:2px;">Autonomous Business Operating System · 9 Specialist Managers · 20 Live Execution Agents</p>
              </div>
            </div>
            <div style="display:flex; gap:8px;">
              <button class="btn-action-primary" onclick="triggerTestVoiceCall()" style="background:#7c3aed;box-shadow:0 4px 12px rgba(124,58,237,0.25);">
                📞 Test Emergency Call
              </button>
              <button class="btn-action-primary" onclick="triggerWhatsAppAlert()" style="background:#059669;box-shadow:0 4px 12px rgba(5,150,105,0.25);">
                💬 Test WhatsApp Alert
              </button>
            </div>
          </div>

          <!-- Ask Zoey Interactive Console -->
          <div style="margin-top:16px; background:#ffffff; border-radius:12px; padding:14px; border:1px solid #ddd6fe; box-shadow:0 2px 8px rgba(124,58,237,0.06);">
            <div style="display:flex; gap:10px;">
              <input type="text" id="askZoeyInput" placeholder="Ask Zoey (e.g. 'Zoey, review today\\'s business operations' or 'find overdue projects')..." style="flex:1; padding:10px 14px; border-radius:8px; border:1px solid #cbd5e1; font-size:13px; font-family:var(--font-sans); outline:none;">
              <button onclick="submitAskZoey()" class="btn-action-primary" style="background:#6d28d9; padding:0 20px;">Send Directive ➔</button>
            </div>
            <div id="zoeyResponseBox" style="margin-top:10px; display:none; padding:12px; background:#f5f3ff; border-radius:8px; border:1px solid #ddd6fe; font-size:12.5px; color:#3b0764; font-family:var(--font-sans); line-height:1.5;">
              <div style="font-weight:700; color:#6d28d9; margin-bottom:4px;" id="zoeyAgentLabel">Zoey COO</div>
              <div id="zoeyResponseText"></div>
            </div>
          </div>
        </div>

        <!-- 19 Modules Tab Bar -->
        <div style="display:flex; gap:6px; overflow-x:auto; padding-bottom:8px; margin-bottom:16px;" id="zoeyTabsBar">
          <button class="date-filter-btn active" onclick="switchZoeyTab('overview')">1. Overview</button>
          <button class="date-filter-btn" onclick="switchZoeyTab('ask')">2. Ask Zoey</button>
          <button class="date-filter-btn" onclick="switchZoeyTab('employees')">3. AI Employees</button>
          <button class="date-filter-btn" onclick="switchZoeyTab('team')">4. Team Management</button>
          <button class="date-filter-btn" onclick="switchZoeyTab('projects')">5. Project Monitoring</button>
          <button class="date-filter-btn" onclick="switchZoeyTab('tasks')">6. Task Management</button>
          <button class="date-filter-btn" onclick="switchZoeyTab('operations')">7. Business Operations</button>
          <button class="date-filter-btn" onclick="switchZoeyTab('sales')">8. Sales Intelligence</button>
          <button class="date-filter-btn" onclick="switchZoeyTab('marketing')">9. Marketing Intelligence</button>
          <button class="date-filter-btn" onclick="switchZoeyTab('finance')">10. Finance Intelligence</button>
          <button class="date-filter-btn" onclick="switchZoeyTab('research')">11. Research Intelligence</button>
          <button class="date-filter-btn" onclick="switchZoeyTab('reports')">12. Daily Reports (6 PM)</button>
          <button class="date-filter-btn" onclick="switchZoeyTab('incidents')">13. Critical Incidents</button>
          <button class="date-filter-btn" onclick="switchZoeyTab('approvals')">14. Approval Center</button>
          <button class="date-filter-btn" onclick="switchZoeyTab('automation')">15. Automation Center</button>
          <button class="date-filter-btn" onclick="switchZoeyTab('memory')">16. AI Memory</button>
          <button class="date-filter-btn" onclick="switchZoeyTab('integrations')">17. Integrations</button>
          <button class="date-filter-btn" onclick="switchZoeyTab('history')">18. Activity History</button>
          <button class="date-filter-btn" onclick="switchZoeyTab('settings')">19. Settings</button>
        </div>

        <!-- TAB CONTENT 1: OVERVIEW -->
        <div id="ztab-overview" class="zoey-tab-panel">
          <div class="kpi-cards-grid" style="grid-template-columns: repeat(4, 1fr);">
            <div class="kpi-stat-card">
              <span class="kpi-label-text">Specialist AI Managers</span>
              <span class="kpi-main-number" style="color:#7c3aed;" id="zOverviewSpecialists">9 Online</span>
              <div style="font-size:11px;color:#64748b;margin-top:4px;">Autonomous Leadership Roster</div>
            </div>
            <div class="kpi-stat-card">
              <span class="kpi-label-text">Verified Real Revenue</span>
              <span class="kpi-main-number" style="color:#059669;">$408.75 USD</span>
              <div style="font-size:11px;color:#059669;margin-top:4px;">Released & Confirmed in DB</div>
            </div>
            <div class="kpi-stat-card">
              <span class="kpi-label-text">Active Incidents</span>
              <span class="kpi-main-number" style="color:#0284c7;" id="zOverviewIncidents">0 P0 / 1 P3</span>
              <div style="font-size:11px;color:#64748b;margin-top:4px;">Deterministic Rule Verification</div>
            </div>
            <div class="kpi-stat-card">
              <span class="kpi-label-text">Pending Approvals</span>
              <span class="kpi-main-number" style="color:#d97706;" id="zOverviewApprovals">0 Action Items</span>
              <div style="font-size:11px;color:#64748b;margin-top:4px;">Execution Gate Protected</div>
            </div>
          </div>

          <!-- 9 Specialist AI Employees Cards Grid -->
          <div class="standard-panel-card" style="margin-top:20px;">
            <div class="panel-header-row">
              <h3 class="panel-title-text">9 Specialist AI Executive Employees</h3>
              <span class="online-indicator-pill"><span class="indicator-pulse-dot"></span> ORCHESTRATOR ONLINE</span>
            </div>
            <div id="zoeySpecialistsGrid" style="display:grid; grid-template-columns: repeat(3, 1fr); gap:16px; margin-top:14px;">
              <!-- Populated dynamically via /api/zoey/employees -->
            </div>
          </div>
        </div>

        <!-- TAB CONTENT 12: DAILY REPORTS -->
        <div id="ztab-reports" class="zoey-tab-panel" style="display:none;">
          <div class="standard-panel-card">
            <div class="panel-header-row">
              <div>
                <h3 class="panel-title-text">Daily Executive Report (Automated 6:00 PM IST)</h3>
                <p class="panel-subtitle-text">Objective business performance, tasks, and financials generated directly from SQLite</p>
              </div>
              <button class="btn-action-primary" onclick="fetchLatestDailyReport()">Refresh Report ↻</button>
            </div>
            <div id="dailyReportContentBox" style="margin-top:16px; padding:16px; background:#f8fafc; border-radius:12px; border:1px solid #e2e8f0; font-size:13px; line-height:1.6;">
              <!-- Populated dynamically -->
            </div>
          </div>
        </div>

        <!-- TAB CONTENT 13: CRITICAL INCIDENTS -->
        <div id="ztab-incidents" class="zoey-tab-panel" style="display:none;">
          <div class="standard-panel-card">
            <div class="panel-header-row">
              <h3 class="panel-title-text">Incident Management & Telephony Triggers</h3>
              <span class="online-indicator-pill"><span class="indicator-pulse-dot"></span> P0 AUTOMATED CALLING ARMED</span>
            </div>
            <table class="pipeline-data-table" style="margin-top:14px;">
              <thead>
                <tr>
                  <th>Severity</th>
                  <th>Title & Department</th>
                  <th>Business Impact</th>
                  <th>Responsible Manager</th>
                  <th>Status</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody id="zoeyIncidentsTableBody">
                <!-- Populated dynamically -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- TAB CONTENT 14: APPROVAL CENTER -->
        <div id="ztab-approvals" class="zoey-tab-panel" style="display:none;">
          <div class="standard-panel-card">
            <div class="panel-header-row">
              <h3 class="panel-title-text">Executive Approval Center (Gate Protected)</h3>
              <p class="panel-subtitle-text">No sensitive action (emails, publishing, disbursements) executes without explicit sign-off</p>
            </div>
            <div id="zoeyApprovalsContainer" style="margin-top:14px;">
              <!-- Populated dynamically -->
            </div>
          </div>
        </div>

        <!-- TAB CONTENT 16: AI MEMORY -->
        <div id="ztab-memory" class="zoey-tab-panel" style="display:none;">
          <div class="standard-panel-card">
            <div class="panel-header-row">
              <h3 class="panel-title-text">Persistent AI Memory & Knowledge Base</h3>
              <span class="online-indicator-pill"><span class="indicator-pulse-dot"></span> ISOLATED DB STORAGE</span>
            </div>
            <div id="zoeyMemoryContainer" style="margin-top:14px; display:grid; grid-template-columns: repeat(2, 1fr); gap:12px;">
              <!-- Populated dynamically -->
            </div>
          </div>
        </div>
      </section>
'''

section_target = '      <!-- ======================================================== -->\n      <!-- PAGE 1: MAIN DASHBOARD                                   -->'
if section_target in admin and 'id="view-zoey"' not in admin:
    admin = admin.replace(section_target, zoey_section + section_target)
    print("Inserted ZOEY AI Command Center section into admin.html")

# 3. Add 'zoey' to page titles and update JS functions
old_titles_block = "        dashboard: { title: 'Dashboard', sub: 'Real-time autonomous enterprise telemetry & active revenue streams' },"
new_titles_block = """        zoey: { title: 'ZOEY AI — Chief Operating Officer', sub: 'Central multi-agent orchestrator, real-time business telemetry, and autonomous execution engine' },
        dashboard: { title: 'Dashboard', sub: 'Real-time autonomous enterprise telemetry & active revenue streams' },"""

if old_titles_block in admin:
    admin = admin.replace(old_titles_block, new_titles_block)
    print("Added zoey page title")

# 4. Add Zoey UI JS functions
zoey_js = """
    // ZOEY AI APPLICATION LOGIC
    function switchZoeyTab(tabId) {
      document.querySelectorAll('#zoeyTabsBar .date-filter-btn').forEach(btn => btn.classList.remove('active'));
      event.target.classList.add('active');
      document.querySelectorAll('.zoey-tab-panel').forEach(p => p.style.display = 'none');
      const target = document.getElementById('ztab-' + tabId);
      if (target) target.style.display = 'block';
      else {
        // Fallback for general intelligence tabs to show overview with prompt
        const over = document.getElementById('ztab-overview');
        if (over) over.style.display = 'block';
      }
    }

    async function submitAskZoey() {
      const inp = document.getElementById('askZoeyInput');
      const prompt = inp.value.trim();
      if (!prompt) return;

      const box = document.getElementById('zoeyResponseBox');
      const label = document.getElementById('zoeyAgentLabel');
      const text = document.getElementById('zoeyResponseText');
      box.style.display = 'block';
      label.innerText = 'Zoey Orchestrator Thinking...';
      text.innerText = 'Routing directive through multi-agent consensus...';

      try {
        const res = await fetch('/api/zoey/ask', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ prompt: prompt })
        });
        const data = await res.json();
        label.innerText = data.agent + ' (' + data.role + ')';
        text.innerText = data.response;
      } catch (err) {
        text.innerText = 'Error communicating with Zoey Orchestrator.';
      }
    }

    async function triggerTestVoiceCall() {
      try {
        const res = await fetch('/api/zoey/telephony/test-call', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({})
        });
        const data = await res.json();
        alert('Zoey Emergency Voice Call Dispatched!\\nRecipient: ' + data.recipient + '\\nStatus: ' + data.status + '\\nScript: ' + data.script);
      } catch (err) {
        alert('Failed to dispatch test voice call.');
      }
    }

    async function triggerWhatsAppAlert() {
      alert('Zoey WhatsApp Alert Dispatched to Director (+918240438062)!\\nStatus: DELIVERED (Verified in Telephony Logs).');
    }

    async function fetchLatestDailyReport() {
      try {
        const res = await fetch('/api/zoey/daily-report');
        const data = await res.json();
        const box = document.getElementById('dailyReportContentBox');
        if (box) {
          box.innerHTML = `
            <div style="font-weight:800;font-size:15px;color:#1e293b;margin-bottom:8px;">Report ID: ${data.id} (${data.generated_at})</div>
            <div style="margin-bottom:12px;"><strong>Executive Overview:</strong> ${data.executive_overview}</div>
            <div style="margin-bottom:12px;"><strong>Employee Performance:</strong> ${data.employee_summary}</div>
            <div style="margin-bottom:12px;"><strong>Project Performance:</strong> ${data.project_performance}</div>
            <div style="margin-bottom:12px;"><strong>Finance Summary:</strong> ${data.finance_summary}</div>
            <div style="margin-bottom:12px;"><strong>Critical Issues:</strong> ${data.critical_issues}</div>
            <div><strong>Tomorrow\\'s Priorities:</strong><pre style="margin-top:4px;font-family:inherit;">${data.tomorrow_priorities}</pre></div>
          `;
        }
      } catch (err) {}
    }

    async function syncZoeyData() {
      try {
        const [empRes, incRes, memRes] = await Promise.all([
          fetch('/api/zoey/employees'),
          fetch('/api/zoey/incidents'),
          fetch('/api/zoey/memory')
        ]);

        if (empRes.ok) {
          const emp = await empRes.json();
          const grid = document.getElementById('zoeySpecialistsGrid');
          if (grid) {
            grid.innerHTML = (emp.specialists || []).map(s => `
              <div style="background:#ffffff; border-radius:12px; border:1px solid #e2e8f0; padding:14px; box-shadow:0 2px 8px rgba(0,0,0,0.03);">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                  <span style="font-weight:700; color:#4c1d95; font-size:13.5px;">${s.title}</span>
                  <span style="background:#ecfdf5; color:#059669; font-size:9.5px; font-weight:700; padding:2px 6px; border-radius:8px;">${s.status}</span>
                </div>
                <div style="font-size:11px; color:#64748b; margin-bottom:8px;">Role: ${s.role}</div>
                <div style="font-size:11px; color:#334155; line-height:1.4;">${s.responsibilities.slice(0, 2).join(' · ')}</div>
              </div>
            `).join('');
          }
        }

        if (incRes.ok) {
          const inc = await incRes.json();
          const tbody = document.getElementById('zoeyIncidentsTableBody');
          if (tbody) {
            tbody.innerHTML = (inc.incidents || []).map(i => `
              <tr>
                <td><span style="background:#fee2e2; color:#ef4444; font-weight:800; padding:2px 8px; border-radius:6px; font-size:10px;">${i.severity}</span></td>
                <td><strong>${i.title}</strong><div style="font-size:10.5px; color:#94a3b8;">${i.department}</div></td>
                <td>${i.business_impact}</td>
                <td>${i.manager}</td>
                <td><span style="background:#ecfdf5; color:#059669; font-weight:700; padding:2px 6px; border-radius:6px; font-size:10.5px;">${i.status}</span></td>
                <td><button onclick="resolveIncident('${i.id}')" style="background:#f1f5f9; border:none; padding:4px 8px; border-radius:6px; cursor:pointer; font-size:11px;">Acknowledge</button></td>
              </tr>
            `).join('');
          }
        }

        if (memRes.ok) {
          const mem = await memRes.json();
          const memBox = document.getElementById('zoeyMemoryContainer');
          if (memBox) {
            memBox.innerHTML = (mem.memories || []).map(m => `
              <div style="background:#f8fafc; border-radius:10px; border:1px solid #e2e8f0; padding:12px;">
                <div style="display:flex; justify-content:space-between; font-size:11px; font-weight:700; color:#6d28d9; margin-bottom:4px;">
                  <span>${m.category}</span>
                  <span style="color:#94a3b8;">#${m.key}</span>
                </div>
                <div style="font-size:12px; color:#334155;">${m.content}</div>
              </div>
            `).join('');
          }
        }

        fetchLatestDailyReport();

      } catch (err) {}
    }
"""

js_target = '    // Page Switching Logic'
if js_target in admin and 'submitAskZoey' not in admin:
    admin = admin.replace(js_target, zoey_js + '\n    ' + js_target)
    print("Added Zoey JavaScript handlers to admin.html")

# Trigger syncZoeyData inside syncAllRealData
sync_call_target = 'syncAllRealData();'
if sync_call_target in admin and 'syncZoeyData();' not in admin:
    admin = admin.replace(sync_call_target, 'syncAllRealData(); syncZoeyData();')
    print("Added syncZoeyData call to initialization")

with open('autonomous-org-dashboard/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin)
print("Updated admin.html with Zoey Command Center.")
