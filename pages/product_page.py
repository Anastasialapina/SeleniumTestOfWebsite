from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_bucket(self):
        self.button_should_be_able_to()
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BUCKET)
        button.click()

    def button_should_be_able_to(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BUCKET), "Button for adding to bucket not found"

    def message_about_add_product_should_be_able_to(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_NAME), "Message about adding to bucket not found"

    def product_name_should_be_able_to(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_NAME), "Product name not found"

    def price_should_be_able_to(self):
        assert self.is_element_present(*ProductPageLocators.PRICE), "Price not found"

    def should_be_promo_url(self):
        # проверка на корректный url адрес
        URL = self.browser.current_url
        assert "?promo=newYear" in URL, "It is not promo URL"

    def get_message_about_name_product(self):
        self.message_about_add_product_should_be_able_to()
        return self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_NAME)

    def get_message_about_adding(self):
        return self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING)

    def get_message_about_price(self):
        return self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_PRICE)

    def get_product_name(self):
        self.product_name_should_be_able_to()
        return self.browser.find_element(*ProductPageLocators.PROGUCT_NAME)

    def get_price(self):
        self.price_should_be_able_to()
        return self.browser.find_element(*ProductPageLocators.PRICE)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "The message did not found"
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "The message did not disapear"

    def check_product_name(self, page):
        messange_about_name_product = page.get_message_about_name_product()
        product_name = page.get_product_name()
        assert product_name.text == messange_about_name_product.text

    def check_message_about_adding(self, page):
        messange_about_adding = page.get_message_about_adding()
        assert "Deferred benefit offer" in messange_about_adding.text

    def check_price(self, page):
        messange_about_price = page.get_message_about_price()
        price = page.get_price()
        assert price.text == messange_about_price.text

