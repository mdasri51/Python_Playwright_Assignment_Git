
from pages.task5_Logout_Page import LogoutPage
from pages.task1_Login_Page import LoginPage
from pages.task4_Demand_Pursuit_Page import DemandPursuits
from utils.config import USERNAME, PASSWORD


def test_demand_pursuit(page):

    
    login = LoginPage(page)
    login.launch_baseurl()
    login.login(USERNAME, PASSWORD)
    login.is_logged_in()
    
    dp = DemandPursuits(page)
    dp.navigation_demandPursuit("Mayuri Dasri")
  #  dp.serach_pursuit("Mayuri Dasri")
   # dp.navigate_and_search("Mayuri Dasri")


    logout = LogoutPage(page)
    logout.logOut()
    logout.is_logged_out()