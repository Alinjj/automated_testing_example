from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')

try:
    driver.get('http://suninjuly.github.io/find_xpath_form')
    elements = driver.find_elements(By.CSS_SELECTOR,'input')
    for element in elements:
        element.send_keys('text')
    submit_button = driver.find_element(By.XPATH,'//button[text()="Submit"]').submit()
finally:
    #time.sleep(10)
    driver.quit()
