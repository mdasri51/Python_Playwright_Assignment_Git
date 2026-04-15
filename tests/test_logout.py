
from pages.logout_page import LogoutPage
from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD


def test_logout(page):

    login = LoginPage(page)
    login.launch_baseurl()
    login.login(USERNAME, PASSWORD)
    login.is_logged_in()

    logout = LogoutPage(page)
    logout.logOut()
    logout.is_logged_out()

    

