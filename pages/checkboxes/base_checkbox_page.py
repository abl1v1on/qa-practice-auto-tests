from dataclasses import dataclass
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages import locator
from pages.base_page import BasePage


@dataclass(frozen=True)
class BaseCheckboxPageLocator:
    submit_button: locator = (By.ID, 'submit-id-submit')


class BaseCheckboxPage(BasePage):
    def __init__(self, browser: WebDriver, timeout: int = 5) -> None:
        super().__init__(browser, timeout)
        self.url = self.url + '/elements/checkbox'

    @property
    def submit_button(self) -> WebElement:
        return self.find(*BaseCheckboxPageLocator.submit_button)

    def click_to_btn(self) -> None:
        self.submit_button.click()

    def select_checkbox(self, checkbox: WebElement | list[WebElement]) -> None:
        if isinstance(checkbox, list):
            for cb in checkbox:
                cb.click()
        else:
            checkbox.click()

    def select_checkbox_by_label(self, label: WebElement | list[WebElement]) -> None:
        if isinstance(label, list):
            for l in label:
                l.click()
        else:
            label.click()
