from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_options(driver):
    option = Options()
    option.add_experimental_option("prefs", {'intl.accept_languages': 'en'})
    driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe', options=option)