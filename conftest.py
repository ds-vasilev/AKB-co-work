import pytest
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from fixtures.app import Application
from fixtures.constants import LogMessages
from models.register import RegisterUserModel


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://berpress.github.io/react-shop/",
        help="store",
    ),


@pytest.fixture
def app(request):
    url = request.config.getoption("--url")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)  # seconds
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


@pytest.fixture
def login_user(app, register_user):
    """
        Фикстура для логина нового пользователя. Реализована не через АПИ в соотв с заданием.
    """
    data = register_user
    app.login_page.open_login_page()
    app.login_page.entry_data_login(email_data=register_user.email, pass_data=register_user.password_1)
    assert app.login_page.log_status_on_top_right() == LogMessages.SUCCESS
    return data
