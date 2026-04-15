
from pages.logout_page import LogoutPage
from pages.login_page import LoginPage
from pages.clickon_create_button_pursuits_page import CreateButton_Click
from utils.config import USERNAME, PASSWORD


def test_logout(page):

    login = LoginPage(page)
    login.launch_baseurl()
    login.login(USERNAME, PASSWORD)
    login.is_logged_in()


    createClick = CreateButton_Click(page)
    createClick.leftPane()

    page.wait_for_timeout(15000)
    logout = LogoutPage(page)
    logout.logOut()
    logout.is_logged_out()
