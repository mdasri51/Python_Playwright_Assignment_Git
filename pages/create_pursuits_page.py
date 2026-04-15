from playwright.sync_api import expect
from playwright.sync_api import Page

class CreatePursuitsPage:

    def __init__(self, page):   
        self.page = page

    def newPursuits(self):
        self.page.click("//button[@class='_menuItem_1tt27_90']")
        self.page.wait_for_timeout(5000)
        self.page.click("//div[text()='Create Pursuit']")

        element =self.page.locator("//span[text()='Create Pursuit']")
        if element.is_visible(): 
                print("Successfully landed on next page - We can create pursuits")
        else:
                raise Exception ("There may be error in navigating to next page")
            

        """
        assert element.is_visible(), "Successfully landed on next page - We can create pursuits"
        print("There may be error in navigating to next page")
        """