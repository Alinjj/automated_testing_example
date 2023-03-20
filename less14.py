from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')

try:
    #driver.execute_script("alert('Robots at work');")

    #driver.execute_script("document.title='Script executing';")
    driver.execute_script("alert('Robots at work');document.title='Script executing';")
    #time.sleep(3)
finally:
    driver.quit()