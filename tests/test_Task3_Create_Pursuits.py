from pages.task5_Logout_Page import LogoutPage
from pages.task1_Login_Page import LoginPage
from pages.task3_Create_Pursuits_Page import CreatePursuitsPage
from utils.config import USERNAME, PASSWORD


def test_create_new_pursuits(page):

    
    #login = LoginPage(page)
    #login.launch_baseurl()
    #page.wait_for_load_state("load")
    #login.login(USERNAME, PASSWORD)
    #login.is_logged_in()

    createPursuits = CreatePursuitsPage(page)
    createPursuits.new_create_pursuits_page()
    createPursuits.validate_button_atbottom()
    createPursuits.validate_mandatory_field_erros()
    createPursuits.add_new_client()
    createPursuits.fill_pursuit_form("Testing", "India", "UI100")
    createPursuits.create_pursuit()
    createPursuits.validate_success_message()


    #logout = LogoutPage(page)
    #logout.logOut()
    #logout.is_logged_out()
    
