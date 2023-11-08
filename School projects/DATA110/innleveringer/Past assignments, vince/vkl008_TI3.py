# Oppgave 1
# 1. Her er to boole'ske uttrykk:
# * x!=7 and y<=50
# * (x>7 or 50<y) and (x>y or y<100)
# a) hva evalueres uttrykkene til når x=9 og y= 66?
# b) Finn et ekvivalent uttrykk for det første.

# svar
# a)
#     * falce
#     * true
# b)
#     * (x--7) and y<51


# oppgave 2.
# For å bli ordfører i Tulleby må du være minst 30 år og ha bodd i byen i minst 9 år
# For å sitte i bystyret er de tilsvarende tallene 25 år og 5 år.
# Lag et program som leser inn alder og antall år man har vært bosatt i byen og så skriver ut om man kvalifiserer til ordfører og/eller bystyremedlem evt når man kan bli kvalifisert. Eksempler:
# Oppgi alder: 32
# Hvor lenge har du bodd i Tulleby? 11
# Du kan bli ordfører eller sitte i bystyret
# Oppgi alder: 29
# Hvor lenge har du bodd i Tulleby? 6
# Du kan sitte i bystyret
# Prøv igjen om 3 år for å blir ordfører
# Oppgi alder: 27
# Hvor lenge har du bodd i Tulleby? 4
# Du er ikke kvalifisert enda, prøv igjen om 1 år

alder = int(input('Din alder: '))
tid_bosat = int(input('Hvor lenge har du bodd i Tulleby? '))

if alder >= 25 and tid_bosat < 5:
    t_t_kvalifikasjon = 5 - tid_bosat
elif tid_bosat >= 5 and alder < 25:
    t_t_kvalifikasjon = 25 - alder
elif tid_bosat >= 9 and alder < 30:
    t_t_ordfører= 30 - alder
else:
    t_t_ordfører= 9 - tid_bosat

if alder >= 30 and tid_bosat >= 9:
    print('Du kvalifiserer til bystyret og ordfører')
elif alder >= 25 and tid_bosat >= 5:
    print(f'Du kvalifiserer til bystyret\
     \nprøv igjen om {t_t_ordfører} år for å bli ordfører')
else:
    print(f'Du kvalifiserer ikke enda, prøv igjen om {t_t_kvalifikasjon} år')

# oppgave 3.
# Skriv om følgende program slik at den ikke har nestede if-setninger.
# x=int(input('tall:'))
# if x>5 :
#     if x<10 :
#        print('6,7,8 eller 9')
#     if x>=10:
#        print('minst 10')
# if x<=5 :
#    print('max 5')

x = int(input('tall:'))
if 5 < x < 10:
    print('6,7,8 eller 9')
elif 5 < x >= 10:
    print('minst 10')
elif x < 5:
    print('max 5')
