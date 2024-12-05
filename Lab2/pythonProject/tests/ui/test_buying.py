# tests/ui/test_buying.py

import pytest
from pages.buying_page import BuyingPage

@pytest.mark.dependency(depends=["test_login"])  # Test runs only after login
def test_buying(page):
    buying_page = BuyingPage(page)

    # Add items to cart
    buying_page.add_items_to_cart()

    # Proceed to checkout
    buying_page.proceed_to_checkout()

    # Fill in checkout info
    buying_page.fill_checkout_info(first_name="John", last_name="Doe", postal_code="12345")

    # Complete the purchase
    buying_page.finish_purchase()

    # Validate order completion
    assert buying_page.validate_order_completion()
