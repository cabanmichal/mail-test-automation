@compose
Feature: Compose an email

    Scenario: Open the mail compose dialog
        Given the user is logged-in to their mailbox
        When the user clicks on the mail compose button
        Then the mail compose dialog is shown

    Scenario Outline: Compose an email
        Given the user is logged-in to their mailbox
        And the mail compose dialog is shown
        When the user adds a contact <contact> to the recipients
        And the user enters text <subject> to Subject field
        And the user enters text <body> to mail body area
        Then the To field, Subject field and mail body are filled-in

        Examples:
            | contact               | subject          | body                           |
            | john.doe@example.test | Hi from the test | Mail sent by an automated test |

    @attachment
    Scenario: Attach an attachment
        Given the user is logged-in to their mailbox
        And the mail compose dialog is shown
        When the user clicks on the Attach button and selects the "attachment.txt" file
        And the user uploads the attachment
        Then the file is attached to the email