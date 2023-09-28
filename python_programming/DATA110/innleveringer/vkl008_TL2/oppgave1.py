import math                 #importerer matte modulen
radius = input('Radius: ')  #tast in Radius
try:
    areal = float(radius) ** 2 * math.pi
    print(f'Arealet av en sirkel med radius {float(radius)} er {areal}')
except:
    print('Det er ikke et gylding input. Prøv igjen!')
    quit()
