from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')

def calc(x):
    return (str(math.log(abs(12*math.sin(int(x))))))

try:
    driver.get('http://suninjuly.github.io/get_attribute.html')
    treasure = driver.find_element(By.ID,'treasure')
    treasure_x = treasure.get_attribute('valuex')

    driver.find_element(By.ID,'answer').send_keys(calc(treasure_x))

    driver.find_element(By.ID,'robotCheckbox').click()

    driver.find_element(By.ID,'robotsRule').click()

    driver.find_element(By.CLASS_NAME,'btn-default').submit()

    #time.sleep(1)


finally:
    driver.quit()