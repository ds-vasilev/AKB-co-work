class TestCases:
    INVALID_EMAILS_LIST_FOR_REG = [
        ["nekorrektnii#email"],
        ["nekorrektniinekorrektniinekorrrrrrrekorrektniinekortniinekorrektniinekorrektniinekorrektnii#email"],
        ["nekorrektnii@email"],
        ["nekorrektnii.ru"],
        ["nekorrektnii@.ru"],
        ["@nekorrektnii.ru"],
        ["nekorrektnii@ru"],
        ["@nekorrektnii@mail"],
        ["@nekorrektnii@mail"],
        ["биба@яндекс.рф"],  # сайт не работает с кирилическими доменами
    ]

    INVALID_DATA_FOR_LOG_PAGE = [
        ["", ""],
        ["invalid", "invalid"],
        ["111@test.ru", ""],
        ["", "11111111"],
    ]

    INVALID_DATA_FOR_BALANCE_PAGE_CARD_NUM = [
        ["34562345"],
        ["324657236485234576237485"],
        [""]
    ]

    INVALID_DATA_FOR_BALANCE_PAGE_CARD_DATE = [
        [""]
    ]

    INVALID_DATA_FOR_BALANCE_PAGE_CARD_USER = [
        [""]
    ]

    INVALID_DATA_FOR_BALANCE_PAGE_CARD_CASH = [
        [""]
    ]
