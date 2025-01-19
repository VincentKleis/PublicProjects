class Graph2:
    graph = dict()

    def set_costs(self, costs):
        self.costs = costs

    def find_lowest_cost(self, visited):
        lowest_cost = float('inf')
        lowest_cost_node = None

        for node in self.costs:
            cost = self.costs[node]
            if cost < lowest_cost \
                    and node not in visited:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    def dijkstra(self):
        visited = []
        node = self.find_lowest_cost(visited)

        while node is not None:
            print("[", node, end=" ] ")
            cost = self.costs[node]
            neighbors = self.graph[node]

            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if self.costs[n] > new_cost:
                    self.costs[n] = new_cost
            visited.append(node)
            node = self.find_lowest_cost(visited)

g2 = Graph2()
my_graph = g2.graph
my_graph['start'] = {'A': 6, 'B': 2}
my_graph['A'] = {'finish': 1}
my_graph['B'] = {'A': 3, 'finish': 5}
my_graph['finish'] = {}

costs = {'A': 6, 'B': 2, 'finish': float('inf')}
g2.set_costs(costs)



g2.dijkstra()