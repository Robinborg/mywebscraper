'''My first attempt at a webscraper'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re


# path = input("Copy paste website:\n")
path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(path)

#Website
driver.get("http://www.kaihdinliikesandberg.fi/")
w_page = driver.page_source
#Search pattern
emails = re.findall(r"[a-z0-9\.\-+_]+@a-z0-9\.\-+_]+\.com", w_page, re.I)

for email in emails:
    print(email)


#Work the website to parse infomration
# for a in driver.find_elements_by_xpath('.//a'):
#     al = a.get_attribute('href')
    #Check if the contactpage is among the sites 

    #Store all the possible pages emails

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located((By.LINK_TEXT, "yhteystiedot"))
#     )
#     element.click()
#     print(element.title)
# except: 
#     driver.quit() 

