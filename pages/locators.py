from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    FORM_REGISTER = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    NAME_BOOK = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRICE_BOOK = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    SUCCESS_MESSAGE_STRONG = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    MESSAGE_2 = (By.CSS_SELECTOR, "#messages > div:nth-child(2) > div")
    MESSAGE_2_STRONG = (By.CSS_SELECTOR, "#messages > div:nth-child(2) > div > strong")
    MESSAGE_3 = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1)")
    MESSAGE_3_STRONG = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
