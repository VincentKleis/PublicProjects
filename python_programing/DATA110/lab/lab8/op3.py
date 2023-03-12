# a)
def settinn(informasjon: str = '',fil_navn: str = ''):
    with open(fil_navn, 'r') as f:
        adresser = f.readlines()

    adresser.append(informasjon+'\n')
    adresser.sort()

    with open(fil_navn, 'w') as o:
        o.writelines(adresser)

settinn('Hans Kirkegata 3','adresse.txt')
settinn('Siv Kirkegata 1', 'adresse.txt')

# b)
def sorter(fil_navn:str):
    settinn(fil_navn='sortert_'+fil_navn)

sorter('telefon.txt')
