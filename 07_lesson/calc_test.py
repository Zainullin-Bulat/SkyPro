import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    yield driver
    driver.quit()


@pytest.fixture
def calculator(driver):
    calc = CalculatorPage(driver)
    calc.open()
    return calc


def test_02_calc(calculator):
    calculator.set_delay(45)
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")
    calculator.wait_for_result("15")

    assert calculator.get_result() == "15"
