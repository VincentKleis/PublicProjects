from heuristic import Heuristic
from make_grid import SIZE
from math import sqrt

class ZeroH(Heuristic):

    @staticmethod
    def h(node):
        return 0

class MinHeuristikk(Heuristic):
    
    @staticmethod
    def h(node):
        dif_x, dif_y = SIZE-node.i, SIZE-node.j
        return max([dif_x, dif_y])

class EuklidiskHeuristikk(Heuristic):
    
    @staticmethod
    def h(node):
        dif_x, dif_y = SIZE-node.i, SIZE-node.j
        dif_z = sqrt(dif_x**2+dif_y**2)
        return dif_z

class TreHeuristikk(Heuristic):
    
    @staticmethod
    def h(node):
        dif_x, dif_y = SIZE-node.i, SIZE-node.j
        return max([dif_x, dif_y])*3

