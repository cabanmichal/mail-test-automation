from pytest_bdd import parsers, scenarios, then, when

from pages.compose import ComposePage

scenarios("../features/add_recipient.feature")


# when steps


@when(parsers.parse("the user selects the address book {address_book}"))
def select_address_book(compose_page: ComposePage, address_book: str) -> None:
    compose_page.select_address_book(address_book)
    compose_page.wait_for_contacts_loaded()


@when(
    parsers.parse("the user double clicks on the contact {contact}"),
    target_fixture="contact",
)
def add_contact(compose_page: ComposePage, contact: str) -> str:
    compose_page.select_contact(contact)

    return contact


# then steps


@then("the contact is added to mail recipients")
def verify_contact_added(compose_page: ComposePage, contact: str) -> None:
    compose_page.verify_contact_added(contact)
