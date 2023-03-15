from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\automated_testing_example\chromedriver.exe')

try:
    driver.get('http://suninjuly.github.io/file_input.html')
    driver.find_element(By.NAME,'firstname').send_keys('firstname')
    driver.find_element(By.NAME,'lastname').send_keys('surname')
    driver.find_element(By.NAME,'email').send_keys('email')

    with open('test.txt', 'w') as file:
        file.write('test')   # Создаем/открываем для записи файла и пишем туда "test"

    path = os.getcwd() + '/' + 'test.txt'   # Используем для нахождения пути файла, который создали выше, используя модуль os

    driver.find_element(By.ID,'file').send_keys(path)

    driver.find_element(By.CLASS_NAME,'btn-primary').submit()

    time.sleep(5)
    os.remove(path) #удаляем созданный файл

finally:
    driver.quit()