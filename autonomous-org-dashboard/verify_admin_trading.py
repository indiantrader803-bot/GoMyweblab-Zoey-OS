import asyncio
from playwright.async_api import async_playwright

async def verify_capital_displays():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1440, 'height': 900})

        # Admin Dashboard Verification
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
        await admin_page.click("li[onclick*=\"switchPageView('trading'\"]")
        await admin_page.wait_for_timeout(1000)

        trading_page_cap = await admin_page.inner_text('#tradingPageTotalCapital')
        print(f"Admin Trading Page Total Capital: {trading_page_cap}")

        await admin_page.screenshot(path='autonomous-org-dashboard/admin_trading_exchanges_breakdown.jpg')

        await browser.close()
        print("Admin Trading verification finished cleanly!")

if __name__ == '__main__':
    asyncio.run(verify_capital_displays())
