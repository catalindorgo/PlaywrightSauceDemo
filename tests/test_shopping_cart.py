import pytest
from playwright.sync_api import Page
from utility.ui.pages.products_page import ProductsPage
from utility.ui.pages.shopping_cart_page import ShoppingCartPage



class TestShoppingCartUI:

    @pytest.mark.usefixtures('login_to_saucedemo', 'setup', 'add_backpack_to_cart')
    def test_product_added_to_cart(self, page: Page) -> None:
        assert self.shopping_cart_page.get_item_text() == 'Sauce Labs Backpack'

#this is the better method to use (vs the one above), cause it can find any product in the list
    @pytest.mark.usefixtures('login_to_saucedemo', 'setup', 'add_backpack_to_cart')
    def test_product_added_to_cart_v2(self, page: Page) -> None:
        assert self.shopping_cart_page.product_is_visible_in_list("Sauce Labs Backpack")


    @pytest.fixture(scope='function')
    def setup(self, page: Page) -> None:
        self.product_page = ProductsPage(page)
        self.shopping_cart_page = ShoppingCartPage(page)

    @pytest.fixture(scope='function')
    def add_backpack_to_cart(self) -> None:
        self.product_page.add_backpack_to_cart()
        self.product_page.navigate_to_shopping_cart()
        yield         #the yield will be executed after the Test is finished, like a clean up (here is done, after the assert in the test method)
        #self.shopping_cart_page.remove_backpack()   - this method was removing a particular item, so used the more generic one remove_product instead
        self.shopping_cart_page.remove_product("Sauce Labs Backpack")
        self.shopping_cart_page.continue_shopping()
