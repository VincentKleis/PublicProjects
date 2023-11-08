import random
import string
from large_list import liste


# ex 1
def selection_sort_one_pass(lst: list):
    smalest_item = None
    for item in lst:
        if smalest_item is None or smalest_item > item:
            smalest_item = item

    smalest_item_index = lst.index(smalest_item)
    item_0 = lst.pop(0)
    lst.insert(0, smalest_item)
    lst.pop(smalest_item_index)
    lst.insert(smalest_item_index, item_0)

    return lst


test = [5, 2, 3, 4, 0, 1]
result_test1 = selection_sort_one_pass(test)
# print(result_test1)

# ex 2
def filter_tuples(lst):
    result = []
    for tple in lst:
        item_1, item_2, item_3 = tple
        if item_1 + item_2 == item_3:
            result.append(tple)
    return result


def selection_sort(array):
    array_coppy = array
    result = []
    while result < array_coppy:
        smallest = None
        for item in array_coppy:
            if smallest is None or smallest > item:
                smallest = item

        result.append(smallest)
        array_coppy.pop(array_coppy.index(smallest))

    return result


random_list = []
for i in range(0, 9):
    random_list.append(random.randint(0, 20))

test1 = selection_sort(random_list)
# print(test1)

def tuple_selection_sort(array: list):
    array_coppy = array
    result = []
    while result < array_coppy:
        smallest = None
        for item in array_coppy:
            if smallest is None or smallest[2] > item[2]:
                smallest = item

        result.append(smallest)
        array_coppy.pop(array_coppy.index(smallest))

    return result


test2 = filter_tuples(liste)
test2 = tuple_selection_sort(test2)


# ex 3
def anagram_finder(str1:str, str2:str):
    str1 = str1.replace(' ', '')
    str2 = str2.replace(' ', '')
    if len(str1) != len(str2):
        return 'false'
    else:
        list1 = list(str1.lower())
        list2 = list(str2.lower())
        alfabet_list = list(string.ascii_letters)
        for i in list1:
            list1[list1.index(i)] = alfabet_list.index(i)
        for i in list2:
            list2[list2.index(i)] = alfabet_list.index(i)

        list1 = selection_sort(list1)
        list2 = selection_sort(list2)
        
        if list1 == list2:
            return 'true'
    return 'failed'

print(anagram_finder('abc', 'cba'))
print(anagram_finder('ABBA', 'baba'))
print(anagram_finder('Cat', 'Act'))
print(anagram_finder('Astronomer', 'Moon starer'))
print(anagram_finder('The Detectives', 'Detect Thieves'))
print(anagram_finder('Funeral', 'Real fun'))
print(anagram_finder('Listen', 'Silent'))