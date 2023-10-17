# 1. all of the trees are full as far as i can see

# 2.
# importing binary_tree functions from lecture 8
from binary_tree import *
def make_tree():
    root = binary_tree(1)
    insert_left_child(root, 2)
    insert_right_child(root, 3)

    insert_left_child(root[1], 4)

    insert_left_child(root[2], 5)
    insert_right_child(root[2], 6)

    print(root)

make_tree()

# 3.
# importing a the graph class from lecture 7
from graph import graph

def build_my_graph2():
    root = graph()

    root.add_edge('a', 'b')
    root.add_edge('a', 'c')
    root.add_edge('b', 'c')
    root.add_edge('b', 'd')
    root.add_edge('c', 'e')
    root.add_edge('d', 'e')
    root.add_edge('d', 'g')
    root.add_edge('d', 'h')
    root.add_edge('e', 'f')
    root.add_edge('f', 'c')

    root.depth_first_search('a')

build_my_graph2()
# what is printed is [ a ] [ b ] [ c ] [ e ] [ f ] [ d ] [ g ] [ h ]

print()

# 4.

class binarySearchTree:

    def __init__(self, value=None):
        self.value = value
        if self.value:
            self.left_child = binarySearchTree()
            self.righ_child = binarySearchTree()
        else:
            self.left_child = None
            self.righ_child = None
    
    def is_empty(self):
        return self.value is None

    def insert(self, value):
        if self.is_empty():
            self.value = value
            self.left_child = binarySearchTree()
            self.righ_child = binarySearchTree()

        elif value < self.value:
            self.left_child.insert(value)
        
        elif value > self.value:
            self.righ_child.insert(value)
    
    def in_order(self):
        if self.is_empty():
            return []
        else:
            return self.left_child.in_order() + \
                    [self.value] + \
                        self.righ_child.in_order()
    
    def compute_sum(self):
        """Sums the current node and the next leaf node if the current node is a branch (has a child)
        if the current node is a leaf return the value.
        if the current node is a root find the sum of current node and any branch or leaf.

        Returns:
            int: the sum of of every node
        """
        if self.righ_child is None:
            if self.left_child is None:
                if self.value is None:
                    return 0
                else:
                    return self.value
            else:
                return self.value + self.left_child.compute_sum()
        else:
            if self.left_child is None:
                return self.righ_child.compute_sum() + self.value
            else:
                return self.left_child.compute_sum() + self.righ_child.compute_sum() + self.value
    
    def compute_count(self):
        """Same as previus method but sums a count instead of the current value

        Returns:
            int: the count of nodes
        """
        if self.righ_child is None:
            if self.left_child is None:
                if self.value is not None:
                    return 1
                else:
                    return 0
            else:
                return 1 + self.left_child.compute_count()
        else:
            if self.left_child is None:
                return self.righ_child.compute_count() + 1
            else:
                return self.left_child.compute_count() + self.righ_child.compute_count() + 1

    # as we used a recursive traversing of the tree both times we can implement 
    # a fuction like the in_order() function from the lecture to simplify
    
    def compute_sum2(self):
        """Uses the in order function defined in the lecture to compute sum more acuratly

        Returns:
            int: sum of node values
        """
        result_list = self.in_order()
        result_sum = 0
        for i in result_list:
            result_sum += int(i)
        return result_sum
    
    def compute_count2(self):
        """Uses the in order function to count the number of nodes

        Returns:
            int: number of nodes
        """
        result_list = self.in_order()
        result_count = 0
        for i in result_list:
            result_count += 1
        return result_count

my_tree = binarySearchTree()

my_tree.insert(2)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(8)
my_tree.insert(10)

print('sum:', my_tree.compute_sum())
print('count:', my_tree.compute_count())
print('sum:', my_tree.compute_sum2())
print('count:', my_tree.compute_count2())