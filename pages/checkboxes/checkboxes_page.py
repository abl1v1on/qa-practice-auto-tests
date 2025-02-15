from dataclasses import dataclass
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages import locator
from pages.checkboxes.base_checkbox_page import BaseCheckboxPage


@dataclass(frozen=True)
class CheckboxesPageLocator:
    one_checkbox: locator = (By.ID, 'id_checkboxes_0')
    one_checkbox_label: locator = (By.XPATH, '//label[@for="id_checkboxes_0"]')
    two_checkbox: locator = (By.ID, 'id_checkboxes_1')
    two_checkbox_label: locator = (By.XPATH, '//label[@for="id_checkboxes_1"]')
    three_checkbox: locator = (By.ID, 'id_checkboxes_2')
    three_checkbox_label: locator = (By.XPATH, '//label[@for="id_checkboxes_2"]')


class CheckboxesPage(BaseCheckboxPage):
    def __init__(self, browser: WebDriver, timeout: int = 5) -> None:
        super().__init__(browser, timeout)
        self.url = self.url + '/mult_checkbox'

    @property
    def one_checkbox(self) -> WebElement:
        return self.find(*CheckboxesPageLocator.one_checkbox)

    @property
    def one_checkbox_label(self) -> WebElement:
        return self.find(*CheckboxesPageLocator.one_checkbox_label)

    @property
    def two_checkbox(self) -> WebElement:
        return self.find(*CheckboxesPageLocator.two_checkbox)

    @property
    def two_checkbox_label(self) -> WebElement:
        return self.find(*CheckboxesPageLocator.two_checkbox_label)

    @property
    def three_checkbox(self) -> WebElement:
        return self.find(*CheckboxesPageLocator.three_checkbox)

    @property
    def three_checkbox_label(self) -> WebElement:
        return self.find(*CheckboxesPageLocator.three_checkbox_label)
