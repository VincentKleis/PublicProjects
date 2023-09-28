# oppgave 1
def enda_navn_nummer(navn_nummer):
    with open('telefon.txt', 'a') as f:
        f.write(navn_nummer+'\n')

def interaktiv():
    while True:
        navn_nummer = input('Navn og nummer: ')
        if navn_nummer == '': break
        enda_navn_nummer(navn_nummer)

def ikke_interaktiv():
    enda_navn_nummer('Alf 99706050')
    enda_navn_nummer('Guro 98102030')

# for å teste bruk interaktiv() for å taste in selv og ikke interaktiv for å la programmet gjøre oppgaven uten at man trenger å taste
ikke_interaktiv()

# oppgave 2
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
ikke_interaktiv()

# oppgave 3
def fjern_vokaler(fil_navn:str)-> str:
    vokaler = ['a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å']

    with open(fil_navn, 'r', encoding='UTF-8') as f:
        text = f.read()

    for n in vokaler:
        text = text.replace(n, '')
    print(text)
    
    with open('ny_'+fil_navn, 'w', encoding='UTF-8') as f:
        f.write(text)
    
# test
fjern_vokaler('tre_små_kinesere.txt')