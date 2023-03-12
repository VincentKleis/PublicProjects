# 1. #
import math

def pi(d=2):
    pi = math.pi
    if d > 15:
        print('For mange desimaler')
    x = round(pi, d)
    return x

###########################
##########TEST#############

print(pi(4))
print(pi(10))
print(pi(50))
print(pi())




# 2. #
C = u"\N{degree celsius}"
F = u"\N{degree fahrenheit}"
def temp_konv(tall, scala = 'C'):
    if scala == 'C':
        return f'{tall} grade {C}  er {tall*(9/5)+32} {F}'
    elif scala == 'F':
        return f'{tall} grade {F}  er {(tall-32)*5/9} {C}'

###########################
##########TEST#############

print(temp_konv(34,'C'))
print(temp_konv(93.2,'F'))
print(temp_konv(34))



# 3. #

# a)

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

def beregnRente():
    rente = rentesats * saldo   # beregner rente
    return rente

def renteoppgjør():
    global saldo
    rente = beregnRente()
    saldo = rente + saldo     # beregner årlig renteoppgjør
    return saldo

###########################
##########TEST#############

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
rente = 0.01

def valg_c():
    x = 0               # teller antal ganger noe har blitt lagt till 'historie' slik at neste ellement kan indexes på et annet sted
    historie = ['', '', '']       # lager en liste med plass holdere, som skal brukes til å lagre endringer på saldo

    while True:

        print('''--------------------
1 - vis saldo
2 - innskudd
3 - uttak
4 - renteoppgjør
5 - siste endringer (trykk igjen for å reversere listen)
6 - stopp program
--------------------''')

        user = int(input('Velg handling:'))
        if x == 3:
            x = 0                           # Resetter index-telleren om den når 3, slik at nye elementer overskriver gamle

        if user == 1:
            print(f'Saldo:  {saldo}')

        elif user == 2:
            påfyll = int(input('Beløp:'))
            historie[x] = f'+{påfyll}'
            x += 1                          # teller index-telleren
            innskudd(påfyll)
            print(f'Saldo: {saldo}')

        elif user == 3:
            trekk = int(input(f'Beløp:'))
            historie[x] = f'-{trekk}'
            x += 1
            uttak(trekk)
            print(f'Saldo: {saldo}')

        elif user == 4:
            renteoppgjør()
            beregnRente()
            historie[x] = f'+{beregnRente()}'
            x += 1
            
        elif user == 5:
            historie.reverse()                  # reverserer listen (i oppgave er nyest endring øverst)
            print(*historie, sep= '\n')         # skriver ut listen nyest til elst

        elif user == 6:
            break

        else:
            print('Ikke et valg')
        
    """[printer en valg skjerm]
    Utifra valg etter valg skjermen så utføres en koresponderende handlging gjennom 'if-elif-else'
    Men nå finnes det en valg 5 som er å se de 3 siste endringene 
    """

valg_c()
