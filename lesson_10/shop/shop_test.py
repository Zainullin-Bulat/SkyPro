import pytest
import allure
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


@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест оформления заказа в интернет-магазине")
@allure.description("Проверка полного цикла покупки "
                    "товаров в интернет-магазине")
def test_shop(driver, login, products, cart, checkout):
    with allure.step("Авторизация пользователя"):
        login.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        products.add_items_to_cart()

    with allure.step("Переход в корзину"):
        products.go_to_cart()

    with allure.step("Начало оформления заказа"):
        cart.checkout()

    with allure.step("Заполнение информации для доставки"):
        checkout.fill_info("Ivan", "Ivanov", "123456")

    with allure.step("Проверка итоговой суммы"):
        actual_total = checkout.get_total()
        with allure.step(f"Проверка что итоговая \
                    сумма равна $58.29, актуальная: {actual_total}"):
            assert actual_total == "$58.29"
