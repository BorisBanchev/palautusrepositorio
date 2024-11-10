*** Settings ***
Resource  resource.robot
Resource    login.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page
*** Test Cases ***
Register With Valid Username And Password
    Set Username  boris
    Set Password    salainen007
    Set Confirmation    salainen007
    Submit Credentials Register
    Register Should Succeed
Register With Too Short Username And Valid Password
    Set Username  bo
    Set Password    salainen007
    Set Confirmation    salainen007
    Submit Credentials Register
    Register Should Fail With Message    Too short username!

Register With Valid Username And Too Short Password
    Set Username  boris
    Set Password    s
    Set Confirmation    s
    Submit Credentials Register
    Register Should Fail With Message    Too short password!

Register With Valid Username And Invalid Password
    Set Username  boris
    Set Password    salainen
    Set Confirmation    salainen
    Submit Credentials Register
    Register Should Fail With Message    Invalid password!




Register With Nonmatching Password And Password Confirmation
    Set Username  boris
    Set Password    salainen007
    Set Confirmation    salainen
    Submit Credentials Register
    Register Should Fail With Message   Nonmatching passwords! 

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password    salainen007
    Set Confirmation    salainen007
    Submit Credentials Register
    Register Should Fail With Message    User already exists!

Login After Successful Registration
    Set Username    boris
    Set Password    salainen007
    Set Confirmation    salainen007
    Submit Credentials Register
    Register Should Succeed
    Click Link    Continue to main page
    Main Page Should Be Open
    Click Button    Logout
    Login Page Should Be Open
    Set Username  boris
    Set Password  salainen007
    Submit Credentials Login
    Login Should Succeed

Login After Failed Registration
    Set Username    bo
    Set Password    salainen007
    Set Confirmation    salainen007
    Submit Credentials Register
    Register Should Fail With Message    Too short username!
    Click Link    Login
    Login Page Should Be Open
    Set Username  bo
    Set Password  salainen007
    Submit Credentials Login
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
Login Should Succeed
    Main Page Should Be Open
Submit Credentials Register
    Click Button  Register

Submit Credentials Login
    Click Button  Login

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

