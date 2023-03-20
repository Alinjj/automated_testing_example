import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import time
import math

@pytest.mark.parametrize("task",['236895','236896','236897','236898','236899','236903','236904','236905'])
class TestParametrize():

    def test_auth(self,driver,task):
        link = f"https://stepik.org/lesson/{task}/step/1"
        driver.get(link)
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,'ember33'))).click()
        email = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'id_login_email')))
        email.send_keys('')
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'id_login_password')))
        password.send_keys("")
        btn_enter_form = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, 'sign-form__btn')))
        btn_enter_form.click()
        text_area = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CLASS_NAME,'ember-text-area')))
        text_area.clear()
        text_area.send_keys(str(math.log(int(time.time()+0.071))))
        btn = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CLASS_NAME,'submit-submission')))
        time.sleep(5)
        btn.click()
        smart_tab = WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.CLASS_NAME,'smart-hints__hint'))).text

        assert smart_tab == 'Correct!'




#The owls are not what they seem! OvO