from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


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
