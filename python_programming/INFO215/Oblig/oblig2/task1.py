from urllib.request import urlopen
from bs4 import BeautifulSoup
# page url
url = "https://en.wikipedia.org/wiki/Star_Wars:_The_Rise_of_Skywalker"

html = urlopen(url)

# the page as a soup object
soup = BeautifulSoup(html, 'html.parser')

# 1.1

links = []

# gets every link on the page
for link in soup.find_all('a'):
    links.append((link.get('href'), link.get('title')))

# clean the list of links for None values
links = [x for x in links if x[0] != None]

url_start = url[:24]

# adds url_start to the start of every link starting with /wiki/
links = [(url_start+x[0], x[1]) if x[0][:6]=='/wiki/' else x for x in links]

# replaces second element of the tuples if None with Unknown
links = [(x[0], 'Unknown') if x[1] == None else x for x in links]

# add https: to the beginning of links that start with //
links = [('https:'+x[0], x[1]) if x[0][:2] == '//' else x for x in links]

print('links:\n', *links, sep='\n')

# 1.2
images = []
for image in soup.find_all('img'):
    images.append(image.get('src'))

# add https://en.wikipedia.org/ to the beginning of links that start with /static
images = ['https://en.wikipedia.org/'+x if x[:7] == '/static' else x for x in images ]

# add https: to the beginning of links that start with //
images = ['https:'+x if x[:2] == '//' else x for x in images]

print('\nimages:',*images, sep='\n')