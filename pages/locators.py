from selenium.webdriver.common.by import By

class PageLoginLocators():
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_EMAIL = (By.NAME, "registration-email")
    REGISTER_PASSWORD = (By.NAME, "registration-password1")
    REGISTER_REPEAT_PASSWORD = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    MESSAGE_ABOUT_NAME = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, '#messages > div:nth-child(2) > div > strong')
    MESSAGE_ABOUT_PRICE = (By.CSS_SELECTOR,
        '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
    PROGUCT_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPagLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR,
        "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    ITEMS_TO_BUY = (By.CLASS_NAME, "col-sm-6 h3")
    MESSAGE_CONTINUE_SHOPPING = (By.CSS_SELECTOR, "#content_inner > p > a")



