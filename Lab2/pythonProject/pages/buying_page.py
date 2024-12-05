from .base_page import BasePage


class BuyingPage(BasePage):

    def add_items_to_cart(self):
        # Add multiple items to cart
        self.page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
        self.page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
        self.page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()

    def proceed_to_checkout(self):
        # Go to cart and then checkout
        self.page.locator("[data-test=\"shopping-cart-link\"]").click()
        self.page.locator("[data-test=\"checkout\"]").click()

    def fill_checkout_info(self, first_name, last_name, postal_code):
        # Fill in the necessary checkout information
        self.page.locator("[data-test=\"firstName\"]").fill(first_name)
        self.page.locator("[data-test=\"lastName\"]").fill(last_name)
        self.page.locator("[data-test=\"postalCode\"]").fill(postal_code)
        self.page.locator("[data-test=\"continue\"]").click()

    def finish_purchase(self):
        # Finish the checkout process
        self.page.locator("[data-test=\"finish\"]").click()

    def validate_order_completion(self):
        # Validate if order is completed by checking if a confirmation message appears
        success_message = self.page.locator("text=THANK YOU FOR YOUR ORDER")
        return success_message.is_visible()

