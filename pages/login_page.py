from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
	
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        actual_url = self.browser.current_url
        assert "login" in actual_url, "'login' is not in actual url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login Form is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration Form is not presented"
	
    def register_new_user(browser, email, password):
        input_email =browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION)
        input_email.send_keys(email)
        input_password_one = browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION_ONE)
        input_password_one.send_keys(password)
        input_password_thwo = browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION_THWO)
        input_password_thwo.send_keys(password)
        browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
		
