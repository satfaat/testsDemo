*** Settings ***
Documentation   Search Dara
Library         SeleniumLibrary


*** Variables ***
${URL}          https://specialty.ru/coffee/
${BROWSER}      Firefox
${page_title}   Кофе в зернах в Москве — купить зерновой кофе в интернет-магазине specialty.ru
${search_word}  Dara
${expected_text}   Кофе Ethiopia Sidamo Dara

*** Test Cases ***
Checking search bar
    Open Browser and site
    Confirm geolocation
    Input word for search
    Submit search
    Serched product
    [Teardown]  Close Browser

*** Keywords ***
Open Browser and site
    Open Browser        ${URL}  ${BROWSER}
    Title Should Be     ${page_title}

Confirm geolocation
    [Arguments]
    SeleniumLibrary.Wait Until Element Is Visible    css:.main-header__geo-confirm div:nth-child(1) div:nth-child(2) button:nth-child(2)
    Sleep   2s
    Click Button  css:.main-header__geo-confirm div:nth-child(1) div:nth-child(2) button:nth-child(2)

Input word for search
    [Arguments]     
    Input Text      css:.suggest-search__field     ${search_word}

Submit search
    Click Button    css:.suggest-search__button
    Sleep   1s

Serched product
    Element Text Should Be  css:.coffee-card__title     ${expected_text}