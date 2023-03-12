'''
2.
For å bli ordfører i Tulleby må du være minst 30 år og ha bodd i byen i minst 9 år
For å sitte i bystyret er de tilsvarende tallene 25 år og 5 år.
Lag et program som leser inn alder og antall år man har vært bosatt i byen og så skriver ut om man kvalifiserer til ordfører og/eller bystyremedlem evt når man kan bli kvalifisert. Eksempler:
Oppgi alder: 32
Hvor lenge har du bodd i Tulleby? 11
Du kan bli ordfører eller sitte i bystyret
Oppgi alder: 29
Hvor lenge har du bodd i Tulleby? 6
Du kan sitte i bystyret
Prøv igjen om 3 år for å blir ordfører
Oppgi alder: 27
Hvor lenge har du bodd i Tulleby? 4
Du er ikke kvalifisert enda, prøv igjen om 1 år
'''
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