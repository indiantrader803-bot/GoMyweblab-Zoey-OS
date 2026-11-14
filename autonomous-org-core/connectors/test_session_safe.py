import asyncio
import os
import json
import shutil
from playwright.async_api import async_playwright

USER_DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "browser_session")
TEMP_SESSION_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "temp_agent_session")

async def test_session_copy():
    # Make a temporary copy to avoid file locks if a window is still open
    if os.path.exists(TEMP_SESSION_DIR):
        try:
            shutil.rmtree(TEMP_SESSION_DIR)
        except Exception:
            pass

    try:
        shutil.copytree(USER_DATA_DIR, TEMP_SESSION_DIR, ignore=shutil.ignore_patterns("Singleton*", "*.lock"))
    except Exception as e:
        print("Copy notice:", e)

    results = {"freelancer": False, "upwork": False, "details": []}

    async with async_playwright() as p:
        try:
            context = await p.chromium.launch_persistent_context(
                user_data_dir=TEMP_SESSION_DIR if os.path.exists(TEMP_SESSION_DIR) else USER_DATA_DIR,
                headless=True,
                channel="chrome",
                args=["--disable-blink-features=AutomationControlled"]
            )

            page = context.pages[0] if context.pages else await context.new_page()

            # Freelancer check
            await page.goto("https://www.freelancer.com/dashboard", timeout=20000, wait_until="domcontentloaded")
            await asyncio.sleep(2)
            f_url = page.url
            f_title = await page.title()
            results["freelancer"] = "login" not in f_url.lower()
            results["details"].append(f"Freelancer: URL={f_url}, Title={f_title}")

            # Upwork check
            await page.goto("https://www.upwork.com/nx/find-work/", timeout=20000, wait_until="domcontentloaded")
            await asyncio.sleep(2)
            u_url = page.url
            u_title = await page.title()
            results["upwork"] = "login" not in u_url.lower()
            results["details"].append(f"Upwork: URL={u_url}, Title={u_title}")

            await context.close()
        except Exception as e:
            results["details"].append(f"Execution notice: {str(e)}")

    if os.path.exists(TEMP_SESSION_DIR):
        try:
            shutil.rmtree(TEMP_SESSION_DIR)
        except Exception:
            pass

    return results

if __name__ == '__main__':
    res = asyncio.run(test_session_copy())
    print("\nVerified Account Access:", json.dumps(res, indent=2))
