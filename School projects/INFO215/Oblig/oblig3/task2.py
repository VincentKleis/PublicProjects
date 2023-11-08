from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from random import randint

op = webdriver.ChromeOptions()
op.add_argument('--headless')
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=op)

url = 'https://twitter.com/search?q=%23Winter'
i = 0

while i < 6:

    driver.get(url)
    time.sleep(3)

    elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/hashtag')]")
    hashtags = [element.get_attribute('href') for element in elements]

    # select a hastag with random index in the range 0 ot len(hastag)-1
    rand_hash = hashtags[randint(0,len(hashtags)-1)]

    url = rand_hash
    i += 1
    print(i, url)
