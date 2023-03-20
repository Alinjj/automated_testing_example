from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')

try:
    driver.get("https://SunInJuly.github.io/execute_script.html")
    btn = driver.find_element(By.TAG_NAME,'button')

    driver.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()
    time.sleep(3)
finally:
    driver.quit()