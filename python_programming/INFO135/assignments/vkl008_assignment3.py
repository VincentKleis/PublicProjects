import random
from math import factorial
import hashlib as hl


# 1.
def hash_function(string, salt):
    total = 0
    length = len(string)
    for i in range(length):
        total += ord(string[i]) + length
    return total % salt


my_list = ['a1b2c3', 'CiTiBnk', '232323', 'myLaptrop']
random_salt = 19
for item in my_list:
    print(hash_function(item, random_salt), end='')
# resultat: 59164
print('')


# 2.
class HashClass:

    def __init__(self, id_number):
        self.id_number = str(id_number)
        self.hash_id = None

    def hash_it(self):
        salt = random.randint(1, 1000)
        self.id_number += str(salt)
        self.hash_id = hl.sha1(self.id_number.encode('utf-8')).hexdigest()

    def print_it(self):
        print(self.hash_id)


test = HashClass(11011999)
test.hash_it()
test.print_it()

# ex3
list_of_tuples = [('Birds of Pray', 97.1),
                  ('Dolittle', 175.0),
                  ('The Gentlemen', 7.0),
                  ('Falling', 22.0)]


def insertion_sort(array: list):
    for index in range(1, len(array)):
        current = array[index]
        prev_index = index - 1
        # iterrate backwards through the array and compare the current elements second value to every ellements second
        # value
        while prev_index >= 0 and current[1] < array[prev_index][1]:
            # move the previus element forward each time
            array[prev_index + 1] = array[prev_index]
            prev_index -= 1
        # when condition breaks set the current element in the position in front of the element that broke the condition
        array[prev_index + 1] = current


def sort_and_print(array):
    insertion_sort(array)
    print(f'the movie with the largest budget was: {array[-1][0]}')


sort_and_print(list_of_tuples)


# ex4
def magic_function(array: str, result=None, depth = 0):
    if depth == 0: 
        return magic_function(array, list(array), depth+1)

    if depth < len(array): 
        result = [i+j for i in result for j in list(array) if j not in list(i)]
        return magic_function(array, result, depth+1)

    return result

def permute_loop(array: str):
    result = list(array)

    while len(result) != factorial(len(array)): 
        result = [i+j for i in result for j in list(array) if j not in list(i)]

    return [i+j for i in result for j in list(array) if j not in list(i)]

print(permute_loop('abcd'))