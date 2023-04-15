import os
import time

from selenium import webdriver

# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# element.send_keys(file_path)

# print('ex_1:', os.path.abspath(__file__))
# print('ex_2:', os.path.abspath(os.path.dirname(__file__)))

link = 'http://suninjuly.github.io/file_input.html'
current_dir: str = os.path.abspath(os.path.dirname(__file__))

with webdriver.Firefox() as browser:
    browser.get(link)

    first_name = browser.find_element_by_name('firstname')
    first_name.send_keys('Yourvan')

    last_name = browser.find_element_by_name('lastname')
    last_name.send_keys('ubvanov')

    email = browser.find_element_by_name('email')
    email.send_keys('1@mail.ru')

    file_name = 'file.txt'
    file_path: str = os.path.join(current_dir, file_name)
    # downloading = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    downloading = browser.find_element_by_name('file')
    downloading.send_keys(file_path)

    button = browser.find_element_by_class_name('btn-primary')
    button.click()
    time.sleep(7)

    if False:
        alert = browser.switch_to.alert
        alert.accept()

        alert = browser.switch_to.alert
        alert_text = alert.text

        confirm = browser.switch_to.alert
        confirm.dismiss()

        prompt = browser.switch_to.alert
        prompt.send_keys("My answer")
        prompt.accept()
