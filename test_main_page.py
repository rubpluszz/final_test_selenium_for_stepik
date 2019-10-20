from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.locators import BasePageLocators
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
	
    def test_guest_can_go_to_login_page(self, browser):
		#Сhecking the possibility of going to the registration page not registered user
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser,link)  
        page.open() 
        page.go_to_login_page() 
        login_page = LoginPage(browser,browser.current_url)
        login_page.should_be_login_page()
	
    def test_guest_should_seelogin_link(self, browser):
        #Check for a link to the registration page
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
	#Testing the addition of goods to the basket by an unauthorized user
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.product_in_basket_opened()
    page.should_not_be_product_in_bascet()
    page.should_be_emptay_basket_message()
    assert "empty" in browser.find_element(*BasePageLocators.CHECKING_TEXT).text, "No empty basket message"
