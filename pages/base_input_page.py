from dataclasses import dataclass
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from . import locator
from .base_page import BasePage


@dataclass(frozen=True)
class BaseInputPageLocator:
    result_block: locator = (By.ID, 'result')
    result_text: locator = (By.ID, 'result-text')
    error_message: locator = (
        By.XPATH, 
        '//span/strong'
    )
    input_field: locator = (
        By.XPATH, 
        '//input[@class="textinput textInput form-control"]'
    )


class BaseInputPage(BasePage):
    def __init__(self, browser: WebDriver, timeout: int = 5) -> None:
        super().__init__(browser, timeout)
        self.url = self.url + '/elements/input'

    @property
    def result_block(self) -> WebElement:
        return self.find(*BaseInputPageLocator.result_block)

    @property
    def result_text(self) -> WebElement:
        return self.find(*BaseInputPageLocator.result_text)
    
    @property
    def error_message(self) -> WebElement:
        return self.find(*BaseInputPageLocator.error_message)

    @property
    def input_field(self) -> WebElement:
        return self.find(*BaseInputPageLocator.input_field)

    def check_result_text(self, text: str) -> bool:
        expected_result = text
        actual_result = self.result_text.text
        return True if expected_result == actual_result else False

    def check_error_message(self, error: str) -> bool:
        expected_error = error 
        actual_error = self.error_message.text
        return True if expected_error == actual_error else False

    def fill_and_press_enter(self, text: str) -> None:
        self.input_field.send_keys(text + Keys.ENTER)
