from playwright.sync_api import sync_playwright


# Launch Playwright browser and interact with a website
def run_playwright():
    with sync_playwright() as p:
        # Launch a browser (Chromium by default)
        browser = p.chromium.launch(headless=False)  # Set headless=False to see the browser
        page = browser.new_page()

        # Navigate to a website (e.g., Google)
        page.goto('https://google.com')

        # Print the title of the webpage
        print(f"Title of the page: {page.title()}")

        # Perform more actions if needed, e.g., click, fill forms
        # page.click('text=More information')

        # Close the browser
        browser.close()

if __name__ == "__main__":
    run_playwright()

# ***************************
