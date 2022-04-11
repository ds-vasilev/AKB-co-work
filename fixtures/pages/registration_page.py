from selenium.webdriver.common.by import By
from models.register import RegisterUserModel


class RegistrationPage:
    REG_BUTTON_ON_HEADER = (By.ID, "register-link")
    EMAIL = (By.ID, "name")
    PASS_1 = (By.ID, "password1")
    PASS_2 = (By.ID, "password2")
    REG_BUTTON = (By.ID, "register")

    def __init__(self, app):
        self.app = app

    def open_registration_page(self):
        """
        open reg page
        """
        self.app.driver.get(self.app.url)
        self.app.driver.fullscreen_window()   # todo уточнить про реализацию
        # self.app.driver.add_argument('--start-maximized')  # не сработало
        reg_button = self.app.driver.find_element(*self.REG_BUTTON_ON_HEADER)
        reg_button.click()

    def entry_data_registration(self, data: RegisterUserModel):
        """
        data entry in fields
        """
        self._entry_email(data.email)
        self._entry_password(data.password_1)
        self._entry_password_repeat(data.password_2)
        self._click_button_register()
        # email_field = self.app.driver.find_element(*self.EMAIL)
        # email_field.send_keys(f"user{random.randint(0, 1000)}@test.com")  # todo заглушка
        # pass_1_field = self.app.driver.find_element(*self.PASS_1)
        # pass_1_field.send_keys("1234567")
        # pass_2_field = self.app.driver.find_element(*self.PASS_2)
        # pass_2_field.send_keys("1234567")
        #
        # reg_button = self.app.driver.find_element(*self.REG_BUTTON)
        # reg_button.click()

    # def error_text(self) -> str:
    #     element = self.app.driver.find_element(*self.ERROR_TEXT)
    #     return element.text

    def _entry_email(self, data: str):
        email = self.app.driver.find_element(*self.EMAIL)
        email.send_keys(data)

    def _entry_password(self, data: str):
        email = self.app.driver.find_element(*self.PASS_1)
        email.send_keys(data)

    def _entry_password_repeat(self, data: str):
        email = self.app.driver.find_element(*self.PASS_2)
        email.send_keys(data)

    def _click_button_register(self):
        reg_button = self.app.driver.find_element(*self.REG_BUTTON)
        reg_button.click()

