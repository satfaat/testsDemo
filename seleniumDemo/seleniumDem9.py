from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# link = 'http://suninjuly.github.io/cats.html'
link = 'http://suninjuly.github.io/wait2.html'

with webdriver.Firefox() as browser:
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )

    button.click()
    message = browser.find_element_by_id("verify_message")

    # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
    button = WebDriverWait(browser, 5).until_not(
        EC.element_to_be_clickable((By.ID, "verify"))
    )

    assert "successful" in message.text

    # говорим WebDriver искать каждый элемент в течение 5 секунд
    # browser.implicitly_wait(5)
    # browser.find_element_by_id("button")

    if False:
        browser.get("http://suninjuly.github.io/wait1.html")

        button = browser.find_element_by_id("verify")
        button.click()
        message = browser.find_element_by_id("verify_message")

        assert "successful" in message.text
