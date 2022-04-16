import pytest
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from fixtures.app import Application
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
def reg_log_user():
    data = RegisterUserModel.random()
    payload = {"username": data.email, "password": data.password_1}
    r = requests.post("https://stores-tests-api.herokuapp.com/register", data=payload)

    assert r.status_code == 201
    return data
