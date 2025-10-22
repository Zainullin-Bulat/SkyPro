from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://bonigarcia.dev/"
                        "selenium-webdriver-java/slow-calculator.html")
        return self

    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(str(delay))
        return self

    def click_button(self, text):
        self.driver.find_element(By.XPATH, f"//span[text()='{text}']").click()
        return self

    def wait_for_result(self, expected, timeout=46):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"),
                                             expected)
        )
        return self

    def get_result(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
