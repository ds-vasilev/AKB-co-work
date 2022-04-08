from fixtures.constants import ErrorText


class TestRegistrationPage:
    def test_prepare_base(self, app):  # todo не смог подобрать селлектор
        """
        Подготовка базы через клик на Prepere data
        """
        pass


    def test_valid_register(self, app):
        pass


    def test_invalid_email_register(self, app):  # кирилические домены не работают
        pass


    def test_invalid_pass_mach_register(self, app):
        """Совпадение паролей."""
        pass


    def test_invalid_pass_long_register(self, app):
        """Длина паролей."""
        pass


    def test_base_drop_404(self, app):  # Todo проверить  Error, check network
        """после 3 попыток база падает."""
        pass