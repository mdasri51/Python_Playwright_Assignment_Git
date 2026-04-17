from playwright.sync_api import expect
from playwright.sync_api import Page
from playwright.sync_api import Locator
import time
import logging

class CreatePursuitsPage:

    def __init__(self, page):   
        self.page = page

    def new_create_pursuits_page(self):
        self.page.locator("//button[@class='_menuItem_1tt27_90']").click()
        self.page.locator("//div[normalize-space()='Create Pursuit']").click() 


    def validate_button_atbottom(self):
        cancel_button= self.page.get_by_role("button", name="Cancel", exact=True)
        create_button= self.page.get_by_role("button", name="Create", exact=True)

        expect(cancel_button).to_be_visible(timeout=10000)
        expect(create_button).to_be_visible(timeout=10000)

        print("Cancel button is present")
        print("Create button is present")

    def validate_mandatory_field_erros(self):
        create_button= self.page.get_by_role("button", name="Create", exact=True)
        create_button.click()
        self.page.wait_for_timeout(1500)

        error_fields = self.page.locator("//div[@class='ant-form-item-explain-error']")
        error_count = error_fields.count()

        print("Error field count : ", error_count)
        assert error_count == 9, f"Expected 9 Errors, but found {error_count}"

    def add_new_client(self):
         self.page.wait_for_timeout(5000)
         self.page.wait_for_load_state("load")
         self.page.locator("//span[text()='Add New Client']").click()

        #adding new client name
         #self.page.wait_for_load_state("load")
         self.page.locator("//input[@placeholder='Add New Client']").fill("Mayuri Dasri")

        #selecting value fron dropdown from industry
         industry_input = self.page.locator("#rc_select_14")
         industry_input.wait_for(state="visible")
         industry_input.click()

         #self.page.wait_for_timeout(5000)
         industry_dd = self.page.locator("//div[@title='Consumer']")
         industry_dd.wait_for(state="visible")
         industry_dd.click()

         sector_input=self.page.locator("//input[@id='rc_select_15']")
         sector_input.wait_for(state="visible")
         sector_input.click()
         
         sector_dd=self.page.locator("//div[@title='Automotive, Transportation']")
         sector_dd.wait_for(state="visible")
         sector_dd.click()


         self.page.locator("//span[normalize-space()='Save']").click()
         self.page.wait_for_timeout(1500)

         time.sleep(20)

    def fill_pursuit_form(self, pursuit_name: str, country: str, jupiter_id: str):
        
        self.page.locator("//input[@placeholder='Enter pursuit name']").fill(pursuit_name)
        
        self.page.locator("//input[@id='rc_select_8']").click()
        self.page.locator("//div[@title='Assets']").click()

        self.page.locator("//input[@aria-controls='rc_select_9_list']").click()
        self.page.locator("//div[@title='Test Automation']").click()

        self.page.locator("//input[@id='rc_select_10']").fill(country)
        self.page.locator("//div[@title='India']").click()

        self.page.locator("//input[@id='rc_select_13']").click()
        self.page.locator("//div[@title='NA']").click()

        self.page.locator("//input[@placeholder='Start date']").click()
        self.page.locator("//td[@title='2026-04-17']").click()
        self.page.locator("//td[@title='2026-05-30']").click()
        self.page.get_by_role("button", name="Done").click()

        self.page.locator("//input[@placeholder='Enter jupiter ID']").fill(jupiter_id)


    def create_pursuit(self):
        self.page.locator("//span[normalize-space()='Create']").click()
        self.page.wait_for_timeout(2000)

    def validate_success_message(self):
        success_msg = self.page.locator("text='New pursuit is created'")
        expect(success_msg).to_be_visible()
        expect(success_msg).to_have_text("New pursuit is created")

