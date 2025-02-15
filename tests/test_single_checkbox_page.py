import pytest
from typing import Generator
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from pages.checkboxes.single_checkbox_page import SingleCheckboxPage


@pytest.fixture(scope='function')
def page(browser: WebDriver) -> Generator[SingleCheckboxPage, None, None]:
    page = SingleCheckboxPage(browser=browser)
    page.open()
    yield page


"""
BUG: Selenium can't click to button in headless mod
"""

def test_single_checkbox_result_is_displayed_after_select_checkbox(
        page: SingleCheckboxPage
    ) -> None:
    page.js_click(page.single_checkbox)
    page.js_click(page.submit_button)
    assert page.check_result_text('select me or not'), (
        'Неправильное отображение результата'
    )


def test_single_checkbox_select_checkbox_by_label(page: SingleCheckboxPage) -> None:
    page.js_click(page.single_checkbox_label)
    page.js_click(page.submit_button)
    assert page.check_result_text('select me or not'), (
        'Неправильное отображение результата'
    )


def test_single_checkbox_no_select_checkbox(page: SingleCheckboxPage) -> None:
    with pytest.raises(NoSuchElementException):
        page.js_click(page.submit_button)
        assert not page.result_block.is_displayed(), 'Блок с результатом отображается'
