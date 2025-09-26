from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get("https://bonigarcia.dev/selenium-webdriver\
-java/loading-images.html")

third_image = WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "spinner")))
third_image = driver.find_elements(By.TAG_NAME, "img")[3]
src_value = third_image.get_attribute("src")

print(src_value)
