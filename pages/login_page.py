from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find('login') >= 0, "Login page is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def register_new_user(self, email: str, password: str):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        password_confirm_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_CONFIRM)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_SUBMIT)

        email_field.send_keys(email)
        password_field.send_keys(password)
        password_confirm_field.send_keys(password)
        submit_button.click()
