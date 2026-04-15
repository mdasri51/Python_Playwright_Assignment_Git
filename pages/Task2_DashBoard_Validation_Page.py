import logging

from playwright.sync_api import Page
from playwright.sync_api import expect

class DemandPursuit:

    def __init__(self, page):   
        self.page = page
    

    #Test1
    def six_category_validate(self):

        expected_categories = {
        "All" : "//span[text()='All'] ",
        "New" : "(//span[text()='New'])[1]",
        "In Progress" : "(//span[text()='In Progress'])[1]",
        "Cancelled" :"//span[text()='Cancelled']",
        "Won" : "//span[text()='Won']",
        "Deferred" : "//span[text()='Deferred']"
        }
        
        for name, xpath in expected_categories.items():
            locator =self.page.locator(xpath)
            expect(locator).to_be_visible()
            logging.info(f"{name} is visible")      #Storing record in report file 
            print(f"{name} is visible")

    #Test2
    def card_count(self):

        categories = [
            ("ALL","//span[text()='All']/following-sibling::span"),
            ("New","(//span[text()='New'])[1]/following-sibling::span"),
            ("In Progress","(//span[text()='In Progress'])[1]/following-sibling::span"),
            ("Cancelled","//span[text()='Cancelled']/following-sibling::span"),
            ("Won","//span[text()='Won']/following-sibling::span"),
            ("Deferred","//span[text()='Deferred']/following-sibling::span"),
        ]
        
        for name, xpath in categories:
            element = self.page.locator(xpath)
            assert element.is_visible(), f"{name} count not visible"
            count = element.inner_text()
            print(f"{name} has {count} cards")

    #Test3
    def pursuite_option_validation(self):
        expect(self.page.get_by_text("List of all pursuits")).to_be_visible()   
        #//h3[@class="sc-dLMFT ljnIHJ pursuit-table-title pursuit-table-title"]

    
    #Test4
    def leftPane_validation(self):
        self.page.click("//button[@class='_menuItem_1tt27_90']")

        self.page.wait_for_timeout(5000)

        expected_categories = [
        ("Collapse" , "//div[text()='Collapse'] "),
        ("Demand Pursuits" , "//div[text()='Demand Pursuits']"),
        ("Create Pursuit" , "//div[text()='Create Pursuit']"),
        ]
        
        for name, xpath in expected_categories:
            element =self.page.locator(xpath)
            assert element.is_visible(), f"{name} is not visible"
            print(f"{name} is visible")

           