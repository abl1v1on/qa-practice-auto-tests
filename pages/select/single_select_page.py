from dataclasses import dataclass
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

from pages import locator
from pages.base_page import BasePage


@dataclass(frozen=True)
class SingleSelectPageLocator:
    choose_lang_select: locator = (By.ID, 'id_choose_language')
    submit_button: locator = (By.ID, 'submit-id-submit')


class SingleSelectPage(BasePage):
    def __init__(self, browser: WebDriver, timeout: int = 5) -> None:
        super().__init__(browser, timeout)
        self.url = self.url + '/elements/select/single_select'
    
    @property
    def choose_lang_select(self) -> Select:
        return self.find(*SingleSelectPageLocator.choose_lang_select)
 
    @property
    def submit_button(self) -> WebElement:
        return self.find(*SingleSelectPageLocator.submit_button)

    def select_lang_by_value(self, value: str) -> None:
        select = Select(self.choose_lang_select)
        select.select_by_value(value)

    def submit(self) -> None:
        self.submit_button.click()
