from selenium.webdriver.common.by import By
from base_page import BasePage


class CheckoutPage(BasePage):
    def fill_info(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self):
        total = self.driver.find_element(By.CLASS_NAME,
                                         "summary_total_label").text
        return total.replace("Total: ", "")
