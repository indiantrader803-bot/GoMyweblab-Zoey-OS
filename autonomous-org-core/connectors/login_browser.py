import asyncio
import os
from playwright.async_api import async_playwright

USER_DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "browser_session")
os.makedirs(USER_DATA_DIR, exist_ok=True)

async def launch_persistent_login():
    """
    Opens an independent Chrome window with a dedicated user profile.
    When you log into Upwork or Freelancer once in this window, your session
    and login cookies remain permanently saved on your disk for the autonomous agents.
    """
    async with async_playwright() as p:
        print("Launching Dedicated Agent Browser...")
        print(f"Session Storage Path: {USER_DATA_DIR}")
        
        # Launch persistent context
        context = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            channel="chrome", # Uses your installed Google Chrome
            viewport={"width": 1280, "height": 800},
            args=["--disable-blink-features=AutomationControlled"]
        )

        page = context.pages[0] if context.pages else await context.new_page()
        
        print("Opening Freelancer and Upwork tabs for one-time manual sign-in...")
        await page.goto("https://www.freelancer.com/login")
        
        upwork_page = await context.new_page()
        await upwork_page.goto("https://www.upwork.com/ab/account-security/login")

        print("\n" + "="*70)
        print("BROWSER IS READY!")
        print("1. Log into your Freelancer.com account in Tab 1.")
        print("2. Log into your Upwork account in Tab 2.")
        print("3. When you are logged in, simply close the browser window.")
        print("Your agents will then be able to access both accounts directly!")
        print("="*70 + "\n")

        # Keep browser open until user closes it
        while len(context.pages) > 0:
            await asyncio.sleep(2)

        print("Session saved successfully! Agents now have account access.")

if __name__ == '__main__':
    asyncio.run(launch_persistent_login())
