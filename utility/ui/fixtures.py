import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page

from utility.ui.pages.login_page import LoginPage
from utility.ui.constants import LoginConstants




@pytest.fixture(scope='function')
def login_to_saucedemo(page: Page) -> None:
    LoginPage(page).navigate(LoginConstants.URL)
    LoginPage(page).login(LoginConstants.USER_NAME, LoginConstants.PASSWORD)

@pytest.fixture(scope='function')
def launch_app(page: Page) -> None:
    LoginPage(page).navigate(LoginConstants.URL)




"""
def launch_browser() -> Page:
    with sync_playwright() as p:
        browser = p.chromium.launch(headed = True)
        context = browser.new_context()
        page = context.new_page()
        return page
"""