from fixtures.constants import RegMessages
from models.register import RegisterUserModel


class TestRegistrationPage:
    def test_valid_register(self, app):
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.reg_status_on_top_right() == RegMessages.SUCCESS

    def test_invalid_email(self, app):
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.email = "nekorrektnii#email"
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.reg_status_big_red_tab() == RegMessages.INVALID_EMAIL[0]\
               + str(data.email) + RegMessages.INVALID_EMAIL[1]

    def test_different_passwords(self, app):
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.password_2 = "drugoypass"
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.reg_status_big_red_tab() == RegMessages.INVALID_SECOND_PASS

    def test_short_passwords(self, app):
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.password_1 = "short"
        data.password_2 = "short"
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.reg_status_big_red_tab() == RegMessages.INVALID_SHORT_PASS


    # def test_invalid_email_register(self, app):  # кирилические домены не проходят проверку
    #     pass
    #
    # def test_base_drop_404(self, app):  # Todo проверить  Error, check network
    #     """после 3 попыток база падает."""
    #     pass