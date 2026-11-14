import asyncio
import os
import json
import sqlite3
from playwright.async_api import async_playwright

USER_DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "browser_session")
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "freelance_pipeline.db")

async def verify_sessions():
    """Verifies that the saved session can access Freelancer and Upwork."""
    results = {"freelancer": False, "upwork": False, "details": []}

    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=True,
            channel="chrome",
            args=["--disable-blink-features=AutomationControlled"]
        )

        page = context.pages[0] if context.pages else await context.new_page()

        # Check Freelancer session
        try:
            print("Checking Freelancer.com authentication state...")
            await page.goto("https://www.freelancer.com/dashboard", timeout=25000, wait_until="domcontentloaded")
            await asyncio.sleep(2)
            url = page.url
            title = await page.title()
            is_logged_in = "login" not in url.lower()
            results["freelancer"] = is_logged_in
            results["details"].append(f"Freelancer: URL={url}, Title={title}, LoggedIn={is_logged_in}")
        except Exception as e:
            results["details"].append(f"Freelancer error: {str(e)}")

        # Check Upwork session
        try:
            print("Checking Upwork.com authentication state...")
            await page.goto("https://www.upwork.com/nx/find-work/", timeout=25000, wait_until="domcontentloaded")
            await asyncio.sleep(2)
            u_url = page.url
            u_title = await page.title()
            u_logged = "login" not in u_url.lower()
            results["upwork"] = u_logged
            results["details"].append(f"Upwork: URL={u_url}, Title={u_title}, LoggedIn={u_logged}")
        except Exception as e:
            results["details"].append(f"Upwork error: {str(e)}")

        await context.close()

    return results

if __name__ == '__main__':
    res = asyncio.run(verify_sessions())
    print("\nVerification Results:", json.dumps(res, indent=2))
