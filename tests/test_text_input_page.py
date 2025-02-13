import pytest
from dataclasses import dataclass
from typing import Generator
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.webdriver import WebDriver

from pages import FieldIsRequiredErrorMixin
from pages.inputs.text_input_page import TextInputPage


@dataclass(frozen=True)
class TextInputPageError(FieldIsRequiredErrorMixin):
    TWO_OR_MORE_CHARS: str = 'Please enter 2 or more characters'
    NO_MORE_25_CHARS: str = 'Please enter no more than 25 characters'
    ENTER_A_VALID_STRING: str = (
        'Enter a valid string consisting of letters, numbers, underscores or hyphens.'
    )


@pytest.fixture(scope='function')
def page(browser: WebDriver) -> Generator[TextInputPage, None, None]:
    page = TextInputPage(browser)
    page.open()
    yield page


@pytest.mark.smoke
def test_text_field_with_valide_text(page: TextInputPage) -> None:
    text = 'photography'
    page.fill_and_press_enter(text)
    assert page.check_result_text(text), 'Неправильное отображение результата'


def test_text_field_min_length_text(page: TextInputPage) -> None:
    text = 'hi'
    page.fill_and_press_enter(text)
    assert page.check_result_text(text), 'Неправильное отображение результата'


def test_text_field_max_length_text(page: TextInputPage) -> None:
    text = 'ig85g_iqa5gpyto284_-gae4g'
    page.fill_and_press_enter(text)
    assert page.check_result_text(text), 'Неправильное отображение результата'


def test_text_field_is_required(page: TextInputPage) -> None:
    page.text_field.send_keys(Keys.ENTER)
    errors = ['Заполните это поле.', 'Please fill out this field.']
    assert page.validation_message(page.text_field) in errors, (
        'Не отображается сообщение от браузера об обязательности поля'
    )


def test_text_field_text_with_digits(page: TextInputPage) -> None:
    text = 'numbers1234'
    page.fill_and_press_enter(text)
    assert page.check_result_text(text), 'Неправильное отображение результата'


def test_text_field_text_with_underscopes(page: TextInputPage) -> None:
    text = 'text_with_uscope'
    page.fill_and_press_enter(text)
    assert page.check_result_text(text), 'Неправильное отображение результата'


def test_text_field_text_with_spaces_at_beginning_and_end(page: TextInputPage) -> None:
    text = '   text   '
    page.fill_and_press_enter(text)
    assert page.check_result_text(text.strip()), 'Неправильное отображение результата'


def test_text_field_only_with_digits(page: TextInputPage) -> None:
    text = '6742357901'
    page.fill_and_press_enter(text)
    assert page.check_result_text(text), 'Неправильное отображение результата'


def test_text_field_text_with_hyphens(page: TextInputPage) -> None:
    text = 'text-with-hyphens'
    page.fill_and_press_enter(text)
    assert page.check_result_text(text), 'Неправильное отображение результата'


def test_text_field_only_with_underscopes(page: TextInputPage) -> None:
    text = '__________'
    page.fill_and_press_enter(text)
    assert page.check_result_text(text), 'Неправильное отображение результата'


def test_text_field_only_with_hyphens(page: TextInputPage) -> None:
    text = '--------------'
    page.fill_and_press_enter(text)
    assert page.check_result_text(text), 'Неправильное отображение результата'


def test_text_field_text_with_digits_underscopes_hyphens(page: TextInputPage) -> None:
    text = 'text_w_a11wd-symbls'
    page.fill_and_press_enter(text)
    assert page.check_result_text(text), 'Неправильное отображение результата'


def test_text_field_out_of_min_length_text(page: TextInputPage) -> None:
    text = 'h'
    page.fill_and_press_enter(text)
    assert page.check_error_message(TextInputPageError.TWO_OR_MORE_CHARS), (
        'Неправильное отображение ошибки'
    )


def test_text_field_out_of_max_length_text(page: TextInputPage) -> None:
    text = 'jg85_ag95-_94--4gopq35896_'
    page.fill_and_press_enter(text)
    assert page.check_error_message(TextInputPageError.NO_MORE_25_CHARS), (
        'Неправильное отображение ошибки'
    )


def test_text_field_text_contains_spaces(page: TextInputPage) -> None:
    text = 'hello world space'
    page.fill_and_press_enter(text)
    assert page.check_error_message(TextInputPageError.ENTER_A_VALID_STRING), (
        'Неправильное отображение ошибки'
    )


def test_text_field_only_with_spaces(page: TextInputPage) -> None:
    text = '                '
    page.fill_and_press_enter(text)
    assert page.check_error_message(TextInputPageError.REQUIRED_FIELD), (
        'Неправильное отображение ошибки'
    )


def test_text_field_text_with_special_symbols(page: TextInputPage) -> None:
    text = 'special@symb#ls!'
    page.fill_and_press_enter(text)
    assert page.check_error_message(TextInputPageError.ENTER_A_VALID_STRING), (
        'Неправильное отображение ошибки'
    )


def test_text_field_text_on_russian(page: TextInputPage) -> None:
    text = 'русский_текст'
    page.fill_and_press_enter(text)
    assert page.check_error_message(TextInputPageError.ENTER_A_VALID_STRING), (
        'Неправильное отображение ошибки'
    )


def test_text_field_only_with_special_symbols(page: TextInputPage) -> None:
    text = '*?;:№?%*%'
    page.fill_and_press_enter(text)
    assert page.check_error_message(TextInputPageError.ENTER_A_VALID_STRING), (
        'Неправильное отображение ошибки'
    )


def test_text_field_remove_required_attr_from_input(page: TextInputPage) -> None:
    page.remove_attribute(page.text_field, 'required')
    page.text_field.send_keys(Keys.ENTER)
    assert page.check_error_message(TextInputPageError.REQUIRED_FIELD), (
        'Неправильное отображение ошибки'
    )
