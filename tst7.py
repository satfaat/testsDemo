import time
import math

from selenium import webdriver

link = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Firefox() as browser:
    browser.get(link)

    browser.find_element_by_class_name('btn-primary').click()

    browser.switch_to.alert.accept()
    time.sleep(3)
    x = browser.find_element_by_id('input_value').text
    answer = calc(x)

    browser.find_element_by_id('answer').send_keys(answer)
    browser.find_element_by_class_name('btn-primary').click()
    time.sleep(10)

    if False:
        browser.switch_to.window(window_name)
        new_window = browser.window_handles[1]
        first_window = browser.window_handles[0]
        current_window = browser.current_window_handle
    
