from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')
try:
    driver.get('http://suninjuly.github.io/huge_form.html')
    elements = driver.find_elements(By.CSS_SELECTOR,'input')
    for element in elements:
        element.send_keys('text')
    driver.find_element(By.CLASS_NAME,'btn-default').click()
finally:
    #time.sleep(10)
    driver.quit()