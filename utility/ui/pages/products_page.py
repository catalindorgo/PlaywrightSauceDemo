from playwright.sync_api import Page, sync_playwright
from utility.ui.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.add_to_cart_backpack_button = page.locator("xpath=.//button[@name='add-to-cart-sauce-labs-backpack']")
        self.shopping_cart = page.locator("xpath=.//a[@class='shopping_cart_link']")

    def add_backpack_to_cart(self) -> None:
        self.add_to_cart_backpack_button.click()

    def navigate_to_shopping_cart(self) -> None:
        self.shopping_cart.click()