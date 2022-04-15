from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage
from models.register import RegisterUserModel


class LoginPage(BasePage):
    LOGIN_BUTTON_ON_HEADER = (By.ID, "login-link")
    EMAIL = (By.ID, "name")
    PASS = (By.ID, "password")
    LOG_BUTTON = (By.ID, "register")
    MESSAGE_LOG_STATUS_TOP_RIGHT = (By.CLASS_NAME, "toast")


    def open_login_page(self):
        """
        open log page
        """
        self.open_page(self.app.url)
        self.click_element(locator=self.LOGIN_BUTTON_ON_HEADER)

    def entry_data_login(self,email_data: str, pass_data: str):
        """
        ввод данных в поля и клик
        """
        self.fill(locator=self.EMAIL, value=email_data)
        self.fill(locator=self.PASS, value=pass_data)
        self.click_element(locator=self.LOG_BUTTON)

    def log_status_on_top_right(self) -> str:
        """информационная всплывашка справа-вверху"""
        element = self.text(locator=self.MESSAGE_LOG_STATUS_TOP_RIGHT)
        return element

    # def click_login_button(self):
    #     """
    #     open log page
    #     """
    #     self.click_element(locator=self.LOGIN_BUTTON_ON_HEADER)
