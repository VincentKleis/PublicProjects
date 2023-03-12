import math

# ____________________________________________________________________________________________
# 1. Suppose you’re looking for a word in the following dictionaries. In the worst case how
#   many steps do you think the search will take with Binary Search?
#
#   a) Persian dictionary with 171476 words
#   b) English dictionary with 1100373 words
#   c) Chinese dictionary with 260000 words

answers_a = f'{math.ceil(math.log(171476, 2))}' + " words for Persian\n"
print(answers_a)
#17 words for Persian in the worst case scenario

answers_b = f'{math.ceil(math.log(1100373, 2))}' + " words for English\n"
print(answers_b)
#20 words for English in the worst case scenario

answers_c = f'{math.ceil(math.log(260000, 2))}' + " words for Chinese\n"
print(answers_c)

# 18 words for Chinese in the worst case scenario
#
# ____________________________________________________________________________________________
# 2. Write a class called Student that has two following methods:
#   • Method 1: __init__() that receives name, age and country of a student and sets
#     them as instance variables.
#   • Method 2: greeting() that prints the following message for a student whose name
#     is Sara, 25 years old and from Norway:
#
#
# student = Student("Sara", 25, "Norway")
# student. greeting()
#
# [Output]
#
#   Hei! my name is Sara
#   I am 25 years old.
#   I am from Norway.

class student:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def greeting(self):
        greeting = f'Hei! my name is {self.name}\n\
I am {self.age} years old.\n\
I am from {self.country}.\n'
        print(greeting)

# test = student("Sara", 25, "Norway")
# test.greeting()

#____________________________________________________________________________________________
# 3. Given the following linked-list class, write a method called print_list() that loops
# over and prints the entire contents of a linked-list starting from head.
#
# class LinkedList:
#
#   def __init__(self):
#       self.head = None

class node:
    def __init__(self, data) -> None:
        self.data = data
        next = None

class LinkedList:

    def __init__(self):
        self.head = None

def print_list(LinkedList):

    current = LinkedList.head
    while current:
        print(current)
        current = current.next
    print(current)

# ____________________________________________________________________________________________
# 4. Write a function reverse_list() that receives a Python list, builds a Stack with the
# same elements, and prints the reversed list.
#
# [Hint]: you can find the implementation of Stack in the slides of Lecture 2.

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

my_list = [1, 2, 3, 4, 5]

def reverse_list(list):
    result = []

    reverse_stack = stack()
    for item in list:
        reverse_stack.push(item)
    
    while reverse_stack.size() >= 1:
        result.append(reverse_stack.peek())
        reverse_stack.pop()

    print(result)

reverse_list(my_list)