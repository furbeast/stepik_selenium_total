from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def press_button_add_to_basket(self):
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button_add.click()

    def check_message_1(self):
        # assert self.browser.find_element(*ProductPageLocators.MESSAGE_1).text == f''
        check_message_strong()

    def check_message_strong(self):
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_1_STRONG).text == self.browser.find_element(*ProductPageLocators.NAME_BOOK).text, "Incorrect name book in message"
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_2_STRONG).text == "Deferred benefit offer", "Incorrect name book in message"
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_3_STRONG).text == self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text, "Incorrect price book in message"
