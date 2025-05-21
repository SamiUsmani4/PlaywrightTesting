import asyncio
from playwright.async_api import async_playwright

# Asynchronous function to run Playwright
async def run_playwright():
    async with async_playwright() as p:
        # Launch a browser (Chromium by default)
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Navigate to a website
        await page.goto('https://google.com')

        # Print the title of the page
        print(f"Title of the page: {await page.title()}")

        # Close the browser
        await browser.close()

# Run the asynchronous Playwright function
asyncio.run(run_playwright())

# ***************************
