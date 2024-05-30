from playwright.sync_api import Page, expect

LOGIN_PAGE_URL = "https://webmail.wedos.net/"


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.login_form = page.locator("#login-form")
        self.username_input = page.locator("#rcmloginuser")
        self.password_input = page.locator("#rcmloginpwd")
        self.login_button = page.locator("#rcmloginsubmit")
        self.warning = page.locator("#message > .warning")

    def navitage(self) -> None:
        self.page.goto(LOGIN_PAGE_URL)

    def enter_username(self, username: str) -> None:
        self.username_input.fill(username)

    def enter_password(self, password: str) -> None:
        self.password_input.fill(password)

    def click_login_button(self) -> None:
        self.login_button.click()

    def login(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def verify_logged_out(self) -> None:
        expect(self.login_form).to_be_visible()

    def verify_warning_shown(self) -> None:
        expect(self.warning).to_be_visible()
