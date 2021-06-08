import time
import math

from selenium import webdriver

link = 'http://suninjuly.github.io/get_attribute.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))  # ln(abs(12*sin(x)))

with webdriver.Firefox() as browser:
    browser.get(link)

    x = browser.find_element_by_id('treasure')
    value_x = x.get_attribute('valuex')
    print(value_x)

    answer = calc(value_x)
    input_answer = browser.find_element_by_id('answer')
    input_answer.send_keys(answer)
    time.sleep(2)

    robot_chk = browser.find_element_by_id('robotCheckbox')
    robot_chk.click()

    robot_rad_btn = browser.find_element_by_id('robotsRule')
    robot_rad_btn.click()

    button = browser.find_element_by_class_name('btn-default')
    button.click()
    time.sleep(10)

    if False:
        browser.find_element_by_tag_name("select").click()
        browser.find_element_by_css_selector("option:nth-child(2)").click()
        browser.find_element_by_css_selector("[value='1']").click()

        from selenium.webdriver.support.ui import Select
        select = Select(browser.find_element_by_tag_name("select"))
        select.select_by_value("1") # ищем элемент с текстом "Python"
        # select.select_by_visible_text("text")
        # select.select_by_index(index)
