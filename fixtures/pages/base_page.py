import time
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, app):
        self.app = app

    def _find_element(self, locator, wait_time = 20):
        """
        Find element. Use Explicit wait
        :param locator: locator like (By.ID, 'name')
        :param wait_time: wait time
        :return: return selenium element
        """
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        return element

    def _find_all_elements(self, locator, wait_time = 20):
        """
        Find element. Use Explicit wait
        :param locator: locator like (By.ID, 'name')
        :param wait_time: wait time
        :return: return selenium element
        """
        elements = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        return elements

    def click_element(self, locator, wait_time = 20):
        """
        Click element.
        """
        element = self._find_element(locator, wait_time)
        element.click()
        self.app.driver.fullscreen_window()

    def fill(self, locator, value: str, wait_time=20):
        """
        Fill element (fill == send_keys)
        :param data: string to fill
        """
        element = self._find_element(locator, wait_time)
        if value:
            element.send_keys(value)

    def text(self, locator, wait_time=20) -> str:
        """
        Get element text.
        """
        element = self._find_element(locator, wait_time)
        return element.text

    def open_page(self, url: str):
        """
        Open page.
        """
        self.app.driver.get(url)
        self.app.driver.fullscreen_window()

    def clear(self, locator, wait_time = 20):
        """
        Clear element.
        """
        element = self._find_element(locator, wait_time)
        element.clear()

    def re_fresh(self, locator, wait_time = 20):
        """
        Refresh element.
        """
        element = self._find_element(locator, wait_time)
        element.send_keys(Keys.F5)
        self.app.driver.fullscreen_window()

    def text_on_all_same_fields(self, locator, wait_time=20) -> list:
        """
        Get elementS text.
        """
        elements = self._find_all_elements(locator, wait_time)
        biba = []
        for i in elements:
            n = i.text
            biba.append(n)
        return biba

    def time_mashine(self, locator, what_we_find, wait_time=5):
        """
        Реализация слипа через явные ожидания.
        """
        timestamp = time.time() + wait_time
        while time.time() < timestamp:
            element = self._find_element(locator)
            print(element.text, what_we_find)
            if element.text == what_we_find:
                return
            time.sleep(0.5)
        raise Exception
