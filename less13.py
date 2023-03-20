from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')
link1 = 'http://suninjuly.github.io/selects2.html'
link2 = 'http://suninjuly.github.io/selects1.html'
try:
    driver.get(link1)

    num1 = driver.find_element(By.ID,'num1')
    num_txt = num1.text
    num2 = driver.find_element(By.ID,'num2')
    num2_txt = num2.text

    sum = (int(num_txt)+(int(num2_txt)))

    select = Select(driver.find_element(By.CLASS_NAME,'custom-select'))
    select.select_by_value(str(sum))

    btn = driver.find_element(By.CLASS_NAME,'btn-default').submit()

    #time.sleep(5)


finally:
    driver.quit()