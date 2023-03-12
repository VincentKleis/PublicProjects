# a) best av 3
import random
def stein_saks_papir():
    n = int(input('Hvor mange runder? '))
    x = 1
    while x < n:
        spiller_valg = input(f'Runde {x} - Velg (1=papir,2=saks eller 3=stein): ')
        maskin_valg = random.randint(1,3)
        maskin_vinner = spiller_valg == 1 and maskin_valg == 2 or spiller_valg == 2 and maskin_valg == 3 or spiller_valg == 3 and maskin_valg == 1
        spiller_vinner = spiller_valg == 1 and maskin_valg == 3 or spiller_valg == 2 and maskin_valg == 1 or spiller_valg == 3 and maskin_valg == 2

        if maskin_vinner == True:
            print('Du tapte')
        elif spiller_vinner == True:
            print('Du vant')
        else:
            print('Det ble uavgjort')
        x += 1

stein_saks_papir()