from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return (math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')


try:
    driver.get('http://suninjuly.github.io/redirect_accept.html')
    driver.find_element(By.CLASS_NAME,'trollface').submit()

    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    x = driver.find_element(By.ID,'input_value').text
    driver.find_element(By.ID,'answer').send_keys(calc(x))

    driver.find_element(By.CLASS_NAME,'btn-primary').submit()

    #time.sleep(5)

finally:
    driver.quit()