# 1.
# of the three options:
# a) { (A,B), (B,C), (B,D), (C,A), (C,D) }
# b) { (A,B), (B,C), (B,D), (C,A), (D,A) }
# c) { (A,B), (B,C), (C,B), (C,A), (D,A) }
# d) { (A,B), (B,C), (A,C), (C,A), (D,B) }
# e) None of the above

# "b)" represents every edge in the graph drawn in the first question

# 2.
from operator import length_hint
from re import L


COLUMNS = "abcde"
NUM_QUEENS = len(COLUMNS)
ACCEPT = 1
CONTINUE = 2
ABANDON = 3
all_solutions = []

num_solve = 0


def extend(partial_sol: str):
    results = []
    row = len(partial_sol) + 1

    for column in COLUMNS:
        new_solution = list(partial_sol)
        new_solution.append(column + str(row))
        results.append(new_solution)

    return results


def attacks(p1, p2):
    column1 = COLUMNS.index(p1[0]) + 1
    row1 = int(p1[1])

    column2 = COLUMNS.index(p2[0]) + 1
    row2 = int(p2[1])

    return row1 == row2 or column1 == column2 or abs(row1-row2) == abs(column1-column2)


def examine(partial_sol):
    for i in range(len(partial_sol)):
        for j in range(i + 1, len(partial_sol)):
            if attacks(partial_sol[i], partial_sol[j]):
                return ABANDON

    if len(partial_sol) == NUM_QUEENS:
        return ACCEPT
    else:
        return CONTINUE


def solve(partial_sol):
    exam = examine(partial_sol)

    if exam == ACCEPT:
        all_solutions.append(partial_sol)

    elif exam != ABANDON:
        for p in extend(partial_sol):
            solve(p)

def insertion_sort(array: list):
    for index in range(1, len(array)):
        current = array[index]
        prev_index = index - 1
        while prev_index >= 0 and current[1] < array[prev_index][1]:
            array[prev_index + 1] = array[prev_index]
            prev_index -= 1
        array[prev_index + 1] = current

def is_solution(candidate:list):
    insertion_sort(candidate)
    print(f'sorted candidate: {candidate}')

    if all_solutions == []:
        solve([])
    
    if candidate in all_solutions:
        return 'Valid!'
    elif candidate not in all_solutions:
        return 'Invalid'

candidate_solution1 = ['d3', 'c1', 'e5', 'b4', 'a2']
candidate_solution2 = ['e4', 'a1', 'c5', 'd2', 'b1']

result1 = is_solution(candidate_solution1)
print("Candidate Solution 1:", result1)

result2 = is_solution(candidate_solution2)
print("Candidate Solution 2:", result2)

# 3.
class Graph:
    graph = dict()
    searched = []

    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)

    def print_graph(self):
        print(self.graph)

    def print_edges(self):
        for node in self.graph:
            for neighbour in self.graph[node]:
                print("(", node, ",", neighbour, ")")

    def breath_first_search(self, node):

        result = []

        searched = [node]
        search_queue = [node]

        while search_queue:
            node = search_queue.pop(0)

            result.append(node)

            if node in self.graph:
                for neighbour in self.graph[node]:
                    if neighbour not in searched:
                        searched.append(neighbour)
                        search_queue.append(neighbour)

        return result

    def deapth_first_search(self, node):
        if node not in self.searched:

            self.searched.append(node)
            if node in self.graph:
                for neighbour in self.graph[node]:
                    self.deapth_first_search(neighbour)

    def find_scycle(self, node):
        mother_tree = self.breath_first_search(node)
        for i in mother_tree:
            if i == mother_tree[0]:
                continue
            if i in self.graph:
                for j in self.graph[i]:
                    if j in mother_tree and mother_tree.index(j) > mother_tree.index(i):
                        return 'Cycle found!'
            else:
                return 'No cycle found'

        


my_graph = Graph()
my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'B')
my_graph.add_edge('C', 'J')
my_graph.add_edge('D', 'E')
my_graph.add_edge('D', 'F')
my_graph.add_edge('E', 'C')
my_graph.add_edge('E', 'G')
my_graph.add_edge('F', 'H')
my_graph.add_edge('G', 'I')
test1 = my_graph.find_scycle('G')
print(test1)
my_graph.print_graph()