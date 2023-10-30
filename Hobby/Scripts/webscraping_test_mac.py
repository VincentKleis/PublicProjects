from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
chromedriver = "/Users/vincentkleis/Documents/Drivers/chromedriver"
driver = webdriver.Chrome(chromedriver)
sleep(2)
year = 0
while year == 0:
    date_option = input('for year press:1 and enter\nfor year and month press:2 and enter\nfor year, month and day press:3 and enter\n')
    if date_option == '1':
        year = input('what year would you like to search?:')
    elif date_option == '2':
        year = input('what year would you like to search?:')
        month = input('what month would you like to search?:')
    elif date_option == '3':
        year = input('what year would you like to search?:')
        month = input('what month would you like to search?:')
        day = input('what day would you like to search?:')
    else:
        print('sorry, that input is not valid')


driver.get(f'https://en.wikipedia.org/wiki/{year}')
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')
months_of_the_year = ['January', 'Februrary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
entries = soup.findAll('li')
entries_str = []
for entrie in entries:
    entries_str.append(entrie.prettify())

with open('HOBBY/TXT_files/test_output_2.html', 'w', encoding='utf8') as output:
    output.writelines(entries_str)

driver.quit()