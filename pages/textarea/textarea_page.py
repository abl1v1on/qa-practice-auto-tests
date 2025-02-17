from dataclasses import dataclass
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from pages import locator
from pages.base_page import BasePage


@dataclass(frozen=True)
class TextareaPageLocator:
    textarea: locator = (By.ID, 'id_text_area')
    submit_button: locator = (By.ID, 'submit-id-submit')


class TextareaPage(BasePage):
    def __init__(self, browser: WebDriver, timeout: int = 5) -> None:
        super().__init__(browser, timeout)
        self.url = self.url + '/elements/textarea/single'
    
    @property
    def textarea(self) -> WebElement:
        return self.find(*TextareaPageLocator.textarea)

    @property
    def submit_button(self) -> WebElement:
        return self.find(*TextareaPageLocator.submit_button)

    def fill_textarea(self, text: str) -> None:
        self.textarea.send_keys(text)
    
    def submit(self) -> None:
        self.submit_button.click()
