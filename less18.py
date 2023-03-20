from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')

def calc(x):
    return (math.log(abs(12*math.sin(int(x)))))

try:
    driver.get('http://suninjuly.github.io/alert_accept.html')
    driver.find_element(By.CLASS_NAME,'btn-primary').submit()
    #alert = driver.switch_to.alert
    #alert.accept()
    x = driver.find_element(By.ID,'input_value')
    x_txt = x.text

    driver.find_element(By.ID,'answer').send_keys(calc(x_txt))
    driver.find_element(By.CLASS_NAME,'btn-primary').submit()

    #time.sleep(3)

finally:
    driver.quit()