from selenium import webdriver
from selenium.webdriver.common.by import By


"""Поиск кнопки по локатору ID"""

driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')

driver.get("http://suninjuly.github.io/simple_form_find_task.html")
button = driver.find_element(By.ID, "submit_button")
driver.quit()

