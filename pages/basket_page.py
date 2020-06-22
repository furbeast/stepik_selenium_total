from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket not empty"

    def basket_empty_text(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text.find('empty'), "Basket text empty not found"
