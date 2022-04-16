from fixtures.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class BalancePage(BasePage):
    NAME_BAYER = (By.ID, "name")
    CARD_BAYER = (By.ID, "card")
    DATA_CARD_BAYER = (By.ID, "data-card")
    COUNT_CASH = (By.ID, "data-money")
    CHECK_AGREE = (By.XPATH, "//input[@type='checkbox']")
    BT_TRANSFER = (By.CLASS_NAME, "waves-effect waves-light btn")
    BT_BALANCE = (By.ID, "blance-link")

    def open_balance_page(self):
        """
        open balance page
        """
        self.click_element(locator=self.BT_BALANCE)

    def entry_data_balance(self, name: str, card: int, date_card: str, cash: float):
        """
        ввод данных в поля и клик
        """
        self.fill(locator=self.NAME_BAYER, value=name)
        self.fill(locator=self.CARD_BAYER, value=card)
        self.fill(locator=self.DATA_CARD_BAYER, value=date_card)
        self.fill(locator=self.COUNT_CASH, value=cash)
        self.click_element(locator=self.CHECK_AGREE)
        self.click_element(locator=self.BT_TRANSFER)

    # def log_status_on_top_right(self) -> str:
    #     """информационная всплывашка справа-вверху"""
    #     element = self.text(locator=self.MESSAGE_LOG_STATUS_TOP_RIGHT)
    #     return element
