from playwright.sync_api import Page, sync_playwright, expect
from utility.ui.base_page import BasePage

class ShoppingCartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.remove_backpack_button = page.locator("xpath=.//button[@id='remove-sauce-labs-backpack']")
        self.continue_shopping_button = page.get_by_text("Continue Shopping")
        self.backpack_item_added = page.locator("xpath=.//div[@class='inventory_item_name']")
        self.table_body = page.locator("xxxx")
        self.table_head = page.locator("xxxx")


    def remove_backpack(self) -> None:
        self.remove_backpack_button.click()

    def remove_product(self, product_name: str) -> None:
        """
        Removes the product from the shopping cart, based on the provided product_name parameter
        """
        cart_item_remove_btn = self.page.locator(f"xpath=.//div[@class='inventory_item_name' and text()='{product_name}']"
                                                 f"/../..// button[text()='Remove']")
        cart_item_remove_btn.click()


    def get_item_text(self) -> str:
        return self.backpack_item_added.text_content()

    def continue_shopping(self) -> None:
        self.continue_shopping_button.click()

    #------------method for checking value in table (Cata + chatGPT)-----------------
    def product_is_visible_in_list(self, product_name: str) -> bool:
        """
        Checks if product is visible by altering the locator
        The xpath of a product will contain the Product Name inside of it, so it checks that webelement exists & visible
        """
        cart_itme = self.page.locator(f"xpath=.//div[@class='inventory_item_name' and text()='{product_name}']")
        if cart_itme:
            return cart_itme.is_visible()
        return False



    #   -------------------- methods for checking in a table a value is present --------------------
    #this method returns the text from a locator, based on the index.
    #then in the test_ you can compare it vs an expected txt
    def product_exists_in_cart(self, product_name: str) -> bool:
        """Check if a product is in the lister"""
        name_index = self.__get_column_name_index('Product')
        try:
            self.table_body.locator(f'//tr/td[{name_index + 1}]').all_inner_texts().index(product_name)
            return True
        except ValueError:
            return False

    #this method is private __ and it returns the index of the columnn you wannt to use
    #the triky part is to construct the xpath/locator to work here
    def __get_column_name_index(self, column_name: str) -> str:
        """Get the index for a table column"""
        columns = self.table_head.locator("th").all_inner_texts()
        index = 0
        for column in columns:
            if column == column_name:
                return index
            else:
                index += 1
        return -1