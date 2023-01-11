import pytest
from playwright.sync_api import Page

@pytest.mark.usefixtures('go_to_base_url')
class BaseTest:
    
    def cleanup(self):
        print('cleanup')