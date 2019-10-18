from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
	REGISTRATION_FORM = (By.CSS_SELECTOR, ".registortion_form")

class ProductPageLocators():
	ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
	CHECKING_TEXT = (By.CSS_SELECTOR, ".product_main>h1")
	PRODUCT_ADDED = (By.CSS_SELECTOR, "#messages>div:nth-child(1)> div:nth-child(2) > strong")
	
class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
	REGISTRATION_FORM = (By.CSS_SELECTOR, ".registortion_form")
