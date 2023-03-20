from selenium import webdriver
from selenium.webdriver.common.by import By


"""Используем конструкцию try/finally для закрытия браузера в любом случае,дабы не тратить оперативную память , если код прервется"""
try:
    driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')
    driver.get("http://suninjuly.github.io/simple_form_find_task.html")
    button = driver.find_element(By.ID, "submit_button")
    button.submit()

finally:
    driver.quit()