def endre_nummer(navn: str = input('Navn: '), gammelt_nummer: str = input(' Gammel telefonnummer: '), nytt_nummer:str = input(' Nytt nummer: ')) -> str:
    with open('telefon.txt') as f:
        telefonliste = f.read()

    ny_telefonliste = telefonliste.replace(f'{navn} {gammelt_nummer}', f'{navn} {nytt_nummer}')

    print(ny_telefonliste)

    with open('telefon.txt', 'w') as f:
        f.write(ny_telefonliste)

def interaktiv():
    endre_nummer()

def ikke_interaktiv():
    endre_nummer('Jens', '99776612', '99889999')

# i ikke_interaktiv() trenger man bare trykke enter
