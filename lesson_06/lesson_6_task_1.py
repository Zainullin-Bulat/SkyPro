from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.ID, "ajaxButton").click()

text = WebDriverWait(driver, 16).until(
    EC.presence_of_element_located((By.CLASS_NAME, "bg-success"))
).text

print(text)
driver.quit()
