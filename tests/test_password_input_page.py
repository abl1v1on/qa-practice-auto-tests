import pytest
from dataclasses import dataclass
from typing import Generator
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.webdriver import WebDriver

from pages import FieldIsRequiredErrorMixin
from pages.inputs.password_input_page import PasswordInputPage


@dataclass(frozen=True)
class PasswordInputPageError(FieldIsRequiredErrorMixin):
    LOW_COMPLEXITY: str = 'Low password complexity'
    PASSWORD_TOO_LONG: str = 'Password is too long.'

"""
BUG: Неинформативное сообщение об ошибке при попытке ввода пароля с длинной меньше допустимой 
BUG:
"""

@pytest.fixture(scope='function')
def page(browser: WebDriver) -> Generator[PasswordInputPage, None, None]:
    page = PasswordInputPage(browser)
    page.open()
    yield page


@pytest.mark.smoke
def test_password_field_with_valide_password(page: PasswordInputPage) -> None:
    password = 'fit0gAe#t_h'
    page.fill_and_press_enter(password)
    assert page.check_result_text(password), 'Неправильное отображение результата'


def test_password_field_min_length_password(page: PasswordInputPage) -> None:
    password = '0g#1qpOt'
    page.fill_and_press_enter(password)
    assert page.check_result_text(password), 'Неправильное отображение результата'


@pytest.mark.xfail
def test_password_field_password_is_too_long(page: PasswordInputPage) -> None:
    """
    BUG: Не отображается сообщение об 
    ошибке при вводе очень длинного пароля
    """
    password = 'oI0*#g' * 100
    page.fill_and_press_enter(password)
    assert page.check_error_message(PasswordInputPageError.PASSWORD_TOO_LONG), (
        'Нерпавльное отображение ошибки'
    )


def test_password_field_is_required(page: PasswordInputPage) -> None:
    page.password_field.send_keys(Keys.ENTER)
    errors = ['Please fill out this field.', 'Заполните это поле.']
    assert page.validation_message(page.password_field) in errors, (
        'Бразуер не отображает стандартную ошибку про обязательность поля'
    )


def test_password_field_out_of_min_length_password(page: PasswordInputPage) -> None:
    """
    BUG: Неинформативное сообщение об ошибке 
    при попытке ввода пароля с длинной меньше допустимой
    """
    password = 'tiY0p@e'
    page.fill_and_press_enter(password)
    assert page.check_error_message(PasswordInputPageError.LOW_COMPLEXITY), (
        'Нерпавльное отображение ошибки'
    )


def test_password_field_only_with_lowercase_chars(page: PasswordInputPage) -> None:
    """
    BUG: Неинформативное сообщение об ошибке. 
    Указать какие именно символы должны быть в пароле
    """
    password = 'kgpiaejgpieahg'
    page.fill_and_press_enter(password)
    assert page.check_error_message(PasswordInputPageError.LOW_COMPLEXITY), (
        'Нерпавльное отображение ошибки'
    )


def test_password_field_only_with_uppercase_chars(page: PasswordInputPage) -> None:
    """
    BUG: Неинформативное сообщение об ошибке. 
    Указать какие именно символы должны быть в пароле
    """
    password = 'OGEAPIHGPEAGTLS'
    page.fill_and_press_enter(password)
    assert page.check_error_message(PasswordInputPageError.LOW_COMPLEXITY), (
        'Нерпавльное отображение ошибки'
    )


def test_password_field_only_with_digits(page: PasswordInputPage) -> None:
    """
    BUG: Неинформативное сообщение об ошибке. 
    Указать какие именно символы должны быть в пароле
    """
    password = '6780987324686'
    page.fill_and_press_enter(password)
    assert page.check_error_message(PasswordInputPageError.LOW_COMPLEXITY), (
        'Нерпавльное отображение ошибки'
    )


def test_password_field_only_with_special_symbols(page: PasswordInputPage) -> None:
    """
    BUG: Неинформативное сообщение об ошибке. 
    Указать какие именно символы должны быть в пароле
    """
    password = '*?:№%;?"*!);(*;?'
    page.fill_and_press_enter(password)
    assert page.check_error_message(PasswordInputPageError.LOW_COMPLEXITY), (
        'Нерпавльное отображение ошибки'
    )


@pytest.mark.xfail
def test_password_field_password_with_space(page: PasswordInputPage) -> None:
    """
    BUG: Система пропускает пароль содержащий пробел
    """
    password = 'gaMVj&@oth a0@EhAEg"'
    page.fill_and_press_enter(password)
    assert page.check_error_message(PasswordInputPageError.LOW_COMPLEXITY), (
        'Нерпавльное отображение ошибки'
    )


def test_password_field_only_with_spaces(page: PasswordInputPage) -> None:
    password = '            '
    page.fill_and_press_enter(password)
    assert page.check_error_message(PasswordInputPageError.REQUIRED_FIELD), (
        'Нерпавльное отображение ошибки'
    )


def test_password_field_password_with_russian_chars(page: PasswordInputPage) -> None:
    """
    BUG: Неинформативное сообщение об ошибке. 
    Указать какие именно символы должны быть в пароле
    """
    password = 'пгкЫПщпгы13п4ы(*3фпШр'
    page.fill_and_press_enter(password)
    assert page.check_error_message(PasswordInputPageError.LOW_COMPLEXITY), (
        'Нерпавльное отображение ошибки'
    )


def test_password_field_remove_required_attr_from_input(page: PasswordInputPage) -> None:
    page.remove_attribute(page.password_field, 'required')
    page.password_field.send_keys(Keys.ENTER)
    assert page.check_error_message(PasswordInputPageError.REQUIRED_FIELD), (
        'Неправильное отображение ошибки'
    )
