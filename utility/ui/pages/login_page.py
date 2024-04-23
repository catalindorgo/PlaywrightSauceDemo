from playwright.sync_api import Page, sync_playwright
from utility.ui.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.user_input = page.locator("xpath=.//input[@id='user-name']")
        self.user_password = page.locator("xpath=.//input[@id='password']")
        self.login_button = page.get_by_text("Login")
        self.page_title = page.locator("aaa23")



    def navigate(self, url: str) -> None:
        """
        Navigate to the specified URL
        Args:
            url(str): URL of the page to navigate to
        """
        self.page.goto(url)



    def login(self, username: str, password: str) -> None:
        """
        Login to SauceDemo

        Args:
            username (str): username
            password (str): password
        """
        self.wait_for_page()       #not necesarly, I added it just to see the BasePage is imported. Can be deleted.
        self.user_input.fill(username)
        self.user_password.fill(password)
        self.login_button.click()

    def get_page_title(self) -> str:
        """
        Get current page title
        """
        return self.page_title.text_content()

    """
        async def navigate_to_url(self, url: str) -> Page:
            page = await self.launch_browser().new_page()
            await page.goto(url)
            return page
    """
    """
        def navigate1(url: str, browser_type: str = "chromium", headless_bool = False) -> None:
            with sync_playwright() as p:

                if browser_type == "chromium":
                    browser = p.chromium.launch(headless = headless_bool)
                elif browser_type == "firefox":
                    browser = p.firefox.launch(headless = headless_bool)
                else:
                    raise ValueError(f"Unsupported browser type: {browser_type}")

                page = browser.new_page()
                page.goto(url)

        """

    """
    def navigate3(self, url: str, headless_value = False) -> None:
        with sync_playwright() as p:
            self.browser = p.chromium.launch(headless=headless_value)
            self.page = self.browser.new_page()
            self.page.goto(url)
    """
