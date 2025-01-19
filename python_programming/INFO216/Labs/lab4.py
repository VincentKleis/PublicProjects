from SPARQLWrapper import SPARQLWrapper, JSON, POST, RDFXML
from rdflib import Graph

namespace = "kb"
sparql = SPARQLWrapper("http://192.168.0.108:9999/blazegraph/namespace/"+ namespace + "/sparql")

sparql.setReturnFormat(JSON)
sparql.setQuery("""
    SELECT * WHERE { ?s ?o ?p }
""")

results1 = sparql.query().convert()

# results of query 1. (to remove the hastags use the command to remove them, default is CTRL K + U consecetuvely in vscode. and CTRL K + C to add them back)
# for result in results1["results"]["bindings"]:
#     print(result["s"]["value"] + ", " + result["o"]["value"] + ", " + result["p"]["value"])

sparql.setQuery("""
    PREFIX ex: <http://example.org/>
    SELECT ?CadeInterest
    WHERE { ex:Cade foaf:interest ?CadeInterest }
""")

results2 = sparql.query().convert()

# results of query 2.
# for result in results2["results"]["bindings"]:
#     print("CadeInterest: " + result["CadeInterest"]["value"])

sparql.setQuery("""
    PREFIX ex: <http://example.org/>
    PREFIX schema: <http://schema.org/>
    SELECT ?emmaCity ?emmaCountry
    WHERE {
        ex:Emma schema:address ?address.
        ?address schema:city ?emmaCity.
        ?address schema:Country ?emmaCountry.
    }
    """)

results3 = sparql.query().convert()

# result of query 3.
# for result in results3["results"]["bindings"]:
#     print("EmmaCity: "+ result["emmaCity"]["value"] +", EmmaCountry: "+ result["emmaCountry"]["value"])

sparql.setQuery("""
    PREFIX schema: <http://schema.org/>
    SELECT ?person ?age
    WHERE {
        ?person foaf:age ?age
    FILTER(?age > 26)
    }""")

results4 = sparql.query().convert()

# result of qquery 4:
# print("Persons older than 26:")
# for result in results4["results"]["bindings"]:
#     print("Person: " + result["person"]["value"]+ ", Age: "+ result["age"]["value"])

sparql.setQuery("""
    PREFIX dbr: <http://dbpedia.org/resource/>
    SELECT ?Name ?value ?Degree
    WHERE {
        ?Name dbr:Education ?Education .
        ?Education ?value ?Degree .
    Filter(?value = dbr:Bachelor_of_Science || ?value = dbr:Master_of_Science)
    }""")

results5 = sparql.query().convert()

# results of query 5.
# print("People with a bachelors degree:")
# for result in results5["results"]["bindings"]:
#     print("Person: "+ result["Name"]["value"]+ ", Degree: " + result["value"]["value"] + ", Field: " + result["Degree"]["value"])

sparql.setMethod(POST)

sparql.setQuery("""
    PREFIX ex: <http://example.org/>
    PREFIX dbr: <http://dbpedia.org/resource/>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    DELETE DATA
    {
      ex:Cade foaf:interest dbr:Photographing.
    }""")

# Cade query 6:
# results6 = sparql.query()
# print(results6.response.read())


sparql.setQuery("""
    PREFIX ex: <http://example.org/>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dbr: <http://dbpedia.org/resource/>
    PREFIX schema: <https://schema.org/>
    INSERT DATA {
     ex:Siergo a foaf:Person ;
         dbr:Education [ dbr:Alumni dbr:University_of_Valencia ;
                            dbr:Expert dbr:Big_data,
                            dbr:Semantic_technologies,
                            dbr:Machine_learning ;
                     dbr:Graduation "2008";
                     dbr:Master_of_Science dbr:Computer_science ] ;
         foaf:firstName "Sergio" ;
         foaf:lastName "Pastor" ;
         schema:address [ a schema:address ;
                     schema:Country dbr:Spain ;
                     schema:city dbr:Valencia ;
                     schema:postalCode "46021";
                     schema:state dbr:Valencia ;
                     schema:streetAdress "4 Carrer del Serpis" ] .
            }
""")

# Siergo query 7:
# results7 = sparql.query()
# print(results7.response.read())

sparql.setQuery("""
    PREFIX dbr: <http://dbpedia.org/resource/>

    DELETE {?s ?p dbr:University_of_Valencia.}
    INSERT {?s ?p dbr:Universidad_de_Valencia.}
    WHERE {?s ?p dbr:University_of_Valencia.}
""")

# query 8:
# results8 = sparql.query()
# print(results8.response.read())


sparql.setQuery("""
    PREFIX ex: <http://example.org/>
    DESCRIBE ex:Siergo
    """)

sparql.setReturnFormat(RDFXML)
results9 = sparql.query().convert()
# query 9
# print(results9.serialize(format='turtle'))



sparql.setQuery("""
    PREFIX schema: <http://schema.org/>
    CONSTRUCT { [] ?city ?cityOf}
    WHERE {[] schema:address ?address.
          ?address schema:city ?city.
          ?address schema:Country ?cityOf}
""")

results10 = sparql.query().convert()
# query 10
print(results10.serialize(format='turtle'))
