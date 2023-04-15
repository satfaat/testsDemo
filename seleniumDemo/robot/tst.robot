*** Settings ***
Library         SeleniumLibrary
Suite Setup     Go to Google
Suite Teardown  Close Browser

*** Test Cases ***
Ensure that the capital of a country is displayed
    Search and check        Russia      Moscow

*** Keywords ***
Go to Google
    Open Browser    https://www.google.com  ff

Search and check
    [Arguments]     ${query}        ${expected_result}
    Input Text      name=q          ${query}
    Click Button    jsname=Tg7LZd