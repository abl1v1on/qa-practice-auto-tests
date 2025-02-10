from dataclasses import dataclass
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from . import locator
from .base_page import BasePage


@dataclass(frozen=True)
class BaseInputPageLocator:
    result_block: locator = (By.ID, 'result')
    result_text: locator = (By.ID, 'result-text')


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
    
    def check_result_text(self, text: str) -> bool:
        expected_result = text
        actual_result = self.result_text.text
        return True if expected_result == actual_result else False
