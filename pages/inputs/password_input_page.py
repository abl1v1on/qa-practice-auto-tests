from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from .base_input_page import BaseInputPage


class PasswordInputPage(BaseInputPage):
    def __init__(self, browser: WebDriver, timeout: int = 5) -> None:
        super().__init__(browser, timeout)
        self.url = self.url + '/passwd'

    @property
    def password_field(self) -> WebElement:
        return super().input_field
