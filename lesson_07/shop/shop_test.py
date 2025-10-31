import pytest
from selenium import webdriver
from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    return LoginPage(driver)


@pytest.fixture
def products(driver):
    return ProductsPage(driver)


@pytest.fixture
def cart(driver):
    return CartPage(driver)


@pytest.fixture
def checkout(driver):
    return CheckoutPage(driver)


def test_shop(driver, login, products, cart, checkout):
    login.login("standard_user", "secret_sauce")

    products.add_items_to_cart()

    products.go_to_cart()

    cart.checkout()
    checkout.fill_info("Ivan", "Ivanov", "123456")

    actual_total = checkout.get_total()
    assert actual_total == "$58.29"
