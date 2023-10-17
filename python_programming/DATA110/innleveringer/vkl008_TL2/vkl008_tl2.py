#oppgave 1
import math                 #importerer matte modulen
radius = input('Radius: ')  #tast in Radius
try:
    areal = float(radius) ** 2 * math.pi
    print(f'Arealet av en sirkel med radius {float(radius)} er {areal}')
except:
    print('Det er ikke et gylding input. Prøv igjen!')
    quit()

#oppgave 2
prompt = input('Sentence: ')    # ber om setning som den skal måle lengde på
length = len(prompt)
gues = input('Gues the length (including spaces): ')
if length == int(gues):
    print("That's correct!!")
else:
    print("That's false!")

#oppgave 3
import random #importerer random modulen
tall = input('GI MEG ET TALL!:')
random_tall = random.randint(0,100)
print(f'{random_tall}/{int(tall)} = {random_tall/int(tall)}') #deller tillfeldig tall mellom 0 og 1000 på inputt tallet, og printer resultatet
