import time


class TestReactShop:
    def test_buy_goods_valid(self, app, balance_user):
        """
        Юзкейс на обработку покупки и проверку списания баланса.
        """
        app.react_shop_page.open_shop_page()
        app.react_shop_page.item_add_in_basket()
        app.react_shop_page.open_basket()
        balance_on_start = int(app.react_shop_page.balance()[11:])
        app.react_shop_page.press_buy_in_basket()
        assert app.react_shop_page.log_status_on_top_right() is not None
        if balance_on_start != 0:
            app.react_shop_page.refresh_for_buy()
            time.sleep(1)
            assert int(app.react_shop_page.balance()[11:]) == balance_on_start - \
               int(app.react_shop_page.first_place_price()[:-1])
        print(type(app.react_shop_page.balance()), app.react_shop_page.balance())

    def test_buy_all_goods_valid(self, app):
        """
        Тест на добавление в корзину всех товаров.
        """
        app.react_shop_page.open_shop_page()
        all_goods = app.react_shop_page.all_card_title()
        assert len(all_goods) > 0
        # print(all_goods)
        # for i in all_goods:
        #     print(i)

    def test_search_valid(self, app):
        """
        Проверка работы поиска существующего товара и выдачи.
        """
        app.react_shop_page.open_shop_page()
        x = app.react_shop_page.first_card_title()
        app.react_shop_page.search_product(search_data=x)
        assert app.react_shop_page.first_card_title() == x

    # прикрутить xfail
    def test_search_invalid(self, app):
        """
        Проверка работы поиска существующего товара и выдачи.
        """
        app.react_shop_page.open_shop_page()
        x = "бипки"
        app.react_shop_page.search_product(search_data=x)
        assert app.react_shop_page.first_card_title() == x

    def test_buy(self, app):
        """
        Проверка покупки товара и отображения его в корзине.
        """
        pass
