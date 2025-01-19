class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


Node1 = Node()
Node2 = Node()
Node3 = Node()
Node1.next = Node2
Node2.next = Node3


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, new_data):
        new_node = f'Node{new_data}'
        if self.head is None:
            self.head = new_node

        last_node = self.head

        while last_node:
            last_node = last_node.next

        last_node.next = new_node

    def add_at_begining(self, data):

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current.next:
            print(current.data, end=',')
            current = current.next
        print(current.next)


my_list = LinkedList()
my_list.add('A')
print(my_list)
my_list.add('B')
my_list.add('C')
