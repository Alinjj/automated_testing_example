from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_conftest(driver):
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR,'#login_link')