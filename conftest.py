import pytest
from typing import Generator
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ie.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from utils import enable_proxy, disable_proxy


@pytest.fixture(scope='session', autouse=True)
def proxy() -> Generator:
    disable_proxy()
    yield
    enable_proxy()


@pytest.fixture(scope='session')
def options() -> Generator[Options, None, None]:
    options = Options()
    yield options


@pytest.fixture(scope='session')
def service() -> Generator[Service, None, None]:
    service = Service(ChromeDriverManager().install())
    yield service


@pytest.fixture(scope='function')
def browser(options: Options, service: Service) -> Generator[WebDriver, None, None]:
    chrome_browser = Chrome(options=options, service=service)
    yield chrome_browser
    chrome_browser.quit()
