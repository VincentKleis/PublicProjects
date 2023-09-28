from rdflib import FOAF, OWL, RDF, RDFS, Graph, URIRef, Namespace
import owlrl

g = Graph()

EX = URIRef('http://example.org/')
DBR = URIRef('http://dbpedia.org/resource/')
SCHM = URIRef('http://schema.org/')
ex = Namespace('http://example.org/')

g.bind('', EX)
g.bind('dbr', DBR)
g.bind('schm', SCHM)

NS = {
    '':EX,
    'rdf':RDF,
    'rdfs':RDFS,
    'dbr':DBR,
    'schm':SCHM,
    'owl':OWL,
    'foaf':FOAF
}

g.update("""
INSERT DATA{
    :University_of_California rdf:type :University .
    :University_of_Valencia rdf:type :University .
    :University rdfs:subClassOf :Higher_Education_Institute .
    :expertise rdfs:domain foaf:Person .
    :expertise rdfs:range :Subject .
    :degreeSubject rdfs:subPropertyOf :expertise .
    :graduation rdfs:domain foaf:Person .
    :graduation rdfs:range :Higher_Education_Institute .
    :degreeFrom rdfs:subPropertyOf :graduation .
    :Student rdfs:subClassOf foaf:Person .
    :Knows rdfs:subPropertyOf :Married .
    rdfs:label rdfs:subPropertyOf :Name .

    :degree rdfs:subClassOf :Graduation .
    :capital rdfs:subClassOf :city .
}
""", initNs=NS)

g.parse(location="turtleGraph.txt", format="turtle")

rdfs = owlrl.RDFSClosure.RDFS_Semantics(g, False, False, False)
rdfs.closure()
rdfs.flush_stored_triples()

meeting_trpls = g.query("""
CONSTRUCT {
?person1 :knows ?person2 .
?person1 dbr:Travel ?city .
}
WHERE {
?person1 :at ?Meeting .
?Meeting schm:location ?city .
?Meeting :hasPerson ?person2
} 
""", initNs=NS)

for triple in meeting_trpls:
    if triple[0] != triple[2]:
        g.add((triple))

universities = g.query("""
ASK {
    :University_of_California rdf:type :Higher_Education_Institute .
    :University_of_Valencia rdf:type :Higher_Education_Institute .
}
""", initNs=NS)
persons = g.query("""
ASK {
    :Cade rdf:type foaf:Person.
    :Emma rdf:type foaf:Person.
    :Mary rdf:type foaf:Person.
}
""", initNs=NS)


g.serialize('turtleGraph.txt', format='turtle')

print(bool(universities))
print(bool(persons))
