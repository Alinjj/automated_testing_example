from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_btn(driver):
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CLASS_NAME,'btn-primary')))
