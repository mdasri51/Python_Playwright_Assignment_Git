from playwright.sync_api import expect
from playwright.sync_api import Page

class LogoutPage:

    def __init__(self, page):   
        self.page = page

    def logOut(self):
        self.page.click("//div[@class='user-profile-trigger false']")
        self.page.click("//span[text()='Logout'] ")

    def is_logged_out(self):
        self.page.wait_for_timeout(5000)
        expect(self.page.get_by_text("Login using your Deloitte account to continue")).to_be_visible()   
        
           
   # //p[text()='Login using your Deloitte account to continue'] xpath for logout page
