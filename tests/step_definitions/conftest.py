import os

import pytest
from playwright.sync_api import Page
from pytest_bdd import given

from pages.compose import COMPOSE_PAGE_URL, ComposePage
from pages.home import HOME_PAGE_URL, HomePage
from pages.login import LoginPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page)


@pytest.fixture
def compose_page(page: Page) -> ComposePage:
    return ComposePage(page)


@pytest.fixture
def credentials() -> dict[str, str]:
    return {
        "valid_username": os.environ.get("TEST_MAIL_USERNAME", ""),
        "valid_password": os.environ.get("TEST_MAIL_PASSWORD", ""),
        "invalid_username": "nobody@example.invalid",
        "invalid_password": "invalid",
    }


@pytest.fixture
def mail() -> dict[str, str]:
    return {
        "recipient": os.environ.get("TEST_MAIL_RECIPIENT", ""),
        "subject": "Hi from the test",
        "body": "Mail sent by an automated test",
        "attachment": "attachment.txt",
    }


# common steps


@given("the login page is shown")
def login_page_is_shown(login_page: LoginPage) -> None:
    login_page.navitage()
    login_page.verify_logged_out()


@given("the user is logged-in to their mailbox")
def user_logged_in(
    login_page: LoginPage, home_page: HomePage, credentials: dict[str, str]
) -> None:
    login_page.navitage()
    login_page.login(credentials["valid_username"], credentials["valid_password"])

    home_page.wait_for_url(HOME_PAGE_URL)
    home_page.wait_for_loading_done()
    home_page.verify_username(credentials["valid_username"])
    home_page.verify_on_home_page()


@given("the mail compose dialog is shown")
def mail_comopse_is_shown(home_page: HomePage, compose_page: ComposePage) -> None:
    home_page.compose_mail()

    compose_page.wait_for_url(COMPOSE_PAGE_URL)
    compose_page.verify_on_compose_page()
