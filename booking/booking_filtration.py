#This file will include a class with instance methods.
#That will be responsible to interact with our website
#After we have some results, to apply filtrations.
from selenium.webdriver.remote.webdriver import WebDriver

class BookingFiltration:
    def __init__(self, driver:WebDriver): #constractor
        self.driver = driver


    def apply_star_rating(self, *star_values): #* used because you are passing as attribute a list
        star_filtration_box = self.driver.find_element_by_id('filter_class')
        star_child_elements = star_filtration_box.find_elements_by_css_selector('*')
        #* to filter all the elements

        for star_value in star_values:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                #strip delete all the white spaces
                    star_element.click()