import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import time
url = "https://angular-7bf43.web.app/auth"
uselector ='input[placeholder="Email-ID"]'
pselector = 'input[placeholder="Password"]'
bselector = 'button[type="submit"]'
username = 'jon@gmail.com'
password = '123123'
switchSelector = "button[type='submit']+p"
d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'browser':'ALL' }
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path='./chromedriver',options=chrome_options,desired_capabilities=d)



driver.get(url)
print(driver.find_element_by_css_selector("button[type='submit']+p").click())

uelem = driver.find_element_by_css_selector(uselector)
pelem = driver.find_element_by_css_selector(pselector)
belem = driver.find_element_by_css_selector(bselector)
uelem.send_keys(username)
pelem.send_keys(password)
belem.click()
time.sleep(8)
driver.get('https://angular-7bf43.web.app/')

# traverse

# driver.get('http://127.0.0.1:5500/tester/1.html')
# elems = driver.find_elements_by_tag_name('a')[2]

# print(elems.get_attribute('href'))
# driver.quit()

# res = driver.get('http://127.0.0.1:5500/tester/1.html')
# print(driver.page_source)
# log = driver.get_log('performance')
# print (str(performance_log).strip('[]'))
