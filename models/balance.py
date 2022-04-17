import random
from faker import Faker

fake = Faker()


class BalanceUserModel:
    def __init__(self, name: str = None, card: str = None,
                 card_data: str = None, cash: str = None):
        self.name = name
        self.card = card
        self.card_data = card_data
        self.cash = cash

    @staticmethod
    def random():
        name = fake.name()
        card = fake.credit_card_number()
        # card_data = fake.credit_card_expire()
        card_data = "12/12"
        print(card_data)
        cash = str(random.randint(1000, 5000))
        return BalanceUserModel(name=name, card=card,
                                card_data=card_data, cash=cash)
