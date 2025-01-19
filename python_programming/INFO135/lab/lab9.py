# ex 1
# a) HADECBGF
# b) DAEHCGBF
# c) DEAGFBCH

# ex 2
import math


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node
            
    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def print_tree(self, tree):
        
        if tree.left_child == None:
            if tree.right_child == None:
                return tree.value
            else:
                return tree.value + self.print_tree(tree.right_child)
        elif tree.left_child != None:
            if tree.right_child == None:
                return self.print_tree(tree.left_child) + tree.value
        
        return self.print_tree(tree.left_child) + tree.value + self.print_tree(tree.right_child)

def build_my_tree():
    tree = BinaryTree('H')
    tree.insert_left('A')
    tree.insert_right('C')

    tree.left_child.insert_left('D')
    tree.left_child.insert_right('E')

    tree.right_child.insert_right('B')

    tree.right_child.right_child.insert_left('G')
    tree.right_child.right_child.insert_right('F')

    return tree

tree = build_my_tree()
tree.print_tree(tree)

# ex 3

class BinarySearchTree:
    
    def __init__(self, value=None):
        self.value = value
        if self.value:
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()
        else:
            self.left_child = None
            self.right_child = None
        
    def is_empty(self):
        return self.value is None

    def insert(self, value):
        if self.is_empty():
            self.value = value
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()

        elif value < self.value:
            self.left_child.insert(value)

        elif value > self.value:
            self.right_child.insert(value)

    def in_order(self):
        if self.is_empty():
            return []
        else:
            return self.left_child.in_order() + \
                    [self.value] + \
                    self.right_child.in_order()
    
    def print_tree(self):
        print(self.in_order())

my_tree = BinarySearchTree()
my_tree.insert(3)
my_tree.insert(1)
my_tree.insert(4)
my_tree.insert(2)
my_tree.insert(5)
print(my_tree.in_order()[1], my_tree.in_order()[-1])

# ex 4
# O(n^2) this is because the result has to grow faster than O(n) with 9n^4, but slower than O(!n) since the calculation does not multiply anny n by an other n
# we can also test it to aproximate
big_o_test_set = [1,5,10,15,20,25,30,35,40]
big_o_set_function = [9*x**4+math.log2((x**2)*2)+8*x for x in big_o_test_set]
big_o_exponential = [x**2 for x in big_o_test_set]
big_o_linier = [x for x in big_o_test_set]
print(big_o_set_function, big_o_linier, big_o_exponential, sep='\n')
# we see that i was wrong
for index in range(0, len(big_o_test_set)-1):
    print(big_o_set_function[index+1]-big_o_set_function[index], end=', ')
print()
# by printing the growth of the numbers we se that its most probably a hocky stick curve that starts at 18, 
# therfore we can asume that the function has logarithmic growt witch has the big O notation of O(log(n))
