"""
The task: https://stepik.org/lesson/138920/step/10?unit=196194
Only filling in the required fields.
"""

from selenium import webdriver
import time


link_tested_site1 = "http://suninjuly.github.io/registration1.html"
link_tested_site2 = "http://suninjuly.github.io/registration2.html"

"""
Option one. Unique search - correct
"""
try:
    browser = webdriver.Firefox()
    for link_tested_site in link_tested_site1, link_tested_site2:
        browser.get(link_tested_site)

        input_first_name = browser.find_element_by_css_selector(
            ".first_class > input[required='']")
        input_first_name.send_keys("Ihar")
        time.sleep(0.7)

        input_email = browser.find_element_by_css_selector(
            ".second_class > input[required='']")
        input_email.send_keys("Alishkevich")
        time.sleep(0.7)

        input_email = browser.find_element_by_css_selector(
            ".third_class > input[required='']")
        input_email.send_keys("IharAlishkevich@gmail.com")
        time.sleep(0.7)

        submit_button = browser.find_element_by_css_selector("button.btn")
        submit_button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(2)
    browser.quit()

"""
Option two. Complete search - correct
"""
try:
    browser = webdriver.Chrome()
    for link_tested_site in link_tested_site1, link_tested_site2:
        browser.get(link_tested_site)

        required_inputs_elements = browser.find_elements_by_tag_name(
            "input[required='']")
        assert len(required_inputs_elements) == 3

        for require_input_element in required_inputs_elements:
            require_input_element.send_keys("Test value")
            time.sleep(0.7)

        submit_button = browser.find_element_by_css_selector("button.btn")
        submit_button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(2)
    browser.quit()
