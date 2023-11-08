def binary_tree(r):
    return [r, [], []]

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

def insert_left_child(root: list, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root

def insert_right_child(root: list, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root

class binarySearchTree:

    def __intit__(self, value= None):
        self.value =  value
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
    
    def compute_sum(self):
        if self.left_child.value is None and self.righ_child.value is None:
            return self.value
