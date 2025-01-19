import time

class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
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

        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current.next:
            print(current.data, end=',')
            current = current.next
        print(current.next)

class stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

class que:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def performance_test(function_1_str, function_2_str)->str:
    first_start = time.perf_counter_ns()
    exec(function_1_str)
    first_stop = second_start = time.perf_counter_ns()
    exec(function_2_str)
    second_stop = time.perf_counter_ns()

    result1 = eval(function_1_str)
    result2 = eval(function_2_str)

    text1_1 = f'the time {function_1_str} took was:'
    text_2 = 'and the result was:'
    text2_1 = f'the time {function_2_str} took was:'

    return f'{text1_1 : <40} {first_stop-first_start}ns, {text_2 : ^30} {result1}\n\
{text2_1 : <40} {second_stop-second_start}ns, {text_2: ^30} {result2}'

def binary_search(array, item):
    begin = 0
    end = len(array) - 1
    found = False
    while begin <= end and not found:
        mid = (begin + end) // 2
        if array[mid] > item:
            end = mid - 1
        elif array[mid] < item:
            begin = mid + 1
        else:
            found = True
    return found


