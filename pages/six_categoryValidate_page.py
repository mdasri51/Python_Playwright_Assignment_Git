from utils.config import BASEURL
from playwright.sync_api import Page
from playwright.sync_api import expect
import logging

class Six_CategoryPage:

    def __init__(self, page):   
        self.page = page
    
    def category_validate(self):

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
            logging.info(f"{name} is visible")
            print(f"{name} is visible")