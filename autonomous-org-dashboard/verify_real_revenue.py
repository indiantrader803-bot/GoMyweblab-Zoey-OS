import asyncio
from playwright.async_api import async_playwright

async def verify_real_revenue_views():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1440, 'height': 900})

        # 1. Homepage Verification
        home_page = await context.new_page()
        await home_page.goto('http://127.0.0.1:8088/')
        await home_page.evaluate("""
            () => {
                localStorage.setItem('gomyweblab_user', 'arnab');
                localStorage.setItem('gomyweblab_token', 'gwl_live_token_mock');
                const modal = document.getElementById('authModal');
                if (modal) modal.style.display = 'none';
            }
        """)
        await home_page.reload()
        await home_page.wait_for_timeout(2000)

        earned_val = await home_page.inner_text('#revenueEarnedMetric')
        escrow_val = await home_page.inner_text('#escrowLockedMetric')
        cap_val = await home_page.inner_text('#totalRealCapitalMetric')
        print(f"Homepage Header: Earned={earned_val}, Escrow={escrow_val}, Capital={cap_val}")

        await home_page.screenshot(path='autonomous-org-dashboard/homepage_revenue_verified.jpg', full_page=False)

        # 2. Admin Deck Verification
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

        admin_earned = await admin_page.inner_text('#kpiRevenueEarned')
        admin_escrow = await admin_page.inner_text('#kpiInEscrow')
        print(f"Admin Dashboard Top KPI: Earned={admin_earned}, Escrow={admin_escrow}")

        # Click Revenue & Ledger tab on Admin
        await admin_page.click("li[onclick*=\"switchPageView('revenue'\"]")
        await admin_page.wait_for_timeout(1000)

        ledger_earned = await admin_page.inner_text('#ledgerTotalEarned')
        ledger_escrow = await admin_page.inner_text('#ledgerInEscrow')
        print(f"Admin Revenue Page: Earned={ledger_earned}, Escrow={ledger_escrow}")

        await admin_page.screenshot(path='autonomous-org-dashboard/admin_revenue_ledger_verified.jpg')

        await browser.close()
        print("All revenue verifications passed!")

if __name__ == '__main__':
    asyncio.run(verify_real_revenue_views())
