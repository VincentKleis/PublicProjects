import turtle
from rdflib import PROV, Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, XSD
import xml.etree.ElementTree as ET
import requests
import re

g = Graph()
ex = Namespace("http://example.org/")
prov = Namespace("http://www.w3.org/ns/prov#")
g.bind("ex", ex)
g.bind("prov", prov)


# URL of xml data
url = 'http://feeds.bbci.co.uk/news/rss.xml'

# Retrieve the xml data from the web-url.
resp = requests.get(url)

# Creating an ElementTree from the response content
tree = ET.ElementTree(ET.fromstring(resp.content))
tree2 = ET.parse('writers.xml')

# Or saving the xml data to a .xml file and creating a tree from this
# with open('news.xml', 'wb') as f:
#     f.write(resp.content)

root = tree.getroot()
root2 = tree2.getroot()
writer_dict = {}
for lines in root2.findall('./news_publisher/journalist'):
    whenWriting = lines.attrib
    whenWritingList = whenWriting['whenWriting'].split(', ')
    writerFName = lines.find('./firstname').text
    writerLName = lines.find('./lastname').text
    for i in whenWritingList:
        writer_dict[i] = writerFName + writerLName

g.add((ex.BBC, RDF.type, PROV.Entity))

for item in root.findall('./channel/item'):
    news_id = item.find('./guid').text
    news_id = URIRef(news_id)
    title = item.find('./title').text
    description = item.find('./description').text
    link = item.find('./link').text
    pub_date = item.find('./pubDate').text
    writer = writer_dict[pub_date[:3]]
    writer = URIRef(ex + writer.replace(' ', '_'))
    g.add((ex.BBC, ex.hasEntry, news_id))
    g.add((news_id, RDF.type, PROV.entity))
    g.add((news_id, ex.hasTitle, Literal(title, datatype='str')))
    g.add((news_id, ex.hasDescription, Literal(description, datatype='str')))
    g.add((news_id, ex.hasLink, Literal(link, datatype='link')))
    g.add((news_id, ex.hasPubDate, Literal(pub_date, datatype=XSD.date)))
    g.add((news_id, PROV.wasAttributedTo, writer))
    g.add((writer, RDF.type, PROV.agent))
    g.add((writer, PROV.actedOnBehalfOf, ex.BBC))    

g.serialize('news.ttl',format='turtle')
