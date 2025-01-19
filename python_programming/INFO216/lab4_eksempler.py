#Delete cades photography interest
sparql.setQuery("""
    PREFIX ex: <http://example.org/>
    DELETE DATA {
        ex:Cade ex:interest ex:Photography .
        } 
        """)
sparql.setMethod(POST)
results = sparql.query()
print(results.response.read())

###

# Describe Sergio
sparql.setReturnFormat(TURTLE)
sparql.setQuery("""
    PREFIX ex: <http://example.org/>
    DESCRIBE ex:Sergio ?o
    WHERE {
        ex:Sergio ?p ?o .
        ?o ?p2 ?o2 .
    }
    """)
results = sparql.query().convert()
print(results.serialize(format='turtle'))

###

#for abstrakte ting som "capital"
dbo = Namespace('https://dbpedia.org/ontology/') 
#for konkrete ting som "Paris"
dbr = Namespace('https://dbpedia.org/page/')

###

# Solution 5 using existing vocabularies for address 

# (in this case https://schema.org/PostalAddress from schema.org). 
# Also using existing ontology for places like California. (like http://dbpedia.org/resource/California from dbpedia.org)

schema = Namespace("https://schema.org/")
dbp = Namespace("https://dpbedia.org/resource/")

g.add((ex.Cade_Tracey, schema.address, ex.CadeAddress))
g.add((ex.CadeAddress, RDF.type, 

###

# Construct that any city is in the country in an address
sparql.setQuery("""
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
    PREFIX ex: <http://example.org/>
    CONSTRUCT {?city ex:locatedIn ?country}
    Where {
        ?s rdf:type ex:Address .
        ?s ex:city ?city .
        ?s ex:country ?country.
        }
    """)
sparql.setReturnFormat(TURTLE)
results = sparql.query().convert()
print(results.serialize(format='turtle'))
