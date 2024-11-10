*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page
*** Test Cases ***
Register With Valid Username And Password
    Set Username  boris
    Set Password    salainen007
    Set Confirmation    salainen007
    Submit Credentials 
    Register Should Succeed
Register With Too Short Username And Valid Password
    Set Username  bo
    Set Password    salainen007
    Set Confirmation    salainen007
    Submit Credentials
    Register Should Fail With Message    Too short username!

Register With Valid Username And Too Short Password
    Set Username  boris
    Set Password    s
    Set Confirmation    s
    Submit Credentials
    Register Should Fail With Message    Too short password!

Register With Valid Username And Invalid Password
    Set Username  boris
    Set Password    salainen
    Set Confirmation    salainen
    Submit Credentials
    Register Should Fail With Message    Invalid password!




Register With Nonmatching Password And Password Confirmation
    Set Username  boris
    Set Password    salainen007
    Set Confirmation    salainen
    Submit Credentials
    Register Should Fail With Message   Nonmatching passwords! 

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password    salainen007
    Set Confirmation    salainen007
    Submit Credentials
    Register Should Fail With Message    User already exists!




*** Keywords ***
Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation
    [Arguments]    ${password_confirmation}
    Input Password    password_confirmation    ${password_confirmation}
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

