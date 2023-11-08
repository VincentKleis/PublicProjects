def fak(x):
    fak_list = []
    fak_res = 1
    while 0 < x:
        fak_list.append(x)
        x -= 1
    for i in fak_list:
        fak_res *= i
    return fak_res

print(fak(1))
print(fak(2))
print(fak(3))
print(fak(4))