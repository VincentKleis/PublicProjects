from itertools import permutations
from random import choice

spar    = '\u2660'
ruter   = '\u2666'
kløver  = '\u2663'
hjerter = '\u2665'

class ønske_kabal:

    def generer_kortstokk(self):
        """genererer en shuflet kortstokk

        Returns:
            [list]: kortstokk
        """
        kortstokk = []
        mulig_valør = ['A', '7', '8', '9', '10', 'J', 'Q', 'K']
        while len(kortstokk) != 32:
            kort = (choice([spar, ruter, kløver, hjerter]), choice(mulig_valør))
            if kort not in kortstokk:
                kortstokk.append(kort)
        return kortstokk


    def lag_bunker(sefl, kortstokk:list)-> list:
        """deler kortstokk opp i bunker

        Args:
            kortstokk (list):

        Returns:
            [type]: bunker
        """
        bunker = []
        for _ in range(0,8):
            bunker.append([])
        
        while len(kortstokk) != 0:
            for x in range(0,8):
                bunker[x].append(kortstokk[0])
                kortstokk.pop(0)
        
        return bunker


    def print_bunker(self, bunker:list):
        """genererer lister med ting som skal vises på skjermen, for så å printe dem til konsollen

        Args:
            bunker (list): 8 shuflede bunker
        """
        visbare_kort = []
        for i in bunker:
            if len(i) == 0:
                visbare_kort.append('')
                continue

            farge, verdi = i[0]
            visbare_kort.append(f'[{farge}{verdi}]')

        bunke_sørelse = []
        for i in bunker:
            bunke_sørelse.append(len(i))
        indexer = []
        for i in range(0,8):
            indexer.append(chr(i+65))
        
        print(f'  {indexer[0]:6}{indexer[1]:6}{indexer[2]:6}{indexer[3]:6}\
{indexer[4]:6}{indexer[5]:6}{indexer[6]:6}{indexer[7]:6}(Bunke)\
\n{visbare_kort[0]:6}{visbare_kort[1]:6}{visbare_kort[2]:6}{visbare_kort[3]:6}\
{visbare_kort[4]:6}{visbare_kort[5]:6}{visbare_kort[6]:6}{visbare_kort[7]:6}  (Øverste kort)\
\n{bunke_sørelse[0]:3}{bunke_sørelse[1]:6}{bunke_sørelse[2]:6}{bunke_sørelse[3]:6}\
{bunke_sørelse[4]:6}{bunke_sørelse[5]:6}{bunke_sørelse[6]:6}{bunke_sørelse[7]:6}     (Kort i bunke)')


    def fjern_kort(self, bunker:list, index_a:int, index_b:int)->list:
        """tar imot liste med bunker fjerne første kort i bunke på plass index_a og index_b

        Args:
            bunker (list): liste med bunker
            index_a (int): bunke a sin plasering
            index_b (int): bunke b sin plasering

        Returns:
            list: ny liste med bunker
        """
        bunke_1, bunke_2 = [bunker[index_a], bunker[index_b]]
        bunke_1.pop(0)
        bunke_2.pop(0)


    def er_lik_valør(self, bunker:list, bunke_1:int, bunke_2:int)->bool:
        """finner ut om første kort i bunke 1 og bunke 2 av bunker matcher

        Args:
            bunker (list): listen over bunker
            kort_1 (int):
            kort_2 (int):

        Returns:
            bool: True = førte kort i begge bunkene er like, False = første kort i begge bunkene er ikke like
        """
        bunke_x = bunker[bunke_1]
        bunke_y = bunker[bunke_2]
        kort_x = bunke_x[0]
        kort_y = bunke_y[0]
        farge_x, valør_x = kort_x
        farge_y, valør_y = kort_y
        if valør_x == valør_y:
            return True
        else:
            return False

    
    def fin_lik_valør(self, bunker:list) -> list:
        """tar imot liste med bunker og finner indexene på kortene med like valører

        Returns:
            [list]: liste med indexer på kort som har lik valør
        """
        øverste_kort= []

        for i in bunker:
            if len(i) == 0:
                øverste_kort.append(())
                continue

            øverste_kort.append(i[0])
        
        permutasjoner = permutations(øverste_kort, 2)
        like_valørindexer = []
        for permutasjon in permutasjoner:
            kort_x, kort_y = permutasjon
            if kort_x == () or kort_y == ():
                continue

            farge_x, valør_x = kort_x
            farge_y, valør_y = kort_y
            if valør_x == valør_y:
                like_valørindexer.append( (øverste_kort.index(kort_x), øverste_kort.index(kort_y)) )

        return like_valørindexer

    
    def ordne_størelse(self, bunker, like_valør_indexer:list)->list:
        """tar imot en liste med like kort og ordner dem etter menden kort i bunkene de kommer fra
        """
        for tupl in like_valør_indexer:
            bunke_1, bunke_2 = tupl
            tupl_ny = (len(bunker[bunke_1])+len(bunker[bunke_2]), bunke_1, bunke_2)
            like_valør_indexer[like_valør_indexer.index(tupl)] = tupl_ny

        resultat = sorted(like_valør_indexer, reverse=True)

        for tupl in resultat:
            vekt, bunke_1, bunke_2 = tupl
            tupl_ny = (bunke_1, bunke_2)
            resultat[resultat.index(tupl)] = tupl_ny
        
        return resultat


    def er_tom_bunke(self, bunker:list, bunke_1:int, bunke_2:int)->bool:
        """tar imot en liste med bunker og ser om noen av dem er tomme

        Args:
            bunker (list): liste med bunker
            bunke_1 (int): index på en bunke
            bunke_2 (int): index på en annen bunke

        Returns:
            bool:
        """
        bunke_a, bunke_b = [bunker[bunke_1], bunker[bunke_2]]

        if len(bunke_a) == 0 or len(bunke_b) == 0:
            return True
        else:
            return False


    def kabal(self, bunker:list):
        """tar imot en liste med bunker og spille ønskekabal

        Args:
            kortstokk (list): [description]
        """
        self.print_bunker(bunker)
        valgt_kortstokk = input('Velg matchende kortstokker (x for stopp): ')

        if valgt_kortstokk == 'x':
            velg = input('Spill avbrutt. velg 2 for lagre, m for meny: ')
            if velg == '2':
                with open('lagret_bunker.txt', 'w') as fhand:
                    fhand.write(str(bunker))
            velg = input()
            if velg == 'm':
                start()
            print('Ha det bra!')
            quit()

        bunke_a, bunke_b = list(valgt_kortstokk.upper())
        bunke_1, bunke_2 = [ord(bunke_a)-65, ord(bunke_b)-65]

        if self.er_tom_bunke(bunker, bunke_1, bunke_2) == False:
            if self.er_lik_valør(bunker, bunke_1, bunke_2) == True:
                self.fjern_kort (bunker, bunke_1, bunke_2)
            else:
                print('Kortene i disse bunkene er ikke like')

        else:
            print('En av Bunkene du valgte var tom')

    
    def autospill(self, bunker:list):
        """velger den første matchende bunkene fra listen av bunker

        Args:
            bunker (list): lsite av bunker
        """

        like_kort = self.fin_lik_valør(bunker)
        like_kort = self.ordne_størelse(bunker, like_kort)

        kort_1, kort_2 = like_kort[0]
        self.print_bunker(bunker)
        print('Valgte kort:',chr(kort_1+65), chr(kort_2+65))    

        self.fjern_kort(bunker, kort_1, kort_2)

    
    def antall_kort(self, bunker:list)->int:
        x = 0
        for bunke in bunker:
            x += len(bunke)

        return x



def start():
    spill = ønske_kabal()
    kortstokk = spill.generer_kortstokk()
    bunker = spill.lag_bunker(kortstokk)
    print("""\
-Spill:     0
-Auto:      1
-Lagre:     2
-Gjennopta: 3
-Stopp:     x
velg m for meny""")
    while True:
        valg = input()
        if valg == '0':
            while len(spill.fin_lik_valør(bunker)) != 0:
                spill.kabal(bunker)

            if spill.antall_kort(bunker) != 0:
                spill.print_bunker(bunker)
                print('Så synd, prøv igjen')
                break
            else:
                print('Gratulerer!')
                break

        if valg == '1':
            while len(spill.fin_lik_valør(bunker)) != 0:
                spill.autospill(bunker)
            
            if spill.antall_kort(bunker) != 0:
                spill.print_bunker(bunker)

                print('Jeg hadde ikke nok flaks .__.')
                break

            else:
                print('Gratulerer!')
                break
        
        if valg == '2':
            with open('lagret_bunker.txt', 'w') as fhand:
                fhand.write(bunker)
        
        if valg == '3':
            with open('lagret_bunker.txt', 'r') as fhand:
                bunker = fhand.read()
                bunker = eval(bunker)

        if valg == 'm':
            print("""\
-Spill:     0
-Auto:      1
-Lagre:     2
-Gjennopta: 3
-Stopp:     x
velg m for meny""")

        if valg == 'x':
            break
            


start()