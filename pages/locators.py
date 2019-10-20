from selenium.webdriver.common.by import By

class MainPageLocators():
    pass

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CHECKING_TEXT = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_ADDED = (By.CSS_SELECTOR, "#messages>div:nth-child(1)> div:nth-child(2) > strong")
    DEL_USSER_BUTTON = (By.CSS_SELECTOR,".form-group>button")
    PASSWORD_TO_USER_DEL = (By.CSS_SELECTOR, "#id_password")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    PRODUCT_ADDED = (By.CSS_SELECTOR, "#id_form-0-quantity")
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group>a")
    CHECKING_TEXT = (By.CSS_SELECTOR, "#content_inner>p:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
	
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTRATION_ONE =(By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REGISTRATION_THWO = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")
