from dataclasses import dataclass
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from . import locator
from .base_input_page import BaseInputPage


@dataclass(frozen=True)
class PasswordInputPageLocator:
    password_field: locator = (By.ID, 'id_password')


class PasswordInputPage(BaseInputPage):
    def __init__(self, browser: WebDriver, timeout: int = 5) -> None:
        super().__init__(browser, timeout)
        self.url = self.url + '/passwd'

    @property
    def password_field(self) -> WebElement:
        return self.find(*PasswordInputPageLocator.password_field)
