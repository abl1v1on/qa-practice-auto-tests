from dataclasses import dataclass
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

from pages import locator
from pages.base_page import BasePage


@dataclass(frozen=True)
class BaseButtonPageLocator:
    submit_button: locator = (By.NAME, 'submit')
    like_a_button: locator = (By.XPATH, '//a[text()="Click"]')


class BaseButtonPage(BasePage):
    def __init__(self, browser: WebDriver, timeout: int = 5) -> None:
        super().__init__(browser, timeout)
        self.url = self.url + '/elements/button'
    
    @property
    def button(self) -> WebElement:
        try:
            return self.find(*BaseButtonPageLocator.submit_button)
        except NoSuchElementException:
            return self.find(*BaseButtonPageLocator.like_a_button)
    
    def click_to_btn(self) -> None:
        self.button.click()
