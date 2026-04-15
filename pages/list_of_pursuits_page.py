

from playwright.sync_api import Page
from playwright.sync_api import expect


class List_of_pursuitsPage:

    def __init__(self, page):   
        self.page = page
    
    def pursuite_option(self):
        expect(self.page.get_by_text("List of all pursuits")).to_be_visible()   

        #//h3[@class="sc-dLMFT ljnIHJ pursuit-table-title pursuit-table-title"]