*** Settings ***
Documentation   Starter robot for the Beginners' course. You, a human being (just assuming!)
Library         RPA.Browser.Selenium 
#Library         SeleniumLibrary
Library         RPA.HTTP
Library         RPA.Excel.Files
Library         RPA.PDF
#Library         RequestsLibrary

*** Keywords ***
Open The Intranet Website
    Open Browser    https://robotsparebinindustries.com/

*** Keywords ***
Log In  # by name attr
    Input Text      username    maria
    Input Password  password    thoushallnotpass
    Submit Form
    Wait Until Page Contains Element    id:sales-form

*** Keywords ***
Fill And Submit The Form For One Person
    [Arguments]    ${sales_rep}
    Input Text      firstname     ${sales_rep}[First Name]
    Input Text      lastname      ${sales_rep}[Last Name]
    Input Text      salesresult   ${sales_rep}[Sales]
    ${target_as_string}=    Convert To String    ${sales_rep}[Sales Target]
    Select From List By Value    salestarget    ${target_as_string}
    Click Button    Submit

*** Keywords ***
Download The Excel file
    Download    https://robotsparebinindustries.com/SalesData.xlsx      target_file=tmp/SalesData.xlsx    overwrite=True
    # GET Request : url=https://robotsparebinindustries.com/SalesData.xlsx

*** Keywords ***
Fill The Form Using The Data From The Excel File
    Open Workbook       tmp/SalesData.xlsx
    ${sales_reps}=      Read Worksheet As Table    header=True
    Close Workbook
    FOR    ${sales_rep}    IN    @{sales_reps}
        Fill And Submit The Form For One Person    ${sales_rep}
    END

*** Keywords ***
Collect The Results
    #Screenshot    css:div.sales-summary    ${CURDIR}${/}screenshot${/}sales_summary.png
    Screenshot    css:div.sales-summary    tmp_screenshot/sales_summary.png

*** Keywords ***
Export The Table As A PDF
    Wait Until Element Is Visible    id:sales-results
    ${sales_results_html}=    Get Element Attribute    id:sales-results    outerHTML
    Html To Pdf    ${sales_results_html}    tmp/sales_results.pdf

*** Keywords ***
Log Out And Close The Browser
    Click Button    Log out
    Close Browser

# *** Tasks ***
# Say hello to the world
#     Log    Hello World!

*** Tasks ***
Insert the sales data for the week and export it as a PDF
    Open The Intranet Website
    Log In
    Download The Excel File
    Fill The Form Using The Data From The Excel File
    Collect The Results
    Export The Table As A PDF
    [Teardown]    Log Out And Close The Browser
