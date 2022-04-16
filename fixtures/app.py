from fixtures.pages.main_page import MainPage
from fixtures.pages.registration_page import RegistrationPage
from fixtures.pages.login_page import LoginPage


class Application:

    def __init__(self, driver, url: str):
        self.driver = driver
        self.url = url
        self.main_page = MainPage(self)
        self.registration_page = RegistrationPage(self)
        self.login_page = LoginPage(self)

    def quit(self):
        self.driver.quit()
