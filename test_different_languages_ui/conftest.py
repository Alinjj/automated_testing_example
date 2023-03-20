from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption('--language',action='store',default=None,help='Choose language: es or ru')

@pytest.fixture(scope='function')
def driver(request):
    language = request.config.getoption("language")
    driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\test_different_languages_ui\chromedriver.exe')
    if language == "ru":
        print('\nstart browser with ru language...')
        driver.get('http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/')
    elif language == "es":
        print('\nstart browser with es language...')
        driver.get('http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/')
    yield driver
    print('\nbrowser quit')
    driver.quit()

