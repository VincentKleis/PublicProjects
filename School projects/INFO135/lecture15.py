import xml.etree.ElementTree as ET
import json
import requests

url = 'https://cutt.ly/movie-xml'
file = requests.get(url)

print(file.content)

with open('movie.xml', 'w') as movie:
    movie.write(file.content)


tree = ET.parse(file)

root = tree.getroot()
for branch in root:
    print(f'{branch.tag} \t:{branch.attrib}')