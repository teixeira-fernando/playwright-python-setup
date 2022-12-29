"""
This module contains the page object for SauceLabs Login Page
"""

from playwright.sync_api import Page

class LoginPage:

    PATH = ''

    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_field = page.locator('#user-name')
        self.password_field = page.locator('#password')
        self.login_button = page.locator('#login-button')

    def load(self) -> None:
        self.page.goto(self.page.url + self.PATH)

    def login(self, username: str, password: str) -> None:
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
