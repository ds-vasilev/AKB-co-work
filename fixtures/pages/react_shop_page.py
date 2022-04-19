from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage
import time


class ReactShopPage(BasePage):
    SHOP_LOGO = (By.CLASS_NAME, "brand-logo")
    BUY_BUTTON_ON_GOOD_CARD = (By.XPATH, "//button[@class='btn']")
    BASKET_BUTTON = (By.CLASS_NAME, "material-icons")
    BUY_BUTTON_IN_BASKET = (By.XPATH, "//button[@class='btn red btn-small']")
    MESSAGE_STATUS_TOP_RIGHT = (By.CLASS_NAME, "toast")
    BALANCE_ID = (By.ID, "blance-link")
    FIRST_PLACE_PRICE = (By.XPATH, "//span[@class='right']")
    SEARCH_PRODUCT = (By.ID, "email_inline")
    SEARCH_BUTTON = (By.CLASS_NAME, "search-btn")
    FIRST_CARD_TITLE = (By.CLASS_NAME, "card-title")

    def open_shop_page(self):
        """
        Open shop mainpage.
        """
        self.open_page(self.app.url)
        self.click_element(locator=self.SHOP_LOGO)

    def item_add_in_basket(self):
        """
        Добавление товара в карзину и проверка наличия.
        """
        self.click_element(locator=self.BUY_BUTTON_ON_GOOD_CARD)

    def open_basket(self):
        """
        Открыть корзину для покупок.
        """
        self.click_element(locator=self.BASKET_BUTTON)

    def press_buy_in_basket(self):
        """
        Кликнуть кнопку "Buy" в корзине.
        """
        self.click_element(locator=self.BUY_BUTTON_IN_BASKET)

    def refresh_for_buy(self):
        """
        Рефреш страницы.
        """
        # self.re_fresh(locator=self.SHOP_LOGO)
        time.sleep(1)
        self.click_element(locator=self.SHOP_LOGO)


    def log_status_on_top_right(self) -> str:
        """
        Информационная всплывашка сверху-справа.
        """
        element = self.text(locator=self.MESSAGE_STATUS_TOP_RIGHT)
        return element

    def balance(self) -> str:
        """
        Текст с поля баланса.
        """
        element = self.text(locator=self.BALANCE_ID)
        return element

    def first_place_price(self) -> str:
        """
        Цена первого товара в выдаче.
        """
        element = self.text(locator=self.FIRST_PLACE_PRICE)
        return element

    def first_card_title(self) -> str:
        """
        Цена первого товара в выдаче.
        """
        element = self.text(locator=self.FIRST_CARD_TITLE)
        return element

    def search_product(self, search_data: str):
        """
        Поиск в товарах.
        """
        self.fill(locator=self.SEARCH_PRODUCT, value=search_data)
        time.sleep(2)
        self.click_element(locator=self.SEARCH_BUTTON)

    def all_card_title(self):
        """
        Цена первого товара в выдаче.
        """
        element = self.text_on_all_same_fields(locator=self.FIRST_CARD_TITLE)
        return element