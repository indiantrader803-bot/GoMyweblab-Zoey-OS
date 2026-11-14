import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        
        # 1. Login to admin
        await page.goto("http://127.0.0.1:8088/admin")
        await page.fill("#authUsername", "arnab")
        await page.fill("#authPassword", "arnab123")
        await page.click("#authSubmitBtn")
        await page.wait_for_timeout(1000)
        
        # 2. Click Insights tab
        await page.click("text=Insights")
        await page.wait_for_timeout(1000)
        await page.screenshot(path="c:/Users/karth/.gemini/antigravity/brain/47f2e8e0-eb84-436b-a9dc-58380aa002f7/frames_v5/admin_insights_clicked.jpg")
        print("Captured Insights page in Admin Orbit!")
        
        # 3. Click Tokenization tab
        await page.click("text=Tokenization")
        await page.wait_for_timeout(1000)
        await page.screenshot(path="c:/Users/karth/.gemini/antigravity/brain/47f2e8e0-eb84-436b-a9dc-58380aa002f7/frames_v5/admin_tokenization_clicked.jpg")
        print("Captured Tokenization page in Admin Orbit!")
        
        await browser.close()

asyncio.run(run())
