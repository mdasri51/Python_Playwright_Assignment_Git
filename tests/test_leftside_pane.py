
from pages.logout_page import LogoutPage
from pages.login_page import LoginPage
from pages.leftside_pane_page import LeftsidePane
from utils.config import USERNAME, PASSWORD


def test_logout(page):

    login = LoginPage(page)
    login.launch_baseurl()
    login.login(USERNAME, PASSWORD)
    login.is_logged_in()


    leftpaneObj = LeftsidePane(page)
    leftpaneObj.leftPane()

    logout = LogoutPage(page)
    logout.logOut()
    logout.is_logged_out()
