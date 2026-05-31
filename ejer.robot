*** settings ***
Library    SeleniumLibrary

*** test cases ***
Login Correcto

    Open Browser    https://www.saucedemo.com/    chrome

    Maximize Browser Window

    Input Text    id:user-name    standard_user

    Input Text    id:password    secret_sauce

    Click Button    id:login-button

    Capture Page Screenshot    mi_captura.png


    Sleep    3s

    Close Browser
