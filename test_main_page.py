from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
	
	print("Goto link")
	link = "http://selenium1py.pythonanywhere.com/"
	page = MainPage(browser,link) #инициализацируем Page Object, передаем в конструктор Экземляр класа и url 
	page.open() #открываем страницу
	page.go_to_login_page() #выполняем метод страницы - переходим на страницу логина
	login_page = LoginPage(browser,browser.current_url)
	login_page.should_be_login_page()
	
def test_guest_should_seelogin_link(browser):
	
	print("Goto link")
	link = "http://selenium1py.pythonanywhere.com/"
	page = MainPage(browser, link)
