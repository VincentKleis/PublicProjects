def decimal_til_biner(x:int) -> int:
    """tar imot decimal tall som x og gir et binært tall

    Args:
        x (int): decimal

    Returns:
        int: binær
    """
    Biner_størelser = {64:1000000, 32:100000, 16:10000, 8:1000, 4:100, 2:10, 1:1}
    y = 0
    t = 0
    for i in Biner_størelser:
        if i <= x - t:
            y += Biner_størelser[i]
            t += i

    return y

def decimal_og_biner(x:int) -> str:
    """tar imot et decimal tall og printer en liste 
    med tall i binær og decimal opp til det tallet

    Args:
        x (int): desimal

    Returns:
        str: liste med desimal og binær
    """
    oversikt = ''
    count = 0
    while count <= x:
        oversikt += f'{decimal_til_biner(count)} = {count}\n'
        count += 1
    
    return oversikt

def biner_compar(x:int, y:str)-> list:
    """tar imot to tall, x og y. x er lengden på listen som skal sammenlignes, og y er tallet som skal sammenlignes.
        skal kunne sammelinge med tall som er på en hvis sørelse eller starter med y

    Args:
        x (int): lengden liste som skal sammenlignes
        y (str): tall som skal sammenlignes. 

    Returns:
        list: likheter på størelse x, med x der det ikke er noen likheter
    """
    decimal_list = decimal_og_biner(x).split('\n')
    likheter = ''
    liste_for_samenligning = []
    y = y.split()
    for i in decimal_list:
        i = i.split(' = ')
        print(y)
        tall = i[1].split()
        count = 0
        for n in y:
            if n != tall[count] and n == 'x':
                likheter += n
                count += 1
                continue
            if n == tall[count]:
                liste_for_samenligning.append(i[0])
        print(liste_for_samenligning)

test = biner_compar(100, '6 x')
