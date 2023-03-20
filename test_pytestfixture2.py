import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def driver():
    print("\nbrowser start for test...")
    driver = webdriver.Chrome(executable_path="C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe")
    yield driver
    print("\nbrower quit...")
    driver.quit()

class TestMainPage():

    def test_login_link(self,driver):
        print("start test1")
        driver.get("http://selenium1py.pythonanywhere.com/")
        driver.find_element(By.CSS_SELECTOR,'#login_link')
        print("finish test1")