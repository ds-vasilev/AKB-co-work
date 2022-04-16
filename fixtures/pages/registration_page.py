from selenium.webdriver.common.by import By
from models.register import RegisterUserModel


class RegistrationPage:
    REG_BUTTON_ON_HEADER = (By.ID, "register-link")
    EMAIL = (By.ID, "name")
    PASS_1 = (By.ID, "password1")
    PASS_2 = (By.ID, "password2")
    REG_BUTTON = (By.ID, "register")
    MESSAGE_REG_STATUS_TOP_RIGHT = (By.CLASS_NAME, "toast")
    MESSAGE_REG_STATUS_ERROR_BIG_RED = (By.CLASS_NAME, "card-panel")

    def __init__(self, app):
        self.app = app

    def open_registration_page(self):
        """
        open reg page
        """
        self.app.driver.get(self.app.url)
        self.app.driver.fullscreen_window()  # todo уточнить про реализацию
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

    def reg_status_on_top_right(self) -> str:
        element = self.app.driver.find_element(*self.MESSAGE_REG_STATUS_TOP_RIGHT)
        return element.text

    def _entry_email(self, data: str):
        email = self.app.driver.find_element(*self.EMAIL)
        email.clear()
        email.send_keys(data)

    def _entry_password(self, data: str):
        email = self.app.driver.find_element(*self.PASS_1)
        email.clear()
        email.send_keys(data)

    def _entry_password_repeat(self, data: str):
        email = self.app.driver.find_element(*self.PASS_2)
        email.clear()
        email.send_keys(data)

    def _click_button_register(self):
        reg_button = self.app.driver.find_element(*self.REG_BUTTON)
        reg_button.click()

    def reg_status_big_red_tab(self) -> str:
        element = self.app.driver.find_element(*self.MESSAGE_REG_STATUS_ERROR_BIG_RED)
        return element.text
