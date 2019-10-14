from .base_page import BasePage
from .locators import MainPageLocators

class LoginPage(BasePage):
	def should_be_login_page(self):
		self.should_be_login_url()
		self.should_be_login_form()
		self.should_be_register_form()

	def should_be_login_url(self):
		actual_url = self.browser.current_url
		assert "login" in actual_url, "'login' is not in actual url"

	def should_be_login_form(self):
		self.is_element_present(*MainPageLocators.LOGIN_FORM), "Login Form is not presented"


	def should_be_register_form(self):
		self.is_element_present(*MainPageLocators.REGISTRATION_FORM), "Registration Form is not presented"

