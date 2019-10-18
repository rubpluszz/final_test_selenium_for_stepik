from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductPage(BasePage):
	
	def add_product_to_basket(self):
		
		print("find button 'add to basket'")
		addtobasket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
		print("clicked to button")		
		addtobasket_button.click()
		BasePage.solve_quiz_and_get_code(self)
		
	def should_be_added_to_basket_message(self):
		
		print("Checking added product to basket")
		checking_text = self.browser.find_element(*ProductPageLocators.CHECKING_TEXT).text
		assert checking_text == self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED).text, "No report that the item has been added to basket"
	
	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED), "Success message is presented, but should not be"

		
	def is_disappeared(self, how, timeout=4):
		try:
			WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((*ProductPageLocators.PRODUCT_ADDED)))
		except TimeoutException:
			return False

		return True
		
		
