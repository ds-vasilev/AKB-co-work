from fixtures.pages.main_page import MainPage
from fixtures.pages.registration_page import RegistrationPage


class Application:

    def __init__(self, driver, url: str):
        self.driver = driver
        self.url = url
        self.main_page = MainPage(self)
        self.registration_page = RegistrationPage(self)

    def quit(self):
        self.driver.quit()
