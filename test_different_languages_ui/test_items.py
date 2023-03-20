from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_btn(driver):
    driver.get(link)
    btn = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CLASS_NAME,'btn-primary')))
    assert len(btn) > 0,'button not found'