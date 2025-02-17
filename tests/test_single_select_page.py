import pytest
import time
from dataclasses import dataclass
from typing import Generator
from selenium.webdriver.ie.webdriver import WebDriver

from pages import FieldIsRequiredErrorMixin
from pages.select.single_select_page import SingleSelectPage


@dataclass(frozen=True)
class SingleSelectPageError(FieldIsRequiredErrorMixin):
    SELECT_VALID_CHOISE: str = (
        'Select a valid choice. 6 is not one of the available choices.'
    )


@pytest.fixture(scope='function')
def page(browser: WebDriver) -> Generator[SingleSelectPage, None, None]:
    page = SingleSelectPage(browser)
    page.open()
    yield page


langs = [
    ('1', 'Python'),
    ('2', 'Ruby'),
    ('3', 'JavaScript'),
    ('4', 'Java'),
    ('5', 'C#'),
]


@pytest.mark.parametrize('lang', langs)
def test_single_select_choose_valid_language(
        page: SingleSelectPage, 
        lang: tuple[str, str]
    ) -> None:
    page.select_lang_by_value(lang[0])
    page.submit()
    assert page.check_result_text(lang[1]), 'Неправильное отображение результата'


def test_single_select_if_required_field(page: SingleSelectPage) -> None:
    page.submit()
    errors = ['Выберите один из пунктов списка.']
    assert page.validation_message(page.choose_lang_select) in errors, (
        'Отсутствует сообщение об обязательности поля от браузера'
    )


def test_single_select_add_other_lang(page: SingleSelectPage) -> None:
    page.execute_script('add_select_option')
    page.select_lang_by_value('6')
    page.submit()
    assert page.check_error_message(SingleSelectPageError.SELECT_VALID_CHOISE), (
        'Неправильное отображение ошибки'
    )


def test_single_select_remove_required_attr(page: SingleSelectPage) -> None:
    page.remove_attribute(page.choose_lang_select, 'required')
    page.submit()
    assert page.check_error_message(SingleSelectPageError.REQUIRED_FIELD), (
        'Неправильное отображение ошибки'
    )
