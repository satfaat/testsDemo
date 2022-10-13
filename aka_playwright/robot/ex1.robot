*** Settings ***
Library     Browser
Variables   ../.devdata/variables.py

# *** Test Cases ***
# Example Test
#     New Page    https://playwright.dev
#     Get Text    h1    contains    Playwright

*** Keywords ***
Open Page
    Open Browser    https://www.mantisbt.org/bugs/my_view_page.php      firefox
    #New Page        https://www.mantisbt.org/bugs/my_view_page.php

*** Keywords ***
Do Login
    Click  css=div.btn-group:nth-child(2) > a:nth-child(1)
    Type Text  id=username        ${secret}[username]
    Click     css=.width-40

*** Keywords ***
Do password
    #Wait Until Page Contains Element    id:password
    Type Secret  id=password    ${secret}[password]
    Click     css=.width-40

*** Keywords ***
Sucsessful Login
    Get Text  css=.user-info    *=  anonymous

*** Tasks ***
Login checkup
    Open Page
    Do Login
    Do password
    Sucsessful Login