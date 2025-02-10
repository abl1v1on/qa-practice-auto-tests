import time
import pytest
from typing import Generator
from selenium.webdriver.ie.webdriver import WebDriver

from pages.text_input_page import TextInputPage


@pytest.fixture(scope='function')
def page(browser: WebDriver) -> Generator[TextInputPage, None, None]:
    page = TextInputPage(browser)
    page.open()
    yield page


def test_open_text_page(page: TextInputPage) -> None:
    page.text_field.send_keys('some text')
    time.sleep(100)
