from utils.config import BASEURL
from playwright.sync_api import expect

class LoginPage:

    def __init__(self, page):   #calls like constructor
        self.page = page    #self refer to current object of class
                            #page value is storing in to self.page sp other can use it

    def launch_baseurl(self):
        self.page.goto(BASEURL)

    def login(self, username, password):
        self.page.click("button[type='button']")   #clicking SSO Button
        #self.page.click("//button[@type='button']")

        self.page.locator("#signInFormUsername:visible").fill(username);   #Entering username
        #self.page.locator("(//input[@placeholder='Username'])[1]").fill(username);

        self.page.locator("#signInFormPassword:visible").fill(password);    #Entering password
        #self.page.locator("(//input[@name='password'])[1]").fill(password);
        
        self.page.click("input[name='signInSubmitButton']:visible")
        #self.page.click("(//input[@value='Sign in'])[1])");

        self.page.wait_for_timeout(15000)
        cookie_close = self.page.locator(".onetrust-close-btn-handler:visible")

        if cookie_close.is_visible():
            cookie_close.click()

    def is_logged_in(self):
        expect(self.page.get_by_text("Demand Pursuits")).to_be_visible()

        
