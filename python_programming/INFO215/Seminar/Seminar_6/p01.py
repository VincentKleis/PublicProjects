from selenium import webdriver
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

print(driver.find_element(By.ID, 'content').text)

driver.close()
