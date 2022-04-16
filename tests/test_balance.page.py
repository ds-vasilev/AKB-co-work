import pytest
from fixtures.constants import LogMessages
from fixtures.constants_test_cases import TestCases
import time
from models.balance import BalanceUserModel


class TestBalancePage:

    def test_valid_entry_data_balance(self, app, register_user):
        """
        Add balance
        """
        app.login_page.open_login_page()
        app.login_page.entry_data_login(email_data=register_user.email, pass_data=register_user.password_1)
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        app.balance_page.entry_data_balance(data=data)
        # assert app.login_page.log_status_on_top_right() == LogMessages.SUCCESS



    # def test_name_lastame(self, app):  # todo ластнейма нет
    #     """имя"""
    #     pass
    #
    # def test_name_lastame_null(self, app):
    #     """имя нулевое"""
    #     pass
    #
    # def test_cart_number_16(self, app):
    #     """номер карты цифр 16"""
    #     pass
    #
    # def test_cart_number_16_null(self, app):
    #     """номер карты цифр 16 нулевое"""
    #     pass
    #
    # def test_cart_number_16_invalid_more(self, app):
    #     """номер карты цифр <16"""
    #     pass
    #
    # def test_cart_number_16_invalid_less(self, app):
    #     """номер карты цифр >16"""
    #     pass
    #
    # def test_cart_number_16_invalid_str(self, app):
    #     """номер карты буквы"""
    #     pass
    #
    # def test_date(self, app):
    #     """Дата"""  # todo нет контроля формы даты
    #     pass
    #
    # def test_date_null(self, app):
    #     """Дата нулевая"""
    #     pass
    #
    # def test_summ(self, app):  # todo нет контроля формы, проходят и букы
    #     """наличие суммы в поле суммы"""
    #     pass
    #
    # def test_summ_null(self, app):
    #     """пустое поле суммы"""
    #     pass
    #
    # def test_agree_rules(self, app):
    #     """галка в согласии"""
    #     pass
    #
    # def test_agree_rules_null(self, app):
    #     """без галки в согласии"""
    #     pass
