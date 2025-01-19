import random


spar    = '\u2660'
ruter   = '\u2666'
kløver  = '\u2663'
hjerter = '\u2665'
class ønske_kabal:
    bunker = {'A':[], 'B':[], 'C':[], 'D':[], 'E':[], 'F':[], 'G':[], 'H':[]}
    kortstokk = []

    def generer_kortstokk(self):
        mulig_valør = ['A', '7', '8', '9', '10', 'J', 'Q', 'K']
        mulig_farge = [spar, ruter, kløver, hjerter]
        self.kortstokk = [(j, i) for i in mulig_valør for j in mulig_farge]
    
    def del_in_kort(self):
        itter = 0
        index = 0
        key = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for i in range(0, len(self.kortstokk)-1):
            kort = self.kortstokk.pop(random.randint(0, len(self.kortstokk)))
    
    def formater(self, liste):
        resultat = []
        for i in liste:
            resultat.append(f'[{i[0]}{i[1]}]')
        return resultat


test = ønske_kabal()
test.generer_kortstokk()
test.del_in_kort()
print(test.bunker, sep='\t')