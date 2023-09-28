from cgitb import html
from bs4 import BeautifulSoup
from requests import get

url = 'https://mangabuddy.com/mbx10-one-piece-digital-colored-comics/vol-12-chapter-106-the-town-of-welcoming'

html_page = get(url)

soup = BeautifulSoup(html_page.content, 'html.parser')

img = soup.find_all('img')

print(img)