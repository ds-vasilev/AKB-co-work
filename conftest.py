import logging
import pytest
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from fixtures.app import Application
from selenium.webdriver.chrome.options import Options
from models.register import RegisterUserModel

logger = logging.getLogger("rss")

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://berpress.github.io/react-shop/",
        help="store",
    ),
    parser.addoption("--headless", action="store_true", help="Headless mode"),


@pytest.fixture
def app(request):
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    chrome_options = Options()
    if headless:
        chrome_options.headless = True
    else:
        chrome_options.headless = False
    logger.info(f"Start app on {url}")
    driver = webdriver.Chrome(ChromeDriverManager().install(),
                              options=chrome_options)
    app = Application(driver, url)
    yield app
    app.quit()


@pytest.fixture
def register_user():
    data = RegisterUserModel.random()
    payload = {"username": data.email, "password": data.password_1}
    r = requests.post("https://stores-tests-api.herokuapp.com/register", data=payload)
    assert r.status_code == 201
    return data
