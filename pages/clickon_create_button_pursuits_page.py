from playwright.sync_api import expect
from playwright.sync_api import Page
import logging


class CreateButton_Click:

    def __init__(self, page):   
        self.page = page

    def leftPane(self):
        self.page.click("//button[@class='_menuItem_1tt27_90']")
        self.page.wait_for_timeout(5000)
        self.page.click("//div[text()='Create Pursuit']")
        self.page.wait_for_timeout(15000)
        self.page.locator("//span[text()='Create']").scroll_into_view_if_needed()  
        self.page.click("//span[text()='Create']")
        #button is not getting visible

        expect(self.page.get_by_text("Client name is required")).to_be_visible()
        expect(self.page.get_by_text("Pursuit name is required")).to_be_visible()
        expect(self.page.get_by_text("Proposal type is required")).to_be_visible()
        expect(self.page.get_by_text("Project type is required")).to_be_visible()
        expect(self.page.get_by_text("Country is required")).to_be_visible()
        expect(self.page.get_by_text("Industry is required")).to_be_visible()
        expect(self.page.get_by_text("Billing arrangement is required")).to_be_visible()
        expect(self.page.get_by_text("Date range is required")).to_be_visible()
        expect(self.page.get_by_text("Resolve all the errors to proceed")).to_be_visible()

    
    
    
    
    
    
    
    
        
        
       

