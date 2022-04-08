from fixtures.constants import ErrorText


class TestSignInPage:
    # todo подумать, как передать сюда валидный пароль со страницы регистрации. Вариант - возвращать в app,
    #  уточнить про реализацию



    def test_valid_login(self, app):
        """логин"""
        pass


    def test_repeated_login(self, app):
        """повторный логин без логаута"""
        pass


    def test_invalid_login_login(self, app):
        """Неверный логин"""
        pass


    def test_invalid_login_login_zero(self, app):
        """пустой логин"""
        pass


    def test_invalid_login_pass(self, app):
        """Неверный пароль"""
        pass
