from dataclasses import dataclass
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

from pages import locator
from pages.buttons.base_button_page import BaseButtonPage


@dataclass(frozen=True)
class DisabledButtonPageLocator:
    button_state_selector: locator = (By.ID, 'id_select_state')


class DisabledButtonPage(BaseButtonPage):
    def __init__(self, browser: WebDriver, timeout: int = 5) -> None:
        super().__init__(browser, timeout)
        self.url = self.url + '/disabled'

    @property
    def disabled_button(self) -> WebElement:
        return super().button

    @property
    def button_state_selector(self) -> WebElement:
        return self.find(*DisabledButtonPageLocator.button_state_selector)

    def select_state(self, value: str) -> None:
        select = Select(self.button_state_selector)
        select.select_by_value(value)
