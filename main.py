import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')


driver.get("https://suninjuly.github.io/text_input_task.html")
textarea = driver.find_element(By.CSS_SELECTOR,".textarea")
textarea.send_keys("get()")
submit_button = driver.find_element(By.ID,"submit_button")
submit_button.submit()
time.sleep(5)
driver.quit()

