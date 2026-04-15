from pages.logout_page import LogoutPage
from pages.login_page import LoginPage
from pages.create_pursuits_page import CreatePursuitsPage
from utils.config import USERNAME, PASSWORD


def create_new_pursuits(page):

    login = LoginPage(page)
    login.launch_baseurl()
    login.login(USERNAME, PASSWORD)
    login.is_logged_in()

    createPursuits = CreatePursuitsPage(page)
    createPursuits.newPursuits()

    logout = LogoutPage(page)
    logout.logOut()
    logout.is_logged_out()
