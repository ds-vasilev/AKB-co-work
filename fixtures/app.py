from fixtures.pages.balance_page import BalancePage
from fixtures.pages.login_page import LoginPage
from fixtures.pages.registration_page import RegistrationPage


class Application:

    def __init__(self, driver, url: str):
        self.driver = driver
        self.url = url
        self.registration_page = RegistrationPage(self)
        self.login_page = LoginPage(self)
        self.balance_page = BalancePage(self)

    def quit(self):
        self.driver.quit()
