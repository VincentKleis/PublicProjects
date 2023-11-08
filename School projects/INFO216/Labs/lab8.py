from rdflib import FOAF, RDFS, Graph, OWL, URIRef, RDF, Literal, Namespace

g = Graph()
g.parse(location='turtleGraph.txt', format='turtle')

EX = URIRef('http//example.org')
DBR = URIRef('http://dbpedia.org/resource/')
DBO = URIRef('http://dbpedia.org/ontology/')
GN = URIRef('http://sws.geonames.org/')
SCHM = URIRef('http://schema.org/')
AKT = URIRef('http://www.aktors.org/ontology/portal#')
VScard = URIRef('http://www.w3.org/2006/vcard/ns#')
ex = Namespace('http//example.org')

g.bind('',EX)
g.bind('dbr',DBR)
g.bind('gn', GN)
g.bind('schm', SCHM)
g.bind('akt', AKT)
g.bind('vscard', VScard)
g.bind('dbo', DBO)

NS = {
    '' : EX,
    'owl' : OWL,
    'rdf' : RDF,
    'rdfs' : RDFS,
    'dbr' : DBR,
    'dbo' : DBO,
    'gn' : GN,
    'schm' : SCHM,
    'akt' : AKT,
    'foaf' : FOAF,
    'vscard' : VScard,
}

g.update("""
INSERT DATA{
    :Cade owl:differentFrom :Emma .
    :USA rdf:type :Country .
    :USA owl:sameAs dbr:United_States .
    foaf:person owl:sameAs akt:Person .
    foaf:person owl:sameAs schm:Person .
    foaf:person owl:disjointWith :University .
    foaf:person owl:disjointWith :city .
    :city owl:disjointWith :University .
    schm:postalCode rdfs:subPropertyOf vscard:postal-code .
    schm:postalCode rdf:type owl:InverseFunctionalObjectProperty .
    schm:adress owl:sameAs foaf:base_near .
    schm:adress owl:inverseOf dbo:hometown .
}
""", initNs=NS)
g.add((ex.USA, OWL.sameAs, URIRef('http://sws.geonames.org/6252001')))

g.add((ex.Cade, ex.married, ex.Mary))
g.add((ex.Cade, ex.livesWith, ex.Mary))
g.add((ex.Cade, ex.sibling, ex.Andrew))
g.add((ex.Cade, ex.hasFather, ex.Bob))
g.add((ex.Bob, ex.fatherOf, ex.Cade))

g.add((ex.married, RDF.type, OWL.SymmetricProperty))