from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

op = webdriver.ChromeOptions()
op.add_argument('--headless')
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=op)

driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(3)
#print(drivers.find_element_by_id('content').text)
pageSource = driver.page_source
bs = BeautifulSoup(pageSource, 'html.parser')
print(bs.find(id='content').get_text())

driver.close()