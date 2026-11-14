import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        
        # 1. Login with Arnab on Homepage
        await page.goto("http://127.0.0.1:8088/")
        await page.evaluate("""() => {
            localStorage.setItem('gomyweblab_user', 'arnab');
            localStorage.setItem('gomyweblab_token', 'gwl_session_token_123');
        }""")
        await page.reload()
        await page.wait_for_timeout(1000)
        
        # 2. Capture expanded state
        await page.screenshot(path="c:/Users/karth/.gemini/antigravity/brain/47f2e8e0-eb84-436b-a9dc-58380aa002f7/frames_v5/log_expanded_success.jpg")
        print("Captured expanded screenshot!")
        
        # 3. Click Collapse button
        await page.click("#logToggleBtn")
        await page.wait_for_timeout(500)
        await page.screenshot(path="c:/Users/karth/.gemini/antigravity/brain/47f2e8e0-eb84-436b-a9dc-58380aa002f7/frames_v5/log_collapsed_success.jpg")
        print("Captured collapsed screenshot!")
        
        await browser.close()

asyncio.run(run())
