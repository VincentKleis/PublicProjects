import random
class terning:

    def __init__(self) -> None:
        self.verdi = random.randint(1,6)
        self.id = self.verdi

class kopp:

    def trill(self) -> None:
        terning_1 = terning()
        terning_2 = terning()
        self.id = terning_1.id * terning_2.id
        self.sum = terning_1.verdi + terning_2.verdi

class spiller:

    def __init__(self, navn) -> None:
        self.navn = navn
        self.verdi = 0

    def spill(self, kopp) -> int:
        kopp.trill()
        self.verdi = kopp.sum
        self.id = kopp.id

class terningspill:
    spillere = []

    def leggTilSpiller(self, navn):
        self.spillere.append(spiller(navn))

i = 20
while i >= 0:
    test = terningspill()
    test.leggTilSpiller('vincent')
    test.spillere[0].spill(kopp())
    print(test.spillere[0].verdi)
    i -= 1