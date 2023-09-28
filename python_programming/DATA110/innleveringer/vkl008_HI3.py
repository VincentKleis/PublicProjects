import random, time

def generer_bunker():
    spar    = '\u2660'
    ruter   = '\u2666'
    kløver  = '\u2663'
    hjerter = '\u2665'
    bunker = []
    for i in range(0,8):
        exec(f'{chr(i+65)} = []')                       #omvender tall fra [0,8) til bokstaver fra A til og med H
        exec(f'bunker.append({chr(i+65)})')    #skaper en liste med lister, der ver liste er knyttet til en variabel fra A til og med H

    mulige_kort = []
    mulig_valør = ['A', '7', '8', '9', '10', 'J', 'Q', 'K']

    while len(mulige_kort) != 32:
        kort = (random.choice([spar, ruter, kløver, hjerter]), random.choice(mulig_valør))
        if kort not in mulige_kort:
            mulige_kort.append(kort)    #genererer shuflet kortstokk

    while len(mulige_kort) != 0:
        for i in range (0, 8):
            exec(f'{chr(i+65)}.append(mulige_kort[0])')
            mulige_kort.pop(0)          #fordeler alle korterene på alle bunkene likt.
    
    return bunker

class bunke_manipuler():                         #en classe for å manipulere bunkene
    bunker = None

    def __init__(self, bunker):
        self.bunker = bunker

    def fin_første_kort(self):
        første_kort = []
        for bunke in self.bunker:
            if len(bunke) == 0:
                første_kort.append('')
                continue
            kort = bunke[0]
            kortfarge, valør = kort
            første_kort.append( (kortfarge, valør) )
        return første_kort

    def vis_bunker(self, første_kort, bunker):

        for_skjerm = []
        for i in første_kort:
            if i == '':
                for_skjerm.append(i)
                continue
            farge, verdi = første_kort[første_kort.index(i)]
            for_skjerm.append(f'[{farge}{verdi}]')
        
        print('  A','B','C','D','E','F','G','H','(Bunke)', sep='     ')
        print(f'{for_skjerm[0]:5s} {for_skjerm[1]:5s} {for_skjerm[2]:5s} {for_skjerm[3]:5s} {for_skjerm[4]:5s} {for_skjerm[5]:5s} {for_skjerm[6]:5s} {for_skjerm[7]:5s}   (Øverste kort)\n\
{len(bunker[0]):3} {len(bunker[1]):5} {len(bunker[2]):5} {len(bunker[3]):5} {len(bunker[4]):5} {len(bunker[5]):5} {len(bunker[6]):5} {len(bunker[7]):5}     (Antall kort)')
    antall_kort = 0

    def tell_kort(self):
        resultat = 0
        for bunke in self.bunker:
            resultat += len(bunke)
        
        self.antall_kort = resultat
        return resultat

    like_kort = []          #en liste med de to første like kortene i bunkene

    def sammenlign_kort(self, første_kort:list):
        samenlign = første_kort
        for i in første_kort:
            if i == '':
                første_kort.pop(første_kort.index(i))
                continue

        for kortfarge_a, valør_a in samenlign:
            samenlign.pop(samenlign.index((kortfarge_a, valør_a)))

            for kortfarge_b, valør_b in første_kort:
                if valør_a == valør_b:
                    like_kort = []
                    like_kort.append( chr(første_kort((kortfarge_a, valør_a))+65) )
                    like_kort.append( chr(første_kort((kortfarge_b, valør_b))+65) )
                    return True
        return False

    def fjern_kort(self, bunke_1, bunke_2):

        bunke_a, bunke_b = [self.bunker[ord(bunke_1)-65], self.bunker[ord(bunke_2)-65]]   #gjør bukstaver fra A til og med F om til tall fa 0 til 8
        farge, verdi_a = bunke_a[0]
        farge, verdi_b = bunke_b[0]

        if verdi_a[0] == verdi_b[0]:
            for bunke in self.bunker:
                if bunke == bunke_a or bunke == bunke_b:
                    bunke.pop(0)
                
                
        else:
            print('Disse to kortene har ikke samme verdi')

    def spill_wish_solitair(self):
        while self.sammenlign_kort(self.fin_første_kort()) == True and self.tell_kort() != 0:
            self.vis_bunker(self.fin_første_kort(), self.bunker)
            valgt_kort = input('Velg bunker: ')

            if valgt_kort.lower() == 'stopp':
                quit()
            
            if valgt_kort.lower() == 'auto':
                valgt_kort = f'{self.like_kort[0]}'
                time.sleep(1)


            kort = list(valgt_kort.upper())
            for i in kort:
                if ord(kort[kort.index(i)])-65 >= 8:
                    print(f'{kort[0]} og {kort[1]} er ikke bunker i dette spillet')
                    continue
            self.fjern_kort(kort[0], kort[1])
        
        if len(bunker) == 0:
            print('Gratulerer! du vant!')
        else:
            self.vis_bunker(self.fin_første_kort(), self.bunker)
            print('Så synd. prøv igjen...')
        
#test
bunker = generer_bunker()
test = bunke_manipuler(bunker).spill_wish_solitair()

