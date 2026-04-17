import logging
from playwright.sync_api import Page
from playwright.sync_api import expect

class DemandPursuit:

    def __init__(self, page):   
        self.page = page
    

    #Test1
    def six_category_validate(self):

        expected_categories = {
        "All" : "//span[@class='sc-eeDRCX bEezqN' and text()='All'] ",
        "New" : "//span[@class='sc-eeDRCX bEezqN' and text()='New']",
        "In Progress" : "//span[@class='sc-eeDRCX bEezqN' and text()='In Progress']",
        "Cancelled" :"//span[@class='sc-eeDRCX bEezqN' and text()='Cancelled']",
        "Won" : "//span[@class='sc-eeDRCX bEezqN' and text()='Won']",
        "Deferred" : "//span[@class='sc-eeDRCX bEezqN' and text()='Deferred']"
        }
        
        for name, xpath in expected_categories.items():
            locator =self.page.locator(xpath)
            expect(locator).to_be_visible()
            logging.info(f"{name} is visible")      #Storing record in report file 
            print(f"{name} is visible")


    #Test2
    def card_count(self):

        categories = [
            ("ALL","//span[@class='sc-eeDRCX bEezqN' and text()='All']/following-sibling::span"),
            ("New","//span[@class='sc-eeDRCX bEezqN' and text()='New']/following-sibling::span"),
            ("In Progress","//span[@class='sc-eeDRCX bEezqN' and text()='In Progress']/following-sibling::span"),
            ("Cancelled","//span[@class='sc-eeDRCX bEezqN' and text()='Cancelled']/following-sibling::span"),
            ("Won","//span[@class='sc-eeDRCX bEezqN' and text()='Won']/following-sibling::span"),
            ("Deferred","//span[@class='sc-eeDRCX bEezqN' and text()='Deferred']/following-sibling::span"),
        ]
        
        for name, xpath in categories:
            locator  = self.page.locator(xpath)
           # assert element.is_visible(), f"{name} count not visible"
            count = locator.inner_text()
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
          #  assert element.is_visible(), f"{name} is not visible"
            expect(element).to_be_visible()
            print(f"{name} is visible")

