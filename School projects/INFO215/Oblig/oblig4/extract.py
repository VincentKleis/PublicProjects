# requires you to do $pip install newspaper3k
from newspaper import Article
from requests import get
from zipfile import ZipFile
from io import BytesIO
url = 'http://data.gdeltproject.org/gdeltv2/lastupdate.txt'

article = Article(url)

article.download()

zips = article.html

zips = zips.split('\n')

things = [thing.split(' ') for thing in zips]

links = []
for thing in things:
    if len(thing)>2:
        links.append(thing[2])

print(links)

# Method inspired by https://stackoverflow.com/questions/9419162/download-returned-zip-file-from-url
zip_files = [get(link).content for link in links]
zip_files = [BytesIO(file) for file in zip_files]
zip_files = [ZipFile(file, 'r') for file in zip_files]

for file in zip_files:
    # since i'm only expecting zips of singular csv files i'm always extracting the first file
    name = file.namelist()[0]
    file.extract(name)