from argparse import Namespace
import requests
import spotlight
from rdflib import FOAF, Graph, RDF, Namespace, URIRef, Literal

g = Graph()

ex = Namespace('http://example.org/')

r = requests.get('http://api.open-notify.org/astros.json')

SERVER = "https://api.dbpedia-spotlight.org/en/annotate"

g.bind("ex", ex)

people = r.json()["people"]
crews = []

for item in people:
    craft = item["craft"].replace(' ', '_')
    annotated_craft = spotlight.annotate(SERVER, craft)
    craft_uri = annotated_craft[0]["URI"]
    craft_type = annotated_craft[0]["types"]
    crew = item["name"].replace(' ', '_')
    crew_uri = URIRef(ex + crew)
    print(crew)
    try:
        annotated_crew = spotlight.annotate(SERVER, crew)
    except:
        ...

    g.add((craft_uri, RDF.type, Literal(craft_type, datatype="str")))
    g.add((crew_uri, RDF.type, ex.Crew))
    g.add((crew_uri, ex.CrewIn, craft_uri))
    crews.append((craft, crew))

for i in crews:
    for j in crews:
        if i[0] == j[0] and i[1] != j[1]:
            crew_i = URIRef(ex + i[1])
            crew_j = URIRef(ex + j[1])

            g.add((crew_i, FOAF.knows, crew_j))

print(g.serialize(format='json-ld'))