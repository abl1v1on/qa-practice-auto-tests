from pathlib import Path
from dataclasses import dataclass
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from . import locator


BASE_DIR = Path(__file__).parent.parent


@dataclass(frozen=True)
class BasePageLocator:
    result_block: locator = (By.ID, 'result')
    result_text: locator = (By.ID, 'result-text')
    error_message: locator = (
        By.XPATH, 
        '//span/strong'
    )


class BasePage:
    def __init__(self, browser: WebDriver, timeout: int = 5) -> None:
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self.url = 'https://www.qa-practice.com'
    
    def open(self) -> None:
        self.browser.get(self.url)
    
    def find(
            self, 
            by: str, 
            value: str, 
            many: bool = False
        ) -> WebElement | list[WebElement]:
        if many:
            return self.browser.find_elements(by, value)
        return self.browser.find_element(by, value)

    def remove_attribute(self, element: WebElement, attr: str) -> None:
        self.browser.execute_script(
            f'arguments[0].removeAttribute("{attr}");', 
            element
        )
    
    def validation_message(self, element: WebElement) -> None:
        return self.browser.execute_script(
            'return arguments[0].validationMessage;',
            element
        )
    
    def scroll_to(self, element: WebElement) -> None:
        self.browser.execute_script(
            'arguments[0].scrollIntoView();',
            element
        )
    
    def js_click(self, element: WebElement) -> None:
        self.browser.execute_script(
            'arguments[0].click();',
            element
        )

    def execute_script(self, script_name: str) -> None:
        script = BASE_DIR / 'scripts' / f'{script_name}.js'

        if script.exists():
            self.browser.execute_script(script.read_text())

    def check_result_text(self, text: str) -> bool:
        expected_result = text
        actual_result = self.result_text.text
        return True if expected_result == actual_result else False

    def check_error_message(self, error: str) -> bool:
        expected_error = error 
        actual_error = self.error_message.text
        return True if expected_error == actual_error else False

    """
    NOTE: Базовые элементы, которые есть почти на каждой странице.
    Конкретно в этом примере имеет смысл вынести их в базовый класс,
    чтобы избежать дублирования.
    """
    
    @property
    def result_block(self) -> WebElement:
        return self.find(*BasePageLocator.result_block)

    @property
    def result_text(self) -> WebElement:
        return self.find(*BasePageLocator.result_text)

    @property
    def error_message(self) -> WebElement:
        return self.find(*BasePageLocator.error_message)
