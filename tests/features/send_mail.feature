@send
Feature: Send an email to a contact from an address book

    Scenario: Send the email
        Given the user is logged-in to their mailbox
        And the mail compose dialog is shown
        And the mail is composed
        When the user clicks the Send button
        Then the user is redirected to their mailbox
        And the email is sent
