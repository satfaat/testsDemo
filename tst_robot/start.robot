*** Settings ***
Documentation   Starter robot for the Beginners' course. You, a human being (just assuming!)
Library         SeleniumLibrary
Library         RPA.HTTP
Library         RPA.Excel.Files
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
Fill And Submit The Form  # by label hardcoded data
    Input Text      firstname     John
    Input Text      lastname      Smith
    Input Text      salesresult   123
    Select From List By Value    salestarget    10000
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

# *** Tasks ***
# Say hello to the world
#     Log    Hello World!

*** Tasks ***
Insert the sales data for the week and export it as a PDF
    Open The Intranet Website
    Log In
    Download The Excel File
    Fill The Form Using The Data From The Excel File
