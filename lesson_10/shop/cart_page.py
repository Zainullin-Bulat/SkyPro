from selenium.webdriver.common.by import By
from base_page import BasePage


class CartPage(BasePage):
    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
