from pages.task5_Logout_Page import LogoutPage
from pages.task1_Login_Page import LoginPage
from pages.task2_DashBoard_Validation_Page import DemandPursuit
from utils.config import USERNAME, PASSWORD


def test_demandPursuite_validation(page):

    #login = LoginPage(page)
    #login.launch_baseurl()
    #login.login(USERNAME, PASSWORD)
    #login.is_logged_in()
    
    dp = DemandPursuit(page)
    dp.six_category_validate()
    dp.card_count()
    dp.pursuite_option_validation()
    dp.leftPane_validation()


   # logout = LogoutPage(page)
    #logout.logOut()
    #logout.is_logged_out()
    