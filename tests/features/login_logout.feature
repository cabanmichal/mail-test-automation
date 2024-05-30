@login_logout
Feature: Login to mailbox and logout

    @login
    Scenario: Login with valid credentials
        Given the login page is shown
        When the user enters valid username
        And the user enters valid password
        And the user clicks the Login button
        Then the user is logged-in to their mailbox

    @login @invalid
    Scenario: Login with valid username and invalid password
        Given the login page is shown
        When the user enters valid username
        And the user enters invalid password
        And the user clicks the Login button
        Then the login fails
        And a warning is shown

    @login @invalid
    Scenario: Login with invalid username and valid password
        Given the login page is shown
        When the user enters invalid username
        And the user enters valid password
        And the user clicks the Login button
        Then the login fails
        And a warning is shown

    @logout
    Scenario: Logout
        Given the user is logged-in to their mailbox
        When the user cklicks the Logout button
        Then the user is logged-out