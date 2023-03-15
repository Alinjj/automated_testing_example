from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')

try:
    driver.get('http://suninjuly.github.io/wait1.html')
    btn = driver.find_element(By.ID,'verify').submit()
    successful = driver.find_element(By.ID,'verify_message').text
    assert 'successful' in successful

finally:
    driver.quit()