import time

from fixtures.constants import LogMessages
from models.balance import BalanceUserModel

#16 символов
class TestSignInPage:
    # todo подумать, как передать сюда валидный пароль со страницы регистрации. Вариант - возвращать в app,
    #  уточнить про реализацию
    def test_valid_login(self, app, login_user):
        """
        Логин.
        """
        # data = BalanceUserModel.random()
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        # time.sleep(10)
        app.balance_page.entry_data_balance(name=data.name, card=data.card, date_card=data.card_data, cash=data.cash)
        while True:
            ...
