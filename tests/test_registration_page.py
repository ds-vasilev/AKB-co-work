from fixtures.constants import ErrorText
from models.register import RegisterUserModel


class TestRegistrationPage:
    # def test_prepare_base(self, app):  # todo не смог подобрать селлектор
    #     """
    #     Подготовка базы через клик на Prepere data
    #     """
    #     pass

    def test_valid_register(self, app):
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        app.registration_page.entry_data_registration(data=data)

        import time   # todo заглушка
        time.sleep(2)

    def test_invalid_email(self, app):
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.email = "nekorrektnii#email"
        app.registration_page.entry_data_registration(data=data)

        import time   # todo заглушка
        time.sleep(2)

    def test_different_password(self, app):
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.password_2 = "drugoypass"
        app.registration_page.entry_data_registration(data=data)

        import time   # todo заглушка
        time.sleep(2)

    def test_short_password(self, app):
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.password_1 = "short"
        data.password_2 = "short"
        app.registration_page.entry_data_registration(data=data)

        import time   # todo заглушка
        time.sleep(2)



    # def test_invalid_email_register(self, app):  # кирилические домены не работают
    #     pass
    #
    #
    # def test_invalid_pass_mach_register(self, app):
    #     """Совпадение паролей."""
    #     pass
    #
    #
    # def test_invalid_pass_long_register(self, app):
    #     """Длина паролей."""
    #     pass
    #
    #
    # def test_base_drop_404(self, app):  # Todo проверить  Error, check network
    #     """после 3 попыток база падает."""
    #     pass