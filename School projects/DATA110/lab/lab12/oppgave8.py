def regnearter(x:int,y:int,z:str):
    """tar imot to tall og en streng med regner arter
    bruker så alle regneartene i strengen og printer en liste med utregninger til consollen

    Args:
        x (int): tall1
        y (int): tall2
        z (str): regnearter
    """
    l_regne = list(z)
    
    for i in l_regne:
        # utrenging = f'print("{x}{i}{y} =", {x}{i}{y})'
        # exec(utrenging)
        # alternativt
        utrenging = eval(f'{x} {i} {y}')
        print(f'{x}{i}{y} = {utrenging}')

print('test1')
test1 = regnearter(5,2,'+')
print('test2')
test2 = regnearter(10,7,'+-*/')