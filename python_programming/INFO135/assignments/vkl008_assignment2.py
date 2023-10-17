# 1. Suppose you have the following list of numbers to sort:
# [ 1001, 1030, 1050, 1020, 300, 1080, 1100]
# What will be the partially sorted list after 3 passes of Selection Sort?
# ------------------------------------------------------------------------
# using a algorithme like this:
from re import A


def selection_sort(array:list):
    result = []
    while len(array) > 0:
        smallest = None
        for item in array:
            if smallest is None or smallest > item:
                smallest = item

        result.append(smallest)
        array.pop(array.index(smallest))

    return result

# selection sort would create two lists and pop the items of the first list 
# in order from smallest to largest
# so you would end upp with a partually sorted list looking like this-:
part_sorted_list = [300, 1001, 1020]

# and a unsorted list looking like this-:
unsorted_list = [1030, 1050, 1080, 1100]

# after 3 passes

# _______________________________________________________________________
# 2. Suppose you have the following list of numbers to sort:
# [ 210, 15, 111, 90, 45, 120, 150, 200, 100, 140 ]
# What will be the partially sorted list after 3 passes of Bubble Sort?
# -----------------------------------------------------------------------
# to solve this i made an fuction that sorts as bublesort one pass at a time:
def buble_sort_one_pass(array:list):
    for i in range(0, len(array)-1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
    return array

# i can then answer like this
second_list = [210, 15, 111, 90, 45, 120, 150, 200, 100, 140]
print(second_list)
pass_one = buble_sort_one_pass(second_list)
pass_two = buble_sort_one_pass(pass_one)
pass_thre = buble_sort_one_pass(pass_two)
print(pass_thre)
# reading from console i now get that the list pre and post 3-passes of 
# bubles sort are ass follows:
# [210, 15, 111, 90, 45, 120, 150, 200, 100, 140]
# [15, 45, 90, 111, 120, 100, 140, 150, 200, 210]
# notice that the thre largest numbers have "bubled" to the end, 
# this is a clear indicatior that buble sort has done it's job
#
# _____________________________________________________________________
# 3. Write a function called sort_and_rem_dup() that receives a list of numbers and
# returns a sorted list where the duplicates in the numbers are removed.
#
# Please note that:
#   • you can choose and implement Selection sort, Insertion sort or Bubble sort.
#   • you cannot use Python Set data structure to remove the duplicates.
#   • you cannot use sort() or sorted() built-in functions for Python list.
# 
# [Hint]: you can find an implementation of sorting algorithms in the slides of Lecture 3.

def insertion_sort(array: list):
    for index in range(1, len(array)):
        # finds the current element
        current = array[index]
        prev_index = index - 1
        # untill we reach the first item: test if the current ellement is smaler than the previus element
        while prev_index >= 0 and current < array[prev_index]:
            # set the value of the element ahed of the element with an index eqal to the prev_index + 1,
            # to the element with the index prev_index
            array[prev_index + 1] = array[prev_index]
            prev_index -= 1
        # when pev_index is 0 or the ellement with index prev_index is larger than the current element, insert the
        # current element into the array at position prev_index+1
        array[prev_index + 1] = current

def sort_and_rem_dup(array:list):
    insertion_sort(array)
    result = []
    prev = None
    for i in array:
        if prev is None:
            prev = i
            result.append(i)
            continue
        elif prev != i:
            result.append(i)
            prev = i
    return result


my_list = [5, 4, 3, 2, 1, 2, 3, 4, 5]
new_list = sort_and_rem_dup(my_list)
print(new_list)

# _____________________________________________________________________
# 4. Write a function check_palindrome(word) that receives a string variable called
# word as an input parameter, and builds a Stack and a Queue where their elements are the
# letters (characters) of that word. Then, the function should check and print if the word is
# a Palindrome or not.
#
# [Hint 1]: Palindrome is a word whose characters are equal backward and forward.
# [Hint 2]: you can find implementation of Stack and Queue in the slides of Lecture 2 & 3.
#
#
# result = check_palindrome('hello')
# print(result)
#
# result = check_palindrome('civic')
# print(result)
#
#
# [Output]:
#   Not Palindrome
#   Palindrome

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

def check_palindrome(word:str):
    # Initiates a que and a stack
    word_que = que()
    word_stack = stack()
    # Iterates over every character in the string variable "word"
    for i in list(word):
        # Adds every character to the que and the stack
        word_que.enqueue(i)
        word_stack.push(i)
    # A loop that stops only when the que is empty
    while word_que.is_empty() is False:
        # Removes the item at the end of the que and sets it as the value of the variable a
        a = word_que.dequeue()
        # Removes the item at the top of the stack and sets it as the value of the variable b
        b = word_stack.pop()
        # Testes a against b and sees if they are equal
        if a != b:
            return 'Not Palindrome'
        # If you get to the end of the que and the stack with every string being equal the original word must be a palindrome
        if word_que.is_empty() is True and a == b:
            return 'Palindrome'

result = check_palindrome('hello')
print(result)

result = check_palindrome('civic')
print(result)