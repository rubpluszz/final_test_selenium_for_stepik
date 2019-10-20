from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.locators import BasePageLocators
from .pages.base_page import BasePage
import pytest
import time


@pytest.mark.need_review							  
def test_guest_can_add_product_to_basket(browser):
	link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
	page = ProductPage(browser,link)
	page.open()
	page.add_product_to_basket()
	page.should_be_added_to_basket_message()
	
def test_guest_should_see_login_link_on_product_page(browser):

	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

@pytest.mark.need_review	
def test_guest_can_go_to_login_page_from_product_page (browser):
	
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()
	login_page = LoginPage(browser, browser.current_url)
	login_page.should_be_login_page()
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):

	link = "http://selenium1py.pythonanywhere.com/"
	page = ProductPage(browser, link)
	page.open()
	page.product_in_basket_opened()
	page.should_not_be_product_in_bascet()
	page.should_be_emptay_basket_message()
	print("Checking empty basket")
	assert "empty" in browser.find_element(*BasePageLocators.CHECKING_TEXT).text, "No empty basket message"

@pytest.mark.usser_add_to_basket
class TestUserAddToBasketFromProductPage():
	
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):	
		link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
		page = ProductPage(browser,link)
		page.open()
		email = str(int(time.time()))+"@hoolymail.org"
		password = str(int(time.time()))+"qwerty"
		LoginPage.register_new_user(browser, email, password)
		self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
		yield
		page.deleted_usser(browser, password)
		
	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self, browser):
		
		page = ProductPage(browser, self.link)
		page.open()
		page.add_product_to_basket()
		page.should_be_added_to_basket_message()
	
	def test_usser_cant_see_success_message(self, browser): 
		
		page = ProductPage(browser, self.link)
		page.open()
		page.should_not_be_success_message()

 
