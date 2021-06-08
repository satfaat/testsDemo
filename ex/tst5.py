import math
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/execute_script.html'

def calc(x_value):
  return str(math.log(abs(12*math.sin(int(x_value)))))

with webdriver.Firefox() as browser:
    browser.get(link)

    x_value = browser.find_element_by_id('input_value').text
    answer = calc(x_value)

    input_answer = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_answer)
    input_answer.send_keys(answer)

    robot_chk = browser.find_element_by_id('robotCheckbox')
    robot_chk.click()

    robot_rad_btn = browser.find_element_by_id('robotsRule')
    robot_rad_btn.click()

    button = browser.find_element_by_class_name('btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    time.sleep(10)


    #button = browser.find_element_by_tag_name("button")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #browser.execute_script("window.scrollBy(0, 100);")
    if False:
        #// javascript
        button = document.getElementsByTagName("button")[0];
        button.scrollIntoView(true);

        import os
        from selenium import webdriver
        from selenium.webdriver.common.by import By

        link = "http://suninjuly.github.io/file_input.html"
        browser = webdriver.Firefox()
        browser.get(link)
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_name = "file_example.txt"
        file_path = os.path.join(current_dir, file_name)
        element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
        element.send_keys(file_path)
