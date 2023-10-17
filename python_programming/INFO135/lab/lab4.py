import math
# Exercise 1
# You have a list of length n = 8,649.
n = 8649
# What do you think the O notation of a function is given the following amount of operations?
# a) 113,115
print(113115/n)
print(math.ceil(n*math.log(n, 2)))
# from my short experimenting i found that O(n*log2(n)) is not only a close aproximation but the answer
# -----------------------------------------------------------------------------------------------------

# b) 74,805,201
# this number is so big that there is only one big o i can imagine it being
print(n**2)
# ass it turns out i was right and the big o was O(n^2)
# -----------------------------------------------------------------------------------------------------

# c) 8,649
# this big o is obvius O(n)
# _______________________________________________________________________________________________________

# Exercise 2
# def one_pass(liste, index):
#   sub_liste = liste[index:]
#   smallest = min(sub_liste)
#   smallest_index = sub_liste.index(smallest) + index
#   liste[index], liste[smallest_index] = liste[smallest_index],
#   liste[index]
#   return liste

# liste = [-4,0,1,9,0]
# selection_sort(liste)
# Expected output: [-4, 0, 0, 1, 9]

# Above you can see the function one_pass(liste, index). This is one of the solutions to last lab’s
# exercise. Use this function to sort an entire list.
# There are two approaches to this exercise: You can choose to use one_pass(liste, index) as a helper
# function, I.e. create another function that uses one_pass(liste, index) to complete a sort.
# Or you can rewrite one_pass(liste, index) to recursively sort the entire list by itself. The second
# approach is slightly more challenging.

def selection_sort(liste:list, index=0):
    if index == len(liste):
        return liste
    sub_liste = liste[index:]
    smallest = min(sub_liste)
    smallest_index = sub_liste.index(smallest) + index
    liste[index], liste[smallest_index] = liste[smallest_index], liste[index]
    return selection_sort(liste,index+1)

liste = [-4,0,1,9,0]
print(selection_sort(liste))

# _____________________________________________________________________________________________________________________
# Exercise 3
# Given a set of n nuts of different sizes, and n bolts of different sizes there is a one to one mapping
# between the nuts and bolts. We need to find the correct matches, and assign that nut with the
# matching bolt.
# Comparison of a nut to another nut, or a bolt to another bolt is not allowed! It means that a nut can
# only be compared with a bolt, and a bolt can only be compared with a nut to see which one is
# bigger/smaller.
# Input:
# The lists of locks and keys:
# nuts = ['@', '#', '$', '%', '^', '&']
# bolts = ['$', '%', '&', '^', '@', '#']
# Expected output after matching nuts and bolts:
# Nuts: # $ % & @ ^
# Bolts: # $ % & @ ^
# Another way of asking this problem is, given a box with locks and keys where one lock can be opened
# by one key in the box. We need to match the pair and we cannot match locks with locks or keys with
# keys.
# To solve this problem you will need to use quick sort (a divide and conquer algorithm), and do some
# slight modifications to match the nuts and bolts.
# You will need to make two functions:
# def partition(list, low, high, pivot):
# def quick_sort(nuts, bolts, low, high):
# First perform a partition by taking the last element of the bolt as a pivot, and rearrange the list of
# nuts. Return the partition index such that nuts smaller than nuts[partition index] are on the left side,
# and nuts greater that nuts[partition index] are on the right side.
# Then using this pivot index we can partition the list of bolts, with nuts[pivot index} as our pivot
# value. After that is done, we apply this partitioning recursively on the left and right sub lists of both
# the nuts and bolts to get all the matches.
# With both of them sorted, you will then have a case where bolts[i] = nuts[i] and you have your
# matched lists.
# On the next page is the psuedo code for the nuts and bolts code. Try to do without, and construct the
# quick sort algorithms and modify it to this case. But if you are stuck it can be a great help.
# partition(array, low, high, pivot)
# Input: One array, the low index, high index, the selected pivot element.
# Output: Final location of pivot element.
# Begin
# i = low
# j = low
# while j < high, do
# if array[j] < pivot, then
# swap array[i] and array[j]
# increase i by 1
# else if array[j] = pivot, then
# swap array[j] and array[high]
# decrease j by 1
# increase j by 1
# done
# swap array[i] and array[high]
# return i
# End
# nutAndBoltMatch(nuts, bolts, low, high)
# Input: The list of nuts, the list of bolts, lower index, higher index of
# the array.
# Begin
# if low < high, then
# pivot = partition(nuts, low, high, bolts[high])
# partition(bolts, low, high, nuts[pivot])
# nutAndBoltMatch(nuts, bolts, low, pivot-1)
# nutAndBoltMatch(nuts, bolts, pivot + 1, high)
# End
# matchPairs(nuts, bolts, 0, list_length - 1)
# Print nuts and bolts lists

# this lab exercise is increadably dificult to read and comprehend, 
# so i have re writen it to the way i see the question at hand:
# Imagine having two lists of nuts and bolts that look something like this:
# nuts = ['@', '#', '$', '%', '^', '&']
# bolts = ['$', '%', '&', '^', '@', '#']
# these nuts and bolts are special and every individual nut has one and only one coresponding bolt
# sort the two list with the functions
# def partition(list, pivot):
# def quick_sort(nuts, bolts):
# so that you get the output:
# Nuts: # $ % & @ ^
# Bolts: # $ % & @ ^
# 
# partition takes the list and returns the index of the pivot that would splitt the list in the midle,
# quick_sort takes the lists of nuts and bolts and returns them in the order where they correspond.
# try making the functions your self if not follow the following psudokode:
# ...
# insert random psudokode
# ...
# 
# i can solve this with only one very simple function by exploiting the fact that these chars have ascii values

def quick_sort(array:list):
    if len(array) < 2:
        return array

    pivot = array[0]
    if type(pivot) == int:
        left = [i for i in array[1:] if i <= pivot]
        right = [i for i in array[1:] if i > pivot]
    if type(pivot) == str:
        left = [i for i in array[1:] if ord(i.lower()) <= ord(pivot.lower())]
        right = [i for i in array[1:] if ord(i.lower()) > ord(pivot.lower())]

    return quick_sort(left) + [pivot] + quick_sort(right)

nuts = ['@', '#', '$', '%', '^', '&']
bolts = ['$', '%', '&', '^', '@', '#']
print(*quick_sort(nuts))
print(*quick_sort(bolts))
