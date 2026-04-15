from pages.logout_page import LogoutPage
from pages.login_page import LoginPage
from pages.card_count_display_page import CardCountDisplay
from utils.config import USERNAME, PASSWORD


def test_card_count(page):

    login = LoginPage(page)
    login.launch_baseurl()
    login.login(USERNAME, PASSWORD)
    login.is_logged_in()

   

    card_count = CardCountDisplay(page)
    card_count.card_print_value()

    logout = LogoutPage(page)
    logout.logOut()
    logout.is_logged_out()
