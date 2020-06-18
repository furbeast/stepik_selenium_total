from .pages.product_page import ProductPage
import time


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    # page.math_alert()
    page.solve_quiz_and_get_code()
    time.sleep(2)
