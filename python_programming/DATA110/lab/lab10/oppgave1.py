tall=(1,2,3,4,5)
storetall=(99,88,77,66,55)
bokstaver=('a','b','c','d','e')

def tripler(x:tuple, y:tuple, z:tuple) -> tuple:
    t = []
    for i, _ in enumerate(tall) :
        t.append( (x[i], y[i], z[i]) )

    return tuple(t)

print(tripler(bokstaver,tall,storetall))