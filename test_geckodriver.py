from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager



browser = webdriver.Firefox(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\geckodriver.exe')
browser.get('https://stepik.org/lesson/25969/step/8')
