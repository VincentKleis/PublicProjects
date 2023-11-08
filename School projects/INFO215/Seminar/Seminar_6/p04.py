from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

op = webdriver.ChromeOptions()
op.add_argument('--headless')
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=op)

driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'loadedButton')))
except TimeoutException:
    print('Did not find the element')
finally:
    print(driver.find_element(By.ID, 'content').text)
    driver.close()
