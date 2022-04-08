from fixtures.constants import ErrorText


class TestSignInPage:

    # todo Баланс неправильно считается после списания !!!!!!!!!!!!!11
    # todo Баланс неправильно отображается


    def test_name_lastame(self, app): #  todo ластнейма нет
        """имя"""
        pass


    def test_name_lastame_null(self, app):
        """имя нулевое"""
        pass


    def test_cart_number_16(self, app):
        """номер карты цифр 16"""
        pass


    def test_cart_number_16_null(self, app):
        """номер карты цифр 16 нулевое"""
        pass

    def test_cart_number_16_invalid_more(self, app):
        """номер карты цифр <16"""
        pass


    def test_cart_number_16_invalid_less(self, app):
        """номер карты цифр >16"""
        pass


    def test_cart_number_16_invalid_str(self, app):
        """номер карты буквы"""
        pass


    def test_date(self, app):
        """Дата"""  # todo нет контроля формы даты
        pass


    def test_date_null(self, app):
        """Дата нулевая"""
        pass


    def test_summ(self, app): # todo нет контроля формы, проходят и букы
        """наличие суммы в поле суммы"""
        pass


    def test_summ_null(self, app):
        """пустое поле суммы"""
        pass


    def test_agree_rules(self, app):
        """галка в согласии"""
        pass


    def test_agree_rules_null(self, app):
        """без галки в согласии"""
        pass
    