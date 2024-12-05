from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def login(self, username, password):
        #self.page.fill('input[name="standard_user"]', username)
        #self.page.fill('input[name="secret_sauce"]', password)

        self.page.locator("[data-test=\"username\"]").click()
        self.page.locator("[data-test=\"username\"]").fill("standard_user")
        self.page.locator("[data-test=\"password\"]").click()
        self.page.locator("[data-test=\"password\"]").fill("secret_sauce")
        self.page.locator("[data-test=\"login-button\"]").click()
        #self.page.click('button[type="login-button"]')
