from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def press_button_add_to_basket(self):
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button_add.click()

    def check_message_strong(self):
        # self.browser.implicitly_wait(20)
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_STRONG).text == self.browser.find_element(*ProductPageLocators.NAME_BOOK).text, "Incorrect name book in message"
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_2_STRONG).text == "Deferred benefit offer", "Incorrect name book in message"
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_3_STRONG).text == self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text, "Incorrect price book in message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
