import pytest
from dataclasses import dataclass
from typing import Generator
from selenium.webdriver.ie.webdriver import WebDriver

from pages import FieldIsRequiredErrorMixin
from pages.textarea.textarea_page import TextareaPage


@dataclass(frozen=True)
class TextareaPageError(FieldIsRequiredErrorMixin):
    TEXT_IS_TOO_LONG: str = 'Text is too long.'


@pytest.fixture(scope='function')
def page(browser: WebDriver) -> Generator[TextareaPage, None, None]:
    page = TextareaPage(browser=browser)
    page.open()
    yield page


def test_textarea_with_valid_value(page: TextareaPage) -> None:
    text = 'Some text for testing this textarea field'
    page.fill_textarea(text)
    page.submit()
    assert page.check_result_text(text), 'Неправильное отображение результата'


def test_textarea_min_length_text(page: TextareaPage) -> None:
    text = 'h'
    page.fill_textarea(text)
    page.submit()
    assert page.check_result_text(text), 'Неправильное отображение результата'


def test_textarea_text_with_russian_chars(page: TextareaPage) -> None:
    text = 'русский текст без смысла'
    page.fill_textarea(text)
    page.submit()
    assert page.check_result_text(text), 'Неправильное отображение результата'


def test_textarea_text_with_special_chars(page: TextareaPage) -> None:
    text = 'i am not @ robot #'
    page.fill_textarea(text)
    page.submit()
    assert page.check_result_text(text), 'Неправильное отображение результата'


def test_textarea_text_only_with_digits(page: TextareaPage) -> None:
    text = '45678765432123456'
    page.fill_textarea(text)
    page.submit()
    assert page.check_result_text(text), 'Неправильное отображение результата'


def test_textarea_split_spaces_at_beginning_and_at_the_end(page: TextareaPage) -> None:
    text = '    do you strip spaces    '
    page.fill_textarea(text)
    page.submit()
    assert page.check_result_text(text.strip()), 'Неправильное отображение результата'


@pytest.mark.xfail(reason='need to fix bug')
def test_textarea_too_long_text(page: TextareaPage) -> None:
    text = 'texttext' * 200
    page.fill_textarea(text)
    page.submit()
    assert page.check_error_message(TextareaPageError.TEXT_IS_TOO_LONG), (
        'Неправильное отображение ошибки'
    )


def test_textarea_is_required(page: TextareaPage) -> None:
    page.submit()
    errors = ['Заполните это поле.', 'Please fill out this field.']
    assert page.validation_message(page.textarea) in errors, (
        'Не отображается ошибка от браузера'
    )


def test_textarea_text_only_with_spaces(page: TextareaPage) -> None:
    text = '             '
    page.fill_textarea(text)
    page.submit()
    assert page.check_error_message(TextareaPageError.REQUIRED_FIELD), (
        'Неправильное отображение ошибки'
    )


def test_textarea_remove_required_attr(page: TextareaPage) -> None:
    page.remove_attribute(page.textarea, 'required')
    page.submit()
    assert page.check_error_message(TextareaPageError.REQUIRED_FIELD), (
        'Неправильное отображение ошибки'
    )
