from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD


def test_login(page):
    login = LoginPage(page)
    login.launch_baseurl()
    login.login(USERNAME, PASSWORD)
    login.is_logged_in()



   