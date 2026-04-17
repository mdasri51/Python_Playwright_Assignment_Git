from pages.task1_Login_Page import LoginPage
from utils.config import USERNAME, PASSWORD


def test_login(page):
    
    login = LoginPage(page)
    #login.launch_baseurl()
    #page.wait_for_load_state("load")
    #login.login(USERNAME, PASSWORD)
    login.is_logged_in()


    

   