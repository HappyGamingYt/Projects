#Selenium Webdriver must be installed for this to work

import time;
from selenium import webdriver;

#time to refresh page (seconds)
Timer = 10

#youtube link
link = 'https://www.youtube.com/watch?v=jojHTA_K2bY&t=11s'

#number of views
views = 1000

driver = webdriver.Chrome('webdrivers\chromedriver.exe')
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
  
