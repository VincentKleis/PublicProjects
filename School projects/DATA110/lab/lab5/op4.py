'''Skriv en funksjon lesHeltall(meldinger, Min, Max)som skal lese inn et heltall
fra tastaturet, i intervallet fra Min til Max. Parameteren meldinger er en liste av
ledetekster som skal brukes i de ulike forsøkene brukeren får til å taste inn en gyldig
verdi. Dvs den første meldingen brukes innledningsvis, dersom brukeren ikke gir et
gyldig tall får han/hun et nytt forsøk med den andre meldingen osv inntil alle
meldingene er brukt. Da får ikke brukeren flere forsøk og None blir returnert.
La Min og Max være valgfrie, dvs du kan sette begge grensene, en av dem eller
ingen.
Eksempler:
>>> lesHeltall(['Gi et tall større enn 100: ']*3, Min=100)
Gi et tall større enn 100: 132
132
>>>
>>> lesHeltall(['Gi et tall større enn 100: ']*3, Min=100)  # husk at liste*n gir n kopier av liste-innholdet
Gi et tall større enn 100: 32
Gi et tall større enn 100: 99
Gi et tall større enn 100: 54                               # siste sjanse
>>>
>>> M=['Barnets alder:','Gi et tall mellom 0 og 13:','MELLOM 0 OG 13 SA JEG!', 'SISTE SJANSE:']
>>>
>>> lesHeltall(M, Min=0, Max=13)
Barnets alder: 24
Gi et tall mellom 0 og 13: 15
MELLOM 0 OG 13 SA JEG! 38
SISTE SJANSE: 40
>>>
'''

def lesHeltall(melding, Min = 0, Max = 1000):
    for i in melding:
        delmeld = int(input(i))
        if delmeld < Min or delmeld > Max:
            continue
        elif delmeld > Min and delmeld < Max:
            print(delmeld)
            break

test1 = lesHeltall(['Gi et tall større enn 100: ']*3, Min=100)
test2 = lesHeltall(['Gi et tall større enn 100: ']*3, Min=100)

M=['Barnets alder: ','Gi et tall mellom 0 og 13: ','MELLOM 0 OG 13 SA JEG! ', 'SISTE SJANSE: ']

test3 =  lesHeltall(M, Min=0, Max=13)
