"""Module with login tests"""
import re
from playwright.sync_api import Page, expect
import pytest
from pages.login import LoginPage
from tests.base_test import BaseTest

class TestLogin(BaseTest):
    def testUserCanLoginSuccessfully(self, page: Page, login_page: LoginPage):
        expect(page).to_have_title(re.compile('Swag Labs'))
        expect(page.locator('.login_logo')).to_be_visible()

        login_page.login('standard_user', 'secret_sauce')

        expect(page.locator('.inventory_container')).to_be_visible() 
        
    def testLoginErrorWhenInvalidCredentials(self, page: Page, login_page: LoginPage):
        expect(page).to_have_title(re.compile('Swag Labs'))
        expect(page.locator('.login_logo')).to_be_visible()

        login_page.login('invalid_user', 'invalid_password')

        expect(page.locator('[data-test="error"]')).to_be_visible()