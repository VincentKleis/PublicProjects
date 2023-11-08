def fact_funct2(n):
    memory = []
    while n>=1:
        memory.append(n)
        n -=1
    memory.sort()
    x = 0
    for i in memory:
        if i == 1:
            x = 1
            continue
        x *= i
    return x

test = []
for i in range(0, 9):
    test.append(i)

test_fact = [fact_funct2(x) for x in test]

print([x for x in range(1,20)])