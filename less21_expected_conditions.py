from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')

try:
    driver.get('http://suninjuly.github.io/wait2.html')
    btn = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,'verify')))
    btn.submit()
    mess = driver.find_element(By.ID,'verify_message')
    assert 'successful' in mess.text

finally:
    driver.quit()