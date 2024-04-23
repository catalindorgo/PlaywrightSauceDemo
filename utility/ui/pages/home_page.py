from playwright.sync_api import Page
from utility.ui.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
    """
        self.title = page.locator("xpath=locaatooor")

    def get_page_title(self) -> str:
        ""
        Get current page title
        ""
        return self.title.text_content()
    
    THE METHOD ABOVE IS Getting the title for this page, and it's implemennted here, but commented out because I'm tryig to use the same 
    method, but implemennted in BasePage (and it will be imported straight innto the Test)
    """