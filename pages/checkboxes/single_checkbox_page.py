from dataclasses import dataclass
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages import locator
from pages.checkboxes.base_checkbox_page import BaseCheckboxPage


@dataclass(frozen=True)
class SingleCheckBoxPageLocator:
    single_checkbox: locator = (By.ID, 'id_checkbox_0')
    single_checkbox_label: locator = (By.XPATH, '//label[@for="id_checkbox_0"]')


class SingleCheckboxPage(BaseCheckboxPage):
    def __init__(self, browser: WebDriver, timeout: int = 5) -> None:
        super().__init__(browser, timeout)
        self.url = self.url + '/single_checkbox'

    @property
    def single_checkbox(self) -> WebElement:
        return self.find(*SingleCheckBoxPageLocator.single_checkbox)
    
    @property
    def single_checkbox_label(self) -> WebElement:
        return self.find(*SingleCheckBoxPageLocator.single_checkbox_label)
