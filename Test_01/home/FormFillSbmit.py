# pip install playwright
# python -m playwright install
# https://playwright.dev/python/docs/intro
import asyncio
from playwright.async_api import async_playwright


# Asynchronous function to perform search
async def perform_search():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto('https://auth.motivefinancial.com/login')
        print(f"Title of the page: {await page.title()}")

        await page.fill('input[id="panNum"]', "12345678")
        await page.fill('input[id="password"]', "test")
        # await page.get_by_label('Remember Me').check()
        await page.pause()
        await page.get_by_role("button", name="Login").click()

        # Close the browser
        await browser.close()

# Run the asynchronous search function
asyncio.run(perform_search())

# ***************************
