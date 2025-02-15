import pytest
from typing import Generator
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.ie.webdriver import WebDriver

from pages.checkboxes.checkboxes_page import CheckboxesPage


@pytest.fixture(scope='function')
def page(browser: WebDriver) -> Generator[CheckboxesPage, None, None]:
    page = CheckboxesPage(browser=browser)
    page.open()
    yield page


def test_checkboxes_result_is_displayed_after_select_first_checkbox(
        page: CheckboxesPage
    ) -> None:
    page.js_click(page.one_checkbox)
    page.js_click(page.submit_button)
    assert page.check_result_text('one'), 'Неправильное отображение результата'


def test_checboxes_result_is_displayed_after_select_second_checkbox(
        page: CheckboxesPage
    ) -> None:
    page.js_click(page.two_checkbox)
    page.js_click(page.submit_button)
    assert page.check_result_text('two'), 'Неправильное отображение результата'


def test_checkboxes_result_is_displayed_after_select_third_checkbox(
        page: CheckboxesPage
    ) -> None:
    page.js_click(page.three_checkbox)
    page.js_click(page.submit_button)
    assert page.check_result_text('three'), 'Неправильное отображение результата'


def test_checkboxes_select_two_checkboxes(page: CheckboxesPage) -> None:
    page.js_click(page.one_checkbox)
    page.js_click(page.three_checkbox)
    page.js_click(page.submit_button)
    assert page.check_result_text('one, three'), 'Неправильное отображение результата'


def test_checkboxes_select_all_checkboxes(page: CheckboxesPage) -> None:
    page.js_click(page.one_checkbox)
    page.js_click(page.two_checkbox)
    page.js_click(page.three_checkbox)
    page.js_click(page.submit_button)
    assert page.check_result_text('one, two, three'), (
        'Неправильное отображение результата'
    )


def test_checkboxes_select_first_checkbox_by_label(page: CheckboxesPage) -> None:
    page.js_click(page.one_checkbox_label)
    page.js_click(page.submit_button)
    assert page.check_result_text('one'), 'Неправильное отображение результата'


def test_checkboxes_select_second_checkbox_by_label(page: CheckboxesPage) -> None:
    page.js_click(page.two_checkbox_label)
    page.js_click(page.submit_button)
    assert page.check_result_text('two'), 'Неправильное отображение результата'


def test_checkboxes_select_third_checkbox_by_label(page: CheckboxesPage) -> None:
    page.js_click(page.three_checkbox_label)
    page.js_click(page.submit_button)
    assert page.check_result_text('three'), 'Неправильное отображение результата'


def test_checboxes_no_select_checboxes(page: CheckboxesPage) -> None:
    with pytest.raises(NoSuchElementException):
        page.js_click(page.submit_button)
        assert not page.result_block.is_displayed(), 'Блок с результатом отображается'
