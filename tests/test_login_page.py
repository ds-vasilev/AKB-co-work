import pytest
from fixtures.constants import LogMessages
from fixtures.constants_test_cases import TestCases
import time


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

    def test_repeated_login(self, app, register_user):
        """
        Повторный логин без логаута.
        """
        app.login_page.open_login_page()
        app.login_page.entry_data_login(email_data=register_user.email, pass_data=register_user.password_1)
        time.sleep(1)
        app.login_page.entry_data_login(email_data=register_user.email, pass_data=register_user.password_1)
        assert app.login_page.log_status_on_top_right() == LogMessages.ALREADY_LOGIN

    @pytest.mark.parametrize("inval_email, inval_pass", (TestCases.INVALID_DATA_FOR_LOG_PAGE))
    def test_invalid_login_login(self, app, inval_email, inval_pass):
        """
        Неверные и пустые логины-пароли.
        """
        app.login_page.open_login_page()
        app.login_page.entry_data_login(email_data=inval_email, pass_data=inval_pass)
        assert app.login_page.log_status_on_top_right() == LogMessages.INVALID_CREDENTAILS
