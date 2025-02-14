from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.buttons.base_button_page import BaseButtonPage


class SimpleButtonPage(BaseButtonPage):
    def __init__(self, browser: WebDriver, timeout: int = 5) -> None:
        super().__init__(browser, timeout)
        self.url = self.url + '/simple'

    @property
    def simple_button(self) -> WebElement:
        return super().button
