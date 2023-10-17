#oppgave 3 a)

saldo = 500
rentesats = 0.01

def innskudd(x):
    global saldo
    global rentesats # henter globale variablene 'saldo' og 'rentesats' så jeg kan manipulere dem i funksjonen
    saldo = saldo + x 
    if saldo >= 1000000:
        rentesats = 0.02
        print('gratulerer, du får mer i rente!')

    """ Gjør ett innskud på saldo,
        dersom innskuddet gjør saldo større en 1mil så får du mer i rente
    Returnerer:
        saldo + innskudd
        eventuelt ny rentesats, og en gratulasjon 
    """

def uttak(x):
    global saldo
    global rentesats
    if x > saldo:
        print('overtrekk')
        return                       
    saldo = saldo - x                               # trekker fra uttak, og om saldoen faller under 1 mill fjerner den ekstra renten,
    if saldo < 1000000 and saldo + x >= 1000000:    # og dersom uttrekket er større en saldoen så er det overtrekk og funksjonnen stopper
        print('du har nå ordiner rente')
        rentesats = 0.01

    """ Gjør et uttak fra saldo
        kunne også definert som innskudd * -1
    Returnerer:
        int: saldo - uttak
    """

rente = 0
def beregnRente():
    global rente
    rente = rentesats * saldo   # beregner rente
    return rente

def renteoppgjør():
    beregnRente()
    global saldo
    saldo = rente + saldo     # beregner årlig renteoppgjør

print(saldo)
print(rentesats)
innskudd(300)
print(saldo)
uttak(100)
print(saldo)
print(beregnRente())
print(saldo)
renteoppgjør()
print(saldo)
innskudd(1000000)
print(saldo)
print(rentesats)
uttak(500000)
print(saldo)
print(rentesats)
uttak(1000000)
print(saldo)

# b)

saldo = 500
user = None
def valg_b():
    while True:
        print('''--------------------
1 - vis saldo
2 - innskudd
3 - uttak
4 - renteoppgjør
5 - stopp program
--------------------''')
        user = int(input('Velg handling:'))
        if user == 1:
            print(f'Saldo:  {saldo}')
        elif user == 2:
            påfyll = int(input('Beløp:'))
            innskudd(påfyll)
            print(f'Saldo: {saldo}')
        elif user == 3:
            trekk = int(input(f'Beløp:'))
            uttak(trekk)
            print(f'Saldo: {saldo}')
        elif user == 4:
            renteoppgjør()
        elif user == 5:
            break
        else:
            print('Ikke et valg')
    """[printer en valg skjerm]
    Utifra valg etter valg skjermen så utføres en koresponderende handlging gjennom 'if-elif-else' 
    """

valg_b()

# c)

saldo = 500
user = None
def valg_c():
    while True:
        print('''--------------------
1 - vis saldo
2 - innskudd
3 - uttak
4 - renteoppgjør
5 - siste endringer
6 - stopp program
--------------------''')
        user = int(input('Velg handling:'))
        endringer = ''
        if user == 1:
            print(f'Saldo:  {saldo}')
        elif user == 2:
            påfyll = float(input('Beløp:'))
            innskudd(påfyll)
            endringer = endringer + f'+{påfyll}\n'
            print(f'Saldo: {saldo}')
        elif user == 3:
            trekk = int(input(f'Beløp:'))
            uttak(trekk)
            endringer = endringer + f'-{trekk}\n'
            print(f'Saldo: {saldo}')
        elif user == 4:
            renteoppgjør()
            endringer = endringer + f'+{renteoppgjør()}'
        elif user == 5:
            print(endringer)
        elif user == 6:
            break
        else:
            print('Ikke et valg')
    """[printer en valg skjerm]
    Utifra valg etter valg skjermen så utføres en koresponderende handlging gjennom 'if-elif-else' 
    """

valg_c()