
*** Settings ***
Library   Browser

*** Test Cases ***
Open page
    New Page    https://lps.alvexo.ae/discover-the-stock-test  #https://trader.alvexo.com/login-area-new/sign-up
    #Get Text    h1    ==   Sign up
    Get Text    css=.h2-desktop   ==   امُؤسس يتميز بتركيزه

*** Test Cases ***
Fulfill form
    #Click       \#input form-control fullName invalid 
    Type Text   xpath=//input[@name="FirstName"]          Ian
    Type Text   xpath=//input[@name="Email"]                Ian@m.co
    Type Text   xpath=//input[@name="PhoneCountryCode"]      1998993344
    #Type Text  xpath=//input[@name="Password"]      Hebf782h
    Click       submit