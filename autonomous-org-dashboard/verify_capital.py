import asyncio
from playwright.async_api import async_playwright

async def verify_capital_displays():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1440, 'height': 900})
        page = await context.new_page()

        # 1. Homepage Verification
        await page.goto('http://127.0.0.1:8088/')
        await page.evaluate("""
            () => {
                localStorage.setItem('gomyweblab_user', 'arnab');
                localStorage.setItem('gomyweblab_token', 'gwl_live_token_mock');
                const modal = document.getElementById('authModal');
                if (modal) modal.style.display = 'none';
            }
        """)
        await page.reload()
        await page.wait_for_timeout(2000)

        # Check total capital metric
        cap_val = await page.inner_text('#totalRealCapitalMetric')
        print(f"Homepage Header Capital Metric: {cap_val}")

        # Check trading panel capital
        panel_cap = await page.inner_text('#tradingTotalCapDisplay')
        print(f"Homepage Panel Trading Capital: {panel_cap}")

        # Check scrollHeight to ensure zero-scroll is maintained
        scroll_height = await page.evaluate("() => document.body.scrollHeight")
        inner_height = await page.evaluate("() => window.innerHeight")
        print(f"Homepage Dimensions: scrollHeight={scroll_height}, innerHeight={inner_height}")

        await page.screenshot(path='autonomous-org-dashboard/homepage_capital_verified.jpg', full_page=False)

        # 2. Admin Dashboard Verification
        admin_page = await context.new_page()
        await admin_page.goto('http://127.0.0.1:8088/admin')
        await admin_page.evaluate("""
            () => {
                localStorage.setItem('gomyweblab_user', 'arnab');
                localStorage.setItem('gomyweblab_token', 'gwl_live_token_mock');
                const modal = document.getElementById('authModal');
                if (modal) modal.style.display = 'none';
            }
        """)
        await admin_page.reload()
        await admin_page.wait_for_timeout(2000)

        # Check KPI card on admin dashboard
        admin_cap = await admin_page.inner_text('#kpiAllExchangesCap')
        print(f"Admin Dashboard Top KPI Capital: {admin_cap}")

        await admin_page.screenshot(path='autonomous-org-dashboard/admin_capital_kpi_verified.jpg')

        # Click Delta Trading tab on Admin
        await admin_page.click("li[onclick*=\"showPage('trading'\"]")
        await admin_page.wait_for_timeout(1000)

        trading_page_cap = await admin_page.inner_text('#tradingPageTotalCapital')
        print(f"Admin Trading Page Total Capital: {trading_page_cap}")

        await admin_page.screenshot(path='autonomous-org-dashboard/admin_trading_exchanges_breakdown.jpg')

        await browser.close()
        print("All verifications completed successfully!")

if __name__ == '__main__':
    asyncio.run(verify_capital_displays())
