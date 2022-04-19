import logging
import pytest
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from fixtures.app import Application
from fixtures.constants import LogMessages
from models.register import RegisterUserModel
from selenium.webdriver.chrome.options import Options
from models.balance import BalanceUserModel
import time

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
    """
    Фикстура для регистрации нового пользователя.
    """
    data = RegisterUserModel.random()
    payload = {"username": data.email, "password": data.password_1}
    r = requests.post("https://stores-tests-api.herokuapp.com/register", data=payload)
    assert r.status_code == 201
    print(data.email, data.password_1)
    return data


@pytest.fixture
def login_user(app, register_user):
    """
    Фикстура для логина нового пользователя. Реализована не через АПИ в соотв с заданием.
    """
    app.login_page.open_login_page()
    app.login_page.entry_data_login(email_data=register_user.email, pass_data=register_user.password_1)
    assert app.login_page.log_status_on_top_right() == LogMessages.SUCCESS


@pytest.fixture
def balance_user(app, login_user):
    """
    Фикстура для создания нового пользователя, регистрации, доб. баланса.
    Реализована не через АПИ в соотв с заданием.
    """
    app.balance_page.open_balance_page()
    data = BalanceUserModel.random()
    data.name = "Jonathan Fox"  # захардкожено для стабильности
    data.card = "5185122551503962"
    data.card_data = "12/12"
    data.cash = "5000"
    app.balance_page.entry_data_balance(name=data.name, card=data.card,
                                        date_card=data.card_data, cash=data.cash)
    print(data.name, data.card, data.card_data, data.cash)
