from owlready2 import get_ontology, destroy_entity, Thing, OneOf, Not, FunctionalProperty, DataProperty
from pyparsing import one_of
from rdflib import RDF, Graph, Namespace, Literal

BASE = 'http://info216.uib.no/owlready2-lab/'
onto = get_ontology(BASE)

def clean_onto(onto):
    with onto:
        for ind in onto.individuals():
            destroy_entity(ind)
        for prop in onto.properties():
            destroy_entity(prop)
        for cls in onto.classes():
            destroy_entity(cls)

def onto2graph(onto):
    graph = Graph()
    onto.save('temp.nt', format='ntriples')
    graph.parse('temp.nt', format='ntriples')
    return graph

def print_onto(onto):
    g = onto2graph(onto)
    g.bind('', Namespace(BASE))
    print(g.serialize(format='ttl'))

clean_onto(onto)
_empty_graph = onto2graph(onto)

def print_onto2(onto):
    g = onto2graph(onto)
    for t in _empty_graph:
        if t in g:
            g.remove(t)
    g.bind('', Namespace(BASE))
    print(g.serialize(format='ttl'))

# A graduate is a student with at least one degree.
with onto:
    class Student(Thing): pass
    class Degree(Thing): pass
    class hasDegree(Student >> Degree): pass
    class Graduate(Student): 
        is_a = [hasDegree.some(Degree)]

    # A university graduate is a student whit at least one degree from a university.
    class University(Thing): pass
    class universityDegree(Degree >> University): pass
    class UniversityGraduate(Graduate):
        is_a = [hasDegree.some(universityDegree)]

    # A grade is either a A, B, C, D, E, or F

    class Grade(Thing):
        is_a = [OneOf(['A', 'B', 'C', 'D', 'E', 'F'])]

    # A straigh a student is a student with only A
    class hasGrade(Student >> Grade): pass
    class StraightAStudent(Student): 
        is_a = [hasGrade.only('A')]

    # a graduate has no F Grades
    class Graduate(Student):
        is_a = [hasDegree.some(Degree) & Not(hasGrade.some('F'))]

    # a student has some uniqe student number
    class hasStudnetNumber(Student >> int):
        is_a = [FunctionalProperty]

    # each student has exactly one average grade
    class hasAverageGrade(Student >> float): pass
    class Student(Thing):
        is_a = [Thing & hasAverageGrade.max(1, Grade)]

    # a course is either a bachelor, a master or a Ph.D course
    class Courses(Thing):
        is_a = [OneOf(['bachelor', 'master', 'PhD'])]
    class takesCourses(Student >> Courses): pass
    
    # a bachelor student takes only bachelor courses
    class BachelorCourses(Courses): 
        is_a = [takesCourses.only('bachelor')]
    class bachelorStudent(Student >> BachelorCourses): pass

    # a master student takes only master courser, exept for at most one bachelor course
    class MasterCourses(Courses):
        is_a = [takesCourses.only('master')]
    class masterStudent(Student >> Courses): 
        is_a = [MasterCourses & takesCourses.max(1, BachelorCourses)]

    # a PhD student takes only PhD courses, exept for two master courses
    # a PhD student cannot take any bachelor courses
    class PhDCourses(Courses):
        is_a = [takesCourses.only('PhD')]
    class PhDStudent(Student >> Courses):
        is_a = [PhDCourses & takesCourses.max(2, MasterCourses) & takesCourses.max(0, BachelorCourses)]


print_onto2(onto)