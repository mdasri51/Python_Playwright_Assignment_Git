from utils.config import BASEURL
from playwright.sync_api import Page
from playwright.sync_api import expect
import logging

class CardCountDisplay:

    def __init__(self, page):   
        self.page = page
    
    def card_print_value(self):

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


            