from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return (math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')

try:
    driver.get('http://suninjuly.github.io/execute_script.html')
    x = driver.find_element(By.ID,'input_value')

    driver.find_element(By.ID,'answer').send_keys(calc(x.text))

    btn = driver.find_element(By.CLASS_NAME,'btn-primary')
    driver.execute_script("return arguments[0].scrollIntoView(true);",btn)

    driver.find_element(By.ID,'robotCheckbox').click()

    driver.find_element(By.ID,'robotsRule').click()

    btn.submit()
    #time.sleep(3)
finally:
    driver.quit()