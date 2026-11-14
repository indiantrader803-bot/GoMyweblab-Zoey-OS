with open('autonomous-org-dashboard/admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

# 1. Add Revenue & Financial Ledger to the sidebar navigation under Core Operations
old_nav_deals = '''          <li class="nav-item" onclick="switchPageView('deals', this)">
            <div class="nav-left-content">
              <svg viewBox="0 0 24 24"><path d="M20 12V8H6a2 2 0 0 1-2-2c0-1.1.9-2 2-2h12v4"/><path d="M4 6v12c0 1.1.9 2 2 2h14v-4"/><circle cx="18" cy="12" r="2"/></svg>
              <span>Deals & RFPs</span>
            </div>
            <span class="nav-badge-pill" id="sidebarDealsBadge">5</span>
          </li>'''

new_nav_deals = '''          <li class="nav-item" onclick="switchPageView('revenue', this)">
            <div class="nav-left-content">
              <svg viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="2"/><line x1="12" y1="8" x2="12" y2="16"/><line x1="8" y1="12" x2="16" y2="12"/></svg>
              <span>Revenue & Ledger</span>
            </div>
            <span class="nav-badge-pill" style="background:#059669;color:#fff;">$408.75</span>
          </li>
          <li class="nav-item" onclick="switchPageView('deals', this)">
            <div class="nav-left-content">
              <svg viewBox="0 0 24 24"><path d="M20 12V8H6a2 2 0 0 1-2-2c0-1.1.9-2 2-2h12v4"/><path d="M4 6v12c0 1.1.9 2 2 2h14v-4"/><circle cx="18" cy="12" r="2"/></svg>
              <span>Deals & RFPs</span>
            </div>
            <span class="nav-badge-pill" id="sidebarDealsBadge">5</span>
          </li>'''

if old_nav_deals in admin_html:
    admin_html = admin_html.replace(old_nav_deals, new_nav_deals)
    print("Added Revenue & Ledger to sidebar navigation")

# 2. Add PAGE: REVENUE & FINANCIAL LEDGER Section
revenue_section = '''      <!-- ======================================================== -->
      <!-- PAGE: REVENUE & FINANCIAL LEDGER (REAL EARNINGS)         -->
      <!-- ======================================================== -->
      <section class="page-view-container" id="view-revenue">
        <!-- Top Revenue Stats -->
        <div class="kpi-cards-grid">
          <div class="kpi-stat-card" style="border:1.5px solid #a7f3d0; background:linear-gradient(145deg, #ffffff 0%, #f0fdf4 100%);">
            <div class="kpi-header-row">
              <div class="kpi-icon-label">
                <div class="kpi-icon-bubble bubble-green">💰</div>
                <span class="kpi-label-text" style="font-weight:700;color:#065f46;">Total Real Earned</span>
              </div>
              <span class="kpi-delta-pill delta-positive">Released & Paid</span>
            </div>
            <div class="kpi-value-row">
              <span class="kpi-main-number" id="ledgerTotalEarned" style="color:#047857;font-weight:800;">$408.75</span>
              <div style="font-size:11px;color:#059669;font-weight:600;">100% Verified in DB</div>
            </div>
          </div>

          <div class="kpi-stat-card">
            <div class="kpi-header-row">
              <div class="kpi-icon-label">
                <div class="kpi-icon-bubble bubble-blue">🔒</div>
                <span class="kpi-label-text">Funds In Escrow</span>
              </div>
              <span class="kpi-delta-pill delta-positive">Pending Milestone</span>
            </div>
            <div class="kpi-value-row">
              <span class="kpi-main-number" id="ledgerInEscrow" style="color:#0284c7;font-weight:800;">$64.40</span>
              <div style="font-size:11px;color:#64748b;">Escrow Locked</div>
            </div>
          </div>

          <div class="kpi-stat-card">
            <div class="kpi-header-row">
              <div class="kpi-icon-label">
                <div class="kpi-icon-bubble bubble-purple">🏦</div>
                <span class="kpi-label-text">Settlement Destination</span>
              </div>
              <span class="kpi-delta-pill delta-positive">RazorpayX Live</span>
            </div>
            <div class="kpi-value-row">
              <span class="kpi-main-number" style="font-size:17px;color:#7c3aed;">8240438062@superyes</span>
              <div style="font-size:11px;color:#64748b;">Director: Arnab</div>
            </div>
          </div>

          <div class="kpi-stat-card">
            <div class="kpi-header-row">
              <div class="kpi-icon-label">
                <div class="kpi-icon-bubble bubble-amber">📊</div>
                <span class="kpi-label-text">Total Cumulative Value</span>
              </div>
              <span class="kpi-delta-pill delta-positive">Earned + Escrow</span>
            </div>
            <div class="kpi-value-row">
              <span class="kpi-main-number" id="ledgerCumulativeValue" style="color:#1e293b;">$473.15</span>
              <div style="font-size:11px;color:#64748b;">4 Active Transactions</div>
            </div>
          </div>
        </div>

        <!-- Real Financial Ledger Table Card -->
        <div class="standard-panel-card">
          <div class="panel-header-row">
            <div>
              <h3 class="panel-title-text">Official Enterprise Financial Ledger (Live Database)</h3>
              <p class="panel-subtitle-text">Every recorded client invoice, milestone release, and escrow deposit tracked in gomyweblab_state.db</p>
            </div>
            <span class="online-indicator-pill"><span class="indicator-pulse-dot"></span> LIVE SETTLEMENT ENGINE</span>
          </div>

          <table class="pipeline-data-table" style="margin-top:14px;">
            <thead>
              <tr>
                <th>Tx Reference</th>
                <th>Project & Milestone</th>
                <th>Client & Platform</th>
                <th>Amount (USD)</th>
                <th>Status</th>
                <th>Timestamp</th>
              </tr>
            </thead>
            <tbody id="realFinancialLedgerTableBody">
              <!-- Dynamically populated from /api/financial-ledger -->
            </tbody>
          </table>
        </div>
      </section>

'''

deals_page_marker = '''      <!-- ======================================================== -->
      <!-- PAGE 4: DEALS & RFPS PAGE                                -->
      <!-- ======================================================== -->'''

if deals_page_marker in admin_html and 'id="view-revenue"' not in admin_html:
    admin_html = admin_html.replace(deals_page_marker, revenue_section + deals_page_marker)
    print("Inserted PAGE: REVENUE & FINANCIAL LEDGER into admin.html")

# 3. Add 'revenue' to page title mappings
old_titles = '''      const titles = {
        dashboard: { title: 'Dashboard', sub: 'Real-time autonomous enterprise telemetry & active revenue streams' },'''

new_titles = '''      const titles = {
        dashboard: { title: 'Dashboard', sub: 'Real-time autonomous enterprise telemetry & active revenue streams' },
        revenue: { title: 'Revenue & Financial Ledger', sub: 'Live earnings, verified payouts, and autonomous milestone escrow settlements' },'''

if old_titles in admin_html:
    admin_html = admin_html.replace(old_titles, new_titles)
    print("Added revenue title mapping")

# 4. Add renderFinancialLedger and update syncAllRealData in admin.html
old_render_deals = '''    // Populate Real Deals in Tables
    function renderDeals(deals) {'''

new_render_functions = '''    // Populate Real Financial Ledger in Table
    function renderFinancialLedger(items) {
      const tbody = document.getElementById('realFinancialLedgerTableBody');
      if (!tbody) return;
      
      tbody.innerHTML = items.map(tx => {
        const isEarned = tx.status === 'RELEASED_EARNED';
        const badgeStyle = isEarned 
          ? 'background:#ecfdf5;color:#059669;border:1px solid #a7f3d0;' 
          : 'background:#eff6ff;color:#2563eb;border:1px solid #bfdbfe;';
        const statusLabel = isEarned ? '● RELEASED & EARNED' : '🔒 ESCROW LOCKED';
        
        return `
          <tr>
            <td>
              <strong style="font-family:var(--font-mono);color:#059669;">${tx.ref}</strong>
              <div style="font-size:10px;color:#94a3b8;">${tx.deal_ref || 'FL-DIRECT'}</div>
            </td>
            <td>
              <div class="deal-title-cell" style="font-weight:700;">${tx.title}</div>
            </td>
            <td>
              <div style="font-weight:600;color:#334155;">${tx.client}</div>
              <div style="font-size:10.5px;color:#94a3b8;">${tx.platform}</div>
            </td>
            <td>
              <span style="font-family:var(--font-mono);font-size:14px;font-weight:800;color:${isEarned ? '#059669' : '#0284c7'};">
                $${tx.amount.toFixed(2)}
              </span>
            </td>
            <td>
              <span style="font-family:var(--font-mono);font-size:10px;font-weight:700;padding:3px 8px;border-radius:12px;${badgeStyle}">
                ${statusLabel}
              </span>
            </td>
            <td style="font-family:var(--font-mono);font-size:11px;color:#64748b;">
              ${tx.released_at ? tx.released_at : tx.date}
            </td>
          </tr>
        `;
      }).join('');
    }

    // Populate Real Deals in Tables
    function renderDeals(deals) {'''

if old_render_deals in admin_html:
    admin_html = admin_html.replace(old_render_deals, new_render_functions)
    print("Added renderFinancialLedger function")

# 5. Fetch /api/financial-ledger in syncAllRealData
old_sync_promises = '''        const [statusRes, pipeRes, agentsRes] = await Promise.all([
          fetch('/api/status'),
          fetch('/api/freelance-pipeline'),
          fetch('/api/agents-roster')
        ]);'''

new_sync_promises = '''        const [statusRes, pipeRes, agentsRes, ledgerRes] = await Promise.all([
          fetch('/api/status'),
          fetch('/api/freelance-pipeline'),
          fetch('/api/agents-roster'),
          fetch('/api/financial-ledger')
        ]);'''

if old_sync_promises in admin_html:
    admin_html = admin_html.replace(old_sync_promises, new_sync_promises)
    print("Added ledgerRes promise")

old_sync_post = '''        if (agentsRes.ok) {
          const ag = await agentsRes.json();
          renderAgentCards(ag.agents || []);
          document.getElementById('kpiActiveAgents').innerText = (ag.agents || []).length + ' / 20';
        }'''

new_sync_post = '''        if (agentsRes.ok) {
          const ag = await agentsRes.json();
          renderAgentCards(ag.agents || []);
          document.getElementById('kpiActiveAgents').innerText = (ag.agents || []).length + ' / 20';
        }

        if (ledgerRes && ledgerRes.ok) {
          const led = await ledgerRes.json();
          renderFinancialLedger(led.ledger || []);
          const earnEl = document.getElementById('ledgerTotalEarned');
          if (earnEl) earnEl.innerText = '$' + led.total_earned_usd.toFixed(2);
          const escEl = document.getElementById('ledgerInEscrow');
          if (escEl) escEl.innerText = '$' + led.in_escrow_usd.toFixed(2);
          const cumEl = document.getElementById('ledgerCumulativeValue');
          if (cumEl) cumEl.innerText = '$' + (led.total_earned_usd + led.in_escrow_usd).toFixed(2);
        }'''

if old_sync_post in admin_html:
    admin_html = admin_html.replace(old_sync_post, new_sync_post)
    print("Added ledger sync processing logic")

with open('autonomous-org-dashboard/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)
print("Updated admin.html written.")
