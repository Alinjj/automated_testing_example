from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')

try:
    driver.get('http://suninjuly.github.io/find_link_text')
    message = str(math.ceil(math.pow(math.pi, math.e)*10000))
    driver.find_element(By.LINK_TEXT,message).click()

    driver.find_element(By.CSS_SELECTOR, '.form-group:nth-child(1) input').send_keys('Name')
    driver.find_element(By.CSS_SELECTOR, '.form-group:nth-child(2) input').send_keys('surname')
    driver.find_element(By.CSS_SELECTOR, '.form-group:nth-child(3) input').send_keys('Seattle')
    driver.find_element(By.CSS_SELECTOR, '.form-group:nth-child(4) input').send_keys('USA')

    btn = driver.find_element(By.CLASS_NAME, 'btn').submit()
    #time.sleep(10)
finally:
    driver.quit()