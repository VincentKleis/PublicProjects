def evaluer(x:str) -> int:
    start = x.split()
    try:
        start[0] = int(start[0])
        start[-1] = int(start[-1])
    except:
        print(f'{start[0]} eller {start[-1]} er ikke tall')

    dict = {'pluss' : start[0] + start[-1], 'ganger': start[0] * start[-1], 'minus': start[0] - start[-1], 
    'delt på': start[0] / start[-1] , 'multiplisert med': start[0] * start[-1], 'dividert med': start[0] / start[-1] }
    
    y = ' '.join(start[1:-1])

    if y in dict:
        return dict[y]
    else:
        return f'{y} er ikke forstått av maskinen'

test = evaluer('4 delt på 2')
print(test)
        