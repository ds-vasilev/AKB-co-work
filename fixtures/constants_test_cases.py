class TestCases:
    INVALID_EMAILS_LIST = [
        {"test_input": "nekorrektnii#email"},
        {"test_input": "nekorrektniinekorrektniinekorrrrrrrekorrektniinekortniinekorrektniinekorrektniinekorrektnii#email"},
        {"test_input": "nekorrektnii@email"},
        {"test_input": "nekorrektnii.ru"},
        {"test_input": "nekorrektnii@.ru"},
        {"test_input": "@nekorrektnii.ru"},
        {"test_input": "nekorrektnii@ru"},
        {"test_input": "@nekorrektnii@mail"},
        {"test_input": "@nekorrektnii@mail"},
        {"test_input": "биба@яндекс.рф"},  # todo неработает с кирилическими доменами
    ]
