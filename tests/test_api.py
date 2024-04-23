import pytest

from typing import Generator
from playwright.sync_api import Playwright, APIRequestContext, expect


class TestAPI:

    @pytest.mark.usefixtures('api_request_context1')
    def test_account_login(self) -> None:
        payload = {
            "email": "qaone@yopmail.com",
            "password": "Password123$",
            "nbjwt": "string"
                }
        self.post_request = self.request_context.post(f"/api/Account/Login", data=payload)
        assert self.post_request.ok
        assert self.post_request.status == 200





    @pytest.fixture(scope="function")
    def api_request_context1(self, playwright: Playwright ) -> Generator[APIRequestContext, None, None]:
        self.request_context = playwright.request.new_context(
            base_url="https://qa-build-api.actionbutton.co"
        )
        yield self.request_context
        self.request_context.dispose()