from pytest_bdd import scenarios, then, when

from pages.home import HOME_PAGE_URL, HomePage
from pages.login import LoginPage

scenarios("../features/login_logout.feature")

# when steps


@when("the user enters valid username")
def enter_username(login_page: LoginPage, credentials: dict[str, str]) -> None:
    login_page.enter_username(credentials["valid_username"])


@when("the user enters valid password")
def enter_password(login_page: LoginPage, credentials: dict[str, str]) -> None:
    login_page.enter_password(credentials["valid_password"])


@when("the user enters invalid username")
def enter_invalid_username(login_page: LoginPage, credentials: dict[str, str]) -> None:
    login_page.enter_username(credentials["invalid_username"])


@when("the user enters invalid password")
def enter_invalid_password(login_page: LoginPage, credentials: dict[str, str]) -> None:
    login_page.enter_password(credentials["invalid_password"])


@when("the user clicks the Login button")
def click_login_button(login_page: LoginPage) -> None:
    login_page.click_login_button()


@when("the user cklicks the Logout button")
def click_logout_button(home_page: HomePage) -> None:
    home_page.logout()


# then steps


@then("the user is logged-in to their mailbox")
def verify_user_logged_in(home_page: HomePage, credentials: dict[str, str]) -> None:
    home_page.wait_for_url(HOME_PAGE_URL)
    home_page.verify_username(credentials["valid_username"])
    home_page.verify_on_home_page()


@then("the login fails")
@then("the user is logged-out")
def verify_login_failed(login_page: LoginPage) -> None:
    login_page.verify_logged_out()


@then("a warning is shown")
def verify_warning_shown(login_page: LoginPage) -> None:
    login_page.verify_warning_shown()
