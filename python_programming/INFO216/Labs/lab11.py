from tkinter import Button
from bs4 import BeautifulSoup as bs
from rdflib import Graph, Literal, URIRef, Namespace
from rdflib.namespace import RDF, OWL, SKOS, RDFS, XSD
import requests
import re

g = Graph()
a = RDF.type
ex = Namespace("http://example.org/")
g.bind("ex", ex)

# Download html from URL and parse it with BeautifulSoup.
url = "https://www.semanticscholar.org/topic/Knowledge-Graph/159858"
page = requests.get(url)
html = bs(page.content, features="html.parser")
# print(html.prettify())

# Find the html that surrounds all the papers
papers = html.find_all('div', attrs={'class': 'flex-container'})

# Iterate through each paper to make triples:
for paper in papers:
    # e.g selecting title. 
    title = paper.find('div', attrs={'class': 'timeline-paper-title'}).text
    pub_date = paper.find('li', attrs={'data-selenium-selector': 'paper-year'}).text
    authors = paper.find_all('span', attrs={'class': 'author-list'})
    author_list = []
    for author in authors:
        author = author.text
        author_list = author.replace('.', '').replace(', ', ',').replace(' ', '_').split(',')

    for author in author_list:
        paper_author = ex + URIRef(author)
        author_list[author_list.index(author)] = paper_author

    paper_title = ex + URIRef(title.replace(' ', '_').replace(':', '').replace('-', '').replace('.', '_'))
    paper_pup_date = Literal(pub_date)

    g.add((paper_title, a, ex.sicencPaper))
    g.add((paper_title, ex.pubDate, paper_pup_date))

    for paper_author in author_list:
        g.add((paper_title, ex.author, paper_author))

# ex 2

topic = html.find('h1', attrs={'class': 'entity-name'}).text
known_as = html.find_all('span', attrs={'class': 'entity-alias'})
known_as_list = []
for alias in known_as:
    alias = alias.text.lstrip(', ')
    known_as_list.append(alias.replace(' ', '_'))

related_topics = html.find_all('a', attrs={'class':'related-entity-link related-entity-list-item flex-row-vcenter'})
related_topics_list = []
for related_topic in related_topics:
    related_topics_list.append(related_topic.text.replace(' ', '_'))


topic = ex + URIRef(topic.replace(' ', '_'))
g.add((topic, a, SKOS.prefLabel))

for i in known_as_list:
    i = ex + URIRef(i)
    g.add((topic, SKOS.altLabel, i))

for i in related_topics_list:
    i = ex + URIRef(i)
    g.add((topic, SKOS.relatedMatch, i))

g.serialize('resultingGraph.ttl', format='ttl')
