import logging
import pytest


class TestReactShop:
    def test_buy_goods_valid(self, app, balance_user):
        """
        Юзкейс на обработку покупки и проверку списания баланса.
        """
        app.react_shop_page.open_shop_page()
        app.react_shop_page.item_add_in_basket()
        app.react_shop_page.open_basket()
        balance_on_start = int(app.react_shop_page.balance()[11:])  # сумма из строки баланса. Отрезаем "Balance is "
        first_item_price = int(app.react_shop_page.first_place_price()[:-1])  # стоимость первого товара, обрезаем " ₽"
        balance_on_finish_calculate = balance_on_start - first_item_price  # Рассчитываем баланс после покупки
        app.react_shop_page.press_buy_in_basket()
        assert app.react_shop_page.log_status_on_top_right() is not None
        app.react_shop_page.refresh_for_buy()
        app.react_shop_page.time_balance_checker(balance_on_finish=balance_on_finish_calculate)
        balance_on_finish = int(app.react_shop_page.balance()[11:])  # сумма из строки баланса. Отрезаем "Balance is "
        assert balance_on_finish == balance_on_start - first_item_price
        logging.info(f"баланс {app.react_shop_page.balance()}")

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

    @pytest.mark.xfail()
    def test_search_invalid(self, app):
        """
        Проверка работы поиска не существующего товара и выдачи.
        """
        app.react_shop_page.open_shop_page()
        x = "бипки"
        app.react_shop_page.search_product(search_data=x)
        assert app.react_shop_page.first_card_title()
