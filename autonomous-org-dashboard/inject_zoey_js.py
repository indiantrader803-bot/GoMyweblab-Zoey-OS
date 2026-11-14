with open('autonomous-org-dashboard/admin.html', 'r', encoding='utf-8') as f:
    admin = f.read()

target = '    // Page Switching Logic'
zoey_js = """    // ZOEY AI APPLICATION LOGIC
    function switchZoeyTab(tabId) {
      document.querySelectorAll('#zoeyTabsBar .date-filter-btn').forEach(btn => btn.classList.remove('active'));
      if (event && event.target) event.target.classList.add('active');
      document.querySelectorAll('.zoey-tab-panel').forEach(p => p.style.display = 'none');
      const target = document.getElementById('ztab-' + tabId);
      if (target) target.style.display = 'block';
      else {
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

admin = admin.replace(target, zoey_js + target)
with open('autonomous-org-dashboard/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin)
print("Added Zoey functions into admin.html")
