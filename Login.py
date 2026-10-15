from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            headless=False
        )
    page = browser.new_page()
    page.goto("https://iswmpune.in/")
    page.wait_for_timeout(5000)
    page.locator("#txtUser").fill("scstech@gmail.com")
    page.locator("#txtPassward").fill("iswm_admin@2026")
    page.wait_for_timeout(10000)
    page.locator("#btnLogin").click()
    page.wait_for_timeout(10000)
    