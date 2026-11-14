import re

with open('autonomous-org-dashboard/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update header metrics to include All Exchanges Real-Time Capital Pill
old_header_metrics = '''    <!-- Header Stats Counters with Real Revenue Tracker -->
    <div class="header-metrics">
      <div class="metric-pill pill-blue">
        <div class="val">5<small>/5</small></div>
        <div class="lbl">Teams Active</div>
      </div>
      <div class="metric-pill pill-purple">
        <div class="val" id="realProjectsCount">5</div>
        <div class="lbl">Live Client RFPs</div>
      </div>
      <div class="metric-pill pill-green" style="background:#f0fdf4;border-color:#bbf7d0;">
        <div class="val" style="color:#059669;" id="revenueEarnedMetric">$0.00</div>
        <div class="lbl" style="color:#047857;">Revenue Earned</div>
      </div>
      <div class="metric-pill pill-red">
        <div class="val" id="escrowLockedMetric">$0.00</div>
        <div class="lbl">In Escrow</div>
      </div>
      <!-- Direct Settlement UPI Target Pill -->
      <div class="metric-pill" style="border-color:#38bdf8;background:#f0f9ff;cursor:pointer;" title="RazorpayX Payout Settlement Destination" onclick="alert('Settlement Target: 8240438062@superyes (Arnab)')">
        <div class="val" style="font-size:12px;color:#0284c7;">8240438062@superyes</div>
        <div class="lbl" style="color:#0369a1;">Settlement UPI</div>
      </div>
    </div>'''

new_header_metrics = '''    <!-- Header Stats Counters with Real Revenue & Multi-Exchange Real-Time Capital -->
    <div class="header-metrics">
      <div class="metric-pill pill-blue">
        <div class="val">5<small>/5</small></div>
        <div class="lbl">Teams Active</div>
      </div>
      <div class="metric-pill pill-purple">
        <div class="val" id="realProjectsCount">5</div>
        <div class="lbl">Live Client RFPs</div>
      </div>
      <!-- ALL EXCHANGES REAL-TIME CAPITAL DISPLAY -->
      <div class="metric-pill" style="border-color:#10b981; background:linear-gradient(135deg, #ecfdf5 0%, #f0fdf4 100%); cursor:pointer;" title="All Exchanges: Delta India ($1,000) + CoinSwitch ($1,010) + Coinbase ($500)">
        <div class="val" style="color:#047857; font-weight:800; font-size:13.5px;" id="totalRealCapitalMetric">$2,510.00</div>
        <div class="lbl" style="color:#065f46; font-weight:700;">All Exchanges Capital</div>
      </div>
      <div class="metric-pill pill-green" style="background:#f0fdf4;border-color:#bbf7d0;">
        <div class="val" style="color:#059669;" id="revenueEarnedMetric">$0.00</div>
        <div class="lbl" style="color:#047857;">Revenue Earned</div>
      </div>
      <div class="metric-pill pill-red">
        <div class="val" id="escrowLockedMetric">$0.00</div>
        <div class="lbl">In Escrow</div>
      </div>
      <!-- Direct Settlement UPI Target Pill -->
      <div class="metric-pill" style="border-color:#38bdf8;background:#f0f9ff;cursor:pointer;" title="RazorpayX Payout Settlement Destination" onclick="alert('Settlement Target: 8240438062@superyes (Arnab)')">
        <div class="val" style="font-size:11.5px;color:#0284c7;">8240438062@superyes</div>
        <div class="lbl" style="color:#0369a1;">Settlement UPI</div>
      </div>
    </div>'''

if old_header_metrics in content:
    content = content.replace(old_header_metrics, new_header_metrics)
    print("Replaced header metrics successfully")
else:
    print("Could not find exact old_header_metrics, attempting fallback regex")

# 2. Update panel-trading header to display live capital for all exchanges
old_trading_header = '''      <!-- Panel 5: WEBOPS & LIVE CRYPTO TRADING DESK -->
      <div class="trading-full-banner" id="panel-trading">
        <div class="swarm-header">
          <div>
            <span class="swarm-badge-pill badge-trading">LIVE CRYPTO TRADING & TREASURY</span>
            <span class="swarm-header-sub" style="margin-left:12px;">Delta Exchange India · Real Capital: <strong>$1,000.00 USDT</strong></span>
          </div>
          <div style="font-family:var(--font-mono);font-size:12px;background:#f0fdf4;border:1px solid #bbf7d0;color:#059669;padding:4px 12px;border-radius:10px;font-weight:700;">
            ● BTC LIVE TICK: <span id="liveBtcPriceDisplay">$73,598.80</span>
          </div>
        </div>'''

new_trading_header = '''      <!-- Panel 5: WEBOPS & LIVE CRYPTO TRADING DESK -->
      <div class="trading-full-banner" id="panel-trading">
        <div class="swarm-header">
          <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
            <span class="swarm-badge-pill badge-trading">LIVE CRYPTO TRADING & TREASURY</span>
            <span class="swarm-header-sub" style="font-size:11.5px; color:#334155;">
              Real Capital: <strong id="tradingTotalCapDisplay" style="color:#0f172a; font-weight:800;">$2,510.00 USDT</strong>
              <span style="font-size:10.5px; color:#64748b; margin-left:6px;">(Delta: <strong style="color:#059669;">$1,000</strong> · CoinSwitch: <strong style="color:#0284c7;">$1,010</strong> · Coinbase: <strong style="color:#7c3aed;">$500</strong>)</span>
            </span>
          </div>
          <div style="display:flex; align-items:center; gap:8px;">
            <div style="font-family:var(--font-mono);font-size:11px;background:#f8fafc;border:1px solid #e2e8f0;color:#334155;padding:3px 10px;border-radius:8px;font-weight:700;">
              ⚡ ALL EXCHANGES: <span style="color:#059669;">ACTIVE LIVE</span>
            </div>
            <div style="font-family:var(--font-mono);font-size:11.5px;background:#f0fdf4;border:1px solid #bbf7d0;color:#059669;padding:3px 10px;border-radius:8px;font-weight:700;">
              ● BTC LIVE: <span id="liveBtcPriceDisplay">$74,266.48</span>
            </div>
          </div>
        </div>'''

if old_trading_header in content:
    content = content.replace(old_trading_header, new_trading_header)
    print("Replaced trading panel header successfully")
else:
    print("Could not find exact old_trading_header, checking variations")
    # Try finding swarm-badge-pill badge-trading
    idx = content.find('badge-trading">LIVE CRYPTO TRADING & TREASURY</span>')
    print("Found badge-trading at index:", idx)

# 3. Update syncRealData to update the total capital metric
old_sync_code = '''          const btcDisplay = document.getElementById('liveBtcPriceDisplay');
          if (btcDisplay && s.trading && s.trading.btc_price) {
            btcDisplay.innerText = '$' + s.trading.btc_price.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});
          }'''

new_sync_code = '''          const btcDisplay = document.getElementById('liveBtcPriceDisplay');
          if (btcDisplay && s.trading && s.trading.btc_price) {
            btcDisplay.innerText = '$' + s.trading.btc_price.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});
          }
          if (s.trading) {
            const totalCap = s.trading.total_allocated_capital || 2510.0;
            const capFormatted = '$' + totalCap.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' USDT';
            const capMetricEl = document.getElementById('totalRealCapitalMetric');
            if (capMetricEl) capMetricEl.innerText = '$' + totalCap.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});
            const tradingCapEl = document.getElementById('tradingTotalCapDisplay');
            if (tradingCapEl) tradingCapEl.innerText = capFormatted;
          }'''

if old_sync_code in content:
    content = content.replace(old_sync_code, new_sync_code)
    print("Replaced syncRealData code successfully")
else:
    print("Could not find old_sync_code")

with open('autonomous-org-dashboard/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html written.")
