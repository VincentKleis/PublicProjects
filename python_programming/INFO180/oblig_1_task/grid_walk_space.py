'''
    Implementation of the search space for the grid walk search
    Written by: Bjornar Tessem, Aug 2022
'''

import time
from copy import deepcopy
from queue import Queue, LifoQueue, PriorityQueue

# from approx_max_dim_h import ApproxMaxDimH
from grid_walk_node import GridWalkNode
from grid_walk_path import GridWalkPath
from make_grid import is_goal
# from max_dim_h import MaxDimH
# from pythagoras_h import PythagorasH
from zero_h import ZeroH, MinHeuristikk, EuklidiskHeuristikk, TreHeuristikk
from heuristic import Heuristic



class GridWalkSpace:
    '''
    This class is a representation of the search space for grid walk search.
    It allows for various approaches to search for a solution
    '''

    HEURISTIC = Heuristic()

    @staticmethod
    def h(node):
                '''
                The heuristic used in the A/A* search
                :param node: the GridWalkNode to compute h-value for
                :return: the estimated distance to the goal
                '''

                return GridWalkSpace.HEURISTIC.h(node)

    def __init__(self, frontier = Queue(), heuristic = Heuristic()):
        '''
        Initialisation of the space
        '''
        self.start = GridWalkNode(0,0)
        # the search always starts in the upper left corner of the grid
        self.visited = set()
        # at start we have not visited any nodes (squares in the grid)

        # The search frontier is given in the argumentlist
        self.frontier = frontier
        GridWalkSpace.HEURISTIC = heuristic

        self.frontier.put(GridWalkPath([self.start],self.h(self.start)))
        # put the start node on the frontier
        # adding the start position's h-value as an estimate of length to goal state
        # the h-value is only useful in A search

    def solve(self):
        '''
        :return: path for grid walk solution
        '''
        start = time.time()
        # start time for timing

        while not self.frontier.empty():
            # if frontier is empty there is no solution
            next_path = self.frontier.get()
            # get the next path from the frontier
            last_node = next_path.node_list[-1]
            # get the last node of this path

            if is_goal(last_node.i, last_node.j):
                # if we have a solution

                end = time.time()
                # we stop timing
                print("Time: ", end-start)
                # print time spent

                print("Nodes visited ", len(self.visited)+1)
                # print the number of nodes visited in the search space

                print("Length: ", len(next_path.node_list), " Cost: ", next_path.cost)
                #print length and cost of path

                return next_path
                # and return the found path

            children = self.get_children(next_path)
            # else find the children for this path
            for child in children:
                # put children on the frontier
                self.frontier.put(child)

        print("No solution found")
        # print than no solutions are found

        return None


    def get_children(self, path):
        '''
        makes a list of paths that are children of the input path
        :param path: the path to add children for
        :return: the list of children paths
        '''
        children = []
        last = path.node_list[-1]
        # find the last node of the path

        if not self.is_visited(last):
            # only do this if the last one is not already visited
            # add moves by making moves where you move in
            # in different directions
            self.add_move(children, path.node_list, last.up_left())
            self.add_move(children, path.node_list, last.up())
            self.add_move(children, path.node_list, last.up_right())
            self.add_move(children, path.node_list, last.left())
            self.add_move(children, path.node_list, last.right())
            self.add_move(children, path.node_list, last.down_left())
            self.add_move(children, path.node_list, last.down())
            self.add_move(children, path.node_list, last.down_right())

            self.visited.add(last)
            # add last to the set of visited nodes

        return children

    def is_visited(self, last):
        '''
        checks if a node in the search space is already visited
        :param last: the node to check
        :return: true if already visitetd
        '''
        return last in self.visited

    def add_move(self, children, path, node):

        '''
        Adds a single new path to a set of paths contained in children
        Copies path and adds node into the copied path
        :param children: the set of paths to add the new path to
        :param path: the path to which a next move is added
        :param node: the new node in the search space that is added to the path
        :return: nothing
        '''
        if node is not None:

            new_path = deepcopy(path)
            # make a deep copy of path

            new_path.append(node)
            # append node to this path

            grid_path = GridWalkPath(new_path,self.h(node))
            # makes a new GridWalkPath object with the new path and the h value (for A search)

            children.append(grid_path)




if __name__ == '__main__':

    # print("Breidde-først")
    # sp = GridWalkSpace(Queue())
    # sp.solve()

    # print("Djupn-først-søk")
    # sp = GridWalkSpace(LifoQueue())
    # sp.solve()

    print("Best-først-søk")
    sp = GridWalkSpace(PriorityQueue())
    sp.solve()

    print("Heuristisk-søk")
    sp = GridWalkSpace(PriorityQueue(), MinHeuristikk())
    sp.solve()

    print("Eucklidisk-søk")
    sp = GridWalkSpace(PriorityQueue(), EuklidiskHeuristikk())
    sp.solve()

    print("ganger-tre-heuristisk-søk")
    sp = GridWalkSpace(PriorityQueue(), TreHeuristikk)
    sp.solve()


sizes = [10, 40, 160, 320]
probs = [0.10, 0.30, 0.50, 0.70]
seed = 6458

# all_combinations = [(x,y,seed)for x in sizes for y in probs]
# print(all_combinations)
# [(10, 0.1, 6458), (10, 0.3, 6458),
# (40, 0.1, 6458), (40, 0.3, 6458),
# (160, 0.1, 6458), (160, 0.3, 6458),
# (320, 0.1, 6458), (320, 0.3, 6458)]

# results
# (10, 0.1, 6458)
# Best-først-søk
# Time:  0.030921459197998047
# Nodes visited  89
# Length:  12  Cost:  25
# Heuristisk-søk
# Time:  0.016982316970825195
# Nodes visited  58
# Length:  12  Cost:  25
# Eucklidisk-søk
# Time:  0.016955852508544922
# Nodes visited  50
# Length:  12  Cost:  25
# ganger-tre-heuristisk-søk
# Time:  0.0049860477447509766
# Nodes visited  14
# Length:  11  Cost:  27

# (10, 0.3, 6458)
# Best-først-søk
# Time:  0.014989614486694336
# Nodes visited  60
# Length:  13  Cost:  28
# Heuristisk-søk
# Time:  0.008976459503173828
# Nodes visited  42
# Length:  13  Cost:  28
# Eucklidisk-søk
# Time:  0.009000778198242188
# Nodes visited  41
# Length:  13  Cost:  28
# ganger-tre-heuristisk-søk
# Time:  0.004988670349121094
# Nodes visited  17
# Length:  13  Cost:  28

# (40, 0.1, 6458)
# Best-først-søk
# Time:  1.699162483215332
# Nodes visited  1440
# Length:  54  Cost:  87
# Heuristisk-søk
# Time:  1.1147098541259766
# Nodes visited  1010
# Length:  54  Cost:  87
# Eucklidisk-søk
# Time:  1.1992919445037842
# Nodes visited  982
# Length:  56  Cost:  87
# ganger-tre-heuristisk-søk
# Time:  0.06682205200195312
# Nodes visited  69
# Length:  46  Cost:  107

# (40, 0.3, 6458)
# Best-først-søk
# Time:  1.104733943939209
# Nodes visited  1123
# Length:  52  Cost:  103
# Heuristisk-søk
# Time:  0.8980450630187988
# Nodes visited  953
# Length:  53  Cost:  103
# Eucklidisk-søk
# Time:  0.8777742385864258
# Nodes visited  942
# Length:  54  Cost:  103
# ganger-tre-heuristisk-søk
# Time:  0.07280468940734863
# Nodes visited  98
# Length:  50  Cost:  113

# (160, 0.1, 6458)
# Best-først-søk
# Time:  132.531188249588
# Nodes visited  23135
# Length:  206  Cost:  353
# Heuristisk-søk
# Time:  104.69171500205994
# Nodes visited  19663
# Length:  206  Cost:  353
# Eucklidisk-søk
# Time:  105.62635636329651
# Nodes visited  19489
# Length:  212  Cost:  353
# ganger-tre-heuristisk-søk
# Time:  1.447127103805542
# Nodes visited  354
# Length:  184  Cost:  423

# (160, 0.3, 6458)
# Best-først-søk
# Time:  100.60627365112305
# Nodes visited  17976
# Length:  205  Cost:  408
# Heuristisk-søk
# Time:  66.765465259552
# Nodes visited  16013
# Length:  206  Cost:  408
# Eucklidisk-søk
# Time:  66.61386799812317
# Nodes visited  15933
# Length:  206  Cost:  408
# ganger-tre-heuristisk-søk
# Time:  2.0974209308624268
# Nodes visited  589
# Length:  203  Cost:  453

# (320, 0.1, 6458)
# Best-først-søk
# Time:  1184.89946103096
# Nodes visited  92220
# Length:  413  Cost:  692
# Heuristisk-søk
# Time:  940.4092814922333
# Nodes visited  77711
# Length:  413  Cost:  692
# Eucklidisk-søk
# Time:  923.3607292175293
# Nodes visited  76677
# Length:  420  Cost:  692
# ganger-tre-heuristisk-søk
# Time:  4.847561597824097
# Nodes visited  629
# Length:  376  Cost:  807

# (320, 0.3, 6458)
# Best-først-søk
# Time:  727.9884338378906
# Nodes visited  71717
# Length:  444  Cost:  824
# Heuristisk-søk
# Time:  659.5825679302216
# Nodes visited  66505
# Length:  439  Cost:  824
# Eucklidisk-søk
# Time:  633.2571337223053
# Nodes visited  66385
# Length:  442  Cost:  824
# ganger-tre-heuristisk-søk
# Time:  10.202713966369629
# Nodes visited  1409
# Length:  398  Cost:  913

# vi ser at den eneste heuristicen som underestimerer nok er ganger-tre-heuristisk-søk, 
# ettersom den tar den lengste forskjellen i x eller y kordinat mellom foreløpig-tilstand og måltilstand og ganger med tre,
# men vi kan ikke si med sikkerhet at den alltid underestimerer, man kan se for seg en worst case der roboten må gå i et 
# sik-sak mønster over hele brettet som vil tilsvare å gå mer en 3 ganger lengden for alle bret over 3*3 størelse