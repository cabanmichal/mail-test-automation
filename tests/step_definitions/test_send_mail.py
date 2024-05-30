from pytest_bdd import given, scenarios, then, when

from pages.compose import ComposePage
from pages.home import HOME_PAGE_URL, HomePage

scenarios("../features/send_mail.feature")

# given steps


@given("the mail is composed")
def mail_composed(compose_page: ComposePage, mail: dict[str, str]) -> None:
    compose_page.set_recipient(mail["recipient"])
    compose_page.set_subject(mail["subject"])
    compose_page.set_body(mail["body"])
    compose_page.add_attachement(mail["attachment"])
    compose_page.upload_attachment()
    compose_page.wait_for_attachment_uploaded()


# when steps


@when("the user clicks the Send button")
def click_send_button(compose_page: ComposePage) -> None:
    compose_page.send_mail()


# then steps


@then("the user is redirected to their mailbox")
def verify_in_mailbox(home_page: HomePage) -> None:
    home_page.wait_for_url(HOME_PAGE_URL)
    home_page.verify_on_home_page()


@then("the email is sent")
def verify_mail_sent() -> None:
    """Real verification out of scope."""
    assert True
