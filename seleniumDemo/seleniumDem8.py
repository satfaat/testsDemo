import time
import math

from selenium import webdriver

link = 'http://suninjuly.github.io/redirect_accept.html'


def calc(x) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Firefox() as browser:
    browser.get(link)

    browser.find_element_by_class_name('trollface').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(2)

    x = browser.find_element_by_id('input_value').text
    answer: str = calc(x)
    browser.find_element_by_id('answer').send_keys(answer)

    browser.find_element_by_class_name('btn-primary').click()
    time.sleep(7)

    if False:
        message = browser.find_element_by_id("verify_message")
        assert "successful" in message.text
