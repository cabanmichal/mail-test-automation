from re import Pattern

from playwright.sync_api import Page, expect


class BasePage:
    """Functionality common to many pages."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.top_line = TopLine(page)
        self.top_navigation = TopNavigation(page)
        self.notification_list = NotificationList(page)

    @property
    def username(self) -> str | None:
        if self.top_line.username.is_visible():
            return self.top_line.username.text_content()
        return None

    def verify_username(self, username: str) -> None:
        expect(self.top_line.username).to_have_text(username)

    def wait_for_url(self, url: str | Pattern) -> None:
        self.page.wait_for_url(url)

    def wait_for_loading_done(self) -> None:
        expect(self.notification_list.loading_notifications).to_have_count(0)


# helper classes


class TopLine:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username = page.locator("#topline .username")
        self.logout = page.locator("#topline .button-logout")


class TopNavigation:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.logo = page.locator("#toplogo")
        self.mail_button = page.locator("#topnav .button-mail")
        self.addressbook_button = page.locator("#topnav .button-addressbook")
        self.blacklist_button = page.locator("#topnav .button-wedos-blacklist")
        self.settigns_button = page.locator("#topnav .button-settings")


class NotificationList:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.notifications = page.locator("#messagestack > div")
        self.loading_notifications = page.locator("#messagestack .loading")
