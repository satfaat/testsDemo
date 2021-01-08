import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

links = {
    'link_1': 'http://suninjuly.github.io/simple_form_find_task.html',
    'link_2': 'https://stepik.org/lesson/25969/step/12',
    'link_3': 'http://suninjuly.github.io/find_link_text',
    'link_4': 'http://suninjuly.github.io/huge_form.html',
    'link_5': 'http://suninjuly.github.io/find_xpath_form',
}

with webdriver.Firefox() as browser:
    #wait = WebDriverWait(browser, 10)
    browser.get(links['link_5'])

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")

    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()
    time.sleep(7)

    if False:
        # Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
        # Ищем поле для ввода текста
        textarea = browser.find_element_by_css_selector(".textarea")

        # Напишем текст ответа в найденное поле
        textarea.send_keys("get()")
        time.sleep(5)

        # Найдем кнопку, которая отправляет введенное решение
        submit_button = browser.find_element_by_css_selector(".submit-submission")

        # Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
        submit_button.click()
        time.sleep(5)

        #button = browser.find_element_by_id("submit_button")
        #button = browser.find_element(By.ID, "submit_button")

    elif False:
        browser.get("https://fake-shop.com/book1.html")

        # добавляем товар в корзину
        add_button = browser.find_element_by_css_selector(".add")
        add_button.click()

        # открываем страницу второго товара
        browser.get("https://fake-shop.com/book2.html")

        # добавляем товар в корзину
        add_button = browser.find_element_by_css_selector(".add")
        add_button.click()

        # тестовый сценарий
        # открываем корзину
        browser.get("https://fake-shop.com/basket.html")

        # ищем все добавленные товары
        goods = browser.find_elements_by_css_selector(".good")

        # проверяем, что количество товаров равно 2
        assert len(goods) == 2
    elif False:
        key = str(math.ceil(math.pow(math.pi, math.e)*10000))
        link = browser.find_element_by_link_text(key)
        link.click()

        input1 = browser.find_element_by_tag_name('input')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_name('last_name')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name('city')
        input3.send_keys("Smolensk")
        input4 = browser.find_element_by_id('country')
        input4.send_keys("Russia")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
    
    elif False:
        elements = browser.find_elements_by_tag_name('input')
        for element in elements:
            element.send_keys("Мой ответ")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()