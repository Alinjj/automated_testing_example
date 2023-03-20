from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')

def calc(x):
    return (math.log(abs(12*math.sin(int(x)))))

try:
    driver.get('http://suninjuly.github.io/explicit_wait2.html')
    book_btn = WebDriverWait(driver,13).until(EC.text_to_be_present_in_element((By.ID,'price'),'100'))
    btn = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,'book')))
    btn.click()


    x = driver.find_element(By.ID,'input_value')

    driver.find_element(By.ID,'answer').send_keys(calc(x.text))
    driver.find_element(By.ID,'solve').click()
    #time.sleep(5)

finally:
    driver.quit()