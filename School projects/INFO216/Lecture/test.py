from rdflib import Graph, RDF, RDFS, OWL, Namespace
import owlrl

EX = Namespace('http://example.org#')

g = Graph()
g.bind('', EX)
NS = {
    '': EX,
    'rdf': RDF,
    'rdfs': RDFS,
}
g.update("""
INSERT DATA {
    :Socrates rdf:type :Human .
    :Human rdfs:subClassOf :Mortal .

    :Socrates :husbandOf :Xantippe .
    :husbandOf rdfs:domain :Man .
    :husbandOf rdfs:range :Woman .
}
""", initNs=NS)

rdfs_engine = owlrl.RDFSClosure.RDFS_Semantics(g, False, False, False)
rdfs_engine.closure()
rdfs_engine.flush_stored_triples()

res = g.query("""
ASK { :Socrates rdf:type :Mortal . }
""", initNs=NS)
print(res.askAnswer)