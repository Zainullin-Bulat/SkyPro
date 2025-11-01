from selenium.webdriver.common.by import By
from base_page import BasePage


class ProductsPage(BasePage):
    def add_items_to_cart(self):
        self.driver.find_element(By.ID,
                                 "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID,
                                 "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.ID,
                                 "add-to-cart-sauce-labs-onesie").click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
