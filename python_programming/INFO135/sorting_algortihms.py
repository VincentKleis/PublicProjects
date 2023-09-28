import random, math


def random_list(list_length: int):
    result = []
    for i in range(0, list_length):
        result.append(random.randint(0, 9))
    return result


def selection_sort(array):
    array_coppy = array
    result = []
    while len(array_coppy) > 0:
        smallest = None
        for item in array_coppy:
            if smallest is None or smallest > item:
                smallest = item

        result.append(smallest)
        array_coppy.pop(array_coppy.index(smallest))

    return result

def buble_sort_one_pass(array:list):
    for i in range(0, len(array)-1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
    return array


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


def bucket_sort(array, number_buckets: int = 1):
    buckets = []
    while number_buckets > 0:
        buckets.append([])
        number_buckets -= 1

    M = max(array)

    for i in range(0, len(array)):
        buckets.insert()
        ...


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


def merge_sort(array):

    if len(array) > 1:
        mid_index = len(array) // 2
        left = array[:mid_index]
        right = array[mid_index:]
        merge_sort(left)
        merge_sort(right)

        print(left, right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
