import pytest
from typing import Generator
from selenium.webdriver.ie.webdriver import WebDriver

from pages.buttons.simple_button_page import SimpleButtonPage


@pytest.fixture(scope='function')
def page(browser: WebDriver) -> Generator[SimpleButtonPage, None, None]:
    page = SimpleButtonPage(browser=browser)
    page.open()
    yield page


@pytest.mark.xfail(reason='Selenium не нажимает на кнопки в headless моде')
def test_simple_button_result_block_is_displayed(page: SimpleButtonPage) -> None:
    page.click_to_btn()
    assert page.check_result_text('Submitted'), 'Неправильное отображение результата'
