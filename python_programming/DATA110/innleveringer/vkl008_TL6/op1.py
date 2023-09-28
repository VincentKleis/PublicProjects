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
