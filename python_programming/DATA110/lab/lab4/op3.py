import random

def tilf_kort():
    spar='\u2660'
    ruter='\u2666'
    kløver='\u2663'
    hjerter='\u2665'
    valg_farg = input('Velg farge (1:Spar, 2:Ruter, 3:Kløver, 4:Hjerter, (eller enter for tillfeldig)\n: ')
    mulig_farg = ['1','2','3','4']
    mulig_tall = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Knekt', 'Dronning', 'Konge']

    if valg_farg not in mulig_farg:
        valg_farg = random.randint(1,4)
    else:
        valg_farg = int(valg_farg)
    if valg_farg == 1:
        farg = spar
    elif valg_farg == 2:
        farg = ruter
    elif valg_farg == 3:
        farg = kløver
    elif valg_farg == 4:
        farg = hjerter
        
    kort = farg + random.choice(mulig_tall)
    print(f'ditt kort: [{kort}]')
    return kort
tilf_kort()