import uuid
from playwright.sync_api import Page, sync_playwright, Browser
from utility.logger import configure_logging
log = configure_logging(__name__)


class BasePage:

    DEFAULT_TIMEOUT = 30000
    MEDIUM_TIMEOUT = 60000
    LONG_TIMEOUT = 90000

    def __init__(self, page: Page):
        self.page = page
        self.user_menu = self.page.locator("xpath=.//button[@id='react-burger-menu-btn']")    #with xpath
        self.logout_button = self.page.get_by_text("Logout")
        self._page_title = self.page.locator("xpath=.//span[@class='title']")

    def wait_for_page(self) -> None:
        self.page.wait_for_load_state()

    def logout(self) -> None:
        self.user_menu.click()
        self.logout_button.click()

    def _attach_screenshot(self) -> None:               #not sure this method what it does but copied it to investigate it.
        log.info('Screenshot',
        attachment={
            "name": f"Test screenshot{uuid.uuid4()}",
            "data": self.page.screenshot(),
            "mime": "image/png"
                   }
        )

    def get_page_title(self) -> str:
        """ Get current page title"""
        return self._page_title.text_content()


    """
    def launch_browser(headless_value = False) -> Browser:
        with sync_playwright() as p:
            browser = p.firefox.launch(headless=headless_value)
            return browser
    """