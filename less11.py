from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')

try:
    driver.get('http://suninjuly.github.io/math.html')
    people_rule = driver.find_element(By.ID,"peopleRule")
    people_checked = people_rule.get_attribute("checked")
    print(f"value of people_rule :",people_checked)
    assert people_checked == 'true'

    robots_rule = driver.find_element(By.ID,'robotsRule')
    robots_checked = robots_rule.get_attribute('checked')
    print("value of robots_rule: ",robots_checked)
    assert robots_checked is None

    time.sleep(10)
    submit_btn = driver.find_element(By.CLASS_NAME,'btn-default')

    submit_btn_dis = submit_btn.get_attribute("disabled")
    print("value of submit_btn : ", submit_btn_dis)
    assert submit_btn_dis == 'true'

finally:
    driver.quit()