from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.buttons.base_button_page import BaseButtonPage


class LikeAButtonPage(BaseButtonPage):
    def __init__(self, browser: WebDriver, timeout: int = 5):
        super().__init__(browser, timeout)
        self.url = self.url + '/like_a_button'

    @property
    def look_like_button_link(self) -> WebElement:
        return super().button
