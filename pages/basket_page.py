from .base_page import BasePage
from .locators import BasketPagLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasketPage(BasePage):
    def basket_button_should_be_able_to(self):
        assert self.is_element_present(*BasketPagLocators.BASKET_BUTTON), "Basket button not found"

    def go_to_basket(self):
        self.basket_button_should_be_able_to()
        basket_buttom = self.browser.find_element(*BasketPagLocators.BASKET_BUTTON)
        basket_buttom = WebDriverWait(self.browser, 30)\
            .until(EC.element_to_be_clickable(basket_buttom))
        basket_buttom.click()

    def should_not_found_prodict_in_basket(self):
        assert self.is_not_element_present(*BasketPagLocators.ITEMS_TO_BUY), "In the basket found items"
    def should_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPagLocators.MESSAGE_CONTINUE_SHOPPING), "Basket button not found"

