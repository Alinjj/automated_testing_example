import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    print("\nstart browser for test...")
    driver = webdriver.Chrome(executable_path=r"C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe")
    yield driver
    print("\nbrowser close")
    driver.quit()
