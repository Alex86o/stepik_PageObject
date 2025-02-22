from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "/login/" in self.browser.current_url,\
                        "It's not page log and registration"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME),\
                        "Unpresent form login user name"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD),\
                        "Unpresent form login passworg"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL),\
                           "Unpresent form email"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD),\
                          "Unrpesent form password"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_REPEAT),\
                    "Unpresent form repeat password"



