from selenium.webdriver.common.by import By

class MainPageLocators():
	PRODUCT_ADDED = (By.CSS_SELECTOR, "#id_form-0-quantity")
	ADD_TO_BASKET = (By.CSS_SELECTOR, "..btn-group > a")
	CHECKING_TEXT = (By.CSS_SELECTOR, ".alertinner>p:nth-child(1)")
	
class ProductPageLocators():
	ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
	CHECKING_TEXT = (By.CSS_SELECTOR, ".product_main>h1")
	PRODUCT_ADDED = (By.CSS_SELECTOR, "#messages>div:nth-child(1)> div:nth-child(2) > strong")
	
class BasePageLocators():
	
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	PRODUCT_ADDED = (By.CSS_SELECTOR, "#id_form-0-quantity")
	VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group>a")
	CHECKING_TEXT = (By.CSS_SELECTOR, "#content_inner>p:nth-child(1)")
	
class LoginPageLocators():
	
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
