from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage
from models.register import RegisterUserModel


class RegistrationPage(BasePage):
    REG_BUTTON_ON_HEADER = (By.ID, "register-link")
    EMAIL = (By.ID, "name")
    PASS_1 = (By.ID, "password1")
    PASS_2 = (By.ID, "password2")
    REG_BUTTON = (By.ID, "register")
    MESSAGE_REG_STATUS_TOP_RIGHT = (By.CLASS_NAME, "toast")
    MESSAGE_REG_STATUS_ERROR_BIG_RED = (By.CLASS_NAME, "card-panel")
    REG_INTERFACE_IMAGE = (By.CLASS_NAME, "image-login")
    REG_INTERFACE_REG_NEW_USER = (By.CSS_SELECTOR, "h4")
    # REG_INTERFACE_EMAIL = (By.CLASS_NAME, "image-login")
    # REG_INTERFACE_PASS_1 = (By.CLASS_NAME, "image-login")
    # REG_INTERFACE_PASS_2 = (By.CLASS_NAME, "image-login")

    def header_verifiers(self):   # Todo будет вынесено в отдельную страницу после окончательно обсуждения внутри команды
        pass

    def footer_verifiers(self):  # Todo будет вынесено в отдельную страницу после окончательно обсуждения внутри команды
        pass

    def reg_interface_image(self):
        element = self.app.driver.find_element(*self.REG_INTERFACE_IMAGE)
        element = self.app.driver.find_element(*self.REG_INTERFACE_REG_NEW_USER)

    def open_registration_page(self):
        """
        open reg page
        """
        self.open_page(self.app.url)
        self.click_element(locator=self.REG_BUTTON_ON_HEADER)


    def entry_data_registration(self, data: RegisterUserModel):
        """
        data entry in fields
        """
        self._entry_email(data.email)
        self._entry_password(data.password_1)
        self._entry_password_repeat(data.password_2)
        self._click_button_register()

    def reg_status_on_top_right(self) -> str:
        """информационная всплывашка справа-вверху"""
        element = self.text(locator=self.MESSAGE_REG_STATUS_TOP_RIGHT)
        return element

    def _entry_email(self, data: str):
        self.fill(locator=self.EMAIL, value=data)

    def _entry_password(self, data: str):
        self.fill(locator=self.PASS_1, value=data)

    def _entry_password_repeat(self, data: str):
        self.fill(locator=self.PASS_2, value=data)

    def _click_button_register(self):
        """
        Клик.
        """
        self.click_element(locator=self.REG_BUTTON)

    def reg_status_big_red_tab(self) -> str:
        """
        алертная всплывашка снизу на невалидные данные.
        """
        element = self.text(locator=self.MESSAGE_REG_STATUS_ERROR_BIG_RED)
        return element
