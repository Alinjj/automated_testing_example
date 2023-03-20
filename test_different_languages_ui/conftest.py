from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

def pytest_addoption(parser):
    parser.addoption('--language',action='store',default=None,help='Choose language: es,ru,fr')

@pytest.fixture(scope='function')
def driver(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    driver = webdriver.Chrome(options=options)
    print("\nlanguage:%s" % language)
    yield driver
    print("\nquit browser..")
    driver.quit()

