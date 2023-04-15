*** Settings ***
Documentation   Login on site
Library         SeleniumLibrary


*** Keywords ***
Open The Intranet Website
    Open Browser    https://www.mantisbt.org/bugs/my_view_page.php

*** Keywords ***
Do Login
    Click Link  css:div.btn-group:nth-child(2) > a:nth-child(1)
    Wait Until Page Contains Element    id:login-form
    Input Text  username        anonymous
    Submit Form

*** Keywords ***
Do password
    Wait Until Page Contains Element    id:password
    Input Password  id:password    anonymous
    Submit Form

*** Keywords ***
Sucsessful Login
    Wait Until Page Contains Element    class:user-info
    Element Should Contain  class:user-info     anonymous

*** Keywords ***
Close The Browser
    Close Browser

*** Tasks ***
Login checkup
    Open The Intranet Website
    Do Login
    Do Password
    Sucsessful Login
    [Teardown]  Close The Browser