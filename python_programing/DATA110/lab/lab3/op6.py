print('Oppgi teller og nevner(heltall)')
try:
    teller = int(input('Teller: '))
except:
    teller = int(input('Ugyldig tall, prøv igjen: '))

try:
    nevner = int(input('Nevner: '))
except:
    nevner = int(input('Ugyldig tall, prøv igjen: '))

if teller > 100 or teller < 0:
    teller = input('Telleren må være mellom 0 og 100\n Prøv igjen: ')
if nevner > 100 or nevner < 1:
    nevner = input('Nevneren må være mellom 1 og 100\n Prøv igjen: ')

resultat = int(teller)/int(nevner)
print(teller,'/', nevner, '=', '%.2f' % resultat)
