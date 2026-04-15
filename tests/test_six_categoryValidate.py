from pages.logout_page import LogoutPage
from pages.login_page import LoginPage
from pages.six_categoryValidate_page import Six_CategoryPage
from utils.config import USERNAME, PASSWORD


def test_six_category(page):

    login = LoginPage(page)
    login.launch_baseurl()
    login.login(USERNAME, PASSWORD)
    login.is_logged_in()

   

    six_group = Six_CategoryPage(page)
    six_group.category_validate()

    logout = LogoutPage(page)
    logout.logOut()
    logout.is_logged_out()
