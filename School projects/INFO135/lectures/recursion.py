import time
def sum(n):
    if n < 2:
        return n
    return sum(n-1) + n

def fast_sum(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result

