import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'

with webdriver.Firefox() as browser:
    browser.get(link)

    #browser.execute_script("alert('Robots at work');")
    #browser.execute_script("document.title='Script executing';")
    browser.execute_script("document.title='Script executing';alert('Robots at work');")
    element = browser.execute_script('document.getElementsByName("name")')
    # "return arguments[0].scrollIntoView(true);"
    time.sleep(7)

    num_1 = browser.find_element_by_id('num1').text
    num_2 = browser.find_element_by_id('num2').text
    sum = int(num_1) + int(num_2)

    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(sum))
    #time.sleep(1)

    button = browser.find_element_by_class_name('btn-default')
    button.click()
    time.sleep(5)

    if False:
        button = browser.find_element_by_tag_name("button")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
        # browser.execute_script("window.scrollBy(0, 100);")
        # javascript
        button = document.getElementsByTagName("button")[0];
        button.scrollIntoView(true);