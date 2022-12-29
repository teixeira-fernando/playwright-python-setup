"""
This module contains shared fixtures and test config.
"""
import os
import pytest
from playwright.sync_api import Page
from pages.login import LoginPage

def get_env_var(varname: str) -> str:
    value = os.getenv(varname)
    assert value, f'{varname} is not set'
    return value

def get_base_url():
    return get_env_var('BASE_URL')

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture(scope='function')
def go_to_base_url(page: Page):
    page.goto(get_base_url())