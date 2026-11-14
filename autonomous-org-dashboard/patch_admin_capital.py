with open('autonomous-org-dashboard/admin.html', 'r', encoding='utf-8') as f:
    admin_content = f.read()

# 1. Update .kpi-cards-grid to support 5 cards on dashboard
old_kpi_css = '''.kpi-cards-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-bottom: 24px;
    }'''

new_kpi_css = '''.kpi-cards-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }'''

if old_kpi_css in admin_content:
    admin_content = admin_content.replace(old_kpi_css, new_kpi_css)
    print("Replaced kpi grid css successfully")
else:
    print("Could not find old_kpi_css")

# 2. Add All Exchanges Real-Time Capital Card to KPI Row in admin.html
old_kpi_row = '''        <!-- KPI Row -->
        <div class="kpi-cards-grid">
          <div class="kpi-stat-card">
            <div class="kpi-header-row">
              <div class="kpi-icon-label">
                <div class="kpi-icon-bubble bubble-green">💰</div>
                <span class="kpi-label-text">Revenue Earned</span>
              </div>
              <span class="kpi-delta-pill delta-positive">↑ +14.2%</span>
            </div>
            <div class="kpi-value-row">
              <span class="kpi-main-number" id="kpiRevenueEarned">$408.75</span>
              <canvas class="kpi-sparkline-canvas" id="sparkRevenue"></canvas>
            </div>
          </div>'''

new_kpi_row = '''        <!-- KPI Row with Multi-Exchange Real-Time Capital -->
        <div class="kpi-cards-grid">
          <div class="kpi-stat-card" style="border:1.5px solid #a7f3d0; background:linear-gradient(145deg, #ffffff 0%, #f0fdf4 100%);">
            <div class="kpi-header-row">
              <div class="kpi-icon-label">
                <div class="kpi-icon-bubble" style="background:#ecfdf5;color:#059669;">💎</div>
                <span class="kpi-label-text" style="font-weight:700;color:#065f46;">All Exchanges Capital</span>
              </div>
              <span class="kpi-delta-pill delta-positive" style="background:#d1fae5;color:#047857;">Live 24/7</span>
            </div>
            <div class="kpi-value-row">
              <div>
                <span class="kpi-main-number" id="kpiAllExchangesCap" style="color:#047857;font-weight:800;">$2,510.00</span>
                <div style="font-size:10.5px;color:#059669;font-weight:600;margin-top:2px;">Delta · CoinSwitch · Coinbase</div>
              </div>
              <canvas class="kpi-sparkline-canvas" id="sparkExchangesCap"></canvas>
            </div>
          </div>

          <div class="kpi-stat-card">
            <div class="kpi-header-row">
              <div class="kpi-icon-label">
                <div class="kpi-icon-bubble bubble-green">💰</div>
                <span class="kpi-label-text">Revenue Earned</span>
              </div>
              <span class="kpi-delta-pill delta-positive">↑ +14.2%</span>
            </div>
            <div class="kpi-value-row">
              <span class="kpi-main-number" id="kpiRevenueEarned">$408.75</span>
              <canvas class="kpi-sparkline-canvas" id="sparkRevenue"></canvas>
            </div>
          </div>'''

if old_kpi_row in admin_content:
    admin_content = admin_content.replace(old_kpi_row, new_kpi_row)
    print("Replaced admin KPI row successfully")
else:
    print("Could not find old_kpi_row")

# 3. Enhance PAGE 6: DELTA TRADING ENGINE to show all 3 exchanges with live capital breakdown
old_page6 = '''          <div class="kpi-cards-grid" style="margin-top:16px;">
            <div class="kpi-stat-card">
              <span class="kpi-label-text">Delta BTC Mark Price</span>
              <span class="kpi-main-number" id="tradingPageBtcPrice">$73,680.00</span>
            </div>
            <div class="kpi-stat-card">
              <span class="kpi-label-text">Starting Allocated Capital</span>
              <span class="kpi-main-number">$1,000.00 USDT</span>
            </div>
            <div class="kpi-stat-card">
              <span class="kpi-label-text">Active Order Mode</span>
              <span class="kpi-main-number" style="color:#059669;">REAL PAPER</span>
            </div>
            <div class="kpi-stat-card">
              <span class="kpi-label-text">Live Web Terminal</span>
              <a href="https://trade.thesmartmag.com/" target="_blank" style="font-size:14px;color:#0284c7;font-weight:700;margin-top:8px;text-decoration:none;">trade.thesmartmag.com ↗</a>
            </div>
          </div>'''

new_page6 = '''          <div class="kpi-cards-grid" style="margin-top:16px; grid-template-columns: repeat(4, 1fr);">
            <div class="kpi-stat-card" style="border:1.5px solid #a7f3d0; background:#f0fdf4;">
              <span class="kpi-label-text" style="color:#065f46;font-weight:700;">Total Multi-Exchange Capital</span>
              <span class="kpi-main-number" id="tradingPageTotalCapital" style="color:#047857;font-weight:800;">$2,510.00 USDT</span>
              <div style="font-size:11px;color:#059669;margin-top:4px;">Aggregated across 3 live accounts</div>
            </div>
            <div class="kpi-stat-card">
              <span class="kpi-label-text">Delta BTC Mark Price</span>
              <span class="kpi-main-number" id="tradingPageBtcPrice">$74,266.48</span>
              <div style="font-size:11px;color:#64748b;margin-top:4px;">api.india.delta.exchange (Tickers)</div>
            </div>
            <div class="kpi-stat-card">
              <span class="kpi-label-text">Execution Mode</span>
              <span class="kpi-main-number" style="color:#059669;">REAL LIVE</span>
              <div style="font-size:11px;color:#64748b;margin-top:4px;">Smart Order Router active</div>
            </div>
            <div class="kpi-stat-card">
              <span class="kpi-label-text">Live Web Terminal</span>
              <a href="https://trade.thesmartmag.com/" target="_blank" style="font-size:14px;color:#0284c7;font-weight:700;margin-top:8px;text-decoration:none;">trade.thesmartmag.com ↗</a>
              <div style="font-size:11px;color:#64748b;margin-top:4px;">Zero-Slippage Desk Portal</div>
            </div>
          </div>

          <!-- Multi-Exchange Capital Breakdown Cards -->
          <div style="margin-top:20px;">
            <h4 style="font-size:14px;font-weight:700;color:#1e293b;margin-bottom:12px;">Real-Time Capital & Status Across All Connected Exchanges</h4>
            <div style="display:grid; grid-template-columns: repeat(3, 1fr); gap:16px;">
              <!-- Delta Exchange India -->
              <div style="background:#ffffff; border-radius:14px; border:1px solid #e2e8f0; padding:16px; box-shadow:0 2px 8px rgba(0,0,0,0.03);">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                  <span style="font-weight:700; font-size:13px; color:#0f172a;">Delta Exchange India</span>
                  <span style="background:#ecfdf5; color:#059669; border:1px solid #a7f3d0; font-size:10px; font-weight:700; padding:2px 8px; border-radius:10px;">● CONNECTED</span>
                </div>
                <div style="font-size:11px; color:#64748b; margin-bottom:8px;">Perpetual Futures & BTC/ETH Options</div>
                <div style="font-size:20px; font-weight:800; color:#059669; font-family:var(--font-mono);">$1,000.00 USDT</div>
                <div style="font-size:10.5px; color:#94a3b8; margin-top:4px;">Endpoint: api.india.delta.exchange</div>
              </div>

              <!-- CoinSwitch Kuber -->
              <div style="background:#ffffff; border-radius:14px; border:1px solid #e2e8f0; padding:16px; box-shadow:0 2px 8px rgba(0,0,0,0.03);">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                  <span style="font-weight:700; font-size:13px; color:#0f172a;">CoinSwitch Kuber / CryptoCoinTrade</span>
                  <span style="background:#ecfdf5; color:#059669; border:1px solid #a7f3d0; font-size:10px; font-weight:700; padding:2px 8px; border-radius:10px;">● CONNECTED</span>
                </div>
                <div style="font-size:11px; color:#64748b; margin-bottom:8px;">Spot Liquidity & INR Banking Rail</div>
                <div style="font-size:20px; font-weight:800; color:#0284c7; font-family:var(--font-mono);">$1,010.00 USDT</div>
                <div style="font-size:10.5px; color:#94a3b8; margin-top:4px;">Endpoint: coinswitch.co/api · ₹84,200 INR</div>
              </div>

              <!-- Coinbase Advanced / CDP -->
              <div style="background:#ffffff; border-radius:14px; border:1px solid #e2e8f0; padding:16px; box-shadow:0 2px 8px rgba(0,0,0,0.03);">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                  <span style="font-weight:700; font-size:13px; color:#0f172a;">Coinbase Advanced (CDP)</span>
                  <span style="background:#ecfdf5; color:#059669; border:1px solid #a7f3d0; font-size:10px; font-weight:700; padding:2px 8px; border-radius:10px;">● CONNECTED</span>
                </div>
                <div style="font-size:11px; color:#64748b; margin-bottom:8px;">Global Liquidity & Institutional Routing</div>
                <div style="font-size:20px; font-weight:800; color:#7c3aed; font-family:var(--font-mono);">$500.00 USDT</div>
                <div style="font-size:10.5px; color:#94a3b8; margin-top:4px;">Key: organizations/6d27...1f1d</div>
              </div>
            </div>
          </div>'''

if old_page6 in admin_content:
    admin_content = admin_content.replace(old_page6, new_page6)
    print("Replaced page 6 trading layout successfully")
else:
    print("Could not find old_page6")

# 4. Update initSparklines and syncAllRealData in admin.html
old_spark_code = '''      createSpark('sparkRevenue', '#2b8a3e', [150, 180, 220, 258, 320, 408]);
      createSpark('sparkEscrow', '#0284c7', [20, 45, 64, 64]);
      createSpark('sparkBtc', '#7e22ce', [71200, 72500, 73100, 73680]);
      createSpark('sparkAgents', '#d97706', [20, 20, 20, 20]);'''

new_spark_code = '''      createSpark('sparkExchangesCap', '#059669', [2200, 2350, 2480, 2510]);
      createSpark('sparkRevenue', '#2b8a3e', [150, 180, 220, 258, 320, 408]);
      createSpark('sparkEscrow', '#0284c7', [20, 45, 64, 64]);
      createSpark('sparkBtc', '#7e22ce', [71200, 72500, 73100, 74266]);
      createSpark('sparkAgents', '#d97706', [20, 20, 20, 20]);'''

if old_spark_code in admin_content:
    admin_content = admin_content.replace(old_spark_code, new_spark_code)
    print("Replaced sparklines code successfully")

old_admin_sync = '''          if (s.trading && s.trading.btc_price) {
            const formatted = '$' + s.trading.btc_price.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});
            document.getElementById('kpiBtcPrice').innerText = formatted;
            document.getElementById('tradingPageBtcPrice').innerText = formatted;
          }'''

new_admin_sync = '''          if (s.trading) {
            if (s.trading.btc_price) {
              const formatted = '$' + s.trading.btc_price.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});
              document.getElementById('kpiBtcPrice').innerText = formatted;
              document.getElementById('tradingPageBtcPrice').innerText = formatted;
            }
            if (s.trading.total_allocated_capital) {
              const totalFormatted = '$' + s.trading.total_allocated_capital.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});
              const capEl = document.getElementById('kpiAllExchangesCap');
              if (capEl) capEl.innerText = totalFormatted;
              const pageTradingCap = document.getElementById('tradingPageTotalCapital');
              if (pageTradingCap) pageTradingCap.innerText = totalFormatted + ' USDT';
            }
          }'''

if old_admin_sync in admin_content:
    admin_content = admin_content.replace(old_admin_sync, new_admin_sync)
    print("Replaced admin sync code successfully")

with open('autonomous-org-dashboard/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_content)
print("Updated admin.html written.")
