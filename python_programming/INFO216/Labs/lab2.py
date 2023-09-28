from rdflib import Graph, Namespace, URIRef, BNode, Literal, RDFS, FOAF
from rdflib.namespace import Namespace, NamespaceManager
from rdflib.namespace import RDF, XSD, OWL

# from lab1
g = Graph()
a = RDF.type

EX = Namespace('http://example.org/')
DBO = Namespace('http://dbpedia.org/ontology/')
DBR = Namespace('http://dbpedia.org/resource/')

adress = BNode()

g.add((EX.Cade, a, FOAF.Person))
g.add((EX.Mary, a, FOAF.Person))
g.add((EX.Cade, DBR.Mariage, EX.Mary))
g.add((DBR.Paris, a, DBO.capital))
g.add((DBR.France, DBO.capital, DBR.Paris))
g.add((EX.Cade, EX.age, Literal(27)))
g.add((EX.Mary, EX.age, Literal(26)))
g.add((EX.Mary, EX.interest, DBR.Hiking))
g.add((EX.Mary, EX.interest, DBR.Chocolate))
g.add((EX.Mary, EX.interest, DBR.Biology))
g.add((EX.Mary, a, DBR.Student))
g.add((DBR.Paris, a, DBR.City))
g.add((DBR.Paris, RDFS.subClassOf, DBR.France))
g.add((EX.Cade, OWL.hasValue, DBR.Kindness))
g.add((EX.Mary, OWL.hasValue, DBR.Kindness))


# from lab 2
SCHM = Namespace('http://schema.org/')
NamespaceManager(g).bind("Example", EX)
NamespaceManager(g).bind('dbr', DBR)
NamespaceManager(g).bind('dbo', DBO)
g.bind('schm', SCHM)

adress_cade = BNode()

g.add((EX.Cade, SCHM.adress, adress_cade))
g.add((adress_cade, a, SCHM.adress))
g.add((adress_cade, SCHM.streetAdress, Literal('1516 Henry Street')))
g.add((adress_cade, SCHM.city, DBR.berkly))
g.add((adress_cade, SCHM.state, DBR.california))
g.add((adress_cade, SCHM.postalCode, Literal(94709, datatype=SCHM.postalCode)))
g.add((adress_cade, SCHM.Country, DBR.USA))

education_cade = BNode()

g.add((EX.Cade, DBR.Education, education_cade))
g.add((education_cade, DBR.Bachelor_of_Science, DBR.biology))
g.add((education_cade, DBR.Alumni, EX.University_of_California))
g.add((education_cade, EX.graduation, Literal(2011, datatype=XSD.gYear)))


g.add((EX.Cade, EX.interest, DBR.Birds))
g.add((EX.Cade, EX.interest, DBR.Ecology))
g.add((EX.Cade, EX.interest, DBR.Environment))
g.add((EX.Cade, EX.interest, DBR.Photographing))
g.add((EX.Cade, EX.interest, DBR.Traveling))

g.add((EX.Cade, DBR.Travel, DBR.Canada))
g.add((EX.Cade, DBR.Travel, DBR.France))

g.add((EX.Emma, a, FOAF.Person))
g.add((EX.Emma, EX.firstName, Literal('Emma')))
g.add((EX.Emma, EX.lastName, Literal('Dominguez')))

adress_emma = BNode()

g.add((EX.Emma, SCHM.adress, adress_emma))
g.add((adress_emma, a, SCHM.adress))
g.add((adress_emma, SCHM.streetAdress, Literal('Carrer de la Guardia Civil 20')))
g.add((adress_emma, SCHM.city, DBR.Valencia))
g.add((adress_emma, SCHM.state, DBR.Valencia))
g.add((adress_emma, SCHM.postalCode, Literal(46020, datatype=SCHM.postalCode)))
g.add((adress_emma, SCHM.Country, DBR.Spain))

education_emma = BNode()

g.add((EX.Emma, DBR.Education, education_emma))
g.add((education_emma, DBR.Master_of_Science, DBR.Chemestry))
g.add((education_emma, DBR.Alumni, EX.University_of_Valencia))
g.add((education_emma, EX.graduation, Literal(2015, datatype=XSD.gYear)))
g.add((education_emma, DBR.Expert, DBR.Waste_management))
g.add((education_emma, DBR.Expert, DBR.Toxic_waste))
g.add((education_emma, DBR.Expert, URIRef('http://dbpedia.org/resource/Category:Air_pollution')))

emma_interest = BNode()

g.add((EX.Emma, EX.interest, emma_interest))
g.add((emma_interest, EX.interest, DBR.Cycling)) 
g.add((emma_interest, EX.interest, DBR.Music))
g.add((emma_interest, EX.interest, DBR.Travel))

g.add((EX.Emma, DBR.Travel, DBR.Portugal))
g.add((EX.Emma, DBR.Travel, DBR.Italy))
g.add((EX.Emma, DBR.Travel, DBR.France))
g.add((EX.Emma, DBR.Travel, DBR.Germany))
g.add((EX.Emma, DBR.Travel, DBR.Denmark))
g.add((EX.Emma, DBR.Travel, DBR.Sweeden))

g.add((EX.Cade, EX.at, EX.Meeting))
g.add((EX.Emma, EX.at, EX.Meeting))
g.add((EX.Meeting, EX.hasPerson, EX.Cade))
g.add((EX.Meeting, EX.hasPerson, EX.Emma))
g.add((EX.Meeting, SCHM.location, DBR.Paris))
g.add((EX.Meeting, SCHM.date, Literal('2014/08', datatype=XSD.gYearMonth)))


print(g.serialize(destination='turtleGraph.txt', format='turtle'))
