from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://twitter.com/search?q=Sweden')
bs = BeautifulSoup(html, 'html.parser')

print(bs.get_text())

