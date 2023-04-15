import time
import math

from selenium import webdriver

link = 'http://suninjuly.github.io/math.html'


def calc(x) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Firefox() as browser:
    browser.get(link)

    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    # assert people_checked == "true", "People radio is not selected by default"

    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robot radio: ", robots_checked)
    assert robots_checked is None

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y: str = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    time.sleep(2)

    robot_chk = browser.find_element_by_id('robotCheckbox')
    robot_chk.click()

    robot_rad_btn = browser.find_element_by_id('robotsRule')
    robot_rad_btn.click()

    button = browser.find_element_by_class_name('btn-default')
    button.click()
    time.sleep(10)
