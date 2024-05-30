@add_recipient
Feature: Select a contact from an address book

    Scenario Outline: Add contact to recipients
        Given the user is logged-in to their mailbox
        And the mail compose dialog is shown
        When the user selects the address book <address_book>
        And the user double clicks on the contact <contact>
        Then the contact is added to mail recipients

        Examples:
            | address_book       | contact                          |
            | Personal Addresses | John Doe <john.doe@example.test> |
