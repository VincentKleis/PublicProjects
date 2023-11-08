import random #importerer random modulen
tall = input('GI MEG ET TALL!:')
random_tall = random.randint(0,100)
print(f'{random_tall}/{int(tall)} = {random_tall/int(tall)}') #deller tillfeldig tall mellom 0 og 1000 på inputt tallet, og printer resultatet
