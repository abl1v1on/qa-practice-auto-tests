import pytest
from typing import Generator
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.ie.webdriver import WebDriver

from pages.buttons.disabled_button_page import DisabledButtonPage


@pytest.fixture(scope='function')
def page(browser: WebDriver) -> Generator[DisabledButtonPage, None, None]:
    page = DisabledButtonPage(browser)
    page.open()
    yield page


@pytest.mark.xfail(reason='Selenium не нажимает на кнопки в headless моде')
def test_disabled_button_is_unclickable_if_state_is_disabled(
        page: DisabledButtonPage
    ) -> None:
    with pytest.raises(ElementClickInterceptedException):
        page.select_state('disabled')
        page.click_to_btn()


@pytest.mark.xfail(reason='Selenium не нажимает на кнопки в headless моде')
def test_disabled_button_is_clickable_if_state_is_enabled(
        page: DisabledButtonPage
    ) -> None:
    page.select_state('enabled')
    page.click_to_btn()
    assert page.check_result_text('Submitted'), 'Неправильное отображение результата'


@pytest.mark.xfail(reason='Selenium не нажимает на кнопки в headless моде')
def test_disabled_button_add_other_state_and_choose_it(page: DisabledButtonPage) -> None:
    page.execute_script('add_new_state')
    page.select_state('new-state')
    page.click_to_btn()
    assert page.check_error_message(
        'Select a valid choice. new-state is not one of the available choices.'
    ), 'Неправильное отображение ошибки'
