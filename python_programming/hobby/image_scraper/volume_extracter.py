from bs4 import BeautifulSoup
from requests import get

url = 'https://onepiece.fandom.com/wiki/Chapters_and_Volumes/Volumes'

html_page = get(url)

soup = BeautifulSoup(html_page.content, 'html.parser')

warning = soup.find('main')

div = warning.find('div', 'mw-parser-output')

tables = div.find_all('table')

tables.pop(0)

volumes = []

for table in tables:
    name = table.find('span')
    title = table.find('td')
    if name is None:
        continue
    volumes.append(name.text)

print(volumes)
