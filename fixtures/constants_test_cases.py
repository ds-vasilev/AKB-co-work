class TestCases:
    INVALID_EMAILS_LIST = [
        ["nekorrektnii#email"],
        ["nekorrektniinekorrektniinekorrrrrrrekorrektniinekortniinekorrektniinekorrektniinekorrektnii#email"],
        ["nekorrektnii@email"],
        ["nekorrektnii.ru"],
        ["nekorrektnii@.ru"],
        ["@nekorrektnii.ru"],
        ["nekorrektnii@ru"],
        ["@nekorrektnii@mail"],
        ["@nekorrektnii@mail"],
        ["биба@яндекс.рф"],  # todo неработает с кирилическими домена]и
    ]
