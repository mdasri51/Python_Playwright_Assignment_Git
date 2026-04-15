from playwright.sync_api import expect
from playwright.sync_api import Page
import logging

class LeftsidePane:

    def __init__(self, page):   
        self.page = page

    def leftPane(self):
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

            """
             if element.is_visible(): 
                print(f"{name} is visible")
            else:
                raise Exception (f"{name} is not visible")
            
            """


            """
            only to check text is visible or not 
            expect(self.page.get_by_text("Collapse")).to_be_visible()  #//div[text()='Collapse']
            expect(self.page.get_by_text("Demand Pursuits")).to_be_visible()   #//div[text()='Demand Pursuits']
            expect(self.page.get_by_text("Create Pursuit")).to_be_visible()     #//div[text()='Create Pursuit']


            only to checj text is visible or not 
            expect(locator).to_be_visible()
            logging.info(f"{name} is visible")
            print(f"{name} is visible")
            """

