import pytest
from dataclasses import dataclass
from typing import Generator
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.webdriver import WebDriver

from pages.email_input_page import EmailInputPage


@dataclass(frozen=True)
class EmailInputPageError:
    ENTER_A_VALID_EMAIL: str = 'Enter a valid email address.'
    REQUIRED_FIELD: str = 'This field is required.'


@pytest.fixture(scope='function')
def page(browser: WebDriver) -> Generator[EmailInputPage, None, None]:
    page = EmailInputPage(browser)
    page.open()
    yield page


@pytest.mark.smoke
def test_email_field_with_valide_email(page: EmailInputPage) -> None:
    email = 'maximdanilov@mail.ru'
    page.fill_and_press_enter(email)
    assert page.check_result_text(email), 'Неправильнон отображение результата'


def test_emaiL_field_min_length_email(page: EmailInputPage) -> None:
    email = 'a@m.ru'
    page.fill_and_press_enter(email)
    assert page.check_result_text(email)


def test_email_field_is_required(page: EmailInputPage) -> None:
    page.email_field.send_keys(Keys.ENTER)
    assert page.validation_message(page.email_field) == 'Заполните это поле.', (
        'Неправильнон отображение результата'
    )


def test_email_field_email_with_digits(page: EmailInputPage) -> None:
    email = 'danilov169056@mail.ru'
    page.fill_and_press_enter(email)
    assert page.check_result_text(email), 'Неправильнон отображение результата'


def test_email_field_only_with_digits(page: EmailInputPage) -> None:
    email = '5768491367@mail.ru'
    page.fill_and_press_enter(email)
    assert page.check_result_text(email), 'Неправильнон отображение результата'


def test_email_field_email_with_underscopes(page: EmailInputPage) -> None:
    email = 'some_email@gmail.com'
    page.fill_and_press_enter(email)
    assert page.check_result_text(email), 'Неправильнон отображение результата'


def test_email_field_email_with_hyphens(page: EmailInputPage) -> None:
    email = 'hello-email@outlook.com'
    page.fill_and_press_enter(email)
    assert page.check_result_text(email), 'Неправильнон отображение результата'


def test_email_field_email_with_point(page: EmailInputPage) -> None:
    email = 'test.rail.mail@mail.ru'
    page.fill_and_press_enter(email)
    assert page.check_result_text(email), 'Неправильнон отображение результата'


def test_email_field_email_with_digits_undrscp_hyphen_point(page: EmailInputPage) -> None:
    email = 'test_c1se34-email.test@gmail.com'
    page.fill_and_press_enter(email)
    assert page.check_result_text(email), 'Неправильнон отображение результата'


@pytest.mark.xfail
def test_email_field_email_too_long(page: EmailInputPage) -> None:
    """
    BUG: На странице не появляется ошибка с сообщением о том, 
    что превышена максимально допустимая длина email-а
    """
    email = f'{'emailchars' * 50}@mail.ru'
    page.fill_and_press_enter(email)
    assert page.check_error_message(EmailInputPageError.ENTER_A_VALID_EMAIL), (
        'Неправильное отображени ошибки'
    )


def test_email_field_out_of_min_length_email(page: EmailInputPage) -> None:
    email = 'i@i.i'
    page.fill_and_press_enter(email)
    assert page.check_error_message(EmailInputPageError.ENTER_A_VALID_EMAIL), (
        'Неправильное отображени ошибки'
    )


def test_email_field_text_instead_of_email(page: EmailInputPage) -> None:
    text = 'this_is_not_email'
    page.fill_and_press_enter(text)
    assert page.check_error_message(EmailInputPageError.ENTER_A_VALID_EMAIL), (
        'Неправильное отображени ошибки'
    )


def test_email_field_point_at_the_begining(page: EmailInputPage) -> None:
    email = '.point_email@gmail.com'
    page.fill_and_press_enter(email)
    assert page.check_error_message(EmailInputPageError.ENTER_A_VALID_EMAIL), (
        'Неправильное отображени ошибки'
    )


def test_email_field_point_at_the_end(page: EmailInputPage) -> None:
    email = 'point_email.@gmail.com'
    page.fill_and_press_enter(email)
    assert page.check_error_message(EmailInputPageError.ENTER_A_VALID_EMAIL), (
        'Неправильное отображени ошибки'
    )

@pytest.mark.xfail
def test_email_field_hyphen_at_the_begining(page: EmailInputPage) -> None:
    """
    BUG: На странице не отображется ошибка с сообщением "Enter a valid email address."
    По стандарту RFC 5322 email адрес не может начинаться или заканчиваться га дефис
    """
    email = '-new_email@mail.com'
    page.fill_and_press_enter(email)
    assert page.check_error_message(EmailInputPageError.ENTER_A_VALID_EMAIL), (
        'Неправильное отображени ошибки'
    )


@pytest.mark.xfail
def test_email_field_hyphen_at_the_end(page: EmailInputPage) -> None:
    """
    BUG: На странице не отображется ошибка с сообщением "Enter a valid email address."
    По стандарту RFC 5322 email адрес не может начинаться или заканчиваться га дефис
    """
    email = 'lololol-@gmail.com'
    page.fill_and_press_enter(email)
    assert page.check_error_message(EmailInputPageError.ENTER_A_VALID_EMAIL), (
        'Неправильное отображени ошибки'
    )


def test_email_field_email_with_space(page: EmailInputPage) -> None:
    email = 'email with_space@mail.ru'
    page.fill_and_press_enter(email)
    assert page.check_error_message(EmailInputPageError.ENTER_A_VALID_EMAIL), (
        'Неправильное отображени ошибки'
    )


def test_email_field_only_with_spaces(page: EmailInputPage) -> None:
    email = '         @gmail.com'
    page.fill_and_press_enter(email)
    assert page.check_error_message(EmailInputPageError.ENTER_A_VALID_EMAIL), (
        'Неправильное отображени ошибки'
    )


@pytest.mark.xfail
def test_email_field_only_with_underscopes(page: EmailInputPage) -> None:
    """
    BUG: На странице не отображается ошибка с сообщением "Enter a valid email address."
    Часть email-а до @ не может состоять только из нижних подчеркиваний
    """
    email = '______________@mail.com'
    page.fill_and_press_enter(email)
    assert page.check_error_message(EmailInputPageError.ENTER_A_VALID_EMAIL), (
        'Неправильное отображени ошибки'
    )


@pytest.mark.xfail
def test_email_field_email_with_special_symbols(page: EmailInputPage) -> None:
    """
    BUG: На странице не отображается ошибка с сообщением "Enter a valid email address."
    """
    email = 'wtf&whats$going#n@mail.ru'
    page.fill_and_press_enter(email)
    assert page.check_error_message(EmailInputPageError.ENTER_A_VALID_EMAIL), (
        'Неправильное отображени ошибки'
    )


def test_email_field_email_on_russian(page: EmailInputPage) -> None:
    email = 'русскоемыло@gmail.com'
    page.fill_and_press_enter(email)
    assert page.check_error_message(EmailInputPageError.ENTER_A_VALID_EMAIL), (
        'Неправильное отображени ошибки'
    )


def test_email_field_only_with_special_symbols(page: EmailInputPage) -> None:
    email = ':%;%*(?:%@gmail.com'
    page.fill_and_press_enter(email)
    assert page.check_error_message(EmailInputPageError.ENTER_A_VALID_EMAIL), (
        'Неправильное отображени ошибки'
    )


def test_email_remove_required_attr_from_input(page: EmailInputPage) -> None:
    page.remove_attribute(page.email_field, 'required')
    page.email_field.send_keys(Keys.ENTER)
    assert page.check_error_message(EmailInputPageError.REQUIRED_FIELD), (
        'Неправильное отображени ошибки'
    )
