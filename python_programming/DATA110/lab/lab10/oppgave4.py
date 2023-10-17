from math import sqrt
punkt1 = input('Punt1: ')
punkt2 = input('Punt2: ')

def gjør_til_tuple(x:str ) -> tuple:
    tall_x = [int(i) for i in x if i.isdigit()]
    x = tuple(tall_x)
    return x

punkt1 = gjør_til_tuple(punkt1)
punkt2 = gjør_til_tuple(punkt2)

print(punkt1, punkt2)
def avstand(punkt1: tuple, punkt2: tuple) -> float:
    x_avstand = abs(punkt1[0] - punkt2[0])
    y_avstand = abs(punkt1[1] - punkt2[1])

    x_avstand_i_andre = x_avstand**2
    y_avstand_i_andre = y_avstand**2

    return sqrt(x_avstand_i_andre + y_avstand_i_andre)

try:
    print(f'avstand {avstand(punkt1, punkt2)}')
except:
    print('Ikke gyldig inputt')