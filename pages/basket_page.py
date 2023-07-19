from .base_page import BasePage
from .locators import BucketPagLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasketPage(BasePage):
    def bucket_button_should_be_able_to(self):
        assert self.is_element_present(*BucketPagLocators.BUCKET_BUTTON), "Bucket button not found"

    def go_to_bucket(self):
        self.bucket_button_should_be_able_to()
        bucket_buttom = self.browser.find_element(*BucketPagLocators.BUCKET_BUTTON)
        bucket_buttom = WebDriverWait(self.browser, 30)\
            .until(EC.element_to_be_clickable(bucket_buttom))
        bucket_buttom.click()

    def should_not_found_prodict_in_bucket(self):
        assert self.is_not_element_present(*BucketPagLocators.ITEMS_TO_BUY), "In the bucket found items"
    def should_message_bucket_is_empty(self):
        assert self.is_element_present(*BucketPagLocators.MESSAGE_CONTINUE_SHOPPING), "Bucket button not found"

