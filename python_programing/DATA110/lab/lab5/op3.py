'''Lag en funksjon som beregner tverrsummen av et heltall, dvs summen av sifrene i
tallet. For eksempel er tverrsummen 452 = 4+5+2 = 11
(hint: sifferHøyre(tall) fra oppgavene til forelesning 4 om funksjoner eller
str- og int-konvertering).
'''
def tverSum(x):
    x = str(x)
    total = 0
    for i in x:
        total += int(i)
    return total

print(tverSum(452))