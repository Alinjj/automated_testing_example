import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    print("\nstart browser for test...")
    driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')
    yield driver
    print("\nbrowser quit...")
    driver.quit()

class TestMainPage1():
    def test_login_link(self,driver):
        driver.get("http://selenium1py.pythonanywhere.com/")
        driver.find_element(By.CSS_SELECTOR,"#login_link")
        

