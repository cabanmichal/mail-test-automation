from playwright.sync_api import Page, expect

from pages.base import BasePage

HOME_PAGE_URL = "https://webmail.wedos.net/?_task=mail&_mbox=INBOX"


class HomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.toolbar = MessageToolbar(page)

    def verify_on_home_page(self) -> None:
        expect(self.toolbar.compose_button).to_be_visible()

    def logout(self) -> None:
        self.top_line.logout.click()

    def compose_mail(self) -> None:
        self.toolbar.compose_button.click()


# helper classes


class MessageToolbar:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.checkmail_button = page.locator("#messagetoolbar .button.checkmail")
        self.back_button = page.locator("#messagetoolbar .button.back")
        self.compose_button = page.locator("#messagetoolbar .button.compose")
        self.attach_button = page.locator("#messagetoolbar .button.attach")
        self.send_button = page.locator("#messagetoolbar .button.send")
        self.delete_button = page.locator("#messagetoolbar .button.delete")
