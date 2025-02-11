from dataclasses import dataclass
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from . import locator
from .base_input_page import BaseInputPage


@dataclass(frozen=True)
class EmailInputPageLocator:
    email_field: locator = (By.ID, 'id_email')


class EmailInputPage(BaseInputPage):
    def __init__(self, browser: WebDriver, timeout: int = 5) -> None:
        super().__init__(browser, timeout)
        self.url = self.url + '/email'

    @property
    def email_field(self) -> WebElement:
        return self.find(*EmailInputPageLocator.email_field)

    # TODO: вынеси в базовый класс инпутов
    def fill_and_press_enter(self, email: str) -> None:
        self.email_field.send_keys(email + Keys.ENTER)
