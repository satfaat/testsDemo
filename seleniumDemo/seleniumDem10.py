import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://suninjuly.github.io/explicit_wait2.html'


def calc(x) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Firefox() as browser:
    browser.get(link)
    # browser.implicitly_wait(5)

    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    browser.find_element_by_id('book').click()

    x = browser.find_element_by_id('input_value').text
    answer: str = calc(x)
    browser.find_element_by_id('answer').send_keys(answer)

    browser.find_element_by_id('solve').click()
    time.sleep(8)

    if False:
        assert abs(-42) == -42, "Should be absolute value of a number"
        assert self.is_element_present(
            'new_announcement_button', timeout=30), "No new announcement button on profile page"
        # считываем текст и записываем его в переменную
        catalog_text = self.catalog_link.text
        assert catalog_text == "Каталог", \
            f"Wrong language, got {catalog_text} instead of 'Каталог'"

        # str.format
        "Let's count together: {}, then goes {}, and then {}".format(
            "one", "two", "three")

        # f string
        actual_result = "abrakadabra"
        f"Wrong text, got {actual_result}, something wrong"
