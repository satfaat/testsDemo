import time

from selenium import webdriver

link = "http://suninjuly.github.io/registration2.html"

with webdriver.Firefox() as browser:  # Chrome() Firefox()
    browser.get(link)

    first_name =  browser.find_element_by_class_name('first_block .first')
    first_name.send_keys("Ivan")

    last_name = browser.find_element_by_class_name('first_block .second')
    last_name.send_keys("Ivanov")

    email = browser.find_element_by_class_name('first_block .third')
    email.send_keys("Ivan@mail.ru")
    time.sleep(5)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

    time.sleep(10)