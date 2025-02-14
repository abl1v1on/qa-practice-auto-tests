import pytest
from typing import Generator
from selenium.webdriver.ie.webdriver import WebDriver

from pages.buttons.like_a_button_page import LikeAButtonPage


@pytest.fixture(scope='function')
def page(browser: WebDriver) -> Generator[LikeAButtonPage, None, None]:
    page = LikeAButtonPage(browser)
    page.open()
    yield page


def test_like_a_button_result_block_is_displayed(page: LikeAButtonPage) -> None:
    page.click_to_btn()
    assert page.check_result_text('Submitted'), 'Неправильное отображение результата'
