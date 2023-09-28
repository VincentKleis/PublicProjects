import collections
from numpy import average
from rdflib import Graph, Literal, Namespace, BNode
from rdflib.namespace import RDF, OWL, RDFS
from rdflib.collection import Collection

g = Graph()
ex = Namespace("http://example.org/")
g.bind("ex", ex)
g.bind("owl", OWL)
a = RDF.type

# anyone who is a graduate has at least one degree
br = BNode()
g.add((br, RDF.type, OWL.Restriction))
g.add((br, OWL.onProperty, ex.degree))
g.add((br, OWL.minCardinality, Literal(1)))
bi = BNode()
Collection(g, bi, [ex.person, br])
g.add((ex.graduate, OWL.intersectionOf, bi))

# Continue here with the other statements:
# anyone who is a university graduate has atleast one degree form a university
br = BNode()
g.add((br, RDF.type, OWL.Restriction))
g.add((br, OWL.onProperty, ex.degree))
g.add((br, OWL.someValuesFrom, ex.university))
bi = BNode()
Collection(g, bi, [ex.graduate, br])
g.add((ex.universityGraduate, OWL.intersectionOf, bi))

# a grade is either an A, B, C, D, E or F
bi = BNode()
b1 = BNode()
Collection(g, b1, [Literal('A'), Literal('B'), Literal('C'), Literal('D'), Literal('E'), Literal('F')])
Collection(g, bi, [OWL.oneOf, b1])
g.add((ex.grade, OWL.equivalentClass, bi))

# a straight A student is a student that has only A grades
b1 = BNode()
b2 = BNode()
bi = BNode()

g.add((b1, RDF.type, OWL.Restriction))
g.add((b1, OWL.onProperty, ex.grade))
g.add((b1, OWL.allValuesFrom, Literal('A')))

g.add((b2, RDF.type, OWL.Restriction))
g.add((b2, OWL.onProperty, ex.grade))
g.add((b2, OWL.someValuesFrom, Literal('A')))


Collection(g, bi, [ex.student, b1, b2])
g.add((ex.straighAStudent, OWL.intersectionOf, bi))

# a graduate has no F grades
b1 = BNode()
g.add((b1, RDF.type, OWL.Restriction))
g.add((b1, OWL.onProperty, ex.grade))
g.add((b1, OWL.cardinality, Literal(0)))

b2 = BNode()
g.add((b2, RDF.type, OWL.Restriction))
g.add((b2, OWL.onProperty, ex.grade))
g.add((b2, OWL.allValuesFrom, Literal('F')))

bi = BNode()
Collection(g, bi, [b1, b2])
g.add((ex.hasGraduated, OWL.unionOf, bi))

# a student has a unique student number
g.add((ex.studentNumber, a, OWL.InverseFunctionalProperty))
g.add((ex.student, OWL.hasValue, ex.studnentNumber))

# each student has exaclty one average grade
bi = BNode()
b1 = BNode()

g.add((b1, a, OWL.Restriction))
g.add((b1, OWL.onProperties, ex.averageGrade))
g.add((b1, OWL.cardinality, Literal(1)))

Collection(g, bi, [OWL.hasValue, b1])

g.add((ex.student, OWL.unionOf, bi))

# a course is either a bachelor, master or Ph.D
bi = BNode()
b1 = BNode()
Collection(g, b1, [ex.bachelor, ex.master, ex.PhD])
Collection(g, bi, [OWL.oneOf, b1])
g.add((ex.course, RDFS.subClassOf, bi))

# a bachelor student takes only bachelor courses
g.add((ex.bachelorStudent, a, OWL.Restriction))
g.add((ex.bachelorStudent, OWL.onProperty, ex.student))
g.add((ex.bachelorStudent, OWL.allValuesFrom, ex.bachelorCourses))

# a master sutdent takes only master courses, except for at moste one bahcelor course
b1 = BNode()
b2 = BNode()
bi = BNode()

g.add((b1, a, OWL.Restriction))
g.add((b1, OWL.allValuesFrom, ex.masterCourses))

g.add((b2, a, OWL.Restriction))
g.add((b2, OWL.onProperty, ex.bachelorCourses))
g.add((b2, OWL.maxCardinality, Literal(1)))

Collection(g, bi, [ex.student, b1, b2])

g.add((ex.masterStuden, OWL.unionOf, bi))

# a Ph.D student takes only Ph.D courses, except for at most two masters courses
b1 = BNode()
b2 = BNode()
bi = BNode()

g.add((b1, a, OWL.Restriction))
g.add((b1, OWL.allValuesFrom, ex.PhDCourses))

g.add((b2, a, OWL.Restriction))
g.add((b2, OWL.onProperty, ex.masterCourses))
g.add((b2, OWL.maxCardinality, Literal(2)))

# Collection(g, bi, [ex.student, b1, b2])

# g.add((ex.PhDStudent, OWL.unionOf, bi))

# a Ph.D student cannot take any bachelor course
b3 = BNode()
g.add((b3, a, OWL.Restriction))
g.add((b3, OWL.onProperty, ex.bachelorCourses))
g.add((b3, OWL.cardinality, Literal(0)))

Collection(g, bi, [ex.student, b1, b2, b3])

g.add((ex.PhDStudent, OWL.unionOf, bi))

print(g.serialize(format="turtle"))