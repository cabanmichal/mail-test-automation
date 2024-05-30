from pytest_bdd import parsers, scenarios, then, when

from pages.compose import COMPOSE_PAGE_URL, ComposePage
from pages.home import HomePage

scenarios("../features/compose_mail.feature")


# when steps


@when("the user clicks on the mail compose button")
def click_mail_compose(home_page: HomePage, compose_page: ComposePage) -> None:
    home_page.compose_mail()
    compose_page.wait_for_url(COMPOSE_PAGE_URL)


@when(parsers.parse("the user enters text {text} to Subject field"))
def set_mail_subject(
    compose_page: ComposePage, text: str, mail: dict[str, str]
) -> None:
    compose_page.set_subject(text)
    mail["subject"] = text


@when(parsers.parse("the user enters text {text} to mail body area"))
def set_mail_body(compose_page: ComposePage, text: str, mail: dict[str, str]) -> None:
    compose_page.set_body(text)
    mail["body"] = text


@when(parsers.parse("the user adds a contact {contact} to the recipients"))
def set_mail_recipient(
    compose_page: ComposePage, contact: str, mail: dict[str, str]
) -> None:
    compose_page.set_recipient(contact)
    mail["recipient"] = contact


@when(
    parsers.parse(
        'the user clicks on the Attach button and selects the "{attachment}" file'
    )
)
def select_attachment(
    compose_page: ComposePage, attachment: str, mail: dict[str, str]
) -> None:
    compose_page.add_attachement(attachment)
    mail["attachment"] = attachment


@when("the user uploads the attachment")
def upload_attachment(compose_page: ComposePage) -> None:
    compose_page.upload_attachment()
    compose_page.wait_for_attachment_uploaded()


# then steps


@then("the mail compose dialog is shown")
def mail_compose_dialog_shown(compose_page: ComposePage) -> None:
    compose_page.wait_for_url(COMPOSE_PAGE_URL)
    compose_page.verify_on_compose_page()


@then("the To field, Subject field and mail body are filled-in")
def verify_mail_composed(compose_page: ComposePage, mail: dict[str, str]) -> None:
    compose_page.verify_contact_added(mail["recipient"])
    compose_page.verify_subject_set(mail["subject"])
    compose_page.verify_body_set(mail["body"])


@then("the file is attached to the email")
def verify_attachment_attached(compose_page: ComposePage, mail: dict[str, str]) -> None:
    compose_page.verify_attachment_attached(mail["attachment"])
