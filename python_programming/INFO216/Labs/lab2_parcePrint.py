from doctest import Example
from rdflib import Graph, RDF
from rdflib.namespace import Namespace

g = Graph()
EX = Namespace('https://example.org/')

g.parse(location='Labs/turtleGraph.txt', format='turtle')
g.remove((EX.mary, None, None))
for RDF.subject, RDF.predicate, RDF.object in g:
    if 'emma' in RDF.subject or 'emma' in RDF.object:
        if 'cade' in RDF.subject or 'cade' in RDF.object or'mary' in RDF.subject or 'mary' in RDF.object:
            print(RDF.subject, RDF.predicate, RDF.object, end='\n\n', sep='  ')

print(g.serialize())