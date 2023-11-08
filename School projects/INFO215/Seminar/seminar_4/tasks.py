from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re
url_abbey = "https://simple.wikipedia.org/wiki/Abbey_Road"

html_abbey = urlopen(url_abbey)

bs_abbey = BeautifulSoup(html_abbey, 'html.parser')

# task 1
for line in bs_abbey.find_all('a'):
    try:
        # remove comment to use
        # print(line.get('href'))
        ...
    except:
        continue

# task 2
internal_urls = []
for link in bs_abbey.find_all('a', href=re.compile('^(/wiki/)')):
    try:
        internal_urls.append(link['href'])
    except:
        continue

# print(*internal_urls, sep='\n')

# task 3
domain = 'https://en.wikipedia.org'
for url in internal_urls:
    index = internal_urls.index(url)
    url = urljoin(domain, url)

    internal_urls[index]=url

# print(*internal_urls, sep='\n')

# task 4

url_beatles = 'https://simple.wikipedia.org/wiki/Category:The_Beatles_albums'

html_beatles = urlopen(url_beatles)

bs_beatles = BeautifulSoup(html_beatles, 'html.parser')
albums = bs_beatles.find('div', {'class': 'mw-category mw-category-columns'})

for link in albums.find_all('a'):
    print(link['href'])