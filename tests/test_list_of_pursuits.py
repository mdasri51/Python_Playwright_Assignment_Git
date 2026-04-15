
from pages.logout_page import LogoutPage
from pages.login_page import LoginPage
from pages.list_of_pursuits_page import List_of_pursuitsPage
from utils.config import USERNAME, PASSWORD


def test_six_category(page):

    login = LoginPage(page)
    login.launch_baseurl()
    login.login(USERNAME, PASSWORD)
    login.is_logged_in()

   

    text_name = List_of_pursuitsPage(page)
    text_name.pursuite_option()

    logout = LogoutPage(page)
    logout.logOut()
    logout.is_logged_out()
