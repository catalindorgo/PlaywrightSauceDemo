import pytest
from playwright.sync_api import Page


from utility.ui.pages.login_page import LoginPage
from utility.ui.base_page import BasePage
from utility.ui.constants import ProductsConstants
from utility.common import generate_string
from utility.logger import configure_logging

log = configure_logging(__name__)

@pytest.mark.hooome_custom_suite_name

class TestHomeUI:

    @pytest.mark.usefixtures('login_to_saucedemo', 'setup_base')
    def test_home_title(self) -> None:
        """
        Checks if the home page title is SauceDemo
        """
        log.info(f'Check if the page title is \'{ProductsConstants.PAGE_TITLE}\'')    #not really using it, is to log in console or in reports tstuff i think
        assert self.base.get_page_title() == ProductsConstants.PAGE_TITLE

    @pytest.mark.usefixtures('launch_app', 'setup_base')
    def test_register_user(self) -> None:
        """
        Writing this method to use a random string generator.
        """
        self.random_user = f'test_{generate_string(5)}'
        self.random_password = f'P@SS1_{generate_string(4)}'
        self.login_page.login(self.random_user, self.random_password)


    @pytest.fixture(scope='function')
    def setup_base(self, page : Page) -> None:
        self.base = BasePage(page)
        self.login_page = LoginPage(page)


