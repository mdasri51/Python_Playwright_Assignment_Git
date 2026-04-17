import pytest
from playwright.sync_api import sync_playwright
from pages.task1_Login_Page import LoginPage
from pages.task5_Logout_Page import LogoutPage
from utils.config import USERNAME, PASSWORD

@pytest.fixture(scope="function")

def page(request):
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        #Before Test-Login
        login = LoginPage(page)
        login.launch_baseurl()
        page.wait_for_load_state("load")
        login.login(USERNAME, PASSWORD)
       #login.is_logged_in()
    

        yield page

        #skip logout for lougout test

        #After Test -Logout
        if "test_Task5_Logout" not in request.node.name:
            logout = LogoutPage(page)
            logout.logOut()
            logout.is_logged_out()

        browser.close()