from dataclasses import dataclass
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from . import locator
from .base_page import BasePage


@dataclass(frozen=True)
class BaseInputPageLocator:
    input_field: locator = (
        By.XPATH, 
        '//input[@class="textinput textInput form-control"]'
    )


class BaseInputPage(BasePage):
    def __init__(self, browser: WebDriver, timeout: int = 5) -> None:
        super().__init__(browser, timeout)
        self.url = self.url + '/elements/input'

    @property
    def input_field(self) -> WebElement:
        return self.find(*BaseInputPageLocator.input_field)

    def fill_and_press_enter(self, text: str) -> None:
        self.input_field.send_keys(text + Keys.ENTER)
