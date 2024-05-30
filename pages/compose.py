import re

from playwright.sync_api import Locator, Page, expect

from pages.home import HomePage

COMPOSE_PAGE_URL = "https://webmail.wedos.net/?_task=mail&_action=compose*"


class ComposePage(HomePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.contacts = Contacts(page)
        self.to_input = page.locator("#_to")
        self.subject_input = page.locator("#compose-subject")
        self.mail_body = page.locator("#composebody")
        self.attachments = page.locator("#attachment-list > li")
        self.upload_button = page.locator(
            "#upload-dialog .formbuttons .button.mainaction"
        )

    def select_address_book(self, name: str) -> None:
        """Click on the address book with given name."""
        for address_book in self.contacts.address_books.all():
            value = address_book.inner_text()

            if value == name:
                address_book.click()
                break

    def select_contact(self, contact: str) -> None:
        """Doubleclick on the contact with given name and address.

        Expects contact in format "Name <email@address>"
        """
        for current_contact in self.contacts.contacts.all():
            name_and_address = Contact(current_contact).name_and_address

            if name_and_address == contact:
                current_contact.dblclick()
                break

    def send_mail(self) -> None:
        self.toolbar.send_button.click()

    def set_subject(self, text: str) -> None:
        self.subject_input.fill(text)

    def set_body(self, text: str) -> None:
        self.mail_body.fill(text)

    def set_recipient(self, recipient: str) -> None:
        self.to_input.fill(recipient)

    def add_attachement(self, attachement: str) -> None:
        with self.page.expect_file_chooser() as fc:
            self.toolbar.attach_button.click()
            fc.value.set_files(attachement)

    def upload_attachment(self) -> None:
        self.upload_button.click()

    def verify_on_compose_page(self) -> None:
        expect(self.mail_body).to_be_visible()

    def verify_attachment_attached(self, attachment: str) -> None:
        names = [Attachment(a).name for a in self.attachments.all()]
        assert attachment in names

    def verify_subject_set(self, subject: str) -> None:
        expect(self.subject_input).to_have_value(subject)

    def verify_body_set(self, body: str) -> None:
        expect(self.mail_body).to_have_value(body)

    def verify_contact_added(self, contact: str) -> None:
        expect(self.to_input).to_have_value(re.compile(Contact.normalize(contact)))

    def wait_for_contacts_loaded(self) -> None:
        expect(self.contacts.contacts).not_to_have_count(0)

    def wait_for_attachment_uploaded(self) -> None:
        expect(self.attachments.last).not_to_have_class("uploading")


# helper classes


class Contacts:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.sidebar = page.locator("#compose-contacts")
        self.address_books = page.locator("#directorylist > li > a")
        self.contacts = page.locator("#contacts-table tr")


class Contact:
    def __init__(self, locator: Locator) -> None:
        self.locator = locator
        self._name: str | None = None
        self._address: str | None = None

    @property
    def name(self) -> str:
        if self._name is None:
            contact = self.locator.inner_text().strip()
            if "@" in contact:
                parsed = re.match(r"(.+)\s *<?.+?>?", contact)
                assert parsed is not None
                self._name = parsed.group(1)
            else:
                self._name = contact

        return str(self._name)

    @property
    def address(self) -> str:
        if self._address is None:
            self._address = self.locator.locator("a").first.get_attribute("title")

        return str(self._address)

    @property
    def name_and_address(self) -> str:
        return f"{self.name} <{self.address}>"

    @staticmethod
    def normalize(contact: str) -> str:
        return re.sub(r"\s+", " ", contact)


class Attachment:
    def __init__(self, locator: Locator) -> None:
        self.locator = locator
        self._name: str | None = None

    @property
    def name(self) -> str:
        if self._name is None:
            name_and_size = self.locator.inner_text().strip()
            size = self.locator.locator(".attachment-size").inner_text()
            self._name = name_and_size.replace(size, "").strip()

        return str(self._name)
