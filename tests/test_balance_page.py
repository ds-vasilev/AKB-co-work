from fixtures.constants import BalMessages
from fixtures.constants_test_cases import TestCases
from models.balance import BalanceUserModel
import pytest


# доделать при вводе в поля буквенных символов Erorr! Please check network!
# разнести ерроры в файл
# баг при введении 16 символов в поле номер карты

class TestSignInPage:
    @pytest.mark.xfail()
    def test_valid_login(self, app, login_user):
        """
        Валидный тест. Внесение денег на карту
        """
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        app.balance_page.entry_data_balance(name=data.name, card=data.card, date_card=data.card_data, cash=data.cash)
        assert app.balance_page.log_status_on_top_right() == f"All good, you added {data.cash} RUB to your account"

    @pytest.mark.xfail()
    @pytest.mark.parametrize("invalid_card_number", TestCases.INVALID_DATA_FOR_BALANCE_PAGE_CARD_NUM)
    def test_invalid_card_number(self, app, login_user, invalid_card_number):
        """
        Проверка ввода невалидных значений в поле номер карты
        """
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        app.balance_page.entry_data_balance(name=data.name, card=invalid_card_number, date_card=data.card_data,
                                            cash=data.cash)
        assert app.balance_page.log_status_invalid() == "Check card number! It must be 16 symbols and not empty!"

    @pytest.mark.xfail()
    @pytest.mark.parametrize("invalid_card_number", TestCases.INVALID_DATA_FOR_BALANCE_PAGE_CARD_NUM_WORD)
    def test_invalid_card_number_input_word(self, app, login_user, invalid_card_number):
        """
        Проверка ввода невалидных значений в поле номер карты
        """
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        app.balance_page.entry_data_balance(name=data.name, card=invalid_card_number, date_card=data.card_data,
                                            cash=data.cash)
        assert app.balance_page.log_status_invalid_input_word() == "Erorr, check network!"

    @pytest.mark.parametrize("invalid_card_date", TestCases.INVALID_DATA_FOR_BALANCE_PAGE_CARD_DATE)
    def test_invalid_card_date(self, app, login_user, invalid_card_date):
        """
        Пустое значение поля ввода дота карты
        """
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        app.balance_page.entry_data_balance(name=data.name, card=data.card, date_card=invalid_card_date,
                                            cash=data.cash)
        assert app.balance_page.log_status_invalid() == "Check card date! It must be not empty!"

    @pytest.mark.xfail()
    @pytest.mark.parametrize("invalid_card_date", TestCases.INVALID_DATA_FOR_BALANCE_PAGE_CARD_DATE_WORD)
    def test_invalid_card_date_input_word(self, app, login_user, invalid_card_date):
        """
        Проверка ввода невалидных значений в поле номер карты
        """
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        app.balance_page.entry_data_balance(name=data.name, card=data.card, date_card=invalid_card_date,
                                            cash=data.cash)
        assert app.balance_page.log_status_invalid_input_word() == "Erorr, check network!"

    @pytest.mark.parametrize("invalid_card_user", TestCases.INVALID_DATA_FOR_BALANCE_PAGE_CARD_USER)
    def test_invalid_card_date(self, app, login_user, invalid_card_user):
        """
        Пустое значение поля ввода имени пользователя
        """
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        app.balance_page.entry_data_balance(name=invalid_card_user, card=data.card, date_card=data.card_data,
                                            cash=data.cash)
        assert app.balance_page.log_status_invalid() == "Check user name and last name! It must be not empty!"

    @pytest.mark.parametrize("invalid_card_cash", TestCases.INVALID_DATA_FOR_BALANCE_PAGE_CARD_USER)
    def test_invalid_card_cash(self, app, login_user, invalid_card_cash):
        """
        Пустое значение поля ввода денежных средств
        """
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        app.balance_page.entry_data_balance(name=data.name, card=data.card, date_card=data.card_data,
                                            cash=invalid_card_cash)
        assert app.balance_page.log_status_invalid() == "Check money! It must be not empty!"

    @pytest.mark.parametrize("invalid_card_cash", TestCases.INVALID_DATA_FOR_BALANCE_PAGE_CARD_USER)
    def test_invalid_card_cash(self, app, login_user, invalid_card_cash):
        """
        Пустое значение поля ввода денежных средств
        """
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        app.balance_page.invalid_entry_data_balance(name=data.name, card=data.card, date_card=data.card_data,
                                                    cash=data.cash)
        assert app.balance_page.log_status_invalid() == "Read agree and click checkbox!"
