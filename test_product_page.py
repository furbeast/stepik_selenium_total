import time
import pytest
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


PRODUCT_LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
LOGIN_LINK = 'http://selenium1py.pythonanywhere.com/accounts/login/'

urls = [f'{PRODUCT_LINK}?promo=offer{n}' for n in range(10)]
urls[7] = pytest.param(urls[7], marks=pytest.mark.xfail)
# urls = [f'{PRODUCT_LINK}?promo=offer{n}' for n in range(1)]



@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        email = str(time.time()) + "@fakemail.org"
        password = "LIcKu6tOD"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.press_button_add_to_basket()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    @pytest.mark.parametrize('link', urls)
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.press_button_add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_message_strong()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.press_button_add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_message_strong()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.press_button_add_to_basket()
    page.should_dissapear_of_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, PRODUCT_LINK)
    page.open()
    page.go_to_basket_page()
    page.basket_empty()
    page.basket_empty_text()
