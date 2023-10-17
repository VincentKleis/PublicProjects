import pandas as pd
import rdflib

from rdflib import FOAF, Graph, Namespace, URIRef, Literal, BNode
from rdflib.namespace import RDF, RDFS, XSD

ex = Namespace("http://example.org/")
dbr = Namespace("http://dbpedia.org/resource/")
sem = Namespace("http://semanticweb.cs.vu.nl/2009/11/sem/")
tl = Namespace("http://purl.org/NET/c4dm/timeline.owl#")

g = Graph()
g.bind("ex", ex)
g.bind("dbr", dbr)
g.bind("sem", sem)
g.bind("tl", tl)

# windows
df = pd.read_csv("G:\My Drive\Python_learning\Info216\\russia-investigation.csv")
# mac
# df = pd.read_csv("/Volumes/GoogleDrive/My Drive/Python_learning/Info216/russia-investigation.csv")
# We need to correct the type of the columns in the DataFrame, as Pandas assigns an incorrect type when it reads the file (for me at least). 
# We use .astype("str") to convert the content of the columns to a string.
df["name"] = df["name"].astype("str")
df["type"] = df["type"].astype("str")

# iterrows creates an iterable object (list of rows)
for index, row in df.iterrows():
	# Do something here to add the content of the row to the graph
    # name of the investigation
    investi_name = row["investigation"]
    investigation = URIRef(ex + investi_name)
    g.add((investigation, RDF.type, sem.Event))

    # start adding the date information to the investigation
    investi_start = row["investigation-start"]
    investi_day = row["investigation-days"]
    investi_end = row["investigation-end"]

    g.add((investigation, sem.hasBeginTimeStamp, Literal(investi_start, datatype=XSD.date)))
    g.add((investigation, tl.duationInt, Literal(investi_day, datatype="int")))
    g.add((investigation, sem.hasEndTimeStamp, Literal(investi_end, datatype=XSD.date)))

    # sub investigations
    indictment_dur = row["indictment-days "]
    investi_type = row["type"]
    overturned = row["overturned"]
    pardon = row["pardoned"]
    cp_date = row["cp-date"]
    cp_days = row["cp-days"]
    name = row["name"]
    name = name.replace(' ', '_')
    name = name.replace('.', '')
    name = name.replace('"', "'")

    sub_investi = URIRef(ex + name + f'_{investi_type}')
    
    g.add((sub_investi, RDF.type, sem.Event))
    g.add((investigation, sem.hasSubEvent, sub_investi))
    g.add((sub_investi, sem.hasActor, Literal(name, datatype="str")))
    g.add((sub_investi, ex.IndictmenDays, Literal(indictment_dur, datatype="float")))
    g.add((sub_investi, ex.Overturned, Literal(overturned, datatype="bool")))
    g.add((sub_investi, ex.Pardon, Literal(pardon, datatype="bool")))
    g.add((sub_investi, sem.hasTime, Literal(cp_date, datatype=XSD.date)))
    g.add((sub_investi, tl.durationInt, Literal(cp_days, datatype="int")))

g.serialize("output.ttl", format="ttl")
