from faker import Faker

fake = Faker()


class RegisterUserModel:
    def __init__(self, email: str = None, password_1: str = None,
                 password_2: str = None):
        self.email = email
        self.password_1 = password_1
        self.password_2 = password_2

    @staticmethod
    def random():
        email_ = fake.email()
        password = fake.password()
        return RegisterUserModel(email=email_, password_1=password,
                                 password_2=password)
