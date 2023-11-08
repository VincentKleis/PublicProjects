from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

op = webdriver.ChromeOptions()
op.add_argument('--headless')
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=op)

url = 'http://www.webscrapingfordatascience.com/complexjavascript/'
driver.get(url)
time.sleep(3)
for quote in driver.find_elements(By.CLASS_NAME, 'quote'):
    print(quote.text)

input('Press ENTER to close the automated browser')
driver.quit()