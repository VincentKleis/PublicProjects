from rdflib import Namespace, FOAF, Graph, RDF, Literal, RDFS

g = Graph()
a = RDF.type

EX = Namespace('https://example.org/')
DBO = Namespace('https://dbpedia.org/ontology/')
DBP = Namespace('https://dbpedia.org/page/')

g.add((EX.cade, DBP.Mariage, EX.mary))
g.add((DBP.Paris, DBO.capital, DBP.France))
g.add((EX.cade, FOAF.age, Literal(27)))
g.add((EX.mary, FOAF.age, Literal(26)))
g.add((EX.mary, FOAF.interest, DBP.Hiking))
g.add((EX.mary, FOAF.interest, DBP.Chocolate))
g.add((EX.mary, FOAF.interest, DBP.Biology))
g.add((EX.mary, a, DBP.Student))
g.add((DBP.Paris, a, DBP.City))
g.add((DBP.Paris, RDFS.subClassOf, DBP.France))
g.add((EX.cade, a, DBP.Kindness))
g.add((EX.mary, a, DBP.Kindness))

g.namespace_manager.bind(EX, namespace='https://example.org/')
g.namespace_manager.bind(DBO, namespace='https://dbpedia.org/ontology/')
g.namespace_manager.bind(DBP, namespace='https://dbpedia.org/page/')

print(g.serialize())