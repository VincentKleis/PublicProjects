file = [3380, 4770, 4693, 2271, 1156, 1817, 4414, 2211, 2213, 9208]
result = {}

for i in file:
    result[i] = i%8

def dict_sort(dictionary: dict) -> dict:
    result = {}
    
print(result, sep=', ')