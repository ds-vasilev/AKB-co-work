from fixtures.constants import LogMessages
from models.register import RegisterUserModel
import time
import requests



class TestSignInPage:
    # todo подумать, как передать сюда валидный пароль со страницы регистрации. Вариант - возвращать в app,
    #  уточнить про реализацию
    def test_valid_login(self, app, register_user):
        """
        Логин.
        """
        app.login_page.open_login_page()
        app.login_page.entry_data_login(email_data=register_user.email, pass_data=register_user.password_1)
        assert app.login_page.log_status_on_top_right() == LogMessages.SUCCESS


    def test_repeated_login(self, app):
        """
        Повторный логин без логаута.
        """
        pass


    def test_invalid_login_login(self, app):
        """
        Неверный логин.
        """
        pass


    def test_invalid_login_login_zero(self, app):
        """
        Пустой логин.
        """
        pass


    def test_invalid_login_pass(self, app):
        """
        Неверный пароль.
        """
        pass
