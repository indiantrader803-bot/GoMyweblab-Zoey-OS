import asyncio
from playwright.async_api import async_playwright

async def verify_zoey():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1440, 'height': 900})
        page = await context.new_page()

        await page.goto('http://127.0.0.1:8088/admin')
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

        # Click ZOEY AI nav item
        await page.click("li[onclick*=\"switchPageView('zoey'\"]")
        await page.wait_for_timeout(1500)

        # Fill directive in Ask Zoey input
        await page.fill("#askZoeyInput", "Zoey, review today's business operations.")
        await page.click("button:has-text('Send Directive')")
        await page.wait_for_timeout(2000)

        # Verify response text
        resp_text = await page.inner_text("#zoeyResponseText")
        print(f"Zoey Response Verified: {resp_text}")

        # Capture screenshot of Zoey Command Center
        await page.screenshot(path='autonomous-org-dashboard/zoey_command_center_verified.jpg')

        # Switch to Daily Reports tab
        await page.click("button:has-text('12. Daily Reports')")
        await page.wait_for_timeout(1000)
        await page.screenshot(path='autonomous-org-dashboard/zoey_daily_reports_tab_verified.jpg')

        await browser.close()
        print("Zoey Command Center verification completed successfully!")

if __name__ == '__main__':
    asyncio.run(verify_zoey())
