from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')
def calc(x):
    return(str(math.log(abs(12*math.sin(int(x))))))
try:
    driver.get('https://suninjuly.github.io/math.html')
    text_el = driver.find_element(By.ID,'input_value')
    x = text_el.text

    driver.find_element(By.ID,'answer').send_keys(calc(x))

    driver.find_element(By.CSS_SELECTOR,"label[for='robotCheckbox']").click()

    driver.find_element(By.CSS_SELECTOR,"label[for='robotsRule']").click()

    driver.find_element(By.CLASS_NAME,"btn-default").click()
    #time.sleep(5)

finally:
    driver.quit()