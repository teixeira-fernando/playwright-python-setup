"""Module with first playwright test example."""
import re
from playwright.sync_api import Page, expect
import pytest
from pages.login import LoginPage


@pytest.mark.usefixtures('go_to_base_url')
class TestLogin:
    def testUserCanLoginSuccessfully(self, page: Page, login_page: LoginPage):
        page.goto(page.url)
        # Expect a title "to contain" a substring.
        expect(page).to_have_title(re.compile('Swag Labs'))

        expect(page.locator('.login_logo')).to_be_visible()

        login_page.login('standard_user', 'secret_sauce')

        expect(page.locator('.inventory_container')).to_be_visible()
