from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/"

def test_succesful(driver):
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR,'#login_link')


def test_fail(driver):
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR, "#magic_link")