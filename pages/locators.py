from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini .btn-group')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FORM = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD_FORM = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_DOUBLE_PASSWORD_FORM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[value = Register]')


class ProductPageLocators():
    ADD_TO_BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_COST = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    MESSAGE_ADD_TO_BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages :nth-child(1) > .alertinner strong")
    MESSAGE_COST_OF_BASKET = (By.CSS_SELECTOR, '#messages :nth-child(3) > .alertinner p strong')


class BasketPageLocators:
    EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
    PRODUCT_IN_BASKET_HEADER = (By.CSS_SELECTOR, '.basket-title .row h2')
    BASKET_HEADER = (By.CSS_SELECTOR, '.page-header h1')