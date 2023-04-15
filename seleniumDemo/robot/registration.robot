*** Settings ***
Documentation   Registration on site
Library         SeleniumLibrary


*** Keywords ***
Open The Intranet Website
    Open Browser    https://www.mantisbt.org/bugs/my_view_page.php

*** Keywords ***
Do Registration
    Click Link  css:a.btn:nth-child(2)
    Wait Until Page Contains Element    id:signup-form
    Input Text  username        Tom
    Input Text  email-field     1@mail.ru
    Submit Form

*** Keywords ***
Sucsessful Registration
    Wait Until Page Contains Element    class:user-info
    Element Should Contain  class:user-info     Tom

*** Keywords ***
Close The Browser
    Close Browser

*** Tasks ***
Registration checkup
    Open The Intranet Website
    Do Registration
    Sucsessful Registration
    [Teardown]  Close The Browser