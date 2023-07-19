from .base_page import BasePage
from .locators import PageLoginLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        URL = self.browser.current_url
        assert "login" in URL, "It is not login URL"

    def should_be_login_form(self):
        assert self.is_element_present(*PageLoginLocators.LOGIN_FORM), "Login form not found"

    def should_be_register_form(self):
        assert self.is_element_present(*PageLoginLocators.REGISTER_FORM), "Register form not found"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*PageLoginLocators.REGISTER_EMAIL)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*PageLoginLocators.REGISTER_PASSWORD)
        password_input.send_keys(password)
        repeat_password_input = self.browser.find_element(*PageLoginLocators.REGISTER_REPEAT_PASSWORD)
        repeat_password_input.send_keys(password)
        button = self.browser.find_element(*PageLoginLocators.REGISTER_BUTTON)
        button.click()


