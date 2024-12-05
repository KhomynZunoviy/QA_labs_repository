import pytest
from pages.login_page import LoginPage
@pytest.mark.dependency(name="test_login")
def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.navigate('https://www.saucedemo.com/')
    login_page.login('standard_user', 'secret_sauce')
    assert page.url == 'https://www.saucedemo.com/inventory.html'
