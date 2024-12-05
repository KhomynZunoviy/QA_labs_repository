import re
from playwright.sync_api import Playwright, sync_playwright, expect


def longtest(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
    page.locator("[data-test=\"add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("john")
    page.locator("[data-test=\"firstName\"]").press("ArrowDown")
    page.locator("[data-test=\"lastName\"]").click()
    page.locator("[data-test=\"lastName\"]").press("ArrowDown")
    page.locator("[data-test=\"lastName\"]").fill("hoe")
    page.locator("[data-test=\"postalCode\"]").click()
    page.locator("[data-test=\"postalCode\"]").fill("1488")
    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"finish\"]").click()
    page.locator("[data-test=\"back-to-products\"]").click()

    # ---------------------
    context.close()
    browser.close()

def shorttest(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"remove-sauce-labs-backpack\"]").click()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    longtest(playwright)
    shorttest(playwright)
