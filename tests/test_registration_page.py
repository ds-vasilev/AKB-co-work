import pytest
import time
from fixtures.constants import RegMessages
from models.register import RegisterUserModel
from fixtures.constants_test_cases import TestCases
#НУЖНЫ ПРОВЕРКИ ИНТЕРФЕЙСА


class TestRegistrationPage:
    def test_valid_register(self, app):
        """
        Тест на успешную регистрацию.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.reg_status_on_top_right() == RegMessages.SUCCESS

    @pytest.mark.parametrize("invalid_email", (TestCases.INVALID_EMAILS_LIST_FOR_REG))
    def test_invalid_email(self, app, invalid_email):
        """
        Тесты на невалидный эмейл.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.email = invalid_email
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.reg_status_big_red_tab() == RegMessages.INVALID_EMAIL[0]\
               + str(data.email[0]) + RegMessages.INVALID_EMAIL[1]

    def test_different_passwords(self, app):
        """
        Тест несовпадение паролей.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.password_2 = "drugoypass"
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.reg_status_big_red_tab() == RegMessages.INVALID_SECOND_PASS

    def test_short_passwords(self, app):
        """
        Тест на слишком короткий пароль.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.password_1 = "short"
        data.password_2 = "short"
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.reg_status_big_red_tab() == RegMessages.INVALID_SHORT_PASS

    def test_base_drop_404(self, app):
        """
        Тест вылетает "Error, check network!".   TODO РЕАЛИЗОВАТЬ НОРМАЛЬНЫЙ НА ДВОЙНОЙ ВВОД!!!!!!!!!!!!!11111
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.email  = "112@111.ru"
        data.password_1  = "111@111.ru"
        data.password_2  = "111@111.ru"
        app.registration_page.entry_data_registration(data=data)
        time.sleep(3)
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.reg_status_on_top_right() == RegMessages.ERROR_CHECK_NETWORK
