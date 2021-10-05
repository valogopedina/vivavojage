import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()

driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
driver.implicitly_wait(5)
try:
    no_button = driver.find_element_by_class_name('at-cm-no-button') #intera classe era at-cv-button at-cv-lightbox-yesno at-cm-no-button ma si puo' manipolare
    no_button.click() #clicca su un bottone in un popup che puo' comparire prima del form
except:
    print('No element found with that class. Skipping...')

sum1 = driver.find_element_by_id('sum1')
sum2 = driver.find_element_by_id('sum2')

sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5) ##sum1.send_keys(15)
sum2.send_keys(15)

#btn = driver.find_element_by_class_name('btn btn-default')
btn = driver.find_element_by_css_selector('button[onclick="return total()"]')
btn.click()


