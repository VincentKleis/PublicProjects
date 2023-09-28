# ex1
import hashlib as hl
import random


graph = [("A","B"), ("A","C"), ("B","A"), ("C","A"), ("B","C")]

def remove_node(node:str, graph: list):
    result = []
    for i in graph:
        x, y = i
        if node != x and node != y:
            result.append(i)
    return result

graph = remove_node("A", graph)
print(graph)

# ex2
class Graph:
    graph = dict()

    def add_edge(self, node, neighbour):
        self.graph.setdefault(node, []).append(neighbour)
        self.graph.setdefault(neighbour, []).append(node)

    def get_neighbours(self, node):
        if node in self.graph:
            return self.graph[node]
        return []

    def remove_node(self, node):
        neighbours = self.get_neighbours(node)
        for i in neighbours:
            # gets a list of nodes that every neighbour node is connected to
            edges = self.graph[i]
            for edge in edges:
                if node == edge:
                    edges.pop(edges.index(edge))
            # re-assinges the modified edges to the list of edges for the nodes
            self.graph[i] = edges
        # removes the node and all it's edges
        self.graph.pop(node)
        

graph = Graph()
graph.add_edge("A","B")
graph.add_edge("A","C")
graph.add_edge("B","A")
graph.add_edge("C","A")
graph.add_edge("B","C")
graph.remove_node("A")
print(graph.graph)

# ex3
class Course:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def hash_it(self):
        salt = random.randint(0, 10000)
        hash_value = str(self.title) + str(self.year) + str(salt)
        self.hash_value = hl.sha1(hash_value.encode('utf-8')).hexdigest()
    
    def print_it(self):
        print(self.hash_value)

my_course = Course('INFO125', 2019)
my_course.hash_it()
my_course.print_it()