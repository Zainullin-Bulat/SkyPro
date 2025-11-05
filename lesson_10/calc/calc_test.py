import pytest
import allure
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


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Тест работы калькулятора с задержкой")
@allure.description("Проверка вычисления 7 + 8 с задержкой 45 секунд")
def test_calc(calculator):
    with allure.step("Установка задержки вычислений"):
        calculator.set_delay(45)

    with allure.step("Выполнение операции 7 + 8"):
        calculator.click_button("7")
        calculator.click_button("+")
        calculator.click_button("8")
        calculator.click_button("=")

    with allure.step("Ожидание результата"):
        calculator.wait_for_result("15")

    with allure.step("Проверка результата вычислений"):
        result = calculator.get_result()
        with allure.step(
                f"Проверка что результат равен 15, актуальный: {result}"):
            assert result == "15"
