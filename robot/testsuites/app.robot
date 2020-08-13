*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${app_server}   %{SERVER_URL} 
${name}    Alice
${mob_num}    1234567890
${email_add}    Alice@gmail.com
${pass}    123456
${intro}    Alice from wonderland!!
${Modified_name}    Bob

*** Test Cases ***
Insert Data
    Comment    Open Browser
    Open Browser    ${app_server}    headlesschrome
    Wait Until Element Is Visible    //input[@id="name"]
    Comment    Giving Input to the locators
    Input Text    //input[@id="name"]    ${name}
    Input Text    //input[@id="mobile"]    ${mob_num}
    Input Text    //input[@id="email"]    ${email_add}
    Input Text    //input[@id="password"]    ${pass}
    Input Text    //textarea[@id="introduction"]    ${intro}
    Comment    Submitting the values
    Click Element    //button[text()="Submit"]
    Capture Page Screenshot
    Comment    Validating the values added
    Page Should Contain Element    //tr//td[text()="${name}"]
    Page Should Contain Element    //tr//td[text()="${mob_num}"]
    Page Should Contain Element    //tr//td[text()="${email_add}"]
    Page Should Contain Element    //tr//td[text()="**************"]
    Page Should Contain Element    //tr//td[text()="${intro}"]
    [Teardown]    Close Browser
Modify Data
    Open Browser    ${app_server}    headlesschrome
    Wait Until Element Is Visible    //tr//td[text()="${name}"]/..//td//button[text()="Edit"]
    Click Element    //tr//td[text()="${name}"]/..//td//button[text()="Edit"]
    Capture Page Screenshot
    Input Text    //input[@id="name"]    ${Modified_name}
    Click Element    //button[text()="Update"]
    Capture Page Screenshot
    Comment    Validating the values added
    Page Should Contain Element    //tr//td[text()="${Modified_name}"]
    [Teardown]    Close Browser
Delete Data
    Open Browser    ${app_server}    headlesschrome
    Wait Until Element Is Visible    //tr//td[text()="${Modified_name}"]/..//td//button[text()="Delete"]
    Click Element    //tr//td[text()="${Modified_name}"]/..//td//button[text()="Delete"]
    Page Should Not Contain Element    //tr//td[text()="${Modified_name}"]/..//td//button[text()="Delete"]
    [Teardown]    Close Browser
