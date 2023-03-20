import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name',action='store',default=None,help='Choose browser: Chrome or FireFox')


@pytest.fixture(scope="function")
def driver(request):
    driver_name = request.config.getoption("browser_name")
    driver = None
    if driver_name == "Chrome":
        print("\nStart browser for test with Chrome...")
        driver = webdriver.Chrome(executable_path=r"C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe")
    elif driver_name == "FireFox":
        print("\nStart browser for test with firefox...")
        driver = webdriver.Firefox(executable_path=r"C:\Users\Mogilat Igor\automated_testing_example\geckodriver.exe")

    else:
        raise pytest.UsageError("--browser_name should be Chrome or FireFox")
    yield driver
    print("\nquit browser")
    driver.quit()