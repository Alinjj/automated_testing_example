import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


def test_first_page():
    driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')

    driver.get('http://suninjuly.github.io/registration1.html')
            # *requirements
    driver.find_element(By.XPATH,'//input[@placeholder="Input your first name"]').send_keys('first_name')
    driver.find_element(By.XPATH,'//input[@placeholder="Input your last name"]').send_keys('surname')
    driver.find_element(By.XPATH,'//input[@placeholder="Input your email"]').send_keys('email')
    driver.find_element(By.CLASS_NAME,'btn-default').submit()
    text_h1 = driver.find_element(By.TAG_NAME,'h1')
    text = text_h1.text

    assert 'Congratulations! You have successfully registered!' in text
    driver.quit()

def test_second_page(self):

    driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')

    driver.get('http://suninjuly.github.io/registration2.html')
    # *requirements
    driver.find_element(By.XPATH, '//input[@placeholder="Input your first name"]').send_keys('first_name')
    driver.find_element(By.XPATH, '//input[@placeholder="Input your last name"]').send_keys('surname')
    driver.find_element(By.XPATH, '//input[@placeholder="Input your email"]').send_keys('email')
    driver.find_element(By.CLASS_NAME, 'btn-default').submit()
    text_h1 = driver.find_element(By.TAG_NAME, 'h1')
    text = text_h1.text

    assert 'Congratulations! You have successfully registered!' in text
    driver.quit()


