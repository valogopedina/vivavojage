# This file is responsible to describe the methods
import bot.vivavoyage.constants as const
import os
from selenium import webdriver
from selenium.webdriver.support.select import Select

class VivaVoyage(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(VivaVoyage, self).__init__()
        self.implicitly_wait(15)  # wait until the element is available on the website. Less if the element is already there
        self.maximize_window()  # clearer look at the website

    def __exit__(self, exc_type, exc_val, exc_tb):  # avoid browser to still open
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def destination(self, place):
        search_field = Select(self.find_element_by_id('destinationId'))
        print(search_field)
        result = search_field.select_by_visible_text("Caribbean")
        print(result)
        # search_field.clear()
        # search_field.send_keys(place)

    def advance_search(self):
        advance_search = self.find_element_by_id('advancedSearchLink')
        advance_search.click()
