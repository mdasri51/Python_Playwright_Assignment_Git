from utils.config import BASEURL
from playwright.sync_api import expect
import pages
import time

class DemandPursuits:

    def __init__(self, page):   #calls like constructor
        self.page = page 

    #navigation to demand and search new pursuit by name, jupiter Id etc
    def navigation_demandPursuit(self, cName):
        self.page.locator("//button[@class='_menuItem_1tt27_90']").click()
        self.page.wait_for_timeout(5000)
        self.page.locator("//div[text()='Create Pursuit']").click()
        self.page.wait_for_timeout(5000)
        self.page.locator("//button[@class='_menuItem_1tt27_90']").click()
        self.page.wait_for_timeout(5000)
        self.page.locator("//div[text()='Demand Pursuits']").click()
        time.sleep(10)

        self.page.locator("//span[@class='anticon anticon-search pursuit-search-icon']").click()
        self.page.locator("input[placeholder='Search Client, Pursuit, JupiterID']").fill(cName)
        self.page.wait_for_timeout(5000)
        
        #row = self.page.locator("tr.ant-table-row", has_text=f"{cName}")
        #expect(row).to_be_visible()
        #row.click()
        #self.page.wait_for_timeout(5000)


        latest_client =self.page.locator("//table//tr[2]", has_text=f"{cName}")
        expect(latest_client).to_be_visible()
        latest_client.click()
        self.page.wait_for_timeout(5000)


        categories = [
            ("Pursuit ID","//span[text()='Pursuit ID']/following-sibling::div/div"),
            ("Start Date","//span[text()='Start Date']/following-sibling::div/div"),
            ("End Date","//span[text()='End Date']/following-sibling::div/div"),
            ("Proposal Type","//span[text()='Proposal Type']/following-sibling::div/div"),
            ("Billing Arrangement","//span[text()='Billing Arrangement']/following-sibling::div/div"),
            ("Industry","//span[text()='Industry']/following-sibling::div/div"),
            ("Sector","//span[text()='Sector']/following-sibling::div/div"),
            ("Pursuit Creator","//span[text()='Pursuit Creator']/following-sibling::div/div"),
            ("Type of Project","//span[text()='Type of Project']/following-sibling::div/div"),
            ("Jupiter ID","//span[text()='Jupiter ID']/following-sibling::div/div"),
            ("Country","//span[text()='Country']/following-sibling::div/div"),
            ("Utilizing AI Assist","//span[text()='Utilizing AI Assist']/following-sibling::div/div"),
        ]
        
        for name, xpath in categories:
            locator  = self.page.locator(xpath)
            values = locator.inner_text()
            print(f"{name} has {values} record")


