def chop(x):
    del x[0]
    del x[-1]

def middle(x):
    y = x[1:-1]
    return y

test = []
n = 0
while n < 100:
    test.append(n)
    n+=1

print(test)
print(middle(test))
test_2 = middle(test)

chop(test)
print(test)