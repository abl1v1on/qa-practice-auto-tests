from dataclasses import dataclass
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from pages import locator
from .base_input_page import BaseInputPage


@dataclass(frozen=True)
class TextInputPageLocator:
    text_field: locator = (By.NAME, 'text_string')


class TextInputPage(BaseInputPage):
    def __init__(self, browser: WebDriver, timeout: int = 5) -> None:
        super().__init__(browser, timeout)
        self.url = self.url + '/simple'

    @property
    def text_field(self) -> WebElement:
        return super().input_field
