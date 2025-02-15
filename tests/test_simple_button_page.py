import pytest
from typing import Generator
from selenium.webdriver.ie.webdriver import WebDriver

from pages.buttons.simple_button_page import SimpleButtonPage


@pytest.fixture(scope='function')
def page(browser: WebDriver) -> Generator[SimpleButtonPage, None, None]:
    page = SimpleButtonPage(browser=browser)
    page.open()
    yield page


def test_simple_button_result_block_is_displayed(page: SimpleButtonPage) -> None:
    page.js_click(page.simple_button)
    assert page.check_result_text('Submitted'), 'Неправильное отображение результата'
